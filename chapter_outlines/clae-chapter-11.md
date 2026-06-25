---
title: "Ch 11 Outline: Least Squares Estimation"
type: chapter-outline
chapter: 11
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 11 Outline: Least Squares Estimation

Co-produced with `chapter_notes/clae-chapter-11.md`. Section-level content plan,
budgets sum to ~30 pp. Source verdicts per section are in the source map; the short
form is here. The chapter is **partial**: 11.1-11.2 adapt lesson 004, 11.3-11.5
(math) are net-new, 11.5 code and 11.6 reframe-and-port HMD onto a from-scratch
Ames fit.

## 11.1 The over-determined system (~4 pp · adapt L4)

- A model fit to noisy data writes more equations than unknowns: n observations, p
  parameters, n > p. Set up Ax = b with A the n-by-p design matrix.
- Why there is no exact solution: b is almost never in the column space of A; the
  worked 5x2 toy from L4 makes "no x solves it" concrete.
- Reframe to Ames: predict sale price from a handful of features, one row per home,
  far more homes than features. The over-determined regime is the data regime.
- The honest pivot: we will not solve Ax = b; we will find the x that comes closest.
- Source verdict: **adapt** (L4 gives the n>p framing and the toy almost turnkey;
  port the motivation from L4's price-vs-features to Ames).

## 11.2 The geometry of least squares (~5 pp · adapt L4)

- "Closest" means smallest residual: minimize the distance ||Ax - b||.
- The geometry: Ax ranges over the column space of A; the closest point to b in that
  space is the orthogonal projection of b onto it.
- The residual b - Ax is orthogonal to the column space: it lies in the left null
  space. This is the geometric heart of the chapter.
- Callback to Ch 2.3 projection and Ch 2.4 column/null space; this is where L4's four
  fundamental subspaces, deferred from Ch 2, finally do their work.
- Forward note (quiet): Ch 12's orthogonality principle is the random-vector analogue
  of this picture.
- Figure: b, its projection onto the column space, and the orthogonal residual (SVG).
- Source verdict: **adapt** (the single best-matched section in the chapter; L4 is
  exactly on-frame). L4 stops at naming the projection, which is fine here, 11.3
  derives it.

## 11.3 The normal equations (~5 pp · net-new)

- The squared-error loss: J(x) = ||Ax - b||^2, expanded as a quadratic in x.
- Calculus route: take the gradient, set it to zero, arrive at A^T A x = A^T b.
- Geometric route: the residual is orthogonal to every column of A, so
  A^T(b - Ax) = 0, the same normal equations. The two routes agreeing is the payoff,
  it ties the algebra to 11.2's picture.
- When A has full column rank, A^T A is invertible and x = (A^T A)^-1 A^T b is unique;
  name the hat matrix A(A^T A)^-1 A^T as the projection of 11.2 made explicit.
- Source verdict: **net-new** (no source derives the normal equations or the loss;
  L4 names the projection but never minimizes anything).

## 11.4 Computation: QR, the SVD pseudoinverse, numerical stability (~5 pp · net-new, leans on Ch 9)

- Why not just invert A^T A: forming A^T A squares the condition number, so collinear
  features make the normal equations numerically fragile. Show it on Ames.
- QR factorization: A = QR, solve R x = Q^T b by back-substitution, never forming
  A^T A. The numerically preferred direct method.
- The SVD pseudoinverse (forward-linked from Ch 9): A = U Sigma V^T gives
  A^+ = V Sigma^+ U^T and x = A^+ b; Sigma^+ inverts the nonzero singular values.
  When A is rank-deficient or ill-conditioned, the SVD route is the safe one and sets
  up ridge (11.5) as singular-value regularization.
- A short decision guide: normal equations (fast, fragile), QR (the default), SVD
  (rank-deficient / diagnostic).
- Source verdict: **net-new** for QR and stability; the pseudoinverse is the in-book
  Ch 9 SVD, not external source.

## 11.5 Regularization: ridge / Tikhonov and the ML bridge (~5 pp · net-new math, reframe-and-port code)

- The ill-posed problem: when p approaches n or features are collinear, the
  least squares fit has huge, unstable coefficients.
- The ridge derivation (net-new): add lambda||x||^2 to the loss; the normal equations
  become (A^T A + lambda I) x = A^T b. lambda I lifts the spectrum off zero, so the
  inverse always exists. This is Tikhonov regularization.
- The SVD reading: ridge shrinks each singular-value contribution by
  sigma_i / (sigma_i^2 + lambda), damping the small (noisy) directions most. Connects
  ridge to 11.4's pseudoinverse cleanly.
- The ML bridge: ridge is regularized least squares, the bias-variance trade in
  linear form; choosing lambda is a model-selection problem. Mention Lasso (L1) as the
  contrast in passing, not derived. This is the chapter's named ML-bridge moment.
- Interpreting coefficients: why standardized features (Ch 2.5-2.6) are required for
  the penalty to be meaningful.
- Figure: singular-value shrinkage and/or the coefficient path vs lambda (SVG).
- Source verdict: ridge **math net-new**; the alpha-sweep / train-test-score harness
  is the HMD `lm.py` pattern, **reframed** from sklearn to from-scratch and **ported**
  Boston to Ames.

## 11.6 Implementation: predict Ames sale price; pseudoinverse via SVD (~4 pp · adapt HMD prep, fit net-new)

- Load and prep Ames the HMD way (numerical features, simple impute, standardize),
  but author the fit; HMD has no Ames least squares fit anywhere.
- Fit sale price three ways and confirm they agree on a well-conditioned subset:
  `np.linalg.lstsq`, the normal equations, and the pseudoinverse via SVD (reusing the
  Ch 9 SVD code).
- Train/test split, fit, predict, score (R^2 / RMSE in dollars); then sweep lambda for
  ridge and pick the alpha that scores best on held-out data (the HMD harness pattern,
  from scratch).
- Show the conditioning failure concretely: A^T A on collinear features vs the QR/SVD
  route, so 11.4's claims are demonstrated, not asserted.
- Checkpoint: a fitted Ames sale-price model, train and test scores, and a chosen
  ridge alpha.
- Source verdict: **adapt** HMD for data-prep and harness pattern only; the fit is
  **net-new**.

## 11.7 Summary and exercises (~2 pp · net-new)

- "By the end" recap tied to the exit state: over-determined, project, derive,
  compute three ways, regularize, predict.
- Exercises: derive the normal equations both ways; show A^T A squares the condition
  number; relate the SVD pseudoinverse to the normal equations; derive the ridge
  shrinkage factor; an Ames fit/score problem seeded from the 11.6 harness.
- Forward to Ch 12: the projection / orthogonal-residual geometry returns as the
  orthogonality principle when the vectors become random.
- Source verdict: **net-new** (HMD scoring loop is the only exercise seed).

## Figures

- **Fig 11.1** (11.2): b projected onto the column space of A; the orthogonal
  residual in the left null space. The chapter's geometric anchor. SVG.
- **Fig 11.2** (11.5): ridge as singular-value shrinkage, and/or the coefficient path
  as lambda increases. SVG.

## Dataset

- **Ames housing** (the recurring hero), target `SalePrice`. Prep via the HMD Ames
  preprocessing pattern (numerical features, impute, standardize); the fit is
  authored from scratch. The 5x2 toy from L4 carries 11.1-11.2 before Ames enters.
- Clean assets only: case-study-05-ames and the PCA-tutorial `ames_features` /
  `ames_target`. Never copy student submissions from `assessments/` (PII).

## Budget

| Section | Pages |
|---|---|
| 11.1 Over-determined system | 4 |
| 11.2 Geometry of least squares | 5 |
| 11.3 The normal equations | 5 |
| 11.4 Computation (QR, SVD, stability) | 5 |
| 11.5 Regularization (ridge / ML bridge) | 5 |
| 11.6 Implementation (Ames fit) | 4 |
| 11.7 Summary and exercises | 2 |
| **Total** | **30** |

## Open items for section-level work

- 11.4: decide whether to *derive* the QR back-substitution solve or state it and
  point to a numerical-methods reference; lean toward stating, since the book is
  estimation-first, not numerical-linear-algebra.
- 11.5: decide depth on Lasso (lean: named as the L1 contrast, not derived) and
  whether the figure is shrinkage, coefficient path, or both.
- 11.6: decide the exact Ames feature subset for the fit (small, well-conditioned set
  for the three-ways agreement; a larger collinear set to demonstrate the conditioning
  failure and motivate ridge). Decide R^2 vs RMSE-in-dollars as the headline score.
- 11.6: confirm the train/test split protocol matches whatever Ch 8/10 used, for
  cross-chapter consistency.
