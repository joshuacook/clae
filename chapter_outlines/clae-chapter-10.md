---
title: "Ch 10 Outline: Principal Component Analysis (capstone)"
type: chapter-outline
chapter: 10
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 10 Outline: Principal Component Analysis (capstone)

Co-produced with `chapter_notes/clae-chapter-10.md`. Section-level content plan;
budgets sum to ~36 pp. Source verdicts per section are in the source map
(`chapter_notes/clae-chapter-10-source-map.md`). Part III project capstone (PCA): the reunion
of the eigen road (Ch 3) and the SVD road (Ch 9), PCA taught as an estimator.

**Dataset.** Hero: **Ames housing** (the sample covariance assembled in Part II is
the object whose eigendecomposition is PCA). Verification: **image_features**
(known rank 3, for scree/rank recovery and the convergence demo). Vignette:
**wholesale customers** (interpretable loadings; PCA as upstream preprocessing).
A small synthetic two-feature set carries the 10.1 geometric toy.

**Convention committed once (10.3):** the sample (n-1) covariance. Principal
directions equal the right singular vectors *exactly*; eigenvalues of the sample
covariance equal **singular values squared, divided by (n-1)**. Stated once,
propagated; no later section reintroduces ÷n (sklearn's internal ÷n is named as an
implementation detail in 10.6, not a competing definition).

## 10.1 The problem: directions of maximum variance (~4 pp · adapt pca-tutorial nb02/05, reframe to Ames)

- The setup: a dataset with many correlated features (Ames) varies along far fewer
  directions than it has columns. We want those directions, ranked by how much the
  data varies along them.
- Variance as the goal: the first principal direction is the unit vector maximizing
  the variance of the projected data; each subsequent one is orthogonal to the prior
  and maximizes remaining variance.
- The 2D geometric toy (clean synthetic two-feature cloud): rotate the axes to align
  with the cloud's spread; the long axis is the first principal direction. Then map
  the picture onto two correlated Ames features.
- Change of basis framing: PCA is a rotation to a basis where the data is
  uncorrelated and the axes are ordered by variance.
- **Figure 10.1:** the 2D cloud with original axes and the principal axes overlaid.

## 10.2 PCA via eigendecomposition of the covariance (~5 pp · adapt pca-tutorial nb04/06, reframe Iris to Ames)

- Consume Part II's Ames covariance: the sample covariance matrix C (centered data,
  (n-1) convention) is the object we eigendecompose.
- The result (worked): the eigenvectors of C are the principal directions; the
  eigenvalues are the variance along each. C is symmetric positive semidefinite, so
  the eigenvectors are orthogonal and the eigenvalues are real and nonnegative
  (callback to Ch 3's symmetric eigendecomposition).
- The explicit recipe: center the data, form C, eigendecompose, sort eigenpairs
  descending, read explained variance from the eigenvalues, project onto the top
  eigenvectors. (Adapted from nb06's 5-step recipe, re-derived on the (n-1)
  convention, **not** nb06's ÷n.)
- Worked on Ames: the top eigenvectors and what their large-magnitude entries
  (loadings) say about which features co-vary.

## 10.3 PCA via SVD of the centered data (the equivalence) (~6 pp · NET-NEW)

- The second road: take the SVD of the centered data matrix directly,
  X_c = UΣVᵀ (Ch 9 tool, not re-derived). Claim: the right singular vectors V are
  the principal directions, same as 10.2's eigenvectors.
- **The derivation (load-bearing, the chapter's center):** substitute X_c = UΣVᵀ
  into C = (1/(n-1)) X_cᵀ X_c to get C = V (Σ²/(n-1)) Vᵀ. Read off: V
  diagonalizes C, so its columns are C's eigenvectors (the principal directions,
  exactly equal to the right singular vectors); the eigenvalues of C are the
  diagonal of Σ²/(n-1).
- **Resolve the normalization once:** state the (n-1) sample convention explicitly,
  contrast it with the ÷n population form the reader may meet elsewhere, and fix the
  exact relationship: eigenvalue = singular value squared / (n-1). Flag that
  conflating the two (the source's `*149/150` fudge) is exactly the error this
  section exists to prevent.
- Why two roads: eigendecomposition of C squares the data (forms XᵀX), losing
  numerical precision; SVD of X_c is the numerically honest computation. Same answer,
  better conditioning. (Brief; do not re-teach SVD.)
- Numerical agreement on Ames *before* the proof lands: show the two computations
  return the same directions and σ²/(n-1) = eigenvalues, then prove why.
- **Figure 10.2:** the two-roads schematic, eigen-of-covariance and
  SVD-of-centered-data converging on the same V.

## 10.4 PCA as an estimator (~5 pp · NET-NEW beyond project-1/milestone1 sketch)

- The reframe that unifies Parts II and III: the covariance we eigendecompose is the
  **sample** covariance, an estimator of the unknown **population** covariance.
  Therefore the empirical principal components *estimate* population principal
  components; they are not the truth, they are an estimate of it.
- **Callback to Ch 8 (the book-decisions wiring):** the sample covariance converges
  to the population covariance (LLN) and is asymptotically Gaussian (CLT); that is
  *why* empirical PCA works and why the estimate sharpens as n grows. This is the
  payoff of the convergence chapter.
- Bias and consistency, lightly (project-1/milestone1 framing, kept at the book's
  altitude per Ch 8 decision: by argument and simulation, not measure theory).
- In code (verification, deferred in full to 10.7): principal directions stabilize as
  sample size grows; small n gives noisy, unstable components.
- The estimator template named here is reused for every Part III/IV estimator (least
  squares Ch 11, LMMSE Ch 12, Kalman Ch 13/14).

## 10.5 Choosing dimensionality (~4 pp · adapt pca-tutorial nb08 + project-1/final)

- Explained variance ratio: each eigenvalue over their sum; cumulative variance.
- The scree plot and the elbow; the "ad hoc" caveat (nb08) stated honestly.
- The selection trio (project-1/final): elbow, Kaiser (eigenvalue > 1 on
  standardized data), and a percent-variance threshold. When they agree and when
  they do not.
- **Rank check on image_features (net-new wiring):** the dataset has known rank 3;
  the scree plot should show three components carrying essentially all variance and
  a sharp drop after. PCA recovers the planted rank, a concrete estimator-works check.
- **Figure 10.3:** the Ames scree plot with the chosen cutoff marked.

## 10.6 The ML bridge: whitening, dimensionality reduction, learned features (~4 pp · adapt pca-tutorial nb01/02 + wholesale; whitening NET-NEW)

- Dimensionality reduction as the working use: project onto top-k components
  (scores), reconstruct (the `inverse_transform` analogue), and the reconstruction
  error / retained variance duality.
- **Whitening (net-new):** PCA rotates to decorrelate; whitening additionally scales
  each component to unit variance. What it gives downstream learned-feature pipelines
  and why ML pipelines want it.
- PCA as learned features: the sklearn idiom and a brief visualization (digits-style,
  reframed); loadings as interpretable learned directions (wholesale).
- **sklearn's ÷n internal convention named here as an implementation detail**, not a
  competing definition; the book's (n-1) eigenvalues differ by the n/(n-1) factor
  and the reader is told exactly why.
- The ML through-line touchpoint (book decisions): surfaced here because it earns its
  place; resurfaces in Ch 11 (regularization) and Ch 14 (modern filtering).

## 10.7 Project capstone: PCA from intuition to implementation (~6 pp · NET-NEW Ames spine + adapt project-1 + wholesale vignette)

- **Spine: the worked Ames covariance PCA (net-new).** End to end on the hero
  dataset: center the Ames features, assemble the (n-1) covariance, run PCA both ways
  and confirm agreement, choose dimensionality from the scree, interpret the top
  components via their loadings (what each component "means" in housing terms).
- **Verification thread (adapt project-1):** the image_features synthetic set with
  known rank 3, proving the estimator recovers planted ground truth; the convergence
  demo (directions stabilize as n grows), the 10.4 callback realized in code. Routes
  project-1's raw-SVD / four-subspaces content back to Ch 9 / Ch 11 rather than
  re-teaching it.
- **Vignette (honest framing): wholesale PCA-as-preprocessing.** Scaled, deskewed
  data; loadings and scree for interpretation. Stated plainly: the downstream
  segmentation in the source is GMM+BIC, not PCA; PCA is upstream preprocessing only.
- ⊹ **Checkpoint:** a fitted Ames PCA with interpreted top components and a justified
  kept-dimensionality decision; the image_features scree showing rank 3.

## 10.8 Summary and exercises (~2 pp · adapt pca-tutorial practice cells + project-1 deliverables, mostly net-new)

- "By the end" recap tied to the exit state: the two roads, the equivalence, the
  estimator framing, dimensionality selection.
- Exercises: prove the eigen/SVD equivalence on a small matrix; verify
  eigenvalue = σ²/(n-1) numerically; produce and read a scree plot; interpret Ames
  loadings; net-new problems on whitening and on the convergence-with-n behavior.
- Forward to Ch 11: the projection-and-residual picture and the reconstruction-error
  view set up least squares; the estimator template carries into the back half.

## Budget summary

| Section | Pages | Verdict |
|---|---|---|
| 10.1 Directions of maximum variance | 4 | adapt + reframe |
| 10.2 PCA via eigendecomposition | 5 | adapt (turnkey) + reframe |
| 10.3 PCA via SVD (the equivalence) | 6 | net-new |
| 10.4 PCA as an estimator | 5 | net-new |
| 10.5 Choosing dimensionality | 4 | adapt |
| 10.6 The ML bridge | 4 | adapt + net-new (whitening) |
| 10.7 Project capstone | 6 | net-new spine + adapt |
| 10.8 Summary and exercises | 2 | seed + net-new |
| **Total** | **36** | |

## Open items for section-level work

- 10.1: lock the exact two Ames features for the maximum-variance toy (lean: a pair
  with visible positive correlation, e.g. living area and a quality/price proxy, so
  the principal axis is intuitive).
- 10.3: decide how much of the SVD-conditioning argument (why XᵀX loses precision) to
  show versus state, keeping the Ch 9 boundary; lean state-with-one-numerical-example.
- 10.4: settle the depth of bias/consistency. Lean: argument + simulation only, no
  measure theory, matching the Ch 8 altitude decision.
- 10.5: confirm image_features actually scree-breaks cleanly at 3 on the synthetic
  generator's noise level; if not, tune the verification example or caveat it.
- 10.6: decide whether the digits-style visualization survives the Ames reframe or is
  cut for a loadings visualization on Ames/wholesale (lean: keep the chapter on its
  hero datasets, prefer loadings).
- 10.7: confirm the worked Ames PCA notebook is built net-new (no source notebook
  exists; only `ames_features.p` pickled data in the pca-tutorial repo).
