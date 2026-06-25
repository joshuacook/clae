---
title: "Ch 1 Source Map"
type: chapter-source-map
chapter: 1
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 1 Source Map: Vector Spaces and Data Representation

Source Assembly for Ch 1 (per the CLAE source-first modification in
`writing-process.md`). Gathered from `source/coverage-by-chapter.md`: course L1
(+L5), Ames, ILA ch01/ch03/ch07, HMD. Maps source to the book-outline sections,
with a reuse verdict, then notes gaps. Feeds the Ch 1 notes+outline.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 1.1 Data as vectors: motivating problem | HMD (Ames context) | the dataset; a home as a feature record | net-new framing (write the thread hook; no source ties vectors to "recover structure from noise") |
| 1.2 Vector spaces, bases, independence | course L1 §I (def + axioms, R^2 example) | vector-space definition, the axioms | adapt axioms; **bases / independence / dimension is net-new** (L1 punts it to "looking ahead"; ILA ch07 is an empty stub) |
| 1.3 Vector operations and geometry | course L1 §II–III (add, scalar mult, subtraction, magnitude, dot product, angle, with tikz figures); ILA ch03 (inner product as a linear mapping) | full operation set + geometry + derivations + figures | adapt (strongest section) |
| 1.4 Representing a dataset | ILA ch01 (ndarray rank/shape/type; scalar to vector to matrix); HMD (numerical vs categorical features) | the numpy representation; the data matrix; Ames feature structure | adapt (use the numpy framing, drop the TensorFlow tangent and draft typos) |
| 1.5 Implementation: data-as-vectors on Ames | L1 colab (`plot_vector`, `vector_addition`, viz, `practice()`); HMD load notebook | runnable vector ops + visualization; Ames load | adapt (combine L1 ops + HMD load; trim HMD imputation to a load-only slice) |
| 1.6 Summary and exercises | L1 colab `practice()`; L1 math (none) | a starter exercise set | adapt as seed; mostly net-new |

## Gaps and conflicts

- **Under-sourced: vector-space structure.** Bases, linear independence, span, and
  dimension (1.2) have almost no clean source. ILA ch07 is a 3-line stub; L1 stops
  at the axioms. This is the chapter's real writing pocket despite the "strong" tag.
- **Elevation needed.** L1 is R^2 and elementary. The book needs Rⁿ and the
  data-representation angle (a dataset as a matrix of vectors), which the course
  does not frame.
- **ILA ch01 quality.** Draft-grade (typos, an incomplete sentence) and
  TensorFlow-flavored. Reuse the scalar/vector/matrix/tensor representation idea in
  numpy only; do not carry the TF material.
- **HMD scope.** The Ames-load notebook is preprocessing-heavy (NaN imputation,
  categoricals). Ch 1 needs only the load-and-represent slice; defer imputation.
- **Figures.** L1 has clean tikz geometric figures (addition, scalar multiple,
  subtraction, angle) that convert to the book's SVG figure style.
- **Thread.** Nothing in the source connects vectors to "recover structure from
  noisy, incomplete data." The 1.1 hook is net-new and carries the running thread.

## Implication for the chapter outline

The book-outline section sequence (1.1 to 1.6) holds. Two refinements for the Ch 1
notes+outline: 1.4 absorbs the ILA ch01 numpy-representation material, and 1.2
carries an explicit net-new load (bases / independence / dimension) rather than an
adapt. Net assessment: Ch 1 is adapt-heavy on 1.3 and 1.5, net-new on 1.1 and the
1.2 structure material.
