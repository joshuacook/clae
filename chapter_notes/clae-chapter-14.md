---
title: "Ch 14 Notes: Advanced Filtering and Modern Applications"
type: chapter-notes
chapter: 14
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 14 Notes: Advanced Filtering and Modern Applications

Co-produced with `chapter_outlines/clae-chapter-14.md`, built from
`chapter_notes/clae-chapter-14-source-map.md`. The *why* behind the chapter.

## Role in the book

The book's terminal chapter and the finale of the Estimator arc. Chapter 12 built
the static Linear MMSE estimator (one-shot, the orthogonality principle); Chapter
13 made it recursive and scalar (the predict-update cycle on one coordinate of the
tracking data); Chapter 14 completes the arc by lifting that estimator to the full
multivariate Kalman filter that tracks the 2D target, including the stretch of the
track where the measurements go dark. It is also the book's only forward-pointing
chapter: it closes the running thread (*recover structure from noisy, incomplete
data*) at its most demanding instance, then closes the second thread (the ML
bridge) by carrying the Ch 10 and Ch 11 pointers into modern filtering. Everything
here is net-new prose; there is no course lesson, no project handout, and no
`clae-refs` repo that teaches state-space estimation. The chapter is written from
blank, as the source map's "scratch" tag promises.

## Entry and exit state

**Entry:** the reader has built, in Chapter 13, a scalar Kalman filter on the
x-coordinate of the tracking data and understands the predict-update cycle, the
Kalman gain as a precision-weighted blend of prediction and measurement, and the
recursive-LMMSE framing. The reader knows covariance and its PSD geometry (Ch 6),
the conditional Gaussian and the LMMSE estimator (Ch 7, Ch 12), the orthogonality
principle (Ch 12), and least squares including its recursive and regularized forms
(Ch 11). The reader can read a matrix as an action (Ch 2) and invert a small
matrix.

**Exit:** the reader can (1) write down a linear-Gaussian state-space model
(F, H, Q, R) for a tracking problem and run the full multivariate Kalman
predict-update recursions, (2) keep estimating through missing measurements by
running the prediction step alone and watching the error covariance grow, (3)
explain when and why an adaptive filter (LMS or RLS) replaces a Kalman filter when
the model is unknown, and connect RLS back to recursive least squares (Ch 11) and
recursive LMMSE (Ch 13), (4) name where the field goes next (system
identification, communications) at a survey level, (5) articulate how the linear
estimator generalizes to modern learned-dynamics and sequence models, extending
the Ch 10 and Ch 11 ML bridges, and (6) build a working 2D Kalman tracker on the
tracking dataset, in code, that recovers the known ground-truth track through the
gaps.

## Narrative arc

The scalar filter from Chapter 13 becomes a matrix filter (14.1): same
predict-update cycle, now with a state vector, a transition matrix F, a
measurement matrix H, and covariance matrices Q and R in place of scalars. The
matrix recursions are the same five equations the reader already met, promoted to
matrices, so the chapter opens on recognition, not novelty. Then the chapter does
the one thing a static estimator cannot: it keeps estimating when the data stops
(14.2). Missing measurements are not a special case to patch around; they are the
predict step running on its own, with the error covariance growing until a
measurement arrives to pull it back. This is the running thread's sharpest
statement, *recover structure from incomplete data*, made literally visible on the
track. Next the chapter asks what happens when the model itself is unknown (14.3):
adaptive filters (LMS, RLS) drop the requirement of a known F, H, Q, R and learn
the filter from the data stream, with RLS revealed as recursive least squares
wearing a filtering hat. A brief survey (14.4) points past the spine to system
identification and communications. The ML bridge (14.5) closes both the chapter
and the book: the Kalman filter is a linear-Gaussian special case of a far larger
family, and the same estimate-state-from-observations problem reappears as learned
dynamics and sequence models. The capstone (14.6) is the payoff: build the full
2D tracker and watch it recover the planted track through the gaps. Each section
earns the next: the matrix filter makes gap-handling expressible; gap-handling
exposes the model-known assumption that adaptive filtering then relaxes; relaxing
the model is the doorway to learned dynamics.

## Key decisions

- **The spine is the multivariate Kalman filter (14.1-14.2) plus adaptive
  filtering (14.3).** Locked at the book level (decisions log, Ch 14 scope,
  resolved 2026-06-24) and re-confirmed by the source map: there is no source to
  re-weight, so the scope decision is the structure. System identification and
  communications (14.4) are a deliberately brief "further directions" pointer, not
  a full treatment; the ML bridge (14.5) closes the through-line rather than
  introducing standalone machinery.
- **14.6 is the Build-a-Kalman-Filter capstone on the tracking 2D state.** It
  extends Chapter 13's scalar estimator to the full [px, py, vx, vy] tracker and
  is the explicit finale of the Estimator arc. The capstone's headline result is
  recovering the known ground-truth track *through the measurement gaps*, which is
  what makes the synthetic-known-truth dataset earn its place.
- **The tracking dataset, not sensor_readings, carries the arc.** The source map's
  central conflict (sensor_readings is i.i.d. and has no dynamics to track) is
  already resolved at the book level: the purpose-built linear-Gaussian
  state-space dataset (`datasets/generate_tracking.py`, decisions log
  2026-06-25) is the Ch 12-14 hero. Ch 14 uses its full 2D state and its
  deliberately-dropped measurements. The tracking dataset carries all of Ch 12-14;
  sensor_readings is retired from the estimator arc (it survives only in the Ch 9-10
  scale-normalization role).
- **The matrix recursions are taught as a promotion, not a re-derivation.** The
  reader derived the scalar predict-update in Ch 13. Ch 14 presents the five
  matrix equations as the same equations with scalars replaced by matrices, then
  spends its derivation budget on what is genuinely new: the matrix Kalman gain,
  the Joseph-form covariance update for numerical care, and why H selects the
  observed sub-state.
- **Missing measurements are framed as the predict step alone**, not as
  imputation or interpolation. This is the honest Kalman treatment and it makes
  the error-covariance growth the visible payoff. Deliberately avoids any
  fill-the-gap hack.
- **14.5 extends Ch 10.6 and Ch 11.5; it does not start fresh.** The ML bridge is
  the book's named second thread. The source map confirmed the ILA later-ML
  chapters are empty stubs, so there is no external grounding; 14.5 is written by
  carrying forward the whitening/learned-features pointer (Ch 10.6) and the
  regularization/ill-posed pointer (Ch 11.5) into filtering: learned dynamics
  (replace F with a learned map), and sequence models (RNNs, state-space deep
  models) as the modern descendants of the recursive estimator.

## Source posture

Net-new across every section. There is no course lesson, project handout, or repo
chapter that teaches Kalman filtering, adaptive filtering, or state-space models;
the source map confirmed the absence end to end. The only reusable assets are the
book's own internal threads (LMMSE-to-Kalman from Ch 12-13; the ML bridge from Ch
10.6 and 11.5) and the project-1 milestone *format* as a structural template for
the 14.6 capstone write-up. Reference texts for the author's own grounding (not
reader-facing source): Probabilistic Robotics (Thrun, Burgard, Fox) for the
tracking treatment; standard adaptive-filtering references (Haykin) for LMS/RLS.

## Forward and back wiring

- **Back:** the predict-update cycle and the scalar Kalman filter (Ch 13); the
  recursive LMMSE framing (Ch 13); the orthogonality principle and static LMMSE
  (Ch 12); the conditional Gaussian (Ch 7); covariance and its PSD geometry (Ch
  6); recursive and regularized least squares (Ch 11); matrices as actions and
  inversion (Ch 2). RLS in 14.3 explicitly closes the loop back to recursive least
  squares (Ch 11) and recursive LMMSE (Ch 13).
- **Forward:** none within the book; this is the terminal chapter. The forward
  pointers in 14.4 (system identification, communications) and 14.5 (learned
  dynamics, sequence models) point outside the book, into the literature and into
  the reader's own next steps. The ML bridge (14.5) is the terminal node of the
  second thread begun in Ch 10.6 and continued in Ch 11.5.

## Engagement

The "aha" is the gap: the filter keeps tracking when the measurements stop, and
the error-covariance ellipse swelling and then snapping back as a measurement
returns is the chapter's signature image. Lead with it; promise it in the "by the
end" bookend and deliver it in the 14.6 capstone figure. The matrix recursions
(14.1) risk reading as algebra-for-its-own-sake; keep them anchored to the
tracking picture (F moves the target, H is what the sensor sees, Q is how
unpredictably the target maneuvers, R is how noisy the sensor is) so every matrix
has a physical referent on the track. Adaptive filtering (14.3) risks feeling like
a detour after the Kalman climax; frame it as the answer to "but what if we do not
know F, H, Q, R?", which is the natural question the gap section provokes. The ML
bridge (14.5) is the book's closing note; keep it reflective and concrete (one
named generalization per pointer), not a vague gesture at deep learning.

## Code plan

Extend the cumulative library through the Estimator arc. The capstone (14.6)
builds the full multivariate Kalman filter: a `predict(x, P)` step and an
`update(x, P, z)` step over the tracking model (F, H, Q, R, x0 from
`tracking_model.txt`), a main loop that runs predict-only on gap rows and
predict-then-update on observed rows, and a check that the recovered track matches
the known ground truth within the error covariance. Figures: the
predict-update-cycle diagram (matrix form), the tracked-vs-true trajectory with
the gap stretch highlighted, the error-covariance ellipse growing through the gap
and contracting on the next measurement, and an LMS/RLS convergence plot.
Checkpoint: a working 2D tracker that recovers the planted track through the gaps.
PDF output to `/tmp`, SVG figures converted via `rsvg-convert` first; the tracking
dataset is generated off-box (needs numpy), never on cc-host.
