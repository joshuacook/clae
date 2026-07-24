# CLAE — Computational Linear Algebra for Estimation

Springer book. Prose motion (no Claude Code prompts). Draft PDF to the editor by **Aug 1, 2026**.

## Production model (revised 2026-07-11)

**Claude drafts, Josh edits.** `manuscript/` is the book: one file per
document (preface.md, ch01..ch05.md), figures flat in manuscript/figures/.
**Versioning is git**: commits for history, a tag per delivered draft book
(v12, v13, ...). Never version via filenames, directories, or header
comments; never keep parallel copies of the manuscript. Claude writes it from the
feeders (chapter_notes conversation files + source maps, the outline, the
source index); Josh edits in scribe (block edits + `>>` comments) or via the
claude.ai channel, and his edits are the highest-authority voice signal. Study
his diffs and fold what they teach into `agreements/ai-tells.md`.

Voice anchors: §1.0 of Ch 1 as Josh edited it, his verbatim quotes in
`chapter_notes/clae-*-conversation.md`, and *Docker for Data Science*.
`agreements/ai-tells.md` is the mandatory blocklist (no em-dashes, no
"not X, but Y", full list there) and the positive voice spec.

Audience: readers who took linear algebra and either never got excited or lost
the excitement. Re-enchantment, not review. Book policy: assume Gaussian
elimination (use it, don't teach it).

## Before drafting

Read `agreements/ai-tells.md` first, every drafting pass. Then
`agreements/writing-process.md` (artifact classes, lens process, production
flow — see its CLAE modifications) and
`agreements/section-drafting-playbook.md` (9 section types, lens sets).
Then the style agreements: `markdown-style.md`, `paragraph-sizing.md`,
`vocabulary-capitalization.md`, `emdash-purge.md`.

Each chapter begins with a **Source Assembly** pass (gather source, map to outline
sections, build the chapter outline from it) per the CLAE modification in
`writing-process.md`. The source index is `source/coverage-by-chapter.md`.

## Chapter list (15 chapters, 4 parts — Solving inserted 2026-07-16; Springer proposal says 14, flag for Elizabeth)

**I — Linear Algebra Foundations**

1. Vectors and Linear Combinations
2. Matrices and Linear Transformations
3. Solving Linear Systems *(new 2026-07-16: the license as a method, LU, the door to estimation)*
4. Eigenvalues, Eigenvectors, and Diagonalization

**II — Random Vectors and Statistical Structure**

5. Random Vectors and Probability Spaces
6. Expectation and Conditional Probability
7. Covariance, Correlation, and Cross-Correlation
8. Gaussian Random Vectors
9. Convergence — Law of Large Numbers and the Central Limit Theorem

**III — Linear Estimation**

10. Singular Value Decomposition
11. Principal Component Analysis (capstone)
12. Least Squares Estimation
13. Linear MMSE Estimation (capstone)

**IV — Applications**

14. Estimation in Signal Processing
15. Advanced Filtering and Modern Applications

Ruled objectives for the linear-algebra piece (Preface + Ch 1–4):
`chapter_notes/clae-objectives-ruled-2026-07-16.md`. System map + promise
ledger: `chapter_notes/clae-system-map.md`. Old chapter numbers appear in
pre-2026-07-16 notes; the promise ledger carries the renumbered targets.

## Source coverage

Tags are optimistic: book-wide source assembly (2026-06-25) found every "strong"
chapter is adapt-the-mechanics, write-the-payload. Rough: adapt Ch 1–4, 6, 9, 10;
partial Ch 7, 11; write from scratch Ch 5, 8, 12, 13, 14. The ILA repo is mostly
empty stubs (only ch01–03 real); course math lessons use iris not Ames. Real
per-chapter coverage and mismatches: `source/coverage-by-chapter.md` and the
per-chapter maps `chapter_notes/clae-chapter-NN-source-map.md`.

## PII

Never copy student submissions from `~/working/teaching/courses/linalg/assessments/`
into this repo.

## PDF rendering

Output to `/tmp`, never the repo. xelatex via pandoc; `rsvg-convert` SVG→PDF first.

## Running Python — use `clae-py`, always

You have the full NumFOCUS stack (numpy, scipy, pandas, matplotlib, sympy,
scikit-learn, jupyter, nbconvert, seaborn) for figures and numerical examples.
**Run it only through `clae-py`** — e.g. `clae-py script.py`, `clae-py -c "..."`,
`clae-py -m nbconvert --to notebook --execute fig.ipynb`. Bare `python`/`python3`
and the venv interpreter are denied on purpose.

`clae-py` is a bubblewrap sandbox (a blessed exception to this box's no-local-execute
rule, for pure-math compute only). Inside it:

- **No network** — purely offline. Don't write code here that fetches anything.
- **Only the book repos are writable** — `~/working/clae` (manuscript) and
  `~/working/clae-code` (public notebooks). `HOME` is a throwaway `/tmp`; nothing
  else is visible. `clae-py` runs from your current dir when it's inside either repo,
  so notebook-relative paths resolve naturally.
- **The stack is read-only and cannot be extended from here.** To add a package,
  ask Josh — he runs `uv add <pkg>` in `~/.local/share/clae-sci` manually. You
  cannot `pip install` / `uv add` (denied, no pip, read-only site-packages, no net).
