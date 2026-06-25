---
title: "Ch 10 Notes: Principal Component Analysis (capstone)"
type: chapter-notes
chapter: 10
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 10 Notes: Principal Component Analysis (capstone)

Co-produced with `chapter_outlines/clae-chapter-10.md`, built from
`chapter_notes/clae-chapter-10-source-map.md`. The *why* behind the chapter. This
is the Part III capstone: the reunion of the eigen road (Ch 3) and the SVD road
(Ch 9), and the first place the book teaches a named estimator end to end.

## Role in the book

The destination of the first three parts. Part I built the matrix machinery
(transformations, eigendecomposition, SVD); Part II built the statistical
structure (random vectors, covariance, Gaussianity, convergence). PCA is where
both arrive at once. The covariance matrix the reader assembled on Ames in Part II
is the exact object whose eigendecomposition is PCA, and the SVD the reader learned
in Ch 9 is the numerically honest way to compute it. The chapter's thesis: **PCA is
an estimator.** It estimates the directions of maximum variance of a population
from a finite sample, and Ch 8's convergence results are what license that estimate.

## Entry and exit state

**Entry:** the reader can (1) read a matrix as a transformation and project onto a
subspace (Ch 2), (2) eigendecompose a symmetric matrix and read eigenvalues as
stretch factors along orthogonal eigenvectors (Ch 3), (3) factor any matrix as
X = UΣVᵀ and read the singular values and right singular vectors (Ch 9), (4)
assemble and interpret a sample covariance matrix on centered data (Ch 6), and
(5) reason about a sample statistic converging to its population target as n grows
(Ch 8). Standardized, covariance-ready Ames data is in hand from Ch 2/Ch 6.

**Exit:** the reader can (1) state the maximum-variance problem and recognize PCA
as its solution, (2) compute PCA two ways, eigendecomposition of the covariance and
SVD of the centered data, and *prove they coincide*, (3) explain PCA as an
estimator of population principal components with a convergence guarantee, (4)
choose a target dimensionality from a scree plot and a variance-explained
criterion, (5) connect PCA to whitening and learned features for the ML reader,
and (6) run a complete PCA pipeline on Ames covariance, from centered data to
interpreted loadings, in code.

## Narrative arc

The chapter asks one question and answers it twice, then proves the two answers are
the same. We open on the problem: a dataset has too many correlated dimensions, and
we want the few directions along which it actually varies (10.1). Road one:
eigendecompose the covariance matrix; its eigenvectors are those directions and its
eigenvalues are the variance along them (10.2). Road two: take the SVD of the
centered data directly; the right singular vectors are the same directions (10.3).
10.3 is the reunion the whole book has been driving toward: it derives the
equivalence and fixes the normalization convention once. Then the turn that makes
Parts II and III one story: these directions are *estimated* from a sample, and they
converge to the population truth because the sample covariance does (10.4, callback
to Ch 8). With the estimator understood, we make it practical: how many components
to keep (10.5), what PCA becomes in a machine-learning pipeline (10.6), and a full
worked pipeline on Ames (10.7). Each section earns the next: the two roads must both
be on the table before 10.3 can unite them; the equivalence must be settled before
the estimator framing can speak of "the" principal components; the estimator must be
trusted before dimensionality selection is more than a heuristic.

## Key decisions

- **Commit to the (n-1) sample convention, stated once, in 10.3 (author call,
  2026-06-25; ratified in book decisions "draft-time notes").** The source is
  genuinely inconsistent: pca-tutorial nb06 divides by **n** (population covariance,
  matching sklearn's internal convention) and patches the gap with `*149/150`
  rescalings; project-1/milestone1 derives the **sample** covariance (÷(n-1)) from
  first principles; pandas `.cov()` uses ÷(n-1). The book picks **(n-1)** to stay
  consistent with the sample-covariance estimator built in Ch 6 and the
  estimator-convergence story of Ch 8/10.4. The equivalence is therefore stated in
  its exact form: the principal directions equal the right singular vectors of the
  centered data *exactly*, and the eigenvalues of the **sample** covariance equal the
  **squared singular values divided by (n-1)**, not the singular values themselves.
  This convention is announced once in 10.3 and propagated; no later section
  reintroduces ÷n. Where sklearn's ÷n internal convention matters (10.6), it is
  named as an implementation detail, not a competing definition.

- **10.3 is net-new and load-bearing.** No source proves the eigen/SVD equivalence;
  every source either asserts it (L14 skeleton) or works only one road. 10.3 is
  written from scratch and carries two jobs: derive
  C = (1/(n-1)) Xc ᵀ Xc = V (Σ²/(n-1)) Vᵀ from X_c = UΣVᵀ, and resolve the
  normalization. This is the chapter's intellectual center.

- **PCA is taught as an estimator (10.4), net-new beyond project-1's sketch.** This
  is the decision that makes Ch 8 and Ch 9 on-path rather than a detour. The sample
  covariance is an estimator of the population covariance; it converges (LLN) and is
  asymptotically Gaussian (CLT); therefore the empirical principal components
  estimate the population principal components and the estimate improves with n. The
  explicit callback to Ch 8 is the wiring the book decisions log calls for. Only
  project-1/milestone1 touches this, and only as a sketch; the convergence
  callback and the "why empirical PCA works" argument are net-new.

- **Ames is the hero, reframed pervasively from the source's Iris/spring toys.** The
  deepest real source (pca-tutorial) teaches on Iris and the Shlens ball-on-spring.
  The book re-anchors the worked math to Ames so 10.2 consumes the covariance matrix
  the reader assembled in Part II. This reframe is net-new wiring, not adaptation.
  The 2D maximum-variance toy (10.1) keeps a synthetic, clean two-feature picture for
  geometric intuition, then immediately maps it to Ames.

- **The capstone (10.7) is split honestly (per source map's recommendation).** The
  outline conflates three deliverables: Ames covariance PCA, wholesale segmentation,
  and the project-1 pipeline. They are different artifacts. Decision: the **worked
  Ames covariance PCA is the spine** of 10.7 (net-new, the clean Ames-anchored
  capstone the chapter most wants); the **project-1 synthetic pipeline** appears as
  the rank-recovery / convergence verification thread that proves the estimator
  recovers planted truth (image_features known rank 3); **wholesale** is a short
  PCA-as-preprocessing *vignette*, framed honestly (its segmentation is GMM+BIC, PCA
  is upstream preprocessing only, not the clustering method).

- **Whitening is net-new (10.6).** No source covers it. It is taught as the ML-bridge
  payoff: PCA rotates to decorrelate, whitening additionally scales each component to
  unit variance, which is what downstream learned-feature pipelines consume.

- **Do not re-teach SVD (Ch 9 boundary, per source map).** project-1 is an SVD-first
  / four-fundamental-subspaces (FTLA) project. The chapter uses its
  covariance-eigendecomposition and dimensionality-selection content and routes its
  raw-SVD and FTLA material back to Ch 9 (SVD) and Ch 11 (four subspaces, least
  squares). 10.3 *uses* the SVD as a known tool; it does not derive or re-explain it.

## Source posture

Turnkey on the *mechanics* (10.2, 10.5), net-new on the *payload* (10.3, 10.4, 10.6,
the worked Ames capstone), reframe-heavy throughout (Iris/spring to Ames). The
"richest source" label is carried almost entirely by one artifact, the pca-tutorial
case study; PCAt duplicates it, ILA ch09 and L13 are empty, L14 is a topic skeleton.
Effective source is three artifacts: pca-tutorial (deep mechanics), wholesale
(applied preprocessing vignette), project-1 (estimator/convergence framing). Detail
and the section-to-source table are in the source map.

## Forward and back wiring

- **Back:** consumes the Ames sample covariance assembled in Ch 6 (the Part II
  hand-off the book's capstone-per-part decision promised); recalls eigendecomposition
  of a symmetric matrix (Ch 3); uses the SVD factorization X = UΣVᵀ as a known tool
  (Ch 9); leans on convergence of the sample covariance (LLN/CLT, Ch 8) for the
  estimator argument (10.4); reuses centering/standardization as a linear
  transformation (Ch 2).
- **Forward:** the projection-and-residual picture and the
  "minimize reconstruction error = maximize retained variance" duality set up least
  squares (Ch 11); the estimator framing (sample to population, with a convergence
  guarantee) is the template for every estimator in Part III/IV (least squares Ch 11,
  LMMSE Ch 12, Kalman Ch 13/14); whitening and learned features (10.6) seed the ML
  through-line that resurfaces in Ch 11 (regularization) and Ch 14 (modern filtering).

## Engagement

The "two roads arrive at the same place" reveal is the chapter's aha: the reader has
traveled the eigen road and the SVD road separately for nine chapters and watches them
turn out to be one road. The estimator turn (10.4) is the emotional payoff of Part II:
the convergence machinery the reader may have taken on faith in Ch 8 is suddenly the
reason their PCA works. Risk: 10.3's derivation can read as algebra-for-its-own-sake;
keep it tethered to the question "why do two completely different computations give
the same answer?" and show the numerical agreement on Ames before the proof. Risk:
the capstone can sprawl across three datasets; the honest split (Ames spine,
project-1 verification, wholesale vignette) keeps it from becoming three half-projects.

## Code plan

Extend the cumulative library. The reader arrives with centered/standardized Ames
data and a sample-covariance function (Ch 2/Ch 6). Add: eigendecomposition-based PCA
(`np.linalg.eigh` on the covariance, descending sort), SVD-based PCA
(`np.linalg.svd` on centered data), a numerical-agreement check that the two produce
the same directions and that eigenvalues equal σ²/(n-1), explained-variance and
cumulative-variance computation, a scree plot, projection onto the top-k components
(scores) and reconstruction (`inverse_transform` analogue), whitening, and the
loadings table for interpretation. Verification threads: the image_features
rank-3 recovery (does the scree plot show the planted rank?) and a convergence
demonstration (principal directions stabilize as n grows, the Ch 8 callback in code).
Figures: the 2D maximum-variance toy with the principal axes overlaid; the two-roads
schematic (eigen-of-covariance and SVD-of-centered-data converging on the same V);
the Ames scree plot. Checkpoint: a fitted Ames PCA with interpreted top components
and a kept-dimensionality decision the reader can justify.
