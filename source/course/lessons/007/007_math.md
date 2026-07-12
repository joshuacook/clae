---
title: "Linear Transformations and Eigentheory"
subtitle: "Week 4"
author: "Linear Algebra and Estimation Theory"
date: "2025-01-26"
---

# Introduction to Eigentheory

### Connection to Transformations

Every linear transformation can be understood through its eigenvectors:

- They form a special coordinate system i.e. a basis
- The transformation becomes simple in this system
- Diagonalization reveals this structure

### Motivation

Under a transformation:

- Most vectors change direction
- Special vectors (eigenvectors) maintain their direction
- These special directions reveal fundamental structure

Consider:

$$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

- Vector $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ is stretched by 3
- Vector $\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ is stretched by 1

\pagebreak

### Definition and Motivation

For a matrix $A$, we're looking for special vectors $\mathbf{v}$ that maintain their direction when transformed by $A$. These vectors might be stretched or compressed, but they don't change direction.

Mathematically, this means:
$$A\mathbf{v} = \lambda\mathbf{v}$$

where:

- $\mathbf{v}$ is called an eigenvector
- $\lambda$ is called an eigenvalue (the stretch/compression factor)

In general, this equation can be solved by:

\begin{align*}
A\mathbf{v} &= \lambda\mathbf{v} \\
A\mathbf{v} &= \lambda I \mathbf{v} \\
A\mathbf{v} - \lambda I \mathbf{v} &= \mathbf{0} \\
(A-\lambda I)\mathbf{v} &= \mathbf{0}
\end{align*}

### The Characteristic Polynomial

For a 2×2 matrix, we can write the eigenvalue equation as:

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \lambda\begin{bmatrix} x \\ y \end{bmatrix}$$

Which means:
$$ax + by = \lambda x$$
$$cx + dy = \lambda y$$

The values of $\lambda$ that allow non-zero solutions $(x,y)$ are the eigenvalues. These values make the equations "compatible" or "dependent". We can use
this to derive the characteristic polynomial.

Let's derive the characteristic polynomial for a general 2×2 matrix:

1. From our system of equations:
   $$(a-\lambda)x + by = 0$$
   $$cx + (d-\lambda)y = 0$$

2. From first equation: $x = -\frac{by}{a-\lambda}$
   From second equation: $x = -\frac{(d-\lambda)y}{c}$

3. These are equal when:
   $$-\frac{by}{a-\lambda} = -\frac{(d-\lambda)y}{c}$$
   $$bc = (a-\lambda)(d-\lambda)$$
   $$(a-\lambda)(d-\lambda) - bc = 0$$
   $$\lambda^2 - (a+d)\lambda + (ad-bc) = 0$$

This is the characteristic polynomial for any 2×2 matrix. **We would be unlikely to do this for anything of higher dimension.** Importantly, the degree of the polynomial is the number of eigenvalues/eigenvector pairs. This generalizes to higher dimensions.

\pagebreak

## Finding Eigenvalues

The key equation $A\mathbf{v} = \lambda\mathbf{v}$ tells us that eigenvectors are special vectors that maintain their direction under transformation, only being stretched or compressed by $\lambda$.

To find eigenvalues:

1. Write $A\mathbf{v} = \lambda\mathbf{v}$ as a system of equations
2. Look for values of $\lambda$ that allow non-zero solutions
3. These values are the eigenvalues

### Example: Direct Method

For matrix $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$:

1. Write $A\mathbf{v} = \lambda\mathbf{v}$ in components:
   $$\begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \lambda\begin{bmatrix} x \\ y \end{bmatrix}$$
   
   Gives system:
   $$3x + y = \lambda x$$
   $$x + 3y = \lambda y$$

2. Rearrange to standard form:
   $$(3-\lambda)x + y = 0$$
   $$x + (3-\lambda)y = 0$$

3. For non-zero solution in $x$ and $y$, coefficients must be dependent:
   - Let $3-\lambda = a$, then:
   $$ax + y = 0$$
   $$x + ay = 0$$
   - This becomes:
   $$x + \frac{y}{a} = 0$$
   $$x + ay = 0$$
   - Then:
   \begin{align*}
   ay - \frac{y}{a} &= 0 \\
   y(a - \frac{1}{a}) &= 0 \\
   y(a^2 - 1) &= 0
   \end{align*}
   - Thus our system has non-zero solutions only when $a^2 = 1$ because:
   - Therefore $3-\lambda = ±1$
   - Solving: $\lambda = 4$ or $\lambda = 2$

4. Find eigenvectors:
   For $\lambda = 4$ ($a = -1$):
   $$-x + y = 0$$
   $$x - y = 0$$
   These are the same equation: $x = y$
   So $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ is an eigenvector

   For $\lambda = 2$ ($a = 1$):
   $$x + y = 0$$
   $$x + y = 0$$
   These are the same equation: $x = -y$
   So $\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ is an eigenvector

5. Check our work:
   For $\lambda = 4$:
   $$\begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = 4\begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
   
   For $\lambda = 2$:
   $$\begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = 2\begin{bmatrix} 1 \\ -1 \end{bmatrix}$$

\pagebreak

### Example: Upper Triangular Matrix

For matrix $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$:

1. Write $A\mathbf{v} = \lambda\mathbf{v}$ in components:
   $$\begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \lambda\begin{bmatrix} x \\ y \end{bmatrix}$$
   
   Gives system:
   $$3x + y = \lambda x$$
   $$2y = \lambda y$$

2. From second equation:
   $$2y = \lambda y$$
   $$y(2-\lambda) = 0$$
   So either $y = 0$ or $\lambda = 2$

3. From first equation:
   $$3x + y = \lambda x$$
   $$x(3-\lambda) = -y$$
   
   When $\lambda = 2$:
   $$x = -y$$
   Giving eigenvector $\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$

   When $y = 0$:
   $$3x = \lambda x$$
   So $\lambda = 3$ with eigenvector $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

4. Verify:
   $$A\mathbf{v}_1 = \begin{bmatrix} 3 \\ 0 \end{bmatrix} = 3\mathbf{v}_1$$
   $$A\mathbf{v}_2 = \begin{bmatrix} -2 \\ 2 \end{bmatrix} = 2\mathbf{v}_2$$


\pagebreak

## 4. Eigenspaces and Multiplicities

### Key Concepts

- Algebraic multiplicity: power of $(λ-λ_i)$ in characteristic polynomial
- Geometric multiplicity: dimension of eigenspace (number of linearly independent eigenvectors)
- The eigenspace for eigenvalue $\lambda$ contains all vectors $\mathbf{v}$ that satisfy $(A-\lambda I)\mathbf{v} = \mathbf{0}$
- These vectors form a subspace because any linear combination of eigenvectors with eigenvalue $\lambda$ is also an eigenvector with eigenvalue $\lambda$
- For diagonalizable matrices: algebraic = geometric
- When they differ: matrix is defective

### Example

For matrix $H = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$:

1. Characteristic equation: $(2-λ)^2 = 0$
- Algebraic multiplicity of $λ=2$ is 2
- But eigenspace has dimension 1
- Therefore $H$ is defective

\pagebreak

## 5. Matrix Decompositions

### LU Decomposition

The LU decomposition splits a matrix $A$ into a product of two triangular matrices:
$$A = LU$$
where:

- $L$ is lower triangular (ones on diagonal)
- $U$ is upper triangular

For a 2×2 matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:

$$L = \begin{bmatrix} 1 & 0 \\ l & 1 \end{bmatrix}, \quad U = \begin{bmatrix} p & q \\ 0 & r \end{bmatrix}$$

Multiplying these out:
$$\begin{bmatrix} 1 & 0 \\ l & 1 \end{bmatrix}\begin{bmatrix} p & q \\ 0 & r \end{bmatrix} = \begin{bmatrix} p & q \\ lp & lq+r \end{bmatrix}$$

This must equal our original matrix:
$$\begin{bmatrix} p & q \\ lp & lq+r \end{bmatrix} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

This gives us a system of equations:
$$p = a$$
$$q = b$$
$$lp = c$$
$$lq + r = d$$

\pagebreak

#### Example: For $A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}$

1. From equations above:
   $$p = 4$$
   $$q = 2$$
   $$l \cdot 4 = 2 \text{ so } l = \frac{1}{2}$$
   $$\frac{1}{2} \cdot 2 + r = 3 \text{ so } r = 2$$

2. Therefore:
   $$L = \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & 1 \end{bmatrix}, \quad
   U = \begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix}$$

3. Verify: 
   $$LU = \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & 1 \end{bmatrix}
   \begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix} = 
   \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix} = A$$

#### Another Example: $B = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$

1. Eliminate below diagonal:
   - Need to subtract 2 times row 1 from row 2
   - This gives multiplier $l_{21} = 2$
   $$\begin{bmatrix} 2 & 1 & | & 1 & 0 \\ 0 & 1 & | & -2 & 1 \end{bmatrix}$$

2. Read off matrices:
   $$L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}, \quad
   U = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}$$

3. Verify:
   $$LU = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
   \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix} =
   \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix} = B$$

#### Key Points:
1. $L$ always has 1's on diagonal
2. Multipliers become entries in $L$
3. $U$ is the result of elimination
4. Not every matrix has an LU decomposition
5. If row exchanges needed, use PLU decomposition instead

\pagebreak

#### Using LU Decomposition to Compute Inverse

Once we have the LU decomposition of $A$, we can find $A^{-1}$ by solving:
$$A^{-1} = U^{-1}L^{-1}$$

For a 2×2 matrix:
1. $L^{-1}$ is easy because $L$ is unit lower triangular:
   $$\text{If } L = \begin{bmatrix} 1 & 0 \\ l & 1 \end{bmatrix} \text{ then } L^{-1} = \begin{bmatrix} 1 & 0 \\ -l & 1 \end{bmatrix}$$

2. $U^{-1}$ is easy because $U$ is upper triangular:
   $$\text{If } U = \begin{bmatrix} a & b \\ 0 & d \end{bmatrix} \text{ then } U^{-1} = \begin{bmatrix} \frac{1}{a} & -\frac{b}{ad} \\ 0 & \frac{1}{d} \end{bmatrix}$$


Example: For $A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}$
We found:
$$L = \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix}$$

Therefore:
$$L^{-1} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{2} & 1 \end{bmatrix}$$
$$U^{-1} = \begin{bmatrix} \frac{1}{4} & -\frac{1}{4} \\ 0 & \frac{1}{2} \end{bmatrix}$$
$$A^{-1} = U^{-1}L^{-1} = \begin{bmatrix} \frac{3}{8} & -\frac{1}{4} \\ -\frac{1}{4} & \frac{1}{2} \end{bmatrix}$$

Verify: $AA^{-1} = I$

\pagebreak

## 6. Diagonalization

### Process
1. Find eigenvalues $λ_i$
2. Find eigenvectors $\mathbf{v}_i$
3. Form $P = [\mathbf{v}_1 \; \mathbf{v}_2]$
4. Then $P^{-1}AP = D$ (diagonal)

### Worked Example
For matrix $B = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$:

1. Write $B\mathbf{v} = \lambda\mathbf{v}$ in components:
   $$\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \lambda\begin{bmatrix} x \\ y \end{bmatrix}$$
   
   Gives system:
   $$x + 2y = \lambda x$$
   $$2x + 4y = \lambda y$$

2. From first equation:
   $$(1-\lambda)x + 2y = 0$$
   $$y = \frac{(\lambda-1)x}{2}$$

3. Substitute into second equation:
   $$2x + 4(\frac{(\lambda-1)x}{2}) = \lambda y = \lambda(\frac{(\lambda-1)x}{2})$$
   $$2x + 2(\lambda-1)x = \lambda(\lambda-1)x/2$$
   $$4x + 2(\lambda-1)x = \lambda(\lambda-1)x$$
   $$x(4 + 2\lambda - 2 - \lambda^2 + \lambda) = 0$$
   $$x(\lambda^2 - 3\lambda + 2) = 0$$
   $$\lambda = 2 \text{ or } \lambda = 1$$

4. Find eigenvectors:
   For $\lambda = 2$:
   $$-x + 2y = 0$$
   $$y = \frac{x}{2}$$
   So $\mathbf{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$

   For $\lambda = 1$:
   $$2y = 0$$
   $$y = 0$$
   So $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

5. Form $P$ and verify diagonalization:
   $$P = \begin{bmatrix} 2 & 1 \\ 1 & 0 \end{bmatrix}$$

   For a 2×2 matrix, $P^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$
   where $P = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$

   Here: $P^{-1} = \begin{bmatrix} 0 & 1 \\ 1 & -2 \end{bmatrix}$

   Verify:
   $$PP^{-1} = P^{-1}P = I$$
   $$P^{-1}BP = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$$

\pagebreak
### Requirements
- Need n linearly independent eigenvectors
- Algebraic = geometric multiplicity for all $λ_i$
- Not all matrices are diagonalizable

### Special Cases
1. Symmetric matrices:
   - Always diagonalizable
   - Real eigenvalues
   - Orthogonal eigenvectors

2. Defective matrices:
   - Not diagonalizable
   - Algebraic > geometric multiplicity

\pagebreak

## 6. Geometric Interpretation

### Eigenvectors as Special Directions

- Eigenvectors: directions unchanged by transformation
- Eigenvalues: amount of stretching/compression
- Negative eigenvalues: direction reversal

### Examples

1. **Rotation matrices**:
   - No real eigenvectors (except 180° rotation)
   - Complex eigenvalues $e^{±iθ}$

2. **Projection matrices**:
   - Eigenvalues are 0 and 1
   - Eigenvectors: projection direction and kernel

3. **Symmetric matrices**:
   - Real eigenvalues
   - Orthogonal eigenvectors
   - Diagonalizable

## 7. Applications

### Principal Component Analysis
- Eigenvalues measure variance in each direction
- Eigenvectors give principal directions
- Used for dimensionality reduction
- Example: image compression, data analysis

### Dynamical Systems
- Powers of matrices: $A^n\mathbf{x}$
- Long-term behavior determined by eigenvalues
- $|λ| < 1$: decay
- $|λ| > 1$: growth
- Example: population dynamics

### Quantum Mechanics
- Hermitian matrices: special case of symmetric
- Eigenvalues are observable quantities
- Eigenvectors are possible states
- Example: energy levels of hydrogen atom

## Additional Resources
- Strang Chapter 6
- 3Blue1Brown Linear Transformations
- Course notes on matrix operations
- Python numpy.linalg documentation
