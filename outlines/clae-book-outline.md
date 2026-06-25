---
title: "CLAE Book Outline"
type: book-outline
status: draft
created: "2026-06-24"
updated: "2026-06-24"
---

# Computational Linear Algebra for Estimation: Book Outline

Linear algebra taught toward estimation, developed geometrically, then derived,
then implemented in Python. Running thread, planted in the Introduction and
revisited every chapter: *recover structure from noisy, incomplete data.*

A second thread, surfaced only where it earns its place: the bridge to machine
learning and data science (PCA whitening and learned features in Ch 10,
regularized least squares in Ch 11, modern filtering and learned dynamics in Ch 14).

Audience: graduate EE / applied math / data science, plus practicing SP and ML
engineers; assumes calculus, a first probability course, and basic Python (no
measure theory). Every chapter closes with a worked Python implementation and an
end-of-chapter problem set; Ch 10 and Ch 12 add extended project capstones.

Page budgets total ~426 pp; "strong" adapts existing material, "scratch" is
net-new. Per-chapter datasets and source detail: `source/coverage-by-chapter.md`.
Rationale and decisions: `clae-book-decisions.md`.

## Introduction (front matter, read first)

The book's on-ramp; not skippable. Carries the narrative that Ch 1's reference
cannot.

- Motivation: linear algebra texts stop at the mathematics; estimation texts assume it. This book bridges them.
- The running thread: *recover structure from noisy, incomplete data*, revisited every chapter.
- The data: Ames housing (the recurring hero), the synthetic sets (image_features, stock_returns, tracking), the case studies.
- The approach: data as vectors, then covariance, then estimation.
- Roadmap: the four parts and the two capstone arcs (PCA; LMMSE to Kalman); "by the end of this book."

## Part I: Linear Algebra Foundations

### 1. Vector Spaces and Data Representation (~28 pp · skim-first reference, written last)

Not skipped, skimmed: the reader skims this once to calibrate notation, then refers
back to it throughout the book. Written last, calibrated to the notation and
operations the book actually uses. Geometric depth for a specific operation is
taught just-in-time where a later chapter first needs it.

- 1.1 Vectors, vector spaces, and R^n (axioms)
- 1.2 Linear independence, basis, dimension, subspace (the load-bearing structure for rank and column space)
- 1.3 Norm, inner product, distance, angle
- 1.4 Data as vectors: the data matrix and notation
- 1.5 Notation quick reference

### 2. Matrices and Linear Transformations (~28 pp · strong)

- 2.1 Matrices as transformations (a matrix maps vectors to vectors)
- 2.2 Operations and their two views (matrix-vector product; row-wise vs column-wise; composition)
- 2.3 Geometric effects (rotation, scaling, projection, shear)
- 2.4 Systems of linear equations (solving; invertibility; dependence and independence)
- 2.5 Standardization as a transformation (centering and scaling Ames features)
- 2.6 *Implementation:* transforming Ames features
- 2.7 Summary and exercises

### 3. Eigenvalues, Eigenvectors, and Diagonalization (~30 pp · strong)

- 3.1 The eigenvalue problem (Av = lambda v; invariant directions)
- 3.2 Finding eigenvalues and eigenvectors (characteristic polynomial; eigenspaces and multiplicity)
- 3.3 Diagonalization (the eigenbasis; when it exists)
- 3.4 Symmetric matrices and the spectral theorem (real eigenvalues, orthogonal eigenvectors; sets up covariance and PCA)
- 3.5 *Implementation:* power iteration on Ames' second-moment matrix
- 3.6 **Part I capstone, Geometry of Real Data:** recover image_features' known rank 3 by eigendecomposition, before any probability
- 3.7 Summary and exercises; forward to SVD (Ch 9)

## Part II: Random Vectors and Statistical Structure

### 4. Random Vectors and Probability Spaces (~28 pp · strong)

- 4.1 From the vector to the random vector (data as samples from an uncertain process)
- 4.2 Probability spaces and random variables (sample space, distributions; first-course level)
- 4.3 Random vectors (joint distribution; mean vector; marginals)
- 4.4 Linear transformations of random vectors (how the mean transforms)
- 4.5 Random vectors through data (an Ames home as a random draw; empirical vs theoretical)
- 4.6 *Implementation:* simulate random vectors; Monte Carlo
- 4.7 Summary and exercises

### 5. Expectation and Conditional Probability (~28 pp · scratch)

- 5.1 The expectation operator (linearity; expectation of a random vector)
- 5.2 Conditional probability and conditional distributions
- 5.3 Conditional expectation (E[Y|X] as a function of X; the tower property)
- 5.4 The best predictor (the conditional mean minimizes MSE; **MMSE seed**)
- 5.5 *Implementation:* conditional mean of Ames price given features; predict from a partial record
- 5.6 Summary and exercises

### 6. Covariance, Correlation, and Cross-Correlation (~32 pp · strong)

- 6.1 From variance to covariance (covariance as an expectation; the covariance matrix)
- 6.2 The covariance matrix as statistical geometry (PSD; the spread ellipsoid; eigenstructure preview)
- 6.3 Correlation (normalization; the correlation matrix)
- 6.4 Cross-correlation (cross-covariance between two random vectors)
- 6.5 Estimating covariance from data (the sample covariance estimator)
- 6.6 *Implementation:* covariance/correlation of Ames features; cross-correlation on stock_returns
- 6.7 Summary and exercises

### 7. Gaussian Random Vectors (~28 pp · scratch)

- 7.1 The univariate normal, recalled
- 7.2 The multivariate normal (density; mean and covariance; the ellipsoid)
- 7.3 Why Gaussian dominates (closure under linear maps; tractability)
- 7.4 The conditional Gaussian (conditional mean is linear in the conditioning variable; **LMMSE seed**; conditional covariance)
- 7.5 Gaussian vs real data (which Ames features are Gaussian, which are skewed)
- 7.6 *Implementation:* MVN sampling/density; Ames Gaussian-vs-skew
- 7.7 Summary and exercises

### 8. Convergence: Law of Large Numbers and the CLT (~26 pp · scratch)

- 8.1 Estimating from finite samples (why does the sample mean/covariance work?)
- 8.2 Modes of convergence, by simulation (kept concrete, no measure theory)
- 8.3 The Law of Large Numbers (sample covariance to true covariance)
- 8.4 The Central Limit Theorem (sums to Gaussian; retrospective on Ch 7)
- 8.5 Consequences for estimation (sampling distributions; confidence)
- 8.6 *Implementation:* simulate LLN/CLT; stock_returns sample covariance converging
- 8.7 **Part II capstone, Statistical Structure of a Housing Market:** model Ames as a random vector; estimate the covariance; test Gaussianity; show convergence; output covariance for Ch 10
- 8.8 Summary and exercises

## Part III: Linear Estimation

### 9. Singular Value Decomposition (~30 pp · strong)

- 9.1 Review: diagonalization and its limits (recall Ch 3; square/symmetric only)
- 9.2 The SVD (U Sigma V-transpose; existence for any matrix; rotate-scale-rotate geometry)
- 9.3 Singular values and rank (low-rank structure; truncation)
- 9.4 Computing the SVD (connection to eigendecomposition of A-transpose-A and A-A-transpose)
- 9.5 Low-rank approximation (Eckart-Young; recover image_features' rank 3, now via SVD)
- 9.6 *Implementation:* truncated SVD and rank recovery
- 9.7 Sets up PCA (Ch 10) and the pseudoinverse (Ch 11); summary and exercises

### 10. Principal Component Analysis (~36 pp · strong + project-1) **[CAPSTONE]**

- 10.1 The problem: directions of maximum variance
- 10.2 PCA via eigendecomposition of the covariance (consumes Part II's Ames covariance)
- 10.3 PCA via SVD of the centered data matrix (the equivalence; eigenvalues = singular values squared / (n-1))
- 10.4 PCA as an estimator (sample to estimated components; why it works, callback to Ch 8)
- 10.5 Choosing dimensionality (variance explained; scree; rank check on image_features)
- 10.6 The ML bridge (whitening, dimensionality reduction, learned features)
- 10.7 **Project capstone:** PCA from intuition to implementation (Ames covariance PCA; wholesale segmentation; full project-1 pipeline)
- 10.8 Summary and exercises

### 11. Least Squares Estimation (~30 pp · partial)

- 11.1 The over-determined system (fit a model to noisy data; Ames price)
- 11.2 The geometry of least squares (projection onto the column space; orthogonal residual)
- 11.3 The normal equations (derivation; minimizing the loss)
- 11.4 Computation (QR; the SVD pseudoinverse; numerical stability)
- 11.5 Regularization (ridge/Tikhonov; the ML/ill-posed bridge; interpreting coefficients)
- 11.6 *Implementation:* predict Ames sale price; pseudoinverse via SVD
- 11.7 Summary and exercises

### 12. Linear MMSE Estimation (~36 pp · scratch) **[CAPSTONE]**

- 12.1 The estimation problem (estimate X from observations Y; pays off the Ch 5 and Ch 7 seeds)
- 12.2 The orthogonality principle (error orthogonal to the data; the geometric heart)
- 12.3 The Linear MMSE estimator (derivation in covariance and cross-covariance)
- 12.4 The Gaussian case (LMMSE = MMSE = conditional mean; callback to Ch 7)
- 12.5 Performance evaluation (error covariance; the Wiener estimator)
- 12.6 **Project capstone:** static LMMSE estimator on the tracking dataset (the Estimator seed)
- 12.7 Summary and exercises

## Part IV: Applications

### 13. Estimation in Signal Processing (~32 pp · scratch)

- 13.1 From static to dynamic (signals over time; the state-space view)
- 13.2 Filtering, prediction, and smoothing (the three tasks)
- 13.3 Recursive estimation (updating as data arrives; LMMSE done online)
- 13.4 The scalar Kalman filter (the predict-update cycle)
- 13.5 *Implementation:* scalar Kalman on the tracking dataset (1D)
- 13.6 Summary and exercises

### 14. Advanced Filtering and Modern Applications (~34 pp · scratch)

- 14.1 The full multivariate Kalman filter (state and measurement models; the matrix recursions)
- 14.2 Estimation through gaps (tracking through missing measurements)
- 14.3 Adaptive filtering (LMS/RLS; when the model is unknown)
- 14.4 Further directions (system identification; communications, brief)
- 14.5 The ML bridge (modern filtering; learned dynamics; sequence models)
- 14.6 **Project capstone, Build a Kalman Filter:** extend Ch 13's estimator into the full filter (the Estimator finale)
- 14.7 Summary and exercises
