---
title: "Ch 10 Source Map"
type: chapter-source-map
chapter: 10
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 10 Source Map: Principal Component Analysis (capstone)

Source Assembly for Ch 10, the richest-source chapter and Part III capstone.
Gathered from `source/coverage-by-chapter.md`: course L13/L14, the pca-tutorial
case study, the wholesale case study, image_features, project-1
(handouts/milestones/datasets), PCAt repo, ILA ch09. Maps source to the
book-outline sections with a reuse verdict, then notes the (substantial) gaps and
conflicts. The headline finding: the *volume* is real but most of it is one
artifact (the pca-tutorial case study); several named sources are stubs.

## What each source actually is

- **L13 (PCA Foundations):** **absent.** `lessons/013/` is an empty directory. No
  `013_math.md`, no colab. The "foundations" half of the course PCA pair does not exist.
- **L14 (PCA Implementation):** a bare lecture **skeleton** (`014_math.md`), bullet
  headings only ("Direct SVD method", "Eigendecomposition method", subspace
  framing). No prose, no worked math, no code. Topic inventory, not content.
- **pca-tutorial case study:** the real source. Nine notebooks deriving PCA from
  TSS to variance to covariance to eigendecomposition, on Iris and the
  ball-on-spring (Shlens 2014). This is where the chapter's math lives.
- **wholesale case study:** applied sklearn PCA on deskewed/outlier-removed/scaled
  data; loadings, scree, and segmentation. Segmentation is **GMM + BIC**, not PCA.
- **PCAt repo:** a thinner duplicate of the pca-tutorial notebooks; README just
  points to the Shlens arXiv paper and a YouTube playlist. No net-new content.
- **ILA ch09:** a **stub** ("# Unsupervised Learning\n\\pagebreak", 36 bytes). Nothing.
- **project-1:** framed as **"Statistical Estimation through SVD Analysis"** on the
  three synthetic datasets (stock_returns, sensor_readings, image_features), heavy
  on the four-fundamental-subspaces (FTLA) framing and sampling/convergence. Rich,
  but pointed at SVD/estimation, not at Ames/wholesale PCA.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 10.1 Directions of maximum variance | pca-tutorial nb02/05 (change-of-basis, variance-as-goal, ball-on-spring, rotation toy); L14 skeleton | strong motivation + the canonical 2D toy | adapt (strong); port the synthetic 2D demo to Ames intuition |
| 10.2 PCA via eigendecomposition of covariance | pca-tutorial nb04/06 (TSS to variance to covariance to `np.linalg.eig`; the explicit 5-step recipe; explained variance = eigenvalues) | the chapter's mathematical spine, fully worked | adapt (turnkey); **reframe data from Iris to Ames** to consume Part II covariance |
| 10.3 PCA via SVD of centered data (equivalence) | L14 skeleton (lists "Direct SVD: X=UΣVᵀ"); project-1 (SVD framing) | a *claim* of equivalence, not a derivation | **net-new derivation.** No source proves eigenvalues = singular-values²/(n-1); see conflict below |
| 10.4 PCA as an estimator (sample to estimated, callback to Ch 8) | project-1/milestone1 (sample covariance from first principles; bias/consistency; convergence with sample size) | the estimator framing + convergence story | adapt; **only source for the estimator lens** |
| 10.5 Choosing dimensionality (variance explained; scree) | pca-tutorial nb08 (scree, elbow, cumulative ratio, "ad hoc" caveat); project-1/final (elbow/Kaiser/percent-variance trio) | scree + selection methods | adapt (strong); image_features rank-3 check is net-new wiring |
| 10.6 The ML bridge (whitening, dim reduction, learned features) | pca-tutorial nb01/02 (sklearn PCA, digits visualization, inverse_transform); wholesale (loadings, pipelines) | sklearn idiom + visualization | adapt; **whitening is net-new** (no source covers it) |
| 10.7 Project capstone (Ames cov PCA; wholesale segmentation; full project-1 pipeline) | project-1 (handouts/milestones/datasets); wholesale; pca-tutorial Ames data (`ames_features.p`) | a full graded pipeline | **adapt with major reframe** (see conflicts: datasets and SVD-framing mismatch) |
| 10.8 Summary and exercises | pca-tutorial practice cells; project-1 deliverables | exercise seeds | adapt as seed; mostly net-new |

## Gaps and conflicts

- **Redundancy is concentrated, not distributed.** The "richest source" label is
  carried almost entirely by *one* artifact, the pca-tutorial case study. PCAt is a
  duplicate of it; ILA ch09 and L13 are empty; L14 is a skeleton. Effective source
  is: pca-tutorial (deep), wholesale (applied), project-1 (estimation framing). Three
  artifacts, not seven.

- **Eigendecomposition vs SVD: the central unresolved conflict.** The course is
  internally inconsistent on which decomposition *is* PCA.
  - pca-tutorial nb06 states it flatly: "A PCA is the EigenDecomposition of the
    **population** covariance matrix," with a 5-step recipe that divides Aᵀ_cA_c by
    **n** (population).
  - L14 skeleton and project-1 lead with **SVD** (X = UΣVᵀ) as the "direct method."
  - No source contains the bridge the outline's 10.3 promises (eigenvalues =
    singular-values²/(n-1)). 10.3 must be written from scratch, and it must *resolve*
    the n-vs-(n-1) inconsistency the sources leave open.

- **The n vs n-1 normalization is genuinely inconsistent across sources.**
  pca-tutorial nb06 says sklearn PCA uses the **population** covariance (÷n) and
  derives PCA on ÷n; pandas `.cov()` uses ÷(n-1); the notebook fudges the gap with
  `*149/150` rescalings. project-1/milestone1 derives the **sample** covariance (÷(n-1))
  "from first principles." The book must pick one convention and state it once;
  the outline's "/(n-1)" in 10.3 commits to sample, which contradicts nb06's ÷n recipe.

- **Capstone dataset mismatch.** Outline 10.7 says "Ames covariance PCA; wholesale
  segmentation; full project-1 pipeline." But **project-1 runs on synthetic
  stock_returns / sensor_readings / image_features**, not Ames or wholesale. The
  Ames PCA exists only as pickled data in the pca-tutorial repo (`ames_features.p`),
  with no worked Ames PCA notebook. "Full project-1 pipeline" and "Ames covariance
  PCA" are two different deliverables; the outline conflates them.

- **project-1 is an SVD/estimation project, and it overlaps Ch 9.** Its title is
  "Statistical Estimation through SVD Analysis"; deliverables are SVD of the sample
  covariance, FTLA subspaces, convergence. That is as much Ch 9 (SVD) and Ch 8
  (convergence) as Ch 10. Using it whole as the Ch 10 capstone risks re-teaching SVD
  and importing the four-subspaces framing the book has deliberately deferred to Ch 11.

- **Wholesale "segmentation" is not PCA.** The segmentation notebook clusters with a
  Gaussian Mixture Model scored by BIC; PCA is only an upstream preprocessing option
  among 24 pipelines. Framing it as "wholesale segmentation via PCA" overstates PCA's role.

- **Net-new despite the volume:** the SVD/eigen equivalence proof (10.3), whitening
  (10.6), the estimator-convergence callback to Ch 8 (10.4 beyond project-1's sketch),
  and an actual worked Ames PCA. The toy data in the strongest source is Iris and a
  synthetic spring, not the book's Ames spine; reframing to Ames is pervasive work.

## Implication for the chapter outline

The section sequence holds; the work is heavier than "strong (richest)" implies.

- **10.2 is the turnkey core** (pca-tutorial nb04/06), but reframe Iris to Ames to
  pay off Part II's covariance.
- **10.3 is net-new and load-bearing:** it must derive the SVD/eigendecomposition
  equivalence *and* fix the n-vs-(n-1) convention the sources leave inconsistent.
  Resolve it once here and propagate.
- **Split the 10.7 capstone honestly.** It currently bundles three different things.
  Recommend: anchor the capstone on the **project-1 pipeline as-is** (synthetic
  datasets, the graded artifact that actually exists), demote "Ames covariance PCA"
  to a worked example in 10.2/10.5 (build the missing Ames notebook), and reframe
  "wholesale segmentation" as a PCA-as-preprocessing vignette (the clustering is GMM,
  not PCA).
- **Guard the Ch 9 boundary.** project-1 is SVD-first; keep Ch 10's capstone use of
  it pointed at the covariance-eigendecomposition and dimensionality-selection story,
  and route its SVD/FTLA content back to Ch 9/Ch 11 rather than re-teaching it here.

Net assessment: turnkey on 10.2 and 10.5 (one artifact carries them), net-new on
10.3, partial on 10.4/10.6/10.7. The chapter is well-sourced for the *mechanics* of
PCA and under-sourced for the two things the outline most wants from it: the SVD
equivalence and a clean Ames-anchored capstone.
