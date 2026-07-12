"""Markdown -> pandoc-safe markdown with placeholder markers for Springer envs.

Usage: clae-py tools/render/preprocess.py <in.md> <out.md> <figmap.json> <mode>
mode: preface | chapter
Markers (replaced by postprocess.py after pandoc):
  ZZBEGINZZ<env>ZZ <title> ZZENDTITLEZZ ... ZZCLOSEZZ<env>ZZ
  ZZFIGZZ<idx>ZZCAPZZ <caption md> ZZENDFIGZZ
  ZZGRAYZZ ... ZZENDGRAYZZ         ZZQEDZZ
"""
import json
import re
import sys

src, dst, figmap_path, mode = sys.argv[1:5]
text = open(src).read()

# strip the draft header comment
text = re.sub(r'\A<!--.*?-->\s*', '', text, flags=re.S)

# qed
text = text.replace('∎', 'ZZQEDZZ')

# definition / proposition blockquote boxes -> markers
def box(m):
    kind = m.group(1).lower()
    return (f'ZZBEGINZZ{kind}ZZ {m.group(2)} ZZENDTITLEZZ\n\n'
            f'{m.group(3)}\n\nZZCLOSEZZ{kind}ZZ')

text = re.sub(r'^> \*\*(Definition|Claim) \d+\.\d+ \(([^)]+)\)\.\*\* (.+)$',
              box, text, flags=re.M)

# figure image + caption blockquote -> marker paragraph; path kept out of pandoc
figs = []
def fig(m):
    figs.append(m.group(1))
    return (f'ZZFIGZZ{len(figs)-1}ZZCAPZZ {m.group(2)} ZZENDFIGZZ')

text = re.sub(
    r'^!\[[^\]]*\]\((figures/[^)]+)\)\n\n> \*\*Figure \d+\.\d+\.?\*\*[ ]?(.+)$',
    fig, text, flags=re.M)

# honesty box paragraph -> gray box
text = re.sub(r'^\*\*Honesty box\.\*\* (.+)$',
              r'ZZGRAYZZ\n\n**Honesty box.** \1\n\nZZENDGRAYZZ',
              text, flags=re.M)

if mode == 'preface':
    text = re.sub(r'^# Preface\s*$', '', text, flags=re.M)
else:
    # "# Chapter N: Title" -> "# Title"; "## 1.2 Foo" -> "## Foo"
    text = re.sub(r'^# Chapter \d+: (.+)$', r'# \1', text, flags=re.M)
    text = re.sub(r'^## \d+(?:\.\d+)? (.+)$', r'## \1', text, flags=re.M)

open(dst, 'w').write(text)
json.dump(figs, open(figmap_path, 'w'))
print(f'{dst}: {len(figs)} figures')
