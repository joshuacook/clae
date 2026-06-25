---
title: "Ch 3 Notes: Eigenvalues, Eigenvectors, and Diagonalization"
type: chapter-notes
chapter: 3
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 3 Notes: Eigenvalues, Eigenvectors, and Diagonalization

Co-produced with `chapter_outlines/clae-chapter-03.md`, built from
`chapter_notes/clae-chapter-03-source-map.md`. The *why* behind the chapter.

## Role in the book

The third taught chapter and the close of Part I. Ch 2 made a matrix an *action* on
data vectors; Ch 3 asks which directions that action leaves alone and what the
matrix looks like in the basis those directions provide. This is the chapter where
linear algebra stops being about solving systems and starts being about *structure*:
eigenvectors are the axes a matrix is secretly written in, and the spectral theorem
(3.4) is the load-bearing result that turns a symmetric matrix into a set of
orthogonal directions with variances attached. That result is the bridge to the
whole statistical half of the book, the covariance matrix (Ch 6) and PCA (Ch 10),
so this chapter carries more downstream weight than its modest source suggests.

The chapter ends on the **Part I capstone (3.6, "Geometry of Real Data")**: recover
the known rank 3 of `image_features` by eigendecomposition alone, before a single
word of probability. It is the first time the reader watches linear algebra recover
a planted truth from noisy data, the book's running thread made concrete with no
statistical machinery in play.

## Entry and exit state

**Entry:** the reader has finished Ch 2. They can read a matrix as a transformation
via the column picture, reason about Ax = b and invertibility, and standardize an
Ames feature matrix in code. They have a centered, covariance-ready data matrix in
hand from 2.6. They have seen projection geometrically but not yet variance.

**Exit:** the reader can (1) state the eigenvalue problem Av = lambda v as the
search for invariant directions and explain what one buys you, (2) find eigenvalues
and eigenvectors via the determinant characteristic polynomial det(A - lambda I) = 0,
generalizing past 2x2, (3) diagonalize a matrix and read the eigenbasis as the
coordinate system the matrix is diagonal in, (4) state and use the spectral theorem
for symmetric matrices (real eigenvalues, orthogonal eigenvectors), (5) implement
power iteration to extract a dominant eigenvector without a black-box solver, and
(6) recover the rank of a real, noisy matrix by eigendecomposing its second-moment
matrix, the capstone.

## Narrative arc

Special directions exist (3.1), here is how to find them (3.2), here is what they
let you do, rewrite the matrix in their basis (3.3), and for the matrices this book
actually cares about, symmetric ones, those directions are guaranteed to be
orthogonal and real (3.4). Then we compute one without cheating (3.5, power
iteration on Ames' second-moment matrix) and put the whole machine to work
recovering hidden structure from noise (3.6, the capstone). Each section earns the
next: invariant directions motivate the hunt for them; the hunt produces an
eigenbasis; the eigenbasis is only orthogonal when the matrix is symmetric, which is
exactly the case PCA will need; and a second-moment matrix is symmetric by
construction, which is why the capstone works at all.

## Key decisions

These follow the source map's triage (adapt the mechanics, write the payload).

- **3.4 spectral theorem is the priority write (net-new).** L7 states the
  symmetric-matrix properties as a 3-bullet aside, never proved or motivated. This
  section carries the entire Ch 6/10 bridge and is written from scratch: real
  eigenvalues, orthogonal eigenvectors, orthogonal diagonalization A = Q Lambda
  Q-transpose, and an honest, low-machinery argument for orthogonality. PSD and the
  covariance tie-in are *seeded* here but the word "covariance" is deferred to
  Part II to protect the capstone's pre-probability promise.
- **Rewrite the characteristic-polynomial derivation (3.2).** L7 derives the 2x2
  characteristic polynomial by a non-standard "the two equations must be dependent /
  a^2 = 1" trick that does not generalize. Replace it with the standard
  det(A - lambda I) = 0, which carries to n dimensions and connects back to Ch 2's
  invertibility (a nonzero null space means a singular matrix means zero
  determinant). At least one n >= 3 worked case is net-new.
- **Re-anchor examples to Ames and to n dimensions.** Every L7 example is a bare 2x2.
  The chapter keeps one or two clean 2x2 cases for first contact (3.1, 3.2) but moves
  the load-bearing examples to Ames features and to the 10-dimensional capstone, per
  the source map's "re-anchor" instruction.
- **3.5 power iteration is net-new, on Ames' second-moment matrix.** No iterative
  eigen-algorithm exists anywhere in the course; numpy `linalg.eig` is all L7 uses.
  Build power iteration from the eigenvalue definition (repeated multiplication
  amplifies the dominant direction), and construct the Ames second-moment matrix
  X-transpose-X, which is never built in any lesson. This is the implementation
  section and it deliberately avoids the black box so the reader sees *why* the
  dominant eigenvector emerges.
- **3.6 is probability-free by construction.** Project-1 reaches `image_features`'
  rank 3 via the *sample covariance* (a Part II construction). The capstone instead
  eigendecomposes the raw second-moment / Gram matrix X-transpose-X and reads rank
  off the eigenvalue spectrum (three large eigenvalues, seven near-zero from the 0.1
  noise floor). Covariance language is explicitly deferred to Part II. This is the
  deliberate eigen-then-SVD pairing: Ch 9 recovers the *same* rank via SVD, and the
  capstone closes by naming that sequel.
- **Drop L7's Ch 2 ballast.** L7's LU-decomposition and transformation-geometry
  sections (rotation, projection, shear) belong to Ch 2 and are not pulled into Ch 3.

## Source posture

Adapt-heavy on the mechanics, write-from-scratch on the payload.

- **Adapt (real L7 source):** 3.1 (L7's invariant-direction motivation and the
  [[2,1],[1,2]] stretch example, L7's strongest material), 3.2 (worked 2x2 mechanics
  and the multiplicity vocabulary, with the derivation rewritten), 3.3 (the
  P-inverse-A-P diagonalization process and existence conditions, solid at 2x2), 3.7
  (the 2x2 problem bank as an exercise seed).
- **Net-new:** 3.4 (spectral theorem), 3.5 (power iteration plus the Ames
  second-moment construction), 3.6 (the probability-free rank-recovery procedure).
- **Caution:** ILA ch08 is an empty stub and contributes nothing; the coverage
  table's credit for it is vapor. L7 is 2x2-only and carries off-topic ballast.
  Detail in the source map.

## Forward and back wiring

- **Back:** consumes Ch 2's standardized, centered Ames feature matrix (2.6) as the
  input to the second-moment construction; reuses the column picture and the
  determinant / invertibility link from Ch 2.4; relies on Ch 1's basis, dimension,
  and orthogonality as reference.
- **Forward:** the spectral theorem (3.4) is the explicit setup for the covariance
  matrix (Ch 6) and PCA (Ch 10); the second-moment eigendecomposition (3.5, 3.6) is
  the eigen-road that Ch 10 will reunite with the SVD road. The capstone's rank-3
  recovery is deliberately paired with Ch 9, which recovers the same rank via SVD
  (Eckart-Young), so 3.6 closes by foreshadowing SVD as the general tool for
  non-square, non-symmetric matrices. 3.7 carries that forward-pointer.
- **Guard:** keep covariance and probability language out of 3.4 and 3.6 so Part II
  introductions land fresh and the capstone's pre-probability promise holds.

## Engagement

The "aha" is the eigenbasis reveal in 3.3: a matrix that looked like an arbitrary
grid of numbers is, in the right coordinates, just a list of stretch factors. The
spectral theorem (3.4) should land as a promise about the future ("the matrices you
will care about most are the well-behaved ones"), not as an abstract aside. The
capstone is the emotional payoff: noisy 10-dimensional data, and the eigenvalue
spectrum cleanly shows three real directions and seven of noise. Risk: 3.2 can read
as rote 2x2 arithmetic; keep it tied to "what these numbers tell you about the
transformation," and get to Ames and n > 2 quickly. Second risk: the orthogonality
argument in 3.4 can bog down; keep it honest but low-machinery, intuition first.

## Code plan

Extend the cumulative library from Ch 1 and Ch 2 (Ch 1 is written last; assume the
load, vector-ops, and standardization modules exist and stub if needed). Add:

- second-moment / Gram matrix construction X-transpose-X from the standardized Ames
  matrix,
- power iteration (dominant eigenvector and eigenvalue, with a deflation note),
- eigendecomposition via numpy `linalg.eigh` for the symmetric case, contrasted with
  the hand-rolled power iteration,
- the rank-recovery routine for the capstone: eigendecompose `image_features`'
  second-moment matrix, sort the spectrum, read the rank off the gap above the noise
  floor.

Figures (SVG, chapter `figures/`): invariant directions under a 2x2 map (3.1);
eigenbasis as the coordinate system a matrix is diagonal in (3.3); orthogonal
eigenvectors of a symmetric matrix as perpendicular axes (3.4); the eigenvalue
spectrum of `image_features` showing the rank-3 cliff above the noise floor (3.6).
Checkpoint deliverable: a recovered rank for `image_features` and a dominant Ames
eigendirection, both computed without a black-box eigensolver.
