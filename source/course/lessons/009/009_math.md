---
title: "Random Vectors and Their Statistical Properties"
subtitle: "Week 5"
author: "Linear Algebra and Estimation Theory"
date: "2025-02-02"
---

# Random Vectors and Their Properties

## 0. What is a Random Variable?

### 0.1 Definition and Basic Properties
- A random variable $X$ is a function from a sample space $\Omega$ to real numbers $\mathbb{R}$
- Maps uncertain outcomes to numerical values


#### Three key examples:

1. Rolling a die:
   * Sample space $\Omega = \{1,2,3,4,5,6\}$
   * $X(\omega) = \omega$ maps each outcome to its value
   * $P(X=k) = \frac{1}{6}$ for $k \in \{1,\ldots,6\}$
   * Mean $E[X] = 3.5$
   * Variance $\text{Var}(X) = 2.916$

2. Measuring sensor data:
   * Sample space $\Omega = \mathbb{R}$ (all possible readings)
   * $X(\omega)$ = actual reading value
   * Often modeled as Normal: $X \sim N(\mu, \sigma^2)$
   * Example: Temperature sensor with $\mu = 20°C$, $\sigma = 0.1°C$

3. Binary outcome:
   * Sample space $\Omega = \{\text{success}, \text{failure}\}$
   * $X(\omega) = \begin{cases} 1 & \text{if success} \\ 0 & \text{if failure} \end{cases}$
   * $P(X=1) = p$, $P(X=0) = 1-p$
   * Mean $E[X] = p$
   * Variance $\text{Var}(X) = p(1-p)$

\pagebreak

### 0.2 Key Concepts
- Distribution: How probability is assigned to values
  * Discrete: PMF $P(X=x)$
  * Continuous: PDF $f_X(x)$
- Expected Value: "Average" or center
  * $E[X] = \sum_x xP(X=x)$ (discrete)
  * $E[X] = \int_{-\infty}^{\infty} xf_{X}(x)dx$ (continuous)
- Variance: Spread around mean
  * $\text{Var}(X) = E[(X-E[X])^2]$
  * Measures average squared deviation

\begin{figure}[h]
\caption{Plots of PMFs}
\centering
\begin{tikzpicture}[scale=0.8]
% PMF for die roll
\begin{scope}[xshift=-4cm]
    \draw[->] (0,0) -- (7,0) node[right] {$x$};
    \draw[->] (0,0) -- (0,2) node[above] {$P(X=x)$};
    \foreach \x in {1,...,6} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\x};
        \draw[fill=blue] (\x,1/6) circle (2pt);
        \draw (\x,0) -- (\x,1/6);
    }
    \node[below] at (3.5,-0.5) {Die Roll PMF};
\end{scope}

% PMF for coin flip
\begin{scope}[xshift=4cm]
    \draw[->] (0,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,0) -- (0,2) node[above] {$P(X=x)$};
    \foreach \x/\l in {1/0,2/1} {
        \draw (\x,0.1) -- (\x,-0.1) node[below] {\l};
        \draw[fill=red] (\x,0.5) circle (2pt);
        \draw (\x,0) -- (\x,0.5);
    }
    \node[below] at (1.5,-0.5) {Coin Flip PMF};
\end{scope}
\end{tikzpicture}
\end{figure}

\begin{figure}[h]
\caption{Plots of PDFs}
\centering
\begin{tikzpicture}[scale=0.8]
% PDF for normal distribution
\begin{scope}[xshift=-4cm]
    \draw[->] (-3,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,0) -- (0,1) node[above] {$f(x)$};
    \draw[blue, thick, smooth] plot[domain=-3:3, samples=100] 
        (\x,{exp(-(\x)^2/2)/sqrt(2*pi)});
    \node[below] at (0,-0.5) {Normal PDF};
\end{scope}

% PDF for exponential distribution
\begin{scope}[xshift=4cm]
    \draw[->] (0,0) -- (4,0) node[right] {$x$};
    \draw[->] (0,0) -- (0,1.2) node[above] {$f(x)$};
    \draw[red, thick, smooth] plot[domain=0:4, samples=100] 
        (\x,{exp(-\x)});
    \node[below] at (2,-0.5) {Exponential PDF};
\end{scope}
\end{tikzpicture}
\end{figure}

\pagebreak

### 0.3 Linear Properties
- Linearity of Expectation:
  * $E[aX + b] = aE[X] + b$
  * $E[X + Y] = E[X] + E[Y]$
- Variance Properties:
  * $\text{Var}(aX) = a^{2}\text{Var}(X)$
  * $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$ (if independent)
  * $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$ (if dependent)

## 1. Introduction to Random Vectors as Linear Transformations

### 1.1 Random Vectors in Vector Spaces
- Definition: A random vector $\mathbf{X}$ is one complete set of measurements
  * One row in a DataFrame
  * All measurements taken together at one time
  * Multiple random vectors form our dataset

Example: Weather Station
```python
# Each row is a random vector X
data = pd.DataFrame({
    'Temp'    : [20.1,   20.2,   19.8  ],
    'Humidity': [45.0,   48.0,   52.0  ],
    'Pressure': [101.3,  101.2,  101.4 ]
})
# $X_{1} = [20.1, 45.0, 101.3]^{\mathrm{T}}$  # first random vector
# $X_{2} = [20.2, 48.0, 101.2]^{\mathrm{T}}$  # second random vector
# $X_{3} = [19.8, 52.0, 101.4]^{\mathrm{T}}$  # third random vector
```

Key points:

  * Each row is one random vector
  * All measurements in a row come from same time/instance
  * Our dataset is a collection of random vectors
  * They likely come from same distribution

### 1.2 Properties of Expected Value
- Expected value $E[X]$ follows simple rules:
  * For constants $a$ and $b$: $E[aX + b] = aE[X] + b$
  * For two random variables: $E[X + Y] = E[X] + E[Y]$
  * These rules make calculations easier
- Examples:
  * If $X$ is die roll and $a=2$: $E[2X] = 2E[X] = 2(3.5) = 7$
  * If $X$ is die roll and $b=1$: $E[X + 1] = E[X] + 1 = 4.5$

### 1.3 Linear Transformation Properties
1. Linearity of Expectation:
   $$E[a\mathbf{X} + b\mathbf{Y}] = aE[\mathbf{X}] + bE[\mathbf{Y}]$$
   
2. Matrix Operations:
   For matrix $A$ and random vector $\mathbf{X}$:
   $$E[A\mathbf{X}] = AE[\mathbf{X}]$$

3. Example: Linear Combination
   Let $\mathbf{X} = \begin{bmatrix} X_1 \\ X_2 \end{bmatrix}$ with $E[\mathbf{X}] = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$
   
   For $A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$:
   
   $$E[A\mathbf{X}] = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ 7 \end{bmatrix}$$

### 1.4 Domain, Range, and Fundamental Subspaces
- Domain: Sample space $\Omega$ (all possible outcomes)
  * For n observations: Points in $\mathbb{R}^n$
  * Each observation is one point in sample space
  * Row space of data matrix lives here
  * Example: n=1000 stock returns form points in $\mathbb{R}^{1000}$

- Range: Subset of $\mathbb{R}^p$ where $p$ is dimension
  * Feature space where random vector lives
  * Column space of data matrix lives here
  * Example: p=10 stocks form vectors in $\mathbb{R}^{10}$

- Connection to Fundamental Subspaces:
  * Row Space $\subseteq$ Domain: Linear combinations of observations
  * Column Space $\subseteq$ Range: Achievable random vectors
  * Null Space $\subseteq$ Range: Zero-variance directions
  * Left Null Space $\subseteq$ Domain: Zero-correlation observations

- Example with Stock Returns:
  * Domain: Space of all possible trading days
  * Range: Space of all possible stock return vectors
  * Row Space: Trading patterns across days
  * Column Space: Achievable portfolio returns

### 1.5 Connection to Data Structures
Random vectors in practice are stored and manipulated using numpy arrays and pandas DataFrames:

1. Single Random Variable → 1D Array/Series:
   * Each realization is one number
   * Collection forms empirical distribution
   * Example (die rolls):
     ```python
     X = np.array([3, 6, 1, 4, 2, 5])  # 6 rolls
     ```
   * Properties:
     - Mean: `X.mean()` estimates $E[X]$
     - Variance: `X.var()` estimates $\text{Var}(X)$
     - Histogram: empirical PMF

2. Random Vector → 2D Array/DataFrame:
   * Each row is one realization of entire vector
   * Columns represent different variables
   * Example (temperature sensors):
     ```python
     X = np.array([[20.1, 20.3, 19.9],  # One multivariate observation
                   [20.2, 20.1, 20.0],  # Another observation
                   [19.8, 20.2, 20.1]]) # Third observation
     ```
   * Properties:
     - Mean vector: `X.mean(axis=0)` estimates $E[\mathbf{X}]$
     - Covariance: `np.cov(X.T)` estimates $\text{Cov}(\mathbf{X})$

\pagebreak

3. Data Organization:
   * numpy arrays: Pure numerical operations
     - Fast matrix operations
     - Linear algebra computations
     - Statistical calculations
   * pandas DataFrames: Data management
     - Labels and metadata
     - Missing value handling
     - Time series features
     ```python
     df = pd.DataFrame(X, 
                      columns=['Sensor1', 'Sensor2', 'Sensor3'],
                      index=['Day1', 'Day2', 'Day3'])
     ```

4. Connection to Linear Algebra:
   * Each observation is a vector in $\mathbb{R}^p$
   * Sample mean is projection onto 1-vector
   * Sample covariance involves outer products
   * Linear transformations preserve structure:
     ```python
     # Linear transform: scale and rotate
     A = np.array([[2, 1], [1, 2]])
     X_transformed = X @ A  # Still a random vector!
     ```

\pagebreak

## 2. Statistical Properties Through Linear Transformations

### 2.1 Mean Vector as Translation Operator
- Mean vector $\boldsymbol{\mu} = E[\mathbf{X}]$ defines translation:
  * Each component: $\mu_i = E[X_i]$
  * Represents center of mass of distribution
  * First moment of probability distribution

- Centering operation $\mathbf{X} - \boldsymbol{\mu}$:
  * Moves data to origin
  * Preserves relative positions
  * Makes second moments easier to interpret
  * Example with temperature data:
    ```python
    X = [20.1, 20.2, 19.8]  # original readings
    $\mu = 20.0$            # mean temperature
    X - $\mu$ = [0.1, 0.2, -0.2] # centered readings
    ```

- Translation invariance properties:

  * Variance unchanged by translation
  * Covariance unchanged by translation
  * Correlation unchanged by translation
  * Proof: $\text{Var}(X + c) = E[(X + c - (\mu + c))^2] = E[(X - \mu)^2] = \text{Var}(X)$

- Effect on covariance structure:

  * Covariance of centered data: $\text{Cov}(\mathbf{X} - \boldsymbol{\mu}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$
  * Simplifies calculations by removing mean terms
  * Makes geometric interpretation clearer
  * Essential for PCA and other decompositions

### 2.2 Variance as Quadratic Form
- For scalar random variable: $\text{Var}(X) = E[(X-\mu)^2]$
- Vector generalization: $\text{Var}(\mathbf{X}) = E[(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T]$
- Quadratic form interpretation:
  * For any direction $\mathbf{v}$: $\mathbf{v}^T\text{Var}(\mathbf{X})\mathbf{v}$
  * Geometric meaning: squared length in transformed space

### 2.3 Covariance Through Subspaces
Connection to fundamental subspaces:

1. Row Space:
   * Spans directions of non-zero variation
   * Basis reveals principal components
   * Dimension = rank of covariance matrix

2. Null Space:
   * Contains constant random variables
   * Linear combinations with zero variance
   * Important for dimensionality reduction

3. Column Space:
   * Range of possible variations
   * Same as row space (symmetry)
   * Determines achievable transformations

4. Left Null Space:
   * Directions of zero variance
   * Same as null space (symmetry)
   * Critical for understanding dependencies

### 2.4 Correlation Structure
- Correlation as normalized covariance:
  * $\rho_{ij} = \frac{\text{Cov}(X_i,X_j)}{\sqrt{\text{Var}(X_i)\text{Var}(X_j)}}$
- Geometric interpretation:
  * Cosine of angle between centered variables
  * Invariant to scaling
  * Range [-1,1] through Cauchy-Schwarz

\pagebreak

## 3. Understanding Random Vectors Through Data

### 3.1 The Iris Dataset
Let's examine real multivariate data using the famous iris dataset:
```python
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Look at first few measurements
print("First few random vectors (rows):")
print(df.head())

# Each row is one random vector of 4 measurements
# Each column is one type of measurement
```

### 3.2 Statistical Properties in Practice
Let's compute basic properties:
```python
# Mean vector (center of our cloud of points)
mean_vector = df.mean()
print("\nMean vector (expected value):")
print(mean_vector)

# Covariance matrix (spread and relationships)
cov_matrix = df.cov()
print("\nCovariance matrix:")
print(cov_matrix)
```

\pagebreak

### 3.3 Visualizing Multivariate Data
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Look at pairwise relationships
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Multivariate Relationships in Iris Data')

# Show correlation structure
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Structure')

# Plot first two features with confidence ellipse
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, 
                x='sepal length (cm)',
                y='sepal width (cm)')

# Add mean vector
plt.scatter(mean_vector['sepal length (cm)'],
           mean_vector['sepal width (cm)'],
           color='red', s=100, label='Mean Vector')

# Add 95% confidence ellipse
from scipy import stats
cov = df[['sepal length (cm)', 'sepal width (cm)']].cov()
vals, vecs = np.linalg.eigh(cov)
angle = np.degrees(np.arctan2(vecs[1,0], vecs[0,0]))
plt.gca().add_patch(plt.matplotlib.patches.Ellipse(
    mean_vector[['sepal length (cm)', 'sepal width (cm)']],
    2*np.sqrt(5.991*vals[0]), 2*np.sqrt(5.991*vals[1]),
    angle=angle, fill=False, color='red', 
    label='95% Confidence Region'))
plt.legend()
plt.title('Geometric View of Random Vectors')
```

The analysis reveals:

1. Correlation Structure:
   ```python
   print(df.corr().round(3))
   ```

2. Eigenvalues of covariance:
   ```python
   print(np.linalg.eigvals(cov).round(3))
   ```

3. Principal directions (eigenvectors):
   ```python
   print(vecs.round(3))
   ```
- Level sets (regions of constant probability density):
  * For multivariate normal, these are ellipsoids
  * Each ellipsoid represents points with equal probability
  * Like contour lines on a topographic map, but in higher dimensions
  * Example with iris data:
    ```python
    # Points where (x-$\mu$)$^{T}$$\Sigma^{-1}$(x-$\mu$) = constant
    # Form nested ellipsoids of decreasing probability
    levels = [0.5, 1, 2, 3]  # chi-square values
    for level in levels:  
        plt.gca().add_patch(plt.matplotlib.patches.Ellipse(
            mean_vector[['sepal length', 'sepal width']],
            2*np.sqrt(level*vals[0]), 2*np.sqrt(level*vals[1]),
            angle=angle, fill=False, alpha=0.3,
            label=f'Level set {level}'))
    ```
  * Properties:
    - Principal axes align with eigenvectors of $\boldsymbol{\Sigma}$
    - Lengths proportional to square roots of eigenvalues
    - Center at mean vector $\boldsymbol{\mu}$
    - Nested shells of equal probability

- Connection to fundamental subspaces:
  * Row space: directions of non-zero probability density
  * Null space: degenerate directions (if any)
  * Determinant $|\boldsymbol{\Sigma}|$ gives volume

### 3.4 Independence Properties
- Components independent iff covariance matrix diagonal
- Equivalent to orthogonal eigenvectors with:
  * Each component normally distributed
  * No cross-correlation terms
- Critical for understanding PCA transformations

\pagebreak

## 4. Linear Transformations of Random Vectors

### 4.1 Transforming the Iris Dataset
Let's see how linear transformations affect real data:
```python
# Get first two features from iris dataset
X = df[['sepal length (cm)', 'sepal width (cm)']].values

# Define a rotation transformation (45 degrees)
theta = np.pi/4
A = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# Transform data: Y = XA
Y = X @ A  # Each row is transformed random vector
```

### 4.2 Effect on Iris Features
1. Mean Vector Transformation:
   * Before: Mean sepal measurements
   * After: Rotated mean measurements
   * Example:
     ```python
     # Original means
     print("Original means:")
     print("Sepal length mean:", X[:,0].mean())
     print("Sepal width mean:", X[:,1].mean())
     
     # Transformed means
     print("\nRotated means:")
     print("First component mean:", Y[:,0].mean())
     print("Second component mean:", Y[:,1].mean())
     
     # Verify transformation law
     print("\nVerification:")
     print("Direct mean of Y $\\approx$ A @ mean of X:", 
           np.allclose(Y.mean(axis=0), A @ X.mean(axis=0)))
     ```

2. Covariance Structure Changes:
   * Before: Natural sepal length/width correlations
   * After: Rotated correlation structure
   * Example:
     ```python
     # Original covariance
     print("Original covariance:")
     print(pd.DataFrame(
         np.cov(X.T),
         columns=['length', 'width'],
         index=['length', 'width']
     ))
     
     # Transformed covariance
     print("\nRotated covariance:")
     print(pd.DataFrame(
         np.cov(Y.T),
         columns=['comp1', 'comp2'],
         index=['comp1', 'comp2']
     ))
     
     # Verify transformation law
     print("\nVerification:")
     print("Direct cov(Y) $\\approx$ A @ cov(X) @ A.T:", 
           np.allclose(np.cov(Y.T), A @ np.cov(X.T) @ A.T))
     ```

### 4.3 Geometric Understanding
1. Row Space Transformation:
   * Each row (random vector) transformed by $A$
   * Preserves linear relationships between observations
   * Example: Scaling temperature doesn't change patterns

2. Column Space Transformation:
   * Features combined according to $A$
   * Creates new measurement combinations
   * Example: Creating weighted averages of sensors

3. Visualization:
```python
import matplotlib.pyplot as plt

# Plot original vs transformed data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

# Original data
ax1.scatter(X[:,0], X[:,1], alpha=0.5)
ax1.set_title('Original Random Vectors')

# Transformed data
ax2.scatter(Y[:,0], Y[:,1], alpha=0.5)
ax2.set_title('Transformed Random Vectors')

plt.show()
```

### 4.4 Common Transformations in Practice
1. Standardization:
   ```python
   # Center and scale to unit variance
   X_std = (X - X.mean(axis=0)) / X.std(axis=0)
   ```

2. Whitening:
   ```python
   # Transform to uncorrelated variables
   cov = np.cov(X.T)
   L = np.linalg.cholesky(cov)
   X_white = X @ np.linalg.inv(L)
   ```

3. Dimensionality Reduction:
   ```python
   # Project onto first k principal components
   U, S, Vh = np.linalg.svd(X)
   k = 2  # Number of components to keep
   X_reduced = X @ Vh[:k].T
   ```

## Practice Problems

### Problem 1: Covariance Analysis
Given the following temperature and humidity measurements over 5 days:
```python
data = pd.DataFrame({
    'temp': [20.1, 19.8, 20.3, 20.0, 19.9],
    'humidity': [45, 48, 44, 46, 47]
})
```
a) Compute the sample mean vector
b) Calculate the sample covariance matrix
c) Interpret the relationship between temperature and humidity

### Problem 2: Linear Transformations
Consider the random vector $\mathbf{X} = [X_1, X_2]^T$ with:
$$E[\mathbf{X}] = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad 
\text{Cov}(\mathbf{X}) = \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}$$

For the transformation $\mathbf{Y} = A\mathbf{X}$ where:
$$A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$$

a) Find $E[\mathbf{Y}]$
b) Calculate $\text{Cov}(\mathbf{Y})$
c) Verify your results using the transformation laws

### Problem 3: Geometric Understanding
For the iris dataset:
```python
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data[:, [0,1]]  # sepal length and width
```
a) Plot the data points
b) Add the sample mean vector to your plot
c) Draw the 95% confidence ellipse
d) Explain how the ellipse relates to the covariance structure

*Hint: Use the plotting code from section 3.3 as a template*

\pagebreak

## Solutions to Practice Problems

### Solution 1: Covariance Analysis
```python
# a) Sample mean vector
mean_vector = data.mean()
print("Mean vector:")
print(mean_vector)
# temp      20.02
# humidity  46.00

# b) Sample covariance matrix
cov_matrix = data.cov()
print("\nCovariance matrix:")
print(cov_matrix)
# temp      humidity
# temp      0.043   -0.775
# humidity -0.775    2.500

# c) Interpretation:
# - Negative covariance (-0.775) indicates inverse relationship
# - When temperature increases, humidity tends to decrease
# - Humidity has more variance (2.5) than temperature (0.043)
```

### Solution 2: Linear Transformations
a) Expected value of Y:
$$E[\mathbf{Y}] = AE[\mathbf{X}] = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 4 \\ 7 \end{bmatrix}$$

b) Covariance of Y:
$$\text{Cov}(\mathbf{Y}) = A\text{Cov}(\mathbf{X})A^T = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 10 & 7 \\ 7 & 19 \end{bmatrix}$$

c) Verification code:
```python
import numpy as np

# Given values
E_X = np.array([1, 2])
Cov_X = np.array([[4, 2], [2, 5]])
A = np.array([[2, 1], [1, 3]])

# Verify E[Y]
E_Y = A @ E_X
print("E[Y] =", E_Y)  # Should be [4, 7]

# Verify Cov(Y)
Cov_Y = A @ Cov_X @ A.T
print("Cov(Y) =", Cov_Y)  # Should match calculation
```

### Solution 3: Geometric Understanding
```python
import matplotlib.pyplot as plt
from scipy import stats

# a) Plot data points
plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1], alpha=0.5, label='Data points')

# b) Add mean vector
mean = X.mean(axis=0)
plt.scatter(mean[0], mean[1], color='red', s=100, label='Mean')

# c) Add 95% confidence ellipse
cov = np.cov(X.T)
vals, vecs = np.linalg.eigh(cov)
angle = np.degrees(np.arctan2(vecs[1,0], vecs[0,0]))

chi2_val = stats.chi2.ppf(0.95, df=2)
plt.gca().add_patch(plt.matplotlib.patches.Ellipse(
    mean, 2*np.sqrt(chi2_val*vals[0]), 2*np.sqrt(chi2_val*vals[1]),
    angle=angle, fill=False, color='red', 
    label='95% Confidence Region'))

plt.legend()
plt.title('Iris Sepal Measurements with Confidence Ellipse')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.axis('equal')
plt.grid(True)

# d) Explanation:
# - Ellipse orientation shows correlation direction
# - Major axis aligns with direction of maximum variance
# - Minor axis shows direction of minimum variance
# - Size reflects overall spread of the data
# - Center at mean shows typical/expected values
```
