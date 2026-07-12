---
title: "Vector Spaces and Linear Independence Lab"
subtitle: "Lesson 3.1: Hands-on Practice"
---

# Lab Exercises: Vector Spaces and Linear Independence

## Exercise 1: Solving Linear Systems by Inspection

Verify our motivating example from the lecture:

```python
import numpy as np

# Define A and b
A = np.array([[1, 1, 0], 
              [0, 1, 1],
              [1, 0, 1]])
b = np.array([2, 3, 3])

# Our solution from inspection
x = np.array([1, 1, 2])
x_solved = np.linalg.solve(A, b)

# Verify Ax = b
print("Ax =", A @ x)
print("b  =", b)
print("Ax = b is", np.allclose(A @ x, b))
print("Solved Ax = b is", np.allclose(A @ x_solved, b))
```

## Exercise 2: Linear Independence

Test if these vectors are linearly independent:

```python
def are_independent(vectors):
    """Return True if vectors are linearly independent"""
    matrix = np.column_stack(vectors)
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)

# Test vectors from lecture Example 1
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
v3 = np.array([1, 1, 2])

vectors = [v1, v2, v3]
print("Vectors are independent:", are_independent(vectors))

# Show that v3 = v1 + v2
print("v3 =", v3)
print("v1 + v2 =", v1 + v2)
```

## Exercise 3: Four Fundamental Subspaces

Explore the four subspaces for a matrix:

```python
def explore_subspaces(A):
    """Print dimensions and bases of the four fundamental subspaces"""
    m, n = A.shape
    rank = np.linalg.matrix_rank(A)
    
    print(f"Matrix shape: {m}x{n}")
    print(f"Rank: {rank}")
    print(f"\nDimensions:")
    print(f"Column space: {rank}")
    print(f"Row space: {rank}")
    print(f"Nullspace: {n - rank}")
    print(f"Left nullspace: {m - rank}")
    
    # Get nullspace basis
    _, _, Vh = np.linalg.svd(A)
    nullspace_basis = Vh[rank:].T
    
    print("\nNullspace basis:")
    print(nullspace_basis)

# Example matrix from lecture
A = np.array([[1, 0, 1],
              [0, 1, 1]])

explore_subspaces(A)
```

## Exercise 4: Solution Decomposition

Decompose solutions into row space and nullspace components:

```python
def decompose_solution(A, b):
    """Decompose solution x into y (row space) and z (nullspace)"""
    # Get particular solution
    y = np.linalg.pinv(A) @ b
    
    # Get nullspace basis
    _, _, Vh = np.linalg.svd(A)
    rank = np.linalg.matrix_rank(A)
    z = Vh[rank:].T
    
    print("Particular solution y:")
    print(y)
    print("\nNullspace basis vectors:")
    print(z)
    
    return y, z

# Example from lecture
A = np.array([[1, -1, 0],
              [-1, 1, 0]])
b = np.array([0, 0])

y, z = decompose_solution(A, b)

# Verify decomposition
print("\nVerify Ay = b:")
print("Ay =", A @ y)
print("b  =", b)

print("\nVerify Az = 0:")
print("Az =", A @ z)
```

## Challenge Problems

1. Find a basis for the nullspace of:
   ```python
   A = np.array([[1, 2, 3],
                 [2, 4, 6]])
   ```

2. Determine if these vectors span R³:
   ```python
   v1 = np.array([1, 0, 1])
   v2 = np.array([0, 1, 0])
   v3 = np.array([1, 1, 1])
   ```

3. Find the dimension of the intersection of:
   ```python
   # Subspace 1: span{[1,1,0], [0,1,1]}
   # Subspace 2: span{[1,0,1], [1,1,1]}
   ```
