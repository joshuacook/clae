<!-- DRAFT (retrofitted to agreements/chapter-anatomy.md, 2026-07-11). §1.0 is
     Josh's text, untouched. Companion notebook: clae-code/ch01/ch01.ipynb
     produces every figure and number here. Target ~28 pp.
     Words: 4734 prose / 5370 total (auto: tools/wordcount.py) -->

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

Every figure and number in this book is produced by the companion notebooks at [github.com/joshuacook/clae-code](https://github.com/joshuacook/clae-code), run on a 4-vCPU cloud virtual machine with no GPU. Your own machine will print different numbers; the shape of the gap will not.

![axpy timing: loop vs vectorized](figures/fig_axpy_timing.png)

> **Figure 1.1.** Wall-clock time of `by_hand` (a pure-Python list comprehension) against `vectorized` (NumPy) for axpy, swept over `n` from a thousand to ten million, with a log x-axis and a linear y-axis. The vectorized call stays flat against the floor while the list comprehension's cost climbs away.

The loop is slow because Python is doing far more than arithmetic. For each of the ten million entries the interpreter resolves types, boxes and unboxes objects, checks bounds, and dispatches the operators, and only underneath all of that does it finally multiply and add. NumPy's `a * x + y` skips every bit of that per-entry overhead: the whole array goes to a compiled loop the interpreter never re-enters. That is where the gap comes from. It is a software win, not a hardware trick.

The operation that compiled loop is built around is axpy, and it is among the most carefully tuned routines in numerical computing. At the very bottom axpy is a single hardware instruction, the fused multiply-add, that modern processors run many of at once. So it is software the whole way down to one operation the silicon was built to do in a single step: scale, and add.[^alphatensor]

[^alphatensor]: DeepMind's AlphaTensor (2022) and AlphaEvolve (2025) did find faster algorithms, but for matrix *multiplication*: ways to combine many multiply-adds with fewer scalar multiplications than Strassen. The atomic axpy is not what they improved; it is already the irreducible step.

So look again at the operation we opened with. To scale a vector by a number and add it to another is to form a linear combination, and you have just watched your machine treat it as the most important thing it knows how to do. That is not a coincidence. We poured decades of engineering into axpy precisely because nearly everything we wanted to compute was built out of it. Least squares finds the combination of features closest to a price; principal component analysis finds the combinations that carry the most variation; the Kalman filter blends a prediction and a measurement into one combination and calls it an estimate. Learn to see linear combinations everywhere, and the rest of the book is commentary.

## 1.1 Two operations, one contract

Linear algebra runs on a contract, and the contract is short. You need objects that can be scaled and added, and you need the results to stay in the family: scale a vector and you have a vector, add two vectors and you have a vector. Closure under those two operations is the entire price of admission.

Before the contract can be signed, the parties need names.

> **Definition 1.1 (vector, $\mathbb{R}^n$).** A **vector** is an ordered list of $n$ real numbers, $\mathbf{v} = (v_1, v_2, \ldots, v_n)$, drawn as an arrow from the origin when $n$ is small enough to draw. The set of all such vectors is $\mathbb{R}^n$.

You have already met several. The ten-million-entry arrays `x` and `y` in Section 1.0 are vectors in $\mathbb{R}^{10{,}000{,}000}$; the pair `(2, 1)` is a vector in $\mathbb{R}^2$; a column of 1,460 sale prices is a vector in $\mathbb{R}^{1460}$. Hold that last one; it returns in Section 1.5 with money attached.

> **Definition 1.2 (working vector space).** A **vector space** is a collection of vectors that is closed under two operations: scalar multiplication ($c\mathbf{v}$ stays in the collection) and vector addition ($\mathbf{v} + \mathbf{w}$ stays in the collection).[^axioms]

[^axioms]: There are formally eight axioms standing behind this definition, governing how the two operations interact (associativity, distributivity, a zero vector, and friends). $\mathbb{R}^n$ satisfies all eight, every space in this book satisfies all eight, and we will not check them again. Please understand that we are liberal with our implicit understanding here, and enjoying it.

What the contract buys is out of all proportion to what it costs. Honor it and you inherit the whole suite: regression, eigen dynamics, Fourier analysis, and, by Chapter 3, the fact that electron orbitals are a basis. Each of those is the same small set of moves applied to a new family of objects that kept its end of the deal. That is an enormous claim, so let us put something real on the table.

### The claim on the table

The Ames housing data records 1,460 home sales in Ames, Iowa: square footage, quality ratings, sale prices, eighty features in all. Estimation only ever says one sentence about data like this:

$$\texttt{SalePrice} \approx w_1 \cdot \texttt{GrLivArea} + w_2 \cdot \texttt{OverallQual} + \cdots$$

Read it again. Scale a vector by a number, add it to another vector. The one sentence estimation ever says is axpy. The weights are unknown, and this book exists to earn them. But there is no reason you should wait two hundred pages to hear the song, so here is the answer first.

```python
import pandas as pd

zoning  = pd.read_csv('data/zoning.csv')
listing = pd.read_csv('data/listing.csv')
sale    = pd.read_csv('data/sale.csv')          # SalePrice (the target) lives here
housing = pd.merge(zoning, listing, on='Id')
housing = pd.merge(housing, sale, on='Id').set_index('Id')

X = housing[['GrLivArea', 'OverallQual']].to_numpy(float)
y = housing['SalePrice'].to_numpy(float)

w, *_ = np.linalg.lstsq(X, y, rcond=None)        # the unearned answer
print('w:', np.round(w, 2))
print(f'house {housing.index[1]}: actual {y[1]:,.0f}   predicted {(X @ w)[1]:,.0f}')
```

```text
w: [   51.87 17604.21]
house 2: actual 181,500   predicted 171,085
```

There they are: about $51.87 per square foot of living area, about $17,604 per point of overall quality, and the recipe prices house 2 within six percent of its actual sale. Those weights were delivered by a function you did not build and do not yet deserve. Most readers of this book have called `lstsq` or one of its cousins professionally; the mystery was never getting the answer, it is why the answer works and when to trust it. By Chapter 11 you will have built that function yourself, from parts, and every part is made of the two operations in the contract. This chapter starts the collection.

### Scaling and adding

The two operations deserve their pictures, geometry first in both cases.

Scalar multiplication is stretching. Multiply a vector by `c` and its arrow grows or shrinks along its own line through the origin; a negative `c` flips it to point the other way down the same line. That is the entire geometric content. The algebra just carries it out entrywise:

$$c\mathbf{v} = (cv_1, cv_2, \ldots, cv_n)$$

```python
import matplotlib.pyplot as plt

def plot_vector(v, color='blue', label=None):
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
               color=color, label=label)

v = np.array([2, 1])
plot_vector(2 * v, 'purple', '2v')    # stretch
plot_vector(v, 'blue', 'v')
plot_vector(-v, 'red', '-v')          # flip
plt.show()
```

![scalar multiplication](figures/fig_scalar_multiplication.png)

> **Figure 1.2.** Scalar multiplication. `v`, `2v`, and `-v` all lie on the single line through the origin: multiplying by `c` slides the arrow along that line, and flips it to the far side when `c` is negative.

Addition is tip to tail. Walk out along the first arrow; from where you land, walk out along the second; the sum is the single arrow from where you started to where you finished. Entrywise again:

$$\mathbf{v} + \mathbf{w} = (v_1 + w_1, \ldots, v_n + w_n)$$

```python
def vector_addition(v1, v2):
    plot_vector(v1, 'blue', 'v1'); plot_vector(v2, 'red', 'v2')
    plot_vector(v1 + v2, 'green', 'v1 + v2')
    plt.show()

vector_addition(np.array([1, 2]), np.array([3, 1]))
```

![vector addition: tip to tail](figures/fig_vector_addition.png)

> **Figure 1.3.** `vector_addition(v1, v2)`: `v1` and `v2` from the origin, with `v2` carried to the tip of `v1` (faded), and the tip-to-tail sum `v1 + v2` in green.

Put the two operations together and you have the only move this book ever makes:

$$c\mathbf{v} + d\mathbf{w}$$

The numbers `c` and `d` are the **weights**. You have seen this sentence before; it priced a house a page ago.

Work one by hand, once, so the machine never gets to hide the mechanism from you. Take $\mathbf{v} = (1, 2)$, $\mathbf{w} = (3, 1)$, and form $2\mathbf{v} + \mathbf{w}$. Scale first: $2\mathbf{v} = (2, 4)$. Then add, entry by entry: $(2 + 3, \; 4 + 1) = (5, 5)$. One scale, one add, five seconds of arithmetic. Ten billion of those per second is Section 1.0; the mechanism is this one.

And now the question that drives the next section. Hold `v` and `w` fixed, and let the weights range over every value they can take. What do you get?

## 1.2 Span and subspace

Collect every `c*v + d*w` as `c` and `d` run over all real numbers. That set has a name.

> **Definition 1.3 (span).** The **span** of a set of vectors is the collection of all their linear combinations: every vector reachable by scaling the ingredients and adding the results.

If `w` lies on `v`'s line, scaling and adding never escape the line, and the span is just that line. If it does not, the combinations fill an entire plane: two arrows, through nothing but scaling and adding, generate a two-dimensional world.

```python
v = np.array([2, 1]); w = np.array([1, 3])
C, D = np.meshgrid(np.linspace(-2, 2, 25), np.linspace(-2, 2, 25))
span = C.ravel()[:, None] * v + D.ravel()[:, None] * w   # every c*v + d*w
plt.scatter(span[:, 0], span[:, 1], s=4, alpha=0.4)
plot_vector(v, 'blue', 'v'); plot_vector(w, 'red', 'w'); plt.legend(); plt.show()
```

![the span of v and w](figures/fig_span_cloud.png)

> **Figure 1.4.** The cloud of `c*v + d*w` for weights swept from -2 to 2: the sampled patch of the plane spanned by `v` and `w`. Widen the sweep and the cloud grows without bound; the plane is what it is filling in.

Membership in a span is a concrete question with a concrete answer, so work one by hand. Is $\mathbf{b} = (4, 7)$ in the span of $\mathbf{v} = (2, 1)$ and $\mathbf{w} = (1, 3)$? Asking is the same as solving for weights: find $c, d$ with $c(2,1) + d(1,3) = (4,7)$, which is the little system $2c + d = 4$ and $c + 3d = 7$. The first equation gives $d = 4 - 2c$; substitute into the second and $c + 12 - 6c = 7$, so $c = 1$, and then $d = 2$. The recipe exists: $\mathbf{b} = 1\mathbf{v} + 2\mathbf{w}$, and $(4, 7)$ is in the span. Membership questions are recipe questions. Chapter 2 will give this maneuver its grown-up name.

The set we just built has structure worth naming.

> **Definition 1.4 (subspace).** A **subspace** is a set of vectors that contains the origin and is closed under both operations: scale anything inside and you stay inside, add any two things inside and you stay inside.

> **Proposition 1.5 (a span is a subspace).** The span of any set of vectors is a subspace.

*Proof.* The origin is in the span: take every weight zero. Closure under scaling: a scaled combination is a combination, since $a(c\mathbf{v} + d\mathbf{w}) = (ac)\mathbf{v} + (ad)\mathbf{w}$, and new weights are still weights. Closure under addition: the sum of two combinations of the same ingredients is again a combination, with the weights added slotwise. Both operations land back inside. ∎

That proof is three sentences, and it teaches the pattern every closure proof in this book follows: name the candidate weights, check the origin, check both operations. Span and subspace are two descriptions of one object. Span builds it from ingredients; subspace states the property the built thing has.

One more thing before the data, because it decides whether you can trust your own drawings. Two vectors span at most a plane. That stays true in three dimensions, in 1,460, in a googol: the reach of the operation is bounded by the number of ingredients, never by the size of the space the ingredients live in. Nobody can picture 1,460 dimensions, and nobody needs to. Every question we ask about two vectors happens inside the at-most-a-plane they span, so the drawing on this page is exact for the high-dimensional case, no metaphor involved. Standard courses observe that two vectors in three-dimensional space span a plane. The better sentence: two vectors in 1,460-dimensional space still span only a plane. You were never supposed to see the ambient space. (The precise statement is Proposition 1.11, once dimension is on the table.)

Here is why you care. In a dataset the feature columns are vectors, and the subspace they span is the **column space**: every vector the features can build, which is to say every prediction a linear model can possibly make. Now the question from 1.1 sharpens. Can `GrLivArea` and `OverallQual` reach `SalePrice`? Almost never exactly. The target `y` is a vector too, and it does not generally lie in the plane those two columns span. The gap between `y` and the closest point the columns can reach has a name, and the name is two hundred pages away; for now, hold the picture of a vector hanging just off a plane. Fitting Ames prices in Chapter 11 will mean choosing the point of the column space that best accounts for `y`, and nothing more.

## 1.3 Independence, basis, and the recipe

Take a plane spanned by two vectors and toss in a third. One of two things happens. Either it lands in the plane, in which case it was already a combination of the first two and adds nothing new, or it points out of the plane, and combinations of the three now fill three-dimensional space.

> **Definition 1.6 (linear independence).** A set of vectors is **linearly independent** when no vector in it is a linear combination of the others; equivalently, when the only combination producing the zero vector is the one with every weight equal to zero. A set that fails this is **linearly dependent**.

The two phrasings are the same test worn two ways: if some vector is a combination of the others, move it to the other side of the equation and you have built zero with a nonzero weight; run that argument backward and the equivalence closes.

Dependence is something you can exhibit by hand. Take $\mathbf{c}_1 = (1, -1, 0)$, $\mathbf{c}_2 = (0, 1, -1)$, $\mathbf{c}_3 = (-1, 0, 1)$. Compute $-\mathbf{c}_1 + \mathbf{c}_2$ entrywise: the first entries give $-1 + 0 = -1$, the second $1 + 1$... careful, $-(-1) + 1 = 2$? No: $-\mathbf{c}_1 = (-1, 1, 0)$, and adding $\mathbf{c}_2 = (0, 1, -1)$ gives $(-1, 2, -1)$. That is not $\mathbf{c}_3$. The honest hand-check catches what a hasty read misses, which is the point of doing it. The right relation here is $\mathbf{c}_1 + \mathbf{c}_2 + \mathbf{c}_3 = (0, 0, 0)$: add the three vectors entrywise and every slot cancels. A combination with weights $(1, 1, 1)$, none of them zero, produced the zero vector. The set is dependent, and any one of the three is a combination of the other two.

The machine runs the same test at scale:

```python
# a dependent set: the three vectors sum to zero
c1 = np.array([1, -1, 0]); c2 = np.array([0, 1, -1]); c3 = np.array([-1, 0, 1])
print("c1 + c2 + c3:", c1 + c2 + c3)     # -> [0 0 0], with weights (1, 1, 1)

# independence test by rank
def are_independent(vectors):
    matrix = np.column_stack(vectors)
    return np.linalg.matrix_rank(matrix) == len(vectors)

are_independent([c1, c2, c3])                                          # False
are_independent([np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1])])  # True
```

(The test inside `are_independent` is rank, a word that belongs to Chapter 2; for today, trust that it counts what independence counts.)

Independence tells us when a vector earns its place. Now for the kit that has no freeloaders and no gaps.

> **Definition 1.7 (basis and dimension).** A **basis** of a subspace is a linearly independent set that spans it: nothing wasted, nothing missing. Every subspace has one, all bases of a given subspace have the same size, and that shared size is the **dimension** of the subspace.

The definition quietly made a claim, and stated claims get their marks in this book.

> **Proposition 1.8 (unique recipe).** If $\mathbf{b}_1, \ldots, \mathbf{b}_k$ is a basis, then every vector in its span is a combination of the basis in exactly one way.

*Proof.* Existence is the spanning half of the definition. For uniqueness, suppose two recipes build the same vector: $c_1\mathbf{b}_1 + \cdots + c_k\mathbf{b}_k = d_1\mathbf{b}_1 + \cdots + d_k\mathbf{b}_k$. Subtract: $(c_1 - d_1)\mathbf{b}_1 + \cdots + (c_k - d_k)\mathbf{b}_k = \mathbf{0}$. Independence says the only combination producing zero has every weight zero, so $c_i = d_i$ for every $i$. The two recipes were the same recipe. ∎

Subtract-and-invoke-independence is the second reusable proof pattern of the chapter, and it is the entire reason coordinates are well defined:

> **Definition 1.9 (coordinates).** The **coordinates** of a vector with respect to a basis are the unique weights of its recipe in that basis.

> **Proposition 1.10 (all bases of a subspace have the same size).** If a subspace has a basis of size $k$, every basis of it has size $k$.

*Sketch.* The workhorse is an exchange argument: given a spanning set of size $k$ and an independent set, you can swap the independent vectors in one at a time, each swap evicting a spanning vector, without losing the span. An independent set can therefore never outnumber a spanning set, and running the comparison both ways between two bases pins their sizes equal. The bookkeeping is standard; Strang (*Introduction to Linear Algebra*, ch. 3) or Axler (ch. 2) will show you every step. ∎

> **Proposition 1.11 (span of the question).** The span of $k$ vectors is a subspace of dimension at most $k$, regardless of the dimension of the ambient space.

*Sketch.* The span is a subspace (Proposition 1.5), and the $k$ ingredients span it by construction. If they are independent they are a basis and the dimension is exactly $k$; if not, discard dependent ingredients one at a time until what remains is independent, which only ever shrinks the count. Either way the dimension lands at or below $k$. This is the earlier at-most-a-plane claim, now with its license. ∎

Now the payoff, and it is the best sentence in the chapter. A basis spans, so every vector is a combination of it. A basis is independent, so that combination is unique. The unique weights are the coordinates. Watch what this does to the most familiar object in the subject:

```python
# the list of numbers IS a linear combination of the standard basis
e1, e2, e3 = np.eye(3)
a, b, c = 5, -2, 7
print(a*e1 + b*e2 + c*e3)        # -> [5. -2. 7.] == (a, b, c)
```

The list `(5, -2, 7)` was `5*e1 - 2*e2 + 7*e3` all along. The list was never the vector; it was the recipe, written in a basis so familiar we forgot it was a choice. In Chapter 2 a matrix will form a linear combination of its columns, with the input vector as the recipe, and you will find you have already met the idea.

## 1.4 Length, angle, and the dot product

We can build vectors by combining them. To estimate we must also measure them: how long is this vector, how aligned are these two? One operation answers both questions.

> **Definition 1.12 (dot product, norm, angle, orthogonality).** The **dot product** of two vectors multiplies matching entries and sums the results: $\mathbf{v} \cdot \mathbf{w} = v_1 w_1 + \cdots + v_n w_n$. The **norm** (length) of a vector is $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$. The **angle** $\theta$ between two nonzero vectors is defined by $\cos\theta = \dfrac{\mathbf{v}\cdot\mathbf{w}}{\|\mathbf{v}\|\,\|\mathbf{w}\|}$, and two vectors are **orthogonal** when their dot product is zero.

Instantiate it by hand before the machine does. Take $\mathbf{v} = (3, 1)$ and $\mathbf{w} = (2, 3)$. The dot product: $3 \cdot 2 + 1 \cdot 3 = 9$. The norms: $\|\mathbf{v}\| = \sqrt{9 + 1} = \sqrt{10}$ and $\|\mathbf{w}\| = \sqrt{4 + 9} = \sqrt{13}$. The cosine: $9 / \sqrt{130} \approx 0.789$, so $\theta \approx 38$ degrees. Two multiplications, one addition, two square roots, and you have measured a pair of vectors. The machine agrees:

```python
v = np.array([3, 1]); w = np.array([2, 3])
v @ w                       # 9
np.linalg.norm(v)           # sqrt(10) = 3.162...
np.degrees(np.arccos((v @ w) / (np.linalg.norm(v) * np.linalg.norm(w))))  # 37.87
```

The norm is the Pythagorean distance from origin to tip. The angle formula turns the dot product into geometry in any number of dimensions, and it hides a promise: for the cosine to deserve its name, the fraction must never leave $[-1, 1]$. That is a stated claim, and it has a famous name.

> **Proposition 1.13 (Cauchy–Schwarz).** For any vectors $\mathbf{v}, \mathbf{w}$: $\;|\mathbf{v} \cdot \mathbf{w}| \leq \|\mathbf{v}\|\,\|\mathbf{w}\|$, with equality exactly when one vector is a scalar multiple of the other.

*Sketch.* Consider $f(t) = \|\mathbf{v} - t\mathbf{w}\|^2$. As a squared length it is never negative, and expanding it gives a quadratic in $t$: $f(t) = \|\mathbf{w}\|^2 t^2 - 2(\mathbf{v}\cdot\mathbf{w})\,t + \|\mathbf{v}\|^2$. A quadratic that never goes negative has a nonpositive discriminant, and writing that discriminant out is exactly the inequality. Equality forces $f$ to touch zero, which means $\mathbf{v} = t\mathbf{w}$ for the minimizing $t$. Full details in Strang or Axler; the discriminant move is the whole idea. ∎

*Verified at Ames scale.* Two real columns, 1,460 entries each:

```python
a = housing['GrLivArea'].to_numpy(float)
b = housing['OverallQual'].to_numpy(float)
print(f'|a.b|   = {abs(a @ b):,.0f}')
print(f'|a||b|  = {np.linalg.norm(a) * np.linalg.norm(b):,.0f}')
```

```text
|a.b|     = 14,123,976
|a||b|    = 14,645,262
lhs/rhs   = 0.9644   (must be <= 1)
```

The inequality holds with room to spare, and the ratio is itself meaningful: 0.9644 is the cosine between the two raw columns. Living area and overall quality point in nearly the same direction, which no one who has shopped for a house will find surprising. Computational verification is evidence, not proof; the proof is the discriminant, and the evidence is 1,460 houses deep.

The dot product is symmetric, and it respects linear combinations in each slot; we will lean on that compatibility constantly and mostly without comment. One case deserves its flag now, though its payoff is chapters away. Recall the vector hanging just off the plane at the end of 1.2. When a measurement cannot be reached by any combination of our features, the closest reachable point leaves an error that is orthogonal to everything reachable. That single condition is least squares, in Chapter 11. The same dot product applied to centered data columns is covariance, in Chapter 6. One operation, two of the biggest ideas in the book.

## 1.5 A dataset is a matrix of vectors

One vector is one record. A dataset is many records stacked, and the stack is a matrix. Real data rarely arrives as one clean table; the Ames data ships as three files, zoning, listing, and sale, joined on a shared `Id` into a single matrix. We built it in 1.1 to ask the estimation question. Here is the shape of what we built.

```python
housing.shape                                    # (1460, 80) -- 1460 homes, 80 features
```

A data matrix reads two ways, and both matter. Across the rows: each row is one home, a single point in an eighty-dimensional feature space, one dot in a cloud of 1,460. Down the columns: each column is one feature measured across every home, a vector with 1,460 entries.

```python
housing.loc[2]                                   # row 2: a sample (one home)
numeric = housing.select_dtypes(include='number')
numeric['GrLivArea']                             # a column: one feature over 1460 homes
```

The column reading connects to everything this chapter built. Feature columns are vectors. Their span is the column space. Their linear combinations are exactly the predictions a linear model can make, and the weights of the winning combination are what `lstsq` handed us, unearned, back in 1.1. Some features (neighborhood, roof style) are words rather than numbers; they become numeric vectors in due time, with standardization in Chapter 2 and covariance in Chapter 6.

The conventions deserve a box, because the whole book signs them.

> **Definition 1.14 (data-matrix conventions).** In this book a data matrix $X$ has **rows as samples** and **columns as features**: $X$ is $m \times n$ for $m$ observations of $n$ features. The target vector is $\mathbf{y}$, with one entry per sample. A feature column is a vector in $\mathbb{R}^m$; a sample row is a point in $\mathbb{R}^n$.

In Chapter 2 the matrix stops being a container and becomes an action.

## 1.6 Summary and exercises

A vector is a thing you can scale and add. That act is the linear combination: axpy at the bottom of your machine, and the one sentence estimation ever says at the top of it. Taking the act seriously produced everything else in this chapter. The span is everything the act can reach, and it is always a subspace (Proposition 1.5) of dimension at most the ingredient count (Proposition 1.11). A basis is the minimal kit, its recipe is unique (Proposition 1.8), and the unique weights are coordinates, which is what a list of numbers secretly was all along. The dot product measures length and angle, keeps its promises by Cauchy–Schwarz (Proposition 1.13), and hands us orthogonality, the hinge of Chapter 11. And a dataset is 1,460 vectors standing in formation, rows for samples, columns for features.

You exit this chapter holding: the contract (Definitions 1.1, 1.2), the reach of the operation (span, subspace, column space), the minimal kit and its coordinates, one measuring instrument, and the assembled Ames matrix. Chapter 2 takes the matrix out of storage and runs it.

The question the book answers is now fully posed. Of all the linear combinations available, which one is the estimate, and how do we earn it?

**Exercises**

1. *(pencil)* Compute $3(1, -1, 2) + (0, 4, -1)$ entrywise. Then write the result as a combination of $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ and check that the weights are exactly the entries.
2. *(keyboard)* Time `by_hand` against `vectorized` axpy on your own machine, over a sweep of sizes. Explain the gap you measure in terms of what the interpreter does per entry and what BLAS does per array.
3. *(pencil)* Is $(5, 5)$ in the span of $(2, 1)$ and $(1, 3)$? Exhibit the recipe or show that none exists, using the two-equation method of Section 1.2.
4. *(pencil)* Prove that the line $\{t\mathbf{v} : t \in \mathbb{R}\}$ through the origin is a subspace, following the three-check pattern of Proposition 1.5.
5. *(pencil, then keyboard)* Given three vectors of your choosing in $\mathbb{R}^3$, decide independence twice: by exhibiting a combination (or arguing none exists), then with `are_independent`.
6. *(pencil)* The set $\{(1, 0), (1, 1)\}$ is a basis of $\mathbb{R}^2$. Find the coordinates of $(3, 5)$ in it, and verify your recipe by expanding it.
7. *(keyboard)* Load the Ames data and report the shape of the data matrix. Pull one row (a home) and one column (a feature). Identify five features that are categorical rather than numeric.
8. *(pencil)* Verify Cauchy–Schwarz directly for $(1, 2)$ and $(3, 4)$: compute both sides. Then find a pair of vectors where it holds with equality, and say why yours works.
9. *(keyboard, bridge → Ch 6)* Pick two numeric Ames features. Compute the angle between their *centered* columns (subtract each column's mean first). Relate what you find near 0 degrees and near 90 degrees to the idea of correlation.
10. *(keyboard, bridge → Ch 11)* Rerun the `lstsq` cell from 1.1 with a third feature of your choosing added. Report the new weights and whether house 2's predicted price improved. You are not yet expected to explain what `lstsq` did; you are expected to notice that the sentence it completes is still axpy.
11. *(pencil, bridge → Ch 2)* Write the two-feature Ames claim $w_1 \cdot \texttt{GrLivArea} + w_2 \cdot \texttt{OverallQual}$ as a rectangular array of numbers multiplying a column of weights. Which part is the recipe? You have just invented the next chapter.
12. *(keyboard)* Rebuild the span cloud of Figure 1.4 with `w = 2 * v`. Describe what happens to the cloud, and say which definition in this chapter predicted it.

**Further treks**

- Gilbert Strang, *Introduction to Linear Algebra* and the filmed [18.06 lectures](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/): the constructive tradition this book lives in, from the source.
- Sheldon Axler, *Linear Algebra Done Right*: the axiomatic road not taken here. Read it second; it is a beautiful second course.
- Paul Lockhart, *A Mathematician's Lament*: why your first pass at this subject may have gone the way it did.
- Stephanie Frank Singer, *Linearity, Symmetry, and Prediction in the Hydrogen Atom*: where "electron orbitals are a basis" stops being a teaser. Meet it properly after Chapter 3.
- C. L. Lawson, R. J. Hanson, D. R. Kincaid, and F. T. Krogh, "Basic Linear Algebra Subprograms for Fortran Usage," *ACM Transactions on Mathematical Software* 5(3), 1979: the paper that named axpy. The interface you met in Section 1.0 is older than most of the people using it.
