"""CLAE ink-extraction: inked PDF -> grounded census + contact sheet.

Page-level design: ONE Gemini call per page returns an ARRAY of handwriting
marks (transcription + printed anchor + type + confidence). Highlights
(yellow = ai speak / blue = well written) are extracted deterministically
from the ink color mask; FreeText annotations verbatim via PyMuPDF.
Runs in Cloud Build. Hard gate: contact_sheet.html reviewed before filing.
"""
import argparse
import base64
import io
import json
import os

import fitz
import numpy as np
from PIL import Image
from scipy import ndimage

DPI = 250
SCALE = DPI / 72.0
MIN_HL_AREA = 800
PAGE_MAX_W = 1700

MARKS_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "marks": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "transcription": {"type": "STRING"},
                    "anchor_text": {"type": "STRING"},
                    "anchor_kind": {"type": "STRING",
                                    "enum": ["sentence", "paragraph", "phrase",
                                             "heading", "code", "equation",
                                             "figure", "page-global"]},
                    "mark_type": {"type": "STRING",
                                  "enum": ["marginal-note", "inline-note",
                                           "circle", "underline",
                                           "strikethrough", "arrow",
                                           "bracket", "caret-insert",
                                           "other"]},
                    "location": {"type": "STRING",
                                 "description": "where on the page, briefly"},
                    "bbox": {"type": "ARRAY", "items": {"type": "INTEGER"},
                             "description": "[ymin, xmin, ymax, xmax] of the "
                                            "handwritten mark in the FIRST "
                                            "image, normalized 0-1000"},
                    "confidence": {"type": "NUMBER"},
                    "unreadable": {"type": "BOOLEAN"},
                },
                "required": ["transcription", "anchor_text", "anchor_kind",
                             "mark_type", "location", "confidence",
                             "unreadable", "bbox"],
            },
        }
    },
    "required": ["marks"],
}

PROMPT = """You are transcribing an author's handwritten ink marks on a page
of his own book draft. The FIRST image is the page WITH his ink; the SECOND is
the same page clean (printed text only). The full printed text follows below.

Enumerate EVERY handwritten mark on the page, top to bottom. For each mark:
- transcription: the handwriting EXACTLY as written, verbatim; keep his
  abbreviations, casing, punctuation; never complete or correct his words.
  Mark any illegible word as [?] and set unreadable=true. Empty string for
  wordless marks (bare circles, arrows, strikethroughs, carets, paragraph
  symbols).
- anchor_text: the printed text the mark grounds to (the sentence, phrase, or
  quote it points at, circles, strikes, or sits beside), copied VERBATIM from
  the printed text below. Every mark grounds somewhere; use anchor_kind
  "page-global" only for notes about the whole page.
- mark_type, a brief location, your confidence (0-1).

Do not skip small marks. Do not merge distinct notes. Do not include yellow
or blue highlighting (handled separately); DO include handwriting layered on
top of highlights.

Full printed page text:
{page_text}
"""


def png_b64(img):
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()


def shrink(img):
    if img.width > PAGE_MAX_W:
        h = int(img.height * PAGE_MAX_W / img.width)
        return img.resize((PAGE_MAX_W, h))
    return img


def classify_color(rgb):
    r, g, b = rgb.mean(axis=0)
    if r > 150 and g > 120 and b < 140 and (r + g) / 2 - b > 40:
        return 'yellow'
    if b > 130 and b - r > 30:
        return 'blue'
    return 'ink'


def extract(pdf_path, out, project, location, model, name=None):
    os.makedirs(out, exist_ok=True)
    os.makedirs(f'{out}/pages', exist_ok=True)
    doc = fitz.open(pdf_path)
    records = []

    from google import genai
    from google.genai import types
    client = genai.Client(vertexai=True, project=project, location=location)

    for pno, page in enumerate(doc, start=1):
        page_text = page.get_text()
        for annot in page.annots() or []:
            if annot.type[1] == 'FreeText' and annot.info.get('content'):
                records.append({
                    'page': pno, 'kind': 'freetext', 'color': 'typed',
                    'transcription': annot.info['content'],
                    'anchor_text': '(page-level typed note)',
                    'anchor_kind': 'page-global',
                    'mark_type': 'marginal-note', 'location': 'typed note',
                    'confidence': 1.0, 'unreadable': False, 'order': 0,
                    'band': (0, 1),
                })

        pm_ink = page.get_pixmap(dpi=DPI, annots=True)
        pm_cln = page.get_pixmap(dpi=DPI, annots=False)
        with_ink = Image.frombytes('RGB', (pm_ink.width, pm_ink.height),
                                   pm_ink.samples)
        clean = Image.frombytes('RGB', (pm_cln.width, pm_cln.height),
                                pm_cln.samples)
        with_ink.save(f'{out}/pages/p{pno}.png')
        a = np.asarray(with_ink).astype(int)
        c = np.asarray(clean).astype(int)
        mask = (np.abs(a - c).sum(axis=2) > 45)
        if not mask.any():
            continue

        # highlights: deterministic, color-masked regions -> printed words
        for color in ('yellow', 'blue'):
            if color == 'yellow':
                cm = mask & (a[..., 0] > 150) & (a[..., 1] > 120) \
                     & (a[..., 2] < 140) \
                     & ((a[..., 0] + a[..., 1]) / 2 - a[..., 2] > 40)
            else:
                cm = mask & (a[..., 2] > 130) & (a[..., 2] - a[..., 0] > 30)
            merged = ndimage.binary_dilation(cm, np.ones((9, 25)))
            labels, n = ndimage.label(merged)
            words = page.get_text('words')
            for i in range(1, n + 1):
                region = (labels == i) & cm
                if region.sum() < MIN_HL_AREA:
                    continue
                ys, xs = np.where(region)
                hy0, hy1 = ys.min() / SCALE, ys.max() / SCALE
                hx0, hx1 = xs.min() / SCALE, xs.max() / SCALE
                sel = [w[4] for w in words
                       if hx0 - 2 < (w[0] + w[2]) / 2 < hx1 + 2
                       and hy0 - 2 < (w[1] + w[3]) / 2 < hy1 + 2]
                text = ' '.join(sel)
                records.append({
                    'page': pno, 'kind': 'highlight', 'color': color,
                    'transcription': '',
                    'anchor_text': text, 'anchor_kind': 'phrase',
                    'mark_type': 'highlight',
                    'location': f'y~{int(hy0)}pt',
                    'confidence': 1.0, 'unreadable': not bool(text),
                    'order': int(ys.min()),
                    'band': (int(ys.min()), int(ys.max())),
                    'meaning': ('ai speak (poorly written)'
                                if color == 'yellow' else 'well written'),
                })

        # handwriting: one page-level Gemini call, array out
        resp = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(data=png_b64(shrink(with_ink)),
                                      mime_type='image/png'),
                types.Part.from_bytes(data=png_b64(shrink(clean)),
                                      mime_type='image/png'),
                PROMPT.format(page_text=page_text[:9000]),
            ],
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
                response_schema=MARKS_SCHEMA,
            ),
        )
        for j, m in enumerate(json.loads(resp.text)['marks']):
            bb = m.get('bbox') or [0, 0, 1000, 1000]
            y0 = int(bb[0] / 1000 * with_ink.height)
            y1 = int(bb[2] / 1000 * with_ink.height)
            m.update({'page': pno, 'kind': 'handwriting', 'color': 'ink',
                      'order': 10000 + j, 'band': (y0, y1)})
            records.append(m)

    records.sort(key=lambda r: (r['page'], r['order']))
    json.dump(records, open(f'{out}/census.json', 'w'), indent=1)

    lines = ['# Ink census (machine transcription, pending hard-gate review)',
             '']
    ask = []
    for i, r in enumerate(records, 1):
        gate = r['kind'] == 'handwriting' and (
            r['unreadable'] or r['confidence'] < 0.8)
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
                  f'*Mark:* {r["mark_type"]} ({r.get("location", "")}) · '
                  f'*confidence* {r["confidence"]:.2f}', '']
    if ask:
        lines += ['## Ask Josh (low confidence / unreadable)', '']
        lines += [f'- item {i}: p.{r["page"]}, {r.get("location", "?")}'
                  for i, r in ask]
    open(f'{out}/census.md', 'w').write('\n'.join(lines))

    # contact sheet: per page, the inked page image + that page's items
    parts = ['<html><body><h1>Ink contact sheet — verify before filing</h1>']
    for pno in range(1, len(doc) + 1):
        items = [(i, r) for i, r in enumerate(records, 1)
                 if r['page'] == pno]
        if not items:
            continue
        b64 = base64.b64encode(
            open(f'{out}/pages/p{pno}.png', 'rb').read()).decode()
        rows = ''.join(
            f'<tr><td>{i}</td><td>{r["kind"]}<br>{r["color"]}</td>'
            f'<td><b>{r["transcription"] or "(no words)"}</b><br>'
            f'<i>anchor:</i> {r["anchor_text"]}<br>'
            f'{r["mark_type"]} · {r.get("location", "")} · '
            f'conf {r["confidence"]:.2f}</td></tr>'
            for i, r in items)
        parts.append(
            f'<h2>Page {pno}</h2>'
            f'<div style="display:flex;gap:16px;align-items:flex-start">'
            f'<img src="data:image/png;base64,{b64}" style="width:46%">'
            f'<table border=1 cellpadding=6 '
            f'style="border-collapse:collapse;width:52%">{rows}</table>'
            f'</div>')
    parts.append('</body></html>')
    open(f'{out}/contact_sheet.html', 'w').write(''.join(parts))
    # card crops: full-width bands with generous context
    os.makedirs(f'{out}/cards', exist_ok=True)
    pages_px = {}
    for pno in range(1, len(doc) + 1):
        path = f'{out}/pages/p{pno}.png'
        if os.path.exists(path):
            pages_px[pno] = Image.open(path)
    for i, r in enumerate(records, 1):
        img = pages_px.get(r['page'])
        if img is None:
            r['card'] = None
            continue
        y0, y1 = r.get('band', (0, img.height))
        pad = 170
        top = max(0, y0 - pad)
        bot = min(img.height, y1 + pad)
        band = img.crop((0, top, img.width, bot))
        if band.width > 1300:
            band = band.resize((1300, int(band.height * 1300 / band.width)))
        name = f'card_{i}.jpg'
        band.convert('RGB').save(f'{out}/cards/{name}', quality=80)
        r['card'] = name
    review_records = []
    for i, r in enumerate(records, 1):
        d = {k: r.get(k) for k in
             ('page', 'kind', 'color', 'transcription', 'anchor_text',
              'anchor_kind', 'mark_type', 'location', 'confidence',
              'unreadable', 'meaning')}
        d['n'] = i
        d['img'] = (base64.b64encode(
            open(f'{out}/cards/{r["card"]}', 'rb').read()).decode()
            if r.get('card') else '')
        review_records.append(d)
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'review_template.html')).read()
    open(f'{out}/review.html', 'w').write(
        tpl.replace('/*DATA*/', json.dumps(review_records))
           .replace('/*NAME*/', name or os.path.basename(pdf_path).rsplit('.', 1)[0]))
    print(f'{len(records)} marks; {len(ask)} on the ask-Josh list; review app written')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--pdf', required=True)
    p.add_argument('--out', default='inkout')
    p.add_argument('--project', default='cooksfleet-apps')
    p.add_argument('--location', default='global')
    p.add_argument('--model', default='gemini-3.1-pro-preview')
    p.add_argument('--name', default=None)
    a = p.parse_args()
    extract(a.pdf, a.out, a.project, a.location, a.model, a.name)
