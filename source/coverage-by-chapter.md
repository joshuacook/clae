---
title: "CLAE Source Coverage by Chapter"
type: reference
status: active
created: "2026-06-24"
updated: "2026-06-26"
---

# Source Coverage by Chapter

Rewritten 2026-06-25 after book-wide Source Assembly (the per-chapter maps
`chapter_notes/clae-chapter-NN-source-map.md`). The earlier version's tags were
optimistic; this reflects what the source actually contains. A full read of all 14
math lessons and 48 case-study notebooks (2026-06-26) added the per-chapter
runnable-code inventory below.

Level: **adapt** = real usable source for the mechanics (still needs rewrite and
re-anchoring); **partial** = thin source, significant net-new; **scratch** =
little or none. The old "strong" tag is retired: every formerly-strong chapter is
adapt-the-mechanics, write-the-payload.

## Cross-cutting realities

- **The ILA repo is mostly empty stubs.** Only `introduction_to_linear_algebra`
  ch01 (elements), ch02 (systems), ch03 (inner product) have real (draft, often
  TensorFlow-flavored) content. ch04, ch05, ch07, ch08, ch09, ch10-12 are
  title-only stubs. Earlier credits to those chapters are vapor.
- **Course math lessons teach on iris and toy matrices, not Ames.** Re-anchoring
  worked examples to the Ames hero is pervasive net-new work. The Ames-native
  material lives in the case study notebooks (`lessons/case-study-05-ames/05-03`
  EDA, `05-04` ANOVA, `05-05` covariance, `05-06` preprocessing), not the math
  lessons and not HMD.
- **Course lessons leak across the book's chapter boundaries** (see per-chapter
  maps). Pull only the in-scope slice when drafting.
- **The estimation back half is essentially unsourced** (planned lessons 17-20 were
  never written), and its datasets were the wrong shape (see below).

## Part I: Linear Algebra Foundations

| Ch | Usable source | Net-new / key mismatch | Level |
|---|---|---|---|
| 1 Vector Spaces (skim-first ref, written last) | L1 (axioms, ops, R^2 geometry); ILA ch01/ch03 (numpy rep, draft) | bases/independence/dimension; ILA ch07 is an empty stub | partial |
| 2 Matrices | L2 (column picture, row/col views, systems, invertibility) | 2.3 geometric transforms + composition net-new; L4 mis-titled (it is the four subspaces, belongs to Ch 11); reframe 2.5 off ML/Boston to Ames | adapt |
| 3 Eigen | L7 (eigentheory, **2x2-only**, non-standard char-poly) | 3.4 spectral theorem + 3.5 power iteration net-new; ILA ch08 empty; L7 carries LU ballast (to Ch 2) | partial |

## Part II: Random Vectors and Statistical Structure

| Ch | Usable source | Net-new / key mismatch | Level |
|---|---|---|---|
| 4 Random Vectors | L9 (mean, the mean-transform law E[AX]=AE[X]) | probability spaces (4.2), joint law/marginals (4.3), simulation (4.6) net-new; L9 is iris and half-belongs to Ch 6/7 | partial |
| 5 Expectation & Conditional | L9 expectation scrap (for 5.1); Ames ANOVA group-means (R, for the conditional-mean hook) | all conditioning (5.2-5.4) net-new (zero "conditional" anywhere); 5.4 is the MMSE seed | scratch |
| 6 Covariance | L10 (covariance theory, iris); L11 (correlation identity); case-study 05-05 (Ames covariance) | 6.4 cross-correlation net-new; stock_returns has no sector labels; HMD has no covariance code | partial |
| 7 Gaussian | Ames skew diagnostics (case-study 05-03/05-06, univariate) | MVN density/closure/conditional-Gaussian (7.2-7.4) net-new; 7.4 is the LMMSE seed; only iris MVN pictures exist (in Ch 6 lessons) | scratch |
| 8 Convergence (LLN/CLT) | wholesale CLT notebook (informal, conflates LLN/CLT); stock_returns generator (known Sigma) | nearly all net-new; simulation-only, no measure theory | scratch |

## Part III: Linear Estimation

| Ch | Usable source | Net-new / key mismatch | Level |
|---|---|---|---|
| 9 SVD | L12 front half (what the SVD is) | 9.5 Eckart-Young + low-rank recovery net-new; L12 leaks covariance (Ch 6) and PCA (Ch 10); ILA ch08 empty; re-ground on image_features | adapt (front) / scratch (payload) |
| 10 PCA (capstone) | pca-tutorial (deep); wholesale; project-1 (estimation framing) | L13 empty, L14 skeleton, ILA ch09 stub; eigen-vs-SVD and n vs n-1 conflicts; 10.3/10.4/10.6 net-new; capstone-data mismatch (project-1 is synthetic, not Ames; wholesale "segmentation" is GMM not PCA; no worked Ames PCA) | partial |
| 11 Least Squares | L4 (over-determined systems, projection onto column space, the four subspaces) | **ILA ch04/ch05 are empty (the "strong" basis was vapor)**; normal equations (11.3), pseudoinverse/QR (11.4), ridge derivation (11.5) net-new; HMD is Boston/sklearn/Py2 | partial |
| 12 Linear MMSE (capstone) | none (in-book seeds Ch 5.4, Ch 7.4) | every section net-new; uses the new tracking dataset (one-shot LMMSE); needs Ch 5.4 + 7.4 written first | scratch |

## Part IV: Applications

| Ch | Usable source | Net-new / key mismatch | Level |
|---|---|---|---|
| 13 Estimation in Signal Processing | none | every section net-new; scalar/recursive Kalman on the new tracking dataset; extends Ch 12 | scratch |
| 14 Advanced Filtering | none (ILA ML chapters are empty stubs) | every section net-new; full 2D Kalman on the tracking dataset; 14.5 ML bridge extends Ch 10.6/11.5 | scratch |

## Datasets

- **Ames housing** (`lessons/case-study-05-ames`): the real-world hero, but only as
  an ML pipeline; every random-vector/covariance/Gaussian/PCA framing of it is
  net-new. Threads Ch 1-2, 4, 6, 7, 10-11.
- **image_features** (rank-3 + noise, confirmed): Ch 3 and Ch 9 rank recovery, Ch 10.
- **stock_returns** (synthetic, Sigma[i,j]=0.7^|i-j|, no labels): Ch 8 convergence
  (known covariance is the asset); Ch 6 cross-correlation needs an invented split.
- **sensor_readings** (i.i.d., logspace-scaled, no dynamics): Ch 9/10 scale
  normalization only. **Not** for the estimator arc.
- **tracking** (to author): linear-Gaussian constant-velocity state-space, GT
  AI-for-Robotics style. The Estimator-arc dataset for Ch 12-14. See the decision
  in `clae-book-decisions.md`.

## Runnable code inventory (ground truth, full read 2026-06-26)

Where each chapter's runnable code actually lives, after a full read of all 14 math
lessons and 48 case-study notebooks. The math lessons (L001-L014) are toy-matrix and
iris; they give mechanics plus small reusable helpers. The real-data, runnable
computation lives in the case-study notebooks. The book's distinctive authoring task
is **welding the from-scratch numerical derivation onto Ames**: the course's
from-scratch covariance / PCA / SVD code runs on iris / ball-on-spring / wholesale,
while the Ames pipeline uses sklearn (no hand SVD or eigendecomposition anywhere).
Computing covariance, PCA, and least squares on the Ames data matrix by hand (numpy)
is net-new and is the computational spine of the book.

| Ch | Lessons (mechanics + helpers) | Case-study notebooks (runnable, real data) | Key reusable artifacts |
|---|---|---|---|
| 1 | L001 (add/scale/subtract, dot product; `plot_vector`/`vector_addition` quiver helpers), L002 (column picture; difference matrix `[[1,0,0],[-1,1,0],[0,-1,1]]`), L003 (`are_independent` rank test) | 05-01 ingest (three-CSV `pd.merge` on `Id` to a 1460x80 data matrix; target `SalePrice` in `sale.csv`) | `plot_vector`/`vector_addition`; row-vs-column `Ax` loop; `are_independent`; `load_data()` |
| 2 | L002 (column picture, `Ax=b`, invertibility, `np.linalg.solve`; difference matrix), L005 (transformation = matrix; `points @ A.T`) | 05-06 preprocessing (standardize/center as a transform) | row-vs-col `Ax` loop; `plot_vectors` (3D); `plot_transformation` |
| 3 | L007 (eigen: char-poly **2x2-only, determinant-free, bespoke "dependency trick"**; eigenspaces/multiplicity; LU; diagonalization) | - | meshgrid `points @ A.T` eigen viz (little other code) |
| 4-5 | L009 (random-vector-as-DataFrame-row; `E[AX]=AE[X]`, `Cov(AX)=A Cov(X) A^T` with `np.allclose` checks; confidence ellipse) | 05-02 impute (column means), 05-04 ANOVA group means (conditional-mean hook) | mean/cov-transform verification; ellipse code |
| 6 | L010 (covariance, PSD proofs, signal/noise via eigenvalue ratio; `compare_covariance`, `simulation_study`), L011 (standardization to correlation) | 05-05 Ames `numeric_df.corr()` + masked heatmap; wholesale 04-06 (correlation matrix); **pca-tutorial 04** (covariance from `X_c.T@X_c/(n-1)`, TSS, ddof); **pca-tutorial 06** (cov /(n-1) vs corr /n, `np.testing` proofs) | `.corr()`+mask; `X_c.T@X_c/(n-1)`; cov-vs-corr scaling |
| 8 | - | **wholesale 04-05** (10,000-trial Monte-Carlo CLT, sample-mean convergence), 04-04 (z-score standardization), 04-03 (sampling variability vs n) | the CLT simulation loop; z-score line |
| 9 | L012 (`np.linalg.svd`, `full_matrices=False`; verification block `U^T U=I`, reconstruction, `s**2/(n-1)`=cov eigenvalues, `V`=eigvecs(`X^T X`); SVD-from-eigh; "square-root pattern" `sigma=sqrt(lambda)`) | - (no SVD or eig on Ames anywhere) | `np.linalg.svd` + verification; SVD-from-eigh |
| 10 | L010/L012 (cov->PCA, SVD) | **pca-tutorial 06** (PCA = eigendecomp of population covariance; 5-step algorithm; `assert_array_almost_equal(pca.components_.T, eig(X_c.T@X_c/n))`), 02 (geometric: principal axes = max-variance directions; projection/inverse_transform), 05 (eig of cov, SNR, change of basis), 08 (scree, cumulative variance, scaling-dependence), 07 (loadings, sign convention); 05-08 sklearn `PCA(8)` on Ames; wholesale 04-09 (sklearn PCA across variants) | `np.linalg.eig(X.cov())` with proofs; `explained_variance_ratio_`; scree |
| 11 | L004 (over/underdetermined; four subspaces; `np.linalg.lstsq` + residual norm; `decompose_solution` via `pinv`) | 05-10 (normal equation `beta=(X^T X)^{-1} X^T y` in LaTeX), **05-11** (Ridge/Lasso on `dataset_2`: closed form `np.linalg.inv(X.T@X+alpha*I)@X.T@y`, GridSearchCV, coefficient paths), 05-13 benchmark (mean baseline) | `lstsq`+residuals; ridge closed-form; the Ames OLS/ridge fit |
| 12-14 | - | - | no source; write from scratch on the `tracking` dataset |

Notes:

- **pca-tutorial is a fully-expanded dir, not a zip.** Notebook 06 is the single best
  artifact in the corpus (PCA from first principles with passing `np.testing`
  assertions); notebook 04 is the cleanest first-principles covariance.
- **Three divergent `plot_vector` copies** across L001/L002/L004 (2D quiver, 3D, a
  labeled variant); unify on one figure helper book-wide.
- **L007 eigen is 2x2-only** with a determinant-free derivation ("we would be unlikely
  to do this for anything of higher dimension"); Ch 3 must generalize to
  `det(A - lambda I)=0`.
- **Dated code to modernize on lift:** `sns.distplot` -> `histplot`/`displot`;
  `sklearn.externals.six`/`joblib` in `lib/preprocessing.py`; one undefined
  `fit_and_score` in wholesale 04-12.
- **Ch 12-14 confirmed unsourced** (no course or notebook material); written entirely
  on the `tracking` dataset.

## The shape of the work

- **adapt (mechanics, then rewrite + re-anchor to Ames):** Ch 2, Ch 9 front half.
- **partial (real on-ramp, net-new payload):** Ch 1, 3, 4, 6, 10, 11.
- **scratch (write from blank):** Ch 5, 7, 8, 12, 13, 14, and Ch 9's payload.

The estimation half (Ch 5, 7, 8, 12-14) is where the book is genuinely written, not
adapted. Strong-looking front chapters still need their worked examples rebuilt on
Ames. Per-chapter detail and mismatches: the source maps.
