"""P1 paragraph rule (v9): no prose paragraph over ~5 sentences unless
deliberate. Reports offenders; does not fail the build (exceptions are
allowed as stylistic choices, so this is an eval surface, not a gate).

Usage: clae-py tools/render/paracheck.py <file.md> [limit]
"""
import re
import sys

src = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
text = open(src).read()
text = re.sub(r'\A<!--.*?-->', '', text, flags=re.S)

in_code = False
paras, buf, start = [], [], 1
for i, line in enumerate(text.split('\n'), 1):
    if line.startswith('```'):
        in_code = not in_code
        continue
    if in_code or line.startswith(('#', '\\', '!', '  ', '- ', '1.')) or re.match(r'^\d+\. ', line):
        continue
    if line.strip() in ('', '&nbsp;'):
        if buf:
            paras.append((start, ' '.join(buf)))
            buf = []
        continue
    if not buf:
        start = i
    buf.append(line.strip())
if buf:
    paras.append((start, ' '.join(buf)))

count = 0
for ln, p in paras:
    # strip footnote defs' leading markers and inline math to avoid false periods
    clean = re.sub(r'\$[^$]*\$', 'X', p)
    clean = re.sub(r'\b(e\.g|i\.e|vs|Dr|Mr|Ms|cf|ch|Ch|no|No|etc)\.', r'\1', clean)
    sentences = re.findall(r'[.!?](?:\s|$)', clean)
    n = len(sentences)
    if n > limit:
        count += 1
        print(f'{src}:{ln}: {n} sentences :: {p[:90]}...')
print(f'{src}: {count} paragraphs over {limit} sentences ({len(paras)} total)')
