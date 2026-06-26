<!-- SCAFFOLD. Write prose at each `> **BEAT:**` marker. Math, code, tables, and
     figure specs are preloaded. Code is from the course (lesson noted) unless
     marked [net-new]; [MEASURE] marks a real number to fill in. Delete BEAT
     markers as you fill them. -->

# Chapter 1: Vectors and Linear Combinations

## 1.0 In `axpy` we trust

Modern artificial intelligence rests on a single, simple operation: scale a vector by a number, and add it to another vector. That is the whole of the operation. The libraries that perform it ten billion times a second call it **axpy**, for "a x plus y." This book calls it the **linear combination**. Everything else, the layers and the attention heads and the billions of parameters and the warehouses of silicon, is structure built around this one move. The plain timber the whole edifice hangs on is axpy.

The architectures came and went, and the operation stayed. A recurrent network folded a sequence up one step at a time, and each step was a linear combination of the state so far and the next input. Then a single paper announced that attention is all you need, and attention turned out to be a weighted sum of vectors, which is to say a linear combination. The famous title decodes to something quieter: the linear combination is all you need.

That it is foundational you might take on faith. That it is also the operation your computer runs faster than almost anything else, you should not. Let me show you what I mean. 

### `numpy`

NumPy is not math in Python. Python is a high-level wrapper around C, and NumPy is a high-level wrapper around the compiled numerical libraries beneath it, BLAS chief among them, that the whole numerical stack rests on, the models we train and run included. When you write NumPy you are writing a short note that says: have the fast code do this. NumPy is the handle that lets you hold axpy at arm's length. You write `a * x + y` and stay in mathematics, while the fiddly bits, allocating the memory, walking the strides, dispatching the right kernel, calling into Fortran BLAS, happen out of sight. That is the bargain: the speed of the compiled code without having to write it.

We will compute axpy itself, on real arrays: two vectors `x` and `y` of ten million numbers, and a single scalar `a`. We compute it two ways and time both: a pure-Python list comprehension over the entries, and NumPy's vectorized expression.

```python
import time
import numpy as np

def by_hand(a, x, y):       # pure Python, a list comprehension over the entries
    return [a * xi + yi for xi, yi in zip(x, y)]

def vectorized(a, x, y):    # NumPy, the whole array at once
    return a * x + y
```

```python
a = 2.5
rng = np.random.default_rng(0)
x, y = rng.random(10_000_000), rng.random(10_000_000)

t0 = time.perf_counter(); by_hand(a, x, y)
t_loop = time.perf_counter() - t0
t0 = time.perf_counter(); vectorized(a, x, y)
t_vec = time.perf_counter() - t0

print(f'list comprehension: {t_loop:5.2f} s')
print(f'vectorized:         {t_vec * 1e3:5.0f} ms')
print(f'factor:             {t_loop / t_vec:5.0f}x')
```

```text
list comprehension:  4.34 s
vectorized:           138 ms
factor:                32x
```

Both return the same numbers; they do not take the same time. The list comprehension is dozens of times slower, and the gap only widens with `n`. A gap that large is worth chasing.

![axpy timing: loop vs vectorized](figures/fig_axpy_timing.png)

> **Figure 1.1.** Wall-clock time of `by_hand` (a pure-Python list comprehension) against `vectorized` (NumPy) for axpy, swept over `n` from a thousand to ten million, with a log x-axis and a linear y-axis. The vectorized call stays flat against the floor while the list comprehension's cost climbs away. Measured on a 4-vCPU cloud VM.

The loop is slow because Python is doing far more than arithmetic. For each of the ten million entries the interpreter resolves types, boxes and unboxes objects, checks bounds, and dispatches the operators, and only underneath all of that does it finally multiply and add. NumPy's `a * x + y` skips every bit of that per-entry overhead: the whole array goes to a compiled loop the interpreter never re-enters. That is where the gap comes from. It is a software win, not a hardware trick.

The operation that compiled loop is built around is axpy, and it is among the most carefully tuned routines in numerical computing. At the very bottom axpy is a single hardware instruction, the fused multiply-add, that modern processors run many of at once. So it is software the whole way down to one operation the silicon was built to do in a single step: scale, and add.[^alphatensor]

[^alphatensor]: DeepMind's AlphaTensor (2022) and AlphaEvolve (2025) did find faster algorithms, but for matrix *multiplication*: ways to combine many multiply-adds with fewer scalar multiplications than Strassen. The atomic axpy is not what they improved; it is already the irreducible step.

So look again at the operation we opened with. To scale a vector by a number and add it to another is to form a linear combination, and you have just watched your machine treat it as the most important thing it knows how to do. That is not a coincidence. We poured decades of engineering into axpy precisely because nearly everything we wanted to compute was built out of it. Least squares finds the combination of features closest to a price; principal component analysis finds the combinations that carry the most variation; the Kalman filter blends a prediction and a measurement into one combination and calls it an estimate. Learn to see linear combinations everywhere, and the rest of the book is commentary.

## 1.1 Two operations

> **BEAT:** Start with the geometry, first and loud. Scalar multiplication is stretching: multiply a vector by `c` and its arrow grows or shrinks along its own line through the origin, flipping to point backward when `c` is negative. Only after the picture, the algebra: every entry scales by `c`.

$$c\mathbf{v} = (cv_1, cv_2, \ldots, cv_n)$$

> **BEAT:** Geometry first again. Addition is the tip-to-tail rule: walk out along the first arrow, then along the second from where you landed, and the sum is the arrow from start to finish. Then the algebra: add entrywise.

$$\mathbf{v} + \mathbf{w} = (v_1 + w_1, \ldots, v_n + w_n)$$

```python
# L001
import matplotlib.pyplot as plt

def plot_vector(v, color='blue', label=None):
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
               color=color, label=label)

def vector_addition(v1, v2):
    plot_vector(v1, 'blue', 'v1'); plot_vector(v2, 'red', 'v2')
    plot_vector(v1 + v2, 'green', 'v1 + v2')
    plt.title('Vector Addition'); plt.legend(); plt.show()

v1 = np.array([1, 2]); v2 = np.array([3, 1])
vector_addition(v1, v2)
```

![vector addition: tip to tail](figures/fig_vector_addition.png)

> **Figure 1.2.** `vector_addition(v1, v2)`: `v1` and `v2` from the origin, with `v2` carried to the tip of `v1` (faded), and the tip-to-tail sum `v1 + v2` in green.

> **BEAT:** Combine both operations into the linear combination `c*v + d*w`; name `c, d` the weights. This is the one move. Close by posing the question that drives 1.2: as the weights range over all values, what set of vectors do we get?

$$c\mathbf{v} + d\mathbf{w}$$

## 1.2 Span and subspace

> **BEAT:** Fix `v` and `w`, let `c, d` run over all reals, collect every `c*v + d*w`. That set is the span. Same line if `v, w` are parallel; a whole plane if not. Two arrows, through nothing but scaling and adding, generate a two-dimensional space.

```python
# [net-new] all combinations of two vectors sweep out their span
v = np.array([2, 1]); w = np.array([1, 3])
C, D = np.meshgrid(np.linspace(-2, 2, 25), np.linspace(-2, 2, 25))
span = C.ravel()[:, None] * v + D.ravel()[:, None] * w   # every c*v + d*w
plt.scatter(span[:, 0], span[:, 1], s=4, alpha=0.4)
plot_vector(v, 'blue', 'v'); plot_vector(w, 'red', 'w'); plt.legend(); plt.show()
```

> **Figure 1.3** — the cloud of `c*v + d*w` filling the plane spanned by `v` and `w`.

> **BEAT:** The span is closed under both operations (scale or add things inside it, stay inside) and always contains the origin. A set with that property is a subspace. Span and subspace are two views of one object.

> **BEAT:** The data tie. In a dataset the vectors are the feature columns; the subspace they span is the column space, every vector the features can build. Forward-ref: when we fit Ames price in Ch 11, the fitted prices live in the column space, no more and no less. Estimation, stated geometrically, is picking the point of the subspace that best accounts for the measurement.

## 1.3 Independence, basis, and the recipe

> **BEAT:** Toss a third vector into a plane spanned by two. Either it lies in the plane (already a combination of them, adds nothing, dependence) or it points out (its combinations fill 3-space, independence). Define linear independence: no vector is a combination of the others; equivalently, the only combination giving the zero vector is the all-zero one.

```python
# L002 -- a dependent set: c3 is a combination of c1, c2
c1 = np.array([1, -1, 0]); c2 = np.array([0, 1, -1]); c3 = np.array([-1, 0, 1])
print("-c1 + c2:", -c1 + c2)     # -> [-1  0  1] == c3, so c3 adds nothing new

# L003 -- independence test by rank
def are_independent(vectors):
    matrix = np.column_stack(vectors)
    return np.linalg.matrix_rank(matrix) == len(vectors)

are_independent([c1, c2, c3])                                          # False
are_independent([np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1])])  # True
```

> **BEAT:** Independence tells us when a vector earns its place. A basis is an independent set that spans (nothing wasted, nothing missing), the smallest kit whose combinations build the space. Every subspace has one; all bases have the same size, the dimension.

> **BEAT:** The payoff. A basis spans, so every vector is a combination of it; it is independent, so that combination is unique. The unique weights are the coordinates. Then the standard-basis reveal:

```python
# [net-new] the list of numbers IS a linear combination of the standard basis
e1, e2, e3 = np.eye(3)
a, b, c = 5, -2, 7
print(a*e1 + b*e2 + c*e3)        # -> [5. -2. 7.] == (a, b, c)
```

> **BEAT:** `(a, b, c)` was `a*e1 + b*e2 + c*e3` all along. The list was never the vector; it was the recipe, written in a basis so familiar we forgot it was a choice. Forward-ref: in Ch 2 a matrix forms a linear combination of its columns and the input vector is the recipe. We have already met the idea.

## 1.4 Length, angle, and the dot product

> **BEAT:** We can build vectors by combining them; to estimate we must measure them. The dot product multiplies matching entries and sums, one number out.

$$\mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2 + \cdots + v_n w_n$$

```python
# L001 formulas, realized in numpy
v = np.array([3, 1]); w = np.array([2, 3])
v @ w                       # dot product
np.linalg.norm(v)           # length = sqrt(v @ v)
np.degrees(np.arccos((v @ w) / (np.linalg.norm(v) * np.linalg.norm(w))))  # angle, degrees
```

> **BEAT:** Length is `sqrt(v . v)`, the Pythagorean distance from origin to tip. The dot product is symmetric and respects linear combinations in each slot, the compatibility with scale-and-add we will use without comment.

$$\|\mathbf{v}\| = \sqrt{\mathbf{v}\cdot\mathbf{v}}, \qquad \cos\theta = \frac{\mathbf{v}\cdot\mathbf{w}}{\|\mathbf{v}\|\,\|\mathbf{w}\|}$$

> **BEAT:** Orthogonality (dot product zero). Flag it now though the payoff is chapters away: when a measurement cannot be reached by any combination of our features, the closest reachable point leaves an error orthogonal to everything reachable. That one condition is least squares (Ch 11); the same dot product on centered data is covariance (Ch 6).

## 1.5 A dataset is a matrix of vectors

> **BEAT:** One vector is one record; a dataset is many, stacked. The Ames data ships split across three files (zoning, listing, sale) joined on `Id` into one matrix. The real on-ramp: data from three sources, one matrix.

```python
# case-study 05-01 ingest
import pandas as pd
zoning  = pd.read_csv('data/zoning.csv')
listing = pd.read_csv('data/listing.csv')
sale    = pd.read_csv('data/sale.csv')          # SalePrice (the target) lives here

housing = pd.merge(zoning, listing, on='Id')
housing = pd.merge(housing, sale,   on='Id').set_index('Id')
housing.shape                                    # (1460, 80) -- 1460 homes, 80 features
```

> **BEAT:** Two readings of the matrix `X`. Across the rows: each row is a point in `R^n`, one home among all the others, the cloud from the Introduction. Down the columns: each column is a vector in `R^m`, one feature across all `m` homes.

```python
housing.loc[2]                                   # row 2: a sample (one home)
numeric = housing.select_dtypes(include='number')
numeric['GrLivArea']                             # a column: one feature over 1460 homes
```

> **BEAT:** The column reading connects to everything we built: feature columns are vectors, their span is the column space, their linear combinations are exactly the predictions a linear model can make. Note categoricals (neighborhood, roof style) become numeric vectors later (Ch 2 standardization, Ch 6 covariance). Book-wide convention: rows = samples, columns = features. Forward-ref: in Ch 2 the matrix stops being a container and becomes an action.

## 1.6 Summary and exercises

> **BEAT:** One-idea recap in your voice. A vector is a thing you scale and add; the act is the linear combination; span, subspace, basis, the recipe, the dot product, and the data matrix all fell out of taking that act seriously. End on the question the book answers: of all the linear combinations available, which one is the estimate, and how do we find it?

Exercises (seed, expand):

> **EX 1.1:** time `by_hand` vs `vectorized` axpy on your machine; explain the gap in terms of `axpy`.

> **EX 1.2:** given three vectors, decide independence two ways (by hand, then `are_independent`).

> **EX 1.3:** load Ames; report the data-matrix shape; pull one row (a home) and one column (a feature); identify which features are categorical.

> **EX 1.4:** pick two Ames numeric features; compute the angle between their centered columns; relate near-0 / near-90 degrees to correlation (forward-ref Ch 6).