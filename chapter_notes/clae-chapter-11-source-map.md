---
title: "Ch 11 Source Map"
type: chapter-source-map
chapter: 11
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 11 Source Map: Least Squares Estimation

Source Assembly for Ch 11. Gathered from `source/coverage-by-chapter.md` (Ch 11
row): course L19 (planned, no file), Ames, ILA ch04 least squares + ch05
regularization, HMD fit/predict. The Ch 2 map flagged course lesson 004
("Linear Transformations") as the real four-fundamental-subspaces source aimed at
least squares; lesson 004 is therefore a primary source for THIS chapter. Maps
source to the book-outline sections with a reuse verdict, then notes gaps. Feeds
the Ch 11 notes+outline.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 11.1 The over-determined system | L004 (overdetermined systems n>p, worked 5x2 example, "no exact solution", `b` not in column space); L003 (Ax=b, column space, when solutions exist); Ames | the n>p framing, a clean toy system, the "best fit not exact" motivation | adapt (strong framing); port the price-vs-features motivation to Ames |
| 11.2 Geometry of least squares (projection onto column space; orthogonal residual) | L004 (column space = all `Ax`; LS = projection of `b` onto column space; left null space = residual directions); L003 (four subspaces, column ⊥ nullspace) | the geometric heart, exactly on-frame | adapt (strong) — the single best-matched section in the chapter |
| 11.3 The normal equations (derivation; minimizing the loss) | **none** (L004 names the projection but never derives A^T A x = A^T b; ILA ch04 empty) | — | **net-new** (the actual derivation and loss-minimization is unsourced) |
| 11.4 Computation (QR; SVD pseudoinverse; numerical stability) | **none** for QR/stability; Ch 9 SVD (in-book) supplies the pseudoinverse | pseudoinverse is forward-linked from Ch 9, not external source | **net-new** (QR, conditioning, numerical stability all from scratch) |
| 11.5 Regularization (ridge/Tikhonov; ML bridge) | HMD `lib/lm.py` + `boston_redux-01` (sklearn Ridge/Lasso/LinearRegression in a `make_pipeline`, alpha logspace grid search) on **Boston**; ILA ch05 regularization **empty**; L004 (regularization named as the fix for underdetermined p>n) | the *practice* of an alpha sweep and train/test scoring; ML-bridge motivation | adapt-the-code/reframe-the-math: the ridge **derivation** (A^TA+λI) is net-new; sklearn demo must be reframed as linear algebra and ported Boston→Ames |
| 11.6 *Implementation:* predict Ames sale price; pseudoinverse via SVD | HMD Ames notebooks (`-the_rest`, `-04-Round_2`) provide the Ames load/clean pipeline only; the *modeling* cells are DecisionTree/SVM + GridSearchCV on **Boston**, Python 2 | runnable Ames preprocessing; a sklearn fit/score harness | adapt heavily: write the `np.linalg.lstsq` / `pinv`-via-SVD Ames fit from scratch; reuse HMD only for data prep |
| 11.7 Summary and exercises | HMD scoring harness as exercise seed | a train/test-score loop | net-new; mostly from scratch |

## Gaps and conflicts

- **ILA ch04 and ch05 are empty stubs.** Both files are a title plus site
  boilerplate (`# The Least Squares` / `# Regularization and Optimization`,
  then `\pagebreak`; the `.html` is template chrome). The coverage table's
  "strong (via repos)" / "Ch 11 only joined this group via the ILA repo" is
  **wrong for Ch 11** — the ILA least-squares and regularization chapters carry
  zero content. The other ILA chapters cited nearby (ch02 systems, ch03 inner
  product) are TensorFlow-flavored and not usable LS source either.
- **L004 fits, and fits well.** The Ch 2 map's call was right: lesson 004 is the
  primary source for 11.1–11.2. It teaches overdetermined systems (with a worked
  5x2 toy), frames least squares as projection of `b` onto the column space, and
  ties residuals to the left null space — the geometric spine of the chapter.
  But it **stops at naming**: it never derives the normal equations, never shows
  the loss `||Ax-b||^2`, never computes a fit. L003 reinforces the four-subspaces
  framing (some overlap with L004).
- **The normal-equations derivation (11.3) is net-new.** No source minimizes the
  least-squares loss or derives A^T A x = A^T b. This is the analytic core of the
  chapter and is unsourced.
- **11.4 is net-new.** QR, the SVD pseudoinverse route, and numerical stability /
  conditioning have no external source; the pseudoinverse is forward-linked from
  the in-book Ch 9 SVD, which is the right internal dependency to lean on.
- **HMD is off-frame and Boston-flavored.** The only real regression code is
  sklearn pipelines (`lm.simple_alpha_grid_search`, `split_fit_score`) running
  Ridge/Lasso/LinearRegression **on Boston**, plus DecisionTree/SVM +
  GridSearchCV demos in Python 2. The Ames notebooks are preprocessing only
  (impute, categoricals, EDA) — there is **no LinearRegression/Ridge fit on Ames
  anywhere in HMD**. So the promised "Ames fit/predict pipeline" does not exist as
  least squares; it must be written. Reuse HMD for (a) Ames data prep and (b) the
  train/test-score and alpha-sweep *pattern*, reframed from sklearn to the
  pseudoinverse / normal equations.
- **No course lesson file.** L19 ("Linear Estimators") was planned but never
  produced, so there is no lecture-grade LS treatment to adapt; L004/L003 are the
  only course assets.

## Implication for the chapter outline

The section sequence holds; the source distribution does not match the "strong"
tag. The chapter splits cleanly:

- **Well-sourced (adapt):** 11.1 and especially 11.2 — lesson 004 gives the
  overdetermined framing and the projection-onto-column-space geometry almost
  turnkey. Anchor the chapter's opening on L004's n>p example, then move to Ames.
- **Net-new (write from scratch):** 11.3 (normal equations derivation), 11.4
  (QR / SVD-pseudoinverse / stability), and the *mathematics* of 11.5 ridge.
  These are the analytic core and are unsourced.
- **Reframe + port:** 11.5 and 11.6 — HMD supplies sklearn-on-Boston code and Ames
  *preprocessing*; the LS/ridge fit on Ames via `lstsq` and `pinv` must be
  authored, with HMD reused only for data prep and the score/alpha-sweep harness.

Net assessment: Ch 11 is **mis-tagged "strong via repos."** The repo source it was
credited to (ILA ch04/ch05) is empty, and HMD has no Ames least-squares fit. Real
strength is narrow and geometric (L004 → 11.1–11.2). The analytic spine (normal
equations, QR/pseudoinverse, ridge derivation) and the Ames implementation are
genuine write-from-scratch. Treat Ch 11 as **partial**, not strong: solid
geometric on-ramp, net-new estimation core. Forward dependency: lean 11.4 on the
in-book Ch 9 SVD pseudoinverse rather than any external source.
