---
title: "Vector Spaces: Mathematical Foundations"
subtitle: "Lesson 1: Notes"
author: "Linear Algebra and Estimation Theory"
date: "Week 1, Session 1"
---

# Vector Spaces: Mathematical Foundations

## I. Vector Space Definition (15 min)

### Definition
A vector space $V$ over a field $\mathbb{F}$ is a set with two operations:

- Vector addition: $+: V \times V \rightarrow V$
- Scalar multiplication: $\cdot: \mathbb{F} \times V \rightarrow V$

### Vector Space Axioms
For all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $c, d \in \mathbb{F}$:

1. Closure under addition: $\mathbf{u} + \mathbf{v} \in V$
2. Commutativity: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
3. Associativity: $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
4. Additive identity: $\exists \mathbf{0} \in V: \mathbf{v} + \mathbf{0} = \mathbf{v}$
5. Additive invers.e: $\exists -\mathbf{v} \in V: \mathbf{v} + (-\mathbf{v}) = \mathbf{0}$

### Example
$\mathbb{R}^2$ is a vector space over $\mathbb{R}$ with:

- Elements: $\mathbf{v} = (v_1, v_2)$
- Addition: $(v_1, v_2) + (w_1, w_2) = (v_1 + w_1, v_2 + w_2)$
- Scalar multiplication: $c(v_1, v_2) = (cv_1, cv_2)$

## II. Basic Vector Operations (20 min)

### Vector Addition
For $\mathbf{v} = (v_1, v_2)$ and $\mathbf{w} = (w_1, w_2)$:
$$\mathbf{v} + \mathbf{w} = (v_1 + w_1, v_2 + w_2)$$

#### Geometric Interpretation
- Head-to-tail method
- Parallelogram rule

\begin{tikzpicture}[scale=0.7]
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,4) node[above] {$y$};
\draw[thick,blue,->] (0,0) -- (2,1) node[midway,above left] {$\mathbf{v}$};
\draw[thick,red,->] (0,0) -- (1,2) node[midway,left] {$\mathbf{w}$};
\draw[thick,blue,->] (1,2) -- (3,3) node[midway,above] {$\mathbf{v}$};
\draw[thick,green,->] (0,0) -- (3,3) node[midway,right] {$\mathbf{v}+\mathbf{w}$};
\draw[dashed] (2,1) -- (3,3);
\end{tikzpicture}

### Scalar Multiplication
For $c \in \mathbb{R}$ and $\mathbf{v} = (v_1, v_2)$:
$$c\mathbf{v} = (cv_1, cv_2)$$

#### Geometric Interpretation
- Scaling
- Direction revers.al for negative scalars

\begin{tikzpicture}[scale=0.7]
\draw[->] (-2,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-2) -- (0,4) node[above] {$y$};
\draw[thick,blue,->] (0,0) -- (2,1) node[midway,above] {$\mathbf{v}$};
\draw[thick,red,->] (0,0) -- (4,2) node[midway,above] {$2\mathbf{v}$};
\draw[thick,green,->] (0,0) -- (-2,-1) node[midway,below] {$-\mathbf{v}$};
\end{tikzpicture}

### Vector Subtraction
$$\mathbf{v} - \mathbf{w} = \mathbf{v} + (-\mathbf{w}) = (v_1 - w_1, v_2 - w_2)$$

\begin{tikzpicture}[scale=0.7]
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,4) node[above] {$y$};
\draw[thick,blue,->] (0,0) -- (3,2) node[midway,above] {$\mathbf{v}$};
\draw[thick,red,->] (0,0) -- (1,2) node[midway,left] {$\mathbf{w}$};
\draw[thick,red,dashed,->] (3,2) -- (2,0) node[midway,right] {$-\mathbf{w}$};
\draw[thick,green,->] (0,0) -- (2,0) node[midway,below] {$\mathbf{v}-\mathbf{w}$};
\end{tikzpicture}

## III. Vector Properties (20 min)

### Magnitude (Length)
For $\mathbf{v} = (v_1, v_2)$:
$$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2}$$

#### Properties
1. $\|\mathbf{v}\| \geq 0$
2. $\|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}$
3. $\|c\mathbf{v}\| = |c|\|\mathbf{v}\|$

### Dot Product
For $\mathbf{v} = (v_1, v_2)$ and $\mathbf{w} = (w_1, w_2)$:
$$\mathbf{v} \cdot \mathbf{w} = v_1w_1 + v_2w_2$$

#### Properties
1. Commutativity: $\mathbf{v} \cdot \mathbf{w} = \mathbf{w} \cdot \mathbf{v}$
2. Distributivity: $\mathbf{v} \cdot (\mathbf{w} + \mathbf{u}) = \mathbf{v} \cdot \mathbf{w} + \mathbf{v} \cdot \mathbf{u}$
3. Scalar multiplication: $(c\mathbf{v}) \cdot \mathbf{w} = c(\mathbf{v} \cdot \mathbf{w})$

### Angle Between Vectors
$$\cos \theta = \frac{\mathbf{v} \cdot \mathbf{w}}{\|\mathbf{v}\|\|\mathbf{w}\|}$$

\begin{tikzpicture}[scale=0.7]
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,4) node[above] {$y$};
\draw[thick,blue,->] (0,0) -- (3,1) node[midway,below] {$\mathbf{v}$};
\draw[thick,red,->] (0,0) -- (2,3) node[midway,left] {$\mathbf{w}$};
\draw[->] (1.2,0.4) arc (18:56:1.2) node[midway,right] {$\theta$};
\end{tikzpicture}

## IV. Looking Ahead

Topics for next session:

- Matrix operations
- Linear transformations 
- Vector projections

\pagebreak

## Additional Resources
- [Linear Algebra and Its Applications, Gilbert Strang (NOT REQUIRED)](https://a.co/d/8QRh9UF)
- [MIT 1806](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Practice problems](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces)
- [3Blue1Brown](https://www.3blue1brown.com/topics/linear-algebra)
