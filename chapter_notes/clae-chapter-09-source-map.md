---
title: "Ch 9 Source Map"
type: chapter-source-map
chapter: 9
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 9 Source Map: Singular Value Decomposition

Source Assembly for Ch 9 (the Part III opener; the SVD bridge into PCA and the
pseudoinverse). Gathered from `source/coverage-by-chapter.md`: course L12 "SVD and
Covariance Analysis", ILA ch08 eigensystems, image_features (rank-3). Maps source
to the book-outline sections with a reuse verdict, then notes gaps. Feeds the Ch 9
notes+outline.

The "strong" tag is accurate for the *core decomposition* sections but optimistic
for the chapter as a whole: the real source is **L12 alone** (ILA ch08 is an empty
stub), L12 is a discursive lecture handout rather than book prose, roughly a third
of L12 is covariance material that belongs to **Ch 6**, and the chapter's headline
payoff (Eckart-Young low-rank approximation, 9.5) is essentially unsourced.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 9.1 Review: diagonalization and its limits (recall Ch 3; square/symmetric only) | L12 sec 0 ("Review of Diagonalization": A = PDP^-1, the find-the-decomposition steps, the explicit "only works when square / n independent eigvecs / real eigvals" limitations); L12 sec 1.3 ("Why not just use eigendecomposition?") | a clean review + the motivation for needing SVD | adapt (strong); this is well-pitched as an on-ramp. Trim the duplicated 2x2 diagonalization-plot walkthrough (already done in Ch 3). |
| 9.2 The SVD (U Sigma V-transpose; existence for any matrix; rotate-scale-rotate geometry) | L12 sec 1.1-1.2 (X = U Sigma V^T; per-matrix properties; "rotation-scaling-rotation" geometric reading; works for any rectangular/singular matrix); L12 four-fundamental-subspaces bullet list; `generate_svd_plots.py` (`plot_svd_example`) | the decomposition statement, the geometry, the "works for any matrix" framing | adapt (strong); but **existence is asserted, never proved** (no construction, no uniqueness discussion) -- net-new if the book wants a derivation. |
| 9.3 Singular values and rank (low-rank structure; truncation) | L12 sec 1.1.2 (singular values give rank = count of nonzero sigma, condition number, "basis for optimal low-rank approximation"); L12 sec 1.4 (sigma_i always real, non-negative, sorted) | rank-as-nonzero-singular-values, condition number, sorted-sigma intuition | adapt for the rank/condition-number content; **truncation itself is only named, not developed** -- the mechanics belong with 9.5 and are net-new. |
| 9.4 Computing the SVD (connection to eigendecomposition of A^T A and A A^T) | L12 sec 1.4 + sec 3.x (sigma_i = sqrt(lambda_i) of X^T X; X^T X = V Sigma^2 V^T, X X^T = U Sigma^2 U^T; right/left singular vectors = eigenvectors of X^T X / X X^T); L12 sec 2.1 (numpy.linalg.svd `full_matrices=False`; eigh-on-X^T X path to build U, s, Vh) | the eigendecomposition connection, both numerical recipes (svd and eigh) | adapt (strong); this is L12's most book-ready material. Carries a numerical-stability caveat ("avoid squaring the condition number") worth keeping. |
| 9.5 Low-rank approximation (Eckart-Young; recover image_features' rank 3, now via SVD) | **none of substance.** L12 says "basis for optimal low-rank approximation" and "image compression reveals dominant visual patterns" as one-line benefit bullets; never states Eckart-Young, never truncates-and-reconstructs, never touches image_features | a slogan, not a result | **net-new**: the Eckart-Young theorem, the truncated reconstruction X_k = sum_{i<=k} sigma_i u_i v_i^T, the optimality-in-Frobenius/spectral-norm statement, and the image_features rank-3 recovery via SVD are all absent. This is the chapter's headline payoff and is a write-from-scratch. |
| 9.6 *Implementation:* truncated SVD and rank recovery | L12 sec 2.1 (numpy svd, reconstruction check `U @ diag(s) @ Vh == X`, `TruncatedSVD`); L12 colab cells 4-8 (svd properties, orthogonality/reconstruction checks); image_features.csv (1000x10, generated rank-3 + 0.1 noise; ground-truth rank confirmed in project-1 `generate_datasets.py`) | runnable SVD + property checks + the dataset | adapt the SVD/property-check scaffolding; **the truncation-to-k and rank-recovery-on-image_features logic is net-new** (L12's only worked data are the 3x2 toy, a 2D MVN, and iris -- no image_features, no Ames). |
| 9.7 Sets up PCA (Ch 10) and the pseudoinverse (Ch 11); summary and exercises | L12 sec 1.2 bullet ("PCA: uses SVD of centered data"); L12 colab practice cells | a forward-pointer to PCA and a thin starter | adapt as seed; **the pseudoinverse forward-pointer is net-new** (L12 never mentions the pseudoinverse or least squares); mostly net-new exercises. |

## Gaps and conflicts

- **ILA ch08 is an empty stub.** Both `ch08-eigensystems.md` (a title +
  `\pagebreak`) and its `.html` carry zero content. The coverage table's "ILA ch08"
  credit is vapor; real source is **L12 only**. (Same finding as the Ch 3 map.)

- **9.5 Eckart-Young is unsourced -- and it is the chapter's headline.** L12 gestures
  at "optimal low-rank approximation" but never states or proves Eckart-Young, never
  shows truncated reconstruction, and never uses image_features. The outline's
  promise ("recover image_features' rank 3, now via SVD") is a deliberate new
  construction. Write the theorem, the truncation mechanics, and the rank-recovery
  demo from scratch.

- **~1/3 of L12 is Ch 6 covariance material, not SVD.** L12's title is "SVD *and
  Covariance Analysis*", and secs 3.1-3.3 ("Random Vectors", "Covariance Analysis",
  "Feature Scaling") plus the recurring "Cov -> Correlation / Var -> std" square-root
  analogy are covariance/correlation content owned by **Ch 6**. Pull only the narrow
  bridge (X^T X = V Sigma^2 V^T; sigma_i = sqrt(lambda_i)) into 9.4; leave the
  covariance-interpretation, loadings, and scaling-effects discussions to Ch 6. Do
  not import "variance explained" / "explained_variance_ratio" here -- that is Ch 10
  (PCA) vocabulary and pulling it forward creates the same dormancy/forward-reference
  risk flagged in the Ch 3 map.

- **L12 overlaps Ch 10 (PCA).** The iris scaling example computes
  `explained_variance_ratio` and first-component "feature importance" -- that is PCA,
  not SVD per se. Keep 9.x to the decomposition and its rank/approximation
  properties; defer the PCA reading of U/Sigma/V to Ch 10, which the outline already
  routes through SVD (10.3).

- **L12 is lecture handout, not prose; structurally noisy.** Heavy nested bullet
  lists, `\paragraph`/`\subparagraph` LaTeX, a mis-numbered "Why SVD is useful" list
  (jumps 1,2,4,5), and example-dense asides. Usable for content and code, but every
  section needs a full rewrite into book paragraphs.

- **Wrong datasets in every L12 example.** L12's worked data are a 3x2 toy matrix, a
  2D multivariate normal, and **iris** -- never Ames, never image_features. The book's
  recurring datasets do not appear in the source at all; 9.5/9.6 must be re-grounded
  on image_features (and the chapter re-anchored away from iris).

- **SVD existence is asserted, not derived (9.2).** L12 states X = U Sigma V^T and
  its properties but offers no construction or uniqueness discussion. If the book
  wants existence (even via the symmetric eigendecomposition of X^T X), that is
  net-new.

- **No pseudoinverse anywhere (9.7).** L12 never mentions the Moore-Penrose
  pseudoinverse or least squares, so the Ch 11 forward-pointer is net-new (the actual
  pseudoinverse treatment lives in Ch 11 / ILA ch04).

## Implication for the chapter outline

The 7-section sequence holds, but the work splits cleanly into a well-sourced front
half and a net-new payoff:

- **Adapt (real L12 source):** 9.1 (review/limits), 9.2 (decomposition + geometry,
  existence aside net-new), 9.3 (rank, condition number), 9.4 (eigendecomposition
  connection + numerical recipes -- L12's most book-ready material), and the SVD
  scaffolding of 9.6. All need a prose rewrite out of the lecture-bullet format.
- **Net-new:** 9.5 (Eckart-Young + truncation + image_features rank-3 recovery -- the
  priority write, it is the chapter's reason for existing), the image_features
  re-grounding of 9.6, and the pseudoinverse forward-pointer in 9.7.

Two structural cautions. First, **strip the covariance half of L12**: secs 3.1-3.3,
the Var/Cov square-root analogy, loadings, and scaling-effects belong to Ch 6 (and
"variance explained" to Ch 10) -- importing them here duplicates Ch 6 and leaks PCA
forward. Keep only the X^T X = V Sigma^2 V^T bridge in 9.4. Second, **re-anchor onto
image_features**: L12 demonstrates everything on iris, but the book's promise is the
rank-3 recovery, so 9.5-9.6 must be rebuilt on image_features. Note this is the
*second* recovery of image_features' rank 3 -- Ch 3.6 does it by eigendecomposition
of the second-moment matrix; Ch 9.5 must do it via SVD and explicitly call back to
Ch 3 (the outline intends this contrast, but the source supports neither pass, so
coordinate the two so they read as a deliberate before/after, not a repeat).

Net assessment: Ch 9 is adapt-heavy on the decomposition mechanics (9.1-9.4, 9.6
scaffolding) but net-new on the payload (9.5 Eckart-Young + rank recovery). The
"strong" tag reflects L12's solid coverage of *what the SVD is*; it overstates
coverage of *what the SVD is for* in this book (low-rank approximation), and a third
of L12's bulk is Ch 6 covariance content that must be removed, not adapted. ILA ch08
contributes nothing.
