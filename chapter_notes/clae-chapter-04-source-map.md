---
title: "Ch 4 Source Map"
type: chapter-source-map
chapter: 4
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 4 Source Map: Random Vectors and Probability Spaces

Source Assembly for Ch 4. Gathered from `source/coverage-by-chapter.md`: course L9
(Random Vectors), Ames (home as a draw). Maps source to the book-outline sections
with a reuse verdict, then notes gaps. Feeds the Ch 4 notes+outline.

Reality check up front: the "strong" tag is generous. The only course source is one
lesson file, `009_math.md` ("Random Vectors and Their Statistical Properties"), with
**no companion colab** (009 has only `_math.md` plus a scanned notes PDF). That lone
file is half off-frame: much of it is covariance/correlation (Ch 6) and linear
transforms of random vectors that lean on Ch 2, and its worked data is **iris, not
Ames**. The chapter's own title promise, "Probability Spaces," has almost no source.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 4.1 From the vector to the random vector | L9 sec 1.1 (a row of a DataFrame as one random vector; dataset as a collection of draws); L9 sec 1.5 (random variable to 1D array, random vector to 2D array/DataFrame) | the "data row as a draw" framing; the bridge from Ch 1's data-vector to a random vector | adapt (strong on framing); port the weather-station/iris examples to Ames |
| 4.2 Probability spaces and random variables | L9 sec 0 (random variable as a function on a sample space; PMF/PDF; E and Var; die/sensor/binary examples) | a first-course-level definition of a random variable, distributions, expectation, variance | rewrite; **the chapter promises "probability spaces" (sample space, sigma-events, measure) and L9 never builds one** — it defines a random variable informally and moves on. Net-new framing needed |
| 4.3 Random vectors (joint dist; mean vector; marginals) | L9 sec 1.1, 2.1 (random vector defined; mean vector mu = E[X] as center of mass / first moment) | the mean vector and the random-vector object | adapt for the mean vector; **net-new: joint distribution and marginals are essentially absent in L9** (it jumps to covariance, not the joint law) |
| 4.4 Linear transformations of random vectors (how the mean transforms) | L9 sec 1.3 (E[AX]=A E[X], E[aX+bY]=aE[X]+bE[Y], worked); L9 sec 4 (transform iris, verify mean law) | the mean-transform law with a clean worked numeric example and a verification snippet | adapt (strong, turnkey). **Scope discipline: L9 sec 4 also derives Cov(Y)=A Cov(X) A^T and whitening/PCA — that belongs to Ch 6/Ch 10, defer it** |
| 4.5 Random vectors through data (Ames home as a draw; empirical vs theoretical) | L9 sec 1.1 framing only; Ames case study (`05-01-ingest`, `05-03-basic_eda`) | the conceptual draw; Ames load/EDA scaffolding | rewrite; **the Ames "home as a random draw" framing does not exist in source** — the Ames notebooks are an ML modeling pipeline (ingest, impute, EDA, ANOVA, PCA, regularization), never "a home is a sample from a population." Empirical-vs-theoretical is net-new |
| 4.6 *Implementation:* simulate random vectors; Monte Carlo | L9 sec 1.5 (`X.mean(axis=0)`, `np.cov`), sec 4.4 (standardize/whiten snippets) | numpy mechanics for mean/cov on stacked vectors | rewrite; **no Monte-Carlo / simulation code exists in L9** — it computes sample stats on given data, never simulates draws from a specified distribution. Simulation + Monte Carlo is net-new |
| 4.7 Summary and exercises | L9 Practice Problems 1-3 + full solutions (covariance analysis; mean/cov transform law; confidence ellipse on iris) | a ready starter problem set with worked solutions | adapt as seed; **P1 (covariance) and P3 (confidence ellipse) are really Ch 6/Ch 7 material**; port P2 (mean/cov transform) to Ch 4, repoint others |

## Gaps and conflicts

- **The title's "Probability Spaces" has no source.** L9 sec 0 gives an informal
  random-variable definition (function on a sample space) but never constructs a
  probability space (sample space + events + measure), and never reaches the
  first-course rigor the section name implies. 4.2 is effectively net-new.
- **Joint distribution and marginals are missing.** L9 names the random vector and
  jumps straight to first/second moments (mean, then covariance). The joint law and
  marginals (4.3) are net-new; only the mean vector is sourced.
- **L9 is half a Ch 6 lesson.** Roughly sections 2.2-2.4, 3.3-3.4, and 4.2 are
  covariance, the variance quadratic form, correlation, confidence ellipses, and the
  Cov(Y)=A Cov(X) A^T law. That is Ch 6 (Covariance/Correlation) and Ch 7 (Gaussian
  ellipsoids), not Ch 4. Ch 4 must take only the **mean** (first moment) and the
  **mean-transform** law, and hand the covariance content forward, or Ch 4 and Ch 6
  collide.
- **Iris, not Ames.** Every worked example and all three practice problems use iris
  (or a toy weather/temperature DataFrame). The chapter's Ames hero (4.5) is not in
  source and must be written; the Ames case-study notebooks are a supervised-learning
  housing-price pipeline, not a random-vector / sampling treatment.
- **No simulation source.** 4.6 asks for simulating random vectors and Monte Carlo;
  L9 only ever computes statistics on data already in hand. Net-new.
- **No colab.** Unlike most lessons, 009 has no `_colab.md`; code lives only as inline
  snippets inside `009_math.md` (plus a scanned PDF of handwritten notes, unusable as
  text source).
- **A "fundamental subspaces" thread** runs through L9 (sec 1.4, 2.3) mapping row/
  column/null space onto random vectors. It is speculative and partly wrong (e.g.
  "null space contains constant random variables"); do not carry it into Ch 4.

## Implication for the chapter outline

The section sequence holds, but the **source is far thinner than "strong" suggests**
and the chapter is genuinely adapt-light / net-new-heavy:

- **Adapt (real reuse):** 4.1 (data row as a draw) and 4.4 (mean-transform law, with
  L9's turnkey worked example) are the two solid pulls. 4.7 seeds from L9's problem
  set once repointed.
- **Net-new / rewrite:** 4.2 (probability spaces), the joint-law/marginals half of
  4.3, 4.5 (Ames-as-draw), and 4.6 (simulation/Monte Carlo). That is the bulk of the
  chapter.
- **Boundary discipline with Ch 6/Ch 7 is the live decision.** L9 wants to teach the
  whole second-moment story; Ch 4 must stop at the mean and the mean-transform law,
  explicitly deferring covariance, correlation, the spread ellipse, and the
  Cov(Y) law to Ch 6 (and the ellipsoid/confidence-region material to Ch 7). Tag L9
  sections 2.x-3.x and 4.2 as **primary source for Ch 6**, not Ch 4.

Net assessment: one course file, half of which belongs downstream; iris instead of
Ames; no probability-space construction, no joint law, no simulation. Treat Ch 4 as
**partial**, not strong: adapt 4.1/4.4/4.7-seed, write 4.2/4.5/4.6 and the joint-law
part of 4.3 from scratch, and guard the Ch 6 boundary hard.
