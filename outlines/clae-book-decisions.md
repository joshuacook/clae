---
title: "CLAE Book Outline: Decisions Log"
type: book-notes
status: active
created: "2026-06-24"
updated: "2026-06-24"
---

# Book Outline Decisions Log

The *why* behind `clae-book-outline.md`. Structure decisions, rationale, and
tracking items live here; the outline itself stays lean.

## Decision: SVD opens Part III (moved from Part I)

SVD is the master factorization underlying both PCA (Ch 10) and least squares
(Ch 11, the pseudoinverse). In the proposal it sat at Ch 4, where it would go
dormant for five chapters before the estimation capstones needed it. Moving it
to open Part III keeps the matrix-factorization machinery fresh at the moment of
use. Chapter 3 (eigendecomposition) ends by foreshadowing SVD; Chapter 9 opens
by recalling diagonalization and generalizing it, so Part I's machinery wakes up
exactly at the Part III boundary.

Cost: loses the tight eigen-to-SVD adjacency, now carried as a deliberate
callback across the probability chapters. Judged a feature (keeps Part I alive in
the reader's mind). Part balance shifts to 3 / 5 / 4 / 2.

## Decision: Part II re-sequenced so expectation precedes covariance

Expectation and conditional probability (proposal Ch 9) move ahead of covariance,
because covariance *is* an expectation and conditional expectation is the
foundation of MMSE. Convergence (LLN/CLT) becomes the Part II closer: it
justifies estimating from finite, noisy samples and hands directly into the
estimation half.

## Narrative architecture

**Two roads to PCA.** Chapter 10 is the reunion of two threads:

```
   3 eigen ┄┄┄┄(recalled)┄┄┄┄► 9 SVD ──► 10 PCA   (the reunion)
   4 rand ─► 5 E[·] ─► 6 cov ─► 7 Gauss ─► 8 conv ──┘
```

PCA via SVD of the centered data matrix *is* eigendecomposition of the covariance
matrix. Both roads are recently traveled when Chapter 10 unites them. PCA is
taught as an **estimator** (sample covariance to estimated principal components),
which is what makes Chapters 8 and 9 on-path rather than a detour: the sample
covariance converges (LLN) and is asymptotically Gaussian (CLT), which is *why*
empirical PCA works.

**The Kalman spine of the back half.** The Linear MMSE estimator built in
Chapter 12 is the static form of the Kalman filter. One estimator grows across
three chapters: static LMMSE (Ch 12) to recursive/online estimation (Ch 13) to
the full multivariate Kalman filter (Ch 14). Plays to the author's fluency in
exactly the from-scratch chapters where it matters most.

**Estimation seeds.** Two ideas are planted early and paid off in Part III, kept
quiet so they do not muddy the PCA destination:

- Ch 5, conditional mean as best predictor (E[Y|X]). Paid off in Ch 12.
- Ch 7, conditional mean of a jointly Gaussian pair is linear in the
  conditioning variable. The LMMSE seed, paid off in Ch 12.

## Decision: dataset strategy (real heroes + synthetic verification)

Two classes of dataset, used for different jobs.

Real-world data motivates and grounds: **Ames housing** is the recurring hero
(a home is a feature vector), threading vectors, transforms, random vector,
covariance, Gaussianity, PCA, and least squares. **Wholesale customers** supports
interpretable PCA.

Synthetic known-ground-truth data proves the estimator recovers a planted truth,
which is uniquely valuable for an estimation book: **stock_returns** (sector
correlation) for convergence verification, **image_features** (known rank 3) for
SVD/PCA rank recovery, **sensor_readings** (scale and noise) for the estimator
and Kalman back end.

The project-1 synthetic CSVs carry generic `feature_1..feature_10` names.
Never copy student submissions from `assessments/` into this repo (PII).

## Decision: one capstone per part (project-based learning)

Each part closes with an integrative project. Two compounding hand-offs make the
work accumulate: Part II's Ames covariance feeds Part III's PCA; Ch 12's LMMSE
estimator becomes Part IV's Kalman filter. The reader's own earlier code is the
input to the later project.

## Tracking: divergence from the proposal (numbering sync owed)

This outline supersedes the proposal TOC. On lock, sync chapter numbers in
`CLAUDE.md`, `proposals/springer-linalg-proposal.md`, `source/README.md`, and
`TIMELINE.md`. Deferred until after the lens passes in case the order shifts.

## Decision: Ch 1 as skim-first reference, written last (2026-06-25)

The audience mostly knows the vector-space mechanics, so a foundations chapter
opening the book risks reading remedial; the source map confirmed Ch 1 is
review-grade adapt on operations and net-new only on the structure it sets up.
Ch 1 therefore becomes a **skim-first reference** (the reader skims it once to
calibrate notation, then refers back to it throughout the book), kept at number 1
(no renumber), **written last** so it is calibrated to the exact notation and
operations the book uses. It is not framed as "skip to Ch 2"; it stays in the
reading flow as a one-pass calibration and a lookup. Geometric depth for specific
operations is taught just-in-time where later chapters need it. Scope: Ch 1 only;
Ch 2 (Matrices) and Ch 3 (Eigen) stay taught chapters.

Consequence: a skim-grade notation reference is the wrong vehicle for
book-critical narrative. The motivation, the running thread, the Ames/datasets
introduction, and the data-as-vectors framing move to a **must-read Introduction
in front matter** (read before Ch 1). The thread is now planted there. Ch 2 is the
first taught chapter.

Timeline impact: Ch 1 moves to the end of the drafting order; the start shifts to
the Introduction and Ch 2. TIMELINE.md needs a reorder.

## Book-wide source assembly findings (2026-06-25)

All 14 chapter source maps are written (`chapter_notes/clae-chapter-NN-source-map.md`).
Assembling the whole book's source at once surfaced systematic issues the coverage
tags hid:

- The `introduction_to_linear_algebra` repo is mostly empty title-only stubs; only
  ch01 (elements), ch02 (systems), ch03 (inner product) have real draft content.
  This reverses the earlier "Ch 11 strong via ILA" upgrade: **Ch 11 is partial.**
- The course math lessons teach on iris and toy matrices, not Ames; re-anchoring
  every worked example to Ames is pervasive net-new work, not adaptation.
- The synthetic back-half datasets do not match their roles: sensor_readings is
  i.i.d. (no dynamics) so the Kalman arc has nothing to track; stock_returns has no
  sector labels for the Ch 6.4 cross-correlation example.
- Course lessons leak across chapter boundaries (L7 to Ch2, L9 to Ch6/7, L10 to
  Ch8/10, L12 to Ch6/10, L4 to Ch11). Re-sort per chapter, honoring the maps.
- Net: every "strong" chapter is adapt-the-mechanics, write-the-payload.
  `source/coverage-by-chapter.md` to be rewritten to reflect this.

## Decision: Estimator-arc dataset (2026-06-25)

The Ch 12-14 Estimator/Kalman arc gets a purpose-built **linear-Gaussian
state-space dataset**, modeled on the Georgia Tech "AI for Robotics" (Thrun, CS
7638) constant-velocity tracking treatment: state [x, y, vx, vy], motion
x_k = F x_{k-1} + w (w ~ N(0,Q)), measurement z_k = H x_k + v (v ~ N(0,R), position
only), generated like the other synthetics with known ground truth and deliberate
measurement gaps. It threads the arc: Ch 12 static one-shot LMMSE (single update,
orthogonality principle), Ch 13 the 1D recursive filter (LMMSE done online), Ch 14
the full 2D Kalman tracker (the Asteroids-style problem) through missing
measurements. Replaces sensor_readings for the arc. Reference text: Probabilistic
Robotics (Thrun, Burgard, Fox).

## Notation conventions (canonical)

Locked 2026-06-25 (coherence pass). Single source of truth for symbols; chapter
outlines have minor drift to reconcile against this at drafting.

| Object | Symbol |
|---|---|
| Mean vector | mu (mu_X, mu_Y) |
| Covariance, population | Sigma |
| Covariance, sample | Sigma-hat |
| Cross-covariance blocks | Sigma_XX, Sigma_XY, Sigma_YY |
| Correlation | rho_ij (coefficient), R (matrix) |
| Data matrix | X (rows = samples) |
| Second-moment / Gram matrix | M = X-transpose X |
| SVD | A = U S V-transpose; singular values sigma_i on diag(S) |
| Eigenvalue / singular-value link | lambda_i = sigma_i^2 / (n-1) for the sample covariance |
| Least-squares design matrix | A (A x = b); pseudoinverse A^+ |
| State estimate | x-hat (time-subscripted); X-hat for the random-vector estimate (Ch 12) |
| True unobserved state | x, X (no hat) |
| Observation | Y (general estimation); z = H x + v (measurement, Ch 12.3 onward) |
| Kalman model | F transition, H observation, Q process noise, R measurement noise, K gain |
| Kalman error covariance | P (updated), P-minus (predicted); P_{k|k}, P_{k|k-1} |

Guards: Sigma is covariance, never the SVD diagonal (that is S). R is the
correlation matrix in Ch 6 and the measurement-noise covariance in Ch 12-14; they
never co-occur, but state the meaning at each first use. "Through-line" names only
the ML second thread; use "takeaway" for a section's one-line summary.

Reconcile at draft: Ch 6.4 (Cov(X,Y)) and Ch 12 (C_X / C_XY) standardize to
Sigma_XY; Ch 9/10/11 SVD diagonal standardizes to S; Ch 12 m_X to mu_X; Ch 14 adds
hats to its estimates.

## Draft-time notes (from the lens passes)

Correctness and scope reminders surfaced by the lens passes, to honor when the
chapters are drafted:

- **Ch 10 PCA/SVD equivalence:** principal directions equal the right singular
  vectors exactly, but the eigenvalues of the sample covariance equal the squared
  singular values divided by (n-1), not the singular values themselves.
- **Ch 8 convergence altitude:** teach modes of convergence by simulation;
  deliberately avoid almost-sure vs in-probability vs in-distribution
  measure-theoretic distinctions (prerequisite is a first probability course).
- **Ch 14 scope (resolved 2026-06-24):** narrowed. The full multivariate Kalman
  filter and adaptive filtering are the spine; system identification and
  communications are brief further directions; modern ML is the through-line's
  close, not a standalone topic.
- **ML through-line (resolved 2026-06-24):** promoted to a named second thread,
  surfaced only where it earns its place (PCA whitening/learned features Ch 10,
  regularized least squares Ch 11, modern filtering/learned dynamics Ch 14). The
  reach beyond Boyd and Vandenberghe for the ML/data-science audience.

## Status

Spine locked with the author 2026-06-24. Book-outline lens passes complete
(10 lenses x 2, run as the `book-outline-lenses` workflow); both spine-level
decisions they raised (Ch 14 scope, ML through-line) resolved 2026-06-24. The
book outline is locked. The numbering sync across CLAUDE.md, the proposal,
source/README, and TIMELINE is complete (2026-06-24). The outline was then
expanded to section level (about 95 sections, strong chapters mirroring the
course lesson structure); this expansion post-dates the lens passes, which ran on
the chapter-level version, so the section breakdown is not yet lensed.

Source assembly is complete for all 14 chapters (per-chapter maps). The chapter
notes+outline pairs are drafted for Ch 2-14 (Ch 1 reference and the Introduction
are written last). The coherence pass (5 lenses over all 13 pairs) is done and its
fixes applied: stale sensor_readings to tracking, the two Part III capstones
disambiguated, the dangling imputation pointer repointed, notation conventions
locked (above), and Ch 7/8 budgets reconciled. Architecture verified sound
(symmetric seeds/callbacks, clean boundaries, uniform voice). Next: section-level
work, starting with Ch 2 (section notes+outlines, then draft).
