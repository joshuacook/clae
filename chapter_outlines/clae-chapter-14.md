---
title: "Ch 14 Outline: Advanced Filtering and Modern Applications"
type: chapter-outline
chapter: 14
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 14 Outline: Advanced Filtering and Modern Applications

Co-produced with `chapter_notes/clae-chapter-14.md`. Section-level content plan,
budgets sum to ~34 pp. Every section is net-new: the source map confirmed no
course lesson, project handout, or `clae-refs` repo teaches state-space
estimation, adaptive filtering, or the ML bridge. The only reusable assets are the
book's own internal threads (Ch 12-13 LMMSE-to-Kalman; Ch 10.6 and 11.5 ML
bridge) and the project-1 milestone format. Dataset: `tracking` (the
linear-Gaussian state-space track, full 2D state and the measurement gaps).

The chapter opens with a "By the end of this chapter, you will..." bookend that
promises the concrete outcomes: a working 2D Kalman tracker that recovers the
planted track through the missing measurements. The opening also names the **Core
Pattern: Predict-Update Recursion** (recalled from Ch 13, now in matrix form) so
the chapter threads it from open to capstone.

## 14.1 The full multivariate Kalman filter (~6 pp · net-new)

- From scalar to matrix: the Ch 13 predict-update cycle promoted to a state vector. The five recursions are the same equations the reader already derived, with scalars replaced by matrices (recognition, not novelty).
- The state-space model on the tracking target: state x = [px, py, vx, vy]; motion x_k = F x_{k-1} + w (process noise w ~ N(0, Q)); measurement z_k = H x_k + v (measurement noise v ~ N(0, R), position only). Every matrix gets a physical referent: F moves the target, H is what the sensor sees, Q is how unpredictably the target maneuvers, R is how noisy the sensor is.
- The predict step: state prediction x⁻ = F x; covariance prediction P⁻ = F P Fᵀ + Q.
- The update step: the matrix Kalman gain K = P⁻ Hᵀ (H P⁻ Hᵀ + R)⁻¹; the state update x = x⁻ + K(z − H x⁻); the covariance update, with the Joseph form noted for numerical care.
- Why this is still LMMSE: the gain is the recursive-LMMSE blend (Ch 13), now matrix-valued; the orthogonality principle (Ch 12) still holds.
- Figure: the matrix predict-update cycle (SVG), labeled with F, H, Q, R, K.

## 14.2 Estimation through gaps (~5 pp · net-new)

- The one thing a static estimator cannot do: keep estimating when the data stops. This is the running thread (*recover structure from incomplete data*) at its sharpest.
- A missing measurement is not a special case to patch; it is the predict step running on its own. On a gap row, run predict and skip update.
- The error covariance P grows through a gap (no measurement pulls it back) and contracts the moment a measurement returns. The growing-then-snapping-back covariance ellipse is the chapter's signature image.
- Why the velocity sub-state matters here: F propagates position from velocity, so the filter "coasts" sensibly through the gap rather than freezing.
- Deliberately no imputation or interpolation hack; the honest Kalman treatment is the point.
- Figure: tracked-vs-true trajectory with the gap stretch highlighted; the error-covariance ellipse swelling through the gap and contracting on the next measurement.

## 14.3 Adaptive filtering: when the model is unknown (~6 pp · net-new)

- The question the gap section provokes: the Kalman filter assumes a known F, H, Q, R. What if we do not know them?
- Adaptive filters learn the filter from the data stream. Two workhorses.
- **LMS** (least-mean-squares): stochastic-gradient descent on the instantaneous squared error; the step-size / convergence / misadjustment tradeoff, kept concrete.
- **RLS** (recursive least squares): the recursive solution of the least-squares problem as data arrives; the matrix-inversion-lemma update.
- The CLAE-internal callback (the section's payoff): RLS *is* recursive least squares (Ch 11) wearing a filtering hat, and it is the same recursive-LMMSE structure as the Kalman update (Ch 13). The reader has seen this estimator three times now in three guises.
- When to use which: Kalman when the model is known and Gaussian; adaptive when it is not.
- Figure: LMS/RLS error-convergence plot (SVG).

## 14.4 Further directions (~4 pp · net-new, deliberately brief)

- A short "where next" pointer, not a full treatment (scope decision, decisions log 2026-06-24).
- **System identification:** estimating the model (F, H, Q, R) itself from data, the inverse of everything the chapter assumed known; one paragraph naming the problem and the standard approaches at survey level.
- **Communications:** equalization and channel estimation as filtering problems; one paragraph, survey level.
- Honest framing: these are doorways, not destinations; pointers into the literature for the reader's own next steps.

## 14.5 The ML bridge: modern filtering and learned dynamics (~4 pp · net-new, closes the second thread)

- The book's terminal node of the ML through-line begun in Ch 10.6 (whitening, learned features) and continued in Ch 11.5 (regularization, ill-posed problems). Written fresh: the source map confirmed the ILA later-ML chapters are empty stubs.
- The Kalman filter is the linear-Gaussian special case of a much larger family. Relax linear, relax Gaussian, and the same estimate-state-from-observations problem reappears.
- **Learned dynamics:** replace the known transition map F with a learned function; the model is fit, not given (the system-identification idea, taken to its ML conclusion).
- **Sequence models:** RNNs and modern deep state-space models as the descendants of the recursive estimator; the predict-update recursion is a recurrent cell with a hidden state.
- Reflective close, one named generalization per pointer, concrete not vague. The running thread, *recover structure from noisy, incomplete data*, is the same problem the whole field is still solving.

## 14.6 Project capstone, Build a Kalman Filter (~6 pp · net-new, the Estimator finale)

- Extend Chapter 13's scalar estimator to the full 2D tracker on the tracking dataset; the explicit finale of the Estimator arc (Ch 12 static LMMSE to Ch 13 scalar recursive to Ch 14 full multivariate).
- Milestone structure (project-1 format as template): (1) load the tracking data and the known model from `tracking_model.txt`; (2) implement `predict(x, P)` and `update(x, P, z)`; (3) the main loop, predict-only on gap rows, predict-then-update on observed rows; (4) recover the track and compare to the known ground truth; (5) verify the recovered track stays within the error covariance, including through the gaps.
- Headline result: the filter recovers the planted track *through the measurement gaps*, which is the payoff the dataset was built to deliver.
- Checkpoint (questions, answerable from what the reader built): Does the recovered track match the ground truth within P? Does P grow on gap rows and contract on observed rows? What does the gain K do as R is increased?
- Figure: the capstone result, recovered track over true track with the gap stretch and the error band.

## 14.7 Summary and exercises (~3 pp · net-new)

- "By the end" recap tied to the chapter's exit state, item by item against the opening bookend.
- The book-closing note: the Estimator arc is complete (static to recursive to full Kalman); the running thread is closed at its hardest instance; the ML bridge is the open door out of the book.
- Exercises: net-new problems on the matrix recursions (run one predict-update step by hand on a 2-state toy), on gap-handling (predict P through k gaps, show the growth), on adaptive filtering (LMS vs RLS convergence), and a capstone extension (add an acceleration state, or vary Q and R and watch the gain respond).
- Forward: out of the book, to the reader's own filtering problems.

## Open items for section-level work

- 14.1: decide whether to show the full Joseph-form covariance update or note it and use the standard (I − KH)P⁻ form in the main flow; lean toward standard form in prose, Joseph form as a numerical-care callout.
- 14.2: choose the exact gap to feature in the signature figure (a single long gap reads more clearly than several short ones; pick from the seed=42 dataset's actual dropped rows).
- 14.3: decide the depth of the matrix-inversion-lemma derivation for RLS (lean: state it and connect to Ch 11, do not re-derive the lemma in full).
- 14.6: confirm the capstone uses the full 200-step track or a featured sub-window; lean toward a sub-window for figure clarity with the full track in code.
- Budget check: 6 + 5 + 6 + 4 + 4 + 6 + 3 = 34 pp.
