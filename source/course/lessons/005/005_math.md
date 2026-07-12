---
title: "Week 3: Bases, Subspaces, and Linear Transformations"
subtitle: "Comprehensive Coverage of Quiz Topics"
author: "Linear Algebra and Estimation Theory"
date: "Week 3"
---

# Comprehensive Linear Algebra Topics

## 1. Finding and Testing Bases

- A set of basis vectors is a set of vectors that are linearly independent and span the entire space. 
- This means that any vector in the space can be written as a linear combination of the basis vectors.
- e.g. a basis for $\mathbb{R}^2$ is $\{(1,0), (0,1)\}$ because any vector in $\mathbb{R}^2$ can be written as a linear combination of these two vectors.

#### Connection to dimension:

- Theorem: All bases have same number of vectors
- Dimension = number of independent vectors needed to span
- Computing dimensions:
    - Count pivot columns
    - Equals rank of matrix
    - Example: dim(Col A) = rank(A)

\pagebreak

### Systematic Methods for Linear Independence

#### Review: linear independence vs dependence
  
- Vectors $v_1,...,v_n$ are linearly independent if $c_1v_1 + c_2v_2 + ... + c_nv_n = 0$ implies all $c_i = 0$
- Equivalently: no vector can be written as a linear combination of the others
- The only way to get zero is with zero coefficients
  
##### Geometric interpretation:

- In $\mathbb{R}^2$: Two vectors are dependent if they lie on same line through origin
- In $\mathbb{R}^3$: Three vectors are dependent if they lie in same plane
- Generally: Dependent vectors don't "span their full possible dimension"
  
#### Key examples

1. Standard basis vectors are always independent:
    - In $\mathbb{R}^2$: $e_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $e_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$
    - No way to get one from the other

2. Classic dependent vectors:
    - $v_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$, $v_2 = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$
    - $v_2 = 2v_1$ shows dependence

3. Three vectors in $\mathbb{R}^2$ are always dependent:
    - Example: $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$, $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$
    - Third vector is sum of first two
  
#### Common misconceptions:

1. "Parallel vectors are independent" (They're dependent!)
2. "Different-looking vectors are independent" (Not necessarily!)
3. "Zero vector can be part of independent set" (Never!)

\pagebreak

### Row Reduction Method and Row Echelon Form

The row reduction method systematically converts a matrix to row echelon form to test linear independence.

#### Row Echelon Form Properties

A matrix is in row echelon form when:

1. All zero rows are at the bottom
2. Leading entry (pivot) of each nonzero row is to the right of pivots above
3. All entries below a pivot are zero

e.g. 

$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
0 & 1 & -1 & 2 \\
0 & 0 & 1 & 5
\end{bmatrix}
$$

\pagebreak

#### Algorithm for Row Reduction

1. Input: Matrix $A$ with vectors as columns
2. For each column j from left to right:
    a. Find pivot: First nonzero entry in column j
    b. If no pivot exists:
        a. Mark column j as free variable column
        b. Continue to next column
    c. If pivot found:
        a. Divide pivot row by pivot element (make pivot = 1)
        b. For each row i below:
        c. Subtract multiple of pivot row to make entry (i,j) zero
3. Count nonzero rows r in result
4. For each free variable column k:
    a. Set $x_k = t$ where $t \in \mathbb{R}$
    b. Express pivot variables in terms of free variables
    c. Each choice of parameters gives nullspace vector
5. Output: 
    a. Rank = r (number of nonzero rows)
    b. Pivot columns form basis
    c. Free variables give nullspace basis
    d. General solution: $x = x_p + \sum t_k n_k$ where:
        a. $x_p$ is particular solution
        b. $n_k$ are nullspace basis vectors

\pagebreak

##### Example 1: $\begin{bmatrix} 2 & 4 & 6 \\ 1 & 2 & 3 \end{bmatrix}$

Following the algorithm:

1. Input matrix has dimensions $2 \times 3$
2. Column 1 (j=1):
   - Pivot found: $a_{11} = 2$
   - Make pivot 1: Multiply $R_1$ by 0.5
   - Clear below: $R_2 - \frac{1}{2}R_1$
   $\begin{bmatrix} 2 & 4 & 6 \\ 1 & 2 & 3 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{bmatrix}$
3. Column 2 (j=2):
   - No nonzero entries remain
   - Mark $x_2$ as free variable
4. Column 3 (j=3):
   - No nonzero entries remain
   - Mark $x_3$ as free variable
5. Output:
   - Rank = 1 (one nonzero row)
   - Pivot column: $\begin{bmatrix} 2 \\ 1 \end{bmatrix}$
   - Free variables: $x_2, x_3$
   - General solution: $x_1 = -2x_2 - 3x_3$
   - Nullspace basis vectors: (-2, 1, 0) and (-3, 0, 1)

\pagebreak

##### Example 2: $\begin{bmatrix} 1 & 2 & 2 & 3 \\ 2 & 4 & 5 & 8 \\ 3 & 6 & 7 & 11 \end{bmatrix}$

Following the algorithm:

1. Input matrix has dimensions 3 x 4
2. Column 1 (j=1):
   - Pivot found: $a_{11} = 1$
   - Make pivot 1: Already is
   - Clear below using $R_2 - 2R_1$ and $R_3 - 3R_1$:
   $\begin{bmatrix} 1 & 2 & 2 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 2 \end{bmatrix}$
3. Column 2 (j=2):
   - No nonzero entries after clearing
   - Mark $x_2$ as free variable
4. Column 3 (j=3):
   - Pivot found in $R_2$: $a_{23} = 1$
   - Make pivot 1: Already is
   - Clear below using $R_3 - R_2$:
   $\begin{bmatrix} 1 & 2 & 2 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
5. Column 4 (j=4):
   - No more rows to use as pivots
   - Mark $x_4$ as free variable
6. Output:
   - Rank = 2 (two nonzero rows)
   - Pivot columns: columns 1 and 3
   - Free variables: $x_2, x_4$
   - General solution: 
     * $x_1 = -2x_2 - 2x_3 - 3x_4$
     * $x_3 = -2x_4$
   - Nullspace basis vectors: (-2, 1, 0, 0) and (-3, 0, -2, 1)

\pagebreak

##### Example 3: $\begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$

Following the algorithm:

1. Input matrix has dimensions 3×3
2. Column 1 (j=1):
   - Pivot found: $a_{11} = 1$
   - Make pivot 1: Already is
   - Clear below:
   $\begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 1 & 1 \end{bmatrix}$
3. Column 2 (j=2):
   - Pivot found: $a_{22} = -1$
   - Make pivot 1: Multiply $R_2$ by -1
   - Clear below:
   $\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & -1 \\ 0 & 1 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 2 \end{bmatrix}$
4. Column 3 (j=3):
   - Pivot found: $a_{33} = 2$
   - Make pivot 1: Multiply $R_3$ by 1/2
5. Output:
   - Rank = 3 (three nonzero rows)
   - All columns are pivot columns
   - No free variables
   - Unique solution: $x = 0$
   - Nullspace is trivial


#### Additional Notes

##### Gram-Schmidt Process

- a process for orthogonalizing a set of vectors
- with Gram-Schmidt, we can find an orthogonal basis for a subspace

\pagebreak

## 2. Finding Vectors in Subspaces

### Column Space Methods

#### Definition and Properties

1. Column space Col($A$) = all vectors $b$ such that $Ax = b$ has a solution
2. Geometrically: all possible combinations of columns
3. Key fact: Col($A$) = span of columns of $A$

#### Algorithm for finding Col($A$) basis

1. Form matrix $A$ with given vectors as columns
2. Reduce $A$ to row echelon form using row operations
3. Find pivot columns in original $A$
4. These pivot columns form a basis for Col($A$)

#### Example: 

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$

1. Matrix already formed
2. Row reduce:
    $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{bmatrix}$
  3. First column is pivot column
  4. Basis is $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$

#### Computing dimension

- dim(Col($A$)) = rank($A$) = number of pivot columns
- For this example: dim(Col($A$)) = 1
- Explains why not all vectors in $\mathbb{R}^2$ are reachable

\pagebreak
### Nullspace Methods

#### Definition and Properties

1. Nullspace $N(A)$ = all solutions to $Ax = 0$
2. Geometrically: vectors that $A$ maps to zero
3. Key fact: $N(A)$ is a subspace

#### Algorithm for finding $N(A)$ basis

1. Row reduce $A$ to echelon form
2. Identify free variables (non-pivot columns)
3. For each free variable:
    a. Set it to 1 and others to 0
    b. Solve for pivot variables
    c. This gives one basis vector
4. Collect all such vectors to form basis

#### Example

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$

1. Row reduce:
    $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{bmatrix}$
  * Step 2: $x_2$ and $x_3$ are free
  * Step 3: 
    - Let $x_2=1, x_3=0$: gives $(-2, 1, 0)$
    - Let $x_2=0, x_3=1$: gives $(-3, 0, 1)$
  * Step 4: Basis is $\{(-2, 1, 0), (-3, 0, 1)\}$

#### Computing dimension

- dim($N(A)$) = number of free variables
- For this example: dim($N(A)$) = 2
- Explains why not all vectors in $\mathbb{R}^3$ are in $N(A)$

\pagebreak

### Row Space Methods

#### Definition and Properties

1. The row space of $A$ is the column space of $A^T$
2. Key fact: Row($A$) is subspace of $\mathbb{R}^n$ where $n$ = number of columns
3. dim(Row($A$)) = rank($A$)

#### Algorithm for finding Row($A$) basis

1. Row reduce $A$ to echelon form
2. Keep nonzero rows from reduced matrix
3. These rows form a basis for Row($A$)

Note: Original rows of $A$ span Row($A$) but may not be independent

Row operations preserve Row($A$) but change spanning set to basis

#### Example: 

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$

1. Row reduce:
    $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{bmatrix}$
  * Step 2: One nonzero row: $(1, 2, 3)$
  * Step 3: Basis is $\{(1, 2, 3)\}$

#### Connection to previous results:

- dim(Row($A$)) = dim(Col($A$)) = rank($A$) = 1
- Row space is in $\mathbb{R}^3$ (3 columns in $A$)
- Compare: Col($A$) was in $\mathbb{R}^2$ (2 rows in $A$)

#### Practical significance:

- Row space shows which linear combinations of coordinates are possible
- Rank = number of independent equations in system
- Essential for understanding solution spaces

\pagebreak

## 3. Row Space/Nullspace Decomposition

### Orthogonality Properties
- Fundamental Orthogonality Theorem:
  * Row space $\perp$ nullspace
  * Column space $\perp$ left nullspace
  * These relationships are fundamental to matrix theory

- Geometric Interpretation:
  * Example: $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$
  * Row space vector: $r = [1 \; 2 \; 3]$
  * Nullspace vector: $x = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}$
  * Verify orthogonality:
    - $r \cdot x = -2(1) + 1(2) + 0(3) = 0$
    - Geometric visualization:
    \begin{tikzpicture}[scale=0.8]
    \draw[->] (-3,0) -- (4,0) node[right] {$x$};
    \draw[->] (0,-1) -- (0,3) node[above] {$y$};
    \draw[thick,blue,->] (0,0) -- (1,2) node[midway,above] {$r$};
    \draw[thick,red,->] (0,0) -- (-2,1) node[midway,left] {$x$};
    \draw[dashed] (1,2) -- (1.5,1.75);
    \draw[dashed] (-2,1) -- (-1.5,1.25);
    \draw (0.3,0.6) node[right] {$90°$};
    \draw (0.2,0.4) arc (63.43:-26.57:0.5);
    \end{tikzpicture}

- Practical Importance:
  * Helps decompose solutions to $Ax = b$
  * Essential for least squares problems
  * Key to understanding projection matrices
  * Basis for SVD and eigenvalue decomposition

\pagebreak

#### Procedure: Project a vector onto another vector

1. Given vectors $v$ and $w$, to project $v$ onto $w$:
   * Formula: $proj_w v = \frac{v \cdot w}{w \cdot w}w$
   * This gives the component of $v$ in direction of $w$

2. Geometric interpretation:
   * Result is parallel to $w$
   * Length is $\|v\|\cos\theta$ where $\theta$ is angle between vectors
   * Perpendicular component is $v - proj_w v$

   \begin{tikzpicture}[scale=1.2]
   \draw[->] (-1,0) -- (4,0) node[right] {$x$};
   \draw[->] (0,-1) -- (0,3) node[above] {$y$};
   
   % Original vector v
   \draw[thick,blue,->] (0,0) -- (1.5,2) node[midway,above] {$v$};
   
   % Vector to project onto (w)
   \draw[thick,red,->] (0,0) -- (3,3) node[midway,right] {$w$};
   
   % Projection vector
   \draw[thick,green,dashed,->] (0,0) -- (1.75,1.75) node[below right] {$proj_w v$};

   % Perpendicular component
   \draw[thick,purple,dashed,->] (1.75,1.75) -- (1.5, 2) node[midway,above] {$v - proj_w v$};
   
   % Angle marking
   \draw (0.5,0) arc (0:45:0.5);
   \node at (0.7,0.3) {$\theta$};
   \end{tikzpicture}

3. Example:
   * Let $v = \begin{bmatrix} 1.5 \\ 2 \end{bmatrix}$, $w = \begin{bmatrix} 3 \\ 3 \end{bmatrix}$
   * $proj_w v = \frac{(1.5)(3) + (2)(3)}{(3)^2 + (3)^2}\begin{bmatrix} 3 \\ 3 \end{bmatrix}$
   * $= \frac{10.5}{18}\begin{bmatrix} 3 \\ 3 \end{bmatrix} = \begin{bmatrix} 1.75 \\ 1.75 \end{bmatrix}$
   * Perpendicular component: $\begin{bmatrix} 1.5 - 1.75 \\ 2 - 1.75 \end{bmatrix} = \begin{bmatrix} -0.25 \\ 0.25 \end{bmatrix}$

\pagebreak

### Vector Decomposition

#### Fundamental Decomposition Theorem:

* Any vector $x$ uniquely decomposes as $x = x_r + x_n$ where:
  - $x_r$ is in row space Row($A$)
  - $x_n$ is in nullspace $N(A)$
  - $x_r \perp x_n$ (orthogonal components)

#### Example: 

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$

Given vector $x = (1, 2, 1)$

1. Find row space basis $r = (1, 2, 3)$
2. Find nullspace basis vectors:
    - $n_1 = (-2, 1, 0)$
    - $n_2 = (-3, 0, 1)$
3. Project $x$ onto row space:
    - $x_r = \frac{(x \cdot r)}{(r \cdot r)}r$
    - $x_r = \frac{(1(1) + 2(2) + 1(3))}{(1^2 + 2^2 + 3^2)}[1 \; 2 \; 3]$
    - $x_r = (0.5, 1, 1.5)$
4. Find nullspace component:
    - $x_n = x - x_r$
    - $x_n = (0.5, 1, -0.5)$

- Verification:
  * Check $x_r$ is in row space: *Is it a multiple of $(1, 2, 3)$?* Yes
  * Check $x_n$ is in nullspace: *$Ax_n = 0$?* Yes
  * Check orthogonality: *$x_r \cdot x_n = 0$?* Yes
  * Check sum: *$x_r + x_n = x$?* Yes

- Applications:
  * Understanding solution structure
  * Projection matrices
  * Least squares problems
  * Signal processing decompositions

### Connection to Linear Transformations

#### Motivation: From Decomposition to Transformation

The vector decomposition $x = x_r + x_n$ reveals a fundamental principle:
- Every vector splits into two perpendicular parts
- One part (row space) carries all the "useful" information
- One part (nullspace) disappears under the transformation

This leads naturally to the question:
- What happens to vectors under matrix operations?
- How do these operations transform space?
- What patterns and properties emerge?

#### The Bridge: How Decomposition Shapes Transformation

1. Effect on Components:
   * For any linear transformation $T$ represented by matrix $A$:
   * $T(x) = T(x_r + x_n) = T(x_r) + T(x_n)$ by linearity
   * But $T(x_n) = Ax_n = 0$ since $x_n$ is in nullspace
   * Therefore $T(x) = T(x_r)$ - only row space component matters!

2. Geometric Interpretation:
   * Row space vectors: transformed meaningfully by $A$
   * Nullspace vectors: collapsed to zero
   * Any vector: decomposed then transformed

3. Detailed Example: For $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$
   * Let $x = (1,1,1)$
   * Row component: $x_r = (0.5,1,1.5)$
   * Null component: $x_n = (0.5,0,-0.5)$
   * Step by step:
     - First decompose: $x = x_r + x_n$
     - Then transform: $Ax = A(x_r + x_n) = Ax_r + Ax_n = Ax_r$
     - Nullspace component vanishes: $Ax_n = 0$
   * This pattern holds for all vectors!

#### Key Insights Leading to Linear Transformations

1. Matrix Operations as Functions:
   * Every matrix defines a transformation
   * Input: vector $x$
   * Output: transformed vector $Ax$
   * Process: decompose → transform → combine

2. Fundamental Properties Emerging:
   * Linearity preserves combinations
   * Nullspace determines "invisible" directions
   * Row space determines "visible" directions
   * Rank tells us transformation dimension

3. Critical Questions to Address:
   * How do we describe these transformations?
   * What properties do they preserve?
   * When are they invertible?
   * How do they compose?

This understanding leads us naturally to study linear transformations in detail...

\pagebreak

## 4. Linear Transformations

### Fundamental Properties

#### Linear Transformation Definition:

* A function $T: V \rightarrow W$ between vector spaces
* Must satisfy two key properties:
  * Homogeneity: $T(cx) = cT(x)$ for all scalars $c$
  * Additivity: $T(x + y) = T(x) + T(y)$ for all vectors $x,y$

#### Homogeneity Property:

* Formal definition: $T(cx) = cT(x)$ for all $c \in \mathbb{R}$
* Geometric meaning: Scaling input scales output proportionally

- Let $v=(v_x,v_y)$ and scalar $c$:
  * $T(cv) = T(cv_x,cv_y)$
  * $= (2(cv_x)-(cv_y), (cv_x)+(cv_y))$
  * $= (c(2v_x)-cv_y, cv_x+cv_y)$
  * $= c(2v_x-v_y, v_x+v_y)$
  * $= cT(v)$
- Therefore $T(cv) = cT(v)$ for any vector $v$ and scalar $c$

#### Additivity Property:

* Formal definition: $T(x + y) = T(x) + T(y)$ for all $x,y$
* Geometric meaning: Transform of sum equals sum of transforms

##### Example verification

$$T(x,y) = (2x-y, x+y)$$

- Let $v=(v_x,v_y)$ and $w=(w_x,w_y)$:
  * $T(v+w) = T(v_x+w_x,v_y+w_y) = (2(v_x+w_x)-(v_y+w_y), (v_x+w_x)+(v_y+w_y))$
  * $T(v) + T(w) = (2v_x-v_y, v_x+v_y) + (2w_x-w_y, w_x+w_y)$
  * $= (2v_x-v_y+2w_x-w_y, v_x+v_y+w_x+w_y)$
  * $= (2(v_x+w_x)-(v_y+w_y), (v_x+w_x)+(v_y+w_y))$
- Therefore $T(v+w) = T(v) + T(w)$ for any vectors $v$ and $w$

### Matrix Representation

#### Converting Function to Matrix Form:

##### Example: $T(x,y) = (2x-y, x+y)$

- Method: Apply $T$ to standard basis vectors $(1,0)$ and $(0,1)$
  * $T(1,0) = (2,1)$ gives first column
  * $T(0,1) = (-1,1)$ gives second column
- Matrix form: $A = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$
- Verification: $A\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x-y \\ x+y \end{bmatrix}$

#### Properties of Matrix Representation:

- Uniqueness: Each linear transformation has unique matrix
- Composition: $(ST)(x) = S(T(x))$ corresponds to matrix product
  * Invertibility: $T$ invertible iff matrix $A$ invertible
  * Example: For our matrix $A$:
    - det($A$) = $2(1) - (-1)(1) = 3 \neq 0$
    - Therefore $T$ is invertible

#### Computing Transformations:

##### Example 1: Rotation by 90° counterclockwise

- Matrix: $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$
- Input $v = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$
    - $T(v) = A\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$
    - Verify: rotates vector 90° counterclockwise

##### Example 2: Scaling and shear

- Matrix: $A = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}$
- Input $v = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$
- $T(v) = A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}$
    - Geometric effect: scales x by 2, y by 3, adds shear

##### Example 3: Projection onto x-axis

- Matrix: $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$
- Input $v = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$
- $T(v) = A\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}$
- Geometric effect: projects onto x-axis
- Verify linearity:
  * Homogeneity: $T(2v) = 2T(v)$
  * Additivity: $T(v+w) = T(v) + T(w)$

#### Geometric Interpretation:

- Columns show where basis vectors go
- Linear combination preserved
- Matrix multiplication = composition
- Determinant = area/volume scaling

## Additional Resources
- Strang Chapters 2.5, 2.6, 3.1, 3.2
- [MIT OCW 18.06 Lecture 9](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/)
- [3Blue1Brown Linear Transformations](https://www.3blue1brown.com/lessons/linear-transformations)
