---
title: "Ch 5 Outline: Expectation and Conditional Probability"
type: chapter-outline
chapter: 5
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 5 Outline: Expectation and Conditional Probability

Co-produced with `chapter_notes/clae-chapter-05.md`. Section-level content plan,
budgets sum to ~28 pp. Source verdicts per section are in the source map. Scratch
chapter: one adapt-from-source section (5.1), one dataset hook (5.5); the
conditioning spine (5.2-5.4) and the exercises (5.6) are net-new.

## 5.1 The expectation operator (~4 pp · adapt L9)

- Expectation as an operator on random variables and random vectors: the discrete
  and continuous definitions, recalled, not taught cold (first-probability-course
  prerequisite assumed).
- Linearity: E[aX + b] = a E[X] + b and E[X + Y] = E[X] + E[Y]; the vector forms
  E[aX + bY] = a E[X] + b E[Y].
- **E[AX] = A E[X]**, worked with the L9 2x2 example, read through the Part I column
  picture (a deterministic matrix passes through expectation).
- Mean vector mu = E[X] re-stated as the operator applied componentwise.
- Coordination note in prose: Ch 4.4 stated how the mean transforms under a linear
  map; this section owns the operator algebra behind it. (Ch 4.4 points forward
  here; do not re-derive the mean-transforms result, cite it.)
- Figure: E[AX] = A E[X] as a commuting square (apply A then average vs average then
  apply A).
- Source: adapt L9 (the lone sourced section; coordinate with Ch 4 to avoid
  duplicating the mean-vector material).

## 5.2 Conditional probability and conditional distributions (~5 pp · net-new)

- Conditioning as restricting the universe: P(A | B) = P(A and B) / P(B) re-read as
  "probability in the world where B happened."
- Conditional distributions: the conditional pmf/pdf of Y given X = x; the
  conditional density f(y | x) = f(x, y) / f(x).
- The Ames anchor introduced here: what is the distribution of SalePrice *given* a
  home's exterior quality? The conditioning event is "this feature takes this
  value."
- Independence as the degenerate case (conditioning changes nothing).
- Figure: the restricted-universe picture (sample space narrowed by the conditioning
  event B), in the chapter's SVG visual language.
- Source: net-new (no lesson, ILA chapter, or repo mentions "conditional").

## 5.3 Conditional expectation and the tower property (~5 pp · net-new)

- E[Y | X = x] as the mean of the conditional distribution: an ordinary expectation
  taken in the restricted universe of 5.2.
- E[Y | X] as a **random variable**: a function of X, g(X), whose value is the
  conditional mean at each outcome of X. This is the conceptual hinge of the
  chapter.
- The **tower property** (law of total expectation): E[E[Y | X]] = E[Y]; averaging
  the conditional means recovers the unconditional mean. Worked on the Ames anchor:
  the overall mean price is the weighted average of the per-group means.
- Linearity and basic properties of conditional expectation (pulling out known
  functions of X).
- Figure: E[Y | X] as a function of X (a step function over Ames feature groups),
  with the tower property shown as the group-means averaging back to the grand mean.
- Source: net-new (tower property / law of total expectation appears nowhere in any
  source).

## 5.4 The best predictor (~5 pp · net-new, MMSE seed)

- The prediction problem: choose a function g(X) to predict Y, minimizing the mean
  squared error E[(Y - g(X))^2].
- The result: the minimizer is g(X) = E[Y | X], the **conditional mean**. The
  conditional mean is the MSE-optimal predictor.
- Proof via the tower property and the orthogonality intuition: the prediction error
  Y - E[Y | X] is uncorrelated with every function of X, so no function of X can do
  better. Keep the orthogonality picture explicit; it is the same idea Ch 12 uses.
- **Explicit forward link to Ch 12.1 (the MMSE seed):** state in prose that Ch 12
  restricts the predictor to be *linear* in the observation, g(X) = a + B X, and
  recovers the linear MMSE estimator by the same orthogonality argument; this
  section is the unrestricted parent. Leave the door open to Ch 7's result that for
  jointly Gaussian variables the conditional mean *is already linear*, which is what
  makes the Gaussian case collapse the two.
- Figure: best-predictor / orthogonality schematic (Y, its prediction E[Y | X], and
  the error orthogonal to the space of functions of X).
- Source: net-new (the orthogonality/best-predictor result is the Ch 12 LMMSE seed
  and has no upstream source).

## 5.5 Implementation: conditional mean of Ames price given features (~6 pp · adapt + reframe + port L9/ANOVA notebook)

- Load Ames (port from the case-study ingest / HMD `Ames_Iowa_Housing_Prices-*`
  load).
- Compute the empirical conditional mean E[SalePrice | category] via pandas
  `groupby().mean()`, ported from the R `tapply(SalePrice, ExterQual, mean)` /
  `aggregate` in `05-04-Analysis_Of_Variance_ANOVA-r.ipynb`. **Reframed explicitly
  as the empirical conditional mean, not as a hypothesis test.**
- Show the tower property numerically: the group means weighted by group sizes
  return the grand mean (5.3 made concrete).
- **Predict from a partial record (net-new):** given a home with only some features
  known, return E[Price | known features] by conditioning on the available
  features; discuss what happens as more features are conditioned on (the prediction
  sharpens). Foreshadow LMMSE (Ch 12) and estimation from incomplete data (Ch 14.2) in one sentence each.
- Visualization: conditional mean of SalePrice as a function of the conditioning
  feature (group means with dispersion), so 5.3's "function of X" is something the
  reader sees.
- Checkpoint: an empirical-conditional-mean predictor that consumes a partial-record
  query and returns E[Price | known features].
- Source: adapt + reframe + port the ANOVA notebook (R to Python); the
  partial-record prediction is net-new.

## 5.6 Summary and exercises (~3 pp · net-new)

- "By the end" recap tied to the chapter's exit state (expectation operator;
  conditional distribution; E[Y | X] as a function of X; tower property; conditional
  mean as best predictor; empirical conditional mean on Ames).
- Exercises (write-from-blank; no usable L9 seed): operator algebra (verify
  E[AX] = A E[X] on a small matrix); a conditional-distribution computation; a
  tower-property verification; a short best-predictor argument; an Ames coding
  exercise extending the partial-record predictor to a new feature.
- Forward to Ch 6: the expectation operator is about to build the covariance matrix
  (covariance *is* an expectation); and a quiet pointer that 5.4's best predictor
  returns, restricted to linear, as the Ch 12 capstone.
- Source: net-new (L9's practice problems are covariance/transformation-flavored).

## Page budget

| Section | Pages |
|---|---|
| 5.1 The expectation operator | 4 |
| 5.2 Conditional probability and conditional distributions | 5 |
| 5.3 Conditional expectation and the tower property | 5 |
| 5.4 The best predictor (MMSE seed) | 5 |
| 5.5 Implementation: conditional mean of Ames price | 6 |
| 5.6 Summary and exercises | 3 |
| **Total** | **28** |

## Figures

- 5.1: E[AX] = A E[X] as a commuting square (apply-then-average vs
  average-then-apply).
- 5.2: the restricted-universe picture (sample space narrowed by the conditioning
  event).
- 5.3: E[Y | X] as a step function over Ames feature groups, with the tower property
  shown as group means averaging to the grand mean.
- 5.4: best-predictor / orthogonality schematic (error orthogonal to functions of
  X).
- 5.5: conditional mean of SalePrice as a function of the conditioning feature
  (group means with dispersion).

All SVG, in the chapter's `figures/` directory, in the established visual language.

## Dataset

**Ames housing** (the recurring hero). Loaded via the case-study ingest / HMD load.
The conditioning examples use categorical features (ExterQual, MoSold) where the
ANOVA notebook already computes group means; SalePrice is the target Y throughout.
No student submissions (PII).

## Open items for section-level work

- 5.1: settle the exact division of labor with Ch 4.4 when that chapter's outline is
  final; ensure Ch 4.4 carries the forward pointer so 5.1 is not a restatement.
- 5.2/5.5: choose the canonical conditioning feature for the worked thread (lean:
  ExterQual, an ordered categorical with a clean monotone price relationship)
  vs whether to also show a second feature (MoSold) for contrast.
- 5.4: decide how much orthogonality vocabulary to introduce here vs reserve for
  Ch 12 (lean: introduce the intuition and the word "uncorrelated," reserve the
  formal orthogonality-principle statement for Ch 12).
- 5.5: decide how the partial-record predictor handles a conditioning value with few
  or zero matching records (small-group instability), since this motivates the
  shrinkage/LMMSE story later; lean: name it as a limitation and point to Ch 12.
- 5.6: calibrate exercise count to the 3 pp budget once 5.1-5.5 prose lands.
