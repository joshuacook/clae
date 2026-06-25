---
title: "Ch 12 Outline: Linear MMSE Estimation"
type: chapter-outline
chapter: 12
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 12 Outline: Linear MMSE Estimation (capstone)

Co-produced with `chapter_notes/clae-chapter-12.md`. Section-level content plan,
budgets sum to ~36 pp. The **Part III project capstone (the Estimator seed)**. Every section is net-new
theory (source map: no lesson, no case study, no repo chapter); the only reuse is
the `tracking` dataset as a continuity asset and the in-book seeds this chapter
pays off (Ch 5.4, Ch 7.4, Ch 6.4 notation, Ch 11.2 geometry). Source verdicts per
section are in the source map.

## 12.1 The estimation problem (~5 pp · net-new, pays off Ch 5.4 and Ch 7.4)

- The setup: an unknown random vector `X` and an observed random vector `Y`, jointly distributed; estimate `X` from `Y`.
- The criterion: mean squared error, `E[||X - g(Y)||^2]`; "best" means smallest MSE.
- The full answer, recalled from Ch 5.4: the conditional mean `E[X|Y]` is the MMSE estimator over *all* functions `g`. State it, do not re-derive it.
- Why we restrict to **linear** (affine) estimators `X_hat = a + B Y`: the conditional mean needs the full joint distribution; the linear estimator needs only means and covariances, which we can estimate from data (Ch 6). The cost we accept and the cost we avoid.
- Forward promise: in the Gaussian case the restriction is free (12.4); the tracking problem the chapter ends on (estimate state from a noisy position fix).
- Figure: the estimator as a map from observation space to estimate space; all-functions `g` vs the affine subset.

## 12.2 The orthogonality principle (~6 pp · net-new, the geometric heart)

- The claim, stated geometrically first: the best linear estimate is the one whose **estimation error** `X - X_hat` is uncorrelated with (orthogonal to) the data `Y`, `E[(X - X_hat) Y^T] = 0`.
- The inner product that makes "orthogonal" precise for random vectors: `<a, b> = E[a^T b]`; covariance as the geometry.
- The analogue to Ch 11.2, named explicitly: the least-squares residual is orthogonal to the column space; here the error is orthogonal to the span of the observations. Reference Ch 11.2, mark the one difference (random vectors, covariance inner product, not a fixed data matrix).
- Proof that orthogonality characterizes the optimum (any other linear estimate has strictly larger MSE; the Pythagorean decomposition of MSE).
- Why this matters: it hands the closed form in 12.3 without calculus, and it is the single idea the reader keeps.
- Figure: the orthogonality picture, error vector perpendicular to the data subspace, drawn to rhyme with the Ch 11.2 projection figure.

## 12.3 The Linear MMSE estimator (~6 pp · net-new, Ch 6.4 notation)

- Translate orthogonality into covariance: `E[(X - X_hat) Y^T] = 0` with `X_hat = a + B Y` gives the **normal equations** for estimation.
- Solve: `B = C_XY C_YY^{-1}` and `a = m_X - B m_Y`, so `X_hat = m_X + C_XY C_YY^{-1} (Y - m_Y)`. Reuse Ch 6.4 cross-covariance notation (`C_XY`, `C_YY`) exactly.
- The measurement-model form used for the rest of the chapter: with `Y = H X + v`, derive the **gain** `K = C_X H^T (H C_X H^T + R)^{-1}` and `X_hat = m_X + K(Y - H m_X)`. This is the form Ch 13/14 reuse.
- Worked example on the tracking model (one position measurement, a prior on the state): compute `K` and the fused estimate, numbers that 12.6 reproduces in code.
- Interpretation: the estimate is the prior corrected by the **innovation** `Y - H m_X`, weighted by how much to trust the data versus the prior.
- Figure: the LMMSE estimate as a point between prior mean and measurement, pulled toward the more certain one.

## 12.4 The Gaussian case (~5 pp · net-new, synthesis of Ch 5.4 and Ch 7.4)

- The theorem: when `X` and `Y` are jointly Gaussian, the LMMSE estimator equals the full MMSE estimator equals the conditional mean. **LMMSE = MMSE = E[X|Y]**.
- The proof is a callback, not new work: Ch 7.4 already showed the conditional mean of a jointly Gaussian pair is affine in the conditioning variable, with exactly the coefficient `C_XY C_YY^{-1}` from 12.3. Pay off both seeds here, together: Ch 5.4 (conditional mean is MMSE-optimal) plus Ch 7.4 (it is linear) gives the equivalence.
- The consequence: in the Gaussian world the restriction to linear estimators in 12.1 costs nothing; the easy estimator is the optimal one.
- The honest caveat: outside Gaussian, LMMSE is the best *linear* estimator, generally not the best estimator; what we gain is means-and-covariances-only computability.
- Why this licenses the whole Kalman arc: the tracking model is linear-Gaussian by construction, so LMMSE is optimal throughout Ch 12 to 14.

## 12.5 Performance evaluation: the error covariance (~5 pp · net-new)

- The **error covariance** `P = E[(X - X_hat)(X - X_hat)^T]`: not just how good the estimate is on average, but the full uncertainty that remains.
- Closed form: `P = C_X - C_XY C_YY^{-1} C_YX`, equivalently `P = (I - K H) C_X` in the measurement-model form. The estimate *and* its uncertainty, both in closed form.
- The key fact: `P` is smaller (in the PSD order) than the prior `C_X`; observation removes uncertainty, and the formula says exactly how much. Tie back to 12.2 (Pythagoras: removed variance equals explained variance).
- The Wiener estimator named: this LMMSE estimator with its error covariance is, historically, the **Wiener estimator**; the Kalman filter generalizes it to the recursive case (forward to Ch 13).
- Worked: the error covariance on the tracking single-update, shown shrinking from prior to posterior; checkable against ground truth.
- Figure: prior, measurement, and posterior uncertainty ellipses on the position plane, posterior tighter than both.

## 12.6 Project capstone: a static LMMSE estimator on `tracking` (~7 pp · net-new code, `tracking` dataset)

- The problem, stated as estimation: given a prior `(x0_hat, P0)` on the target state `[px, py, vx, vy]` and one noisy position measurement `z` from `tracking.csv`, produce the LMMSE state estimate and its error covariance.
- Dataset: `tracking.csv` (true state `px, py, vx, vy`; measurement `zx, zy`) and `tracking_model.txt` (known `H`, `R`, and the model). Single update step only; the prediction and recursion are Ch 13.
- Build the library function `lmmse_update(x_hat, P, z, H, R)`: gain `K = P H^T (H P H^T + R)^{-1}`, estimate `x_hat + K(z - H x_hat)`, error covariance `(I - K H) P`.
- Run it on one row: show the fused estimate landing between prior and measurement, the velocity components updated through the cross-covariance even though only position is measured (the payoff: LMMSE infers the unobserved state).
- Verify against ground truth: estimate near the true state, error covariance consistent with the realized error, posterior uncertainty below prior.
- The hand-off, stated explicitly: this function is the **update half** of the Ch 13 predict-update cycle; Ch 13 wraps it in a loop and adds the predict step (`F`, `Q` from this same model).
- Checkpoint: the `lmmse_update` function, the fused estimate, and its error covariance.
- Figure: a block diagram of the single update, marked as the update half of the Kalman cycle to come.

## 12.7 Summary and exercises (~2 pp · net-new)

- "By the end" recap tied to the chapter's exit state: the problem, the orthogonality principle, the LMMSE formula, the Gaussian equivalence, the error covariance, the working estimator.
- The one-line through-line: the best linear estimate is a projection in the covariance geometry, and its error covariance says how much the data helped.
- Exercises, net-new: derive `B = C_XY C_YY^{-1}` from orthogonality; show `P` is PSD-dominated by `C_X`; the scalar case by hand; prove LMMSE = MMSE for a given jointly Gaussian pair; vary `R` in the capstone and watch the gain and posterior covariance respond.
- Forward to Ch 13: make the estimator recursive; the static update becomes the predict-update cycle.

## Datasets

- **`tracking`** (`datasets/generate_tracking.py`, `tracking.csv` + `tracking_model.txt`): the Estimator-arc dataset, used here for a single LMMSE update (estimate state from one measurement given a prior). Continuity asset across Ch 12 to 14; same model threaded into the Kalman filter. No external source dataset; the source map's `sensor_readings` is superseded by this per `clae-book-decisions.md` (2026-06-25).

## Open items for section-level work

- **12.3/12.5/12.6 number lock:** fix the prior `(x0_hat, P0)` once (the generative model decision) and use the *same* `H`, `R`, `P0` in every worked example and the capstone, so the theory numbers equal the code output. This is the chapter's internal-consistency risk (see notes); resolve at section-outline time, before any prose.
- **12.2:** decide how much of the Pythagorean MSE decomposition to show in full vs cite, and exactly how closely the figure should mirror the Ch 11.2 projection figure.
- **12.4:** decide whether to re-state the Ch 7.4 conditional-Gaussian formula in full or reference it; lean toward a one-line restatement so the equivalence is self-contained.
- **Sequencing:** this chapter depends on Ch 5.4 and Ch 7.4 (both scratch/partial) being outlined first, and on Ch 11 shipping first in Part III. Do not draft 12.1/12.4 prose until the seeds exist.
- **Budget check:** 5 + 6 + 6 + 5 + 5 + 7 + 2 = 36 pp.
