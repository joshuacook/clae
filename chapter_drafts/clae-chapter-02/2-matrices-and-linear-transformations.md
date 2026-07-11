<!-- DRAFT (retrofitted to agreements/chapter-anatomy.md, 2026-07-11).
     Companion notebook: clae-code/ch02/ch02.ipynb produces every figure and
     number here. Target ~28 pp. Open with Josh: 2.5 categorical depth
     (held to one paragraph + honesty box; say the word for a one-hot demo
     cell in 2.6).
     Words: 4440 prose / 5156 total (auto: tools/wordcount.py) -->

# Chapter 2: Matrices and Linear Transformations

## 2.1 The matrix is a verb

Chapter 1 ended with a matrix full of houses: 1,460 rows, eighty columns, a container. Containers are the smaller half of the story. Multiply a matrix by a vector and the matrix does something to it: stretches it, turns it, flattens it, differentiates it. A matrix is a verb, and this chapter is about learning to read the verb.

The actions in question are exactly the ones that honor Chapter 1's contract.

> **Definition 2.1 (linear transformation).** A function $T$ from vectors to vectors is a **linear transformation** when it respects both operations at once: $T(c\mathbf{x} + d\mathbf{y}) = c\,T(\mathbf{x}) + d\,T(\mathbf{y})$ for all vectors $\mathbf{x}, \mathbf{y}$ and weights $c, d$.

In words: a linear transformation never disturbs a linear combination. Transform the ingredients and the recipe carries over untouched. The doubling map $T(\mathbf{x}) = 2\mathbf{x}$ qualifies; so does rotation about the origin; so does the derivative-taker you are about to meet. Squaring every entry does not (double the input and the output quadruples), and neither does shifting every entry by one (it moves the origin, and Section 2.5 will have to answer for that).

Here is the fact this chapter stands on, and it deserves its box early.

> **Proposition 2.2 (matrices are the linear transformations).** Every matrix gives a linear transformation via $T(\mathbf{x}) = A\mathbf{x}$, and every linear transformation on $\mathbb{R}^n$ is given by exactly one matrix: the matrix whose $j$-th column is $T(\mathbf{e}_j)$, the image of the $j$-th standard basis vector. **The columns of $A$ are where the basis vectors land.**

*Proof.* Chapter 1.3 showed that every $\mathbf{x}$ is a recipe in the standard basis: $\mathbf{x} = x_1\mathbf{e}_1 + \cdots + x_n\mathbf{e}_n$, with the entries as the weights. Apply $T$ and use linearity: $T(\mathbf{x}) = x_1 T(\mathbf{e}_1) + \cdots + x_n T(\mathbf{e}_n)$. That is a linear combination of the fixed vectors $T(\mathbf{e}_j)$ with weights $x_j$; stack those fixed vectors as the columns of a matrix $A$ and the right-hand side is $A\mathbf{x}$ by definition of the product. Conversely $\mathbf{x} \mapsto A\mathbf{x}$ is linear because combinations pass through it slotwise. ∎

Two lines, and the whole chapter falls out of them. To know a linear transformation completely, you need to know it on $n$ inputs only: the basis. Everything else is recipes. And the multiplication $A\mathbf{x}$ is not a new operation at all; it is Chapter 1's one move, a linear combination of $A$'s columns, with $\mathbf{x}$ as the recipe. The matrix is not storing its columns. It is waiting to combine them.

An enormous claim deserves a real exhibit, so here is the one that made the matrix a verb for me. A derivative, on a grid, is a matrix. Sample the interval $[0, 2\pi]$ at a thousand points a distance $h$ apart, and build the matrix that takes differences of neighbors and divides by $h$:

$$D = \frac{1}{h}\begin{bmatrix} -1 & 1 & & \\ & -1 & 1 & \\ & & \ddots & \ddots \\ & & & -1 \end{bmatrix}$$

```python
import numpy as np

n = 1000
x = np.linspace(0, 2*np.pi, n)
h = x[1] - x[0]
D = (np.eye(n, k=1) - np.eye(n)) / h   # forward difference

err = np.abs(D @ np.sin(x) - np.cos(x))[:-1].max()
print(f'max |D @ sin - cos|: {err:.4f}')
```

```text
max |D @ sin - cos|: 0.0031
```

Feed $D$ a sampled sine and it hands back the cosine, wrong in the third decimal, and the error shrinks as the grid tightens. Nothing happened here except scaling and adding: each output entry is a linear combination of two neighboring inputs. The matrix took the derivative.

![the matrix D takes a derivative](figures/fig_matrix_derivative.png)

> **Figure 2.1.** The input `sin(x)`, the output `D @ sin(x)`, and `cos(x)` dashed on top of it. The output sits on the cosine to within the width of the line.

Apply the idea twice and you get the **second difference matrix**, with $1, -2, 1$ down its diagonals: the discrete second derivative.[^provenance]

```python
K = np.eye(n, k=1) - 2*np.eye(n) + np.eye(n, k=-1)   # secondDiff
K = K / h**2
err2 = np.abs((K @ np.sin(x) + np.sin(x))[1:-1]).max()
print(f'max |K @ sin + sin|: {err2:.6f}')
```

```text
max |K @ sin + sin|: 0.000003
```

$K$ applied to a sine returns the negative of the sine, to six decimal places, which is to say $K$ knows that the second derivative of $\sin$ is $-\sin$. Hold on to $K$; it returns in Chapter 3 with a surprise in its eigenvectors.

[^provenance]: The second difference matrix is the hero of Gilbert Strang's *Computational Science and Engineering*, which builds half of applied mathematics out of it. It is also where this book started: the author first met it in an independent research project in Jussi Eloranta's quantum chemistry lab at CSUN, where the Schrödinger equation for a particle in a box collapses into an eigenproblem for exactly this matrix. See Joshua Cook, *Computational Methods in Molecular Quantum Mechanics*, Leanpub, 2016.

## 2.2 One product, two views

Chapter 1 read a data matrix two ways, across the rows and down the columns. The matrix-vector product reads two ways too, and you should be fluent in both.

> **Definition 2.3 (matrix-vector product, both views).** For an $m \times n$ matrix $A$ with columns $\mathbf{a}_1, \ldots, \mathbf{a}_n$ and rows $\mathbf{r}_1, \ldots, \mathbf{r}_m$, the product $A\mathbf{x}$ is: **by columns**, the linear combination $x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$; **by rows**, the vector whose $i$-th entry is the dot product $\mathbf{r}_i \cdot \mathbf{x}$.

Instantiate it on the small example

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}, \qquad \mathbf{x} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}.$$

By rows, each output entry is a dot product: the first row gives $1 \cdot 7 + 2 \cdot 8 = 23$, the second $3 \cdot 7 + 4 \cdot 8 = 53$, the third $5 \cdot 7 + 6 \cdot 8 = 83$. By columns, the output is one linear combination: $7(1,3,5) + 8(2,4,6) = (7, 21, 35) + (16, 32, 48) = (23, 53, 83)$. Same sixteen multiplications, same answer, different story.

> **Proposition 2.4 (the two views agree).** The row view and the column view compute the same vector.

*Proof.* Entry $i$ of the column view is $\sum_j x_j (\mathbf{a}_j)_i = \sum_j x_j A_{ij}$. Entry $i$ of the row view is $\mathbf{r}_i \cdot \mathbf{x} = \sum_j A_{ij} x_j$. The sums are identical term by term. ∎

```python
A = np.array([[1, 2], [3, 4], [5, 6]])
x = np.array([7, 8])

by_rows = np.array([row @ x for row in A])
by_cols = x[0] * A[:, 0] + x[1] * A[:, 1]
print('A @ x      :', A @ x)
print('row view   :', by_rows)
print('column view:', by_cols)
```

```text
A @ x      : [23 53 83]
row view   : [23 53 83]
column view: [23 53 83]
```

The row view is how you compute by hand, one entry at a time. The column view is how you understand: the output lives in the span of the columns, full stop, and that fact runs the rest of the book.[^memory] Most people were taught the row view and only the row view; the column view is the one worth the tuition.

[^memory]: The two views even have a memory address. NumPy stores arrays row-major, so walking a row is walking contiguous memory; pandas stores DataFrames as column blocks, so pulling a feature column is the cheap direction. Your two mental pictures of a data matrix disagree about physical layout, and each library picked a side.

### Composition

Multiplying two matrices answers a natural question: what single action equals doing $B$, then doing $A$?

> **Definition 2.5 (matrix-matrix product).** The product $AB$ is the matrix whose $j$-th column is $A$ applied to the $j$-th column of $B$. It is built precisely so that $(AB)\mathbf{x} = A(B\mathbf{x})$ for every $\mathbf{x}$: the matrix of the composed transformation.

> **Proposition 2.6 (composition works).** With $AB$ as defined, $(AB)\mathbf{x} = A(B\mathbf{x})$ for all $\mathbf{x}$, and matrix multiplication is associative.

*Sketch.* $B\mathbf{x}$ is a combination of $B$'s columns with recipe $\mathbf{x}$; apply $A$ and linearity carries the recipe onto the vectors $A\mathbf{b}_j$, which are the columns of $AB$. Associativity is then inherited from function composition, which never cared about parentheses. Write out the double sum once in your life (exercise 4); after that, trust the functions. ∎

Composition is why the order matters and why $AB \neq BA$ in general: rotate then stretch is a different verb than stretch then rotate. And composition is where a high school memory pays off. Work one rotation by hand first: the ninety-degree rotation sends $\mathbf{e}_1 = (1, 0)$ straight up to $(0, 1)$ and sends $\mathbf{e}_2 = (0, 1)$ to $(-1, 0)$, so by Proposition 2.2 its matrix is those two images stacked as columns. One picture, two columns, no algebra.

> **Proposition 2.7 (rotations compose by adding angles).** $R(a)\,R(b) = R(a+b)$ for the $2 \times 2$ rotation matrices $R(t) = \begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}$.

*Verified computationally below; exercise 5 completes the proof by direct multiplication, and the entries that fall out are the angle-sum identities.*[^trig]

```python
def R(t):
    return np.array([[np.cos(t), -np.sin(t)],
                     [np.sin(t),  np.cos(t)]])

a, b = 0.7, 0.4
print('max |R(a) @ R(b) - R(a+b)|:', np.abs(R(a) @ R(b) - R(a + b)).max())
```

```text
max |R(a) @ R(b) - R(a+b)|: 1.6653345369377348e-16
```

Zero to machine precision. The verdict: two rotations are one rotation, and the machine knew it before you multiplied anything.

[^trig]: Multiply $R(a)R(b)$ out by hand and the entries that fall out are $\cos a \cos b - \sin a \sin b$ and $\sin a \cos b + \cos a \sin b$: the angle-sum identities. The trig identity sheet you memorized in high school is one matrix multiplication, performed on the basis $\{\sin, \cos\}$. If a teacher ever showed you how the whole sheet unfolds from the angle-sum and angle-difference formulas, they were doing linear algebra to you early.

### The identity, the transpose, and the undo

Three named matrices round out the toolkit.

> **Definition 2.8 (identity matrix).** The **identity** $I$ has ones on the diagonal and zeros elsewhere; it is the verb that does nothing, $I\mathbf{x} = \mathbf{x}$. (Check it with Proposition 2.2: it sends every $\mathbf{e}_j$ to itself, so its columns are the standard basis.)

> **Definition 2.9 (transpose).** The **transpose** $A^\mathsf{T}$ swaps rows for columns: $(A^\mathsf{T})_{ij} = A_{ji}$. Its deeper meaning waits for the dot product's return in Chapter 6; for now it is notation you will see constantly.

> **Definition 2.10 (inverse).** A square matrix $A$ is **invertible** when there is a matrix $A^{-1}$ with $A^{-1}A = I$: an undo. Applying $A$ and then $A^{-1}$ is the verb that does nothing.

The difference matrix makes the inverse concrete. What undoes taking differences? Taking running sums.

> **Proposition 2.11 (the inverse of differencing is summing).** The inverse of the $3 \times 3$ first-difference matrix is the lower triangle of ones: the running-sum matrix.

*Verified below; the sketch is one word: telescoping. The $i$-th running sum of the differences of $\mathbf{x}$ collapses to $x_i$, because every intermediate term enters once with each sign.*

```python
A3 = np.array([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])  # difference
print(np.linalg.inv(A3))                            # running sums
b = np.array([1, 3, 5])
print('x = inv(A) @ (1,3,5):', np.linalg.inv(A3) @ b)
```

```text
[[1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]]
x = inv(A) @ (1,3,5): [1. 4. 9.]
```

Differentiation and integration, inverse verbs, and you have known that since calculus; here it is again as two matrices multiplying to the identity. The fundamental theorem of calculus makes a cameo as a pair of triangles.

## 2.3 Geometric effects: rotate, scale, project

To read a verb you watch what it does. Feed the same input, the unit circle, to three matrices and compare the outputs.

```python
t = np.linspace(0, 2*np.pi, 100)
circle = np.vstack([np.cos(t), np.sin(t)])
u = np.array([2.0, 1.0])
P = np.outer(u, u) / (u @ u)               # projection onto u
S = np.diag([2.0, 0.5])                    # scaling
```

![rotation, scaling, projection acting on the unit circle](figures/fig_geometric_effects.png)

> **Figure 2.2.** The unit circle under three verbs. Rotation turns it in place. Scaling stretches it into an ellipse, doubling one axis and halving the other. Projection flattens it onto a line.

Rotation preserves lengths and angles; it moves points without distorting anything. Scaling stretches each axis by its own factor; the diagonal entries are the factors. Both are useful, and both are warmups. The third panel is the one this book runs on.

> **Definition 2.12 (orthogonal projection onto a line).** The **projection** onto the line of a nonzero vector $\mathbf{u}$ sends each vector to its closest point on that line, its shadow. Its matrix is $P = \dfrac{\mathbf{u}\mathbf{u}^\mathsf{T}}{\mathbf{u}^\mathsf{T}\mathbf{u}}$.

Work one by hand before trusting the formula. Project $\mathbf{v} = (3, 4)$ onto the line of $\mathbf{u} = (2, 1)$. The recipe inside $P$ is: dot, normalize, rescale. First $\mathbf{u} \cdot \mathbf{v} = 6 + 4 = 10$ and $\mathbf{u} \cdot \mathbf{u} = 5$. The shadow is $\frac{10}{5}\mathbf{u} = 2\mathbf{u} = (4, 2)$. The leftover is $\mathbf{v} - (4, 2) = (-1, 2)$, and its dot product with $\mathbf{u}$ is $-2 + 2 = 0$. The shadow lies on the line; the leftover is perpendicular to it; integer arithmetic throughout.

That hand computation just previewed both halves of the proposition.

> **Proposition 2.13 (what makes a projection a projection).** $P^2 = P$ (projecting twice is projecting once), and for every $\mathbf{v}$ the residual $\mathbf{v} - P\mathbf{v}$ is orthogonal to $\mathbf{u}$.

*Proof.* Since $\mathbf{u}^\mathsf{T}\mathbf{u}$ is a scalar, $P^2 = \dfrac{\mathbf{u}(\mathbf{u}^\mathsf{T}\mathbf{u})\mathbf{u}^\mathsf{T}}{(\mathbf{u}^\mathsf{T}\mathbf{u})^2} = \dfrac{\mathbf{u}\mathbf{u}^\mathsf{T}}{\mathbf{u}^\mathsf{T}\mathbf{u}} = P$. For the residual, $\mathbf{u}^\mathsf{T}(\mathbf{v} - P\mathbf{v}) = \mathbf{u}^\mathsf{T}\mathbf{v} - \dfrac{(\mathbf{u}^\mathsf{T}\mathbf{u})(\mathbf{u}^\mathsf{T}\mathbf{v})}{\mathbf{u}^\mathsf{T}\mathbf{u}} = 0$. ∎

```python
print('P @ P == P?  max diff:', np.abs(P @ P - P).max())
v = np.array([1.0, 2.0])
print('residual . u =', (v - P @ v) @ u)
```

```text
P @ P == P?  max diff: 1.1102230246251565e-16
residual . u = -2.220446049250313e-16
```

![projection: the shadow and the residual](figures/fig_projection.png)

> **Figure 2.3.** The vector `v`, its shadow `Pv` on the line of `u`, and the residual `v - Pv` running perpendicularly between them. This drawing is the geometry of least squares, two hundred pages early.

Look at Figure 2.3 for a moment longer than it seems to deserve. A vector, the closest point to it inside a subspace, and a perpendicular residual: that is the entire geometry of least squares in Chapter 11, and the directions PCA hunts for in Chapter 10 are the lines that catch the most shadow. Rotation and scaling build intuition. Projection is load-bearing.

## 2.4 Systems: running the verb backwards

Every question so far ran forward: given $\mathbf{x}$, compute $A\mathbf{x}$. Estimation runs the other way. Given the output $\mathbf{b}$, what input produced it? The equation $A\mathbf{x} = \mathbf{b}$ asks, in column language: which recipe of $A$'s columns makes $\mathbf{b}$? Chapter 1 already gave the solvability condition its name. A recipe exists exactly when $\mathbf{b}$ lies in the span of the columns, the column space.

You have in fact already solved one of these by hand. The membership question of Section 1.2, is $(4, 7)$ in the span of $(2, 1)$ and $(1, 3)$, was the system

$$\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} 4 \\ 7 \end{bmatrix},$$

and the substitution you ran, $d = 4 - 2c$ into the second equation, delivered $c = 1$, $d = 2$. Solving a system is finding the recipe; you knew this maneuver before it had a matrix wrapped around it.

The difference matrix behaves perfectly. Its columns are independent, they span all of three-dimensional space, every $\mathbf{b}$ is reachable, and the recipe is unique: run the sums. For $\mathbf{b} = (1, 3, 5)$ the recipe is $\mathbf{x} = (1, 4, 9)$, as Proposition 2.11 computed. One recipe for every target is invertibility, Definition 2.10, seen from the output side.

Now change one entry and watch the behavior collapse. Make the matrix cyclic, so each output entry is a difference and the differences wrap around:

```python
C = np.array([[1, 0, -1], [-1, 1, 0], [0, -1, 1]])  # cyclic differences
print('C @ (3,3,3):', C @ np.array([3, 3, 3]))
print('rank of A3:', np.linalg.matrix_rank(A3),
      '  rank of C:', np.linalg.matrix_rank(C))
```

```text
C @ (3,3,3): [0 0 0]
rank of A3: 3   rank of C: 2
```

$C$ crushes the vector $(3, 3, 3)$ to zero, and it crushes every constant vector the same way: shift a sequence by a constant and its wrapped differences never notice. So $C$ cannot be undone; the constant is gone, and no matrix can recover information that was destroyed. The set of everything a matrix crushes deserves a name.

> **Definition 2.14 (null space).** The **null space** of $A$ is the set of all vectors it sends to zero: every $\mathbf{x}$ with $A\mathbf{x} = \mathbf{0}$.

> **Proposition 2.15 (the null space is a subspace).** For any matrix $A$, the null space of $A$ is a subspace.

*Proof.* The three checks of Proposition 1.5's pattern. $A\mathbf{0} = \mathbf{0}$, so the origin is in. If $A\mathbf{x} = \mathbf{0}$ then $A(c\mathbf{x}) = cA\mathbf{x} = \mathbf{0}$. If $A\mathbf{x} = A\mathbf{y} = \mathbf{0}$ then $A(\mathbf{x} + \mathbf{y}) = \mathbf{0} + \mathbf{0} = \mathbf{0}$. Closed both ways. ∎

For our cyclic $C$, the null space is the line of constant vectors, a one-dimensional subspace, and its existence is exactly what broke invertibility.

> **Proposition 2.16 (invertibility and the null space).** A square matrix is invertible exactly when its null space is $\{\mathbf{0}\}$.

*Sketch.* If something nonzero is crushed to zero, two different inputs share an output (add the crushed vector to any input), and no undo can tell them apart. If nothing but zero is crushed, the columns are independent; $n$ independent columns in $\mathbb{R}^n$ span everything by the dimension count of Proposition 1.11, and every target then has exactly one recipe. That assignment of recipe to target is the inverse. Chapter 11 completes the accounting alongside the other two subspaces waiting there. ∎

The geometry says the same thing in one look: $C$'s three columns lie in a common plane, so their span is that plane and not all of space. A target off the plane, $(1, 3, 5)$ for instance, has no recipe at all; a target on the plane has infinitely many, because you can slide any constant vector into $\mathbf{x}$ for free. Reach (the column space) and crush (the null space) are two sides of one accounting, and the rank computation above measures the reach: 3 of 3 for the difference matrix, 2 of 3 for the cyclic one.

One more pair of names before moving to data. When a system has more equations than unknowns, more measurements than recipe entries, it is **overdetermined**: generally nothing satisfies every equation, and the best we can do is get close. That regime is least squares, Chapter 11. When it has fewer independent directions than it has coordinates, the data is secretly lower-dimensional and the game is finding the directions that matter. That regime is principal component analysis, Chapter 10. The two regimes of estimation are the two ways $A\mathbf{x} = \mathbf{b}$ can fail to be square.

## 2.5 Standardization is a transformation

Return to the weights from Section 1.1: $51.87 per square foot of living area and $17,604 per point of overall quality. Read carelessly, quality matters three hundred times more than size. Read carefully, the comparison is meaningless. GrLivArea ranges over hundreds of square feet, OverallQual over the integers one through ten; each weight is denominated in its feature's units, and the units differ. The weights are answers to two different questions. To compare them we need the features on one shared scale, and putting them there is itself a transformation.

**Standardization** does it in two moves, column by column: subtract the mean, then divide by the standard deviation.

$$z = \frac{x - \mu}{\sigma}$$

Every standardized column is centered at zero with standard deviation one, so a step of one in any of them means the same thing: one standard deviation of that feature.

**Honesty box.** Standardization is not a linear transformation, and this book will not pretend otherwise. The scaling half is honestly linear: dividing each column by its $\sigma$ is multiplication by a diagonal matrix. But the centering half shifts every vector by a constant, and a shift moves the origin, which violates the contract's quietest clause: every linear transformation sends $\mathbf{0}$ to $\mathbf{0}$ (set $c = d = 0$ in Definition 2.1). The name for linear-plus-shift is **affine**. This is the one place in the chapter we bend the contract, we do it knowingly, and Chapter 6 will center everything in sight anyway, because covariance lives in deviations from the mean. Standardization is that chapter's front porch.

Some Ames features are words rather than numbers, neighborhood and roof style among them. Words honor the contract the same way everything else does: give each category its own **indicator column**, a one where the category holds and zeros elsewhere, and a categorical feature becomes a small block of vectors. The move is called **one-hot encoding**, and it is the contract doing its quiet work again: once a word is a vector, every tool in this book applies to it. Two consequences are planted here and paid off later. Regress a price on an indicator alone and the weight you earn is a group mean, which is Chapter 5's bridge between estimation and expectation. And a full block of indicators always sums to the all-ones vector, a built-in dependence that puts a vector in the null space of any design matrix carrying them all; that trap, and the hygiene for it, is Chapter 11 business, and you now own the vocabulary it will be settled in (Definition 2.14).

Indicators also expose a seam in standardization. An indicator is already on a natural scale: zero or one, a category flip. Divide it by its standard deviation and you wreck the interpretation for no gain. Andrew Gelman's resolution is to leave the indicators alone and move the numerics to meet them: center each numeric feature and divide by **two** standard deviations, so that a one-unit change in a scaled numeric spans a typical contrast, low to high, the same size of move as flipping an indicator.[^gelman] That gives the book its second convention, and the two leave this chapter side by side. The matrix $Z$ holds the numerics at one standard deviation, mean zero and unit scale, and feeds the covariance work of Chapters 6 and 10. The **Gelman design matrix** $X_g$ holds the numerics at two standard deviations with the indicators raw, and feeds the regressions of Chapter 11, where every coefficient will speak one currency: dollars per typical contrast.

[^gelman]: Andrew Gelman, "Scaling regression inputs by dividing by two standard deviations," *Statistics in Medicine* 27(15), 2008, pp. 2865–2873. The factor of two is not numerology: a binary variable split evenly between its two values has standard deviation one half, so a zero-to-one flip is a two-standard-deviation move. Dividing the numerics by two puts them on the indicator's scale rather than the other way around.

## 2.6 Implementation: a covariance-ready Ames, twice

The companion notebook carries the full pipeline; here are the moves that matter. Load the three Ames files, keep the complete numeric columns, and standardize the matrix in two lines:

```python
mu = X.mean().to_numpy()
sigma = X.std(ddof=0).to_numpy()
Z = (X.to_numpy(float) - mu) / sigma
print('column means after:', np.abs(Z.mean(axis=0)).max())
print('column stds after :', np.abs(Z.std(axis=0) - 1).max())
```

```text
column means after: 3.567435540277722e-14
column stds after : 2.220446049250313e-16
```

Thirty-three numeric features, all centered at zero to fourteen decimal places, all with standard deviation one to machine precision. The verification is the point: a transformation claims to put every column on one scale, so make it prove it.

![standardization before and after](figures/fig_standardization.png)

> **Figure 2.4.** Four Ames features before and after standardization. Raw, LotArea's scale makes the others invisible; standardized, all four occupy one comparable range.

Now the payoff. Rerun the regression from 1.1 on the standardized features, and the weights come back in shared units: dollars per standard deviation.

```python
w, *_ = np.linalg.lstsq(Zsub, y - y.mean(), rcond=None)
```

```text
weights, dollars per standard deviation:
  GrLivArea  :     29,344
  OverallQual:     45,415
```

The raw weights said living area dominates. The standardized weights say the opposite: one standard deviation of overall quality moves the price about $45,000, half again as much as a standard deviation of living area. Standardization did not change the model; it changed what the weights mean, from dollars per unit to dollars per typical variation, and the story inverted. This is the cheapest important lesson in applied linear algebra: before you compare weights, ask what units they are wearing.

The second convention gets built in the same breath. Scale the numerics by two standard deviations, one-hot the categorical columns, and keep the indicators raw:

```python
Xg_num = (X.to_numpy(float) - mu) / (2 * sigma)
cats = housing.select_dtypes(exclude='number')
indicators = pd.get_dummies(cats)   # every level, raw 0/1
X_g = np.column_stack([Xg_num, indicators.to_numpy(float)])
```

```text
Z  : (1460, 33)   numerics at 1 sd (covariance-ready)
X_g: (1460, 284)  numerics at 2 sd + indicators raw
```

Thirty-three numeric columns and 251 indicators: the words cost more columns than the numbers. The payoff of the two-standard-deviation move is that a regression can now mix the two kinds of feature and the coefficients still compare. Price against scaled living area, scaled quality, and the raw central-air indicator:

```python
central_air = (housing['CentralAir'] == 'Y').to_numpy(float)
Ades = np.column_stack([np.ones(len(y)), Xg_num[:, g], central_air])
w, *_ = np.linalg.lstsq(Ades, y, rcond=None)
```

```text
intercept        :    160,889
GrLivArea  (2 sd):     59,792
OverallQual(2 sd):     87,300
CentralAir (flip):     21,426
```

Read all three the same way: a typical contrast in this input moves the price by this many dollars. A typical swing in living area is worth about $60,000, in overall quality about $87,000, and having central air about $21,000. One currency, numerics and words alike. That is what $X_g$ is for.

The chapter's exit state is both matrices. $Z$: 1,460 homes, thirty-three standardized features, every column mean-zero and unit-scale, waiting for Chapter 6 to take dot products between its columns and call them covariances. $X_g$: the same homes with their words encoded, every coefficient pre-denominated in dollars per typical contrast, waiting for Chapter 11. The data is ready before the theory arrives, twice.

## 2.7 Summary and exercises

A matrix is a verb, and Proposition 2.2 is why the verb is knowable: its columns are where the basis vectors land, so multiplying by it forms a linear combination of the columns with the input as the recipe. Everything else in the chapter was learning to read what the verb does. The collection so far: differencing (a derivative), running sums (its undo, Proposition 2.11), rotation (composing by added angles, Proposition 2.7), scaling, projection (idempotent with an orthogonal residual, Proposition 2.13, and load-bearing for Chapters 10 and 11), and standardization (the affine move that makes weights comparable, bent contract disclosed). Running the verb backwards is a system $A\mathbf{x} = \mathbf{b}$: solvable exactly when the target is in the column space, uniquely when the null space is trivial (Propositions 2.15, 2.16).

You exit this chapter holding: the transformation-matrix dictionary of Proposition 2.2, both product views, five named verbs and two named inverses, the reach-and-crush accounting of column space and null space, and two data matrices, $Z$ and $X_g$, staged for Chapters 6 and 11 respectively.

Chapter 3 asks the question this chapter set up. Most verbs tangle directions together; a rotation moves every vector off itself. But some directions, for some matrices, come out of the action merely stretched. Those directions are the eigenvectors, and the second difference matrix $K$ is carrying a set of them you already know by name.

**Exercises**

1. *(pencil)* Compute `A3 @ x` for `x = (1, 4, 9)` both ways: rows as dot products, columns as a combination. Confirm you recover `(1, 3, 5)`.
2. *(pencil)* The reflection across the horizontal axis sends $(x_1, x_2)$ to $(x_1, -x_2)$. Use Proposition 2.2 to write its matrix without any algebra: where do $\mathbf{e}_1$ and $\mathbf{e}_2$ land?
3. *(keyboard)* Build the forward-difference matrix `D` for `n = 10_000` and measure `max |D @ sin - cos|` again. The grid tightened tenfold; what happened to the error, and why?
4. *(pencil)* Write out $(AB)\mathbf{x}$ and $A(B\mathbf{x})$ as double sums for $2 \times 2$ matrices and confirm they match, completing the sketch of Proposition 2.6. Once in a lifetime suffices.
5. *(pencil)* Multiply $R(a)R(b)$ symbolically and identify the trig identities that fall out, completing the proof of Proposition 2.7.
6. *(pencil)* Show that $P = \mathbf{u}\mathbf{u}^\mathsf{T}/(\mathbf{u}^\mathsf{T}\mathbf{u})$ is symmetric ($P^\mathsf{T} = P$), the property Proposition 2.13 did not use. One line, using $(\mathbf{u}\mathbf{u}^\mathsf{T})^\mathsf{T} = \mathbf{u}\mathbf{u}^\mathsf{T}$.
7. *(pencil)* Project $(1, 5)$ onto the line of $(2, 1)$ by hand: dot, normalize, rescale. Then verify the residual is orthogonal.
8. *(pencil)* Find a nonzero vector in the null space of `C` other than `(3, 3, 3)`, and describe the whole null space in one sentence.
9. *(keyboard)* Confirm computationally that `C`'s null space is one-dimensional: compute `np.linalg.matrix_rank(C)` and use rank + nullity = number of columns (take the identity on faith until Chapter 11).
10. *(keyboard)* Standardize three Ames features of your choosing and refit the 1.1 regression with all three. Which feature moves the price most per standard deviation? Did the raw weights predict that ranking?
11. *(keyboard)* Build `X_g`'s indicator block for `Neighborhood` alone with `pd.get_dummies`, and confirm the block's columns sum to the all-ones vector. You have exhibited the Chapter 11 dummy trap with your own hands; say which definition of this chapter the trap lives in.
12. *(keyboard, bridge → Ch 3)* Apply `K` to a sampled sine, `np.sin(3 * x)`, and to a random vector of the same length. Compare each output to its input: which one came back as a scaled copy of itself, and by what factor? You have just met an eigenvector; Chapter 3 makes it official.

**Further treks**

- Gilbert Strang, *Computational Science and Engineering*: the book built around $K$, and the reason this one exists. Its first chapter gives the second-difference matrix a whole life.
- Joshua Cook, *Computational Methods in Molecular Quantum Mechanics*, Leanpub, 2016: the author's own first walk through $K$'s eigenproblem, quantum flavored, racing hand-built eigensolvers against LAPACK.
- Andrew Gelman, "Scaling regression inputs by dividing by two standard deviations," *Statistics in Medicine* 27(15), 2008: the four-page argument behind $X_g$.
- Charles R. Harris et al., "Array programming with NumPy," *Nature* 585, 2020: how the array you have been multiplying actually lives in memory, from the people who built it.
