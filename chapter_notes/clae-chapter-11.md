---
title: "Ch 11 Notes: Least Squares Estimation"
type: chapter-notes
chapter: 11
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 11 Notes: Least Squares Estimation

Co-produced with `chapter_outlines/clae-chapter-11.md`, built from
`chapter_notes/clae-chapter-11-source-map.md`. The *why* behind the chapter.

## Role in the book

The first estimator the book builds end to end. Part III opened with the SVD
(Ch 9) and PCA (Ch 10); least squares is where the machinery turns into a fitted
model that predicts. It is the deterministic estimator: no random vectors yet,
just an over-determined system and the geometry that resolves it. That geometry,
projection onto the column space with an orthogonal residual, is the load-bearing
idea. It pays off Ch 2.3's projection foreshadowing and becomes the template the
random-vector estimator (Ch 12 LMMSE) rhymes with. The chapter also opens the
book's second thread (the ML bridge) on the estimation side: ridge regression is
where regularized least squares becomes the link to machine learning.

## Entry and exit state

**Entry:** the reader can read a matrix as a transformation via the column picture
(Ch 2.1-2.2), knows projection onto a line and a subspace and the orthogonal
residual (Ch 2.3), can reason about Ax = b solvability via column space and null
space (Ch 2.4), and has the SVD with its pseudoinverse forward-pointer (Ch 9). The
reader has standardized Ames features (Ch 2.5-2.6) and met Ames as the recurring
hero throughout Parts I and II.

**Exit:** the reader can (1) recognize an over-determined system and why it has no
exact solution, (2) derive the least squares solution as the projection of b onto
the column space with a residual orthogonal to that space, (3) derive the normal
equations A^T A x = A^T b by minimizing the squared-error loss, (4) compute the fit
three ways (normal equations, QR, the SVD pseudoinverse) and say when each is
numerically safe, (5) derive ridge regression as (A^T A + lambda I)^-1 A^T b and
read it as both a numerical fix and an ML regularizer, and (6) fit and predict Ames
sale price from scratch with `np.linalg.lstsq` and a pseudoinverse-via-SVD, scoring
train and test.

## Narrative arc

A model fit to noisy data over-determines a system: more equations than unknowns,
no exact solution (11.1). We do not give up on Ax = b; we ask for the closest thing,
and "closest" is geometric: project b onto the column space, the residual is
orthogonal to it (11.2). That geometry is a picture, not yet a formula. Two roads
make it computable. The algebraic road minimizes the squared-error loss and lands on
the normal equations (11.3). The numerical road asks how to solve them without
forming A^T A, which conditions badly, and arrives at QR and the SVD pseudoinverse
(11.4). Then the data fights back: when columns are collinear or p approaches n, the
fit is unstable, and ridge regression both stabilizes it and reframes it as the ML
bridge (11.5). Finally we predict Ames sale price for real, from scratch (11.6).
Each section earns the next: no-exact-solution forces the projection, the projection
names the answer, the loss derives it, conditioning motivates the better algorithms,
instability motivates ridge, and Ames is where it all has to actually run.

## Key decisions

- **L4 is the geometric on-ramp, but it stops at naming.** Lesson 004 gives the
  over-determined framing (n>p, the worked 5x2 toy, "b is not in the column space")
  and the projection-onto-column-space reading almost turnkey, and it ties residuals
  to the left null space. It never derives the normal equations, never writes the
  loss, never computes a fit. So 11.1-11.2 adapt L4 (strong); 11.3 onward is net-new.
  This honors the Ch 2 decision that deferred L4's four fundamental subspaces here.
- **11.3 normal equations is net-new, derived two ways.** The calculus route
  (minimize ||Ax - b||^2, set the gradient to zero) and the geometric route (the
  residual is orthogonal to every column, so A^T(b - Ax) = 0) land on the same
  A^T A x = A^T b. Showing both ties the algebra to 11.2's picture; that the two
  agree is the section's payoff.
- **11.4 leans on the in-book Ch 9 SVD, not external source.** QR and numerical
  stability are net-new (no source). The pseudoinverse is forward-linked from Ch 9:
  A^+ = V Sigma^+ U^T, and x = A^+ b. Teach why forming A^T A squares the condition
  number, so QR (factor A directly) and the SVD route (read off and regularize small
  singular values) are the stable paths. This is the right internal dependency to
  lean on per the source map and the decisions log.
- **11.5 ridge derivation is net-new; the sklearn demo is reframed.** HMD has an
  alpha-sweep / train-test-score harness running sklearn Ridge/Lasso on **Boston**;
  the math (A^T A + lambda I) is unsourced. Decision: derive ridge as linear algebra
  (the loss gains lambda||x||^2, the normal equations gain lambda I, which lifts the
  spectrum off zero and is exactly Tikhonov regularization), then read it through the
  SVD as singular-value shrinkage. Port the alpha-sweep *pattern* from HMD, Boston to
  Ames, sklearn to from-scratch. Ridge is the named ML bridge for the chapter.
- **11.6 Ames fit is written from scratch.** Per the source map, there is no
  LinearRegression/Ridge fit on Ames anywhere in HMD; HMD's Ames notebooks are
  preprocessing only (impute, categoricals, EDA), Python 2, modeling cells run
  DecisionTree/SVM on Boston. So reuse HMD only for the Ames data-prep *pattern* and
  the score/alpha-sweep *harness*; author the `lstsq` and `pinv`-via-SVD fit. Target
  is Ames `SalePrice`.
- **Standardize before fitting, and say why.** Ridge penalizes coefficient size, so
  features must be on a common scale or the penalty is arbitrary. This cashes in
  Ch 2.5-2.6 standardization at the moment it finally matters for a fit.

## Source posture

Adapt-heavy on 11.1-11.2 (L4 is clean and on-frame; the source map calls 11.2 the
single best-matched section in the chapter). Net-new on 11.3 (normal equations
derivation), 11.4 (QR, conditioning, SVD pseudoinverse route, the last forward-
linked from in-book Ch 9), and the mathematics of 11.5 (ridge). Reframe-and-port on
11.5 code and 11.6 (HMD sklearn-on-Boston harness and Ames preprocessing, ported to
a from-scratch Ames fit). Cautions: ILA ch04 (least squares) and ch05
(regularization) are empty stubs, so the "strong via repos" tag is wrong; HMD is
Boston-flavored Python 2 and off-frame for modeling. The chapter is genuinely
**partial**: solid geometric on-ramp, net-new estimation core. Detail in the source
map.

## Forward and back wiring

- **Back:** 11.1-11.2 adapt L4 (over-determined systems, projection onto the column
  space, four fundamental subspaces) and pay off Ch 2.3 projection and Ch 2.4
  column/null space. 11.4 pseudoinverse consumes the Ch 9 SVD (A^+ = V Sigma^+ U^T).
  11.5-11.6 cash in Ch 2.5-2.6 standardization. Uses Ames, the recurring hero from
  the Introduction onward.
- **Forward:** 11.2's projection geometry (orthogonal residual onto the column
  space) is the deterministic analogue that **Ch 12.2's orthogonality principle**
  builds on; Ch 12 references this geometry rather than re-teaching it, and Ch 11
  ships first in Part III so the reference resolves. 11.5 ridge is the regularized-
  least-squares instance of the book's ML bridge (named in the outline alongside
  Ch 10 whitening and Ch 14 learned dynamics). The from-scratch estimator discipline
  in 11.6 sets the pattern for the Ch 12-14 estimator arc.

## Engagement

The hook is the honest admission that the system has no solution, then the
refusal to quit: "closest" is a real, computable answer. The projection picture is
the chapter's "aha," and it is a picture the reader already half-owns from Ch 2.3.
The three-ways-to-compute section risks feeling like a numerical-methods detour;
keep it tied to a concrete failure (form A^T A on collinear Ames features and watch
the condition number explode), so the better algorithms are a fix the reader felt
the need for, not a catalog. Ridge has a satisfying double payoff (it fixes the
instability *and* it is the ML idea), surface both. The Ames prediction is the
concrete reward: an actual dollar prediction with a train/test score.

## Code plan

Extend the cumulative library. Add: a normal-equations solver, a QR-based solver, a
pseudoinverse-via-SVD solver (reusing the Ch 9 SVD code), a ridge solver, and a
train/test split-fit-score harness with an alpha sweep (the HMD pattern, reframed
from sklearn to from-scratch). On Ames: load and prep via the HMD preprocessing
pattern (numerical features, simple impute, standardize), fit sale price, predict,
and score. Demonstrate the conditioning failure (A^T A on collinear features) so
11.4's stability claims are shown, not asserted. Figures: the projection-onto-
column-space picture with the orthogonal residual (11.2), and the ridge singular-
value-shrinkage / coefficient-path plot (11.5), as SVG in the chapter's figures
directory. Checkpoint: a fitted Ames sale-price model with train and test scores and
a chosen ridge alpha. Per CLAUDE.md, render PDFs to /tmp, never the repo.
