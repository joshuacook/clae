---
title: "Introduction to Matrices"
subtitle: "Lesson 2: Mathematical Foundations"
author: "Linear Algebra and Estimation Theory"
date: "Week 1, Session 2"
---

# Matrices: Mathematical Foundations

## 1. Introduction to Matrices

A matrix is a rectangular array of numbers arranged in rows and columns. Let's start with a concrete example:

### Matrix Definition and Structure

A matrix $A$ with $m$ rows and $n$ columns (an $m \times n$ matrix) has the form:

$A = \begin{bmatrix} 
1 & 2 \\
3 & 4 \\
5 & 6
\end{bmatrix}$ is a 3 by 2 matrix: $m = 3$ rows and $n = 2$ columns.

### Matrix-Vector Multiplication

When we multiply a matrix $A$ by a vector $\mathbf{x}$, we get a combination of the columns of $A$:

$A\mathbf{x} = \begin{bmatrix} 
1 & 2 \\
3 & 4 \\
5 & 6
\end{bmatrix} \begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}$ is a combination of the columns: $A\mathbf{x} = x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}$

### Computing Matrix-Vector Products

The components of $Ax$ are dot products of the rows of $A$ with the vector $\mathbf{x}$. Suppose $\mathbf{x} = (7, 8)$. 

$\begin{bmatrix} 
1 & 2 \\
3 & 4 \\
5 & 6
\end{bmatrix} \begin{bmatrix}
7 \\
8
\end{bmatrix} = \begin{bmatrix}
1 \cdot 7 + 2 \cdot 8 \\
3 \cdot 7 + 4 \cdot 8 \\
5 \cdot 7 + 6 \cdot 8
\end{bmatrix} = \begin{bmatrix}
23 \\
53 \\
83
\end{bmatrix}$

### Linear Systems in Matrix Form

A system of linear equations can be written as a matrix equation $Ax = b$:

$\begin{bmatrix}
2 & 5 \\
3 & 7
\end{bmatrix} \begin{bmatrix}
x_1 \\
x_2
\end{bmatrix} = \begin{bmatrix}
b_1 \\
b_2
\end{bmatrix}$ replaces $\begin{cases} 2x_1 + 5x_2 = b_1 \\ 3x_1 + 7x_2 = b_2 \end{cases}$

\begin{boxed}
The solution can be written as $x = A^{-1}b$ when $A^{-1}$ exists (we'll explore when this is possible in later lessons).
\end{boxed}

## Matrix Combinations and Transformations

### Vector Combinations as Matrix Operations

When we combine vectors with coefficients, we can rewrite it as a matrix operation:

$x_1\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix} + x_3\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} x_1 \\ x_2 - x_1 \\ x_3 - x_2 \end{bmatrix}$

This combination can be rewritten using matrix multiplication:

$A\mathbf{x} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} x_1 \\ x_2 - x_1 \\ x_3 - x_2 \end{bmatrix}$

The input is $\mathbf{x}$ and the output is $\mathbf{b} = A\mathbf{x}$. This $A$ is a **difference matrix** because it contains difference of the input vector $\mathbf{x}$.

## Row-wise vs Column-wise Matrix Multiplication
**You are probably used to matrix multiplication by rows. This is showing matrix multiplication by columns.**

Let's compare both approaches using a simple example:

### Row-wise Multiplication
For matrix $A$ and vector $\mathbf{x}$:

$A\mathbf{x} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$

By rows:
1. First row: $(1 \cdot x_1 + 2 \cdot x_2 + 3 \cdot x_3)$
2. Second row: $(4 \cdot x_1 + 5 \cdot x_2 + 6 \cdot x_3)$

The vector for this would be:

$\begin{bmatrix}
x_1 + 2x_2 + 3x_3 \\
4x_1 + 5x_2 + 6x_3
\end{bmatrix}$

### Column-wise Multiplication
The same multiplication viewed as column combinations:

$A\mathbf{x} = x_1\begin{bmatrix} 1 \\ 4 \end{bmatrix} + x_2\begin{bmatrix} 2 \\ 5 \end{bmatrix} + x_3\begin{bmatrix} 3 \\ 6 \end{bmatrix} = \begin{bmatrix} x_1 + 2x_2 + 3x_3 \\ 4x_1 + 5x_2 + 6x_3 \end{bmatrix}$


## Linear Equations

Consider the equation

$$A\mathbf{x} = \mathbf{b}$$

What you are likely more familiar with is where you must compute the linear combination of the columns of $A$ to find $\mathbf{b}$.

\paragraph{A New Viewpoint} Which combination of $\mathbf{u}, \mathbf{v}, \mathbf{w}$ produces a particular vector $\mathbf{b}$? In other words, $A$ and $\mathbf{b}$ are known. What **linear combination** of the columns of $A$ produces $\mathbf{b}$? 

$\rightarrow$ this is $\mathbf{x}$.

### Example System

\begin{align*}
x_1 &= b_1 \\
-x_1 + x_2 &= b_2 \\
-x_2 + x_3 &= b_3
\end{align*}

The solution is:

\begin{align*}
x_1 &= b_1 \\
x_2 &= b_1 + b_2 \\
x_3 &= b_1 + b_2 + b_3
\end{align*}

Look at two specific choices. When $\mathbf{b} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$, we get $\mathbf{x} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$. When $\mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}$, we get $\mathbf{x} = \begin{bmatrix} 1 \\ 4 \\ 9 \end{bmatrix}$.

\paragraph{Invertibility} *If the output is $\mathbf{b} = \mathbf{0}$, then the input must be $\mathbf{x} = \mathbf{0}$*. That statement is true for this matrix $A$. It is not true for all matrices. 

- $A$ is "invertible"
- from $\mathbf{b}$ we can recover $\mathbf{x}$

$$\mathbf{x} = A^{-1}\mathbf{b}$$

\paragraph{A non-invertible matrix}

Let $C = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}$. 

Let's multiply $C$ by a vector $\mathbf{x}$:

$C\mathbf{x} = \begin{bmatrix} 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} x_1 - x_3 \\ -x_1 + x_2 \\ -x_2 + x_3 \end{bmatrix} = \mathbf{b}$


We can have another matrix $C$ where $C\mathbf{x} = \mathbf{0}$ when $C \neq 0$ and $\mathbf{x} \neq \mathbf{0}$.

There are two possibilities:

- $C\mathbf{x}$ has infinite solutions (e.g. $\mathbf{b} = \mathbf{0}$ and $\mathbf{x} = (3,3,3)$ is one solution)
- $C\mathbf{x}$ has no solutions (e.g. $\mathbf{b} = (1, 3, 5)$)

\paragraph{Geometric Interpretation} The columns of $C$ are $\mathbf{u}=(1, -1, 0)$, $\mathbf{v}=(0, 1, -1)$, $\mathbf{w}=(0, 0, 1)$.

- **NO LINEAR COMBINATION OF THESE THREE VECTORS CAN PRODUCE $(1,3,5)$**.
- $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ are in the same plane. $\mathbf{b}$ is not in that plane.

## Dependence and Independence

- Consider $A$ and $C$ and their column vectors, $a_1, a_2, a_3$ and $c_1, c_2, c_3$.
- Let's assume that $a_1$ and $a_2$ define a plane and $c_1$ and $c_2$ define a different plane.
- $a_3$ is independent of $a_1$ and $a_2$ **if and only if** it is not in the same plane.
- $c_3$ is independent of $c_1$ and $c_2$ **if and only if** it is not in the same plane.

\begin{align*}
a_1 &= (1, -1, 0) \\
a_2 &= (0, 1, -1) \\
a_3 &= (0, 0, 1) \\
\end{align*}

For matrix $A$, observe that $a_3$ points straight up in the $z$ direction, while $a_1$ and $a_2$ lie in different planes. No linear combination of $a_1$ and $a_2$ can produce $a_3$, making $a_3$ independent.

\begin{align*}
c_1 &= (1, -1, 0) \\
c_2 &= (0, 1, -1) \\
c_3 &= (-1, 0, 1) \\
\end{align*}

For matrix $C$, note that $c_3 = -c_1 + c_2$, showing that $c_3$ is a linear combination of $c_1$ and $c_2$. Therefore, $c_3$ is dependent on $c_1$ and $c_2$ - it lies in the same plane.

In summary:
- $\mathbf{u}, \mathbf{v}, \mathbf{w}$ are independent. No combination except $0\mathbf{u} + 0\mathbf{v} + 0\mathbf{w} = \mathbf{0}$ gives $\mathbf{b} = \mathbf{0}$.
- $\mathbf{u}, \mathbf{v}, \mathbf{w}^*$ are dependent. Other combinations like $\mathbf{u} + \mathbf{v} + \mathbf{w}^*$ give $\mathbf{b} = \mathbf{0}$.

## Additional Resources
- Strang Chapter 1.3
- [MIT OCW 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [3Blue1Brown Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
