---
title: "Ch 6 Outline: Covariance, Correlation, and Cross-Correlation"
type: chapter-outline
chapter: 6
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 6 Outline: Covariance, Correlation, and Cross-Correlation

Co-produced with `chapter_notes/clae-chapter-06.md`. Section-level content plan,
budgets sum to ~32 pp. Source verdicts per section are in the source map.

## 6.1 From variance to covariance (~5 pp · adapt L10 sec 1.1)

- Recall variance as the expected squared deviation in one dimension; the question this chapter answers is how two dimensions vary *together*.
- Covariance of two components: Cov(X_i, X_j) = E[(X_i - mu_i)(X_j - mu_j)]; sign and meaning (positive, negative, zero).
- The covariance matrix as an expectation: Sigma = E[(X - mu)(X - mu)^T]; entrywise definition; diagonal entries are variances, off-diagonal entries are covariances.
- First worked example re-anchored to Ames: a small feature set (living area, lot area, year built, overall quality, sale price), the 5x5 Sigma read entry by entry.
- Population vs sample framed only as a flag here; the estimator is 6.5.

## 6.2 The covariance matrix as statistical geometry (~6 pp · adapt L10 sec 1.1 + 2.1, PCA-disciplined)

- Symmetry of Sigma (proof from the definition).
- Positive semidefiniteness: a^T Sigma a = Var(a^T X) >= 0 for all a (the proof); consequence, eigenvalues are non-negative (callback to Ch 3.4 spectral theorem).
- The spread ellipsoid: the level set of the quadratic form as the shape of the data cloud; the 95% ellipse picture re-anchored to a 2D Ames feature pair.
- **Eigenstructure preview (and only the preview):** eigenvectors are the axes of the ellipsoid, eigenvalues are the variance along each axis. Explicitly defer rotation-to-align, variance-explained, effective rank, and "this motivates PCA" to Ch 10.
- Figure: the spread ellipsoid with eigenvector axes on a 2D Ames pair (SVG).

## 6.3 Correlation (~4 pp · adapt L11 sec 2.2, pulled forward)

- Why normalize: covariance carries the product of its variables' units, so magnitudes are not comparable across pairs.
- The correlation coefficient: rho_ij = Cov_ij / (sigma_i sigma_j); proof that rho in [-1, 1] (Cauchy-Schwarz).
- The correlation matrix R: standardize the data (Ch 2.5 callback, do not re-teach), and the covariance of the standardized vector *is* R; diagonal is 1.
- Reading R on Ames: which features move together; cite only the correlation result from L11, avoid its scaling/ML framing.

## 6.4 Cross-correlation between two random vectors (~5 pp · net-new)

- The new question: given two *distinct* random vectors X (m-dim) and Y (p-dim), how do they covary?
- Cross-covariance: Cov(X, Y) = E[(X - mu_X)(Y - mu_Y)^T]; an m x p matrix, **not square, not symmetric**.
- The transpose relation: Cov(Y, X) = Cov(X, Y)^T; the cross-correlation matrix as the normalized form.
- How it sits inside the joint covariance of the stacked vector [X; Y]: a block matrix with Sigma_X, Sigma_Y on the diagonal and Cov(X, Y) off-diagonal.
- Worked example with a documented block split (see 6.6); state plainly that the partition is illustrative.
- Forward pointer (quiet): this is the object the LMMSE estimator is built from (Ch 12.3).
- Figure: the block structure of the joint covariance, showing the non-square off-diagonal cross-covariance (SVG).

## 6.5 Estimating covariance from data (~4 pp · adapt L10 endnotes + colab Prob 4, light)

- The sample covariance estimator S from a finite sample of n observations.
- Centering with the sample mean; why dividing by n - 1 (not n) gives an unbiased estimator, E[S] = Sigma (Bessel's correction, derived at first-course level).
- The estimate is itself a random object: it has its own spread, and it improves as n grows (1/sqrt(n) error named, not worked).
- **Forward pointer:** the sample-size simulation and the full convergence argument are the Law of Large Numbers (Ch 8.3); the Part II capstone (Ch 8.7) estimates the Ames covariance that Ch 10 consumes.

## 6.6 Implementation: covariance and correlation of Ames; cross-correlation on stock_returns (~6 pp · adapt for cov/corr, net-new for cross-corr)

- Build on Ch 2's standardized Ames feature matrix.
- Covariance matrix of the Ames feature set via centered data and `np.cov`; read it against 6.1's hand computation.
- Correlation matrix via `np.corrcoef` and via the standardize-then-covary identity (6.3); the two agree.
- The masked lower-triangle correlation heatmap on Ames (from case study 05-05): the scannable payoff.
- Eigendecomposition of the Ames covariance to recover the ellipse axes (6.2 preview, in code).
- **Cross-correlation half (net-new):** load stock_returns (1000x10, generic columns); impose the documented split, block X = columns 1 to 5, block Y = columns 6 to 10; compute the 5x5 Cov(X, Y) and its normalized cross-correlation; print the non-square shape. Text states the partition is illustrative, the columns carry no real-world labels.
- Checkpoint: an estimated Ames covariance matrix and correlation matrix (the object Ch 8.7 and Ch 10 consume).

## 6.7 Summary and exercises (~2 pp · adapt L10 colab Probs 1-4, F-tests dropped)

- "By the end" recap tied to the chapter's exit state (covariance matrix, its geometry, correlation, cross-covariance, estimation).
- Exercises: covariance properties (linearity, Cov(AX) = A Sigma A^T), an eigenstructure/spread problem, a correlation-reading problem on Ames, a net-new cross-covariance shape/transpose problem, and a sample-vs-population estimation problem. Drop the L10 F-test problems (off-chapter).
- Forward to Ch 7: this covariance matrix is the second parameter of the multivariate Gaussian; the spread ellipsoid becomes the Gaussian's level sets.

## Dataset

- **Ames housing** (hero): a small numeric feature set (living area, lot area, year built, overall quality, sale price) for the covariance/correlation worked examples, the spread ellipse, and the heatmap. Covariance source is Ames case study 05-05, not HMD.
- **stock_returns.csv** (1000x10, synthetic, generic `feature_1..feature_10`): the cross-correlation example, via the documented illustrative block split (X = cols 1-5, Y = cols 6-10). Flagged in the source map as a shape mismatch with the cross-correlation framing; the split is acknowledged in the text.

## Figures

- **Figure 6.1** Spread ellipsoid with eigenvector axes on a 2D Ames feature pair (SVG; the geometry "aha").
- **Figure 6.2** Block structure of the joint covariance of [X; Y], showing the non-square off-diagonal cross-covariance (SVG; net-new, supports 6.4).
- **Figure 6.3** Masked lower-triangle correlation heatmap of the Ames feature set (from case study 05-05; the scannable payoff in 6.6).

## Page budget summary

| Section | Pages |
|---|---|
| 6.1 From variance to covariance | 5 |
| 6.2 Covariance matrix as statistical geometry | 6 |
| 6.3 Correlation | 4 |
| 6.4 Cross-correlation between two random vectors | 5 |
| 6.5 Estimating covariance from data | 4 |
| 6.6 Implementation: Ames cov/corr; stock_returns cross-corr | 6 |
| 6.7 Summary and exercises | 2 |
| **Total** | **32** |

## Open items for section-level work

- 6.2: choose the exact 2D Ames feature pair for the spread ellipse (lean: living area vs sale price, the pair the reader most expects to be correlated).
- 6.4 / 6.6: confirm the stock_returns block split convention (cols 1-5 vs 6-10) and the exact illustrative-not-literal disclaimer wording; decide whether to normalize the cross-covariance to a cross-correlation matrix in the worked example or keep it as raw cross-covariance.
- 6.5: decide how much of the unbiasedness derivation to show vs state (lean: show the n-1 argument once, defer the convergence simulation entirely to Ch 8).
- 6.3: confirm correlation is presented strictly as a result, with the standardization mechanics referenced back to Ch 2.5, not re-derived.
