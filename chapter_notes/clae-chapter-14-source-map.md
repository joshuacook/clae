---
title: "Ch 14 Source Map"
type: chapter-source-map
chapter: 14
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 14 Source Map: Advanced Filtering and Modern Applications

Source Assembly for Ch 14 (the estimator finale; tagged **scratch** in
`source/coverage-by-chapter.md`). Gathered from the course lessons
(001-005, 007, 009-014), the project-1 materials, the `sensor_readings`
dataset, and the three `~/working/clae-refs/` repos (ILA, HMD, PCAt). Maps
source to the book-outline sections with a reuse verdict, then notes gaps.
This chapter completes the Ch 12 (static LMMSE) -> Ch 13 (scalar Kalman) ->
Ch 14 (full Kalman) estimator arc; it is also the book's terminal chapter, so
the forward-pointing material is net-new by necessity. Feeds the Ch 14
notes+outline.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 14.1 The full multivariate Kalman filter (state/measurement models; matrix recursions) | **none** | — | **net-new.** No lesson, repo, or handout teaches state-space models or the Kalman recursions. The matrix-algebra prerequisites (covariance, inverse, PSD) come from Ch 6/9/12, not from any Ch 14 source |
| 14.2 Estimation through gaps (tracking through missing measurements) | **none** | — | **net-new.** No source treats missing-data filtering. Builds on 14.1 by skipping the measurement-update step; conceptual, no asset |
| 14.3 Adaptive filtering (LMS/RLS; unknown model) | **none** | — | **net-new.** No source on stochastic-gradient or recursive-least-squares filters. RLS connects back to Ch 11 least squares (recursive form) and Ch 13's recursive LMMSE, but those are CLAE-internal callbacks, not external source |
| 14.4 Further directions (system identification; communications, brief) | **none** | — | **net-new, deliberately brief.** Survey-level; no source. Scope decision (below) holds this to a short "where next" pointer, not a full treatment |
| 14.5 The ML bridge (modern filtering; learned dynamics; sequence models) | **none usable.** ILA ch09-12 (unsupervised / NLP / non-linearity-kernels / deep learning) are **empty title-only stubs** (heading + `\pagebreak`, ~30-40 bytes each); ILA ch01 is TensorFlow-flavored but unrelated | — | **net-new.** The prompt flagged ILA's "later ML chapters" as a possible 14.5 source; confirmed they contain no prose. Reuse the *thread* established in Ch 10.6 (PCA->ML) and Ch 11.5 (regularization->ML), but written fresh |
| 14.6 Project capstone, Build a Kalman Filter (extend Ch 13's estimator) | `sensor_readings.csv` (the only Ch 12-14 dataset asset); project-1 handouts as a *structural* template only | a 1000x10 numeric matrix; a project scaffold pattern | **net-new with a data conflict (see Gaps).** project-1 is a PCA/SVD project, not a filtering project; `sensor_readings` as generated has no time dynamics. The capstone must impose a state-space model the data was not built to carry |
| 14.7 Summary and exercises | course lessons' "additional resources" pattern; project-1 milestone structure | a format template | adapt as seed; content net-new |

## Gaps and conflicts

- **The whole chapter is net-new.** Confirmed absence of any estimation /
  filtering source: the course lesson set runs 001-005, 007, 009-014 with no
  Kalman, MMSE, adaptive-filtering, or state-space lesson (the syllabus
  *planned* L17-L20 = CLT / LLN / linear estimators / MMSE, but no files were
  ever produced). No repo and no project handout fills this in. Ch 14 is a
  write-from-blank chapter, as the "scratch" tag promises.

- **`sensor_readings` does not match its Kalman framing (central conflict).**
  The dataset README and the book outline both describe `sensor_readings` as
  "1000 timestamps, 10 sensors" of IoT time-series, the substrate for "the
  full multivariate Kalman filter." But `generate_datasets.py` builds it with
  `generate_scale_varying_data`: 1000 rows of **i.i.d. multivariate normal**
  draws, each feature scaled by a `logspace(-2, 2, 10)` factor. There is **no
  time index, no autocorrelation, no state-transition dynamics** — the rows are
  exchangeable. As generated, the data was designed to demonstrate
  *scale-varying covariance for PCA normalization* (its real project-1 role),
  not temporal filtering. A Kalman filter run on it has nothing to track. This
  is the same dataset Ch 12 uses for static LMMSE, where i.i.d. rows are
  exactly right; the conflict is specifically with Ch 13/14's dynamic framing.

- **project-1 is a PCA/SVD project, not the "Estimator" project.** The prompt
  frames project-1 as feeding a "full multivariate Kalman filter ... the
  Estimator finale." In fact project-1 (`project-1.yaml`,
  `final_handout.md`, `milestone1/2_handout.md`) is titled *"Statistical
  Estimation through SVD Analysis"* and its deliverables are sample-covariance
  derivation, scaling analysis, direct-SVD-vs-sklearn-PCA, scree plots, and
  component selection. It is the Ch 10 PCA capstone's source, not Ch 14's. Its
  only use for Ch 14 is the *milestone/deliverable structure* as a template for
  the 14.6 capstone write-up.

- **No ML source for 14.5.** ILA ch09-12 are stubs (title + pagebreak only),
  so the "learned dynamics / sequence models" bridge has no external grounding.
  The only available material is the book's own ML-bridge thread (Ch 10.6,
  Ch 11.5).

## Implication for the chapter outline

The seven-section sequence holds, and the scope decision recalled in the prompt
is the right one: the **spine is the multivariate Kalman filter (14.1-14.2) plus
adaptive filtering (14.3)**; system identification and communications (14.4) are
a deliberately brief "further directions" pointer; the ML bridge (14.5) closes
by extending the Ch 10/11 thread rather than introducing new machinery. Nothing
in the source argues for re-weighting; there is no source to re-weight.

The one live decision is the **14.6 capstone data**. Because `sensor_readings`
has no dynamics, the chapter cannot simply "run a Kalman filter on the data."
Two clean options (no fallback hacks):

1. **Author a small dynamic dataset for the Ch 13-14 arc** — a linear-Gaussian
   state-space simulation (constant-velocity or constant-acceleration target,
   a known transition matrix F, process noise Q, measurement matrix H,
   measurement noise R), generated the same way `generate_datasets.py` makes
   the others. This gives a ground-truth trajectory to track, makes "estimation
   through gaps" (14.2) demonstrable by dropping measurements, and lets the
   capstone *recover known dynamics* — the cleanest pedagogy and consistent
   with the book's synthetic-data-with-known-structure pattern. Recommended.

2. **Reinterpret `sensor_readings` rows as a time index** and impose a
   random-walk / slowly-drifting-mean state model on top. This keeps the
   "recurring dataset" promise but is a stretch: the generated rows are
   independent, so a filter will find no real temporal structure to exploit and
   the demo will under-deliver. Only viable if the "one dataset across Ch 12-14"
   continuity is judged more important than the filtering payoff.

Recommendation: option 1. Plant the new state-space dataset in Ch 13 (where the
scalar Kalman filter is introduced) and extend it to the multivariate case in
Ch 14.6, so the Estimator arc tracks a single, honestly-dynamic system from Ch
13 into Ch 14. Keep `sensor_readings` for the Ch 12 static-LMMSE capstone, where
its i.i.d. structure is correct.

Net assessment: Ch 14 is net-new across every section. There is no course or
repo source to adapt; the only reusable assets are the book's own internal
threads (LMMSE -> Kalman from Ch 12-13; the ML bridge from Ch 10-11) and the
project-1 milestone *format*. The headline risk is not missing prose but a
dataset mismatch: the chapter's nominal hero dataset has no dynamics, so the
filtering capstone needs a purpose-built linear-Gaussian state-space dataset.
