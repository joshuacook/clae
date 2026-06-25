---
title: "Ch 3 Outline: Eigenvalues, Eigenvectors, and Diagonalization"
type: chapter-outline
chapter: 3
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 3 Outline: Eigenvalues, Eigenvectors, and Diagonalization

Co-produced with `chapter_notes/clae-chapter-03.md`. Section-level content plan,
budgets sum to ~30 pp. Source verdicts per section are in
`chapter_notes/clae-chapter-03-source-map.md`.

## 3.1 The eigenvalue problem (~4 pp · adapt L7)

- The question: for a transformation A, which directions does A leave invariant,
  scaling but not rotating them? Av = lambda v as "this direction is special."
- Why this matters: special directions reveal the structure of the action; the
  matrix is, in some sense, *about* them.
- First example: the [[2,1],[1,2]] stretch (L7's best material), showing two
  invariant directions and their stretch factors geometrically.
- The derivation of the condition: (A - lambda I)v = 0 must have a nonzero solution,
  which ties straight back to Ch 2.4 (a nonzero null space means A - lambda I is
  singular).
- **Figure 3.1:** input vectors under a 2x2 map; the invariant directions stay on
  their own line while others rotate off.
- Dataset: none (geometric 2x2).

## 3.2 Finding eigenvalues and eigenvectors (~5 pp · adapt L7, derivation rewritten)

- The characteristic polynomial via det(A - lambda I) = 0 (rewrite of L7's
  non-standard dependent-equations trick; this is the standard, generalizable path).
  For 2x2: lambda^2 - (a+d)lambda + (ad - bc) = 0, recovered from the determinant.
- Worked 2x2 examples adapted from L7: a direct case and an upper-triangular case
  (eigenvalues on the diagonal).
- At least one net-new n >= 3 worked case (a 3x3) so the method visibly generalizes
  past the source's 2x2 ceiling.
- Eigenspaces; algebraic vs geometric multiplicity (L7's vocabulary); the defective
  [[2,2],[2,2]]-style case where geometric < algebraic.
- Source verdict: adapt with rewrite of the derivation; the determinant framing and
  the n > 2 case are net-new.
- Dataset: small Ames sub-example (a 2-feature or 3-feature transformation matrix) to
  keep it from reading as pure arithmetic.

## 3.3 Diagonalization (~4 pp · adapt L7)

- The eigenbasis: stack independent eigenvectors as columns of P, then
  P-inverse A P = Lambda is diagonal. The matrix is *diagonal in its own
  eigenbasis*, the chapter's "aha."
- The change-of-basis reading (partly net-new; L7's interpretation is thin): A acts
  by going into eigen-coordinates, scaling each axis by its eigenvalue, and coming
  back.
- Worked example adapted from L7 ([[1,2],[2,4]] or similar), carried through P,
  Lambda, P-inverse.
- When it exists: n independent eigenvectors required; algebraic = geometric
  multiplicity; the not-diagonalizable (defective) case named, pointing forward to
  why SVD (Ch 9) will rescue the general matrix.
- **Figure 3.2:** the eigenbasis as the coordinate grid in which A is a pure
  axis-aligned scaling.
- Dataset: none (worked matrix).

## 3.4 Symmetric matrices and the spectral theorem (~5 pp · net-new)

- The result: a real symmetric matrix has real eigenvalues, has an orthogonal set of
  eigenvectors, and is always diagonalizable. Orthogonal diagonalization
  A = Q Lambda Q-transpose with Q orthogonal.
- Why real eigenvalues: a short, honest argument (the symmetric quadratic form is
  real). Why orthogonal eigenvectors: the low-machinery argument from distinct
  eigenvalues, intuition first, kept from bogging down.
- Why this is the chapter's payload: the matrices the rest of the book cares about,
  second-moment and covariance matrices, are symmetric by construction, so their
  eigen-directions are guaranteed orthogonal and their eigenvalues real and (for PSD)
  nonnegative. Seed PSD here.
- Guard: state the result and its consequences without using the word "covariance"
  or any probability; name the forward payoff as "Part II" only. Protects 3.6 and the
  Part II openings.
- Source verdict: net-new; L7 offers only a 3-bullet unproved aside. Priority write.
- **Figure 3.3:** orthogonal eigenvectors of a symmetric 2x2 as perpendicular axes,
  contrasted with the skew eigenvectors of a non-symmetric matrix.
- Dataset: a small symmetric Ames second-moment block as the concrete instance.

## 3.5 Implementation: power iteration on Ames' second-moment matrix (~4 pp · net-new)

- Construct the second-moment matrix M = X-transpose-X from the standardized,
  centered Ames feature matrix handed over by Ch 2.6 (this construction appears in no
  lesson). Note it is symmetric and PSD, tying back to 3.4.
- Power iteration from first principles: repeated multiplication v <- Mv / ||Mv||
  amplifies the component along the dominant eigenvector; the Rayleigh quotient
  recovers its eigenvalue. Built from the eigenvalue definition, not a black box.
- Contrast with numpy `linalg.eigh` (the symmetric eigensolver) to validate the
  hand-rolled result; a brief deflation note for the next eigenvector.
- **Listing 3.1-3.3:** second-moment construction; power iteration; validation
  against `eigh`.
- Source verdict: net-new (algorithm and the Ames second-moment construction both
  new).
- Dataset: standardized Ames feature matrix from 2.6.

## 3.6 Part I capstone, Geometry of Real Data (~5 pp · net-new framing)

- The task: `image_features` is 1000x10, generated rank 3 plus 0.1 noise. Recover the
  rank by eigendecomposition alone, before any probability.
- The procedure: form the second-moment / Gram matrix X-transpose-X, eigendecompose
  it (now justified by 3.4 as symmetric PSD with a real, orthogonal spectrum), sort
  the eigenvalues, and read the rank off the cliff: three large eigenvalues, seven
  near-zero at the noise floor.
- The running-thread moment: noisy 10-dimensional data, and linear algebra cleanly
  separates three directions of real structure from seven of noise, with zero
  statistical machinery.
- Guard the pre-probability promise: use raw second-moment / Gram language only;
  explicitly defer "covariance" and "PCA" to Part II. State plainly that the *same*
  rank-3 recovery returns in Ch 9 via the SVD (Eckart-Young) and in Ch 10 via PCA,
  the deliberate eigen-then-SVD pairing.
- **Figure 3.4:** the sorted eigenvalue spectrum of `image_features`, the rank-3
  cliff above the noise floor.
- **Listing 3.4:** the rank-recovery routine end to end.
- Source verdict: net-new framing; dataset exists and is genuinely rank-3, the
  probability-free procedure does not.
- Dataset: `image_features.csv`.

## 3.7 Summary and exercises; forward to SVD (~3 pp · adapt L7 problem bank)

- "By the end" recap tied to the chapter's exit state (eigenvalue problem,
  characteristic polynomial, diagonalization, spectral theorem, power iteration,
  rank recovery).
- The limits of what we have: diagonalization needs square matrices and an eigenbasis
  that defective and non-square matrices do not provide. Name SVD (Ch 9) as the
  generalization that handles any matrix, and the reunion with PCA (Ch 10).
- Exercises: seed from L7's 2x2 problem bank (eigenvalue, diagonalization, defective
  cases), plus net-new problems on the determinant derivation, a 3x3 case, the
  spectral theorem, and a small rank-recovery exercise on a synthetic matrix.
- Dataset: small synthetic matrices; a reduced `image_features` slice for the
  rank-recovery exercise.

## Page budget

| Section | Pages |
|---|---|
| 3.1 The eigenvalue problem | 4 |
| 3.2 Finding eigenvalues and eigenvectors | 5 |
| 3.3 Diagonalization | 4 |
| 3.4 Symmetric matrices and the spectral theorem | 5 |
| 3.5 Implementation: power iteration | 4 |
| 3.6 Capstone: Geometry of Real Data | 5 |
| 3.7 Summary and exercises | 3 |
| Total | 30 |

## Open items for section-level work

- 3.2: pick the exact 3x3 net-new example (clean integer eigenvalues vs a mild Ames
  block) when the section pair is produced.
- 3.4: decide how much of the orthogonality argument to show in full vs state with a
  pointer; lean low-machinery, intuition first.
- 3.5: decide whether to show one deflation step for the second eigenvector or only
  name it; lean name-and-defer to keep the section at 4 pp.
- 3.6: confirm `generate_datasets.py` noise scale (0.1) so the eigenvalue-cliff
  figure shows a clean gap; confirm the exact column count fed to X-transpose-X.
