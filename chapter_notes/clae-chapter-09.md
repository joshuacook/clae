---
title: "Ch 9 Notes: Singular Value Decomposition"
type: chapter-notes
chapter: 9
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 9 Notes: Singular Value Decomposition

Co-produced with `chapter_outlines/clae-chapter-09.md`, built from
`chapter_notes/clae-chapter-09-source-map.md`. The *why* behind the chapter.

## Role in the book

The Part III opener and the master factorization of the back half. Part II spent
five chapters building statistical structure (random vectors, expectation,
covariance, Gaussians, convergence); Part III turns that structure into
estimators, and every estimator to come rests on the SVD. PCA (Ch 10) is the SVD
of centered data; least squares (Ch 11) is solved by the SVD pseudoinverse. This
chapter is where Part I's matrix machinery, dormant across the probability
chapters, wakes up: the SVD is diagonalization generalized to any matrix, and the
reader meets it the moment the book needs it.

The chapter has one headline payoff. Diagonalization (Ch 3) told us what a square
symmetric matrix does along its eigenvectors. The SVD tells us what *any* matrix
does, and ranks the pieces by importance. That ranking is the Eckart-Young theorem:
the best low-rank approximation of a matrix is its truncated SVD. We use it to
recover image_features' known rank 3 a second time, now via SVD, as a deliberate
before/after against the Ch 3.6 eigendecomposition pass.

## Entry and exit state

**Entry:** the reader has finished Part II. From Ch 3 they know eigenvalues,
eigenvectors, diagonalization (A = PDP^-1), and the spectral theorem for symmetric
matrices (real eigenvalues, orthogonal eigenvectors). From Ch 6 they know the
covariance matrix and that it is symmetric PSD. They have seen image_features'
rank 3 recovered once, by eigendecomposition of its second-moment matrix (Ch 3.6),
before any probability. They can read a matrix as a transformation (Ch 2) and know
column space, rank, and orthonormal bases (Ch 1 reference).

**Exit:** the reader can (1) state why diagonalization fails for non-square and
non-diagonalizable matrices and why a more general factorization is needed,
(2) write any matrix as U Sigma V-transpose and read it geometrically as
rotate-scale-rotate, (3) connect singular values to rank and to the
eigendecomposition of A-transpose-A and A-A-transpose, (4) state the Eckart-Young
theorem and form the truncated SVD that achieves the optimal low-rank
approximation, and (5) recover image_features' rank 3 via SVD in code, recognizing
it as the same structure Ch 3.6 found by a different road.

## Narrative arc

Diagonalization, then its wall, then the generalization, then what the
generalization is *for*. We open by recalling diagonalization from Ch 3 and
pressing on its limits: it needs a square matrix, n independent eigenvectors, and
(for a clean real picture) real eigenvalues. Real data matrices are rectangular
and the wall is immediate. The SVD walks through that wall: every matrix, square or
not, factors as U Sigma V-transpose, a rotation, then an axis-aligned scaling, then
another rotation. Singular values give rank and order the action by importance.
We compute the SVD by connecting it to the symmetric eigendecomposition the reader
already owns (A-transpose-A = V Sigma-squared V-transpose). Then the payoff: keep
only the largest singular values and you get the *best* low-rank approximation
there is, which Eckart-Young makes precise. We cash this out by recovering
image_features' rank 3, and we close by pointing forward to the two estimators the
SVD unlocks: PCA (Ch 10) and the pseudoinverse (Ch 11).

Each section earns the next. The limits of diagonalization make the SVD's
"any matrix" framing land as relief, not abstraction. The geometry makes singular
values legible as scaling factors. Rank-as-nonzero-singular-values makes truncation
the obvious next question. The eigendecomposition connection makes the SVD
computable with tools the reader already has. Eckart-Young makes truncation
*optimal*, not just convenient. The rank recovery is the proof that it works on
data with a known answer.

## Key decisions

- **9.5 is the chapter, and it is net-new** (source verdict, 2026-06-25). L12
  gestures at "optimal low-rank approximation" as a one-line benefit but never
  states Eckart-Young, never truncates and reconstructs, and never touches
  image_features. The theorem, the truncated reconstruction
  X_k = sum_{i<=k} sigma_i u_i v_i-transpose, the optimality statement (in
  Frobenius and spectral norm), and the rank-3 recovery are written from scratch.
  This is the priority write; the rest of the chapter is the on-ramp to it.

- **The covariance half of L12 is stripped.** L12 is titled "SVD *and Covariance
  Analysis*" and roughly a third of it (random vectors, covariance analysis,
  feature scaling, the Var/Cov square-root analogy, loadings) is Ch 6 material.
  None of it is imported. Only the narrow algebraic bridge survives into 9.4:
  A-transpose-A = V Sigma-squared V-transpose and sigma_i = sqrt(lambda_i). We do
  not re-teach what a covariance matrix is; we use the second-moment / Gram matrix
  as a purely algebraic object, consistent with Ch 3.6's probability-free framing.

- **No PCA vocabulary here.** "Variance explained," "explained_variance_ratio," and
  the U/Sigma/V-as-principal-components reading are Ch 10, not Ch 9. L12 demos all
  of this on iris; we defer every bit of it. 9.7 names PCA as a forward pointer only.
  Pulling PCA forward would duplicate Ch 10 and create the dormancy the book's
  SVD-placement decision was made to avoid.

- **Re-anchor onto image_features, drop iris.** Every L12 worked example uses a 3x2
  toy, a 2D multivariate normal, or iris. The book's promise is the rank-3 recovery
  on image_features (1000x10, generated rank-3 plus 0.1 noise). 9.5 and 9.6 are
  rebuilt on image_features. The toy 3x2 may survive as a hand-computable warm-up in
  9.2/9.6, but the headline demo is image_features.

- **Existence is asserted, lightly justified, not heavily proved** (author call).
  L12 states the SVD and its properties with no construction. The book gives a brief
  existence argument routed through the symmetric eigendecomposition of
  A-transpose-A (which the reader owns from Ch 3.4): the eigenvectors of
  A-transpose-A give V, their eigenvalues' square roots give the singular values,
  and U follows. We state uniqueness up to sign/ordering as a remark. Full
  measure-of-rigor is a graduate-text aside, not a formal theorem with proof; the
  9.4 connection carries the construction.

- **9.5 is a deliberate before/after against Ch 3.6, not a repeat.** Ch 3.6 recovers
  image_features' rank 3 by eigendecomposition of the second-moment matrix; Ch 9.5
  recovers it by SVD of the data matrix directly. The text explicitly calls back to
  Ch 3.6 and frames the contrast: same structure, two roads. The SVD road needs no
  Gram matrix (avoids squaring the condition number) and yields the approximation,
  not just the rank. Coordinate the two passes so they read as a planned diptych.

## Source posture

Adapt-heavy on 9.1 through 9.4 and the SVD scaffolding of 9.6 (L12 secs 0-2 are the
real, and only, source; ILA ch08 is an empty stub contributing nothing). Every
adapted section needs a full rewrite out of L12's lecture-bullet format into book
prose. Net-new on 9.5 (Eckart-Young plus truncation plus the rank-3 recovery, the
headline), the image_features re-grounding of 9.6, and the pseudoinverse forward
pointer in 9.7. Cautions, all from the source map: strip the covariance third of
L12, defer all PCA vocabulary to Ch 10, and re-anchor off iris onto image_features.

## Forward and back wiring

- **Back:** opens by recalling Ch 3 diagonalization and the spectral theorem
  (Ch 3.4), and generalizing them. 9.4 reuses the symmetric eigendecomposition the
  reader built in Ch 3. 9.5 explicitly calls back to Ch 3.6's eigendecomposition
  rank-3 recovery and frames the SVD pass as the before/after counterpart. Uses the
  rank, column space, and orthonormal-basis language from Ch 1/Ch 2.
- **Forward:** 9.5's truncated SVD and 9.4's A-transpose-A connection set up Ch 10
  (PCA via SVD of centered data; eigenvalues = singular values squared over n-1, a
  Ch 10 detail flagged but not used here). 9.7 plants the Ch 11 pseudoinverse: the
  SVD inverts the invertible part of the action and solves least squares, which is
  net-new (L12 never mentions it). The chapter hands a working truncated-SVD routine
  and a rank-recovered image_features into Part III.

## Engagement

The "any matrix" reveal is the chapter's first aha: the reader has spent Ch 3
hemmed in by square-and-symmetric, and the SVD removes the fence. The rotate-scale-
rotate geometry is the visual hook. The headline aha is Eckart-Young: truncation is
not a heuristic, it is provably the best you can do, and the rank-3 recovery proves
it on data with a known answer. Risk: 9.4 (computing the SVD) can read as dry linear
algebra plumbing; keep it tied to the question the reader actually has ("how do I
get U, Sigma, V, and why does it work?") and to the numerical-stability payoff
(the SVD avoids squaring the condition number, a caveat worth keeping from L12).
Second risk: the before/after with Ch 3.6 can read as repetition if not framed
sharply; lead with what the SVD road *adds* (the approximation, the stability).

## Code plan

Extend the cumulative library. The SVD scaffolding adapts cleanly from L12's colab
(numpy.linalg.svd with full_matrices=False, the reconstruction check
U @ diag(s) @ Vh == X, the orthogonality/property checks, the eigh-on-A-transpose-A
path as the alternate route). The net-new code is the truncation-to-k routine
X_k = sum_{i<=k} sigma_i u_i v_i-transpose, the rank-recovery demo on
image_features (1000x10 CSV, generated rank-3 plus 0.1 noise; ground truth confirmed
in project-1's generate_datasets.py), and the singular-value spectrum plot that
shows three large values and a noise floor. Figures: the rotate-scale-rotate
geometry of the SVD (SVG, adapting generate_svd_plots.py's plot_svd_example), the
singular-value spectrum of image_features with the rank-3 cliff, and a
reconstruction-error-versus-k curve illustrating Eckart-Young. Checkpoint: a
truncated-SVD reconstruction of image_features at k=3 and the confirmation that its
error matches the planted noise floor. Per CLAUDE.md, render PDFs to /tmp; SVG to
PDF via rsvg-convert before pandoc.
