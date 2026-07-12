---
title: "The Four Fundamental Subspaces Lab"
subtitle: "Lesson 4.1: Applications in Machine Learning"
---

# Lab Exercises: The Four Fundamental Subspaces

## Part 1: Review of Fundamental Theorem in 2D

Let's visualize the four fundamental subspaces using Python:

```python
import numpy as np
from numpy.linalg import svd, matrix_rank
import matplotlib.pyplot as plt

def plot_vector(v, color='b', label=None):
    """Plot a 2D vector from origin"""
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color)
    if label:
        plt.text(v[0]*1.1, v[1]*1.1, label)

def explore_and_plot_subspaces(A):
    """Analyze and visualize the four fundamental subspaces of a 2D matrix A"""
    m, n = A.shape
    rank = matrix_rank(A)
    
    # Get SVD components
    U, s, Vh = svd(A)
    
    # Column space basis (first r columns of U)
    col_space = U[:, :rank]
    
    # Row space basis (first r rows of Vh)
    row_space = Vh[:rank, :].T
    
    # Nullspace basis (last n-r rows of Vh)
    null_space = Vh[rank:, :].T
    
    # Left nullspace basis (last m-r columns of U)
    left_null = U[:, rank:]
    
    print(f"Matrix dimensions: {m}x{n}")
    print(f"Rank: {rank}")
    print(f"\nDimensions:")
    print(f"Column space: {rank}")
    print(f"Row space: {rank}")
    print(f"Nullspace: {n - rank}")
    print(f"Left nullspace: {m - rank}")
    
    # Plot the subspaces
    plt.figure(figsize=(16, 4))
    
    # Plot original matrix columns
    plt.subplot(141)
    plt.title("Matrix Columns and Column Space")
    for i in range(n):
        plot_vector(A[:, i], 'b', f'col {i+1}')
    for i in range(col_space.shape[1]):
        plot_vector(col_space[:, i], 'r', f'basis {i+1}')
    plt.grid(True)
    plt.axis('equal')
    
    # Plot row space
    plt.subplot(142)
    plt.title("Row Space")
    for i in range(row_space.shape[1]):
        plot_vector(row_space[:, i], 'g', f'row {i+1}')
    plt.grid(True)
    plt.axis('equal')
    
    # Plot nullspace
    plt.subplot(143)
    plt.title("Nullspace")
    if null_space.size > 0:
        for i in range(null_space.shape[1]):
            plot_vector(null_space[:, i], 'purple', f'null {i+1}')
    plt.grid(True)
    plt.axis('equal')
    
    # Plot left nullspace
    plt.subplot(144)
    plt.title("Left Nullspace")
    if left_null.size > 0:
        for i in range(left_null.shape[1]):
            plot_vector(left_null[:, i], 'orange', f'left null {i+1}')
    plt.grid(True)
    plt.axis('equal')
    
    plt.tight_layout()
    plt.show()
    
    return col_space, row_space, null_space, left_null

# Example 2D matrices
A1 = np.array([[1, 0],
               [1, 1]])  # Full rank

A2 = np.array([[1, 1],
               [2, 2]])  # Rank 1

print("Full rank matrix:")
col_space1, row_space1, null_space1, left_null1 = explore_and_plot_subspaces(A1)

print("\nRank deficient matrix:")
col_space2, row_space2, null_space2, left_null2 = explore_and_plot_subspaces(A2)
```

## Part 2: Applications in Machine Learning

## Part 2: Machine Learning Applications

### Example 1: Underdetermined System (PCA Setting)

```python
# Create an underdetermined system (more features than samples)
A_pca = np.array([[1, 2, 3, 4],
                  [2, 4, 6, 8]])  # 2 samples, 4 features

print("PCA setting - Underdetermined system:")
print("Matrix shape:", A_pca.shape)
print("\nAnalyzing subspaces:")
explore_and_plot_subspaces(A_pca)

# Show connection to PCA
U, s, Vh = np.linalg.svd(A_pca)
print("\nSingular values (variance explained):")
print(s)
```

### Example 2: Overdetermined System (Least Squares Setting)

```python
# Create an overdetermined system (more samples than features)
A_ls = np.array([[1, 0],
                 [1, 1],
                 [1, 2],
                 [1, 3]])  # 4 samples, 2 features
b = np.array([1, 2, 4, 4])

print("\nLeast squares setting - Overdetermined system:")
print("Matrix shape:", A_ls.shape)
print("\nAnalyzing subspaces:")
explore_and_plot_subspaces(A_ls)

# Show connection to least squares
x_ls = np.linalg.lstsq(A_ls, b, rcond=None)[0]
residuals = b - A_ls @ x_ls
print("\nLeast squares solution:", x_ls)
print("Residual norm:", np.linalg.norm(residuals))
```

### Example 3: System Analysis

```python
def analyze_and_visualize_system(A, name=""):
    """Analyze and visualize a linear system"""
    m, n = A.shape
    print(f"\n{name} System Analysis:")
    print(f"Shape: {m}x{n}")
    
    if n > m:
        print("Underdetermined system (more features than samples)")
        print("Applications:")
        print("- PCA dimensionality reduction")
        print("- Feature selection")
        print("- Sparse solutions")
    else:
        print("Overdetermined system (more samples than features)")
        print("Applications:")
        print("- Least squares regression")
        print("- Error minimization")
        print("- Model fitting")
    
    explore_and_plot_subspaces(A)

# Example matrices
A1 = np.array([[1, 2, 3],
               [2, 4, 6]])  # Underdetermined
analyze_and_visualize_system(A1, "Underdetermined")

A2 = np.array([[1, 0],
               [1, 1],
               [1, 2]])  # Overdetermined
analyze_and_visualize_system(A2, "Overdetermined")
```

