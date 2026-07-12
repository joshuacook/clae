---
title: "Week 3: Bases, Subspaces, and Linear Transformations Lab"
subtitle: "Practice Problems and Implementations"
---

# Practice Problems: Bases, Subspaces, and Linear Transformations

## Part 1: Finding and Testing Bases (Paper Problems)

1. For the following vectors, determine if they form a basis for $\mathbb{R}^3$:
   $$v_1 = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}, 
   v_2 = \begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}, 
   v_3 = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}$$
   Show all steps of your work.

2. Find a basis for the subspace spanned by:
   $$\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, 
   \begin{bmatrix} 2 \\ 2 \\ 0 \end{bmatrix}, 
   \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$$

3. For the matrix:
   $$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 9 & 12 \end{bmatrix}$$
   Find bases for:
   a) The column space
   b) The row space
   c) The nullspace

## Part 2: Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

def is_independent(vectors):
    """
    Test if vectors are linearly independent
    Return: bool, True if independent
    """
    # Your implementation here
    pass

def find_col_space_basis(A):
    """
    Find a basis for the column space of A
    Return: numpy array with basis vectors as columns
    """
    # Your implementation here
    pass

def find_null_space_basis(A):
    """
    Find a basis for the nullspace of A
    Return: numpy array with basis vectors as columns
    """
    # Your implementation here
    pass

# Test your functions
A = np.array([[1, 2, 3], 
              [2, 4, 6]])

print("Testing independence:")
vectors = [np.array([1, 0]), np.array([0, 1])]
print(is_independent(vectors))

print("\nFinding column space basis:")
col_basis = find_col_space_basis(A)
print(col_basis)

print("\nFinding nullspace basis:")
null_basis = find_null_space_basis(A)
print(null_basis)
```

## Part 3: Vector Decomposition (Paper Problems)

1. For the matrix:
   $$A = \begin{bmatrix} 1 & -1 & 2 \\ -1 & 1 & -2 \end{bmatrix}$$
   Decompose the vector $x = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ into:
   a) Its row space component
   b) Its nullspace component
   Show all steps.

2. Verify that your decomposition is correct by checking:
   a) The components sum to $x$
   b) The components are orthogonal
   c) The row space component is in Row($A$)
   d) The nullspace component is in $N(A)$

## Part 4: Linear Transformations

1. For the transformation $T(x,y) = (3x-y, x+2y)$:
   a) Find its matrix representation
   b) Verify it's linear by checking homogeneity and additivity
   c) Is it invertible? Why or why not?

2. Consider the matrix:
   $$A = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$$
   For the vector $v = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$:
   a) Compute $Av$ directly
   b) Decompose $v$ into row and nullspace components
   c) Show that $Av = A(v_r)$

## Python Implementation: Linear Transformations

```python
def plot_transformation(A, points=None):
    """
    Visualize a 2D linear transformation
    A: 2x2 transformation matrix
    points: optional set of points to transform
    """
    if points is None:
        x = np.linspace(-2, 2, 5)
        y = np.linspace(-2, 2, 5)
        X, Y = np.meshgrid(x, y)
        points = np.column_stack((X.ravel(), Y.ravel()))
    
    transformed = points @ A.T
    
    plt.figure(figsize=(12, 5))
    
    # Original points
    plt.subplot(121)
    plt.scatter(points[:, 0], points[:, 1], c='blue', label='Original')
    plt.grid(True)
    plt.axis('equal')
    plt.title('Original Space')
    
    # Transformed points
    plt.subplot(122)
    plt.scatter(transformed[:, 0], transformed[:, 1], c='red', label='Transformed')
    plt.grid(True)
    plt.axis('equal')
    plt.title('Transformed Space')
    
    plt.tight_layout()
    plt.show()

# Example usage
A = np.array([[2, -1],
              [1, 1]])
plot_transformation(A)
```

## Additional Exercises

1. Implement a function to decompose a vector into its row space and nullspace components.

2. Create a visualization showing how a linear transformation affects:
   a) Vectors in the row space
   b) Vectors in the nullspace
   c) General vectors

3. For the transformation $T(x,y) = (2x+y, x-y)$:
   a) Write a program to verify linearity
   b) Visualize its effect on the unit square
   c) Find its kernel (nullspace) computationally

Solutions will be provided in the next session.

\pagebreak

# Solutions

## Part 1: Finding and Testing Bases

### Problem 1
To determine if vectors form a basis for $\mathbb{R}^3$:
1. Check independence: Form matrix and row reduce
   $$\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 2 & -1 & 3 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$
   Not independent (rank = 2 < 3)

### Problem 2
1. Form matrix with vectors as columns:
   $$\begin{bmatrix} 1 & 2 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 1 \end{bmatrix}$$
2. Row reduce:
   $$\rightarrow \begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$
3. Basis vectors: $\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$

### Problem 3
For matrix $A$:
1. Column space basis: $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ (first column)
2. Row space basis: $(1, 2, 3, 4)$ (first row)
3. Nullspace basis: $\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} -3 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -4 \\ 0 \\ 0 \\ 1 \end{bmatrix}$

## Part 2: Python Implementation Solutions

```python
def is_independent(vectors):
    """Test if vectors are linearly independent"""
    matrix = np.column_stack(vectors)
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)

def find_col_space_basis(A):
    """Find a basis for the column space of A"""
    # Get rank and pivot columns
    rank = np.linalg.matrix_rank(A)
    _, _, Vh = np.linalg.svd(A)
    pivot_cols = A[:, :rank]
    return pivot_cols

def find_null_space_basis(A):
    """Find a basis for the nullspace of A"""
    _, _, Vh = np.linalg.svd(A)
    rank = np.linalg.matrix_rank(A)
    null_space = Vh[rank:].T
    return null_space
```

## Part 3: Vector Decomposition Solutions

### Problem 1
For matrix $A$ and vector $x$:

1. Row space component:
   - Project $x$ onto row space vector $r = (1,-1,2)$
   - $x_r = \frac{x \cdot r}{r \cdot r}r = \frac{2}{6}(1,-1,2) = (\frac{1}{3},-\frac{1}{3},\frac{2}{3})$

2. Nullspace component:
   - $x_n = x - x_r = (\frac{2}{3},\frac{4}{3},\frac{1}{3})$

### Problem 2
Verification:
a) $x_r + x_n = (1,1,1)$ (verified)
b) $x_r \cdot x_n = 0$ (verified)
c) $x_r$ is multiple of row vector (verified)
d) $Ax_n = 0$ (verified)

## Part 4: Linear Transformations Solutions

### Problem 1
For $T(x,y) = (3x-y, x+2y)$:

a) Matrix representation:
   $$A = \begin{bmatrix} 3 & -1 \\ 1 & 2 \end{bmatrix}$$

b) Linearity verification:
   - Homogeneity: $T(cx,cy) = (3cx-cy, cx+2cy) = c(3x-y, x+2y) = cT(x,y)$
   - Additivity: $T(x_1+x_2,y_1+y_2) = T(x_1,y_1) + T(x_2,y_2)$

c) Invertible because det$(A) = 7 \neq 0$

### Problem 2
For matrix $A$ and vector $v$:

a) Direct computation:
   $$Av = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$$

b) Decomposition:
   - Row space component: $v_r = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ (already in row space)
   - Nullspace component: $v_n = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

c) Verification: $Av = Av_r$ since $v = v_r$

## Additional Exercises Solutions

### Exercise 1: Vector Decomposition Function
```python
def decompose_vector(A, x):
    """Decompose vector into row space and nullspace components"""
    # Get row space basis
    U, s, Vh = np.linalg.svd(A)
    rank = np.linalg.matrix_rank(A)
    row_space_basis = Vh[:rank].T
    
    # Project onto row space
    proj_matrix = row_space_basis @ np.linalg.pinv(row_space_basis)
    x_r = proj_matrix @ x
    x_n = x - x_r
    
    return x_r, x_n
```

```python
```python
def visualize_transformation_components(A):
    """Visualize how transformation affects different components"""
    # Generate grid of points
    x = np.linspace(-2, 2, 5)
    y = np.linspace(-2, 2, 5)
    X, Y = np.meshgrid(x, y)
    points = np.column_stack((X.ravel(), Y.ravel()))
    
    # Decompose each point
    row_comps = []
    null_comps = []
    for p in points:
        r, n = decompose_vector(A, p)
        row_comps.append(r)
        null_comps.append(n)
    
    row_comps = np.array(row_comps)
    null_comps = np.array(null_comps)
    
    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    
    # Original space
    axes[0,0].scatter(points[:,0], points[:,1], c='blue')
    axes[0,0].set_title('Original Points')
    
    # Row space components
    axes[0,1].scatter(row_comps[:,0], row_comps[:,1], c='red')
    axes[0,1].set_title('Row Space Components')
    
    # Null space components
    axes[1,0].scatter(null_comps[:,0], null_comps[:,1], c='green')
    axes[1,0].set_title('Null Space Components')
    
    # Transformed points
    transformed = points @ A.T
    axes[1,1].scatter(transformed[:,0], transformed[:,1], c='purple')
    axes[1,1].set_title('Transformed Points')
    
    for ax in axes.flat:
        ax.grid(True)
        ax.axis('equal')
    
    plt.tight_layout()
    plt.show()
```

### Exercise 3: Linearity Verification
```python
def verify_linearity(T_matrix):
    """Verify linearity properties of transformation"""
    # Test vectors
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    c = 2.5
    
    # Test homogeneity
    Tv1 = T_matrix @ v1
    cTv1 = c * Tv1
    Tcv1 = T_matrix @ (c * v1)
    homog_ok = np.allclose(cTv1, Tcv1)
    
    # Test additivity
    Tv1_plus_Tv2 = Tv1 + (T_matrix @ v2)
    T_v1_plus_v2 = T_matrix @ (v1 + v2)
    add_ok = np.allclose(Tv1_plus_Tv2, T_v1_plus_v2)
    
    print(f"Homogeneity satisfied: {homog_ok}")
    print(f"Additivity satisfied: {add_ok}")
    
    return homog_ok and add_ok

# Test the transformation T(x,y) = (2x+y, x-y)
T = np.array([[2, 1], [1, -1]])
verify_linearity(T)

# Find nullspace
null_basis = find_null_space_basis(T)
print("\\nNullspace basis:")
print(null_basis)
```
```
