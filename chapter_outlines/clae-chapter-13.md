---
title: "Ch 13 Outline: Estimation in Signal Processing"
type: chapter-outline
chapter: 13
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 13 Outline: Estimation in Signal Processing

Co-produced with `chapter_notes/clae-chapter-13.md`. Section-level content plan,
budgets sum to ~32 pp. Every section is net-new (the chapter's purest-scratch
status is confirmed in the source map); the chapter's "source" is the in-book
Ch 12 -> Ch 13 dependency. Source verdicts per section are in the source map.

## 13.1 From static to dynamic (~5 pp · net-new)

- The pivot: Ch 12 estimated a fixed quantity X from observations Y; real signals **move**, so the thing we estimate must be allowed to change in time. Open with the moving-target picture (the Ch 12 estimator aimed at a target that will not hold still).
- The **state**: a quantity that evolves over time, indexed by a discrete step k. The **state-space model**: state evolves by `x_k = F x_{k-1} + w_k` (process/motion model, process noise `w`), and we observe it through `y_k = H x_k + v_k` (measurement model, measurement noise `v`).
- Keep it scalar in spirit: write the general matrix form for honesty (F, H, Q, R), then specialize to one dimension for the rest of the chapter; the matrix recursions are Ch 14's job. Name the linear-Gaussian assumption (w, v Gaussian) and note it makes the model jointly Gaussian, so Ch 7's conditional mean still governs (one-sentence callback).
- Tie to the `tracking` dataset: the 1D x-coordinate is exactly this model with state `(px, vx)` and a noisy position read `zx`.
- Figure: the state-space model as a block diagram (state evolves left-to-right, measurement reads it through noise).

## 13.2 Filtering, prediction, and smoothing (~4 pp · net-new)

- The three estimation tasks on a time-indexed signal, defined by which data is available relative to the estimate:
- **Filtering**: estimate the state *now* (step k) using all data up to and including now. The causal, online task; the one this chapter computes.
- **Prediction**: estimate a *future* state (step k+m) using data up to now. One-step prediction is the predict half of the Kalman cycle (foreshadow 13.4).
- **Smoothing**: estimate a *past* state using data that includes the future (a backward pass). Name its value (best possible estimate of the past), state that it needs all the data, and **defer** the backward recursion to Ch 14.
- Frame all three as the same LMMSE question (best linear estimate of the state given the available observations), differing only in which observations count.
- Figure: a timeline showing, for a target step k, which measurements each task is allowed to use (filtering up to k, prediction before the target, smoothing the whole record).

## 13.3 Recursive estimation (~7 pp · net-new, the load-bearing pivot)

- The problem with batch: re-solving the full Ch 12 LMMSE problem at every new sample is wasteful and unbounded in memory; the estimate should be **updated**, not recomputed.
- **Recursive estimation**: given the previous best estimate and its error variance, fold in one new measurement to get the new best estimate. Derive the sequential update directly from the Ch 12 orthogonality principle / LMMSE result, showing the running estimate is corrected by a **gain** times the **innovation** (the part of the new measurement not predicted by the current estimate).
- The headline identity: this online form is **exactly** the Ch 12 batch LMMSE answer, reorganized; nothing is approximated. "LMMSE done online." Show the equivalence in the scalar case so the reader can check the two expressions agree.
- The error-variance recursion: each update **shrinks** the error variance (a new measurement can only help); write the scalar update and read off its limiting behavior.
- Introduce **innovation** and the **sequential gain** as named terms here; 13.4 will recognize the gain as the Kalman gain.
- Coordinate notation with Ch 12 (estimate, error variance, gain carry the same letters, now time-subscripted and split into prior/posterior).

## 13.4 The scalar Kalman filter (~8 pp · net-new)

- Assemble 13.1's state-space model and 13.3's recursive update into the **predict-update cycle**, the scalar Kalman filter.
- **Predict** (time update): advance the state estimate through the motion model (`x` estimate scaled by F) and **inflate** the error variance by the process noise Q. This is the "guess where the state went" half; the only place uncertainty grows.
- **Update** (measurement update): the Ch 12 LMMSE correction applied to the predicted estimate. Compute the **Kalman gain** as the LMMSE gain evaluated against the *predicted* error variance and the measurement noise R (a scalar ratio in 1D); blend prediction and measurement by the gain; **shrink** the error variance. This is the "correct with what you measured" half.
- The identification, stated and shown: the Kalman gain **is** the Ch 12 LMMSE gain in sequential dress, computed against the predicted variance instead of a fixed prior. Make this explicit so the chapter reads as a continuation of Ch 12.
- Gain behavior: small measurement noise drives the gain toward trusting the measurement; large measurement noise drives it toward trusting the prediction. The error variance reaches a **steady state** for a time-invariant model.
- The constant-state special case (process noise zero): the filter **converges to the static Ch 12 LMMSE estimate**, the concrete proof of "LMMSE done online."
- Figure: the predict-update cycle as a loop (predict -> measure -> update -> predict ...), with the two error-variance moves (inflate, shrink) annotated.

## 13.5 Implementation: scalar Kalman tracking on the tracking dataset (~6 pp · net-new code)

- Dataset: the **`tracking`** dataset, **1D x-coordinate only** (decisions log; replaces sensor_readings, which carries no dynamics). Load `t, px, vx` (true state) and `zx` (noisy position measurement); drop the y-coordinate columns. Ignore gap rows for this chapter; estimation through gaps is Ch 14.6.
- Build, extending the cumulative library:
- a `tracking` 1D loader,
- `kalman_predict` (advance estimate, inflate variance by Q),
- `kalman_update` (the Ch 12 LMMSE correction: scalar Kalman gain from predicted variance and R, blend, shrink variance),
- a `scalar_kalman` driver looping predict-update across the series.
- Warm-up first: the **constant-state** case (process noise zero) showing the filter settling onto the static Ch 12 LMMSE answer (side-by-side with the Ch 12 number). Then turn on motion: track the moving x-coordinate from noisy measurements.
- Show: the true track, the noisy measurements, and the smooth filtered estimate on one plot; the error variance converging to steady state on another; one-step prediction overlaid (the predict half) to make 13.2's prediction task concrete.
- Checkpoint: a filtered 1D track with error variance converged; the constant-state filter lands on the Ch 12 LMMSE number; the reader can state what the Kalman gain settled to and why.

## 13.6 Summary and exercises (~2 pp · net-new)

- "By the end" recap tied to the exit state: state-space model, the three tasks, recursive estimation as LMMSE-online, the predict-update cycle, the Kalman gain as the LMMSE gain.
- Exercises (all net-new, no source seed exists): derive the scalar error-variance recursion and its steady state; show by hand that the constant-state filter converges to the Ch 12 LMMSE estimate; vary the process- and measurement-noise scales and predict the gain's behavior; implement one-step prediction and compare to the filtered estimate; (stretch) sketch what changes when the state becomes a vector (forward to Ch 14).
- Forward to Ch 14: state and measurement become vectors, the gain becomes a matrix, scalar division becomes a matrix inverse; smoothing and estimation-through-gaps are taken up there.

## Figures

- **Figure 13.1**: the state-space model block diagram (state evolves, measurement reads it through noise). [13.1]
- **Figure 13.2**: filtering / prediction / smoothing timeline (which measurements each task uses). [13.2]
- **Figure 13.3**: the predict-update cycle as a loop, with inflate/shrink annotated. [13.4]
- **Figure 13.4**: result, true track, noisy measurements, filtered estimate (and one-step prediction). [13.5]
- **Figure 13.5**: result, error variance converging to steady state. [13.5]

## Dataset

- **`tracking`** (book-authored Estimator-arc dataset, `datasets/generate_tracking.py`), **1D x-coordinate only**: true state `(px, vx)`, measurement `zx`. The named through-line asset for Ch 12-14. Ch 13 ignores the gap rows (Ch 14.6's problem) and the y-coordinate (Ch 14's 2D tracker). Per the decisions log, this replaces sensor_readings for the arc; sensor_readings is not used in Ch 13.

## Page budget

- 13.1 ~5 pp
- 13.2 ~4 pp
- 13.3 ~7 pp
- 13.4 ~8 pp
- 13.5 ~6 pp
- 13.6 ~2 pp
- Total: ~32 pp.

## Open items for section-level work

- 13.4: fix the exact scalar symbols (prior/posterior estimate, predicted vs updated error variance, gain) once, in coordination with the Ch 12 outline when it is produced, so 12 -> 13 -> 14 share one notation. Ch 12 notes+outline do not exist yet (only its source map); flag the notation as a shared commitment to settle when Ch 12's outline is written.
- 13.5: pick the exact `tracking` generation knobs for the chapter's run (n, dt, q, r, seed) so the worked numbers in 13.3/13.4 and the plots in 13.5 agree; confirm the constant-state warm-up is generated inline (process noise zero) rather than read from a file.
- 13.2: decide how much of smoothing to show (lean: define and defer; one timeline figure, no backward recursion) so the chapter stays scalar-causal and does not creep into Ch 14.
- 13.3: choose whether to present the innovation explicitly as a named quantity now or introduce the word at 13.4 with the Kalman gain; lean toward naming it in 13.3 where the recursive update is derived.
