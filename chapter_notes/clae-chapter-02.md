---
title: "Ch 2 Notes: Matrices and Linear Transformations"
type: chapter-notes
chapter: 2
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 2 Notes: Matrices and Linear Transformations

Co-produced with `chapter_outlines/clae-chapter-02.md`, built from
`chapter_notes/clae-chapter-02-source-map.md`. The *why* behind the chapter.

## Role in the book

The first taught chapter. The Introduction establishes data as vectors and the
running thread; Ch 1 is a skim-first reference for the vector mechanics. Ch 2
makes matrices the **active objects**: a matrix is an action on the data vectors,
and that action is the seed of every estimator to come (projection becomes least
squares; standardization feeds covariance and PCA).

## Entry and exit state

**Entry:** the reader has read the Introduction (thread, Ames, data-as-vectors)
and can skim Ch 1 for vectors, inner product, norm. Comfort with vectors assumed.

**Exit:** the reader can (1) read a matrix as a transformation via the column
picture, (2) interpret transformations geometrically, projection above all, (3)
set up Ax = b and reason about solvability and invertibility, and (4) standardize
a real dataset as a linear transformation, in code, on Ames.

## Narrative arc

A matrix is an array, then a matrix is an *action* (the column picture), then that
action has *geometry* (projection foreshadows estimation), then we ask when the
action is *invertible* (systems), then we put a real transformation to work
(standardize Ames). Each section earns the next: the column picture makes systems
legible; projection makes least squares inevitable later; standardization makes
covariance possible in Ch 6.

## Key decisions

- **2.3 is net-new, projection-anchored** (author call, 2026-06-25). Projection is
  the load-bearing case (sets up Ch 10 PCA and Ch 11 least squares); rotation and
  scaling carry intuition; shear is a brief aside. Honors the geometric-first promise.
- **L4's four fundamental subspaces are deferred to Ch 11.** Ch 2 introduces column
  space and null space only lightly, as the geometry of solvability. Tagging L4 as
  primary source for Ch 11 avoids the introduce-early-use-late dormancy.
- **Standardization is reframed** from the source's ML/sklearn framing (L11) and
  Boston data (HMD) to "centering and scaling as a linear transformation" on Ames.
- **The column picture (Strang, via L2) is the spine.** Matrix-vector product as a
  combination of columns is the chapter's organizing idea.
- **Composition** of transformations (matrix-matrix product) is net-new.

## Source posture

Adapt-heavy on 2.1, 2.2, 2.4 (L2 is clean and aligned). Net-new on 2.3 and on
composition. Reframe on 2.5 (L11 motivation + HMD technique, ported to Ames).
Cautions: ILA ch01/ch02 are draft-grade; L11/HMD are off-frame. Detail in the
source map.

## Forward and back wiring

- **Back:** uses Ch 1 reference (vectors, inner product, norm); uses the
  Introduction's Ames framing.
- **Forward:** projection (2.3) to Ch 10/11; column/null space (2.4) to Ch 9/11;
  standardization (2.5) to Ch 6 (covariance needs centered data) and Ch 10 (PCA
  centering). 2.7 hands standardized, covariance-ready data toward Ch 3 and Part II.

## Engagement

The column-picture reveal is the chapter's "aha." Projection is the geometric hook
that quietly foreshadows estimation. Standardizing Ames is the concrete payoff.
Risk: 2.4 (systems) can read dry and abstract; keep it tied to a data question
(which feature relationships are recoverable, which are not), not to toy systems.

## Code plan

Extend the cumulative library begun in Ch 1 (note: Ch 1 is written last, so for now
Ch 2 assumes the load and vector-ops module exists and stubs it if needed). Add:
transformation application, projection, standardization, and before/after
visualization on Ames. Figures: projection, rotation, scaling as SVG in the
chapter's figures directory. Checkpoint: a standardized Ames feature matrix.
