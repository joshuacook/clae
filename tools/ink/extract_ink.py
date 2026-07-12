"""CLAE ink-extraction tool: inked-PDF -> grounded census + contact sheet.

Runs inside Cloud Build (network + pip available there; cc-host runs nothing).

Pipeline:
  1. PyMuPDF: enumerate annotations, capture FreeText contents verbatim.
  2. Render each page with/without annotations; diff -> ink-only layer.
  3. Split the ink by color: yellow highlight / blue highlight / handwriting.
  4. Highlights: map regions to PDF coords, read the printed text underneath
     deterministically (no AI). yellow = "ai speak" (poorly written);
     blue = well written.
  5. Handwriting clusters: Gemini (Vertex, structured output) transcribes
     verbatim and selects the printed anchor text. Low confidence or
     unreadable -> the ask-Josh list. No guessing.
  6. Emit census.md (ordered, grounded), census.json, contact_sheet.html
     (hard gate: Josh reviews before the census is filed).

Usage:
  python extract_ink.py --pdf inked.pdf --out outdir \
      --project cooksfleet-apps --location global --model gemini-3.1-pro
"""
import argparse
import base64
import io
import json
import os

import fitz  # PyMuPDF
import numpy as np
from PIL import Image
from scipy import ndimage

DPI = 250
SCALE = DPI / 72.0
MIN_AREA = 400          # px; ignore specks
DILATE = 21             # px; merge nearby strokes into one mark
CONF_GATE = 0.8

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "transcription": {
            "type": "STRING",
            "description": "The handwriting, verbatim, exactly as written. "
                           "Empty string if there are no written words.",
        },
        "anchor_text": {
            "type": "STRING",
            "description": "The exact printed text this mark grounds to: "
                           "the sentence, phrase, or quote it targets, "
                           "copied verbatim from the provided page text.",
        },
        "anchor_kind": {
            "type": "STRING",
            "enum": ["sentence", "paragraph", "phrase", "heading", "code",
                     "equation", "figure", "page-global"],
        },
        "mark_type": {
            "type": "STRING",
            "enum": ["marginal-note", "inline-note", "circle", "underline",
                     "strikethrough", "arrow", "bracket", "other"],
        },
        "confidence": {"type": "NUMBER"},
        "unreadable": {"type": "BOOLEAN"},
    },
    "required": ["transcription", "anchor_text", "anchor_kind",
                 "mark_type", "confidence", "unreadable"],
}

PROMPT = """You are transcribing an author's handwritten ink on a page of his
own book draft. The first image shows the page region WITH the ink; the second
shows the same region clean. Below is the printed text of the region and of
the full page.

Transcribe any handwriting EXACTLY as written: verbatim, keeping his
abbreviations, punctuation, and casing; do not complete or correct words.
Identify the printed text the mark is grounded to (the sentence, phrase, or
quote it points at, underlines, circles, or sits beside) and copy that anchor
verbatim from the printed text provided. Classify the mark. If any written
word is not clearly legible, set unreadable=true and transcribe only what is
certain, marking uncertain words with [?].

Region text:
{region_text}

Full page text:
{page_text}
"""


def png_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()


def render(page, annots: bool) -> Image.Image:
    pm = page.get_pixmap(dpi=DPI, annots=annots)
    return Image.frombytes('RGB', (pm.width, pm.height), pm.samples)


def classify_color(rgb_pixels: np.ndarray) -> str:
    """rgb_pixels: (N, 3) of the mark's own pixels (from the annotated render)."""
    r, g, b = rgb_pixels.mean(axis=0)
    if r > 150 and g > 120 and b < 140 and (r + g) / 2 - b > 40:
        return 'yellow'
    if b > 130 and b - r > 30:
        return 'blue'
    return 'ink'


def extract(pdf_path: str, out: str, project: str, location: str, model: str):
    os.makedirs(out, exist_ok=True)
    os.makedirs(f'{out}/crops', exist_ok=True)
    doc = fitz.open(pdf_path)
    records = []

    from google import genai
    from google.genai import types
    client = genai.Client(vertexai=True, project=project, location=location)

    for pno, page in enumerate(doc, start=1):
        page_text = page.get_text()
        # freetext annotations: verbatim, no AI needed
        for annot in page.annots() or []:
            if annot.type[1] == 'FreeText' and annot.info.get('content'):
                records.append({
                    'page': pno, 'kind': 'freetext', 'color': 'typed',
                    'transcription': annot.info['content'],
                    'anchor_text': '(page-level typed note)',
                    'anchor_kind': 'page-global', 'mark_type': 'marginal-note',
                    'confidence': 1.0, 'unreadable': False, 'y': 0, 'crop': None,
                })

        with_ink = render(page, True)
        clean = render(page, False)
        a = np.asarray(with_ink).astype(int)
        c = np.asarray(clean).astype(int)
        mask = (np.abs(a - c).sum(axis=2) > 45)
        if not mask.any():
            continue

        merged = ndimage.binary_dilation(mask, np.ones((DILATE, DILATE)))
        labels, n = ndimage.label(merged)
        for i in range(1, n + 1):
            region = (labels == i) & mask
            if region.sum() < MIN_AREA:
                continue
            ys, xs = np.where(region)
            y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
            color = classify_color(a[region])
            pad = 30
            box = (max(0, x0 - pad), max(0, y0 - pad),
                   min(a.shape[1], x1 + pad), min(a.shape[0], y1 + pad))
            rect = fitz.Rect(box[0] / SCALE, box[1] / SCALE,
                             box[2] / SCALE, box[3] / SCALE)
            region_text = page.get_text(clip=rect).strip()
            crop_ink = with_ink.crop(box)
            crop_name = f'p{pno}_m{i}_{color}.png'
            crop_ink.save(f'{out}/crops/{crop_name}')

            if color in ('yellow', 'blue'):
                # deterministic: the highlighted printed text IS the payload
                hl_rect = fitz.Rect(x0 / SCALE, y0 / SCALE,
                                    x1 / SCALE, y1 / SCALE)
                hl_text = ' '.join(page.get_text(clip=hl_rect).split())
                records.append({
                    'page': pno, 'kind': 'highlight', 'color': color,
                    'transcription': '',
                    'anchor_text': hl_text,
                    'anchor_kind': 'phrase', 'mark_type': 'highlight',
                    'confidence': 1.0, 'unreadable': not bool(hl_text),
                    'y': int(y0), 'crop': crop_name,
                    'meaning': ('ai speak (poorly written)' if color == 'yellow'
                                else 'well written'),
                })
                continue

            # handwriting -> Gemini, structured output
            crop_clean = clean.crop(box)
            prompt = PROMPT.format(region_text=region_text or '(none)',
                                   page_text=page_text[:6000])
            resp = client.models.generate_content(
                model=model,
                contents=[
                    types.Part.from_bytes(data=png_bytes(crop_ink),
                                          mime_type='image/png'),
                    types.Part.from_bytes(data=png_bytes(crop_clean),
                                          mime_type='image/png'),
                    prompt,
                ],
                config=types.GenerateContentConfig(
                    response_mime_type='application/json',
                    response_schema=SCHEMA,
                ),
            )
            r = json.loads(resp.text)
            r.update({'page': pno, 'kind': 'handwriting', 'color': color,
                      'y': int(y0), 'crop': crop_name})
            records.append(r)

    records.sort(key=lambda r: (r['page'], r['y']))
    json.dump(records, open(f'{out}/census.json', 'w'), indent=1)

    # census.md
    lines = ['# Ink census (machine transcription, pending hard-gate review)',
             '']
    ask = []
    for i, r in enumerate(records, 1):
        gate = (r['kind'] == 'handwriting'
                and (r['unreadable'] or r['confidence'] < CONF_GATE))
        if gate:
            ask.append((i, r))
        head = f'**{i}. p.{r["page"]} {r["kind"]}'
        if r['kind'] == 'highlight':
            head += f' [{r["color"].upper()} = {r["meaning"]}]'
        head += '**' + (' ⚠ LOW CONFIDENCE' if gate else '')
        lines += [head, '']
        if r['transcription']:
            lines += [f'> {r["transcription"]}', '']
        lines += [f'*Grounded to ({r["anchor_kind"]}):* "{r["anchor_text"]}"',
                  f'*Mark:* {r["mark_type"]} · *confidence* '
                  f'{r["confidence"]:.2f}', '']
    if ask:
        lines += ['## Ask Josh (low confidence / unreadable)', '']
        lines += [f'- item {i}: p.{r["page"]}, crop `{r["crop"]}`'
                  for i, r in ask]
    open(f'{out}/census.md', 'w').write('\n'.join(lines))

    # contact sheet (hard gate artifact)
    rows = []
    for i, r in enumerate(records, 1):
        img = ''
        if r.get('crop'):
            b64 = base64.b64encode(
                open(f'{out}/crops/{r["crop"]}', 'rb').read()).decode()
            img = f'<img src="data:image/png;base64,{b64}" style="max-width:520px">'
        rows.append(
            f'<tr><td>{i}</td><td>p.{r["page"]}<br>{r["kind"]}<br>'
            f'{r["color"]}</td><td>{img}</td>'
            f'<td><b>{r["transcription"] or "(highlight)"}</b><br>'
            f'<i>anchor:</i> {r["anchor_text"]}<br>'
            f'conf {r["confidence"]:.2f}'
            f'{" · UNREADABLE" if r["unreadable"] else ""}</td></tr>')
    open(f'{out}/contact_sheet.html', 'w').write(
        '<html><body><h1>Ink contact sheet — verify before filing</h1>'
        '<table border=1 cellpadding=6 style="border-collapse:collapse">'
        '<tr><th>#</th><th>where</th><th>mark</th><th>read</th></tr>'
        + ''.join(rows) + '</table></body></html>')
    print(f'{len(records)} marks; {len(ask)} for the ask-Josh list')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--pdf', required=True)
    p.add_argument('--out', default='inkout')
    p.add_argument('--project', default='cooksfleet-apps')
    p.add_argument('--location', default='global')
    p.add_argument('--model', default='gemini-3.1-pro')
    a = p.parse_args()
    extract(a.pdf, a.out, a.project, a.location, a.model)
