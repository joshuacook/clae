---
title: "Introduction to Matrices"
subtitle: "Lesson 2: Colab"
author: "Linear Algebra and Estimation Theory"
date: "Week 1, Session 2"
---

# Linear Algebra Lab 2: Matrices, Linear Systems, and Independence

## Part 1: Matrix-Vector Multiplication - Both Perspectives

```python
import numpy as np
import matplotlib.pyplot as plt

# Example matrix and vector
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
x = np.array([2, -1, 1])

```
## Row perspective

```python
print("Computing Ax by rows:")
for i in range(3):
    result = np.dot(A[i,:], x)
    print(f"Row {i+1}: {A[i,:]} · {x} = {result}")
```

## Column perspective
```python
print("\nComputing Ax by columns:")
col_results = [A[:,j] * x[j] for j in range(3)]
for j in range(3):
    print(f"Column {j+1} contribution: {x[j]} * {A[:,j]} = {col_results[j]}")
print(f"Final result (sum of columns): {sum(col_results)}")

# Verify both methods give same result
print("\nFull matrix multiplication:")
print(A @ x) # Numpy's @ operator for matrix multiplication
```

### Practice Problem 1
```python
# TODO: Implement both row and column multiplication methods for:
A = np.array([
    [2, -1, 3],
    [4, 0, 1],
    [1, 2, 5]
])
x = np.array([1, 2, 3])

# TODO: Compute using row method
print("Row method results:")
# Your code here

# TODO: Compute using column method
print("\nColumn method results:")
# Your code here

# TODO: Verify results match using numpy's @ operator
```

## Part 2: Linear Systems and Invertibility

```python
# Example from lecture - difference matrix
A = np.array([
    [1, 0, 0],
    [-1, 1, 0],
    [0, -1, 1]
])

# Case 1: System has unique solution
b1 = np.array([1, 2, 3])
x1 = np.linalg.solve(A, b1)
print("Solution for b1:", x1)
print("Verification A@x1:", A @ x1)
print("Equals b1:", b1)

# Check invertibility
try:
    A_inv = np.linalg.inv(A)
    print("\nMatrix A is invertible")
    print("A invers.e:", A_inv)
except np.linalg.LinAlgError:
    print("\nMatrix A is not invertible")
```

### Practice Problem 2
```python
# TODO: Work with the non-invertible matrix C from lecture
C = np.array([
    [1, 0, -1],
    [-1, 1, 0],
    [0, -1, 1]
])

# TODO: Try to solve C@x = b for:
b2 = np.array([1, 3, 5])

# TODO: Show that C@x = 0 has non-zero solutions
# Hint: Try x = [c, c, c] for some constant c

# TODO: Explain why C is not invertible based on your findings
```

## Part 3: Vector Independence

### Complete Example
```python
def plot_vectors(vectors, title):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot zero vector
    ax.scatter([0], [0], [0], color='black', marker='o')
    
    # Plot vectors
    colors = ['r', 'g', 'b']
    for i, v in enumerate(vectors):
        ax.quiver(0, 0, 0, v[0], v[1], v[2], 
                 color=colors[i], arrow_length_ratio=0.1)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.show()

# Independent vectors from lecture
a1 = np.array([1, -1, 0])
a2 = np.array([0, 1, -1])
a3 = np.array([0, 0, 1])

plot_vectors([a1, a2, a3], "Independent Vectors")

# Dependent vectors from lecture
c1 = np.array([1, -1, 0])
c2 = np.array([0, 1, -1])
c3 = np.array([-1, 0, 1])  # = -c1 + c2

plot_vectors([c1, c2, c3], "Dependent Vectors")

# Verify c3 = -c1 + c2
print("c3:", c3)
print("-c1 + c2:", -c1 + c2)
```

### Practice Problem 3
```python
# TODO: Create three vectors v1, v2, v3
# Make v3 a linear combination of v1 and v2

# TODO: Find coefficients a and b such that v3 = av1 + bv2

# TODO: Verify your answer using numpy

# TODO: Plot your vectors using the plot_vectors function

# TODO: Explain why your vectors are dependent
```

## Bonus Challenge
Try creating a function that tests whether three vectors are dependent or independent!
```python
def test_independence(v1, v2, v3):
    # TODO: Implement this function
    # Return True if vectors are independent
    # Return False if vectors are dependent
    pass

# Test your function with the vectors from lecture
```