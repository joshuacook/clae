# CLAE — Computational Linear Algebra for Estimation

Springer book. Prose motion (no Claude Code prompts). Draft PDF to the editor by **Aug 1, 2026**.

## Before drafting

Read `agreements/writing-process.md` (artifact classes, lens process, production
flow) and `agreements/section-drafting-playbook.md` (9 section types, lens sets).
Then the style agreements: `markdown-style.md`, `paragraph-sizing.md`,
`vocabulary-capitalization.md`, `emdash-purge.md`.

Each chapter begins with a **Source Assembly** pass (gather source, map to outline
sections, build the chapter outline from it) per the CLAE modification in
`writing-process.md`. The source index is `source/coverage-by-chapter.md`.

## Chapter list (14 chapters, 4 parts)

**I — Linear Algebra Foundations**

1. Vector Spaces and Data Representation
2. Matrices and Linear Transformations
3. Eigenvalues, Eigenvectors, and Diagonalization

**II — Random Vectors and Statistical Structure**

4. Random Vectors and Probability Spaces
5. Expectation and Conditional Probability
6. Covariance, Correlation, and Cross-Correlation
7. Gaussian Random Vectors
8. Convergence — Law of Large Numbers and the Central Limit Theorem

**III — Linear Estimation**

9. Singular Value Decomposition
10. Principal Component Analysis (capstone)
11. Least Squares Estimation
12. Linear MMSE Estimation (capstone)

**IV — Applications**

13. Estimation in Signal Processing
14. Advanced Filtering and Modern Applications

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
