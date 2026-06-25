---
title: "Ch 12 Notes: Linear MMSE Estimation"
type: chapter-notes
chapter: 12
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 12 Notes: Linear MMSE Estimation

Co-produced with `chapter_outlines/clae-chapter-12.md`, built from
`chapter_notes/clae-chapter-12-source-map.md`. The *why* behind the chapter. This
is the **capstone of Part III** and the first half of the estimation destination
the whole book exists for. Every theory section is net-new; the only reuse is the
`tracking` dataset (continuity, not content) and the in-book seeds this chapter
pays off.

## Role in the book

Chapter 12 is where "recover structure from noisy, incomplete data" stops being a
slogan and becomes a closed-form estimator. Part I built the linear machinery,
Part II built the statistical machinery, and Chapters 9 to 11 spent that machinery
on PCA and least squares. Both of those are deterministic projections onto a data
geometry. Chapter 12 turns the projection statistical: instead of projecting onto
the column space of a data matrix, the reader projects an unknown random vector `X`
onto the span of the observations `Y`, in the geometry the covariance defines.
That single move is the **Estimator seed**. It is the static, one-shot Kalman
update. Chapter 13 makes it recursive and Chapter 14 makes it the full
multivariate Kalman filter, so the estimator built here is the literal starting
point of the book's two-chapter finale.

## Entry and exit state

**Entry:** the reader arrives from Chapter 11 (least squares as projection onto a
column space, the orthogonal residual) and from Part II. They must already carry
two seeds: Ch 5.4, the conditional mean `E[X|Y]` minimizes mean squared error; and
Ch 7.4, for a jointly Gaussian pair the conditional mean is linear in the
conditioning variable with conditional covariance independent of the value
observed. They know covariance and cross-covariance from Ch 6 (`C_XX`, `C_YY`,
`C_XY`) and the multivariate normal from Ch 7.

**Exit:** the reader can (1) state the estimation problem as "find the function of
`Y` closest to `X` in mean square," (2) prove and apply the orthogonality
principle, (3) derive and compute the linear MMSE estimator from covariance and
cross-covariance, (4) explain exactly when and why LMMSE equals the full MMSE
(the Gaussian case, paying off both seeds), (5) compute the error covariance and
name the result the Wiener estimator, and (6) build a static LMMSE estimator that
fuses one noisy measurement with a prior on the `tracking` dataset, in code,
checking the estimate and its error covariance against known ground truth.

## Narrative arc

The chapter is one argument told five ways. First, **state the problem**: among
all estimators of `X` from `Y`, which minimizes mean squared error, and what do we
give up by restricting to linear ones (12.1). Second, **find the geometric
characterization** before grinding any algebra: the best linear estimator is the
one whose error is orthogonal to the data, the orthogonality principle, which is
the random-vector twin of Chapter 11's orthogonal residual (12.2). Third, **cash
the geometry into a formula**: orthogonality written in covariance and
cross-covariance gives the closed-form LMMSE estimator in one short derivation
(12.3). Fourth, **ask when linear is enough**: in the Gaussian case the linear
estimator is the conditional mean, so LMMSE equals MMSE and both equal `E[X|Y]`,
the moment where Ch 5.4 and Ch 7.4 are paid off together (12.4). Fifth, **measure
the result**: the error covariance quantifies how much uncertainty the observation
removed, and this is the Wiener estimator (12.5). Then the capstone applies all
five to fuse one measurement with a prior on the tracking state (12.6). Each
section earns the next: the problem demands a characterization, the geometry yields
the formula, the formula raises the linear-vs-optimal question, and the answer
demands a way to measure performance.

## Key decisions

- **Geometry before algebra (12.2 before 12.3).** The orthogonality principle is
  the conceptual heart of the chapter, so it is taught as a geometric fact first,
  then turned into the normal-equations-style covariance condition. This mirrors
  the chapter's own claim that LMMSE is projection. Deriving the estimator straight
  from a calculus minimization would land the same formula but bury the idea the
  reader is supposed to leave with.
- **Reference Ch 11.2, do not re-teach it.** The orthogonality principle rhymes
  with the least-squares orthogonal residual, but it is a distinct result: the
  inner product is now `E[ab]` (covariance), the subspace is the span of the random
  observations, not the column space of a data matrix. The chapter names the
  analogy explicitly and leans on the reader's Ch 11 intuition, then marks the one
  place it differs (random vectors, covariance inner product).
- **One generative model, fixed in 12.6, threaded backward through 12.1 to 12.5.**
  This is the load-bearing decision. The worked numbers in the theory sections and
  the capstone must agree, so the `Y = HX + v` setup is chosen once and every
  earlier worked example draws on it. See the threat note below.
- **`tracking`, not `sensor_readings`.** The source map was written against
  `sensor_readings`, the project-1 scale-varying PCA asset. The book-decisions log
  (2026-06-25) supersedes that: the Ch 12 to 14 arc gets the purpose-built
  linear-Gaussian state-space `tracking` dataset (`datasets/generate_tracking.py`),
  state `[px, py, vx, vy]`, motion `x_k = F x_{k-1} + w`, measurement
  `z_k = H x_k + v` (position only). Chapter 12 uses a **single update step**:
  estimate the full state from one position measurement given a prior. The source
  map's "impose a signal-plus-noise model" gap is therefore already resolved by the
  dataset's own `H`, `R`, and a prior covariance; the chapter inherits a known
  ground-truth model rather than constructing one.
- **The capstone is static, deliberately.** No prediction step, no time recursion.
  Chapter 12 fuses a prior `(x0_hat, P0)` with one measurement `z` via LMMSE and
  stops. The recursion is Chapter 13's job. Holding the capstone to one update is
  what makes the predict-update cycle in Ch 13 land as "do this again."
- **LMMSE framed as the affine estimator.** The best *linear* estimator includes a
  bias term (`a + B Y`), so the chapter is honest that "linear MMSE" means affine,
  and the constant absorbs the means. This keeps 12.4's "equals the conditional
  mean" exact rather than approximate.

## Source posture

Net-new on every theory section (12.1 to 12.5, 12.7). There is no lesson (course
L20 is title-only), no case study, and no `clae-refs` chapter for MMSE, Wiener, or
the orthogonality principle: the source map confirms a repo-wide grep returned no
estimator content. The capstone (12.6) reuses the `tracking` dataset as a
continuity asset only; it carries a known model but no built-in single-update
estimator, so the estimator code is net-new. The real inputs are the in-book seeds
(Ch 5.4, Ch 7.4), the cross-covariance notation (Ch 6.4), and the projection
geometry (Ch 11.2). This is a from-scratch chapter that earns its place by paying
off debts the earlier chapters deliberately incurred.

## Forward and back wiring

- **Back:** pays off Ch 5.4 (conditional mean minimizes MSE; the MMSE seed) and
  Ch 7.4 (conditional Gaussian is linear; the LMMSE seed), explicitly in 12.1 and
  jointly in 12.4. Reuses Ch 6.4 cross-covariance notation (`C_XY`, `C_YY`) in
  12.3. References, without re-teaching, Ch 11.2 projection and the orthogonal
  residual as the analogue for 12.2. Uses Ch 7's multivariate normal in 12.4.
- **Forward:** the static LMMSE estimator and its error covariance `P` are the
  Estimator seed. Chapter 13 reuses 12.3's gain and 12.5's error-covariance update
  as the **update half** of the predict-update cycle, then adds the predict step
  (the `F` and `Q` from the same `tracking` model). Chapter 14 generalizes to the
  full multivariate filter and estimation through the measurement gaps. The Wiener
  estimator named in 12.5 is the historical anchor the Kalman filter generalizes.

## The threat: internal consistency of one generative model

The source map names the writing risk precisely, and it is not sourcing. It is
**internal consistency**. One linear-Gaussian generative model has to be threaded
through 12.1 to 12.6 and onward into Ch 13 and 14, or the chapter contradicts
itself. Concretely:

- The `tracking` model fixes `F`, `H`, `Q`, `R`, and `x0` (written to
  `tracking_model.txt`). Chapter 12's single-update problem must adopt a prior
  `(x0_hat, P0)` and the measurement model `z = H x + v`, `v ~ N(0, R)`, and then
  **every worked number** in 12.3 (the gain), 12.4 (the Gaussian equivalence), and
  12.5 (the error covariance) must be the numbers that 12.6's code produces on that
  same model. If a theory section uses a toy 2x1 example with different covariances
  than the capstone, the reader who checks will find the chapter inconsistent.
- The same model must survive into Ch 13 and 14. The gain and error-covariance
  update derived in 12.3 and 12.5 are reused verbatim as the Kalman update; the
  `F`, `Q` deferred here are consumed there. Choosing `H`, `R`, `P0` here commits
  the whole arc. This is why the capstone's generative model is fixed first
  (decision above) and the theory written against it.

**Sequencing dependency (flag).** Chapter 12 cannot be drafted convincingly before
**Ch 5.4 and Ch 7.4 exist**, because its two headline results (12.1's problem
framing and 12.4's Gaussian equivalence) are payoffs of those seeds. Both seed
chapters are themselves scratch (Ch 5) or partial (Ch 7) per the source maps.
Sequence Chapter 12 after Ch 5.4 and Ch 7.4 are at least outlined, or 12.1 and
12.4 have nothing to pay off and read as parachuted-in theory. Chapter 11 must
also ship first (Part III order) so 12.2 can reference its projection geometry.

## Engagement

The "aha" is 12.2: the best estimate is a projection, and you can see it before you
compute it. The orthogonality picture (error perpendicular to the data) is the
geometric hook, and because the reader met its deterministic twin in Ch 11, it
lands as recognition rather than a new abstraction. The risk is 12.3 reading as
covariance-algebra grind; keep it tied to the tracking question (how much should I
trust this noisy position fix versus my prior on where the target is?) so the
formula answers a felt question. The capstone payoff is concrete and checkable: the
reader fuses one measurement with a prior and watches the estimate land between
them, closer to whichever is more certain, with an error covariance that is
provably smaller than either input. That "the estimate is better than both inputs"
moment is the chapter's reward.

## Code plan

Extend the cumulative library. The capstone (12.6) needs: load the `tracking`
model (`F`, `H`, `Q`, `R`, `x0`) and one measurement row `z` from `tracking.csv`;
construct a prior `(x0_hat, P0)`; compute the LMMSE gain `K = P0 H^T (H P0 H^T +
R)^{-1}`; form the updated estimate `x_hat = x0_hat + K (z - H x0_hat)` and the
updated error covariance `P = (I - K H) P0`; and verify against the known true
state from the same row. Figures (SVG, chapter `figures/` directory): the
orthogonality principle (error vector perpendicular to the data subspace,
mirroring Ch 11.2 so the reader sees the analogy); the LMMSE estimate as a point
between prior and measurement on the position plane, with prior, measurement, and
posterior uncertainty ellipses (the variance-shrinks picture); a schematic of the
single update as a block diagram, marked as the update half of the Ch 13
predict-update cycle. Checkpoint: a working `lmmse_update(x_hat, P, z, H, R)`
function and the fused estimate with its error covariance, ready to be wrapped in a
loop in Ch 13.
