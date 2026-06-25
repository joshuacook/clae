---
title: "Ch 7 Source Map"
type: chapter-source-map
chapter: 7
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 7 Source Map: Gaussian Random Vectors

Source Assembly for Ch 7. Coverage tag is **partial** (`source/coverage-by-chapter.md`):
Ames grounds the Gaussian-vs-skew story; the multivariate-normal theory is net-new.
Verification result: the tag is **slightly optimistic**. There is NO course lesson on
Gaussian vectors (lessons present are 001-005, 007, 009-014; none is dedicated to the
normal distribution), and the GitHub repos contribute nothing to the theory (ILA has
zero Gaussian/MVN content). The grounding that exists is real but lives in the
covariance lessons (L009/L010) and in skew-diagnostic notebooks, and the only
quantitative skew/normalization pipeline cited in the row (HMD `skew_normal_standardized`)
is Boston, not Ames. An Ames-native skew path does exist in the case study. Maps source
to the book-outline sections with a reuse verdict, then notes gaps.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 7.1 The univariate normal, recalled | L009 (normal PDF, drawn as a TikZ figure; first-course probability framing) | the scalar bell curve and PDF; a recall hook | adapt as a brief recall; mostly **net-new** prose (assumed from the first probability course) |
| 7.2 The multivariate normal (density; mean and covariance; the ellipsoid) | L010 (the covariance ellipse on iris: 95% confidence region, eigenvector axes, mean as center); L009 (level sets are ellipsoids; the Mahalanobis quadratic form (x-mu)^T Sigma^-1 (x-mu) drawn on iris with chi-square levels) | the ellipsoid geometry and the quadratic-form exponent, already visualized | adapt the **geometry**; the MVN density formula, normalization constant, and its derivation are **net-new** |
| 7.3 Why Gaussian dominates (closure under linear maps; tractability) | **none** | — | **net-new** (no source proves or states closure of the MVN under affine maps) |
| 7.4 The conditional Gaussian (conditional mean linear in the conditioner; LMMSE seed; conditional covariance) | **none** | — | **net-new** (the conditional-Gaussian formulas are absent everywhere; this is the load-bearing estimation result of the chapter) |
| 7.5 Gaussian vs real data (which Ames features are Gaussian, which are skewed) | Ames case study `05-03-basic_eda` (SalePrice right-skew, KDE + mean-vs-median skew read); Ames case study `05-06-preprocessing` (skew-normalization: log and Box-Cox, Gelman scaling); Ames `04-Round_2` nb (per-feature distplots, "heavily skewed" callouts); HMD `boston_redux-02-skew_normal_standardized` (systematic skew table via scipy.stats.skew, BoxCoxTransformer) | real-data skew diagnostics + normalization technique | adapt (strong on the **diagnostic** side); **off-frame** (see gaps): HMD is Boston/ML; reframe and prefer the Ames-native path |
| 7.6 *Implementation:* MVN sampling/density; Ames Gaussian-vs-skew | for Ames skew: `05-03`/`05-06` and HMD-02 (skew table, log/Box-Cox, KDE plots, mean/median lines); for **MVN sampling/density: none** | runnable skew diagnostics on real data | adapt the skew half (port to Ames); the MVN-sampling/density half (np.random.multivariate_normal, scipy multivariate_normal, drawing the density ellipse) is **net-new** |
| 7.7 Summary and exercises | none | — | **net-new** |

## Gaps and conflicts

- **No Gaussian lesson exists.** Confirmed: there is no course lesson on Gaussian
  vectors or the normal distribution. The book row's "course lessons" cell is correctly
  empty. Every normal/MVN mention in the lessons is incidental, inside the covariance
  material (L009 random vectors, L010 covariance) which is the Ch 6 source, not a Ch 7
  source. So the chapter borrows two figures' worth of geometry from Ch 6's lessons and
  writes the rest.
- **The theory core (7.2 density, 7.3 closure, 7.4 conditional Gaussian) is net-new.**
  The single most important result for the book's spine, the **conditional-Gaussian
  mean/covariance** (the explicit LMMSE seed that 12.4 pays off), appears in NO source.
  This is true write-from-scratch and is the chapter's center of gravity.
- **The grounding is qualitative, not quantitative-MVN.** What Ames/HMD actually
  supply is **univariate, marginal** skew diagnostics (per-feature histograms, skew
  coefficients, log/Box-Cox normalization), i.e. "is this one feature bell-shaped." None
  of it tests or visualizes **joint/multivariate** normality (no joint density contour,
  no Mahalanobis Q-Q, no chi-square test of the quadratic form). So the data grounds
  7.5 ("which features are skewed") but does not ground 7.2's *multivariate* claim. The
  one multivariate-normal picture in any source is L010's iris confidence ellipse, on
  iris, not Ames.
- **HMD-02 is off-frame (Boston, ML/regularization).** `boston_redux-02-skew_normal_standardized`
  is the only source the coverage row names, and it is Boston housing, framed entirely
  toward regularized linear models (Lasso/Ridge pipelines, alpha grid search). Its
  reusable nucleus is small: the `scipy.stats.skew` table and the Box-Cox idea. Prefer
  the **Ames-native** skew path (`05-03-basic_eda`, `05-06-preprocessing`) so the chapter
  stays on the Ames hero dataset and out of the ML weeds; cite HMD-02 only for the
  skew-table snippet.
- **Box-Cox / log-normalization is a tangent risk.** The Ames and HMD skew material is
  really *preprocessing for regression* (make features model-ready), not *testing a
  Gaussian model of the data*. 7.5's job is the latter. Use the transforms to **show**
  that raw Ames features are non-Gaussian and that a transform can restore approximate
  normality, but do not import the regularized-modeling apparatus around them.
- **ILA contributes nothing.** No Gaussian, multivariate normal, or normal-distribution
  content in any ILA chapter. The repos are silent on Ch 7.

## Implication for the chapter outline

The section sequence holds, but the partial tag should be read as **"mostly scratch with
a real-data skin on 7.5/7.6."** Concretely:

- **7.1-7.4 are net-new theory.** Borrow only two figures from the Ch 6 lessons: the
  scalar normal PDF (L009) for 7.1, and the covariance-ellipse + Mahalanobis quadratic
  form (L010/L009) for 7.2. Everything else (MVN density and its constant, affine closure
  in 7.3, the conditional-Gaussian formulas in 7.4) is written from scratch. Treat 7.4 as
  the chapter's spine and budget accordingly; it is the explicit LMMSE seed for Ch 12.
- **7.5/7.6 are the only adapt-able sections, and they ground only the univariate
  story.** Port the skew diagnostics to **Ames** (`05-03`, `05-06`), not Boston. Add a
  net-new **multivariate** demonstration the sources do not provide: sample from an MVN
  fit to two correlated Ames features, overlay the theoretical density ellipse on the
  scatter, and check the empirical Mahalanobis distances against chi-square. This is the
  honest test of 7.2 on real data and currently has no source.
- **Section-structure note:** consider splitting the implementation so the **MVN
  sampling/density** demo (net-new, synthetic-then-Ames) is visibly distinct from the
  **Ames skew diagnostic** (adapted). They are different claims (here is what a Gaussian
  vector *is* vs is Ames *actually* Gaussian) and conflating them in one 7.6 risks
  implying the skew plots validate the MVN model, which they do not.

Net assessment: Ch 7 is **net-new on 7.1-7.4 and 7.7** (the theory and the chapter's
estimation payload), **adapt on 7.5/7.6 but univariate-only and best re-sourced from Ames
rather than the cited Boston notebook**. The "partial" tag is right in spirit but
overstates the grounding: the real data confirms skew, not multivariate normality, and
the chapter's load-bearing result (conditional Gaussian) has no source at all.
