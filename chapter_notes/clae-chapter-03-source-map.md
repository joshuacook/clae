---
title: "Ch 3 Source Map"
type: chapter-source-map
chapter: 3
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 3 Source Map: Eigenvalues, Eigenvectors, and Diagonalization

Source Assembly for Ch 3 (the Part I eigentheory chapter, ending in the rank-3
capstone). Gathered from `source/coverage-by-chapter.md`: course L7 Eigentheory,
ILA ch08 eigensystems, image_features (rank-3). Maps source to the book-outline
sections with a reuse verdict, then notes gaps. Feeds the Ch 3 notes+outline.

The "strong" coverage tag is optimistic: the real source is **L7 alone**, it is
2x2-only and structurally noisy, and the headline asset (ILA ch08) is an empty
stub.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 3.1 The eigenvalue problem (Av = lambda v; invariant directions) | L7 ("Introduction to Eigentheory": invariant-direction motivation, the [[2,1],[1,2]] stretch example, the (A - lambda I)v = 0 derivation) | clean conceptual on-ramp; the "special directions reveal structure" framing | adapt (strong); this is L7's best material |
| 3.2 Finding eigenvalues and eigenvectors (characteristic polynomial; eigenspaces and multiplicity) | L7 (characteristic-polynomial derivation; direct + upper-triangular worked examples; eigenspaces; algebraic vs geometric multiplicity; the defective [[2,2],[2,2]] case) | worked 2x2 mechanics + multiplicity vocabulary | adapt **with rewrite of the derivation**: L7 derives the char. poly by a 2x2 "equations must be dependent / a^2=1" trick, not via det(A - lambda I)=0. The determinant framing and any n>2 case are net-new. |
| 3.3 Diagonalization (the eigenbasis; when it exists) | L7 (P^-1 A P = D process; worked [[1,2],[2,4]]; requirements: n independent eigenvectors, alg=geom; not-all-diagonalizable) | the diagonalization procedure + existence conditions, worked at 2x2 | adapt (strong for 2x2); the "change of basis" / eigenbasis interpretation is thin and partly net-new |
| 3.4 Symmetric matrices and the spectral theorem (real eigenvalues, orthogonal eigenvectors; sets up covariance and PCA) | L7 (only a 3-bullet "Special Cases" list: symmetric => real eigenvalues, orthogonal eigenvectors, always diagonalizable; stated, never proved or motivated) | the bare statement of the result | **rewrite/net-new**: the spectral theorem is the load-bearing bridge to Ch 6/10, and the course never develops it (no proof, no orthogonality argument, no PSD/covariance tie-in). Build from scratch. |
| 3.5 *Implementation:* power iteration on Ames' second-moment matrix | **none** (power iteration appears nowhere in the course; L7 colab is plotting/eigen examples, no algorithm; Ames second-moment matrix never built in any lesson) | — | **net-new** (algorithm + the Ames second-moment construction are both new) |
| 3.6 **Part I capstone:** recover image_features' rank 3 by eigendecomposition, before any probability | image_features.csv (generated rank-3 + 0.1 noise, 1000x10, confirmed in `generate_datasets.py`); project-1 milestone handouts reference its eigenstructure | the dataset and its known ground-truth rank | **net-new framing**: in project-1 the rank-3 recovery is a *covariance/PCA* task (milestone1 frames it via the sample covariance estimator and eigenstructure). Doing it pre-probability, by raw eigendecomposition of a Gram/second-moment matrix, is a deliberate new construction. Data exists; the procedure does not. |
| 3.7 Summary and exercises; forward to SVD (Ch 9) | L7 colab + practice problems (eigenvalue, diagonalization, defective-matrix problems; all 2x2); L7 "Additional Resources" | a solid 2x2 problem bank | adapt as seed; the forward-pointer to SVD is net-new |

## Gaps and conflicts

- **ILA ch08 is an empty stub.** Both `ch08-eigensystems.md` (27 bytes: a title +
  `\pagebreak`) and `ch08-eigensystems.html` (a website template, no math) contain
  zero eigentheory content. The coverage table's "ILA ch08 eigensystems" credit is
  vapor. Real source for this chapter is L7 only.

- **Source is 2x2-only.** Every L7 example, derivation, and practice problem is a
  2x2 matrix. The book needs the determinant-based characteristic polynomial and at
  least one n>=3 case (the rank-3 capstone is 10-dimensional). All n>2 generalization
  is net-new.

- **L7's characteristic-polynomial derivation is non-standard.** It avoids
  determinants entirely, deriving lambda^2 - (a+d)lambda + (ad-bc) = 0 from a "the
  two equations must be dependent" / a^2 = 1 argument. Usable as intuition but must
  be rewritten to the standard det(A - lambda I) = 0 so it generalizes.

- **L7 carries off-topic ballast.** Roughly a third of L7_math (sections 5 "Matrix
  Decompositions": LU decomposition, inverse via LU) belongs to **Ch 2** (systems /
  invertibility), not eigentheory. Do not pull LU into Ch 3. L7's title
  ("Linear Transformations and Eigentheory") also bleeds Ch 2 transformation content;
  the rotation/projection/shear bullets in its "Geometric Interpretation" overlap the
  Ch 2.3 net-new geometry, not Ch 3.

- **3.4 spectral theorem is essentially unsourced.** L7 states the symmetric-matrix
  properties as a 3-bullet aside and never proves or motivates them. This is the
  single most important section for the downstream PCA/covariance arc and is a
  write-from-scratch.

- **3.5 power iteration is unsourced.** No iterative eigen-algorithm anywhere in the
  course; numpy `linalg.eig` is the only tool L7 colab uses. The Ames second-moment
  matrix is also never constructed in any lesson.

- **3.6 capstone reframes project-1.** image_features exists and is genuinely rank-3,
  but project-1 reaches its rank via the *sample covariance* (a Part II / Ch 6-10
  construction). The outline's promise -- recover rank "before any probability" via
  plain eigendecomposition -- is a new, deliberately probability-free procedure. The
  dataset is reusable; the method is net-new and must avoid importing covariance
  language early (dormancy / forward-reference risk).

## Implication for the chapter outline

The 7-section sequence holds; the work is heavier than "strong" implies. Triage:

- **Adapt (real L7 source):** 3.1, 3.2 (rewrite the derivation), 3.3, 3.7. These are
  solid at 2x2 and need generalization to n dimensions.
- **Net-new:** 3.4 (spectral theorem -- the priority write, it carries the whole
  Ch 6/10 bridge), 3.5 (power iteration + Ames second-moment), 3.6 (probability-free
  rank-3 recovery procedure).

Two structural cautions. First, **keep Ch 2 material out of Ch 3**: drop L7's LU
decomposition and transformation-geometry sections wholesale (they are Ch 2's).
Second, **guard the pre-probability promise in 3.6**: the only worked rank-recovery
the course offers is covariance-based, so the capstone must be written to use a raw
second-moment / Gram eigendecomposition and explicitly defer covariance to Part II,
or the chapter will leak forward references.

Net assessment: Ch 3 is adapt-on-the-mechanics (3.1-3.3, 3.7, all 2x2) but
net-new-on-the-payload (3.4 spectral theorem, 3.5 power iteration, 3.6 capstone).
The "strong" tag reflects L7 existing, not L7 being sufficient; ILA ch08 contributes
nothing.

## Addendum (2026-07-11): 2015-paper loot for Ch 3

- Running example: eigenvectors of the second difference matrix ARE sines;
  eigenvalues 2 − 2cos(kπ/(n+1)). Computed fact + analytic formula, NO
  representation theory (symmetry ruled OUT 2026-07-11).
- Exhibit: the analytic-vs-LAPACK eigensolver race, including the n=100 upset
  ("This last result is astounding" is the quotable verdict sentence).
- §3.5: the power method.
- DFW footnote stock: imaginary-time propagation / seven-solver benchmark.
- Zernike (2014): visual-basis figure candidate here or Ch 1.3.
- K is already planted: Ch 2 closes with "the second difference matrix K is
  carrying a set of [eigenvectors] you already know by name."

Source: Cook, *Computational Methods in Molecular Quantum Mechanics*, Leanpub
2016. Full reuse cleared.
