---
title: "Feature Scaling and Variable Importance Foo"
subtitle: "Week 6"
author: "Linear Algebra and Estimation Theory"
date: "2025-02-09"
---

# Feature Scaling and Variable Importance

## 1. Why Scale Features?

\paragraph{1.1 Motivation: A Logistic Regression Example}

![Scaling Effects](templates/011/scaling_comparison.png)

\subparagraph{The plots show:}

- Left: Original scales show two distinct clusters for each class
- Middle: Same axis limits reveal the vertical structure of the data
- Right: After standardization, we see the natural separation between classes
- Purple and yellow points show the two classes
- Notice how Feature 1 (horizontal axis) provides better class separation

\subparagraph{Consider a binary classification problem with two features:}

- Feature 1: Small scale (around ±2)
- Feature 2: Large scale (around ±100)

\pagebreak

\subparagraph{Without scaling:}

```python
# Generate synthetic classification dataset
from sklearn.datasets import make_classification

# Create dataset with two informative features of different importance
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=2,
    class_sep=2.0,
    weights=[0.8, 0.2],  # Make first feature more important
    flip_y=0.1,
    random_state=42
)

# Scale second feature to be much larger
X[:, 1] = X[:, 1] * 50  # Make second feature 100x larger

# Fit logistic regression
model_raw = LogisticRegression()
model_raw.fit(X, y)
print("Raw coefficients:", model_raw.coef_[0])
# Output shows Feature 2 appears more important due to scale!
```

\pagebreak

\subparagraph{With scaling:}
```
# Scale features to zero mean, unit variance
feature1_scaled = (feature1 - feature1.mean()) / feature1.std()
feature2_scaled = (feature2 - feature2.mean()) / feature2.std()

model_scaled = LogisticRegression()
model_scaled.fit(np.column_stack([feature1_scaled, feature2_scaled]), y)
print("Scaled coefficients:", model_scaled.coef_[0])
# Output shows equal importance after scaling!
```


\subparagraph{Key insights:}

1. Without scaling: Feature 2 appears to dominate due to its large scale
2. With scaling: We can see Feature 1 is actually more important
3. The classes form clear diagonal patterns in the standardized space
4. Scaling reveals the true classification boundary

![Coefficient comparison](templates/011/coefficient_comparison.png)

\pagebreak

\subparagraph{Notes:}

- Feature 1 was designed to be more important (weight=0.8 vs 0.2)
- Feature 2 was artificially scaled up by 50x
- Coefficients in logistic regression show log-odds impact
- Feature 1 range: approximately ±3 units
- Feature 2 range: approximately ±150 units after scaling
- Without scaling, a 1-unit change in Feature 2 appears more important simply due to scale
- After standardization, both features are in standard deviation units
- The scatter plots reveal:
  * Clear class separation in standardized space
  * Feature 1 provides better discrimination between classes
  * Scaling unmasks the true classification boundary

\pagebreak

\paragraph{1.2 Common Scaling Methods}

![Normalization Steps](templates/011/normalization_steps.png)

\subparagraph{The plots above show the steps of standardization:} 

- Left: Original data with arbitrary mean and standard deviation
- Middle: After centering (subtracting mean)
- Right: After scaling (dividing by standard deviation)

\pagebreak

\paragraph{Standardization (Z-score)}

   ```python
   col = X[:,j]
   col_std = (col - col.mean()) / col.std()
   ```

\subparagraph{When to use standardization (z-score scaling):}

1. Machine Learning Algorithms
   - Linear/Logistic Regression
   - Neural Networks
   - Support Vector Machines (SVM)
   - Any algorithm using gradient descent
   - Helps prevent features with larger scales from dominating

2. Statistical Analysis
   - Hypothesis testing
   - When assuming normal distributions
   - Comparing variables with different units
   - Computing z-scores for outlier detection

3. Feature Selection/Importance
   - Comparing coefficient magnitudes
   - Principal Component Analysis (PCA)
   - When feature importance should be scale-independent

4. Distance Metrics
   - Euclidean distance calculations
   - When all features should contribute equally
   - Clustering algorithms (k-means, hierarchical)

\subparagraph{Properties:}

- Transforms to zero mean, unit variance
- Preserves shape of distribution
- Preserves outliers (unlike min-max)
- Output is unitless (standard deviations)
- Linear transformation

\subparagraph{Limitations:}

1. Assumes roughly normal distribution
2. Sensitive to outliers
3. Loses original scale/units
4. May not be appropriate for bounded data

\subparagraph{Example scenarios:}

- Comparing test scores across different subjects
- Analyzing financial ratios
- Processing scientific measurements
- Feature engineering for ML models

\subparagraph{Note on Standardization and Normalization:}

- Standardization is a form of normalization
- Normalization is a broader term that includes other scaling methods
- Frequently, the terms are used interchangeably

\pagebreak

\paragraph{Min-Max Scaling}

![Min-Max Steps](templates/011/minmax_steps.png)

\subparagraph{The plots above show the steps of min-max scaling:}

- Left: Original skewed distribution with arbitrary bounds
- Middle: After shifting minimum to zero
- Right: After scaling maximum to one

   ```python
   # For each feature j:
   X_norm[:,j] = (X[:,j] - min(X[:,j])) / (max(X[:,j]) - min(X[:,j]))
   ```

\subparagraph{When to use min-max scaling:}

1. Neural Networks
   - Input layers often work best with data in [0,1] range
   - Helps with gradient descent convergence
   - Particularly important for activation functions with bounded ranges (sigmoid, tanh)

2. Image Processing
   - Pixel values naturally fit in [0,255] or [0,1]
   - Preserves zero values which often represent "no signal"
   - Maintains relative distances in bounded space

3. Feature Visualization
   - Creates interpretable plots with consistent ranges
   - Helpful when comparing features with different units
   - Makes heatmaps and color maps more intuitive

4. Distance-Based Algorithms
   - K-means clustering
   - K-nearest neighbors
   - When equal feature ranges are important

\subparagraph{Properties:}

- Scales to [0,1] range
- Preserves zero values
- Sensitive to outliers
- Good for bounded features
- Maintains relative distances between points

\subparagraph{Limitations:}

1. Sensitive to outliers
2. Doesn't handle new data outside original bounds well
3. May not be appropriate when data is naturally unbounded
4. Can compress variation in dense regions

\subparagraph{Example scenarios:}

- Normalizing survey responses (1-5 scale)
- Processing sensor readings with known physical limits
- Comparing performance metrics (0-100%)
- Image pixel normalization

\pagebreak

\paragraph{Robust Scaling}

![Robust Scaling Steps](templates/011/robust_steps.png)

\subparagraph{The plots above show the steps of robust scaling:}

- Left: Original data with outliers affecting the distribution
- Middle: After centering using median (more robust than mean)
- Right: After scaling using IQR (more robust than standard deviation)

   ```python
   # For each feature j:
   X_rob[:,j] = (X[:,j] - median(X[:,j])) / IQR(X[:,j])
   ```

\subparagraph{When to use robust scaling:}

1. Outlier-Heavy Data
   - Financial data with extreme events
   - Sensor data with measurement errors
   - Any data where outliers shouldn't dominate scaling

2. Skewed Distributions
   - Long-tailed distributions
   - Power law distributions
   - Non-normal data

3. Robust Statistical Methods
   - Robust regression
   - Outlier detection
   - Robust covariance estimation

4. Data Quality Issues
   - Missing value imputation
   - Noisy measurements
   - Data collection errors

\subparagraph{Properties:}

- Centers using median (50th percentile)
- Scales using IQR (75th - 25th percentile)
- Less sensitive to outliers than z-score
- Preserves data shape better with outliers
- Non-parametric (no distribution assumptions)

\subparagraph{Limitations:}

1. Less efficient with normal data
2. May not scale well with very small datasets
3. Computationally slower because:
   - Requires sorting data to find median (O(n log n))
   - Needs two passes through sorted data for IQR
   - More complex than mean/std which are O(n)
   - Memory overhead from sorting operation
4. Less widely supported in some libraries

\subparagraph{Example scenarios:}

- Stock market returns with crashes
- Sensor readings with interference
- Survey data with extreme responses
- Medical measurements with anomalies

\subparagraph{Key Considerations:}

- Standardization: Best for algorithms assuming normal distributions
- Min-Max: Best when you need bounded values
- Robust: Best when data has outliers or is skewed

\pagebreak

## 2. Mathematical Properties of Scaling

### 2.1 Linear Transformations

\paragraph{Standardization} is a linear transformation using a diagonal matrix:

For data matrix $\mathbf{X}$ with $n$ samples and $p$ features:

1. Center: $\tilde{\mathbf{X}} = \mathbf{X} - \boldsymbol{\mu}$ where $\boldsymbol{\mu}$ is the mean vector
   - $\boldsymbol{\mu} = (\mu_1, \ldots, \mu_p)$
2. Scale: $\hat{\mathbf{X}} = \tilde{\mathbf{X}}\mathbf{D}^{-1}$ where $\mathbf{D} = \text{diag}(\sigma_1, \ldots, \sigma_p)$ contains standard deviations

\subparagraph{Properties:}

- Diagonal matrix $\mathbf{D}^{-1}$ scales each feature independently
- The Inverse of the Diagonal Matrix is the Diagonal Matrix of the Reciprocals of the Original Diagonal Elements
- Preserves linear relationships: $\alpha\hat{\mathbf{X}}_1 + \beta\hat{\mathbf{X}}_2 = \widehat{\alpha\mathbf{X}_1 + \beta\mathbf{X}_2}$
  * This means scaling commutes with linear combinations
  * Example: If we scale height (m) and weight (kg) to unit variance:
    - Adding 2×height + 3×weight then scaling
    - Equals: Adding 2×(scaled height) + 3×(scaled weight)
  * Important for PCA because it preserves linear patterns in the data
  * Lines remain lines, planes remain planes
- Changes distances: $\|\hat{\mathbf{x}}_i - \hat{\mathbf{x}}_j\| \neq \|\mathbf{x}_i - \mathbf{x}_j\|$
  * Original distances depend on feature units (e.g., meters vs kilometers)
  * Scaling changes relative importance of each feature
  * Example: Distance between points (height=1.8m, weight=70kg) and (height=1.7m, weight=75kg)
    - Original: $\sqrt{(0.1\text{m})^2 + (5\text{kg})^2} \approx 5.01$ (dominated by weight)
    - After scaling: $\sqrt{(1\sigma_h)^2 + (1\sigma_w)^2} \approx 1.41$ (equal contribution)
  * This is why scaling matters for distance-based methods (k-means, kNN)

\pagebreak

\subparagraph{Example with 2 features:}

Let $\mathbf{X} = \begin{bmatrix} 1000 & 2 \\ 2000 & 4 \\ 3000 & 6 \end{bmatrix}$ be our original data matrix

The scaling matrix $\mathbf{D}^{-1} = \begin{bmatrix} 1/1000 & 0 \\ 0 & 1/2 \end{bmatrix}$

\subparagraph{Then the scaled data is:}

$\hat{\mathbf{X}} = \mathbf{X}\mathbf{D}^{-1} = \begin{bmatrix} 1.0 & 1.0 \\ 2.0 & 2.0 \\ 3.0 & 3.0 \end{bmatrix}$

```python
# Example code to perform scaling
>>> import numpy as np

# Original data
>>> X = np.array([[1000, 2], [2000, 4], [3000, 6]])

# Scaling matrix
>>> D_inv = np.array([[1/1000, 0], [0, 1/2]])

# Scaled data
>>> X_scaled = X @ D_inv
>>> print(X_scaled)
[[1. 1.]
 [2. 2.]
 [3. 3.]]
```

\subparagraph{Key effects:}

1. Each feature now varies on same scale: $\text{std}(\hat{\mathbf{X}}_j) = 1$
2. Linear patterns preserved: $\text{span}\{\hat{\mathbf{X}}\} \cong \text{span}\{\mathbf{X}\}$
3. Relative distances changed: $\|\hat{\mathbf{x}}_i - \hat{\mathbf{x}}_j\| \neq \|\mathbf{x}_i - \mathbf{x}_j\|$
4. Angles between vectors preserved: $\cos(\theta_{\hat{\mathbf{x}},\hat{\mathbf{y}}}) = \cos(\theta_{\mathbf{x},\mathbf{y}})$

\pagebreak

\paragraph{2.2 Impact on Statistics}

Standardization affects key statistical properties:

\paragraph{Mean and Variance}

After standardization:

- Mean becomes zero: $\mathbb{E}[\hat{\mathbf{X}}] = \mathbf{0}$
- Variance becomes one: $\text{Var}(\hat{\mathbf{X}}_j) = 1$
- Proof:

\begin{align*}
  \hat{\mathbf{X}}_j = \frac{\mathbf{X}_j - \mu_j}{\sigma_j} & \tag{standardization formula} \\[1em]
  \mathbb{E}[\hat{\mathbf{X}}_j] = \mathbb{E}[\frac{\mathbf{X}_j - \mu_j}{\sigma_j}] & \tag{apply expectation} \\
  = \frac{\mathbb{E}[\mathbf{X}_j] - \mu_j}{\sigma_j} & \tag{linearity of expectation} \\
  = \frac{\mu_j - \mu_j}{\sigma_j} = 0 & \tag{$\mathbb{E}[\mathbf{X}_j] = \mu_j$} \\[1em]
  \text{Var}(\hat{\mathbf{X}}_j) = \mathbb{E}[(\frac{\mathbf{X}_j - \mu_j}{\sigma_j})^2] & \tag{variance definition} \\
  = \frac{\mathbb{E}[(\mathbf{X}_j - \mu_j)^2]}{\sigma_j^2} & \tag{move constant out} \\
  = \frac{\text{Var}(\mathbf{X}_j)}{\sigma_j^2} & \tag{variance definition} \\
  = \frac{\sigma_j^2}{\sigma_j^2} = 1 & \tag{$\text{Var}(\mathbf{X}_j) = \sigma_j^2$}
\end{align*}

\pagebreak

\paragraph{Correlation Coefficients}

Standardization preserves correlations:

- Pearson correlation: $\rho_{ij} = \frac{\text{Cov}(\mathbf{X}_i, \mathbf{X}_j)}{\sigma_i\sigma_j}$
- After standardization: $\rho_{ij} = \text{Cov}(\hat{\mathbf{X}}_i, \hat{\mathbf{X}}_j)$
- Proof:

\begin{align*}
  \text{Cov}(\hat{\mathbf{X}}_i, \hat{\mathbf{X}}_j) & = \mathbb{E}[\frac{(\mathbf{X}_i - \mu_i)}{\sigma_i}\frac{(\mathbf{X}_j - \mu_j)}{\sigma_j}] \tag{covariance of standardized variables} \\[1em]
  & = \frac{1}{\sigma_i\sigma_j}\mathbb{E}[(\mathbf{X}_i - \mu_i)(\mathbf{X}_j - \mu_j)] \tag{move constants out} \\[1em]
  & = \frac{\text{Cov}(\mathbf{X}_i, \mathbf{X}_j)}{\sigma_i\sigma_j} \tag{covariance definition} \\[1em]
  & = \rho_{ij} \tag{correlation coefficient definition}
\end{align*}

\paragraph{Covariance Structure}

The covariance matrix after standardization:

- Becomes correlation matrix: $\boldsymbol{\Sigma}_{\hat{\mathbf{X}}} = \mathbf{R}$
- Diagonal elements are 1
- Off-diagonal elements are correlations
- Properties:
  * Symmetric: $\mathbf{R} = \mathbf{R}^T$
  * Positive semidefinite
  * All entries in [-1, 1]
  * Determinant ≤ 1

\pagebreak

Example:
```python
# Original covariance matrix
Σ = [[100, 30],
     [30, 25]]

# After standardization becomes correlation matrix
R = [[ 1.0, 0.6],
     [0.6, 1.0]]
```

Key insights:

1. Standardization makes variances comparable
2. Preserves correlation structure
3. Makes covariance interpretable as correlation
4. Useful for comparing relationships across different scales

\pagebreak

## 3. Measuring Variable Importance

\paragraph{3.1 Variance-Based Methods}

After standardization, we can measure variable importance through variance:

\subparagraph{Total Variance Contribution}
- Each feature's variance after standardization is 1.0
- In PCA, eigenvalues of covariance matrix show variance explained
- Larger eigenvalues indicate more important directions
- $\lambda_i = \sigma_i^2$ where $\sigma_i$ are singular values (!!!)

\subparagraph{Explained Variance Ratio}
- Proportion of variance explained by each component
- $r_i = \frac{\lambda_i}{\sum_j \lambda_j}$
- Cumulative ratio: $R_k = \sum_{i=1}^k r_i$
- Used for dimensionality selection (e.g., keep 95% variance)

\subparagraph{Limitations}
- High variance doesn't always mean high importance
- Sensitive to outliers and noise
- May miss nonlinear relationships
- Example: Stock returns may have high variance but low signal

\pagebreak

## 4. Practical Applications

\paragraph{4.1 When to Scale}

\subparagraph{Distance-Based Algorithms}
- K-means clustering
  * Equal feature influence on distances
  * Prevents dominance by large-scale features
  * Example: Clustering customers by age (years) and income (dollars)

\subparagraph{Gradient-Based Optimization}
- Neural Networks
  * Faster convergence with normalized inputs
  * More stable gradients
  * Example: Deep learning on mixed sensor data

\subparagraph{Feature Comparison}
- Variable importance
  * Comparable coefficient magnitudes
  * Fair feature selection
  * Example: Lasso regression on medical predictors

\pagebreak

\paragraph{4.2 When Not to Scale}

\subparagraph{Interpretability Requirements}
- Business metrics
  * Keep original units for stakeholder understanding
  * Maintain natural relationships
  * Example: Sales forecasting in actual currency

\subparagraph{Natural Relationships}
- Physical measurements
  * Preserve meaningful ratios
  * Maintain domain-specific relationships
  * Example: Length × width = area should hold

\subparagraph{Categorical Variables}
- One-hot encoded features
  * Already on same scale (0/1)
  * Scaling changes semantic meaning
  * Example: Binary indicators for product categories

\pagebreak

\paragraph{4.3 Implementation Considerations}

\subparagraph{Pipeline Design}
- Scaling order matters:
  1. Split train/test first
  2. Fit scaler on training data only
  3. Transform both sets using training statistics
  * Why? Prevent data leakage

\pagebreak

\subparagraph{Cross-Validation}
- Proper scaling in CV:
  * Fit scaler inside each fold
  * Use same scaler for validation
  * Never fit on validation data
  * Example code:


```python
for train_idx, val_idx in cv_splits:
    X_train, X_val = X[train_idx], X[val_idx]
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
```

\pagebreak

\subparagraph{Test Set Handling}

- Production deployment:
  * Save scaler parameters from training
  * Apply exact same transformation to new data
  * Monitor for distribution shifts
  * Example:

```python
# During training
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
joblib.dump(scaler, 'scaler.pkl')

# In production
scaler = joblib.load('scaler.pkl')
X_new_scaled = scaler.transform(X_new)
```

\subparagraph{Key Considerations:}
1. Data leakage prevention
2. Reproducibility
3. Production deployment
4. Distribution monitoring
