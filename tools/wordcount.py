"""Stamp word counts into each chapter draft's header metadata.

Run: clae-py tools/wordcount.py
Counts total words and prose words (excluding code fences, display math,
HTML comments, and footnote-citation lines are kept). Idempotent: replaces
an existing 'Words:' line in the header comment, or inserts one.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = sorted(ROOT.glob('chapter_drafts/*/*.md'))


def counts(text: str):
    total = len(text.split())
    prose = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    prose = re.sub(r'```.*?```', '', prose, flags=re.S)
    prose = re.sub(r'\$\$.*?\$\$', '', prose, flags=re.S)
    prose = re.sub(r'^#+ .*$', '', prose, flags=re.M)      # headings
    prose = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', prose)     # image refs
    return total, len(prose.split())


def stamp(path: Path):
    text = path.read_text()
    total, prose = counts(text)
    line = f'Words: {prose} prose / {total} total (auto: tools/wordcount.py)'
    if text.startswith('<!--'):
        end = text.index('-->')
        head = text[:end]
        if 'Words:' in head:
            head = re.sub(r'Words:.*?(?=\n|$)', line, head)
        else:
            head = head.rstrip() + f'\n     {line} '
        text = head + text[end:]
    else:
        text = f'<!-- {line} -->\n\n' + text
    path.write_text(text)
    print(f'{path.relative_to(ROOT)}: {prose} prose / {total} total')


for p in DRAFTS:
    stamp(p)
