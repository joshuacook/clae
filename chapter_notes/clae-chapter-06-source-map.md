---
title: "Ch 6 Source Map"
type: chapter-source-map
chapter: 6
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 6 Source Map: Covariance, Correlation, and Cross-Correlation

Source Assembly for Ch 6. Gathered from `source/coverage-by-chapter.md`: course
L10 (Covariance), L11 (Variable Importance / Feature Scaling); Ames, wholesale,
stock_returns; HMD. Maps source to the book-outline sections with a reuse verdict,
then notes gaps. Feeds the Ch 6 notes+outline.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 6.1 From variance to covariance | L10 sec 1.1 (Sigma = E[(X-mu)(X-mu)^T]; entrywise definition; diagonal=var, off-diagonal=cov); L10 endnotes (population vs sample, n vs n-1) | the covariance matrix as an expectation, worked, with interpretation | adapt (strong); reframe off iris onto Ames |
| 6.2 Covariance matrix as statistical geometry | L10 sec 1.1 (PSD proof, symmetry proof, non-negative eigenvalues); L10 sec 1.0 + 2.1 (95% ellipse, eigenvectors as spread axes, eigenvalue ratio) | PSD/symmetry proofs; the spread ellipsoid; eigenstructure preview | adapt (strong); the proofs and ellipse picture are turnkey |
| 6.3 Correlation | L11 sec 2.2 (rho_ij = Cov/(sigma_i sigma_j); standardized covariance = correlation matrix R; proof; entries in [-1,1], diag=1) | normalization to correlation; the correlation matrix; proof | adapt (strong); pull from L11, not L10 |
| 6.4 Cross-correlation (between two random vectors) | **none** (L9 sec 3.4 only names "no cross-correlation terms" in passing; no definition, no example) | — | **net-new** (no source defines or works cross-covariance Cov(X,Y) between two distinct random vectors) |
| 6.5 Estimating covariance from data | L10 endnotes (sample covariance S, n-1 unbiasedness, E[S]=Sigma, large-n limit); L10 colab Prob 4 (sample-size simulation, 1/sqrt(n) error) | the sample covariance estimator; bias correction; convergence seed | adapt; the simulation is a Ch 8 (LLN) seed, keep it light here |
| 6.6 Implementation: cov/corr of Ames; cross-corr on stock_returns | Ames 05-05 (numeric_df.corr(), masked heatmap); wholesale 04-06 (.corr() heatmap, redundancy); L10 colab (np.cov, eigendecomp) | runnable correlation matrices + heatmaps on real data; np.cov usage | adapt for cov/corr; **cross-corr half is net-new** (stock_returns has no two-block structure) |
| 6.7 Summary and exercises | L10 colab Probs 1-4 (cov properties, eigen/noise, F-tests, simulation) | a starter exercise set | adapt as seed; drop the F-test problems (off-chapter) |

## Gaps and conflicts

- **6.4 cross-correlation is net-new and unsupported by data.** No source defines
  cross-covariance Cov(X,Y) between two *distinct* random vectors. L9 only mentions
  the phrase in passing. Worse, the assigned dataset **stock_returns.csv is a
  single 1000x10 matrix of generic `feature_1..feature_10` columns** (synthetic,
  no tickers, no dates, no sector labels exposed) — it is built for one covariance
  matrix / PCA, not for cross-correlating two named blocks. The "cross-correlation
  on stock_returns" implementation (6.6) requires inventing a two-block split
  (e.g. tech vs energy sectors) that the data does not label. Cross-correlation is
  a genuine write-from-scratch with a constructed example.
- **L10 is iris-based, not Ames.** Every worked number, ellipse, and figure in L10
  uses the iris dataset. Reuse the theory (definition, PSD/symmetry proofs, ellipse
  geometry) but **re-anchor all examples on Ames** per the book's hero-dataset thread.
- **Correlation lives in L11, not L10.** The covariance lesson (L10) never derives
  the correlation matrix; the rho = Cov/(sigma sigma) result and the
  standardized-covariance = R identity are in L11 (the feature-scaling lesson).
  Source for 6.3 must be pulled forward from L11.
- **Half of L10 is off-chapter.** L10 sec 3 (F-distribution, ANOVA F-tests across
  species), sec 4 (noise simulation, signal-to-noise), and the colab F-test problems
  are hypothesis-testing on iris species — not covariance/correlation/cross-corr.
  This belongs (if anywhere) to Ch 8 convergence or is dropped. Do not pull it into Ch 6.
- **L10 sec 2.1 over-reaches into PCA.** "Fundamental subspaces," rotate-to-align,
  98.8%-variance-explained, "effective rank," "motivates PCA" — this is the Ch 10
  payload. In 6.2 keep only the *preview* (eigenvectors = spread axes, eigenvalue =
  variance along axis); defer rotation/variance-explained/rank to Ch 10.
- **L11 is off-frame ML/sklearn.** L11's framing is feature-scaling-for-ML
  (StandardScaler, train/test leakage, logistic regression, min-max/robust scaling).
  Only sec 2.1-2.2 (standardization as a linear transform; the correlation identity)
  serve Ch 6 — and standardization-as-transform already belongs to **Ch 2.5**, so
  6.3 should cite only the correlation result and avoid re-teaching scaling.
- **HMD is not real source for Ch 6.** Despite the "HMD" tag in coverage, the HMD
  notebooks contain no `np.cov` / `.corr()` covariance work (grep is empty); they
  are impute/categorical/standardize/fit-predict. HMD does not feed Ch 6; the live
  Ames covariance/correlation source is the **Ames case study 05-05**, not HMD.

## Implication for the chapter outline

The seven-section sequence holds, but the source is **front-loaded and thinner than
"strong" implies**: 6.1, 6.2, 6.3 are turnkey adapts (with re-anchoring to Ames and
a pull of correlation from L11), while **6.4 cross-correlation is a true scratch
section** with no theory source and a dataset that does not natively support the
worked example. Two live decisions:

1. **Cross-correlation (6.4 + 6.6 half):** write the Cov(X,Y) theory from scratch
   and either (a) impose a documented two-block split on stock_returns, or (b) pull
   a different cross-correlation example. Flag stock_returns' generic-column,
   single-matrix shape as a mismatch with the "cross-correlation" framing.
2. **Scope discipline against PCA leakage:** L10's strongest, most polished material
   (sec 2.1, sec 4) is exactly the Ch 10 / Ch 8 payload. Hold 6.2 to a covariance-
   eigenstructure *preview*; route F-tests/noise to Ch 8 or drop.

Net assessment: Ch 6 is adapt-heavy on 6.1-6.3 and 6.5; net-new on 6.4 and the
cross-correlation implementation; and requires active re-anchoring (iris to Ames),
a cross-lesson pull (correlation from L11), and firm scope cuts (PCA and F-tests
out). Strong on covariance, genuinely scratch on cross-correlation.
