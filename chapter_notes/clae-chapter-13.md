---
title: "Ch 13 Notes: Estimation in Signal Processing"
type: chapter-notes
chapter: 13
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 13 Notes: Estimation in Signal Processing

Co-produced with `chapter_outlines/clae-chapter-13.md`, built from
`chapter_notes/clae-chapter-13-source-map.md`. The *why* behind the chapter.

## Role in the book

The chapter where the book's estimation arc goes dynamic. Chapter 12 built the
**static** Linear MMSE estimator: one shot, estimate X from a fixed set of
observations Y, error orthogonal to the data. Chapter 13's entire job is to take
that estimator and make it **recursive**, so that each new measurement corrects a
running estimate instead of re-solving from scratch. The destination is the
**scalar Kalman filter**, presented as "LMMSE done online." This is the middle
chapter of the three-chapter Estimator spine (static LMMSE in Ch 12, recursive
scalar filter here, full multivariate Kalman in Ch 14). It is the first chapter
to put time inside the estimate.

## Entry and exit state

**Entry:** the reader has the Ch 12 static LMMSE estimator in hand: the
orthogonality principle (error orthogonal to the data), the LMMSE estimator in
covariance and cross-covariance form, the **LMMSE gain** that weights the
observation, and the error-covariance bookkeeping that says how good the estimate
is. The reader also has Ch 6 covariance/cross-covariance, Ch 7 the Gaussian
conditional mean, and basic numpy from every prior implementation section. No
signal-processing, time-series, or state-space background is assumed.

**Exit:** the reader can (1) write a scalar signal as a **state-space model**
(state evolves, measurements are noisy reads of the state), (2) name and
distinguish the three estimation tasks (filtering, prediction, smoothing), (3)
rederive the Ch 12 LMMSE estimate as a **sequential update**, recognizing that the
running estimate need only be corrected, not recomputed, (4) run the scalar Kalman
**predict-update cycle** by hand and in code, with the Kalman gain understood as
the Ch 12 LMMSE gain in sequential dress, and (5) track a one-dimensional moving
target from noisy measurements in numpy, watching the filter converge and the error
variance settle.

## Narrative arc

Static to dynamic, then static-online to closed-form recursion. First the pivot:
Chapter 12 estimated a fixed quantity; real signals **move**, so we put the
estimand inside a **state** that evolves in time and observe it through noise
(13.1, the state-space model). Then we name what we can ask of a moving signal:
estimate the present from data up to now (filtering), the future (prediction), the
past (smoothing) (13.2). Then the load-bearing move: rather than re-solve the full
LMMSE problem at every new sample, we **update** the previous estimate with the new
measurement, and we show this online form is exactly the Ch 12 LMMSE answer, just
reorganized (13.3, recursive estimation). That recursion, specialized to the
linear-Gaussian state-space model, has a clean closed form: the **predict-update
cycle** of the scalar Kalman filter, where the **Kalman gain** is the LMMSE gain
computed against the predicted error variance (13.4). Finally we run it on a real
moving target (13.5) and close (13.6). Each section earns the next: the state-space
model makes the three tasks definable; the three tasks make "filtering" the thing
we recursively compute; recursion makes the predict-update cycle inevitable.

## Key decisions

- **The chapter is the purest scratch in the book; build entirely from the in-book
  Ch 12 -> Ch 13 dependency.** The source map confirms zero external source for any
  section (no course lesson, no ILA chapter, no clae-refs notebook touches
  recursion, state-space, or Kalman). The chapter's only "source" is the static
  LMMSE estimator built in Ch 12. Every section is net-new and is written *from that
  result*, not from any scrap. 13.3 explicitly rederives the Ch 12 LMMSE estimate in
  sequential form; 13.4 presents the Kalman gain as the Ch 12 LMMSE gain made
  recursive. This is the spine of the chapter's credibility: it reads as a
  continuation of Ch 12, not a new topic parachuted in.
- **Keep the filter scalar (1D). The multivariate generalization is Ch 14's job.**
  Per the decisions log and the source map, 13.4 is the *scalar* predict-update
  cycle: state, measurement, gain, and error variance are all real numbers, not
  matrices. The state-space model is written with matrices F, H, Q, R for honesty
  (so the reader sees the general shape), but the worked recursion and all of 13.5
  collapse to the 1D x-coordinate. The matrix recursions are flagged at the section
  boundary as Ch 14.1/14.6 work. This keeps the algebra legible (no matrix inverses,
  the gain is a scalar ratio) and lets the Kalman-gain-equals-LMMSE-gain
  identification be shown by hand.
- **Dataset: the `tracking` dataset, 1D x-coordinate, NOT sensor_readings.** The
  source map (written 2026-06-25 morning) anchored 13.5 on sensor_readings with a
  heavy caveat that it carries no temporal dynamics. The decisions log (same day,
  later) **resolves** this by introducing a purpose-built linear-Gaussian
  constant-velocity `tracking` dataset for the entire Ch 12-14 arc, replacing
  sensor_readings. Ch 13 uses the **1D x-coordinate only**: true state `(px, vx)`,
  noisy position measurement `zx`. This is the trackable trajectory the filter needs
  (a moving target with known ground truth), so 13.5 can show real filtering,
  prediction, and convergence, not the degenerate "estimate a constant" case. The
  source map's recommendation (a) ("synthesize a companion series with real
  dynamics") is exactly what the `tracking` dataset is; this chapter adopts it as
  the named through-line asset.
- **The constant-state warm-up is retained as a teaching step, not a dataset.**
  Before the full constant-velocity track, 13.4/13.5 open with the degenerate
  "estimate a constant level in noise" case (process noise zero, state does not
  move), because that is where the Kalman filter visibly **converges to the static
  Ch 12 LMMSE estimate**, making the "LMMSE done online" thesis concrete. This is
  generated trivially (constant + measurement noise), not read from a file. Then the
  state is allowed to move (the `tracking` x-coordinate) and the filter has to track.
- **Filtering is the recursion we compute; prediction and smoothing are framed by
  contrast.** 13.2 defines all three tasks, but the chapter computes the **filter**
  (the causal estimate using data up to now). One-step **prediction** falls out for
  free (it is the predict half of the cycle). **Smoothing** (using future data) is
  named, its value stated, and explicitly deferred (a backward pass) so the chapter
  stays scalar-causal and does not creep into Ch 14.
- **Notation is coordinated with Ch 12 so the recursion reads as continuation.** Use
  the Ch 12 symbols throughout: estimate, error covariance/variance, and gain carry
  the same letters, now subscripted by time and split into prior (predicted) and
  posterior (updated) at each step. The Kalman gain is introduced as the Ch 12 LMMSE
  gain evaluated against the predicted error variance, not as a new object. Carrying
  one notation across 12 -> 13 -> 14 is a stated cross-chapter commitment.

## Source posture

Net-new on every section (13.1-13.6). There is no adaptation to do: no Kalman,
state-space, recursive-estimation, or filtering content exists anywhere in the
course lessons, the ILA chapters, or the clae-refs notebooks (confirmed by the
source map's repo-wide and course-wide zero-hit search). The chapter's load-bearing
input is internal: the Ch 12 static LMMSE estimator (orthogonality principle, LMMSE
gain, error covariance). 13.5's implementation is written from scratch in numpy
against the `tracking` dataset's 1D x-coordinate; there is no filtering code to
port. Caution flagged by the source map and honored here: do not lean on
sensor_readings for the dynamics demo (it is white noise with no state to track);
use the `tracking` dataset.

## Forward and back wiring

- **Back:** uses the Ch 12 LMMSE estimator as its foundation (the orthogonality
  principle, the LMMSE gain, the error covariance). 13.3 rederives Ch 12's batch
  estimate in sequential form; 13.4's Kalman gain *is* the Ch 12 gain evaluated
  against the predicted variance. Also uses Ch 6 covariance/cross-covariance
  notation and Ch 7's Gaussian conditional mean (the linear-Gaussian state-space
  model is jointly Gaussian, so the filter's running estimate is the conditional
  mean, a callback worth one sentence). Uses the `tracking` dataset introduced for
  the arc (decisions log).
- **Forward:** hands the scalar predict-update cycle to **Ch 14.1** (full
  multivariate Kalman: state and measurement become vectors, the gain becomes a
  matrix, scalar division becomes a matrix inverse). Hands the `tracking` dataset's
  1D x-coordinate filter to **Ch 14.6** (the Estimator finale, the full 2D tracker
  including estimation through measurement gaps). Smoothing (named here, deferred)
  and estimation-through-gaps (the gap rows in `tracking` are ignored here) are
  explicitly flagged as Ch 14 territory so this chapter leaves clean, labeled
  promises rather than orphaned ones.

## Engagement

The "aha" is the recursion reveal in 13.3: the reader has spent Ch 12 solving a
batch least-squares-flavored estimation problem, and here it collapses into a
two-line update that runs forever in constant memory. The second hook is the
predict-update cycle in 13.4 as a *rhythm* (guess where the state went, then correct
with what you measured), which is intuitive before it is algebraic. The concrete
payoff is 13.5: a noisy point jittering across the screen, the filter's estimate
gliding smoothly through it, the error variance settling to a steady value. Risk:
13.1-13.2 can read as taxonomy (definitions of state-space, filtering, prediction,
smoothing) before the reader sees why they matter. Mitigate by opening 13.1 with the
moving-target picture immediately (the Ch 12 estimator pointed at a target that will
not hold still) and keeping 13.2's three-task taxonomy short and visual (one
timeline figure), getting to the recursion fast. Second risk: the
Kalman-gain-equals-LMMSE-gain identification can feel like an assertion; show it by
hand in the scalar case so the reader verifies the two expressions match.

## Code plan

Extend the cumulative library. Reuse the Ch 12 LMMSE update (the gain and the
error-covariance update) as the inner step; the recursive filter is a loop over
that step. Add:

- a `tracking` 1D loader (read `t, px, vx, zx`, drop the y-coordinate columns;
  ignore gap rows for this chapter, they are Ch 14's problem),
- a `kalman_predict` step (advance the state estimate and inflate the error variance
  by the process noise),
- a `kalman_update` step (the Ch 12 LMMSE correction: compute the scalar Kalman gain
  from the predicted variance and measurement noise, blend prediction and
  measurement, shrink the error variance),
- a `scalar_kalman` driver that runs predict-update across the series,
- the constant-state warm-up (process noise zero) showing convergence to the static
  Ch 12 LMMSE estimate.

Figures (SVG, in the chapter's figures directory, per the diagram-pass house style):
the state-space model as a block diagram (state evolves, measurement reads it
through noise); the filtering/prediction/smoothing timeline; the predict-update
cycle as a loop; and the result plots (true track, noisy measurements, filtered
estimate; error variance settling to steady state). Checkpoint: a filtered
1D track with error variance converged, and a side-by-side showing the
constant-state filter landing on the Ch 12 LMMSE number.
