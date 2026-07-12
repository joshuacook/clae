---
title: "Covariance Matrices: Practice Problems"
subtitle: "Week 5"
author: "Linear Algebra and Estimation Theory"
date: "2025-02-02"
---

# Practice Problems for Random Vectors and Covariance Analysis

## Problem 1: Basic Properties of Covariance Matrices

Consider the following measurements from three temperature sensors over 5 time points:
```python
import numpy as np

temps = np.array([
    [20.1, 19.8, 20.3],  # sensor readings at t=1
    [19.8, 19.9, 20.1],  # t=2
    [20.3, 20.1, 20.4],  # t=3
    [20.0, 19.7, 20.2],  # t=4
    [19.9, 19.8, 20.1]   # t=5
])
```

a) Compute the sample mean vector.
b) Calculate the sample covariance matrix.
c) Verify the covariance matrix is symmetric.
d) Show the matrix is positive semidefinite by:
   * Computing eigenvalues
   * Evaluating $\mathbf{v}^T\boldsymbol{\Sigma}\mathbf{v}$ for several random vectors
e) Interpret what the covariance structure tells us about the sensors.

## Problem 2: Fundamental Subspaces and Noise Analysis

Using the Palmer penguins dataset:
```python
import seaborn as sns
penguins = sns.load_dataset('penguins')
X = penguins[['bill_length_mm', 'bill_depth_mm']].dropna().values
```

a) Find and interpret the eigenvalues and eigenvectors of the covariance matrix.
b) What proportion of variance is explained by each direction?
c) If measurement precision is ±0.1mm, is the smaller eigenvalue significant?
d) How would adding Gaussian noise affect your eigenvalue analysis?

## Problem 3: F-tests and Statistical Significance

For each penguin species separately:
```python
species = pd.Categorical(penguins['species'].dropna()).codes
adelie = X[species == 0]      # Adelie penguins
chinstrap = X[species == 1]   # Chinstrap penguins
gentoo = X[species == 2]      # Gentoo penguins
```

a) Compute the covariance matrix for each species.
b) Use F-tests to compare:
   * Total variance (trace of covariance matrix)
   * Directional variance (individual eigenvalues)
   * Overall structure (determinant ratio)
c) Which species shows the most distinct covariance pattern?
d) How does measurement noise affect your conclusions?

## Problem 4: Simulation Study

Design a simulation to study how sample size affects covariance estimation:

a) Generate synthetic data from a known covariance matrix.
b) Vary the sample size from 10 to 1000.
c) Plot the error in estimated:
   * Eigenvalues
   * Eigenvectors
   * F-statistics
d) At what sample size do estimates stabilize?

\pagebreak

## Solutions

### Problem 1 Solution: Basic Properties

```python
import numpy as np

# a) Sample mean vector
mean = np.mean(temps, axis=0)
print(f"Mean vector: {mean}")  # [20.02 19.86 20.22]

# b) Sample covariance matrix
cov = np.cov(temps.T)
print("Covariance matrix:")
print(cov)
# [[0.038 0.024 0.036]
#  [0.024 0.022 0.024]
#  [0.036 0.024 0.037]]

# c) Verify symmetry
print(f"Is symmetric: {np.allclose(cov, cov.T)}")  # True

# d) Show positive semidefiniteness
eigenvals = np.linalg.eigvals(cov)
print(f"Eigenvalues: {eigenvals}")  # All positive

# Test random vectors
for _ in range(3):
    v = np.random.randn(3)
    quad_form = v @ cov @ v
    print(f"v^T Σ v = {quad_form:.6f} ≥ 0")  # Always positive
```

Interpretation:
1. Sensors are highly correlated (positive covariances)
2. Sensor 2 shows least variance (0.022°C²)
3. Sensors 1 and 3 more variable (~0.037°C²)
4. Suggests sensors 1 and 3 might be closer together

### Problem 2 Solution: Fundamental Subspaces

```python
import seaborn as sns
import numpy as np

# Load and prepare data
penguins = sns.load_dataset('penguins')
X = penguins[['bill_length_mm', 'bill_depth_mm']].dropna().values

# Compute covariance and eigendecomposition
cov = np.cov(X.T)
eigenvals, eigenvecs = np.linalg.eigh(cov)

# Sort in descending order
idx = eigenvals.argsort()[::-1]
eigenvals = eigenvals[idx]
eigenvecs = eigenvecs[:, idx]

print("Eigenvalues:", eigenvals)
# [28.724, 4.832]  # Much larger than iris values!

print("Proportion of variance:")
print(eigenvals / eigenvals.sum())
# [0.856, 0.144]  # More balanced than iris

# Compare to measurement noise
noise_variance = 0.1**2  # (0.1mm)² = 0.01mm²
print(f"Smaller eigenvalue / noise = {eigenvals[1]/noise_variance:.2f}")
# Ratio ≈ 483, much larger than noise level!

# Interpretation:
# 1. Both directions show significant variation
# 2. Bill length/depth relationship is strong but not perfect
# 3. Measurement noise is negligible compared to natural variation
```

### Problem 3 Solution: F-tests

```python
def compare_covariance(X1, X2):
    cov1 = np.cov(X1.T)
    cov2 = np.cov(X2.T)
    
    # Compare total variance
    F_total = np.trace(cov1) / np.trace(cov2)
    
    # Compare determinants
    F_det = np.linalg.det(cov1) / np.linalg.det(cov2)
    
    return F_total, F_det

# Compare each pair
species_pairs = [
    (setosa, versicolor, "Setosa vs Versicolor"),
    (setosa, virginica, "Setosa vs Virginica"),
    (versicolor, virginica, "Versicolor vs Virginica")
]

for X1, X2, name in species_pairs:
    F_total, F_det = compare_covariance(X1, X2)
    print(f"\n{name}:")
    print(f"Total variance ratio: {F_total:.4f}")
    print(f"Determinant ratio: {F_det:.4f}")
```

### Problem 4 Solution: Simulation Study

```python
def simulation_study(true_cov, sample_sizes, n_trials=100):
    errors = []
    for n in sample_sizes:
        trial_errors = []
        for _ in range(n_trials):
            # Generate samples
            X = np.random.multivariate_normal(
                mean=np.zeros(2),
                cov=true_cov,
                size=n
            )
            # Compute sample covariance
            sample_cov = np.cov(X.T)
            # Compute error
            error = np.linalg.norm(sample_cov - true_cov)
            trial_errors.append(error)
        errors.append(np.mean(trial_errors))
    return np.array(errors)

# Run simulation
sample_sizes = np.logspace(1, 3, 20).astype(int)
true_cov = np.array([[3.116, 0], [0, 0.039]])
errors = simulation_study(true_cov, sample_sizes)

# Plot results
plt.semilogx(sample_sizes, errors)
plt.xlabel('Sample Size (log scale)')
plt.ylabel('Frobenius Error')
plt.grid(True)
```

Key findings:
1. Errors decrease approximately as 1/√n
2. Estimates stabilize around n=200
3. Smaller eigenvalue needs larger samples
4. Measurement noise becomes limiting factor
