---
title: "Ch 2 Source Map"
type: chapter-source-map
chapter: 2
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 2 Source Map: Matrices and Linear Transformations

Source Assembly for Ch 2 (first taught chapter). Gathered from
`source/coverage-by-chapter.md`: course L2/L3/L4/L11, Ames, ILA ch01-03, HMD.
Maps source to the book-outline sections with a reuse verdict, then notes gaps.
Feeds the Ch 2 notes+outline.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 2.1 Matrices as transformations | L2 (matrix-vector product as a column combination; the difference matrix as an operation) | the column picture; matrix as an action on a vector | adapt; the abstract T(x)=Ax linearity framing is partly net-new |
| 2.2 Operations and their two views | L2 (explicit row-wise vs column-wise multiplication; computing products as row dot-products) | both multiplication views, worked | adapt (strong); **composition of transformations is net-new** |
| 2.3 Geometric effects (rotation, scaling, projection, shear) | **none** | — | **net-new** (the course never teaches transformation geometry; L4 despite its title does not) |
| 2.4 Systems of linear equations | L2 (Ax=b, invertibility, a non-invertible matrix, the column-plane geometry); L4 (over/under-determined systems, the four fundamental subspaces); ILA ch02 (systems, draft) | rich: solvability, invertibility, column/null space | adapt **with scope discipline** (light column/null space only; defer the full four-subspaces treatment) |
| 2.5 Standardization as a transformation | L11 (why scale; standardization; variable importance); HMD (standardization code on Boston; Ames categoricals) | motivation + technique + code | adapt; **reframe** from ML/sklearn to "centering and scaling as a linear transformation"; port to Ames |
| 2.6 Implementation: transforming Ames features | L2 and L4 colab; HMD standardize + Create_Categorical notebooks | runnable transforms; an Ames pipeline | adapt (port Boston standardization to Ames; combine) |
| 2.7 Summary and exercises | L2 additional resources; colab practice cells | a starter exercise set | adapt as seed; mostly net-new |

## Gaps and conflicts

- **2.3 is net-new.** The course teaches matrices through the column-combination
  picture and systems, never through the geometric-transformation menagerie
  (rotation, scaling, projection, shear). No source covers it.
- **L4 is mis-titled.** "Linear Transformations and Their Applications" is actually
  over/under-determined systems and the four fundamental subspaces (column, row,
  null, left-null), framed toward least squares and PCA. Its real value is
  downstream (Ch 11 least squares, Ch 9-10 PCA), not Ch 2. Pulling all of it into
  2.4 would balloon the chapter and create the dormancy anti-pattern (introduce
  early, use five chapters later). Introduce column space and null space lightly in
  2.4; tag L4 as primary source for Ch 11 when we reach it.
- **L11 and HMD are off-frame.** L11 is ML/sklearn/logistic-regression-flavored on
  synthetic data; HMD standardization is on Boston, not Ames. Reuse the motivation
  and technique, but reframe standardization as a linear transformation and port to
  Ames.
- **ILA quality.** ch02 has an incomplete section ("NEED SECTION TITLE") and ch01 is
  TensorFlow-flavored; use cautiously.
- **Composition** of transformations (2.2) is net-new.

## Implication for the chapter outline

The section sequence mostly holds. The live decision is **2.3**: the course gives
no transformation geometry, so it is a deliberate net-new addition. Recommend
keeping it, because the book's promise is geometric intuition first, and because
**projection** specifically sets up Ch 11 (least squares) and Ch 10 (PCA); anchor
2.3 on projection, with rotation and scaling for intuition. Hold 2.4 to systems +
invertibility + light column/null space, deferring the four subspaces to Ch 11.

Net assessment: Ch 2 is adapt-heavy on 2.1, 2.2, and 2.4; net-new on 2.3 and
composition; reframe on 2.5. Strong source overall, but less turnkey than the
"strong" tag implies, and section 2.3 is a genuine write-from-scratch.

## Addendum (2026-07-11): the 2015 paper joins the source set

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 2.1 (the verb) | Cook, *Computational Methods in Molecular Quantum Mechanics* (Leanpub 2016) | `secondDiff` + the difference-matrix-as-derivative, with the author's own provenance | adapt; now the verb section's centerpiece exhibit |

Citation (pinned, affirmed): Joshua Cook, *Computational Methods in Molecular
Quantum Mechanics*, Leanpub, 2016 (submitted toward Chemistry 451, CSUN),
https://leanpub.com/computationalmethodsinmolecularquantummechanics

STATUS 2026-07-11: Ch 2 drafted in full
(`chapter_drafts/clae-chapter-02/2-matrices-and-linear-transformations.md`,
companion `clae-code/ch02/ch02.ipynb`, real numbers).
