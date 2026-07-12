# Linear Transformations and Their Applications

## System Types and Their Properties

### Underdetermined Systems (p > n)
- More features than observations (p > n)
- Multiple solutions typically exist
- Freedom in solution space
- Example system:
  $$
  \begin{aligned}
  x_1 + x_2 + x_3 + x_4 + x_5 &= 1 \quad \text{[two equations]} \\
  2x_1 - x_2 + x_3 - x_4 + x_5 &= 2 \quad \text{[five unknowns]}
  \end{aligned}
  $$
  Matrix form:
  $$
  \begin{bmatrix} 
  1 & 1 & 1 & 1 & 1 \\
  2 & -1 & 1 & -1 & 1
  \end{bmatrix}
  \begin{bmatrix}
  x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5
  \end{bmatrix} = 
  \begin{bmatrix}
  1 \\ 2
  \end{bmatrix}
  $$
  Has infinitely many solutions
- Real-world examples:
  * High-dimensional data with few samples
  * Image reconstruction from partial data
  * Gene expression with few patients
  * Feature selection problems
- Key characteristic: Need regularization to choose "best" solution
- Common in modern machine learning with p >> n
- **In this class**, we will work with the principal component analysis in term of underdetermined systems

\pagebreak

### Overdetermined Systems (n > p)
- More observations than features (n > p)
- Usually no exact solution exists
- Focus on minimizing errors
- Example system:
  $$
  \begin{aligned}
  x_1 + x_2 &= 1.0 \quad \text{[five equations]} \\
  x_1 - x_2 &= 0.5 \quad \text{[two unknowns]} \\
  2x_1 + x_2 &= 2.5 \\
  x_1 + 2x_2 &= 2.0 \\
  x_1 + x_2 &= 1.5
  \end{aligned}
  $$
  Matrix form:
  $$
  \begin{bmatrix}
  1 & 1 \\
  1 & -1 \\
  2 & 1 \\
  1 & 2 \\
  1 & 1
  \end{bmatrix}
  \begin{bmatrix}
  x_1 \\ x_2
  \end{bmatrix} =
  \begin{bmatrix}
  1.0 \\ 0.5 \\ 2.5 \\ 2.0 \\ 1.5
  \end{bmatrix}
  $$
  Usually has no exact solution
- Real-world examples:
  * Traditional statistical regression
  * Sensor measurements over time
  * Experimental data fitting
  * Customer behavior prediction
- Key characteristic: Need error minimization strategy (e.g., least squares)
- Classical statistical setting with n >> p
- **In this class**, we will work with the least squares in term of overdetermined systems


\pagebreak

## Key Insights from Previous Lesson

### Role of Subspaces in Different Systems

In both cases, $A$ represents the dataset of observations.

#### In Overdetermined Systems (n > p) - Least Squares Setting

1. Column Space
   - Represents all possible outputs $Ax$ for any input $x$
   - Often $b$ is not in column space (no exact solution exists)
   - In least squares: projection of $b$ onto column space gives best fit

2. Row Space
   - Determines system consistency
   - Rank equals column space dimension
   - In least squares: determines which parameters can be estimated

3. Null Space
   - Solutions to $Ax = 0$
   - Usually smaller dimension
   - In least squares: represents unidentifiable parameter combinations

4. Left Null Space
   - Solutions to $A^Ty = 0$
   - Critical for least squares problems
   - In least squares: represents residual directions

#### In Underdetermined Systems (p > n) - PCA Setting

1. Column Space
   - Smaller dimension than input space
   - In PCA: represents all possible outputs $Ax$ in reduced dimension
   - Solutions form lower-dimensional subspaces

2. Row Space
   - Determines which components of solution are fixed
   - In PCA: represents principal component directions
   - Each component captures maximum remaining variance

3. Null Space
   - Large dimension (p - n)
   - In PCA: represents directions of zero variance
   - Key for dimensionality reduction and noise removal

4. Left Null Space
   - Usually trivial or small
   - In PCA: represents discarded dimensions
   - Used for reconstruction error analysis

### Important Applications

1. Null Space Applications:
   - Signal Processing: PCA noise components
   - Control Systems: Zero-output inputs
   - Structural Engineering: Zero-deformation modes

2. Left Null Space Applications:
   - Least Squares: Error analysis
   - Signal Processing: Reconstruction errors
   - Model Fitting: Residual analysis

### Connection to Subspaces and Machine Learning

#### The Four Fundamental Subspaces in Machine Learning

1. Column Space: Model's Prediction Space
   - Represents all possible predictions our model can make
   - In regression: all possible combinations of our features
   - If target y is not in column space, perfect prediction impossible
   - Explains why some patterns can't be captured by our model

2. Null Space: Feature Redundancy
   - Shows which feature combinations are redundant
   - Important for feature selection and multicollinearity
   - In high-dimensional data: helps identify unnecessary features
   - Guides regularization by showing what can be simplified

3. Left Null Space: Error Structure
   - Contains the unavoidable prediction errors
   - Shows patterns our model can never capture
   - In regression: represents systematic prediction errors
   - Helps assess model limitations and bias

4. Row Space: Estimable Parameters
   - Shows which parameter combinations we can actually estimate
   - Crucial for understanding model identifiability
   - In regression: what feature effects can be separated
   - Guides feature engineering and model design

#### Connection to System Types

- Null Space corresponds to Underdetermined Systems
  * Multiple solutions differ by nullspace vectors
  * Each solution adds freedom in nullspace directions
  * Important for finding minimal norm solutions

- Left Null Space corresponds to Overdetermined Systems
  * Represents unavoidable errors
  * Helps analyze accuracy of approximate solutions
  * Critical for understanding residuals

