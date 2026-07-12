---
title: "Covariance Matrices: Theory and Estimation"
subtitle: "Week 5"
author: "Linear Algebra and Estimation Theory"
date: "2025-02-02"
---

# Covariance Matrices: From Theory to Practice

## 1. Theoretical Foundations


## 1.0 Motivation

Consider measuring sepal length ($X_1$) and sepal width ($X_2$) for iris flowers in the iris dataset:

\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{templates/linalg_010_iris_covariance.png}
\end{figure}

1. The red ellipse shows the 95\% confidence region - assuming the measurements follow a multivariate normal (Gaussian) distribution, this boundary encloses 95\% of the probability distribution (See **Endnotes**).

2. The green arrows show the eigenvectors of the covariance matrix, scaled by their corresponding eigenvalues:
   * The longer arrow indicates the direction of maximum variance - the primary axis along which the data varies most
   * The shorter arrow shows the direction of minimum variance - there is less variation in this perpendicular direction
   * The relative lengths of these arrows (approximately 3.6:1) tell us the data varies about 3.6 times more in the primary direction

3. The red dot marks the sample mean $\boldsymbol{\mu}$, which serves as the center of the ellipse. The ellipse's:
   * Orientation is determined by the eigenvectors
   * Shape (eccentricity) is determined by the ratio of eigenvalues
   * Size is determined by both eigenvalues and our chosen confidence level (95%)

### 1.1 Definition and Basic Properties

The population covariance matrix $\boldsymbol{\Sigma}$ captures all pairwise relationships:

\begin{equation*}
\boldsymbol{\Sigma} = E[(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T] = 
\begin{bmatrix} 
\text{Var}(X_1) & \text{Cov}(X_1,X_2) \\
\text{Cov}(X_2,X_1) & \text{Var}(X_2)
\end{bmatrix}
\end{equation*}


- Each entry $\sigma_{ij} = E[(X_i-\mu_i)(X_j-\mu_j)]$ measures relationship between features $i$ and $j$
- Diagonal elements $\sigma_{ii} = \text{Var}(X_i)$ capture spread of individual features
- Off-diagonal elements $\sigma_{ij} = \text{Cov}(X_i,X_j)$ capture feature relationships

\paragraph{For the iris data, this gives:}

\begin{equation*}
\boldsymbol{\Sigma} \approx
\begin{bmatrix}
0.685 & -0.039 \\
-0.039 & 0.188
\end{bmatrix}
\end{equation*}

\paragraph{Interpretation:}

- Sepal length variance: 0.685 $\text{cm}^2$
- Sepal width variance: 0.188 $\text{cm}^2$
- Slight negative covariance: -0.039 $\text{cm}^2$

\paragraph{Key properties with proofs:}

  * Definition of Positive Semidefiniteness:

    A symmetric matrix $\mathbf{A}$ is positive semidefinite if and only if:
    1. $\mathbf{v}^T\mathbf{A}\mathbf{v} \geq 0$ for all vectors $\mathbf{v}$ (quadratic form definition)
    2. All eigenvalues are non-negative
    3. Can be written as $\mathbf{B}^T\mathbf{B}$ for some matrix $\mathbf{B}$
    These definitions are equivalent.

    In simple terms: A positive semidefinite matrix never makes things "more negative" - when you multiply a vector by it, the result always points in a direction that makes a non-negative angle with the original vector. Think of it like a transformation that might squish or stretch things, but never flips them to the opposite side of zero.

  * Symmetric: $\boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$

    *Looking at how variable 1 relates to variable 2 gives you the same information as looking at how variable 2 relates to variable 1*.

    - Proof: For any indices $i,j$:
      \begin{align*}
      \sigma_{ij} &= E[(X_i-\mu_i)(X_j-\mu_j)] \\
                  &= E[(X_j-\mu_j)(X_i-\mu_i)] \text{ (scalar multiplication is commutative)} \\
                  &= \sigma_{ji}
      \end{align*}
  
  * Positive semidefinite: $\mathbf{v}^T\boldsymbol{\Sigma}\mathbf{v} \geq 0$ for all $\mathbf{v}$

    *When you measure the spread of data in any direction, you always get a non-negative number. You can't have a "negative spread"*.

    - Proof:
      \begin{align*}
      \mathbf{v}^T\boldsymbol{\Sigma}\mathbf{v} &= \mathbf{v}^TE[(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T]\mathbf{v} \\
      &= E[\mathbf{v}^T(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T\mathbf{v}] \text{ (linearity of expectation)} \\
      &= E[(\mathbf{v}^T(\mathbf{X}-\boldsymbol{\mu}))^2] \geq 0 \text{ (square of a real number)}
      \end{align*}
  
  * Eigenvalues non-negative: $\lambda_i \geq 0$

    *The eigenvalues tell us how much the data spreads out in different directions. Since spread can't be negative (just like you can't have a negative distance), eigenvalues must always be zero or positive!*.

    - Follows from positive semidefiniteness:
      If $\mathbf{u}_i$ is an eigenvector with $\|\mathbf{u}_i\| = 1$, then:
      \begin{align*}
      0 \leq \mathbf{u}_i^T\boldsymbol{\Sigma}\mathbf{u}_i = \mathbf{u}_i^T\lambda_i\mathbf{u}_i = \lambda_i
      \end{align*}

\pagebreak

\paragraph{What Does the Covariance Matrix Tell Us?}

The covariance matrix is a powerful tool that tells us three key things:

1. How much each variable varies on its own:
   * The diagonal entries tell us the spread of each variable
   * For iris data: sepal length varies more (0.685) than width (0.188)
   * Larger values mean more spread in that variable

2. How variables move together:
   * Off-diagonal entries tell us if variables tend to increase/decrease together
   * Positive values: variables tend to increase together
   * Negative values: when one goes up, the other tends to go down
   * For iris: slight negative relationship (-0.039) between length and width

3. What directions matter most:
   * Eigenvectors show the important directions in our data
   * Eigenvalues tell us how much variation occurs in those directions
   * In our plot: the longer green arrow shows the main direction of variation

\pagebreak

## 2. Linear Algebraic Structure

### 2.1 Fundamental Subspaces

To visualize these concepts, let's examine the iris petal measurements:

\begin{figure}[h]
\centering
\includegraphics[width=0.45\textwidth]{templates/linalg_010_iris_petal_covariance.png}
\includegraphics[width=0.45\textwidth]{templates/linalg_010_iris_petal_rotated.png}
\caption{Left: Original petal measurements with covariance structure. Right: Data rotated to align with principal components (eigenvectors).}
\end{figure}

The left plot shows the original petal measurements, while the right plot shows the same data after rotation to align with the eigenvectors. This rotation reveals:

1. The row space $\mathcal{R}(\boldsymbol{\Sigma})$:
   * Directions of non-zero variance in feature space
   * Span of principal components: $\text{span}\{\mathbf{u}_1,\mathbf{u}_2\}$
   * After rotation, these become the standard basis vectors
   * First principal component captures most variation
   * Second component is orthogonal, captures remaining variation

2. The eigenvalues tell us the scale of variation:
   * First component: $\lambda_1 \approx 3.116$ (major axis)
   * Second component: $\lambda_2 \approx 0.039$ (minor axis)
   * Ratio $\lambda_1/\lambda_2 \approx 80$ indicates near rank deficiency

3. The large eigenvalue ratio reveals an approximate decomposition:
   * Row Space: The direction of $\lambda_1 \approx 3.116$ captures the true signal
     - This single direction explains 98.8% of variation
     - Represents the "effective rank" of the data
     - Suggests data lives primarily on a line
   
   * "Approximate" Null Space: The direction of $\lambda_2 \approx 0.039$
     - So small it could be treated as effectively zero
     - Represents noise or measurement error
     - Nearly perfect linear relationship between variables
     
   This natural separation into dominant and negligible directions:
   * Reveals hidden structure in the data
   * Suggests dimension reduction is appropriate
   * Motivates PCA as a way to find these directions systematically

\pagebreak

## 3. Statistical Testing of Covariance Structure

### 3.1 The F-Distribution and Variance Testing

The F-distribution provides a framework for comparing variability between groups. For measurements from two groups:

1. Basic F-test:
   * Test statistic: $F = \frac{s_1^2}{s_2^2}$
   * Null hypothesis $H_0$: Equal variances ($\sigma_1^2 = \sigma_2^2$)
   * Alternative $H_1$: Different variances ($\sigma_1^2 \neq \sigma_2^2$)
   * Reject $H_0$ if $F < F_{\alpha/2}$ or $F > F_{1-\alpha/2}$

2. Interpretation:
   * $F \approx 1$: Similar variability
   * $F \gg 1$: First group more variable
   * $F \ll 1$: Second group more variable
   * Example: with 49 samples each, reject if $F < 0.61$ or $F > 1.64$

### 3.2 Application to Iris Data

Let's examine how sepal width varies across species. The F-test compares the variances of sepal width measurements between all three species simultaneously:

```python
# Results from scipy.stats F-test comparing sepal width variances:
# H0: All species have equal variance in sepal width
# H1: At least one species has different variance
F-statistic: 49.1600
p-value: < 0.0001

# Sample variances of sepal width:
Setosa:     s² = 0.124 cm²
Versicolor: s² = 0.098 cm²
Virginica:  s² = 0.104 cm²
```

This F-statistic was computed using scipy.stats.f_oneway, which performs a one-way ANOVA F-test. For variances, this computes:

\begin{equation*}
F = \frac{\text{variance between groups}}{\text{variance within groups}} = \frac{\sum_{i=1}^k n_i(\bar{x}_i - \bar{x})^2/(k-1)}{\sum_{i=1}^k\sum_{j=1}^{n_i} (x_{ij} - \bar{x}_i)^2/(N-k)}
\end{equation*}

where:

* $k$ = number of groups (3 species)
* $n_i$ = number of samples in group $i$
* $N$ = total number of samples
* $\bar{x}_i$ = mean of group $i$
* $\bar{x}$ = overall mean

This extremely small p-value indicates strong evidence that sepal width variability differs between at least two species. Looking at the sample variances, we can see that Setosa flowers show more variability in sepal width than the other two species.

### 3.3 Multivariate Extension

For full covariance matrices:

1. Test statistic uses determinants:

   * $F = \frac{|\boldsymbol{\Sigma}_1|}{|\boldsymbol{\Sigma}_2|}$
   * $|\boldsymbol{\Sigma}| = \prod_i \lambda_i$ (product of eigenvalues)
   * Represents "volume" of variation

2. Pairwise Species Comparisons:

```python
# Covariance determinant ratios and p-values:
Setosa vs Versicolor:    F = 0.4220, p = 0.0031
Setosa vs Virginica:     F = 0.2408, p < 0.0001
Versicolor vs Virginica: F = 0.5706, p = 0.0522
```

\pagebreak

### 3.4 Visual Comparison

\begin{figure}
\centering
\includegraphics[width=0.5\textwidth]{templates/linalg_010_iris_species_comparison.png}
\caption{Comparison of covariance structure across iris species. Each species shows distinct patterns in their sepal measurements, with different means (stars) and 95\% confidence regions (ellipses).}
\end{figure}

The covariance structure varies notably between species:

1. Setosa (blue):
   * Most compact probability distribution
   * Nearly circular confidence region
   * Suggests similar variance in both length and width, consistent with spherical normal distribution

2. Versicolor (orange):
   * Intermediate spread
   * Elongated ellipse
   * Shows stronger correlation between length and width

3. Virginica (green):
   * Largest overall spread
   * Most elongated confidence region
   * Strongest directional trend

\pagebreak

## 4. Noise Analysis and Statistical Significance

### 4.1 Sources of Variance in the Row and Null Spaces

Recall that in our petal measurements, we found:

* A dominant direction with $\lambda_1 \approx 3.116$
* A weak direction with $\lambda_2 \approx 0.039$

This separation helps us understand three fundamental sources of variance:

1. Natural Variation (Row Space, $\lambda_1 \approx 3.116$):
   * True biological differences between specimens
   * Environmental effects on growth
   * Genetic diversity within species
   * Represents genuine biological signal
   * Explains 98.8% of total variance

2. Measurement Noise (Near "Null Space", $\lambda_2 \approx 0.039$):
   * Instrument precision limits (±0.1mm caliper)
   * Human measurement error
   * Environmental conditions during measurement
   * Comparable to measurement error variance (~0.01 cm²)
   * Could be treated as effective zero

3. Statistical Noise (Affects Both Spaces):
   * Sampling variability
   * Finite sample effects
   * Estimation uncertainty
   * Impacts eigenvalue estimation
   * Decreases with sample size

### 4.2 Using F-tests to Separate Signal from Noise

Our F-test results help distinguish meaningful differences from noise at multiple scales:

1. Within Individual Species:
   * Setosa width variance: 0.124 cm² (signal + noise)
   * Versicolor width variance: 0.098 cm²
   * Virginica width variance: 0.104 cm²
   * Each significantly above measurement noise (p < 0.0001)

2. Within Total Population:
   * Overall width variance: 0.188 cm²
   * Combines both intra-species variation and between-species differences
   * Still significantly above measurement noise (p < 0.0001)
   * Larger than any individual species variance

3. Between Species Structure:
   * Different covariance structures (ellipse shapes)
   * F-test confirms these differences are not random
   * Suggests distinct biological constraints per species

### 4.3 Why Simulation?

To validate our understanding of noise effects, we need to:

1. Quantify the impact of measurement error
2. Test the robustness of our F-statistics
3. Verify our "approximate null space" interpretation

While theoretical analysis helps, simulation offers several advantages:

* We can control the noise level precisely
* We can repeat experiments many times
* We can observe the full distribution of outcomes
* We can validate our statistical assumptions

### 4.4 Noise Analysis Results

To understand how measurement noise affects our analysis, we:

1. Started with the original iris measurements
2. Added random perturbations (±1mm) to each measurement
3. Repeated this process 1000 times
4. Computed F-statistics for each perturbed dataset
5. Analyzed the distribution of these F-statistics

This approach mimics what would happen if we measured the same flowers multiple times with a precision of ±1mm.

\pagebreak

\paragraph{The simulation code:}

```python
# Parameters
n_simulations = 1000
measurement_noise = 0.1  # 1mm measurement error

# Store results
F_stats = []

# Simulate noisy measurements
for _ in range(n_simulations):
    # Add random noise to measurements
    X_noisy = X + np.random.normal(0, measurement_noise, X.shape)
    
    # Compute F-statistic between species
    F_stats_sim = []
    for i in range(3):
        for j in range(i+1, 3):
            mask_i = species == i
            mask_j = species == j
            
            # Compute covariance matrices
            cov_i = np.cov(X_noisy[mask_i].T)
            cov_j = np.cov(X_noisy[mask_j].T)
            
            # Compute F-statistic
            F_stat = np.linalg.det(cov_i) / np.linalg.det(cov_j)
            F_stats_sim.append(F_stat)
```

Using this approach, we simulated 1000 datasets with 1mm measurement error:

\pagebreak

\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{templates/linalg_010_noise_analysis.png}
\caption{Left: Original iris measurements. Right: Distribution of F-statistics under simulated measurement noise.}
\end{figure}

\paragraph{The simulation reveals:}

1. Robustness of F-statistics:
   * F-statistics remain significant despite noise because the between-species differences (0.188 cm²) are much larger than our measurement noise (0.01 cm²)
   * Species differences persist under measurement error as shown by the clear separation of F-statistic distributions in the right plot
   * Natural variation dominates measurement noise - compare the width of the F-statistic distributions (~0.1) to their separation (~0.3)

2. Precision Requirements:
   * 1mm measurement error (typical caliper precision)
   * Natural variation: 2-7mm from the square root of covariance matrix diagonals (√0.188 ≈ 4.3mm average)
   * Signal-to-noise ratio = 4.3mm/1mm ≈ 4.3 approaches our threshold of 5 for reliable detection

3. Practical Implications:
   * Measurement precision is adequate because 1mm error is smaller than the natural variation we observe
   * Species differences are robust because F-statistic distributions remain well-separated even with noise
   * Current sample sizes (50 per species) provide reliable estimates as shown by the narrow F-statistic distributions

\pagebreak

## Endnotes

The confidence region is defined mathematically by points $\mathbf{x}$ satisfying:
\begin{equation*}
(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}) = \chi^2_{2,0.95}
\end{equation*}

The value $\chi^2_{2,0.95} = 5.991$ used in the equation above is the 95th percentile of the chi-square distribution with 2 degrees of freedom. This specific value arises because we're working in 2 dimensions (sepal length and width) and want a 95\% confidence region.

Note on Population vs Sample Covariance:
Throughout this visualization, we've used the sample covariance matrix $\mathbf{S}$ as an estimate of the population covariance matrix $\boldsymbol{\Sigma}$. The key differences are:

1. Population covariance $\boldsymbol{\Sigma}$ uses the true mean $\boldsymbol{\mu}$ and divides by $n$:
   \begin{equation*}
   \boldsymbol{\Sigma} = \frac{1}{n}\sum_{i=1}^n (\mathbf{x}_i-\boldsymbol{\mu})(\mathbf{x}_i-\boldsymbol{\mu})^T
   \end{equation*}

2. Sample covariance $\mathbf{S}$ uses the sample mean $\bar{\mathbf{x}}$ and divides by $(n-1)$:
   \begin{equation*}
   \mathbf{S} = \frac{1}{n-1}\sum_{i=1}^n (\mathbf{x}_i-\bar{\mathbf{x}})(\mathbf{x}_i-\bar{\mathbf{x}})^T
   \end{equation*}

The $(n-1)$ denominator in the sample covariance makes it an unbiased estimator of $\boldsymbol{\Sigma}$, meaning $E[\mathbf{S}] = \boldsymbol{\Sigma}$. This adjustment accounts for the fact that we're using the estimated mean $\bar{\mathbf{x}}$ rather than the true mean $\boldsymbol{\mu}$. For large sample sizes, the difference between using $n$ or $(n-1)$ becomes negligible since:

\begin{equation*}
\lim_{n \to \infty} \frac{n-1}{n} = 1
\end{equation*}

However, for small samples, using $(n-1)$ is crucial for unbiased estimation. For example, with $n=10$ samples, using $n$ instead of $(n-1)$ would underestimate the variance by about 10%.
