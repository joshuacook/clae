---
title: "Ch 7 Notes: Gaussian Random Vectors"
type: chapter-notes
chapter: 7
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 7 Notes: Gaussian Random Vectors

Co-produced with `chapter_outlines/clae-chapter-07.md`, built from
`chapter_notes/clae-chapter-07-source-map.md`. The *why* behind the chapter.

## Role in the book

The theory engine of Part II and the chapter that plants the book's second
estimation seed. Ch 4 made the random vector; Ch 5 gave the conditional mean as
the best predictor (the MMSE seed); Ch 6 built the covariance matrix as
statistical geometry. Ch 7 puts a *distribution* on the random vector. The
multivariate normal is the one joint law where everything the book needs is
closed-form: marginals stay Gaussian, affine maps stay Gaussian, and, the
load-bearing fact, **the conditional mean is linear in the conditioner**. That
last result (7.4) is the explicit LMMSE seed paid off in Ch 12.4, where LMMSE,
MMSE, and the conditional mean collapse into one estimator in the Gaussian case.
The chapter is mostly net-new theory with a real-data skin on the back half.

## Entry and exit state

**Entry:** the reader has a random vector with a mean vector and a covariance
matrix (Ch 4, Ch 6), reads the covariance matrix as a spread ellipsoid via its
eigenstructure (Ch 6.2), knows the scalar normal PDF from a first probability
course, and can standardize and compute sample covariance on Ames (Ch 2, Ch 6).
Conditional expectation E[Y|X] as best predictor is in hand from Ch 5.

**Exit:** the reader can (1) write the MVN density and read its exponent as a
Mahalanobis quadratic form whose level sets are the Ch 6 covariance ellipsoid,
(2) state and use closure of the MVN under affine maps, (3) write the conditional
Gaussian mean and covariance and recognize the conditional mean as a linear
estimator (the LMMSE seed), (4) diagnose which Ames features are approximately
Gaussian and which are skewed, and (5) sample from and evaluate an MVN in code,
including an honest multivariate normality check on two correlated Ames features.

## Narrative arc

Recall the scalar bell curve (7.1), lift it to a vector by replacing the scalar
variance with the covariance matrix and the squared deviation with the
Mahalanobis quadratic form (7.2), so the density's level sets are exactly Ch 6's
ellipsoid. Then ask *why this distribution and not another*: because it is closed
under the linear maps the whole book runs on (7.3), affine in, affine out, still
Gaussian. Closure is the lever that makes the next result possible: condition one
Gaussian block on another and the conditional law is again Gaussian, with a mean
that is **linear** in the conditioner and a covariance that does not depend on the
observed value (7.4). That linear conditional mean is the estimator Ch 12 builds.
Having claimed all this, test it against reality: most raw Ames features are
*not* Gaussian (7.5), they are right-skewed, and a transform can restore
approximate normality. Then implement both halves separately (7.6), and close
(7.7). Each section earns the next: the quadratic form makes the density legible,
closure makes the conditional result reachable, the conditional result is the
spine, and the data sections keep the theory honest.

## Key decisions

- **7.4 is the chapter's center of gravity and the LMMSE seed** (per the
  decisions log and the source map). The conditional-Gaussian mean
  mu_X + Sigma_XY Sigma_YY^-1 (y - mu_Y) and covariance
  Sigma_XX - Sigma_XY Sigma_YY^-1 Sigma_YX appear in no source; this is
  true write-from-scratch and gets the largest theory budget. The notes flag the
  forward link explicitly: this is the same estimator form derived in Ch 12.3 and
  shown in Ch 12.4 to equal LMMSE and MMSE in the Gaussian case. Plant it quietly
  (one named forward pointer), do not pre-teach Ch 12.
- **7.2-7.4 are net-new theory; 7.1 is a brief recall.** Borrow only two figures
  from the Ch 6 lessons (L009/L010): the scalar normal PDF for 7.1, and the
  covariance ellipse plus Mahalanobis quadratic form for 7.2. The MVN density, its
  normalization constant and derivation, affine closure, and the conditional
  formulas are all written from scratch.
- **Split 7.6 into two visibly distinct halves** (source-map instruction). The
  net-new **MVN sampling/density** demo (synthetic then Ames) is a different claim
  from the adapted **Ames skew diagnostic**. Conflating them would imply the
  univariate skew plots validate the multivariate model, which they do not. The
  outline gives them separate sub-blocks with separate listings.
- **Add a genuine multivariate demonstration** the sources never provide: fit an
  MVN to two correlated Ames features, overlay the theoretical density ellipse on
  the scatter, sample from the fit, and check empirical Mahalanobis distances
  against the chi-square reference. This is the honest test of 7.2's *joint* claim
  on real data; the sources only ever test marginals.
- **7.5 grounds the univariate story only, re-sourced from Ames, not Boston.**
  Port the skew diagnostics from the Ames case study (`05-03-basic_eda`,
  `05-06-preprocessing`); cite HMD-02 only for the `scipy.stats.skew` table
  snippet. Use log / Box-Cox transforms to *show* non-Gaussianity and approximate
  restoration, but do not import the regularized-modeling apparatus around them.
- **Closure (7.3) is stated and proved at first-course altitude**, via the
  characteristic function or the affine-substitution argument, not measure theory.
  It is the load-bearing lemma for 7.4, so it gets a real (short) proof, not a
  citation.

## Source posture

Net-new on 7.1 (brief recall), 7.2 (density and constant), 7.3 (closure), 7.4
(conditional Gaussian), and 7.7. Adapt on 7.5 and the skew half of 7.6, ported
from the Ames case study to keep the hero dataset and stay out of the ML weeds.
The MVN sampling/density half of 7.6 is net-new. Cautions from the source map: no
course lesson on the normal distribution exists; the ILA repos are silent on Ch 7;
the real data confirms skew, not multivariate normality; HMD-02 is off-frame
(Boston, regularized models), reusable only for its skew table. The "partial"
coverage tag reads, honestly, as "mostly scratch with a real-data skin on
7.5/7.6." Detail in `chapter_notes/clae-chapter-07-source-map.md`.

## Forward and back wiring

- **Back:** uses Ch 4's random vector (mean vector, marginals), Ch 5's
  conditional expectation as best predictor (the MMSE seed 7.4 specializes), and
  Ch 6's covariance matrix and spread ellipsoid (7.2's level sets are exactly
  6.2's ellipsoid; the Mahalanobis form reuses Sigma^-1). Assumes the scalar
  normal PDF from a first probability course.
- **Forward:** 7.3 closure under affine maps is reused by the CLT in Ch 8.4
  (sums to Gaussian) and underwrites the Gaussian preservation through linear
  estimators in Part III. 7.4's linear conditional mean is the **LMMSE seed**,
  paid off explicitly in Ch 12.4 (LMMSE = MMSE = conditional mean in the Gaussian
  case) and built on in the Kalman arc (Ch 13-14), where the Gaussian assumption
  is what makes the predict-update recursion exact. 7.5's Gaussianity question
  feeds Ch 8.7's capstone (test Gaussianity on Ames) and informs PCA's
  interpretation in Ch 10.

## Engagement

The "aha" is twofold: the MVN density is *just* the scalar bell curve with the
variance replaced by the covariance matrix (7.2 makes the lift feel inevitable),
and the conditional mean being a straight line in the conditioner (7.4) is the
quiet reveal that an estimator was hiding in the distribution all along. The
honest-test multivariate Ames demo in 7.6 is the concrete payoff and the place
the reader sees theory meet messy data. Risk: 7.3-7.4 can read as formula
bookkeeping. Keep each result anchored to a picture (closure as the ellipsoid
transforming under A; conditioning as slicing the joint ellipsoid and reading off
where the slice centers) and to the running thread, *recover structure from noisy,
incomplete data*: the conditional mean predicts the unobserved block from the
observed one. Second risk: 7.5/7.6 could imply skewness invalidates everything;
frame it as "the model is an approximation, here is how good and how to improve
it," not as a debunking.

## Code plan

Extend the cumulative library (load, vector ops, transforms, covariance from
Ch 2/Ch 6). Two clearly separated implementation blocks in 7.6:

- **MVN sampling and density (net-new):** `np.random.multivariate_normal` to
  sample; `scipy.stats.multivariate_normal` for the density; a helper to draw the
  theoretical density ellipse (eigendecomposition of Sigma, chi-square radius) on
  a scatter. Start synthetic (a known mu, Sigma) so the picture is unambiguous,
  then fit to two correlated Ames features.
- **Ames skew diagnostic (adapt):** per-feature histogram or KDE with mean and
  median lines, a `scipy.stats.skew` table across numerical features, and a
  log / Box-Cox transform showing approximate normalization. Ported from
  `05-03-basic_eda` and `05-06-preprocessing`; HMD-02 only for the skew table.
- **Multivariate honesty check (net-new):** empirical Mahalanobis distances of
  the two-feature Ames sample against the chi-square(2) reference (Q-Q or
  histogram overlay). The honest test of 7.2 on real data.

Figures: scalar normal PDF (7.1, from L009); MVN density surface / contour and
the covariance ellipse with Mahalanobis levels (7.2, adapted from L010/L009);
closure as ellipsoid-under-A (7.3, net-new); conditioning as a slice of the joint
ellipsoid (7.4, net-new); Ames skew before/after transform and the two-feature
MVN-overlay scatter (7.5/7.6). Checkpoint: a fitted MVN on two Ames features with
its density ellipse and a chi-square Mahalanobis check.
