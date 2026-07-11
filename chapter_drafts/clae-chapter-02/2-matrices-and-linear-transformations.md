<!-- DRAFT (Claude, 2026-07-11) for Josh's edit, per the 2026-07-11 work order.
     Companion notebook: clae-code/ch02/ch02.ipynb produces every figure and
     number here. Two open items are PROPOSED in comments (2.3 example, 2.5
     categorical depth), not resolved. -->

# Chapter 2: Matrices and Linear Transformations

## 2.1 The matrix is a verb

Chapter 1 ended with a matrix full of houses: 1,460 rows, eighty columns, a container. Containers are the smaller half of the story. Multiply a matrix by a vector and the matrix does something to it: stretches it, turns it, flattens it, differentiates it. A matrix is a verb, and this chapter is about learning to read the verb.

Write the action as $T(\mathbf{x}) = A\mathbf{x}$: feed in a vector, get out a vector. These actions honor the contract from 1.1 exactly,

$$T(c\mathbf{x} + d\mathbf{y}) = c\,T(\mathbf{x}) + d\,T(\mathbf{y})$$

so a matrix never disturbs a linear combination; it transforms the ingredients and the recipe carries over untouched. Actions with that property are called **linear transformations**, and matrices are precisely how we write them down. You already know what the multiplication *is*, from 1.3: $A\mathbf{x}$ forms a linear combination of the columns of $A$, and $\mathbf{x}$ is the recipe. That column picture is the spine of this chapter. What is new is the reading. The matrix is not storing the columns; it is waiting to combine them.

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

Chapter 1 read a data matrix two ways, across the rows and down the columns. The matrix-vector product reads two ways too, and you should be fluent in both. Take the small example

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}, \qquad \mathbf{x} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}.$$

By rows, each output entry is a dot product: the first row gives $1 \cdot 7 + 2 \cdot 8 = 23$, and so on down. By columns, the output is one linear combination: $7$ of the first column plus $8$ of the second. Same sixteen multiplications, same answer, different story.

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

Multiplying two matrices answers a natural question: what single action equals doing $B$, then doing $A$? The answer is the matrix product $AB$, defined precisely so that $(AB)\mathbf{x} = A(B\mathbf{x})$. Composition is why the order matters and why $AB \neq BA$ in general: rotate then stretch is a different verb than stretch then rotate.

Rotations compose the way angles add, and the machine will happily confirm it:

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

$R(a)R(b) = R(a+b)$, exact to machine precision.[^trig]

[^trig]: Multiply $R(a)R(b)$ out by hand and the entries that fall out are $\cos a \cos b - \sin a \sin b$ and $\sin a \cos b + \cos a \sin b$: the angle-sum identities. The trig identity sheet you memorized in high school is one matrix multiplication, performed on the basis $\{\sin, \cos\}$. If a teacher ever showed you how the whole sheet unfolds from the angle-sum and angle-difference formulas, they were doing linear algebra to you early.

### The identity, the transpose, and the undo

Three named matrices round out the toolkit. The **identity matrix** $I$, ones down the diagonal, is the verb that does nothing: $I\mathbf{x} = \mathbf{x}$. The **transpose** $A^\mathsf{T}$ swaps rows for columns; its deeper meaning waits for the dot product's return in Chapter 6. And when an action can be undone, the undo is itself a matrix, the **inverse** $A^{-1}$, defined by $A^{-1}A = I$.

The difference matrix makes the inverse concrete. What undoes taking differences? Taking running sums.

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

The inverse of differencing is the lower triangle of ones: each output entry is the sum of all inputs so far. Differentiation and integration, inverse verbs, and you have known that since calculus; here it is again as two matrices multiplying to the identity. The fundamental theorem of calculus makes a cameo as a pair of triangles.

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

**Projection** onto the line of a vector $\mathbf{u}$ sends each point to its shadow, the closest point on the line. The matrix is built from $\mathbf{u}$ itself:

$$P = \frac{\mathbf{u}\mathbf{u}^\mathsf{T}}{\mathbf{u}^\mathsf{T}\mathbf{u}}$$

Two facts make projection special, and the machine can verify both. First, projecting twice is the same as projecting once, $P^2 = P$: once you are on the line, your shadow is you. Second, whatever projection removes is orthogonal to the line: the leftover $\mathbf{v} - P\mathbf{v}$ makes a dot product of zero with $\mathbf{u}$.

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

<!-- PROPOSAL (2.3 open item): the worked example above projects onto a generic
     line u = (2, 1). The alternative is to project onto the direction of an
     actual Ames feature column now, which lands harder but requires the
     centered-column machinery we don't have until Ch 6. Recommend keeping the
     generic line here and letting Ch 11 do the Ames projection. Josh to rule. -->

## 2.4 Systems: running the verb backwards

Every question so far ran forward: given $\mathbf{x}$, compute $A\mathbf{x}$. Estimation runs the other way. Given the output $\mathbf{b}$, what input produced it? The equation $A\mathbf{x} = \mathbf{b}$ asks, in column language: which recipe of $A$'s columns makes $\mathbf{b}$? Chapter 1 already gave the solvability condition its name. A recipe exists exactly when $\mathbf{b}$ lies in the span of the columns, the column space.

The difference matrix behaves perfectly. Its columns are independent, they span all of three-dimensional space, every $\mathbf{b}$ is reachable, and the recipe is unique: run the sums. For $\mathbf{b} = (1, 3, 5)$ the recipe is $\mathbf{x} = (1, 4, 9)$, as the inverse computed above. A matrix with this behavior, one recipe for every target, is **invertible**.

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

$C$ crushes the vector $(3, 3, 3)$ to zero, and it crushes every constant vector the same way: shift a sequence by a constant and its wrapped differences never notice. So $C$ cannot be undone; the constant is gone, and no matrix can recover information that was destroyed. The geometry says the same thing. $C$'s three columns lie in a common plane, so their span is that plane and not all of space. A target off the plane, $(1, 3, 5)$ for instance, has no recipe at all; a target on the plane has infinitely many, because you can slide any constant into $\mathbf{x}$ for free.

The two failure modes deserve their names. The **column space** of $A$ is everything the verb can reach. The **null space** is everything the verb crushes to zero: for $C$, the line of constant vectors. Invertibility is the clean case, full reach and nothing crushed, and the rank computation above measures it: rank 3 of 3 possible for the difference matrix, rank 2 for the cyclic one. There is a richer taxonomy here, four subspaces with a beautiful symmetry, and it belongs to Chapter 11; this much is what Chapter 2 needs.

One more pair of names before moving to data. When a system has more equations than unknowns, more measurements than recipe entries, it is **overdetermined**: generally nothing satisfies every equation, and the best we can do is get close. That regime is least squares, Chapter 11. When it has fewer independent directions than it has coordinates, the data is secretly lower-dimensional and the game is finding the directions that matter. That regime is principal component analysis, Chapter 10. The two regimes of estimation are the two ways $A\mathbf{x} = \mathbf{b}$ can fail to be square.

## 2.5 Standardization is a transformation

Return to the weights from Section 1.1: $51.87 per square foot of living area and $17,604 per point of overall quality. Read carelessly, quality matters three hundred times more than size. Read carefully, the comparison is meaningless. GrLivArea ranges over hundreds of square feet, OverallQual over the integers one through ten; each weight is denominated in its feature's units, and the units differ. The weights are answers to two different questions. To compare them we need the features on one shared scale, and putting them there is itself a transformation.

**Standardization** does it in two moves, column by column: subtract the mean, then divide by the standard deviation.

$$z = \frac{x - \mu}{\sigma}$$

Every standardized column is centered at zero with standard deviation one, so a step of one in any of them means the same thing: one standard deviation of that feature. The scaling half is an honest linear transformation, a diagonal matrix with $1/\sigma_j$ down the diagonal. The centering half is a shift, and a shift is not linear: it moves the origin, which no matrix can do. The bookkeeping term for linear-plus-shift is **affine**, and this is the one place in the chapter we bend the contract knowingly. Chapter 6 will center everything in sight anyway, because covariance lives in deviations from the mean; standardization is that chapter's front porch.

Some Ames features are words rather than numbers, neighborhood and roof style among them. The standard move is **one-hot encoding**: give each category its own indicator column, a one where the category holds and zeros elsewhere, so a categorical feature becomes a small block of vectors. We will encode them when a computation actually needs them, and not before.

<!-- PROPOSAL (2.5 open item): categorical handling is held to this one
     paragraph, per the source map's "lean minimal" recommendation. If Josh
     wants the one-hot block shown on real Ames columns (Neighborhood is the
     natural demo), it fits in 2.6 as one cell. Josh to rule. -->

## 2.6 Implementation: a covariance-ready Ames

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

The chapter's exit state is the matrix `Z`: 1,460 homes, thirty-three standardized features, every column mean-zero and unit-scale. Chapter 6 will take dot products between its columns and call them covariances. The data is ready before the theory arrives.

## 2.7 Summary and exercises

A matrix is a verb. Multiplying by one forms a linear combination of its columns, with the input as the recipe, and everything else in the chapter was learning to read what the verb does. The collection so far: differencing (a derivative), running sums (its undo), rotation, scaling, projection (the load-bearing one, idempotent, orthogonal residual), and standardization (the affine move that makes weights comparable). Running the verb backwards is a system $A\mathbf{x} = \mathbf{b}$, solvable exactly when the target is in the column space, uniquely when nothing is crushed to zero.

Chapter 3 asks the question this chapter set up. Most verbs tangle directions together; a rotation moves every vector off itself. But some directions, for some matrices, come out of the action merely stretched. Those directions are the eigenvectors, and the second difference matrix $K$ is carrying a set of them you already know by name.

**Exercises**

1. Compute `A3 @ x` for `x = (1, 4, 9)` by hand, both ways: rows as dot products, columns as a combination. Confirm you recover `(1, 3, 5)`.
2. Build the forward-difference matrix `D` for `n = 10_000` and measure `max |D @ sin - cos|` again. The grid halved; what happened to the error, and why?
3. Verify by hand that $R(a)R(b) = R(a+b)$ for the two-by-two rotation matrices, and identify which trig identities fall out of the multiplication.
4. Show that `P = np.outer(u, u) / (u @ u)` satisfies `P @ P == P` algebraically, not just numerically. One line, using $\mathbf{u}^\mathsf{T}\mathbf{u}$ being a scalar.
5. Find a nonzero vector in the null space of `C` other than `(3, 3, 3)`, and describe the null space in one sentence.
6. Standardize three Ames features of your choosing and refit the 1.1 regression with all three. Which feature moves the price most per standard deviation? Did the raw weights predict that ranking?
