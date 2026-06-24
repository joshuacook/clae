# CLAE — Computational Linear Algebra for Estimation

Springer book. Prose motion (no Claude Code prompts). Draft PDF to the editor by **Aug 1, 2026**.

## Before drafting

Read `agreements/writing-process.md` (artifact classes, lens process, production
flow) and `agreements/section-drafting-playbook.md` (9 section types, lens sets).
Then the style agreements: `markdown-style.md`, `paragraph-sizing.md`,
`vocabulary-capitalization.md`, `emdash-purge.md`.

## Chapter list (14 chapters, 4 parts)

**I — Linear Algebra Foundations**

1. Vector Spaces and Data Representation
2. Matrices and Linear Transformations
3. Eigenvalues, Eigenvectors, and Diagonalization
4. Singular Value Decomposition

**II — Random Vectors and Statistical Structure**

5. Random Vectors and Probability Spaces
6. Covariance, Correlation, and Cross-Correlation
7. Gaussian Random Vectors
8. Convergence — Law of Large Numbers and the Central Limit Theorem
9. Expectation and Conditional Probability

**III — Linear Estimation**

10. Principal Component Analysis (capstone)
11. Least Squares Estimation
12. Linear MMSE Estimation (capstone)

**IV — Applications**

13. Estimation in Signal Processing
14. Advanced Filtering and Modern Applications

## Source coverage (from the course)

Strong source: Ch 1–6, 10. Thin/absent (write from scratch): Ch 7, 9, 11, 12, 13,
14, and most of 8 — the estimation-theory destination. Rich assets: the three case
studies (Ames, wholesale, PCA tutorial) and project-1 feed Ch 10 and the
application chapters.

## PII

Never copy student submissions from `~/working/teaching/courses/linalg/assessments/`
into this repo.

## PDF rendering

Output to `/tmp`, never the repo. xelatex via pandoc; `rsvg-convert` SVG→PDF first.
