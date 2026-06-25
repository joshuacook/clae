---
title: "Ch 6 Notes: Covariance, Correlation, and Cross-Correlation"
type: chapter-notes
chapter: 6
status: draft
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 6 Notes: Covariance, Correlation, and Cross-Correlation

Co-produced with `chapter_outlines/clae-chapter-06.md`, built from
`chapter_notes/clae-chapter-06-source-map.md`. The *why* behind the chapter.

## Role in the book

The structural center of Part II and the hinge of the whole book. Ch 4 made the
data a random vector; Ch 5 gave us the expectation operator and the conditional
mean. This chapter applies that operator to second moments and produces the one
object the estimation half is built on: the covariance matrix. Everything
downstream consumes it. PCA (Ch 10) is the eigendecomposition of this matrix;
LMMSE (Ch 12) is written in covariance and cross-covariance; the Part II capstone
(Ch 8.7) estimates it from data and hands it forward. The chapter's job is to make
the covariance matrix a familiar, geometric, computable object before any
estimator asks for it.

## Entry and exit state

**Entry:** the reader has the expectation operator and its linearity (Ch 5), the
random vector and its mean vector (Ch 4), and standardization as a linear
transformation (Ch 2.5). From Part I they have the symmetric eigenproblem (Ch 3.4,
spectral theorem) and projection (Ch 2.3). They have not yet seen a second-moment
matrix as a statistical object.

**Exit:** the reader can (1) write the covariance matrix as an expectation and read
its entries, (2) explain why it is symmetric positive semidefinite and what its
eigenstructure says about the spread of the data, (3) normalize covariance to
correlation and read a correlation matrix, (4) define and compute the
cross-covariance between two distinct random vectors, (5) estimate covariance from
a finite sample with the right bias correction, and (6) compute and visualize all
three on real data, in code, on Ames.

## Narrative arc

Variance measures spread in one dimension; covariance is the natural extension to
many, and the covariance matrix collects every pairwise second moment into one
object. That object is not just a table of numbers: it is a piece of geometry (the
spread ellipsoid), and its eigenstructure names the directions the data varies in,
the first quiet sighting of PCA. Covariance carries the units of its variables, so
we normalize it to correlation to compare relationships on a common scale. Then we
ask a new question the single-vector view cannot answer: how do two *different*
random vectors covary? That is cross-covariance, and it is the object LMMSE will
need. Finally, none of these are known in practice; we estimate them from a finite
sample, which raises the bias question and plants the convergence seed for Ch 8.
Each section earns the next: the matrix needs its geometry, the geometry needs a
scale-free reading, the scale-free reading generalizes to two blocks, and all of it
has to survive contact with finite data.

## Key decisions

- **6.4 cross-correlation is net-new (author call, 2026-06-25).** No source defines
  or works the cross-covariance Cov(X, Y) between two distinct random vectors; L9
  only names the phrase in passing. The Cov(X, Y) = E[(X - mu_X)(Y - mu_Y)^T]
  definition, its non-square shape, its transpose relation Cov(Y, X) = Cov(X, Y)^T,
  and the worked example are written from scratch. This is the section that most
  needs care; it is also the section that pays the largest dividend (it is the
  literal object of the LMMSE estimator in Ch 12.3).
- **The stock_returns cross-correlation example requires a documented block split.**
  stock_returns.csv is a single 1000x10 matrix of generic `feature_1..feature_10`
  columns: synthetic, no tickers, no dates, no sector labels. It does not natively
  support cross-correlating two named blocks. Decision: impose a documented,
  explicitly-acknowledged split, partition the ten columns into block X (columns
  1 to 5) and block Y (columns 6 to 10) and compute the 5x5 cross-covariance
  Cov(X, Y) between them. The text states plainly that the partition is illustrative
  (the columns carry no real-world meaning), so the example teaches the *mechanics
  and shape* of cross-covariance without overclaiming a sector story. The honest
  framing is a feature: it models how a practitioner reasons about block structure.
- **All L10 worked examples re-anchor from iris to Ames.** Every number, ellipse,
  and figure in the covariance lesson (L10) uses iris. The theory transfers; the
  examples do not. Re-anchor onto Ames per the hero-dataset thread: a small set of
  Ames features (e.g. living area, lot area, year built, overall quality, sale
  price) carries the covariance and correlation worked examples and the ellipse
  picture. This is pervasive net-new work, not adaptation.
- **6.3 correlation is pulled forward from L11, not L10.** The covariance lesson
  never derives the correlation matrix. The rho_ij = Cov_ij / (sigma_i sigma_j)
  result, the standardized-covariance = R identity, and the in-[-1, 1] proof are in
  L11 (the feature-scaling lesson). Cite only the correlation result from L11;
  standardization-as-transform already lives in Ch 2.5, so 6.3 must not re-teach
  scaling or drift into L11's sklearn/ML framing.
- **6.2 holds to a covariance-eigenstructure preview; PCA is deferred to Ch 10.**
  L10 sec 2.1 over-reaches into the Ch 10 payload (fundamental subspaces,
  rotate-to-align, variance-explained, effective rank, "motivates PCA"). 6.2 keeps
  only the preview: eigenvectors are the axes of the spread ellipsoid, eigenvalues
  are the variance along those axes, the matrix is PSD so they are non-negative.
  Rotation, variance-explained, and rank recovery are explicitly held for Ch 10.
- **F-tests and noise simulation are out of scope.** L10 sec 3 (F-distribution,
  ANOVA across iris species) and sec 4 (noise simulation, signal-to-noise) are
  hypothesis testing, not covariance/correlation/cross-correlation. They route to
  Ch 8 (if anywhere) or are dropped. Not pulled into Ch 6.
- **6.5 keeps the sample-covariance convergence light; it seeds Ch 8.** The n vs
  n-1 bias correction and E[S] = Sigma belong here. The sample-size simulation
  (1/sqrt(n) error) from the L10 colab is named as a forward pointer to the Law of
  Large Numbers (Ch 8.3), not worked in full here, so 6.5 does not duplicate the
  convergence chapter.
- **HMD is not source for this chapter.** Despite the coverage tag, the HMD
  notebooks contain no covariance work (the grep is empty). The live Ames
  covariance/correlation source is the Ames case study 05-05, not HMD.

## Source posture

Adapt-heavy on 6.1, 6.2, 6.3, 6.5 (L10 theory and L11 correlation are turnkey,
modulo re-anchoring to Ames and the cross-lesson pull). Net-new on 6.4
(cross-covariance theory) and on the cross-correlation half of 6.6 (the
stock_returns block split). Active re-anchoring (iris to Ames) runs through every
worked example. Firm scope cuts hold PCA out of 6.2 and F-tests out entirely.
Detail in the source map.

## Forward and back wiring

- **Back:** uses the expectation operator and its linearity (Ch 5.1); uses the
  random vector and mean vector (Ch 4.3); uses standardization as a linear
  transformation (Ch 2.5) for the correlation normalization; uses the symmetric
  eigenproblem and spectral theorem (Ch 3.4) for the PSD eigenstructure; uses
  projection geometry (Ch 2.3) lightly for the ellipsoid intuition.
- **Forward:** the covariance matrix is the central hand-off. 6.2's eigenstructure
  preview is paid off as PCA in Ch 10.2 (eigendecomposition of the covariance).
  6.4's cross-covariance Cov(X, Y) is the literal object of the LMMSE estimator
  (Ch 12.3) and of the orthogonality principle (Ch 12.2). 6.5's sample covariance
  and its bias seed the Law of Large Numbers (Ch 8.3) and are estimated in full at
  the Part II capstone (Ch 8.7), which outputs the covariance that Ch 10 consumes.
  The Gaussian ellipsoid (Ch 7.2) reuses 6.2's spread-ellipsoid picture.

## Engagement

The covariance-as-geometry reveal (the spread ellipsoid with eigenvector axes) is
the chapter's "aha," and it is the moment that quietly foreshadows PCA. The
correlation heatmap on Ames is the concrete, scannable payoff (the reader sees
living area and price light up). Risk: 6.4 cross-covariance can read as abstract
machinery with no motivation, since its payoff (LMMSE) is six chapters away. Keep
it grounded by stating the question in plain terms (how does one block of variables
move with another) and by being honest about the illustrative stock_returns split
rather than dressing it as a real sector story. Second risk: 6.5 estimation can
feel like a detour into statistics; tie it to a data question (how many homes do we
need before the covariance estimate is trustworthy) and point forward to Ch 8.

## Code plan

Extend the cumulative library. Building on Ch 2's standardized Ames feature matrix,
add: covariance matrix construction (centered data, np.cov), correlation matrix
(np.corrcoef, the standardized-covariance identity), eigendecomposition of the
covariance for the ellipse axes, and the cross-covariance routine on the
stock_returns block split. Figures: the spread ellipsoid with eigenvector axes
(SVG, on a 2D Ames feature pair), the Ames correlation heatmap (masked
lower-triangle), and the cross-covariance block diagram (SVG, showing the X/Y
partition and the non-square Cov(X, Y)). Checkpoint: an estimated Ames covariance
matrix and correlation matrix, the covariance object that Ch 8.7 and Ch 10 will
consume.
