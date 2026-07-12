"""Pandoc LaTeX fragment -> SNmono environments.

Usage: clae-py tools/render/postprocess.py <frag.tex> <figmap.json> <figdir> [--section-zero]
"""
import json
import re
import sys

tex_path, figmap_path, figdir = sys.argv[1:4]
section_zero = '--section-zero' in sys.argv
tex = open(tex_path).read()
figs = json.load(open(figmap_path))

# theorem-style boxes
tex = re.sub(r'ZZBEGINZZ(definition|claim)ZZ\s*(.*?)\s*ZZENDTITLEZZ',
             lambda m: '\\begin{%s}[%s]' % (m.group(1), m.group(2)),
             tex, flags=re.S)
tex = re.sub(r'ZZCLOSEZZ(definition|claim)ZZ', r'\\end{\1}', tex)

# figures
def fig(m):
    idx = int(m.group(1))
    cap = m.group(2).strip()
    path = f'{figdir}/{figs[idx].split("/")[-1]}'
    return ('\\begin{figure}[!htb]\\centering\n'
            '\\includegraphics[width=0.82\\textwidth]{%s}\n'
            '\\caption{%s}\n\\end{figure}' % (path, cap))

tex = re.sub(r'ZZFIGZZ(\d+)ZZCAPZZ\s*(.*?)\s*ZZENDFIGZZ', fig, tex, flags=re.S)

# gray boxes and qed
tex = tex.replace('ZZGRAYZZ', '\\begin{svgraybox}')
tex = tex.replace('ZZENDGRAYZZ', '\\end{svgraybox}')
tex = tex.replace('ZZQEDZZ', '$\\blacksquare$')

if section_zero:
    tex = re.sub(r'(\\chapter\{[^}]*\}.*?\n)', r'\1\\setcounter{section}{-1}\n',
                 tex, count=1)

open(tex_path, 'w').write(tex)
print(f'{tex_path}: post-processed ({len(figs)} figures)')
