---
title: "Matrix Operations"
subtitle: "Lesson 3.1: Rules for Matrix Operations"
author: "Linear Algebra and Estimation Theory"
date: "Week 2, Session 1"
---

# Solving Linear Systems

## Motivating Example

Consider the system $Ax = b$ where:

$$A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{bmatrix}, \quad b = \begin{bmatrix} 2 \\ 3 \\ 3 \end{bmatrix}$$

We can solve this by inspection:

1. From row 1: $x_1 + x_2 = 2$
2. From row 2: $x_2 + x_3 = 3$
3. From row 3: $x_1 + x_3 = 3$

\pagebreak

The solution is $x = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}$

Verify: $Ax = \begin{bmatrix} 1 + 1 + 0 \\ 0 + 1 + 2 \\ 1 + 0 + 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \\ 3 \end{bmatrix} = b$

\pagebreak

# Vector Spaces and Linear Independence

## 1. Foundations of Linear Transformations

### Linear Independence and Basis

#### Linear Independence

Vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$ are linearly independent if the only solution to:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \text{ is } c_1 = c_2 = \cdots = c_k = 0$$

Key properties:

1. If one vector is a combination of others, the vectors are dependent
2. Adding a new vector to independent vectors may create dependence
3. Removing a vector from dependent vectors may create independence

#### Examples

##### Example 1: Consider vectors in $\mathbb{R}^3$:

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, 
\mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}, 
\mathbf{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}$$

These are dependent because $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$

##### Example 2: The standard basis vectors:

$$\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, 
\mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, 
\mathbf{e}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

Are independent (no combination gives zero except $c_1 = c_2 = c_3 = 0$)

#### Basis

A basis for a vector space is a sequence of vectors that:

1. Are linearly independent
2. Span the space (every vector is a combination of basis vectors)

##### Example 1: The standard basis for $\mathbb{R}^3$

$$\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, 
\mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, 
\mathbf{e}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

##### Example 2: The basis for the space of 2x2 matrices

$$\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, 
\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, 
\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, 
\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$$

##### Example 3: Another basis for $\mathbb{R}^3$

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, 
\mathbf{v}_2 = \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}, 
\mathbf{v}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

These vectors are linearly independent and span $\mathbb{R}^3$. Note that $\mathbf{v}_1$ and $\mathbf{v}_2$ span the xy-plane, while $\mathbf{v}_3$ provides the z-component.

#### Important properties:

1. Every vector has a unique representation in terms of basis vectors
2. Removing any basis vector leaves a set that doesn't span
3. Adding any vector creates dependence

#### Dimension

The dimension of a space is the number of vectors in any basis.

Key facts:

1. All bases have the same number of vectors
2. Dimension = number of independent vectors needed to span the space
3. For matrix $A$: rank + nullity = number of columns
4. If vectors span $\mathbb{R}^n$, at least n vectors are needed
5. If vectors are independent in $\mathbb{R}^n$, at most n vectors are possible

### Subspaces

A subspace is a subset of a vector space that is itself a vector space. 

#### Requirements:

1. The zero vector must be in the subspace
2. The sum of vectors in the subspace stays in the subspace
3. Scalar multiples of vectors in the subspace stay in the subspace

#### Examples in $\mathbb{R}^3$:

- Any line through the origin
- Any plane through the origin
- The whole space $\mathbb{R}^3$
- The zero vector alone

\pagebreak

## 2. The Fundamental Theorem of Linear Algebra

The Fundamental Theorem connects four fundamental subspaces of a matrix $A$:

### Column Space and Row Space

Column Space, $C(A)$
:   contains all combinations of the columns
:   All possible vectors $A\mathbf{x}$
:   Dimension = rank $r$
:   $A\mathbf{x} = \mathbf{b}$ is solvable when $\mathbf{b}$ is in $C(A)$

Row Space, $C(A^T)$
:   contains all combinations of the rows
:   All vectors $\mathbf{y}^TA$
:   Dimension = rank $r$ (same as column space)
:   Basis vectors are rows of reduced row echelon form $R$

### Nullspaces

Nullspace, $N(A)$
:   contains all solutions $\mathbf{x}$ to $A\mathbf{x} = \mathbf{0}$
:   Dimension = $n - r$
:   Basis vectors are special solutions

### Left Nullspace

Left Nullspace, $N(A^T)$
:   contains all solutions $\mathbf{y}$ to $A^T\mathbf{y} = \mathbf{0}$
:   Dimension = $m - r$
:   Basis vectors are rows of reduced row echelon form $R$

### Key Properties

1. Column space $\perp$ nullspace
2. Row space $\perp$ left nullspace
3. $\dim(\text{column space}) + \dim(\text{nullspace}) = n$
4. $\dim(\text{row space}) + \dim(\text{left nullspace}) = m$

\pagebreak

## 3. Visualization and Intuition

### The Big Picture

The four fundamental subspaces help us visualize what happens when we solve $Ax = b$:

1. The row space and nullspace are in the domain of $A$ (where $x$ lives)
2. The column space and left nullspace are in the codomain (where $b$ lives)
3. The transformation $A$ maps:
   - Row space vectors onto the column space
   - Nullspace vectors to zero
   - Nothing onto the left nullspace

\

\includegraphics[width=0.75\textwidth]{data/linalg/lessons/003/image.png}

\pagebreak

### Geometric Interpretation

Consider solving $Ax = b$:

1. First, we decompose $x$ into:
   - A row space component $y$
   - A nullspace component $z$
   
2. Then $A$ acts by:
   - Mapping $y$ to $b$ in the column space
   - Mapping $z$ to $0$
   - The sum $Ay + Az = b + 0 = b$

3. This explains why:
   - Solutions exist when $b$ is in the column space
   - Multiple solutions differ by nullspace vectors
   - The decomposition $x = y + z$ is unique

\pagebreak

## 4. Examples

When we solve $Ax = b$, the solution $x$ splits into two parts:

- $x = y + z$ where:
- $y$ is in the row space (maps to $b$)
- $z$ is in the nullspace (maps to $0$)

### Example 1

Consider the system $Ax = b$ where:

$$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}, 
b = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

To find the decomposition:

1. Find a particular solution $y$ by inspection or elimination:
  $$y = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} \text{ satisfies } Ay = b$$

2. Find the nullspace by solving $Az = 0$:
  $$z = t\begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix} \text{ satisfies } Az = 0$$

3. The complete solution decomposes as:
  $$x = y + z = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} + 
  t\begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix}$$

#### Verify

- $y$ is in the row space (it's a combination of rows of $A$)
- $z$ is in the nullspace ($Az = 0$)
- Any solution $x$ has this form for some $t$

### Example 2

For the matrix:

$$A = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 1 & 0 \end{bmatrix}$$

Let's find the decomposition:

1. Find the row space basis:

   - Row 1: $[1, -1, 0]$
   - Row 2: $[-1, 1, 0]$ is a multiple of row 1
   - Therefore row space is spanned by $\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$

2. Find the nullspace by solving $Ax = 0$:

   - From row 1: $x_1 - x_2 = 0$ so $x_1 = x_2$
   - Row 2 gives same equation
   - $x_3$ is free
   - Therefore nullspace is spanned by $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$

3. Any solution $x$ splits into:
   $$x = c_1\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} + 
   c_2\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

#### Verify

- First vector is in row space (combination of rows)
- Second vector is in nullspace ($A\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$)
- These vectors are orthogonal

1. This decomposition shows that:

   - $Ax = b$ has a solution when $b$ is in the column space
   - The solution is unique when the nullspace contains only zero
   - All solutions differ by nullspace vectors

2. The transformation $A$ maps:

   - Row space vectors to column space vectors
   - Nullspace vectors to zero
   - Any vector $x$ can be uniquely decomposed into these components

This decomposition is fundamental to understanding how linear transformations work and what happens to vectors when we apply them.

