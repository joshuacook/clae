<!-- DRAFT V7 (2026-07-19): the v11 pass per the v10 ink census +
     rulings. OPERATOR-ONLY chapter (census 3): the data identity,
     conventions, houses figure, transpose-as-data-flip, and
     standardization all OUT to Part II stock (.render/
     ch2_data_block.md, ch2_standardization_block.md). Composition
     PROMOTED to its own section (census 5) and receives the preface's
     three-ways display (dedup rule, census 15). Transpose is a slim
     technical section. NULL SPACE defined here at projection, where
     it is first used (census 6), and the inverse claim uses it. The
     inverse section is matrix-first (census 7/9), no operations
     listing, telescoping explained in place (census 8). R1 language
     sweep. Base: V6. -->

# Chapter 2: Matrices and Linear Transformations

Here is what this chapter does. A matrix is an **operator**: a machine that takes a vector in and produces a vector out, the verb of linear algebra. This chapter is that verb, whole: which rules a matrix can encode and why (linear transformations), how the matrix-vector and matrix-matrix products carry those rules (the product, then composition), the two named operators this book leans on hardest (the diagonal matrix and the projection), the space of everything an operator destroys (the null space), and the exact condition under which an operator can be inverted. A matrix is also, in daily practice, a dataset, and that second identity gets its own full treatment when the data arrives in Chapter 5. Here, one identity, done completely.

## 2.1 The verb that differentiates

The preface witnessed the first verb this book ever showed me, and now it gets built properly. A derivative, on a grid, is a matrix. Sample a function $f$ at points a distance $h$ apart, collect the samples in a vector $\mathbf{x}$ with $x_i = f(t_i)$, and build the matrix $D$ that takes differences of neighbors and divides by $h$:

\begin{align}
D = \frac{1}{h}\begin{bmatrix} -1 & 1 & & \\ & -1 & 1 & \\ & & \ddots & \ddots \\ & & & -1 \end{bmatrix}
\end{align}

\lensmark{algebraic} Do the symbolic computation before any code runs. Entry $i$ of $D\mathbf{x}$ is a linear combination of two neighboring samples, weights $-1/h$ and $1/h$:

\begin{align}
(D\mathbf{x})_i \;=\; \frac{-\,x_i + x_{i+1}}{h} \;=\; \frac{f(t_i + h) - f(t_i)}{h}
\end{align}

Look at the right-hand side. It is the difference quotient from the first week of calculus, the expression whose $h \to 0$ limit *defines* the derivative. The matrix is not approximating some formula that resembles differentiation. Row by row, it *is* differentiation, held at a finite step. Tighten the grid and the verb converges to the calculus. \lensmark{computational} Listing 2.2 constructs $D$ on a thousand-point grid over $[0, 2\pi]$.

**Listing 2.2 (building the derivative-taker)**

```python
import numpy as np

n = 1000
x = np.linspace(0, 2*np.pi, n)
h = x[1] - x[0]
D = (np.eye(n, k=1) - np.eye(n)) / h   # forward difference
```

Listing 2.3 feeds $D$ a sampled sine and measures the worst error against the true derivative, the cosine.

**Listing 2.3 (the verb, tested on a sine)**

```python
err = np.abs(D @ np.sin(x) - np.cos(x))[:-1].max()
print(f'max |D @ sin - cos|: {err:.4f}')
```

```text
max |D @ sin - cos|: 0.0031
```

Wrong in the third decimal, and the error shrinks as the grid tightens. Nothing happened except scaling and adding. The matrix took the derivative. Listing 2.4 plots the input, the output, and the truth; Figure 2.2 is its output.

**Listing 2.4 (drawing the derivative)**

```python
import matplotlib.pyplot as plt

plt.plot(x, np.sin(x), label='input: sin(x)')
plt.plot(x[:-1], (D @ np.sin(x))[:-1], label='output: D @ sin(x)')
plt.plot(x, np.cos(x), 'k--', lw=1, label='cos(x)')
plt.legend(); plt.show()
```

![the matrix D takes a derivative](figures/fig_matrix_derivative.png)

> **Figure 2.2.** The input `sin(x)`, the output `D @ sin(x)`, and `cos(x)` dashed on top of it. The output sits on the cosine to within the width of the line.

### What made it possible

Why could a matrix differentiate? Because differentiation is *linear*, and you have known that since your first calculus course without ever hearing the word used this way. The derivative of a sum is the sum of the derivatives, and constants pull out:

\begin{align}
(a f + g)' = a f' + g'
\end{align}

That pair of facts is the whole entrance requirement. Any operation that respects scaling and adding can be caught in a matrix, and only those operations can.

Stop on that sentence, because it is the stone this chapter is built on. What did the exhibit actually show? A rule that eats a whole vector and returns a whole vector, computed by nothing but scalings and additions of the input's entries. The claim being made is that this shape of rule, input vector, output vector, arithmetic that never leaves Chapter 1's two moves, is what a matrix *is*, and the derivative was one citizen of the class, not a trick. Before any more examples, the class gets its formal name.

> **Definition 2.1 (linear transformation).** A function $T$ from vectors to vectors is a **linear transformation** when $T(c\mathbf{x} + d\mathbf{y}) = c\,T(\mathbf{x}) + d\,T(\mathbf{y})$ for all vectors $\mathbf{x}, \mathbf{y}$ and weights $c, d$.

In words, a linear transformation never disturbs a linear combination. Transform the inputs and the recipe carries over untouched. \lensmark{algebraic} Work one qualifying example and one failure, small enough to check at a desk. The doubling map $T(\mathbf{x}) = 2\mathbf{x}$ qualifies:

\begin{align}
T(c\mathbf{x} + d\mathbf{y}) = 2\,(c\mathbf{x} + d\mathbf{y}) = c\,(2\mathbf{x}) + d\,(2\mathbf{y}) = c\,T(\mathbf{x}) + d\,T(\mathbf{y})
\end{align}

Squaring every entry, $T(x_1, x_2) = (x_1^2, x_2^2)$, does not. Test it on $\mathbf{x} = (1, 2)$ with $c = 2$, $d = 0$:

\begin{align}
T(2\mathbf{x}) = T(2, 4) = (4, 16), \qquad\quad 2\,T(\mathbf{x}) = 2\,(1, 4) = (2, 8)
\end{align}

Double the input and the output quadruples. The recipe did not survive, so squaring is out. Differencing qualifies, by the calculus facts above, and the machine agrees on sampled vectors: $D(a\mathbf{x} + \mathbf{y}) = a\,D\mathbf{x} + D\mathbf{y}$ to the last bit, because every entry of $D\mathbf{x}$ is a linear combination and combinations pass through combinations. Shifting every entry by one fails too, more quietly. It moves the origin, and the standardization section will have to answer for that.

Here is the fact this chapter stands on, and it deserves its box early.

> **Claim 2.1 (matrices are the linear transformations).** Every $m \times n$ matrix gives a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ via $T(\mathbf{x}) = A\mathbf{x}$, and every linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ is given by exactly one such matrix: the matrix whose $j$-th column is $T(\mathbf{e}_j)$, the image of the $j$-th standard basis vector. **The columns of $A$ are where the basis vectors land.**
>
> Witness it on the stretch map that doubles the first axis and halves the second. It sends $\mathbf{e}_1 = (1, 0)$ to $(2, 0)$ and $\mathbf{e}_2 = (0, 1)$ to $(0, \tfrac{1}{2})$. Stack the two landing spots as columns and the matrix is built, no algebra spent. The one-breath reason it always works: every $\mathbf{x}$ is a recipe in the standard basis with its own entries as the weights, and a linear $T$ carries the recipe onto the landed vectors $T(\mathbf{e}_j)$.[^landing]

[^landing]: The breath, written out. Chapter 1 showed $\mathbf{x} = x_1\mathbf{e}_1 + \cdots + x_n\mathbf{e}_n$. Apply $T$ and linearity gives $T(\mathbf{x}) = x_1 T(\mathbf{e}_1) + \cdots + x_n T(\mathbf{e}_n)$, a linear combination of the fixed vectors $T(\mathbf{e}_j)$ with weights $x_j$. Stack those fixed vectors as the columns of $A$ and the right-hand side is $A\mathbf{x}$ by definition of the product. Conversely $\mathbf{x} \mapsto A\mathbf{x}$ is linear because combinations pass through it slotwise.

\lensmark{geometric} The witness, drawn:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=1.4]
  \draw[gray!40, ->] (-0.4,0) -- (2.6,0);
  \draw[gray!40, ->] (0,-0.3) -- (0,1.5);
  \draw[gray!30] (0,0) rectangle (1,1);
  \draw[->, very thick] (0,0) -- (1,0) node[below] {$\mathbf{e}_1$};
  \draw[->, very thick] (0,0) -- (0,1) node[left] {$\mathbf{e}_2$};
  \draw[gray!60, dashed] (0,0) rectangle (2,0.5);
  \draw[->, very thick, gray] (0,0) -- (2,0);
  \node[gray, below] at (2.05,-0.05) {$(2, 0)$};
  \draw[->, very thick, gray] (0,0) -- (0,0.5);
  \node[gray, left] at (-0.08,0.62) {$(0, \tfrac{1}{2})$};
  \node at (3.6,0.8) {$S = \begin{bmatrix} 2 & 0 \\ 0 & \tfrac{1}{2} \end{bmatrix}$};
\end{tikzpicture}
\caption{The columns are where the basis vectors land. The stretch map sends $\mathbf{e}_1$ to $(2,0)$ and $\mathbf{e}_2$ to $(0,\frac{1}{2})$, and stacking the landings as columns builds the diagonal matrix $S$. The unit square lands on the dashed rectangle.}
\end{figure}

Two landings, two columns, and the transformation is fully known. That is the content of the claim. To know a linear transformation completely you need to know it on $n$ inputs only, the basis, because everything else is recipes.

$D$'s landings tell the same story with utility attached. $D$ sends the spike $\mathbf{e}_j$ to a dipole, $(\mathbf{e}_{j-1} - \mathbf{e}_j)/h$, which is exactly column $j$ of $D$, and differentiation-on-a-grid is nothing but those dipoles combined by the recipe. And the multiplication $A\mathbf{x}$ is not a new operation at all. It is Chapter 1's one move, a linear combination of $A$'s columns, with $\mathbf{x}$ as the recipe. The matrix is not storing its columns. It is waiting to combine them.

## 2.2 The product

The matrix-vector product is where the operator acts, and it reads two ways. Each reading answers a different question about the verb, and this section is the book's complete treatment of both, the treatment the preface deliberately left to it.

> **Definition 2.2 (matrix-vector product, both views).** For an $m \times n$ matrix $A$ with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n$ and rows $\mathbf{r}_1, \ldots, \mathbf{r}_m$, the product $A\mathbf{x}$ reads two ways. **By columns**, it is the linear combination $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$. **By rows**, its $i$-th entry is the dot product $\mathbf{r}_i \cdot \mathbf{x}$.

\lensmark{algebraic} Work one product both ways. Take the $3 \times 2$ matrix and input

\begin{align}
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}, \qquad \mathbf{x} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}
\end{align}

By rows, each output entry is a dot product, one at a time:

\begin{align}
(1, 2)\cdot(7, 8) = 23, \qquad (3, 4)\cdot(7, 8) = 53, \qquad (5, 6)\cdot(7, 8) = 83
\end{align}

By columns, the output is a single linear combination, formed all at once:

\begin{align}
7\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + 8\begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}
= \begin{bmatrix} 7 \\ 21 \\ 35 \end{bmatrix} + \begin{bmatrix} 16 \\ 32 \\ 48 \end{bmatrix}
= \begin{bmatrix} 23 \\ 53 \\ 83 \end{bmatrix}
\end{align}

Same sixteen multiplications, same answer, different story.

> **Claim 2.2 (the two views agree).** The row view and the column view compute the same vector.
>
> The one-breath reason: entry $i$ of the column view is $\sum_j x_j A_{ij}$, entry $i$ of the row view is $\sum_j A_{ij} x_j$, and the sums are identical term by term.

\lensmark{computational} Listing 2.5 writes each view as its own function, following the definition exactly.

**Listing 2.5 (the two views, defined)**

```python
def by_rows(A: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.array([row @ x for row in A])

def by_cols(A: np.ndarray, x: np.ndarray) -> np.ndarray:
    return sum(x[j] * A[:, j] for j in range(A.shape[1]))
```

Listing 2.6 checks both against NumPy's `@` on the worked example.

**Listing 2.6 (the two views, run)**

```python
A = np.array([[1, 2], [3, 4], [5, 6]])
xx = np.array([7, 8])
print('A @ x      :', A @ xx)
print('row view   :', by_rows(A, xx))
print('column view:', by_cols(A, xx))
```

```text
A @ x      : [23 53 83]
row view   : [23 53 83]
column view: [23 53 83]
```

The row view is how you compute by hand, one entry at a time. The column view is how you understand. The output lives in the span of the columns, always, and that fact runs the rest of the book.[^memory] Most first courses teach the row view only. This book needs you holding both.

[^memory]: The two views even have a memory address. NumPy stores arrays row-major, so walking a row is walking contiguous memory. Pandas stores DataFrames as column blocks, so pulling a feature column is the cheap direction. Your two mental pictures of a data matrix disagree about physical layout, and each library picked a side.

\lensmark{geometric} The column view also draws, and in two dimensions it draws as Chapter 1's tip-to-tail walk. Take the matrix whose columns are Chapter 1's familiar pair $(2, 1)$ and $(1, 3)$, and the input $\mathbf{x} = (1, 2)$:

\begin{align}
\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}
\begin{bmatrix} 1 \\ 2 \end{bmatrix}
= 1\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 3 \end{bmatrix}
= \begin{bmatrix} 4 \\ 7 \end{bmatrix}
\end{align}

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.55]
  \draw[gray!30, ->] (-0.6,0) -- (5.2,0);
  \draw[gray!30, ->] (0,-0.6) -- (0,7.6);
  \draw[->, very thick] (0,0) -- (2,1) node[below right] {$1 \cdot \mathbf{a}_1$};
  \draw[->, thick, gray] (2,1) -- (3,4);
  \draw[->, thick, gray] (3,4) -- (4,7);
  \node[gray, anchor=west] at (3.6,4.9) {$2 \cdot \mathbf{a}_2$, walked};
  \draw[->, very thick, black!70] (0,0) -- (4,7) node[above] {$A\mathbf{x} = (4,7)$};
\end{tikzpicture}
\caption{The column view is Chapter 1 verbatim. One step of the first column, two steps of the second, tip to tail, and the product $A\mathbf{x}$ is the arrow to where you land. This is the recipe $1\,\mathbf{v} + 2\,\mathbf{w} = (4,7)$ from Chapter 1's solving question, computed by a matrix.}
\end{figure}

The drawing is Chapter 1's membership recipe, recomputed by a matrix, and that is the point: the product $A\mathbf{x}$ *is* the linear combination of $A$'s columns with recipe $\mathbf{x}$. Nothing new happened. The operation got an operator.

### The third way: slabs

The slab reading needs one piece of notation first, an operation that is bookkeeping rather than mathematics.

> **Definition 2.3 (transpose).** The **transpose** $A^\mathsf{T}$ swaps rows for columns, $(A^\mathsf{T})_{ij} = A_{ji}$. For a column vector $\mathbf{u}$, the transpose $\mathbf{u}^\mathsf{T}$ is the same numbers laid on their side, so that $\mathbf{u}^\mathsf{T}\mathbf{v}$ is the preface's dot product written in matrix algebra. Its deeper roles arrive on schedule: Chapter 5 flips data matrices with it, Chapter 7 builds covariance from $Z^\mathsf{T}Z$, and Chapter 12 reveals it as the keeper of the subject's right angles. Until then it is notation, and honest about it.

With rows purchasable from columns, the third reading of a product earns its definition.

> **Definition 2.4 (outer product).** The **outer product** of a column $\mathbf{u}$ in $\mathbb{R}^m$ and a column $\mathbf{v}$ in $\mathbb{R}^n$ is the $m \times n$ matrix $\mathbf{u}\mathbf{v}^{\mathsf{T}}$ with entries $u_i v_j$: every entry of one vector times every entry of the other, a full matrix built from two lists. Each column of $\mathbf{u}\mathbf{v}^{\mathsf{T}}$ is a multiple of $\mathbf{u}$, so the outer product is the most concentrated matrix there is, one direction's worth of content spread across a rectangle.

\lensmark{algebraic} The third way reads a *matrix-matrix* product as a sum of these slabs, one per column-row pair, and it collapses the matrix-vector product back to the column view: writing $A = \sum_j \mathbf{a}_j\mathbf{e}_j^{\mathsf{T}}$ slab by slab,

\begin{align}
A\mathbf{x} \;=\; \sum_j \mathbf{a}_j\,(\mathbf{e}_j^{\mathsf{T}}\mathbf{x}) \;=\; \sum_j x_j\,\mathbf{a}_j,
\end{align}

each slab reads off one weight and contributes one scaled column. Three ways, one product: rows to compute, columns to understand, slabs to decompose. The slab reading looks exotic and pays the deepest dividends. The projection matrix later in this chapter is a single slab. The singular value decomposition of Chapter 10 is a matrix taken apart into its slabs, largest first, and it is the closest thing this subject has to a grand finale.

## 2.3 Composition: the product of two matrices

Multiplying two matrices answers a natural question. What single action equals doing $B$, then doing $A$? This is the operation the preface's opening quiz was really about, and it now gets the full account: the definition, why it is exactly composition, and the three ways to read one product.

> **Definition 2.5 (matrix-matrix product).** The product $AB$ is the matrix whose $j$-th column is $A$ applied to the $j$-th column of $B$. It is built precisely so that $(AB)\mathbf{x} = A(B\mathbf{x})$ for every $\mathbf{x}$: the matrix of the composed transformation.

> **Claim 2.3 (composition works).** With $AB$ as defined, $(AB)\mathbf{x} = A(B\mathbf{x})$ for all $\mathbf{x}$, and matrix multiplication is associative.
>
> The one-breath reason: $B\mathbf{x}$ is a combination of $B$'s columns with recipe $\mathbf{x}$. Apply $A$, and linearity carries the recipe onto the vectors $A\mathbf{b}_j$, which are the columns of $AB$. Associativity is inherited from function composition, which never cared about parentheses.[^doublesum]

[^doublesum]: Exercise 4 writes the double sum out once for $2 \times 2$ matrices,
$\sum_k A_{ik} \left( \sum_j B_{kj} x_j \right) = \sum_j \left( \sum_k A_{ik} B_{kj} \right) x_j$,
and after that you may trust the functions.

\lensmark{algebraic} One small product, read three ways, and all three earn their display:

\begin{align}
AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
\end{align}

**Entry by entry**, each number in the answer is a row of $A$ against a column of $B$, four dot products:

\begin{align}
(AB)_{11} &= 1 \cdot 5 + 2 \cdot 7 = 19, & (AB)_{12} &= 1 \cdot 6 + 2 \cdot 8 = 22, \notag \\
(AB)_{21} &= 3 \cdot 5 + 4 \cdot 7 = 43, & (AB)_{22} &= 3 \cdot 6 + 4 \cdot 8 = 50
\end{align}

This is how everyone is taught to compute, and it is the least illuminating reading. Sixteen multiplications, no story. **Column by column**, $A$ acts on each column of $B$, exactly Definition 2.5: each column of the answer is $A$'s columns combined by that column of $B$:

\begin{align}
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 5 \\ 7 \end{bmatrix}
= 5\begin{bmatrix} 1 \\ 3 \end{bmatrix} + 7\begin{bmatrix} 2 \\ 4 \end{bmatrix}
= \begin{bmatrix} 19 \\ 43 \end{bmatrix},
\qquad
\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 6 \\ 8 \end{bmatrix}
= \begin{bmatrix} 22 \\ 50 \end{bmatrix}
\end{align}

**And slab by slab**, using Section 2.2's outer product, the answer assembles from one column of $A$ spread across one row of $B$ at a time:

\begin{align}
\begin{bmatrix} 1 \\ 3 \end{bmatrix}\begin{bmatrix} 5 & 6 \end{bmatrix} + \begin{bmatrix} 2 \\ 4 \end{bmatrix}\begin{bmatrix} 7 & 8 \end{bmatrix} = \begin{bmatrix} 5 & 6 \\ 15 & 18 \end{bmatrix} + \begin{bmatrix} 14 & 16 \\ 28 & 32 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
\end{align}

Entries to compute, columns to understand, slabs to decompose. The slab reading pays furthest ahead: Chapter 10 will take the singular value decomposition apart into exactly these rank-one pieces, largest first.

Composition is why order matters and why $AB \neq BA$ in general. And the composition this book cares about first is one you have already met by name. What is differencing, twice? Alongside the forward difference $D_f$, whose entry $i$ reads $(x_{i+1} - x_i)/h$, build the backward difference $D_b$, whose entry $i$ reads $(x_i - x_{i-1})/h$. Compose them, and the middle terms interlock:

\begin{align}
(D_b D_f\,\mathbf{x})_i
= \frac{(D_f\mathbf{x})_i - (D_f\mathbf{x})_{i-1}}{h}
= \frac{x_{i+1} - 2x_i + x_{i-1}}{h^2}
\end{align}

The stencil $1, -2, 1$ down the diagonals, divided by $h^2$. That composed matrix is the **second difference matrix** $K$, the discrete second derivative, and the hero of the tradition this book grew from.[^provenance] Listing 2.7 builds both factors, composes them, checks the composition against the stencil written directly, and applies $K$ to a sampled sine.

**Listing 2.7 (differencing twice, composed and tested)**

```python
Df = (np.eye(n, k=1) - np.eye(n)) / h    # forward
Db = (np.eye(n) - np.eye(n, k=-1)) / h   # backward
K_composed = Db @ Df
K_stencil  = (np.eye(n, k=1) - 2*np.eye(n) + np.eye(n, k=-1)) / h**2

interior = np.abs(K_composed - K_stencil)[1:-1, :].max()
err2 = np.abs((K_composed @ np.sin(x) + np.sin(x))[1:-1]).max()
print(f'composition vs stencil, interior rows: {interior:.1e}')
print(f'max |K @ sin + sin|: {err2:.6f}')
```

```text
composition vs stencil, interior rows: 0.0e+00
max |K @ sin + sin|: 0.000003
```

The composition and the stencil agree exactly away from the boundary rows, where one-sided differences run out of neighbors. And $K$ applied to a sine returns the negative of the sine, to six decimal places, which is to say $K$ knows that the second derivative of $\sin$ is $-\sin$. Two verbs, one composition, and the matrix Chapter 4 has been waiting for.

[^provenance]: The second difference matrix is the hero of Gilbert Strang's *Computational Science and Engineering*, which builds half of applied mathematics out of it. It is also where this book started. The author first met it in an independent research project in Jussi Eloranta's quantum chemistry lab at CSUN, where the Schrödinger equation for a particle in a box collapses into an eigenproblem for exactly this matrix. See Joshua Cook, *Computational Methods in Molecular Quantum Mechanics*, Leanpub, 2016.

Seeing it beats trusting a printout. Listing 2.8 plots the sine in, $K$'s output, and the negative sine dashed on top; Figure 2.5 is its output.

**Listing 2.8 (the composition, drawn)**

```python
Ks = (K_composed @ np.sin(x))[1:-1]
plt.plot(x, np.sin(x), label='input: sin(x)')
plt.plot(x[1:-1], Ks, label='output: K @ sin(x)')
plt.plot(x, -np.sin(x), 'k--', lw=1, label='-sin(x)')
plt.legend()
```

![the second difference of a sine is the negative sine](figures/fig_k_composition.png)

> **Figure 2.5.** The second difference of a sine lands on the negative sine to within the width of the line. Differentiate twice by multiplying once.

## 2.4 Diagonal matrices

\lensmark{geometric} To read a verb you watch what it does, and the probe this book uses is the preface's unit circle. Feed every direction in the catalog through the matrix and see where the catalog lands.

The first verb to watch is one Claim 2.1 already built. A **diagonal matrix** stretches each axis by its own factor, and the diagonal entries are the factors. It is the plainest verb there is, and it is nowhere near a toy. Standardizing a dataset is multiplication by a diagonal matrix (Section 2.7), and Chapter 4 will take a well-behaved matrix apart into a diagonal heart wearing a change of basis. The second verb is the one the whole book is aimed at. Listing 2.9 builds the circle and both matrices, and verifies each fate numerically before the drawing.

**Listing 2.9 (two verbs, verified)**

```python
t = np.linspace(0, 2*np.pi, 100)
circle = np.vstack([np.cos(t), np.sin(t)])
S = np.diag([2.0, 0.5])
u = np.array([2.0, 1.0])
P = np.outer(u, u) / (u @ u)   # projection onto u
ell = S @ circle
seg = P @ circle
off_line = np.abs(u[1]*seg[0] - u[0]*seg[1]).max()
print('ellipse half-axes:', ell[0].max(), ell[1].max())
print('projected circle off the u-line by:', off_line)
```

```text
ellipse half-axes: 2.0 0.5
projected circle off the u-line by: 2.220446049250313e-16
```

The stretch doubled one half-axis and halved the other, and the projection left the circle nowhere off $\mathbf{u}$'s line. Figure 2.6 draws both fates.

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=1.15]
  \begin{scope}[shift={(0,0)}]
    \draw[gray!50] (0,0) circle (1);
    \draw[thick] (0,0) ellipse (2 and 0.5);
    \draw[gray!40, ->] (-2.3,0) -- (2.4,0);
    \draw[gray!40, ->] (0,-1.3) -- (0,1.35);
    \node[anchor=north] at (0,-1.45) {\small the stretch: circle $\to$ ellipse};
  \end{scope}
  \begin{scope}[shift={(6.2,0)}]
    \draw[gray!50] (0,0) circle (1);
    \draw[gray!40, ->] (-1.5,0) -- (1.7,0);
    \draw[gray!40, ->] (0,-1.3) -- (0,1.35);
    \draw[gray!60] (-1.15,-0.575) -- (1.5,0.75);
    \draw[line width=2pt] (-0.894,-0.447) -- (0.894,0.447);
    \draw[->, thick] (0,0) -- (0.894,0.447) node[below right] {$\mathbf{u}$};
    \node[anchor=north] at (0,-1.45) {\small the projection: circle $\to$ segment};
  \end{scope}
\end{tikzpicture}
\caption{The unit circle under two verbs, drawn. The stretch turns the circle into an ellipse, doubling one axis and halving the other. The projection flattens the whole circle onto a segment of $\mathbf{u}$'s line, a first look at information kept and information discarded.}
\end{figure}

## 2.5 Projection

The stretch distorts but destroys nothing, and an inverse diagonal undoes it. The projection is different in kind. It flattens the whole circle onto a segment, and flattening forgets. That verb, the forgetful one, is the one this book runs on, so it arrives per the creed: picture first, pencil second, formula last.

\lensmark{geometric} The picture is a shadow. Stand a vector $\mathbf{v}$ near a line and drop it straight onto the line, perpendicularly, the way the noon sun drops a stick onto the ground. The landing point is $\mathbf{v}$'s shadow on the line.

\lensmark{algebraic} The pencil work needs no formula, just the preface's dot product. Project $\mathbf{v} = (3, 4)$ onto the line of $\mathbf{u} = (2, 1)$. Score $\mathbf{v}$ against $\mathbf{u}$, calibrate by $\mathbf{u}$'s own score, and stretch $\mathbf{u}$ by the result:

\begin{align}
\mathbf{u} \cdot \mathbf{v} = 6 + 4 = 10, \qquad
\mathbf{u} \cdot \mathbf{u} = 5, \qquad
\frac{10}{5}\,\mathbf{u} = (4, 2)
\end{align}

The leftover is the residual, and it comes out perpendicular:

\begin{align}
\mathbf{v} - (4, 2) = (-1, 2), \qquad
(-1, 2) \cdot (2, 1) = -2 + 2 = 0
\end{align}

\lensmark{geometric} Integer arithmetic throughout, and it draws:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.85]
  \draw[gray!60, thick] (-1.0,-0.5) -- (5.0,2.5);
  \node[gray, anchor=west] at (4.0,1.75) {\scriptsize the line of $\mathbf{u}$};
  \draw[->, very thick] (0,0) -- (3,4) node[above] {$\mathbf{v} = (3,4)$};
  \draw[->, very thick] (0,0) -- (4,2) node[below right] {$P\mathbf{v} = (4,2)$};
  \draw[dashed, thick] (3,4) -- (4,2) node[midway, above right] {$\mathbf{v} - P\mathbf{v}$};
  \draw (3.82,2.36) -- (3.64,2.45) -- (3.73,2.63);
\end{tikzpicture}
\caption{Projection by hand. The shadow $(4, 2)$ lies on the line of $\mathbf{u}$, and the residual $(-1, 2)$ runs perpendicularly from the shadow up to $\mathbf{v}$.}
\end{figure}

The shadow lies on the line. The residual runs perpendicularly from the shadow up to $\mathbf{v}$. Only now, with the picture seen and the numbers worked, does the formula arrive, and Section 2.2 already paid for its notation: the score is $\mathbf{u}^\mathsf{T}\mathbf{v}$, the calibration is $\mathbf{u}^\mathsf{T}\mathbf{u}$, and the whole verb is one slab.

> **Definition 2.6 (orthogonal projection onto a line).** The **projection** onto the line of a nonzero vector $\mathbf{u}$ sends each vector to its shadow, $P\mathbf{v} = \dfrac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}$, with matrix $P = \dfrac{\mathbf{u}\mathbf{u}^\mathsf{T}}{\mathbf{u}^\mathsf{T}\mathbf{u}}$: score, calibrate, stretch. Chapter 12 will prove the shadow is the *closest* point of the line. This chapter proves the two properties below.

The hand computation above already previewed both.

> **Claim 2.4 (what makes a projection a projection).** $P^2 = P$ (projecting twice is projecting once), and for every $\mathbf{v}$ the residual $\mathbf{v} - P\mathbf{v}$ is orthogonal to $\mathbf{u}$.
>
> The one-breath reason: $\mathbf{u}^\mathsf{T}\mathbf{u}$ is a scalar, so the inner factors of $P^2$ collapse and $P^2 = P$. And the residual's dot product with $\mathbf{u}$ cancels exactly, as the worked example just showed at desk scale.[^projalgebra]

[^projalgebra]: The two cancellations in symbols:
$P^2 = \dfrac{\mathbf{u}(\mathbf{u}^\mathsf{T}\mathbf{u})\mathbf{u}^\mathsf{T}}{(\mathbf{u}^\mathsf{T}\mathbf{u})^2} = \dfrac{\mathbf{u}\mathbf{u}^\mathsf{T}}{\mathbf{u}^\mathsf{T}\mathbf{u}} = P$,
and
$\mathbf{u}^\mathsf{T}(\mathbf{v} - P\mathbf{v}) = \mathbf{u}^\mathsf{T}\mathbf{v} - \dfrac{(\mathbf{u}^\mathsf{T}\mathbf{u})(\mathbf{u}^\mathsf{T}\mathbf{v})}{\mathbf{u}^\mathsf{T}\mathbf{u}} = 0$.

\lensmark{computational} Listing 2.10 checks both properties at machine precision.

**Listing 2.10 (the projection properties, measured)**

```python
print('P @ P == P?  max diff:', np.abs(P @ P - P).max())
v = np.array([1.0, 2.0])
print('residual . u =', (v - P @ v) @ u)
```

```text
P @ P == P?  max diff: 1.1102230246251565e-16
residual . u = -2.220446049250313e-16
```

Listing 2.11 renders the projection picture with the machine's numbers; Figure 2.8 is its output.

**Listing 2.11 (the shadow, drawn at scale)**

```python
def arrow(vec: np.ndarray, color: str, label: str) -> None:
    plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy',
               scale=1, color=color, label=label)

arrow(v, 'tab:blue', 'v')
arrow(P @ v, 'tab:green', 'Pv')
plt.plot(*zip(v, P @ v), 'k--', lw=1)
plt.legend(); plt.show()
```

![projection: the shadow and the residual](figures/fig_projection.png)

> **Figure 2.8.** The vector `v`, its shadow `Pv` on the line of `u`, and the residual `v - Pv` running perpendicularly between them.

Look at Figure 2.8 for a moment longer than it seems to deserve. A vector, its shadow inside a subspace, and a perpendicular residual. That is the drawing the preface promised as this book's destination, and it is the entire geometry of least squares in Chapter 12. The directions PCA hunts for in Chapter 11 are the lines that catch the most shadow.

The projection also does something no operator so far has done in the open: it destroys. Every vector perpendicular to $\mathbf{u}$ projects to the zero vector, an entire direction flattened to nothing. The set of everything an operator destroys is a fundamental object, and it gets its name here, at the first operator caught destroying.

> **Definition 2.7 (null space).** The **null space** of a matrix $A$ is the set of all vectors it sends to zero, every $\mathbf{x}$ with $A\mathbf{x} = \mathbf{0}$. It always contains $\mathbf{0}$ itself; anything more means the matrix maps two different inputs to one output, since $A\mathbf{x} = A(\mathbf{x} + \mathbf{z})$ whenever $A\mathbf{z} = \mathbf{0}$.

Chapter 1's two spaces now both sit inside this one operator, and it is worth saying plainly. The column space of $P$ is the line of $\mathbf{u}$, everything the projection can output. The null space of $P$ is the perpendicular line, everything the projection kills. Output space and destroyed space, reach and loss, and the next section shows that the second one decides whether an operator can ever be run backwards. Chapter 3 will measure both spaces and prove their dimensions balance.

## 2.6 The inverse

Some operators can be run backwards and some cannot, and the difference is the deepest fact in this chapter. Two definitions set it up.

> **Definition 2.8 (identity matrix).** The **identity** $I$ has ones on the diagonal and zeros elsewhere. It is the operator that changes nothing: $I\mathbf{x} = \mathbf{x}$ for every $\mathbf{x}$. Check it with Claim 2.1: it sends every $\mathbf{e}_j$ to itself, so its columns are the standard basis.

> **Definition 2.9 (inverse).** A square matrix $A$ is **invertible** when there is a matrix $A^{-1}$, the **inverse** of $A$, with $A^{-1}A = I$. Applying $A$ and then $A^{-1}$ returns every input unchanged: inversion composes with the operator to give the identity.

The difference matrix makes inversion concrete. What operation reverses taking differences? Taking running sums. \lensmark{algebraic} Watch it on one vector first:

\begin{align}
\begin{bmatrix} 1 \\ 4 \\ 9 \end{bmatrix}
\;\xrightarrow{\ \text{differences}\ }\;
\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}
\;\xrightarrow{\ \text{running sums}\ }\;
\begin{bmatrix} 1 \\ 1+3 \\ 1+3+5 \end{bmatrix}
= \begin{bmatrix} 1 \\ 4 \\ 9 \end{bmatrix}
\end{align}

Now say it in matrices, because that is where the fact actually lives. Differencing is the matrix $A_3$, running sums are the lower triangle of ones $S_3$, and the reversal is the statement $S_3 A_3 = I$:

\begin{align}
S_3 A_3 =
\begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\end{align}

Read the product by the column view: $S_3$ applied to each column of $A_3$, and each one lands on a standard basis vector. The sums collapse because consecutive differences cancel in pairs, a **telescoping sum**.[^telescope]

[^telescope]: The name comes from the collapsible telescope: each section slides into the next, and only the two ends survive. In symbols, $\sum_{i=1}^{k} (x_i - x_{i-1}) = x_k - x_0$, every interior term entering once with each sign.

> **Claim 2.5 (the inverse of differencing is summing).** The inverse of the first-difference matrix $A_3$ is the running-sum matrix $S_3$, the lower triangle of ones.
>
> The proof is the display above: $S_3 A_3 = I$, each column a telescoping sum collapsing to a standard basis vector, and Definition 2.9 asks for nothing else.

\lensmark{computational} Listing 2.12 asks NumPy for the inverse and confirms both the matrix and the roundtrip.

**Listing 2.12 (differencing, inverted)**

```python
A3 = np.array([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])
print(np.linalg.inv(A3))
b = np.array([1, 3, 5])
print('inv(A3) @ (1,3,5):', np.linalg.inv(A3) @ b)
```

```text
[[1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]]
inv(A3) @ (1,3,5): [1. 4. 9.]
```

Differentiation and integration, inverse operations, and you have known that since calculus. Here it is as two matrices multiplying to the identity, the fundamental theorem of calculus as a pair of triangles. Listing 2.13 draws the roundtrip, one panel per stage; Figure 2.9 is its output.

**Listing 2.13 (the roundtrip, drawn)**

```python
x3 = np.array([1., 4, 9])
S3 = np.linalg.inv(A3)
stages = [('x', x3), ('A3 @ x', A3 @ x3),
          ('inv(A3) @ A3 @ x', S3 @ A3 @ x3)]
fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
for ax, (name, v) in zip(axes, stages):
    ax.stem(v)
    ax.set_title(name)
```

![the roundtrip: difference, then sum](figures/fig_undo_roundtrip.png)

> **Figure 2.9.** A vector, its differences, and the running sums of those differences. The third panel is the first panel, recovered: $S_3 A_3 = I$ acting on $(1, 4, 9)$.

When does an inverse exist at all? Exactly when the operator destroys no information, and Section 2.5 built the object that measures destruction.

> **Claim 2.6 (invertibility and the null space).** A square matrix is invertible exactly when its null space is $\{\mathbf{0}\}$.
>
> If the null space holds a nonzero $\mathbf{z}$, then $A$ sends $\mathbf{x}$ and $\mathbf{x} + \mathbf{z}$ to the same output, no matrix can tell the two apart afterward, and no inverse can exist. If the null space is trivial, the columns are independent (a dependence with live weights would be a nonzero null-space vector), $n$ independent columns in $\mathbb{R}^n$ are a basis, and every target is reached by exactly one input; the map from each target back to its input is $A^{-1}$.

The projection of Section 2.5 fails this test on the spot: its null space is a whole line, so no inverse exists, and the information a projection discards is discarded forever. That one sentence is most of Part III. Estimation is what you do when the operator between you and the truth is not invertible.

## 2.7 Summary and exercises

A matrix is an operator, and this chapter read the operator completely. The verb worked first ($D$ took a derivative, row by row the difference quotient), then the property that made it possible got its name, linearity, and Claim 2.1 made the name usable: the columns are where the basis vectors land. The product carries the action, rows to compute, columns to understand (Chapter 1's combination, drawn tip to tail), and composition is matrix multiplication, read three ways and witnessed by differencing twice into $K$. Two named operators join the permanent kit: the diagonal matrix, which scales each axis independently, and the projection, idempotent with an orthogonal residual (Claim 2.4), load-bearing for Chapters 11 and 12.

The projection also destroyed a direction in the open, and the set of everything an operator destroys got its name, the null space (Definition 2.7). Inversion closed the chapter: $S_3 A_3 = I$ with each column a telescoping sum, and a square matrix has an inverse exactly when its null space is trivial (Claim 2.6), which is Chapter 1's uniqueness standing guard over information.

Chapter 3 builds the solving machine: by inspection under the license, elimination owned and read as a factorization, and the dimensions of the column space and null space proved to balance. Chapter 5 brings the matrix's second identity, the dataset. And $K$ is packed and waiting for Chapter 4, carrying a set of directions it refuses to tangle.

**Exercises**

1. *(pencil)* Compute `A3 @ x` for `x = (1, 4, 9)` both ways: rows as dot products, columns as a combination. Confirm you recover `(1, 3, 5)`.
2. *(pencil)* The shift matrix sends $\mathbf{e}_1 \to \mathbf{e}_2$, $\mathbf{e}_2 \to \mathbf{e}_3$, and $\mathbf{e}_3 \to \mathbf{0}$. Use Claim 2.1 to write it without any algebra, then say what it does to a sampled signal.
3. *(keyboard)* Build the forward-difference matrix `D` for `n = 10_000` and measure `max |D @ sin - cos|` again. The grid tightened tenfold. What happened to the error, and why does the symbolic computation of Section 2.2 predict it?
4. *(pencil)* Write out $(AB)\mathbf{x}$ and $A(B\mathbf{x})$ as double sums for $2 \times 2$ matrices and confirm they match, completing the argument of Claim 2.3. Once is enough.
5. *(pencil, then keyboard)* Compose the forward difference with itself, $D_f D_f$, by hand on a 4-vector. Compare the stencil you get to $K$'s, and explain the shift. Check yourself in code.
6. *(pencil)* Show that $P = \mathbf{u}\mathbf{u}^\mathsf{T}/(\mathbf{u}^\mathsf{T}\mathbf{u})$ is symmetric ($P^\mathsf{T} = P$), the property Claim 2.4 did not use. One line, using $(\mathbf{u}\mathbf{u}^\mathsf{T})^\mathsf{T} = \mathbf{u}\mathbf{u}^\mathsf{T}$.
7. *(pencil)* Project $(1, 5)$ onto the line of $(2, 1)$ by hand: score, calibrate, stretch, in an align of your own. Then verify the residual is orthogonal, and sketch the three arrows.
8. *(pencil)* Exhibit a nonzero vector in the null space of $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$, and describe the whole null space in one sentence. Which standing question does it kill, for which targets does the other one fail, and what does Claim 2.6 conclude about inversion?
9. *(pencil)* Write the projection matrix onto the line of $(2, 1)$ as a single slab, one outer product divided by one scalar, and confirm it matches Definition 2.6's formula entry by entry.
10. *(pencil)* Compute the null space of the projection matrix onto the line of $(2, 1)$: exhibit the direction it kills, verify $P$ sends it to zero, and conclude from Claim 2.6 whether $P$ is invertible.
11. *(keyboard, curiosity)* The two views have a speed. Time the row view against the column view of Listing 2.5 on a large random matrix, and explain the gap with the memory-address footnote of Section 2.2.
12. *(keyboard, bridge → Ch 4)* Apply `K` to a sampled sine, `np.sin(3 * x)`, and to a random vector of the same length. Compare each output to its input. Which one came back as a scaled copy of itself, and by what factor? You have just met an eigenvector, and Chapter 4 makes it official.
