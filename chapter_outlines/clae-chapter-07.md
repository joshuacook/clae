---
title: "Ch 7 Outline: Gaussian Random Vectors"
type: chapter-outline
chapter: 7
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 7 Outline: Gaussian Random Vectors

Co-produced with `chapter_notes/clae-chapter-07.md`. Section-level content plan,
budgets sum to ~28 pp. Source verdicts per section are in
`chapter_notes/clae-chapter-07-source-map.md`.

## 7.1 The univariate normal, recalled (~3 pp · net-new recall, one figure from L009)

- The scalar normal PDF and its two parameters: mean (location) and variance
  (spread); the bell curve as a recall hook, assumed from the first probability
  course.
- The standardization map z = (x - mu) / sigma as the bridge to the vector case;
  the squared standardized deviation ((x - mu) / sigma)^2 as the scalar precursor
  of the Mahalanobis form.
- Why we recall it now: the multivariate object is built by replacing scalar
  variance with the covariance matrix.
- Figure: the scalar normal PDF, location and spread annotated (adapted from
  L009's TikZ figure).

## 7.2 The multivariate normal (~6 pp · net-new density; geometry adapted from L010/L009)

- The MVN density: the exponent is the **Mahalanobis quadratic form**
  (x - mu)^T Sigma^-1 (x - mu); the normalization constant
  (2 pi)^(-n/2) |Sigma|^(-1/2); derivation by the affine change of variables from
  n independent standard normals (the whitening view, ties to Ch 6 eigenstructure).
- Mean vector and covariance matrix as the *only* parameters: the MVN is fixed by
  its first two moments, the fact that makes Part III's covariance-only estimators
  sufficient.
- The geometry: level sets are ellipsoids centered at mu, axes along the
  eigenvectors of Sigma, semi-axis lengths scaled by sqrt(eigenvalue); this is
  exactly Ch 6.2's spread ellipsoid, now as a density contour. Chi-square levels
  set confidence regions.
- Figures: MVN density surface/contour for n = 2; the covariance ellipse with
  Mahalanobis chi-square levels (adapted from L010's iris confidence ellipse and
  L009's quadratic-form figure, re-anchored away from iris).

## 7.3 Why Gaussian dominates: closure under linear maps (~4 pp · net-new)

- The closure theorem: if X is MVN, then AX + b is MVN with mean A mu + b and
  covariance A Sigma A^T; a short proof at first-course altitude (characteristic
  function or affine substitution), not measure theory.
- Corollaries the book leans on: marginals of an MVN are MVN; any linear
  combination of jointly Gaussian variables is scalar Gaussian; sums of
  independent Gaussians are Gaussian.
- Tractability payoff: this is *why* the Gaussian is the modeling default and why
  linear estimators preserve Gaussianity through Part III; the affine-in,
  affine-out picture as the ellipsoid transforming under A.
- Forward pointer (light): closure is the lever the CLT uses in Ch 8.4 and the
  reason the Kalman recursion stays Gaussian in Ch 13-14.
- Figure: closure as the covariance ellipsoid mapped through A (net-new SVG).

## 7.4 The conditional Gaussian (~7 pp · net-new · the chapter spine, LMMSE seed)

- Partition a jointly Gaussian (X, Y) into blocks with block mean and block
  covariance [[Sigma_XX, Sigma_XY], [Sigma_YX, Sigma_YY]].
- **The result:** the conditional law of X given Y = y is again Gaussian with
  conditional mean mu_X + Sigma_XY Sigma_YY^-1 (y - mu_Y), which is **linear**
  (affine) in y, and conditional covariance
  Sigma_XX - Sigma_XY Sigma_YY^-1 Sigma_YX, which does **not** depend on the
  observed y. Derive from the joint density by completing the square in the
  exponent (uses 7.2's quadratic form and 7.3's block algebra).
- Read the meaning against the running thread: the conditional mean is a linear
  predictor of the unobserved block from the observed block; the conditional
  covariance is the residual uncertainty after observing, smaller than the prior
  Sigma_XX (the Schur complement).
- **Explicit LMMSE-seed link to Ch 12:** this conditional-mean formula is exactly
  the Linear MMSE estimator derived in Ch 12.3 from covariance and
  cross-covariance, and Ch 12.4 shows that in the Gaussian case LMMSE = MMSE =
  this conditional mean. Name the pointer once; specialize Ch 5.4's MMSE seed
  (conditional mean as best predictor) to "and in the Gaussian case it is linear."
- Figure: conditioning as slicing the joint ellipsoid at Y = y; the slice
  centers at the conditional mean and its width is the conditional covariance
  (net-new SVG).

## 7.5 Gaussian vs real data (~4 pp · adapt, re-sourced from Ames)

- The honest question: are real features actually Gaussian? Diagnose on Ames.
  Most raw features (SalePrice, lot area, living area) are **right-skewed**, not
  bell-shaped.
- Diagnostics: histogram/KDE with mean-vs-median read (mean above median signals
  right skew); the skew coefficient as a number (`scipy.stats.skew`).
- Normalization: log and Box-Cox transforms restore approximate normality;
  Gelman-style scaling noted. Framed as "the Gaussian model is an approximation,
  here is how good and how to improve the fit," not a debunking; the regularized
  modeling apparatus around these transforms (Lasso/Ridge pipelines) is
  deliberately left out.
- Scope honesty: these are **univariate, marginal** checks; they do not test
  joint normality. That gap is what 7.6's multivariate demo fills.
- Sources: Ames `05-03-basic_eda`, `05-06-preprocessing`; HMD-02 cited only for
  the skew-table snippet.

## 7.6 Implementation: MVN sampling/density and Ames Gaussian-vs-skew (~4 pp · split: net-new + adapt)

Two visibly distinct halves; they make different claims and must not be conflated.

### 7.6a MVN sampling and density (net-new, synthetic then Ames)

- Sample from a known mu, Sigma with `np.random.multivariate_normal`; evaluate
  the density with `scipy.stats.multivariate_normal`; a helper draws the
  theoretical density ellipse (eigendecomposition of Sigma, chi-square radius).
- The genuine multivariate Ames demo: fit an MVN to **two correlated Ames
  features**, overlay the theoretical density ellipse on the scatter, sample from
  the fit and compare to the empirical cloud.
- The honesty check: empirical Mahalanobis distances of the two-feature Ames
  data against the chi-square(2) reference (Q-Q or histogram overlay). The honest
  test of 7.2's joint claim on real data, which no source provides.

### 7.6b Ames skew diagnostic (adapt)

- Per-feature histogram/KDE with mean and median lines; a `scipy.stats.skew`
  table across numerical features; a log/Box-Cox transform showing approximate
  normalization (before/after). Ported from `05-03`/`05-06`.

- Checkpoint: a fitted MVN on two Ames features with its density ellipse and a
  chi-square Mahalanobis check; a skew table identifying which features are
  approximately Gaussian and which need a transform.

## 7.7 Summary and exercises (~2 pp · net-new)

- "By the end" recap tied to the exit state: density and quadratic form, closure,
  the conditional Gaussian, the data diagnosis.
- Forward to Ch 8: closure (7.3) underwrites the CLT; the Gaussianity question
  (7.5) is tested at scale in the Part II capstone (Ch 8.7).
- Forward to Ch 12 restated: 7.4's conditional mean is the LMMSE estimator.
- Exercises: net-new throughout. Derive the MVN constant; prove a marginal of an
  MVN is MVN (closure corollary); complete the square to get the conditional mean
  for a 2D pair; verify conditional covariance is the Schur complement; compute a
  Mahalanobis distance and read its chi-square p-value; on Ames, skew-diagnose a
  named feature and pick a transform; fit a 2D MVN and run the chi-square check.

## Figures (chapter inventory)

1. 7.1 scalar normal PDF (adapt L009).
2. 7.2 MVN density surface/contour, n = 2 (net-new).
3. 7.2 covariance ellipse with Mahalanobis chi-square levels (adapt L010/L009,
   re-anchored off iris).
4. 7.3 closure: covariance ellipsoid mapped through A (net-new).
5. 7.4 conditioning as a slice of the joint ellipsoid (net-new).
6. 7.5 Ames feature skew, before/after transform (adapt).
7. 7.6 two-feature Ames scatter with MVN density-ellipse overlay; chi-square
   Mahalanobis Q-Q (net-new).

## Dataset

**Ames housing** (the hero), two correlated numerical features for the
multivariate demo (candidate pair: living area and SalePrice, or living area and
lot area, chosen at section-outline time for clean positive correlation);
synthetic known-mu/Sigma MVN for the unambiguous sampling picture. HMD-02 (Boston)
not used as a dataset, only its skew-table snippet.

## Budget check

3 + 5 + 4 + 7 + 4 + 3 + 2 = 28 pp. Trims committed: 7.2's derivation compressed to
the whitening view plus a stated constant; 7.6b's transform demo folded to a single
before/after pair. 7.4 is protected; it is the chapter spine and the LMMSE seed.

## Open items for section-level work

- 7.4: choose the worked conditioning example (a 2D jointly Gaussian pair on two
  Ames features vs an abstract block pair) and decide how much block-matrix
  notation to introduce here vs defer to Ch 12.
- 7.6a: fix the exact two-feature Ames pair and confirm it is clean enough
  (positive correlation, no dominating outliers) for the density-ellipse overlay
  to read well.
- 7.5: decide log vs Box-Cox as the lead transform (lean: log for SalePrice, the
  Ames-native choice; Box-Cox as the general tool).
- Confirm the closure proof altitude (characteristic function vs affine
  substitution) at draft time; pick the one that needs least new machinery for a
  first-probability reader.
