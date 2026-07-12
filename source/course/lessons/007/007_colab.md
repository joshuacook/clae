---
title: "Linear Transformations and Eigentheory"
subtitle: "Week 4 - Practice Problems"
author: "Linear Algebra and Estimation Theory"
date: "2025-01-26"
---

# Practice Problems

## Example 1: Rotation Matrix

Consider the rotation matrix:
$$R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$

1. Apply $R$ to $\mathbf{v} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$
2. Show this is a $90^\circ$ rotation
3. Find $R^2$ and explain its meaning

\pagebreak

### Solution:

1. Apply $R$ to $\mathbf{v}$:
   $$R\mathbf{v} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

2. This is a $90^\circ$ rotation because:
   - Original vector points along x-axis: $(1,0)$
   - Result points along y-axis: $(0,1)$
   - Preserves length: $\|\mathbf{v}\| = \|R\mathbf{v}\| = 1$

3. Find $R^2$:
   $$R^2 = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$
   
   This represents a $180^\circ$ rotation (two successive $90^\circ$ rotations)

\pagebreak

## Example 2: Finding Eigenvalues and Eigenvectors

For matrix $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$:

1. Find eigenvalues
2. Find eigenvectors
3. Verify results

\pagebreak

### Solution:

1. Write $A\mathbf{v} = \lambda\mathbf{v}$ in components:
   $$(3-\lambda)x + y = 0$$
   $$x + (3-\lambda)y = 0$$

   Let $a = 3-\lambda$. For non-zero solutions:
   $$ax + y = 0$$
   $$x + ay = 0$$
   
   These are consistent when $a^2 = 1$
   So $3-\lambda = ±1$
   Therefore $\lambda = 4$ or $\lambda = 2$

2. For $\lambda = 4$:
   $$-x + y = 0$$
   So $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$

   For $\lambda = 2$:
   $$x + y = 0$$
   So $\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

3. Verify:
   $$A\mathbf{v}_1 = \begin{bmatrix} 4 \\ 4 \end{bmatrix} = 4\mathbf{v}_1$$
   $$A\mathbf{v}_2 = \begin{bmatrix} 2 \\ -2 \end{bmatrix} = 2\mathbf{v}_2$$

\pagebreak

## Example 3: LU Decomposition

For matrix $A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}$:

1. Find $L$ and $U$
2. Verify decomposition

\pagebreak

### Solution:

1. For $A = LU$ where:
   $$L = \begin{bmatrix} 1 & 0 \\ l & 1 \end{bmatrix}, \quad U = \begin{bmatrix} p & q \\ 0 & r \end{bmatrix}$$

   From $LU = A$:
   $$p = 4$$
   $$q = 2$$
   $$lp = 2 \text{ so } l = \frac{1}{2}$$
   $$lq + r = 3 \text{ so } r = 2$$

   Therefore:
   $$L = \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix}$$

2. Verify:
   $$LU = \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & 1 \end{bmatrix}\begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix} = A$$

\pagebreak

## Example 4: Visualizing Transformations

```python
import numpy as np
import matplotlib.pyplot as plt

# Create grid of points
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
points = np.column_stack((X.ravel(), Y.ravel()))

# Define transformation
A = np.array([[2, 0], [0, 0.5]])  # Stretches x by 2, compresses y by 1/2

# Plot original and transformed points
plt.figure(figsize=(12, 5))

# Original space
plt.subplot(121)
plt.scatter(points[:,0], points[:,1], alpha=0.2)
plt.grid(True)
plt.axis('equal')
plt.title('Original Space')

# Transformed space
transformed = points @ A.T
plt.subplot(122)
plt.scatter(transformed[:,0], transformed[:,1], alpha=0.2)
plt.grid(True)
plt.axis('equal')
plt.title('Transformed Space')

plt.show()
```

\pagebreak

### Solution:

The visualization shows:
1. Original unit square becomes a rectangle
2. Horizontal stretching by factor of 2
3. Vertical compression by factor of 1/2
4. Area is preserved (2 × 1/2 = 1)
5. Parallel lines remain parallel (linear transformation)

Key observations:
- Eigenvectors are along coordinate axes
- Eigenvalues are 2 and 1/2
- No rotation or shearing occurs

\pagebreak

## Additional Practice Problems

### Eigenvalue Problems

1. Find eigenvalues and eigenvectors for:
   $$A = \begin{bmatrix} 5 & -1 \\ -1 & 5 \end{bmatrix}$$

\pagebreak

2. Find eigenvalues and eigenvectors for:
   $$B = \begin{bmatrix} 3 & -2 \\ 4 & -1 \end{bmatrix}$$

\pagebreak

### LU Decomposition Problems

1. Find $L$ and $U$ for:
   $$C = \begin{bmatrix} 3 & 1 \\ 6 & 4 \end{bmatrix}$$

\pagebreak

2. Find $L$ and $U$ for:
   $$D = \begin{bmatrix} 2 & 3 \\ 4 & 7 \end{bmatrix}$$

\pagebreak

### Diagonalization Problems

1. Diagonalize if possible:
   $$E = \begin{bmatrix} 4 & -1 \\ -1 & 4 \end{bmatrix}$$

\pagebreak

2. Diagonalize if possible:
   $$F = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$$

\pagebreak

3. Determine if diagonalizable and explain why:
   $$G = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

\pagebreak

### Solutions

#### Eigenvalue Problem 1
For $A = \begin{bmatrix} 5 & -1 \\ -1 & 5 \end{bmatrix}$:

1. Write equations:
   $$(5-\lambda)x - y = 0$$
   $$-x + (5-\lambda)y = 0$$

2. For non-zero solutions:
   $$\lambda = 6 \text{ or } \lambda = 4$$

3. Eigenvectors:
   For $\lambda = 6$: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$
   For $\lambda = 4$: $\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

#### Eigenvalue Problem 2
For $B = \begin{bmatrix} 3 & -2 \\ 4 & -1 \end{bmatrix}$:

1. Write equations:
   $$(3-\lambda)x - 2y = 0$$
   $$4x + (-1-\lambda)y = 0$$

2. For non-zero solutions:
   $$\lambda = 2 \text{ or } \lambda = 0$$

3. Eigenvectors:
   For $\lambda = 2$: $\mathbf{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$
   For $\lambda = 0$: $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$

\pagebreak

#### LU Problem 1
For $C = \begin{bmatrix} 3 & 1 \\ 6 & 4 \end{bmatrix}$:

1. From equations:
   $$p = 3$$
   $$q = 1$$
   $$l \cdot 3 = 6 \text{ so } l = 2$$
   $$2 \cdot 1 + r = 4 \text{ so } r = 2$$

2. Therefore:
   $$L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$$

#### LU Problem 2
For $D = \begin{bmatrix} 2 & 3 \\ 4 & 7 \end{bmatrix}$:

1. From equations:
   $$p = 2$$
   $$q = 3$$
   $$l \cdot 2 = 4 \text{ so } l = 2$$
   $$2 \cdot 3 + r = 7 \text{ so } r = 1$$

2. Therefore:
   $$L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 3 \\ 0 & 1 \end{bmatrix}$$

\pagebreak

#### Diagonalization Problem 1
For $E = \begin{bmatrix} 4 & -1 \\ -1 & 4 \end{bmatrix}$:

1. Eigenvalues: $\lambda = 5$ or $\lambda = 3$
2. Eigenvectors:
   For $\lambda = 5$: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$
   For $\lambda = 3$: $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$
3. Diagonalization:
   $$P = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}$$

#### Diagonalization Problem 2
For $F = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$:

1. Eigenvalues: $\lambda = 3$ or $\lambda = 2$
2. Eigenvectors:
   For $\lambda = 3$: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$
   For $\lambda = 2$: $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$
3. Diagonalization:
   $$P = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}$$

#### Diagonalization Problem 3
For $G = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$:

1. Only eigenvalue is $\lambda = 1$ with algebraic multiplicity 2
2. But only one independent eigenvector: $\mathbf{v} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$
3. Therefore $G$ is not diagonalizable (defective matrix)
4. This is a shear transformation
