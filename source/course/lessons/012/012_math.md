---
title: "Singular Value Decomposition and Covariance Analysis"
subtitle: "Week 6"
author: "Linear Algebra and Estimation Theory"
date: "2025-02-11"
---

# Singular Value Decomposition and Covariance Analysis

## 0. Review of Diagonalization

\paragraph{0.1 Eigendecomposition Review}

For any diagonalizable square matrix $\mathbf{A}$, we can decompose it as:
$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$

where:

- $\mathbf{P}$ contains eigenvectors as columns
- $\mathbf{D}$ is diagonal matrix of eigenvalues
- $\mathbf{P}^{-1}\mathbf{P} = \mathbf{I}$ (but not necessarily orthogonal)

```python
# Simple 2x2 example
A = np.array([[4, -1], 
              [-1, 4]])

# Find eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(A)

# Form P and D
P = eigvecs
D = np.diag(eigvals)

# Verify decomposition
print("A = PDP^(-1):", np.allclose(A, P @ D @ np.linalg.inv(P)))
print("Av = λv:", np.allclose(A @ eigvecs[:, 0], eigvals[0] * eigvecs[:, 0]))

```

\pagebreak

Steps to find this decomposition:

1. Find eigenvalues $\lambda_i$ by solving $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$
2. For each $\lambda_i$, find eigenvector $\mathbf{v}_i$ solving $(\mathbf{A} - \lambda_i\mathbf{I})\mathbf{v}_i = \mathbf{0}$
3. Form $\mathbf{P}$ by combining eigenvectors as columns
4. Form $\mathbf{D}$ with eigenvalues on diagonal
5. Verify $\mathbf{A}\mathbf{v}_i = \lambda_i\mathbf{v}_i$ for each pair

Example:

![Diagonalization Steps](templates/012/diagonalization_steps.png)

\paragraph{0.1.1 The plots above show:}

- Left: Original vectors:
  * x: Unit vector along x-axis (red)
  * y: Unit vector along y-axis (blue)
  * diag1: [1,1] diagonal vector (green)
  * diag2: [-1,1] diagonal vector (purple)
  * eigvec1, eigvec2: Eigenvectors of A (orange, brown)
  * v1: [2,1] arbitrary vector (pink)
  * v2: [-1,2] arbitrary vector (gray)

- Middle: After applying matrix A
  * Each vector $\mathbf{v}$ is transformed by $\mathbf{A}\mathbf{v}$
  * For eigenvectors $\mathbf{v}_i$: $\mathbf{A}\mathbf{v}_i = \lambda_i\mathbf{v}_i$
  * For other vectors: direction and length both change
  * Matrix multiplication: $\mathbf{A}\mathbf{v} = \begin{bmatrix} 4 & -1 \\ -1 & 4 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$

- Right: After complete diagonalization
  * First rotate to eigenvector basis: $\mathbf{v} \rightarrow \mathbf{P}^T\mathbf{v}$
  * Then scale by eigenvalues: $\mathbf{D}\mathbf{P}^T\mathbf{v}$
  * Shows vectors in eigenvector coordinate system
  * In code: `points @ eigvecs @ np.diag(eigvals)`

\paragraph{0.2 Limitations}
Diagonalization only works when:

1. Matrix is square
2. Has n linearly independent eigenvectors
3. All eigenvalues are real (for real matrices)

\pagebreak


## 1. SVD Foundations

\paragraph{1.1 The SVD Decomposition}

The Singular Value Decomposition (SVD) is a fundamental matrix factorization that expresses any matrix as a product of three special matrices. It provides a concrete realization of the Fundamental Theorem of Linear Algebra by explicitly constructing orthonormal bases for all four fundamental subspaces.

$$\mathbf{X} = \mathbf{U}\Sigma\mathbf{V}^T$$

\paragraph{1.1.1 Connection to Fundamental Subspaces:}

1. Column Space (Range): 
   * Spanned by left singular vectors (columns of $\mathbf{U}$)
   * Corresponding to non-zero singular values
   * Dimension = rank($\mathbf{X}$)

2. Row Space:
   * Spanned by right singular vectors (columns of $\mathbf{V}$)
   * Corresponding to non-zero singular values
   * Dimension = rank($\mathbf{X}$)

3. Null Space:
   * Spanned by right singular vectors
   * Corresponding to zero singular values
   * Dimension = n - rank($\mathbf{X}$)

4. Left Null Space:
   * Spanned by left singular vectors
   * Corresponding to zero singular values
   * Dimension = m - rank($\mathbf{X}$)

\paragraph{1.1.2 The singular values in $\Sigma$ provide:}

- Rank: Number of non-zero singular values
- Condition number: Ratio of largest to smallest non-zero singular value
- Basis for optimal low-rank approximation

\paragraph{1.1.3 Properties of each matrix:}
  * $\mathbf{U}$: Left singular vectors (n × n orthogonal)
  * $\mathbf\Sigma$: Diagonal matrix of singular values
  * $\mathbf{V}^T$: Right singular vectors (d × d orthogonal)

- Geometric interpretation:
  * Rotation-scaling-rotation decomposition:
    - V^T rotates data to align with principal directions
    - Σ scales along these directions
    - U rotates to final coordinate system

\paragraph{1.2 Why SVD is useful:}

1. Works for any matrix (rectangular, singular, etc.)
   * Can decompose m × n matrices of any shape
   * Handles rank-deficient (singular) matrices gracefully
   * No requirements on matrix properties
   * Example: Document-term matrices are often rectangular

2. Reveals underlying structure and patterns
   * U shows patterns in observations (rows)
   * V shows patterns in features (columns)
   * Σ shows relative importance of patterns
   * Example: In image compression, reveals dominant visual patterns

4. Key tool for dimensionality reduction
   * Projects data onto most important directions
   * Preserves maximum variance in fewer dimensions
   * Maintains relative distances between points
   * Example: Reduce 100D data to 3D for visualization

5. Foundation for many algorithms
   * PCA: Uses SVD of centered data
   * LSI: Uses SVD of document-term matrices
   * Spectral clustering: Uses SVD of similarity matrices
   * Example: Netflix recommendation system uses SVD

\pagebreak

\paragraph{1.3 Why not just use eigendecomposition?}

1. Eigendecomposition limited to square matrices
   * Only works for n × n matrices
   * Can't handle rectangular data directly
   * Would need to form X^T X first
   * Example: Can't directly eigendecompose 1000×100 data matrix

2. SVD more numerically stable
   * Avoids squaring condition number
   * Better with nearly singular matrices
   * More reliable with floating point arithmetic
   * Example: X^T X can amplify numerical errors

3. SVD directly gives principal directions
   * V gives feature space directions
   * U gives observation space directions
   * No need to compute X^T X
   * Example: PCA directions come directly from V

4. SVD handles non-symmetric matrices naturally
   * Works with any rectangular matrix
   * No symmetry requirements
   * Separates row and column space structure
   * Example: Can analyze asymmetric relationship data

5. Singular values always real and non-negative
   * σᵢ = √λᵢ where λᵢ are eigenvalues of X^T X
   * Natural interpretation as importance/magnitude
   * Easy to sort and truncate
   * Example: Can use as feature importance scores

\pagebreak

\paragraph{1.4 SVD vs Eigendecomposition}

\subparagraph{Singular Values vs Eigenvalues:}
- Singular values ($\sigma_i$):
  * Always real and non-negative
  * Square roots of eigenvalues of $\mathbf{X}^T\mathbf{X}$
  * $\sigma_i = \sqrt{\lambda_i}$ where $\lambda_i$ are eigenvalues
  * Measure "stretch" in each direction
  * Natural for rectangular matrices

\subparagraph{The Square Root Pattern:}

This pattern of square roots appears in several places:

- Standard deviation $\sigma = \sqrt{\text{Var}(X)}$

  * Variance measures squared distances from mean
  * Standard deviation brings back to original units
  * Example: If variance is in meters², std dev is in meters

- Singular values $\sigma_i = \sqrt{\lambda_i}$

  * $\lambda_i$ are eigenvalues of $\mathbf{X}^T\mathbf{X}$
  * $\mathbf{X}^T\mathbf{X}$ involves squared terms
  * Singular values bring back to original scale
  * Example: If data is in meters, singular values are in meters

\subparagraph{The Connection:}

- Both involve squaring operations:

  * Covariance: $\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$
  * SVD: $\mathbf{X}^T\mathbf{X} = \mathbf{V}\Sigma^2\mathbf{V}^T$

- Both need square roots to return to original scale:

  * Covariance → Correlation: $\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}$
  * SVD: $\sigma_i = \sqrt{\lambda_i}$ where $\lambda_i$ are eigenvalues of $\mathbf{X}^T\mathbf{X}$

\subparagraph{The intuition:}

- Squaring happens naturally when:
  * Computing averages of products (covariance)
  * Multiplying a matrix by its transpose (SVD)
- Taking square root:
  * Returns to original units
  * Makes values directly interpretable
  * Allows fair comparisons across variables

\subparagraph{Eigenvalues ($\lambda_i$):}

  * Can be complex for real matrices
  * Only defined for square matrices
  * May be negative
  * Measure scaling in eigenvector directions
  * Natural for transformations

\subparagraph{Singular Vectors vs Eigenvectors:}

- Singular vectors ($\mathbf{u}_i$, $\mathbf{v}_i$):
  * Come in left/right pairs
  * Always orthonormal
  * Span input/output spaces
  * $\mathbf{X}\mathbf{v}_i = \sigma_i\mathbf{u}_i$
  * $\mathbf{X}^T\mathbf{u}_i = \sigma_i\mathbf{v}_i$

- Eigenvectors ($\mathbf{e}_i$):
  * Single vector per eigenvalue
  * Not necessarily orthogonal
  * Only for square matrices
  * $\mathbf{A}\mathbf{e}_i = \lambda_i\mathbf{e}_i$

\subparagraph{Relationship to Covariance:}

- SVD connection:
  * $\mathbf{X}^T\mathbf{X} = \mathbf{V}\Sigma^2\mathbf{V}^T$
  * $\mathbf{X}\mathbf{X}^T = \mathbf{U}\Sigma^2\mathbf{U}^T$
  * Right singular vectors = eigenvectors of $\mathbf{X}^T\mathbf{X}$
  * Left singular vectors = eigenvectors of $\mathbf{X}\mathbf{X}^T$
  * Singular values squared = eigenvalues of both

\pagebreak

## 2. Computing SVD

\paragraph{2.1 Implementation Options}

- numpy.linalg.svd:
  * Full vs reduced decomposition: `full_matrices=False` gives compact SVD
  * Returns U, s, Vh directly: `U, s, Vh = np.linalg.svd(X)`
  * Singular values in descending order
  * Example with different scaling:
    ```python
    # Original data
    X = np.array([[1000, 2], [2000, 4], [3000, 6]])
    
    # No scaling
    U1, s1, Vh1 = np.linalg.svd(X)
    print("Original singular values:", s1)
    
    # With standardization
    X_std = (X - X.mean(axis=0)) / X.std(axis=0)
    U2, s2, Vh2 = np.linalg.svd(X_std)
    print("Standardized singular values:", s2)
    
    # With robust scaling
    from sklearn.preprocessing import RobustScaler
    X_rob = RobustScaler().fit_transform(X)
    U3, s3, Vh3 = np.linalg.svd(X_rob)
    print("Robust scaled singular values:", s3)
    
    # Verify properties
    for U, s, Vh in [(U1, s1, Vh1), (U2, s2, Vh2), (U3, s3, Vh3)]:
        # Check orthogonality
        print("U orthogonal:", np.allclose(U.T @ U, np.eye(U.shape[1])))
        print("V orthogonal:", np.allclose(Vh @ Vh.T, np.eye(Vh.shape[0])))
        # Check reconstruction
        print("Reconstruction:", np.allclose(U @ np.diag(s) @ Vh, X))
        
        # Additional validations:
        # 1. Singular values are non-negative and sorted
        print("Singular values sorted:", np.all(s[:-1] >= s[1:]))
        print("Singular values non-negative:", np.all(s >= 0))
        
        # 2. Compare with sklearn implementation
        from sklearn.decomposition import TruncatedSVD
        svd = TruncatedSVD(n_components=X.shape[1])
        X_transformed = svd.fit_transform(X)
        print("Matches sklearn:", np.allclose(np.abs(X_transformed), 
                                            np.abs(X @ Vh.T)))
        
        # 3. Check covariance properties
        X_centered = X - X.mean(axis=0)
        cov = X_centered.T @ X_centered / (len(X) - 1)
        eigvals, eigvecs = np.linalg.eigh(cov)
        idx = np.argsort(eigvals)[::-1]
        print("V matches eigenvectors:", 
              np.allclose(np.abs(Vh.T), np.abs(eigvecs[:, idx])))
        print("s^2/(n-1) matches eigenvalues:",
              np.allclose(s**2/(len(X)-1), eigvals[idx]))
    ```

- `numpy.linalg.eigh`:
  * For symmetric matrices only: Use on X^T X
  * Returns eigenvalues and eigenvectors: `w, v = np.linalg.eigh(X.T @ X)`
  * Convert to SVD form:
    ```python
    # Get SVD from eigendecomposition
    w, v = np.linalg.eigh(X.T @ X)
    s = np.sqrt(np.maximum(w, 0))  # singular values
    Vh = v.T                       # right singular vectors
    U = X @ (v / s)               # left singular vectors
    ```

\pagebreak

## 3. Connection to Previous Topics

\paragraph{3.1 Random Vectors (Lesson 009)}

- SVD of random matrices:
  * Expected properties
  * Concentration results
  * Sample size effects
- Connection to variance directions:
  * Singular values $\sigma_i = \sqrt{\lambda_i}$ where $\lambda_i$ are eigenvalues
  * $\sigma_i$ represents standard deviation along $i$-th principal direction
  * Larger singular values indicate directions of higher variance
- Statistical interpretation:
  * $\mathbf{U}$ columns are normalized principal components
  * $\mathbf{V}$ columns are the **loadings** (how features contribute to each component)
  * $\mathbf{\Sigma}$ shows relative importance of each direction
- Example with random data:
  ```python
  # Generate random data with known covariance structure
  rng = np.random.default_rng(42)
  n_samples = 1000
  X = rng.multivariate_normal(
      mean=[0, 0],
      cov=[[4, 1], [1, 1]],
      size=n_samples
  )
  
  # Compute SVD
  U, s, Vh = np.linalg.svd(X - X.mean(axis=0))
  
  # Compare singular values with theoretical values
  print("Singular values:", s)
  print("Expected stdevs:", np.sqrt([4, 1]))  # sqrt of eigenvalues
  ```

\pagebreak

\paragraph{3.2 Covariance Analysis (Lesson 010)}
- SVD reveals covariance structure:
  * $\mathbf{V}$ gives principal directions
  * $\mathbf{\Sigma}^2$ gives variances
  * Connection to correlation
- Statistical interpretation:
  * Variance decomposition
  * Principal components
  * Feature relationships

\pagebreak

\paragraph{3.3 Feature Scaling (Lesson 011)}
- Impact on SVD:
  * How scaling changes singular values:
    - Rescales singular values proportionally to feature scales
    - Changes relative importance of directions
    - Example: If feature 1 is in kilometers and feature 2 in meters, 
      first singular value will be ~1000 times larger just due to units
  * Effect on singular vectors:
    - Changes direction to account for new relative scales
    - Preserves orthogonality property
    - Can completely change which directions appear most important
  * Preserving important properties:
    - Orthogonality of U and V maintained
    - Rank unchanged by scaling
    - Relative angles between vectors in same space preserved

- When scaling matters:
  * Different units:
    - Features measured in different scales (e.g., meters vs kilograms)
    - Some features naturally larger than others
    - Want to compare importance fairly
  * Varying scales:
    - Features with very different ranges
    - Some features sparse, others dense
    - Need to prevent domination by large-scale features
  * Outlier effects:
    - Extreme values can dominate singular values
    - Robust scaling can reduce outlier impact
    - Choice of scaling affects outlier influence on SVD

\pagebreak

## Example: Scaling effects on SVD

  ```python
  # Load iris dataset
  from sklearn.datasets import load_iris
  X = load_iris().data
  feature_names = load_iris().feature_names
  
  # Compare SVD with different scaling methods
  methods = {
      'none': lambda x: x,
      'standard': StandardScaler().fit_transform,
      'robust': RobustScaler().fit_transform
  }
  
  results = {}
  for name, scaler in methods.items():
      X_scaled = scaler(X)
      U, s, Vh = np.linalg.svd(X_scaled)
      results[name] = {
          'singular_values': s,
          'explained_variance_ratio': s**2/sum(s**2),
          'feature_importance': np.abs(Vh[0])  # First component loadings
      }
  
  # Analyze how scaling affects interpretation
  for name, res in results.items():
      print(f"\n{name.title()} Scaling:")
      print("Singular values:", res['singular_values'])
      print("Variance explained:", res['explained_variance_ratio'])
      print("Feature importance:")
      for feat, imp in zip(feature_names, res['feature_importance']):
          print(f"  {feat}: {imp:.3f}")
  ```
- Key insights:
  * Standard scaling makes singular values comparable
  * Robust scaling reduces outlier impact
  * Choice of scaling affects feature importance
  * Must consider domain knowledge
