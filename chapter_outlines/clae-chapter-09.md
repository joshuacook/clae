---
title: "Ch 9 Outline: Singular Value Decomposition"
type: chapter-outline
chapter: 9
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 9 Outline: Singular Value Decomposition

Co-produced with `chapter_notes/clae-chapter-09.md`. Section-level content plan,
budgets sum to ~30 pp. Source verdicts per section are in
`chapter_notes/clae-chapter-09-source-map.md`. Source is **L12 only** (ILA ch08 is
an empty stub). Adapt the decomposition mechanics (9.1-9.4, 9.6 scaffolding);
write the payload from scratch (9.5, the image_features re-grounding, the
pseudoinverse pointer).

## 9.1 Review: diagonalization and its limits (~4 pp · adapt L12 sec 0, 1.3)

- Recall Ch 3: A = PDP-transpose-inverse, the eigenbasis, and the spectral theorem for symmetric matrices (real eigenvalues, orthogonal eigenvectors). Brief, as a wake-up, not a re-teach.
- The three walls: diagonalization needs a **square** matrix, **n independent eigenvectors** (else not diagonalizable), and real eigenvalues for a clean real picture. Real data matrices are rectangular, so the first wall is fatal.
- "Why not just use eigendecomposition?" (L12 sec 1.3): the motivation for a factorization that works on any matrix.
- Trim the 2x2 diagonalization-plot walkthrough already done in Ch 3; reference it, do not repeat it.
- Opens Part III by recalling Part I exactly where Part III needs it.

## 9.2 The SVD (~5 pp · adapt L12 sec 1.1-1.2; existence aside net-new)

- The decomposition: any matrix A (m x n) factors as A = U Sigma V-transpose, with U (m x m) and V (n x n) orthogonal and Sigma (m x n) diagonal with non-negative entries.
- The geometry: **rotate (V-transpose), scale (Sigma), rotate (U)**. The unit sphere maps to an ellipsoid whose axes are the singular values. The chapter's visual spine.
- "Works for any matrix": rectangular, singular, rank-deficient, all admit an SVD. The relief after 9.1's walls.
- A brief existence argument (net-new): the eigenvectors of A-transpose-A give V, the square roots of its eigenvalues give the singular values, U follows. Uniqueness up to sign and ordering, stated as a remark. Full construction deferred to 9.4.
- The four fundamental subspaces in one breath (column space, null space, row space, left null space read off U and V), light, as orientation; full treatment is Ch 11.
- Figure: the rotate-scale-rotate action of the SVD on the unit circle/sphere (SVG, adapting generate_svd_plots.py).

## 9.3 Singular values and rank (~4 pp · adapt L12 sec 1.1.2, 1.4)

- Singular values are **real, non-negative, and sorted** (sigma_1 >= sigma_2 >= ... >= 0). Why: they are square roots of eigenvalues of a PSD matrix.
- **Rank = number of nonzero singular values.** Low-rank structure shows up as a cliff in the sorted spectrum, where singular values drop to (near) zero.
- The condition number as sigma_max / sigma_min; what it says about sensitivity.
- Truncation, named but not yet developed: keeping the largest k singular values is the route to low-rank approximation. Hands directly to 9.5.
- Figure: a sorted singular-value spectrum (preview, generic), pointing toward the image_features cliff in 9.5/9.6.

## 9.4 Computing the SVD (~4 pp · adapt L12 sec 1.4, 2.1, 3.x bridge only)

- The eigendecomposition connection: A-transpose-A = V Sigma-squared V-transpose and A-A-transpose = U Sigma-squared U-transpose. Right singular vectors are eigenvectors of A-transpose-A; left singular vectors of A-A-transpose; sigma_i = sqrt(lambda_i).
- This is the construction promised in 9.2, and it reuses the symmetric eigendecomposition the reader owns from Ch 3.4.
- **Strip caution:** treat A-transpose-A as a purely algebraic second-moment / Gram object. Do *not* re-teach covariance (Ch 6) or import the Var/Cov square-root analogy, loadings, or feature scaling from L12. The narrow algebraic bridge only.
- Numerical recipes: numpy.linalg.svd (full_matrices=False) as the default; the eigh-on-A-transpose-A path as the alternate. The stability caveat (L12): prefer svd directly to avoid squaring the condition number.

## 9.5 Low-rank approximation (~6 pp · **net-new**, the headline)

- The **truncated SVD**: X_k = sum_{i<=k} sigma_i u_i v_i-transpose, the sum of the first k rank-one outer products.
- The **Eckart-Young theorem**: X_k is the *best* rank-k approximation of X, minimizing the approximation error in both Frobenius and spectral norm; the residual error equals the dropped singular values. State it; argue it at graduate-text altitude, not a full proof.
- Why this is the chapter's reason for existing: truncation is provably optimal, not a heuristic.
- **Recover image_features' rank 3 via SVD:** the singular-value spectrum shows three large values and a noise floor; truncating at k=3 reconstructs the planted structure and the residual matches the 0.1 noise.
- **Before/after with Ch 3.6 (explicit callback):** Ch 3.6 found rank 3 by eigendecomposition of the second-moment matrix; here we find it by SVD of the data matrix directly. Same structure, two roads. The SVD road needs no Gram matrix (no condition-number squaring) and yields the *approximation*, not just the rank count.
- Figures: image_features singular-value spectrum with the rank-3 cliff; reconstruction-error-versus-k curve flattening at k=3 (Eckart-Young made visual).

## 9.6 Implementation: truncated SVD and rank recovery (~4 pp · adapt L12 colab scaffolding + net-new truncation on image_features)

- Extend the library: compute the SVD (numpy svd, full_matrices=False), verify the property checks (orthogonality of U and V, reconstruction U @ diag(s) @ Vh == X), adapted from L12 colab cells.
- Net-new: the truncate-to-k routine and the rank-recovery run on image_features (1000x10, generated rank-3 plus 0.1 noise; ground truth in project-1's generate_datasets.py). Optional 3x2 hand-computable toy as a warm-up before the real data.
- Plot the singular-value spectrum and the reconstruction-error curve from 9.5.
- Checkpoint: reconstruct image_features at k=3 and confirm the residual error matches the planted noise floor; confirm rank from the spectrum.

## 9.7 Sets up PCA and the pseudoinverse; summary and exercises (~3 pp · adapt seed + net-new pointers)

- "By the end" recap tied to the exit state.
- Forward to **Ch 10 PCA**: PCA is the SVD of the centered data matrix; principal directions are right singular vectors (the eigenvalues = singular values squared over (n-1) detail is flagged, used in Ch 10, not here). Pointer only; no variance-explained vocabulary.
- Forward to **Ch 11 pseudoinverse** (net-new): the SVD inverts the invertible part of a matrix's action, which solves the least-squares / over-determined system. The Moore-Penrose pseudoinverse is built from U, Sigma, V.
- Exercises: net-new, on the geometry (read an SVD off an ellipse), rank and condition number, truncation error versus k, and a hand SVD of a small matrix via A-transpose-A. Seed from L12 practice cells where usable.

## Dataset

**image_features** (1000 x 10, synthetic, generated rank-3 plus 0.1 noise; ground
truth confirmed in project-1 `generate_datasets.py`). The chapter's anchor for
9.5-9.6. This is the *second* recovery of its rank 3: Ch 3.6 does it by
eigendecomposition of the second-moment matrix; Ch 9.5 does it by SVD of the data
matrix, as a deliberate before/after. A small 3x2 toy matrix may serve as a
hand-computable warm-up in 9.2/9.6. **No iris** (L12's example dataset is dropped).
**No Ames** in this chapter.

## Figures

1. The rotate-scale-rotate geometry of the SVD on the unit circle (9.2, SVG, adapt generate_svd_plots.py).
2. A generic sorted singular-value spectrum showing a rank cliff (9.3, preview).
3. image_features singular-value spectrum with the rank-3 cliff (9.5/9.6).
4. Reconstruction-error-versus-k curve flattening at k=3 (9.5, Eckart-Young made visual).

## Page budget

| Section | Pages |
|---|---|
| 9.1 Review: diagonalization and its limits | 4 |
| 9.2 The SVD | 5 |
| 9.3 Singular values and rank | 4 |
| 9.4 Computing the SVD | 4 |
| 9.5 Low-rank approximation (Eckart-Young) | 6 |
| 9.6 Implementation: truncated SVD and rank recovery | 4 |
| 9.7 Sets up PCA and the pseudoinverse; summary and exercises | 3 |
| **Total** | **30** |

## Open items for section-level work

- 9.2: decide how much of the existence argument to show inline versus defer the full construction to 9.4 (lean: state it in 9.2, construct it in 9.4, no duplication).
- 9.4: confirm the exact narrow boundary of the A-transpose-A bridge so no covariance interpretation leaks in from L12; coordinate with the Ch 6 author on terminology (second-moment / Gram, not covariance).
- 9.5: fix the precise framing of the Ch 3.6 callback with the Ch 3 author so the diptych reads as planned before/after, not repetition; settle whether the error-versus-k curve or the spectrum is the lead figure.
- 9.7: scope the pseudoinverse pointer so it sets up Ch 11 without pre-teaching it (name the idea, defer the derivation).
- Exercises: confirm none require iris or covariance; keep all on image_features, the toy, or pure-linear-algebra prompts.
