---
title: "Ch 2 Outline: Matrices and Linear Transformations"
type: chapter-outline
chapter: 2
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 2 Outline: Matrices and Linear Transformations

Co-produced with `chapter_notes/clae-chapter-02.md`. Section-level content plan,
budgets sum to ~28 pp. Source verdicts per section are in the source map.

## 2.1 Matrices as transformations (~4 pp · adapt L2)

- A matrix as an action on a vector: T(x) = Ax; linearity, T(ax + by) = aT(x) + bT(y).
- The column picture: Ax is a linear combination of the columns of A (the chapter's spine).
- First example: the difference matrix (L2) as a concrete transformation of a vector.
- Figure: input vector mapped to output vector under A.

## 2.2 Operations and their two views (~4 pp · adapt L2, composition net-new)

- The matrix-vector product two ways: rows as dot products vs columns as combinations (worked, from L2's 3x2 example).
- Matrix-matrix product as **composition** of transformations (net-new).
- Transpose, identity, and the inverse as the undo of a transformation (preview only).

## 2.3 Geometric effects of transformations (~5 pp · net-new, projection-anchored)

- **Projection** onto a line and onto a subspace: the load-bearing case; idempotence; the orthogonal-residual picture.
- Rotation and scaling matrices for geometric intuition; shear as a brief aside.
- Why projection matters now: it is the geometry of least squares (Ch 11) and of PCA's variance directions (Ch 10).
- Figures: projection, rotation, scaling (SVG).

## 2.4 Systems of linear equations (~5 pp · adapt L2/L4, scope-disciplined)

- Ax = b and the column picture of solvability: is b in the span of A's columns? (L2)
- Invertibility: recovering x from b; the invertible vs non-invertible example and its column-plane geometry (L2).
- A light first look at **column space** and **null space** as the geometry of solvability; full four-subspaces treatment deferred to Ch 11.
- Brief: over- vs under-determined systems name the two estimation regimes, least squares (Ch 11) and PCA (Ch 10) (L4).

## 2.5 Standardization as a transformation (~4 pp · reframe L11/HMD to Ames)

- Centering and scaling as a linear (affine) transformation of the data matrix.
- Why it matters: comparability and variable importance (L11 motivation, reframed); the setup for covariance (Ch 6) and PCA (Ch 10).
- On Ames: standardize numerical features; note categorical handling briefly (HMD).

## 2.6 Implementation: transforming Ames features (~4 pp · adapt colab + HMD)

- Extend the library: apply a transformation, project, and standardize the Ames feature matrix.
- Code ported from L2/L4 colab and the HMD standardization/categorical notebooks, onto Ames.
- Before/after visualization of the standardized features.
- Checkpoint: a standardized, covariance-ready Ames feature matrix.

## 2.7 Summary and exercises (~2 pp)

- "By the end" recap tied to the chapter's exit state.
- Exercises: a seed set from L2 and the colab practice cells, plus net-new problems on projection and standardization.
- Forward to Ch 3: the standardized data is ready for eigenstructure.

## Open items for section-level work

- 2.3: choose the exact projection example (onto a single Ames feature direction vs a 2D subspace) when the section outline is produced.
- 2.5: decide how much categorical handling to show vs defer (lean: minimal, numerical-feature standardization is the point).
