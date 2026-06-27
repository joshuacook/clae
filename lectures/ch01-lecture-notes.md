# Chapter 1 — Vectors and Linear Combinations
## Lecture notes (delivery script, ~80 min)

**The one thing they leave with:** a vector is a thing you *scale and add*; that single
act — the **linear combination** (`axpy`: `a*x + y`) — is the seed of span, basis,
coordinates, the dot product, and the data matrix, and it is the operation modern computing
is built to do fastest. Everyone should walk out having had the *Strang moment*: linear
combinations are the most important thing in the room.

**Objectives — by the end they can:**

- state scalar multiplication and addition both geometrically and entrywise;
- form a linear combination and read off its weights;
- define span / subspace, independence / basis / dimension;
- explain that a coordinate list *is* a recipe in the standard basis;
- compute dot product, length, angle; recognize orthogonality;
- read a dataset as a matrix of vectors two ways (rows = samples, columns = features).

**Setup before class:** open the companion notebook `clae-code/ch01/ch01.ipynb`, kernel
warm; have Figures 1.1–1.4 ready to project; board/tablet for the geometry. Demos are live —
run the cells, don't just show numbers.

| Segment | Section | ~min |
|---|---|---|
| Hook: the operation everything rests on | 1.0 | 15 |
| Two operations (geometry first) | 1.1 | 12 |
| Span and subspace | 1.2 | 12 |
| Independence, basis, the recipe | 1.3 | 16 |
| Length, angle, the dot product | 1.4 | 12 |
| A dataset is a matrix of vectors | 1.5 | 10 |
| Close + exercises | 1.6 | 3 |

---

## 1.0 — Hook: "In `axpy` we trust" (~15 min)

**SAY (cold open).** Modern artificial intelligence rests on a single, simple operation:
scale a vector by a number and add it to another vector. That's the whole move. The libraries
that run it ten billion times a second call it **axpy** — "a x plus y." We'll call it the
**linear combination.** Everything else — the layers, the attention heads, the billions of
parameters, the warehouses of silicon — is structure built around this one move.

**BOARD.** Write `a · x + y`. Circle it. Label three names under it: *axpy* (the library),
*linear combination* (this book), *the one move* (us).

**SAY (the lineage — earns the claim).** Architectures came and went; the operation stayed.
A recurrent net folds a sequence one step at a time — each step a linear combination of the
state so far and the next input. Then one paper said *attention is all you need* — and
attention turns out to be a weighted sum of vectors, i.e. a linear combination. The famous
title decodes to something quieter: *the linear combination is all you need.*

**SAY (set up the demo).** That it's foundational, take on faith for a moment. That it's also
the thing your computer does faster than almost anything else — don't. Watch.

**RUN (live, the headline demo).** `by_hand` (pure-Python list comprehension) vs `vectorized`
(NumPy `a*x + y`) on 10-million-element arrays. Expect roughly:
```
list comprehension:  ~4 s
vectorized:          ~100 ms
factor:              tens of times (here ~30–50x; it varies)
```
**SHOW Figure 1.1** — the sweep from n=1k to 10M. Vectorized stays flat on the floor; the
loop climbs away.

**ASK.** "Same answer both times — why is one dozens of times slower?" Take guesses, then land
it: for each of ten million entries the interpreter resolves types, boxes/unboxes objects,
checks bounds, dispatches operators — and only *then* multiplies and adds. NumPy hands the
whole array to one compiled loop the interpreter never re-enters. **It's a software win, not
a hardware trick** — emphasize this, it's the common misconception.

**SAY (the floor).** That compiled loop is built around `axpy`, one of the most tuned routines
in computing, and at the very bottom it's a single hardware instruction — the fused
multiply-add — that processors run many of at once. Software the whole way down to one step
the silicon was built to do: scale, and add. *(Optional aside if asked about "faster matmul":
AlphaTensor/AlphaEvolve sped up matrix multiplication — how you combine many multiply-adds —
not axpy itself, which is already irreducible.)*

**SAY (the turn — this is the payoff of the hook).** Now look again at the operation we opened
with. To scale a vector and add it to another *is* to form a linear combination — and you just
watched the machine treat it as the most important thing it knows how to do. Not a coincidence:
we poured decades of engineering into axpy *because* nearly everything we want to compute is
built from it. Least squares finds the combination of features closest to a price; PCA finds
the combinations carrying the most variation; the Kalman filter blends a prediction and a
measurement into one combination and calls it an estimate. **Learn to see linear combinations
everywhere, and the rest of this book is commentary.**

**TRANSITION.** "We keep saying *scale* and *add*. Let's define those two operations exactly —
and we start with the picture, not the formula."

---

## 1.1 — Two operations (geometry first) (~12 min)

> Deliver the geometry **first and loud**; the algebra is the footnote, not the headline.

**Scalar multiplication = stretching.**

- **SAY.** Multiply a vector by `c` and its arrow grows or shrinks *along its own line through
  the origin*; a negative `c` flips it to point backward. That's the whole geometric content.
- **BOARD / SHOW Figure 1.2.** Draw `v`, then `2v` (longer, same direction), then `-v` (same
  line, other side). Only now write the algebra: `c·v = (cv₁, …, cvₙ)` — every entry scales.
- **RUN.** the `plot_vector` cell (`2v`, `v`, `-v`).

**Addition = tip-to-tail.**

- **SAY.** Walk out along the first arrow; from where you land, walk along the second; the sum
  is the arrow from start to finish.
- **BOARD / SHOW Figure 1.3.** Draw the tip-to-tail triangle. Then the algebra:
  `v + w = (v₁+w₁, …, vₙ+wₙ)` — add entrywise.
- **RUN.** `vector_addition([1,2], [3,1])`.

**Combine them — the one move.**

- **BOARD.** `c·v + d·w`. Name `c, d` the **weights**. Say plainly: *this* is the linear
  combination; scaling and adding are just its two halves.
- **ASK (plant the seed for 1.2).** "Hold `v` and `w` fixed and let the weights `c, d` range
  over *all* real numbers. What set of vectors do you sweep out?" Let it hang — that's the
  next section.

---

## 1.2 — Span and subspace (~12 min)

**SAY.** Fix `v` and `w`; let `c, d` run over all reals; collect every `c·v + d·w`. That whole
set is the **span**. If `v` and `w` point along the same line, you only ever get that line. If
they don't, you fill an entire plane. Two arrows — through nothing but scaling and adding —
*generate* a two-dimensional space.

**RUN / SHOW Figure 1.4.** The meshgrid of weights → the cloud of `c·v + d·w` filling the plane.
Toggle `w` to be parallel to `v` to collapse the cloud to a line (great live moment if time).

**SAY (name the structure).** The span is **closed** under both operations — scale or add
things inside it and you stay inside — and it always contains the origin (take `c=d=0`). A set
with that property is a **subspace**. Span and subspace are two views of one object: span is
the *recipe* (build it from generators), subspace is the *property* (closed, contains 0).

**SAY (the data tie — say this slowly, it pays off all book).** In a dataset the vectors are
the **feature columns**; the subspace they span is the **column space** — every vector the
features can build. **Forward-ref:** when we fit Ames house price in Ch 11, the fitted prices
live in that column space, no more and no less. Estimation, said geometrically, is picking the
point of the subspace that best accounts for the measurement. Hold that sentence; it's the
spine of the whole course.

---

## 1.3 — Independence, basis, and the recipe (~16 min) — *the conceptual climax*

**SAY (thought experiment).** You've got a plane spanned by two vectors. Toss in a third. One
of two things happens: it already lies in the plane — then it's a combination of the two, adds
nothing new, **dependent** — or it points out of the plane, and now combinations fill all of
3-space, **independent**.

**BOARD.** Definition: a set is **linearly independent** when no vector is a combination of the
others — equivalently, the *only* combination that gives the zero vector is the all-zeros one.

**RUN.** the dependent triple `c1, c2, c3` (show `-c1 + c2 == c3`, so `c3` is redundant), then
`are_independent` — `False` for that set, `True` for the standard basis. (Mention: the test is
just rank = number of vectors; rank comes later, trust it today.)

**SAY (basis + dimension).** Independence says when a vector *earns its place*. A **basis** is
an independent set that also spans — nothing wasted, nothing missing — the smallest kit whose
combinations build the whole space. Every subspace has one; all bases have the same size, and
that size is the **dimension**.

**SAY (the payoff — slow down here).** A basis spans, so every vector *is* a combination of it.
It's independent, so that combination is **unique**. Those unique weights are the
**coordinates.**

**RUN (the reveal).** `e1, e2, e3 = np.eye(3)`; show `5·e1 + (-2)·e2 + 7·e3 → [5, -2, 7]`.

**SAY (land it — this is the Strang moment).** The list `(5, -2, 7)` was `5·e1 - 2·e2 + 7·e3`
**all along.** The list was never the vector — it was the **recipe**, written in a basis so
familiar we forgot it was a choice. A vector is a geometric object; the numbers are just its
instructions in one particular coordinate system. **Forward-ref:** in Ch 2 a matrix forms a
linear combination of its columns, and the input vector is the recipe. We've already met the
idea today.

**ASK (check the click).** "If I hand you the same arrow but a different basis, do the
coordinates change? Does the arrow?" (Coordinates yes; arrow no.)

---

## 1.4 — Length, angle, and the dot product (~12 min)

**SAY.** We can *build* vectors by combining them. To *estimate*, we have to **measure** them —
how long, how aligned. One tool does both: the **dot product** — multiply matching entries,
sum, one number out. `v·w = v₁w₁ + … + vₙwₙ`.

**RUN.** `v @ w`; `np.linalg.norm(v)`; the angle line (`arccos` of normalized dot, in degrees).

**BOARD.** `‖v‖ = √(v·v)` — Pythagoras, origin to tip. `cosθ = (v·w)/(‖v‖‖w‖)`. Note the dot
product is symmetric and respects scale-and-add in each slot — the compatibility with linear
combinations we'll use without comment.

**SAY (flag orthogonality — payoff is chapters away, plant it now).** When the dot product is
zero, the vectors are **orthogonal**. Why care today? Because when a measurement can't be reached
by *any* combination of our features, the closest reachable point leaves an error orthogonal to
everything reachable — that single condition *is* least squares (Ch 11). And the same dot
product on centered data is **covariance** (Ch 6). One operation, two of the book's biggest
ideas.

---

## 1.5 — A dataset is a matrix of vectors (~10 min)

**SAY.** One vector is one record. A dataset is many, stacked into a matrix. Real data rarely
arrives as one clean table — the Ames housing data ships as three files (zoning, listing, sale)
joined on `Id`. The real on-ramp: three sources, one matrix.

**RUN.** the merge → `housing.shape → (1460, 80)`: 1460 homes, 80 features. (`SalePrice`, the
target, rides in from the sale file.)

**SAY (two readings — draw both).** Read the matrix `X` two ways:

- **Across the rows:** each row is a point in `Rⁿ` — one home among all the others, the data
  cloud.
- **Down the columns:** each column is a vector in `Rᵐ` — one feature measured across all `m`
  homes.

**RUN.** `housing.loc[2]` (a home) vs `numeric['GrLivArea']` (a feature over 1460 homes).

**SAY (close the loop).** The column reading connects to everything we built today: feature
columns are vectors, their span is the column space, and their linear combinations are *exactly*
the predictions a linear model can make. Convention for the whole book: **rows = samples,
columns = features.** Categoricals (neighborhood, roof style) become numeric vectors later
(Ch 2, Ch 6). **Forward-ref:** in Ch 2 the matrix stops being a *container* and becomes an
*action*.

---

## 1.6 — Close (~3 min)

**SAY (one-breath recap).** A vector is a thing you scale and add. The act is the linear
combination. Span, subspace, basis, coordinates, the dot product, and the data matrix all fell
out of taking that one act seriously.

**SAY (the question the whole book answers).** Of all the linear combinations available to us,
*which one is the estimate* — and how do we find it? That's where we're going.

**Assign:**

- **1.1** Time `by_hand` vs `vectorized` axpy on your own machine; explain the gap in terms of `axpy`.
- **1.2** Given three vectors, decide independence two ways — by hand, then `are_independent`.
- **1.3** Load Ames; report the matrix shape; pull one row (a home) and one column (a feature); say which features are categorical.
- **1.4** Pick two numeric Ames features; compute the angle between their *centered* columns; relate near-0° / near-90° to correlation (we'll formalize it in Ch 6).

---

### Delivery cues

- **Run every demo live.** The axpy gap and the `e1,e2,e3` reveal are the two moments that land
  the lecture — don't reduce them to static slides.
- **Slowest beats:** the 1.0 turn ("look again — it's a linear combination") and the 1.3 reveal
  ("the list was the recipe"). Pause after each.
- **Recurring callback:** every section, name the linear combination out loud — by 1.5 they
  should be finishing the sentence for you.
- **If short on time:** compress 1.4 to length + orthogonality (drop the angle demo) and 1.5 to
  the two-readings picture; never cut the 1.3 reveal.
