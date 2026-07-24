<!-- DRAFT V8 (2026-07-24): the v12 pass per the v11 ink census.
     CENTRAL IDEA: THE AGREEMENT (C1). Vector space defined FIRST (C3);
     coordinates seeded at the "point" remark (C2 C13 C16); subspace
     demoted, Axler tangent cut (C9); membership answered on the spot
     by inspection + TikZ (C7); solving section dissolved into the tour
     (P14/C18: E/U live in the preface review now; existence-failure
     folds into span, uniqueness-failure into independence); standard
     basis = the x/y axes (C14); trivial solution shown (C10a); the
     R2/R3 figure corrected (C10b); span-of-the-question name killed
     (C15); same-space note (C4); LLM footnote rewrite (C5); sweep
     naming unified (C6). Claims->Facts happens in the global pass.
     Base: V7. -->

# Chapter 1: Vectors, Spaces, and the Solving Question

## 1.0 The Method

This chapter is about one idea: **the agreement**. Everything in linear algebra begins as a deal you strike with your objects. You agree to do exactly two things to them, scale them and add them, and they agree that the results stay in the family. That is the whole contract. Every term this chapter introduces is either a party to the agreement (vectors, and the spaces they form), a move the agreement licenses (the linear combination, and the span of everything it can reach), or a question the agreement makes precise (when combinations are genuinely different, and what a basis is). The preface promised that assuming linearity buys you an entire transferable subject. The agreement is what "assuming linearity" means, stated as a rule you could enforce.

So the chapter opens with the agreement itself, then introduces the objects that sign it, through all four of the preface's lenses.

> **Definition 1.1 (vector space, working version).** A **vector space** is a set $S$ of objects, called **vectors**, closed under two operations:[^axioms]
>
> - **Closure under scaling.** For every vector $\mathbf{v}$ in $S$ and every number $c$, the vector $c\mathbf{v}$ is in $S$.
>
> - **Closure under addition.** For every pair of vectors $\mathbf{v}$ and $\mathbf{w}$ in $S$, the vector $\mathbf{v} + \mathbf{w}$ is in $S$.

Read the definition's order of precedence, because it is the chapter's whole philosophy. A vector is not a thing with a fixed nature that happens to allow scaling and adding. A vector is *whatever lives in a set where scaling and adding stay closed*. The agreement comes first; the objects qualify by signing it. Lists of numbers sign it, and they are this chapter's working vectors. Arrows sign it. Functions sign it, as Section 1.6 will show, and random variables will sign it in Chapter 5, which is why one chapter of algebra ends up running an entire book.

Here is the working vector, seen through all four lenses before anything happens to it.

\lensmark{geometric} Through the geometric lens, a vector is an arrow from the origin. The arrow $(2, 1)$ walks two east and one north:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=1.1]
  \draw[gray!40, ->] (-0.5,0) -- (3.0,0);
  \draw[gray!40, ->] (0,-0.5) -- (0,1.8);
  \draw[gray!25] (0,0) grid[step=1] (2.6,1.6);
  \draw[->, very thick] (0,0) -- (2,1) node[above right] {$(2, 1)$};
\end{tikzpicture}
\caption{A vector through two lenses at once. The arrow is the geometric reading, two east and one north from the origin, and its label $(2, 1)$ is the algebraic one, the ordered list the next lens defines.}
\end{figure}

\lensmark{algebraic} Through the algebraic lens, the same vector is an ordered list of numbers, an object with rules for pencil work.

> **Definition 1.2 (the vectors of Part I).** The working vectors of this book's first three parts are ordered lists of $n$ real numbers,[^complexnote] $\mathbf{v} = (v_1, \ldots, v_n)$. With entrywise scaling and addition they sign the agreement, and the vector space they form is $\mathbb{R}^n$.

[^complexnote]: Real by decree, not by necessity. Everything in Part I works unchanged with complex entries, and $\mathbb{C}^n$ takes over when signal processing requires it in Chapter 14. Until then the reals carry the book.

The arrow above is $(2, 1)$ in $\mathbb{R}^2$, and you have almost certainly met this object before under another name: the **point** $(2, 1)$, from every graph you ever plotted. Point and vector are the same data, and the two numbers deserve their proper name now, because it is the name this book will lean on hardest.

> **Definition 1.3 (coordinates, first form).** The numbers in a vector's list are its **coordinates**: how far to walk along each axis to reach it. Section 1.4 will reveal what the axes themselves are and upgrade this definition into the chapter's payoff.

Three dimensions work the same way with one more coordinate: $(1, 0, 2)$, $(3, -1, 4)$, and $(0, 0, 1)$ all live in $\mathbb{R}^3$, arrows in space instead of on a page. Past three dimensions the drawing gives out and the list keeps going.

\lensmark{computational} Through the computational lens, a vector is an array, a contiguous block of memory the compiled libraries can run over at full speed. Listing 1.1 puts one in $\mathbb{R}^2$ and one in $\mathbb{R}^3$ into memory.

**Listing 1.1 (a vector in the machine)**

```python
import numpy as np
v = np.array([2, 1])
u = np.array([1, 0, 2])
```

\lensmark{data} And through the data lens, a vector is a column of measurements: one measured quantity, recorded across many observations, stacked into a single object. Part II opens on a dataset of 1,460 home sales and reads every column of it exactly this way, with all of this chapter's machinery intact.

One object, four appearances: an arrow, a list with rules, an array in memory, a column of measurements. Every concept in this book will make the same tour, the margin announcing each lens as it takes over, and the tour will always run in the creed's order where it can. Picture first, pencil second, machine third, data last.

## 1.1 The two operations, drawn

The agreement names two operations, so here they are in full, picture first. These are the only moves the whole subject will ever make.

**Scalar multiplication.** \lensmark{geometric} Scalar multiplication is stretching. Multiply a vector by $c$ and its arrow grows or shrinks along its own line through the origin. A negative $c$ flips it to point the other way down the same line. What scaling can never do is change the line. Length changes, direction stays or exactly reverses, and no choice of $c$ rotates the arrow off its axis:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.9]
  \draw[gray!40, ->] (-2.6,-1.3) -- (5.4,2.7);
  \draw[->, very thick, gray] (0,0) -- (4,2) node[below right] {$2\mathbf{v}$};
  \draw[->, very thick] (0,0) -- (2,1) node[above left] {$\mathbf{v}$};
  \draw[->, very thick, gray!70] (0,0) -- (-2,-1) node[below left] {$-\mathbf{v}$};
\end{tikzpicture}
\caption{Scalar multiplication is stretching. $\mathbf{v}$, $2\mathbf{v}$, and $-\mathbf{v}$ share one line through the origin.}
\end{figure}

\lensmark{algebraic} The pencil version is entrywise, small enough to do whole:

\begin{align}
3\,(2, 1) = (3 \cdot 2,\; 3 \cdot 1) = (6, 3), \qquad\quad c\,\mathbf{v} = (c v_1,\, c v_2,\, \ldots,\, c v_n)
\end{align}

\lensmark{computational} The machine draws the same picture at whatever scale you ask. Listing 1.6 wraps matplotlib's arrow primitive.

**Listing 1.6 (a vector-drawing helper, defined)**

```python
import matplotlib.pyplot as plt

def plot_vector(v, color='blue', label=None):
    plt.quiver(0, 0, v[0], v[1], angles='xy',
               scale_units='xy', scale=1,
               color=color, label=label)
```

Listing 1.7 puts three multiples of one vector on the same axes. Figure 1.5 is its output.

**Listing 1.7 (scalar multiples, drawn)**

```python
v = np.array([2, 1])
plot_vector(2 * v, 'purple', '2v')
plot_vector(v, 'blue', 'v')
plot_vector(-v, 'red', '-v')
plt.show()
```

![scalar multiplication](figures/fig_scalar_multiplication.png)

> **Figure 1.5.** Scalar multiplication. `v`, `2v`, and `-v` all lie on the single line through the origin: multiplying by `c` slides the arrow along that line, and flips it to the far side when `c` is negative.

**Addition.** \lensmark{geometric} Addition is tip to tail. Walk out along the first arrow. From where you land, walk out along the second. The sum is the single arrow from start to finish. Figure 1.3 already showed it. \lensmark{algebraic} The pencil version is entrywise again:

\begin{align}
(1, 2) + (3, 1) = (4, 3), \qquad\quad \mathbf{v} + \mathbf{w} = (v_1 + w_1,\, \ldots,\, v_n + w_n)
\end{align}

\lensmark{computational} Listing 1.8 renders a sum with the helper from Listing 1.6. Figure 1.6 is its output.

**Listing 1.8 (tip to tail, drawn)**

```python
v1, v2 = np.array([1, 2]), np.array([3, 1])
plot_vector(v1, 'blue', 'v1'); plot_vector(v2, 'red', 'v2')
plot_vector(v1 + v2, 'green', 'v1 + v2')
plt.show()
```

![vector addition: tip to tail](figures/fig_vector_addition.png)

> **Figure 1.6.** `v1` and `v2` from the origin, with `v2` carried to the tip of `v1` (faded), and the tip-to-tail sum `v1 + v2` in green.

Put the two operations together and the book's central object, the linear combination, appears in person. Take $\mathbf{v} = (1, 2)$ and $\mathbf{w} = (3, 1)$ and form the combination $2\mathbf{v} + \mathbf{w}$, scale first, then add:

\begin{align}
2\,(1, 2) + (3, 1) = (2, 4) + (3, 1) = (5, 5)
\end{align}

That arithmetic, repeated ten million times per entry at compiled speed, is Section 1.5's story, and it is the physical form every combination in this book will take.

The two operations are on the table. The next move is the agreement that makes them a subject.

[^axioms]: There is a bootstrap here, and it is worth seeing plainly. A vector space is the thing that stays closed when you scale and add, and scaling and adding are the operations a vector space supports. The circle is not a flaw. It is the agreement. Commit to objects with these two operations, and everything else in the book follows. The full definition adds eight axioms governing how the operations behave (addition commutes and associates, a zero vector exists, every vector has an additive inverse, and scalar multiplication associates, distributes both ways, and respects 1). $\mathbb{R}^n$ satisfies all eight, every space in this book satisfies all eight, and we will not check them again. The scalars bring a rulebook of their own, the arithmetic that makes the reals a **field**, and a vector space is always declared over one; when Chapter 14 trades $\mathbb{R}$ for $\mathbb{C}$, it is trading fields. Sheldon Axler, *Linear Algebra Done Right*, ch. 1, gives the axioms a first-class treatment.

\lensmark{algebraic} The agreement pays immediately. Consent to work only with objects that live in a vector space, and every construction in this book comes with the membership. Take one scaling followed by one addition, $a\mathbf{x} + \mathbf{y}$, and watch each clause do its half of the work.

**Closure under scaling** keeps the first move inside. **Closure under addition** then keeps the finish inside too:

\begin{align}
\mathbf{x} \in S \;\Longrightarrow\; a\mathbf{x} \in S, \qquad\quad a\mathbf{x} \in S,\; \mathbf{y} \in S \;\Longrightarrow\; a\mathbf{x} + \mathbf{y} \in S
\end{align}

On numbers, take $\mathbf{x} = (1, 2)$ and $\mathbf{y} = (3, 1)$ in $\mathbb{R}^2$. Then $2\mathbf{x} = (2, 4)$ is in $\mathbb{R}^2$. So is $2\mathbf{x} + \mathbf{y} = (5, 5)$. \lensmark{geometric} And in a picture, the whole demonstration is two arrows and a walk:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.85]
  \draw[gray!40, ->] (-0.5,0) -- (6.0,0);
  \draw[gray!40, ->] (0,-0.5) -- (0,5.6);
  \draw[->, thick] (0,0) -- (1,2) node[left] {$\mathbf{x}$};
  \draw[->, thick, gray] (0,0) -- (2,4) node[left] {$2\mathbf{x}$};
  \draw[->, thick, gray!70] (2,4) -- (5,5);
  \node[gray!90, above right] at (3.2,4.35) {$\mathbf{y}$, carried};
  \draw[->, very thick] (0,0) -- (5,5) node[above right] {$2\mathbf{x} + \mathbf{y} = (5,5)$};
\end{tikzpicture}
\caption{Closure, drawn. Scale $\mathbf{x}$, carry $\mathbf{y}$ from its tip, and the combination $2\mathbf{x} + \mathbf{y}$ is the arrow to where you land. Every step stays in the vector space.}
\end{figure}

Scale $\mathbf{x}$, walk $\mathbf{y}$ from its tip, and the combination is the arrow to where you land. Every step stayed on the page, which is the picture's way of saying every step stayed in the vector space.

Repeat the two moves and every linear combination of vectors in $S$ lands in $S$. Two clauses in, the whole of Definition 1.4 out. And what the two clauses buy is out of all proportion to their price, because linearity is the assumption behind every incantation this book will teach. Assume it, and here are the spells, a sampling of what linearity enables rather than the whole grimoire, in the order the book casts them: axpy at compiled speed (this chapter), the fact that electron orbitals are a basis (Chapter 4), the directions that carry a dataset's variation (Chapter 11), regression (Chapter 12), and Fourier analysis (Chapter 14). Each one is the same small set of moves applied to a new family of objects that kept the two clauses.

## 1.2 The linear combination

Now the operation. Modern artificial intelligence, and the video gaming industry whose graphics hardware it borrowed, rests on a single, simple move. Scale a vector by a number, and add it to another vector.[^llm] That is the whole of the operation, and it carries its name into a definition.

[^llm]: The claim is not rhetorical. A language model, underneath the chat window, is arithmetic at colossal scale: numbers organized into long lists, the lists scaled, the scaled lists added. Architectures turn over every few years and the operation does not. The recurrent networks that read text one word at a time carried a running summary forward, scaling what they held and adding what they read. The paper that retired them is titled "Attention Is All You Need," and attention is a weighted sum of vectors, which is this definition. Architectures keep being replaced; the recurrent ones were retired for attention, and attention will be retired for something else. The operation they are all made of has not changed since the beginning, and it is the one this chapter is about.

> **Definition 1.4 (linear combination, weights).** A **linear combination** of vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$, all drawn from one vector space, is
>
> \begin{align}
> c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k,
> \end{align}
>
> the vectors scaled by numbers and the results added. The numbers $c_1, \ldots, c_k$ are the **weights**.

Concretely, in $\mathbb{R}^3$, $2\,(1, 0, 2) + 3\,(3, -1, 4) = (2, 0, 4) + (9, -3, 12) = (11, -3, 16)$ is a linear combination of two vectors with weights $2$ and $3$, and $5\,(0, 0, 1)$ is a linear combination of one.

## 1.3 Span and subspace

Hold $\mathbf{v}$ and $\mathbf{w}$ fixed, and let the weights range over every value they can take. What do you get?

> **Definition 1.5 (span).** The **span** of a set of vectors is the collection of all their linear combinations.

\lensmark{geometric} The degenerate case first, drawn before computed. If $\mathbf{w}$ already lies on $\mathbf{v}$'s line, say $\mathbf{w} = 2\mathbf{v}$, then no combination ever leaves that line:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.85]
  \draw[gray!60, thick] (-2.2,-1.1) -- (5.2,2.6);
  \draw[->, very thick] (0,0) -- (2,1) node[above left] {$\mathbf{v}$};
  \draw[->, very thick, gray] (0,0) -- (4,2) node[above left] {$\mathbf{w} = 2\mathbf{v}$};
  \node[gray, anchor=west] at (3.3,1.15) {\scriptsize the span, one line};
\end{tikzpicture}
\caption{The degenerate case. With $\mathbf{w} = 2\mathbf{v}$, every combination stays on $\mathbf{v}$'s line, and the span is that line.}
\end{figure}

\lensmark{algebraic} The picture has an algebra, and the algebra is scalar multiplication in disguise:

\begin{align}
c\,\mathbf{v} + d\,(2\mathbf{v}) = (c + 2d)\,\mathbf{v} = a\,\mathbf{v}, \qquad a = c + 2d
\end{align}

The bundle $a = c + 2d$ is one real number, a scalar like any other, so every combination collapses to a single stretch of $\mathbf{v}$. The span is $\mathbf{v}$'s line, and the second vector bought no new territory. \lensmark{geometric} But let $\mathbf{w}$ point off the line, and the combinations sweep out an entire plane:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.55]
  \fill[gray!12] (-3.55,-4.65) -- (1.25,-2.25) -- (3.55,4.65) -- (-1.25,2.25) -- cycle;
  \draw[->, very thick] (0,0) -- (2,1) node[below right] {$\mathbf{v}$};
  \draw[->, very thick, gray] (0,0) -- (1,3) node[left] {$\mathbf{w}$};
  \draw[gray] (0.9,0.45) arc (27:72:1.0);
  \node[gray] at (1.3,0.98) {\scriptsize $45^\circ$};
  \node[gray, anchor=west] at (1.7,3.6) {\scriptsize the span, a plane};
\end{tikzpicture}
\caption{The full case. With $\mathbf{w}$ off the line, the combinations sweep out an entire plane.}
\end{figure}

\lensmark{computational} The machine can draw the sweep by brute force, and NumPy has a function whose whole job is the word *every*. `meshgrid` takes a sweep of values for $c$ and a sweep for $d$ and crosses them, every $c$ paired with every $d$. Listing 1.10 wraps the cross into a function.

**Listing 1.10 (sweep_span, defined)**

```python
def sweep_span(v: np.ndarray, w: np.ndarray, ax) -> None:
    grid = np.linspace(-2, 2, 25)
    C, D = np.meshgrid(grid, grid)
    cloud = C.ravel()[:, None] * v + D.ravel()[:, None] * w
    ax.scatter(cloud[:, 0], cloud[:, 1], s=4, alpha=0.4)
```

Listing 1.11 runs the identical sweep twice, once with $\mathbf{w}$ on $\mathbf{v}$'s line and once off it. Figure 1.10 is its output, and it verifies both drawings.

**Listing 1.11 (both cases, swept)**

```python
v = np.array([2, 1])
fig, (left, right) = plt.subplots(1, 2, figsize=(9, 4))
sweep_span(v, 2 * v, left)               # w on v's line
sweep_span(v, np.array([1, 3]), right)   # w off the line
plt.show()
```

![the span, swept: degenerate and full](figures/fig_span_pair.png)

> **Figure 1.10.** The same weight sweep, $c$ and $d$ each from $-2$ to $2$, crossed by `meshgrid`. Left: $\mathbf{w} = 2\mathbf{v}$, and every one of the 625 combinations lands on $\mathbf{v}$'s line. Right: $\mathbf{w} = (1, 3)$ points off the line, and the identical sweep fills a patch of plane. Widen the sweep and the patch grows without bound; the plane is what it is filling in.

Membership in a span is a concrete question, and the preface's review taught the method that answers it. Is $\mathbf{b} = (4, 7)$ in the span of $\mathbf{v} = (2, 1)$ and $\mathbf{w} = (1, 3)$? By inspection, yes: one $\mathbf{v}$ and two $\mathbf{w}$s,

\begin{align}
1\,(2, 1) + 2\,(1, 3) = (2, 1) + (2, 6) = (4, 7),
\end{align}

verified by the addition on the page. \lensmark{geometric} And the answer draws as Chapter 1's own tip-to-tail walk:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.55]
  \draw[gray!30, ->] (-0.6,0) -- (5.2,0);
  \draw[gray!30, ->] (0,-0.6) -- (0,7.6);
  \draw[->, very thick] (0,0) -- (2,1) node[below right] {$1 \cdot \mathbf{v}$};
  \draw[->, thick, gray] (2,1) -- (3,4);
  \draw[->, thick, gray] (3,4) -- (4,7);
  \node[gray, anchor=west] at (3.6,4.9) {$2 \cdot \mathbf{w}$, walked};
  \draw[->, very thick, black!70] (0,0) -- (4,7) node[above] {$\mathbf{b} = (4,7)$};
\end{tikzpicture}
\caption{Membership, answered by inspection and drawn. One step of $\mathbf{v}$, two steps of $\mathbf{w}$ tip to tail, and the walk lands exactly on $\mathbf{b} = (4, 7)$: the target is in the span.}
\end{figure}

Membership can also fail, and the failure is just as visible. Replace $\mathbf{w}$ with $(4, 2) = 2\mathbf{v}$ and ask for the same target. The span has collapsed to $\mathbf{v}$'s line, every combination lies on that line, and $(4, 7)$ does not: $4/2 \ne 7/1$. No combination reaches it, and nothing can be computed around that fact; the target is simply outside the reach. The preface's review named these the two standing questions, **existence** (is the target in the span at all?) and **uniqueness** (is the recipe the only one?), and this chapter is quietly building each one a home. Existence lives here, in the span. Uniqueness lives in the next section.

When the vectors being combined sit as the columns of a matrix, which is how Chapter 2 will package them, the span takes the name it carries for the rest of the book.

> **Definition 1.6 (column space).** The **column space** of a matrix is the span of its columns: everything the matrix's columns can reach by combination. Existence, for the systems of Chapter 3 and the models of Part III, is always the question of whether a target lies in a column space.

One vocabulary word before moving on, introduced lightly because it will matter later. Notice that a span honors the agreement all by itself: scale a combination or add two of them and you get another combination, so a span is a vector space in its own right, living inside a larger one. The word for that, a vector space inside a vector space, is **subspace**, and when Part III projects onto subspaces, the spans of this section are what it will mean.

The drawings above are more general than they look, and that is their purpose. Two vectors span at most a plane, in three dimensions, in 1,460, in a googol. The reach of a span is set by how many vectors you combine, never by the size of the space they live in.[^precise] So every question this book asks about two vectors happens inside the at-most-a-plane they span, and a drawing on this page is exact for the 1,460-dimensional case. Nobody can picture $\mathbb{R}^{1460}$, and nobody needs to.

[^precise]: The precise statement arrives in Section 1.4, once dimension is on the table.

\lensmark{data} The data lens will point this machinery at measurements the moment Part II supplies them. A dataset's feature columns are vectors, their span is every prediction a linear model over those features can make, and whether an observed target column lies in that span is an existence question with consequences. Chapter 5 assembles the dataset; Chapter 12 lives inside this exact question.

## 1.4 Independence, basis, and the recipe

Move to $\mathbb{R}^3$ for one drawing, because the idea needs the room. Two independent vectors in $\mathbb{R}^3$ span a plane through the origin. Bring in a third vector. \lensmark{geometric} Either it lands in that plane, already reachable, so three vectors carry no more span than two. Or it points out of the plane, and combinations of the three fill all of space:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.8]
  \fill[gray!12] (-2.2,-1.4) -- (2.8,-1.4) -- (4.2,1.0) -- (-0.8,1.0) -- cycle;
  \draw[->, very thick] (0,0) -- (2,0.4) node[right] {$\mathbf{v}$};
  \draw[->, very thick] (0,0) -- (0.9,-0.9) node[below] {$\mathbf{w}$};
  \draw[->, very thick, gray] (0,0) -- (2.6,-0.5) node[right] {$\mathbf{u}$ in the plane};
  \draw[->, very thick, black!70] (0,0) -- (0.6,2.2) node[above] {$\mathbf{u}'$ out of it};
\end{tikzpicture}
\caption{In $\mathbb{R}^3$: the plane spanned by $\mathbf{v}$ and $\mathbf{w}$, drawn in perspective, and a third vector's two possible fates. $\mathbf{u}$ lies in the plane, so the span does not grow and only two of the three are independent. $\mathbf{u}'$ points out of it, and combinations of all three fill space.}
\end{figure}

> **Definition 1.7 (linear independence).** A set of vectors is **linearly independent** when none of them is a linear combination of the others.[^zerotest]

[^zerotest]: The equivalent test is usually easier to run. The only combination equal to the zero vector is the one with every weight zero. The two phrasings convert by moving one vector across the equals sign, exactly the maneuver the dependent-triple computation below performs in reverse.

\lensmark{algebraic} Both verdicts are pencil work, so render one of each. The working test sets a combination to zero, and the zero is not arbitrary. Any dependence, whichever vector it favors, rearranges to the same shape, everything on one side, a combination equal to the zero vector with at least one live weight. Test zero and every possible dependence is tested at once. The pair $\mathbf{v} = (2, 1)$, $\mathbf{w} = (1, 3)$ is independent. Set a combination to zero and elimination forces both weights to die:

\begin{align}
\begin{aligned} 2c + d &= 0 \\ c + 3d &= 0 \end{aligned}
\qquad\longrightarrow\qquad
d = -2c,\quad c + 3(-2c) = -5c = 0
\qquad\Longrightarrow\qquad c = d = 0
\end{align}

Only the **trivial solution** survives, every weight zero, and that is the independence verdict. Now bring in $\mathbf{u} = (4, 7)$, the vector Section 1.3 left hanging. Here is a recipe for it, offered with no derivation: $\mathbf{u} = 1\,\mathbf{v} + 2\,\mathbf{w}$. Check it, $1\,(2, 1) + 2\,(1, 3) = (4, 7)$, and it holds. Where the recipe came from does not matter yet, and that it does not matter is a theme this chapter is about to make official. The triple is dependent, and moving $\mathbf{u}$ across the equals sign exhibits the zero combination with live weights:

\begin{align}
1\,\mathbf{v} + 2\,\mathbf{w} - 1\,\mathbf{u} = (2, 1) + (2, 6) - (4, 7) = (0, 0)
\end{align}

A **nontrivial** solution, live weights summing to nothing, and that is the dependence verdict. The pencil dichotomy is exactly the definition's: independent means the zero combination has only the trivial solution, dependent means it has a nontrivial one.

And dependence has a consequence worth seeing now, because it is the shape of the preface's second standing question failing. Dependence manufactures recipes. The triple $\{\mathbf{v}, \mathbf{w}, \mathbf{u}\}$ reaches $(4, 7)$ two different ways:

\begin{align}
1\,\mathbf{v} + 2\,\mathbf{w} + 0\,\mathbf{u} = (4, 7), \qquad\quad
0\,\mathbf{v} + 0\,\mathbf{w} + 1\,\mathbf{u} = (4, 7)
\end{align}

Both verify. Neither is wrong. Subtract them and the dependence itself reappears, weight by weight. That is **uniqueness** failing, mechanically: with a dependent set, no recipe means anything on its own, because any claim built on one recipe could have been built on another. Independence is precisely what makes recipes trustworthy, and the next definition is where trustworthy recipes get their name.

\lensmark{computational} Listing 1.12 reuses `sweep_span` on $\mathbf{v}$ and $\mathbf{w}$ and draws $\mathbf{u}$ on top. Figure 1.12 is its output.

**Listing 1.12 (the verdict, drawn)**

```python
v, w, u = np.array([2, 1]), np.array([1, 3]), np.array([4, 7])
ax = plt.gca()
sweep_span(v, w, ax)
arrows = [(v, 'blue', 'v'), (w, 'red', 'w'), (u, 'green', 'u')]
for vec, c, name in arrows:
    ax.quiver(0, 0, *vec, angles='xy', scale_units='xy',
              scale=1, color=c, label=name)
ax.legend(); plt.show()
```

![the dependent third vector inside the span](figures/fig_span_membership.png)

> **Figure 1.12.** The span cloud of $\mathbf{v} = (2,1)$ and $\mathbf{w} = (1,3)$ with the third vector $\mathbf{u} = (4,7)$ drawn on top. The tip of $\mathbf{u}$ sits inside the swept patch. It is reachable, the triple is dependent, and the span did not grow.

> **Definition 1.8 (basis, dimension).** A **basis** of a subspace is a linearly independent set that spans it. All bases of a given subspace have the same size,[^samesize] and that shared size is the subspace's **dimension**.

[^samesize]: A theorem, not an observation. The standard argument swaps the vectors of one basis into the other one at a time without losing the span, so an independent set can never outnumber a spanning set. Axler ch. 2 or Strang ch. 3 for the bookkeeping.

Dimension immediately buys a second word, the honest measure of what a set of vectors delivers.

> **Definition 1.9 (rank).** The **rank** of a set of vectors is the dimension of its span: the number of independent directions the set actually contains, as opposed to the number of vectors it lists. The dependent triple above lists three vectors and has rank 2.

> **Fact 1.1 (unique recipe).** If $\mathbf{b}_1, \ldots, \mathbf{b}_k$ is a basis, every vector in its span is a combination of the basis in exactly one way.[^footnotes]
>
> Witness it small. The set $\{(1, 0), (1, 1)\}$ is a basis of $\mathbb{R}^2$. To build $(3, 5)$, the second entry forces the weight on $(1, 1)$ to be $5$. The first entry then forces the weight on $(1, 0)$ to be $-2$. Forced twice over, no other recipe exists.
>
> The reason it always works is one subtraction. Suppose $c_1\mathbf{b}_1 + \cdots + c_k\mathbf{b}_k$ and $d_1\mathbf{b}_1 + \cdots + d_k\mathbf{b}_k$ build the same vector. Subtract them: $(c_1 - d_1)\mathbf{b}_1 + \cdots + (c_k - d_k)\mathbf{b}_k = \mathbf{0}$. Independence allows only the trivial solution, so $c_i = d_i$ for every $i$, and the two recipes were one recipe all along.

[^footnotes]: A note about this book's footnotes, since this is its first boxed statement: the fuller arguments live down here and in the references, on purpose. The text above is for you. When a reason is cheap you will get it whole. When it is a real theorem you will get the name of someone who proved it properly.

**The license.** Fact 1.1 has a methodological consequence, and it is large enough to state on its own. When a solution is unique, any procedure that produces a verified candidate has produced the solution. The logic is airtight: the verified candidate is a solution, the solution is one of a kind, therefore the candidate is it. This turns solving **by inspection**, producing a candidate by direct examination rather than by procedure, into a rigorous method.

Produce a candidate however you like. Verify it. Uniqueness closes the argument. The underived recipe above was legitimate for exactly this reason, and Jim opened his first lecture with uniqueness, before teaching any solving at all, because the license has to exist before any fast method is legal. Chapter 3 builds this into a working discipline.

> **Definition 1.10 (coordinates).** The **coordinates** of a vector with respect to a basis are the unique weights of its recipe in that basis.

> **Definition 1.11 (standard basis).** The **standard basis** of $\mathbb{R}^n$ is $\mathbf{e}_1, \ldots, \mathbf{e}_n$, where $\mathbf{e}_j$ has a one in entry $j$ and zeros elsewhere.

You have known this basis your whole mathematical life without its name. In $\mathbb{R}^2$, $\mathbf{e}_1 = (1, 0)$ is one step along what you have always called the $x$-axis, and $\mathbf{e}_2 = (0, 1)$ is one step along the $y$-axis. The axes of every graph you have ever drawn *are* the standard basis, and plotting a point at $(3, 5)$ was always the combination $3\mathbf{e}_1 + 5\mathbf{e}_2$: three steps east, five steps north. Definition 1.3's "how far along each axis" was this section's machinery in disguise, and now the disguise comes off.

Here is the payoff. A basis spans, so every vector is a combination of it. A basis is independent, so that combination is unique. The unique weights are the coordinates, and the axes were a choice of basis all along. \lensmark{algebraic} Apply that to the standard basis in $\mathbb{R}^3$ and watch a plain list of numbers come apart:

\begin{align}
5\,\mathbf{e}_1 - 2\,\mathbf{e}_2 + 7\,\mathbf{e}_3
= (5, 0, 0) + (0, -2, 0) + (0, 0, 7)
= (5, -2, 7)
\end{align}

The list $(5, -2, 7)$ was $5\mathbf{e}_1 - 2\mathbf{e}_2 + 7\mathbf{e}_3$ all along. The list was never the vector; it was the recipe, written in a basis so familiar we forgot it was a choice.

> **Fact 1.2 (a span's dimension never exceeds its head count).** The span of $k$ vectors has dimension at most $k$, whatever the dimension of the ambient space.[^ambient]
>
> Why this is true: if the $k$ vectors are independent, they are a basis of their span and the dimension is exactly $k$. If they are dependent, discard a dependent vector; it was already a combination of the others, so the span does not shrink while the count drops. Repeat until what remains is independent, a basis of the original span with at most $k$ members. This is the precise form of the promise made under the span drawings: two vectors buy at most a plane, in $\mathbb{R}^3$, in $\mathbb{R}^{1460}$, anywhere.

[^ambient]: **Ambient space**: the $\mathbb{R}^n$ the vectors happen to live in, as opposed to the subspace they generate. Two feature columns live in the ambient $\mathbb{R}^{1460}$ and generate an at-most-two-dimensional subspace. The 1,460 is the address, and the 2 is the substance.

The preface's two standing questions now both have homes in the agreement's vocabulary. Existence lives in the span: a target is reachable or it is not (Section 1.3 showed one of each). Uniqueness lives in independence: independent sets give one recipe per reachable target (Fact 1.1), dependent sets give a family and take every recipe's meaning with them. Chapter 2 will name the space where uniqueness dies. Chapter 3 will turn the pair into a working method, and Part III will take over when existence fails on real data and *best* becomes the question. That is the whole road ahead, and every step of it is the agreement, applied.

## 1.5 In `axpy` we trust

One definition has been waiting since Section 1.2, and it is the name under which the linear combination earns its living.

> **Definition 1.12 (axpy).** For a number $a$ and vectors $\mathbf{x}$ and $\mathbf{y}$, **axpy** is the linear combination $a\mathbf{x} + \mathbf{y}$, one scaling and one addition.

The strange name is a working credential. Deep in the compiled numerical libraries that every scientific computing stack calls down into, the routine that computes $a\mathbf{x} + \mathbf{y}$ has been named `axpy`, "a times x plus y," since the 1970s. When this book says axpy, it means the operation and it gestures at the machinery. That routine is the most heavily engineered few lines of arithmetic in numerical computing. The claim that axpy is foundational you have just read. The claim that your computer runs it faster than almost anything else it does is measurable, so the next section measures it.


\lensmark{algebraic} Run the operation once by hand before the machine gets it. Take $a = 2$, $\mathbf{x} = (1, 2, 3)$, $\mathbf{y} = (10, 20, 30)$, and do the two moves in order, scale then add:

\begin{align}
a\,\mathbf{x} = 2\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
= \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}, \qquad
a\,\mathbf{x} + \mathbf{y}
= \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}
+ \begin{bmatrix} 10 \\ 20 \\ 30 \end{bmatrix}
= \begin{bmatrix} 12 \\ 24 \\ 36 \end{bmatrix}
\end{align}

\lensmark{computational} That is everything axpy does. Listing 1.2 hands the identical three-vector computation to the machine, which agrees.

**Listing 1.2 (the same axpy, in NumPy)**

```python
a, x, y = 2, np.array([1, 2, 3]), np.array([10, 20, 30])
print(a * x + y)
```

```text
[12 24 36]
```

The machine's real advantage appears at scale, and NumPy is the doorway to it. NumPy is not just math in Python. Python is a high-level wrapper around C. NumPy is a high-level wrapper around the compiled numerical libraries beneath it, BLAS and LAPACK chief among them,[^blas] and the whole numerical stack rests on those libraries. When you write NumPy you are writing a short note that says, "have the fast code do this." You write the expression and stay in mathematics. The fiddly bits happen out of sight: allocating the memory, walking the strides, dispatching the right kernel, calling into Fortran BLAS. You focus on the ideas and let the machine do the computing.[^gpu]

[^blas]: BLAS, the [Basic Linear Algebra Subprograms](https://www.netlib.org/blas/), is the standardized set of vector and matrix routines (axpy among them) that hardware vendors tune for their chips. LAPACK, the [Linear Algebra PACKage](https://www.netlib.org/lapack/), builds the higher operations, solving systems, factorizations, eigenproblems, on top of BLAS. Both are Fortran, both date to the era the preface's tradition grew from, and both are almost certainly on your machine right now.

[^gpu]: The same shape repeats at the next layer of the stack, where the software tricks meet the hardware trick. PyTorch and TensorFlow are high-level wrappers around CUDA kernels running these same operations on graphics hardware, thousands of arithmetic units taking the entries in parallel. Everything in this book runs on an ordinary CPU, and every speedup you will see is software finding the silicon it already had.

Now the measurement. The same expression on arrays too long for a pencil, two vectors of ten million entries, computed two ways with a clock on both. Listing 1.3 writes each version as a function.

**Listing 1.3 (axpy two ways, defined)**

```python
import time

def list_comp_in_python(a: float, x: np.ndarray,
                        y: np.ndarray) -> list:
    return [a * xi + yi for xi, yi in zip(x, y)]

def vectorized_in_numpy(a: float, x: np.ndarray,
                        y: np.ndarray) -> np.ndarray:
    return a * x + y
```

Listing 1.4 runs both on the ten-million-entry arrays and prints the gap.

**Listing 1.4 (the race)**

```python
a = 2.5
rng = np.random.default_rng(0)
x, y = rng.random(10_000_000), rng.random(10_000_000)

t0 = time.perf_counter(); list_comp_in_python(a, x, y)
t_loop = time.perf_counter() - t0
t0 = time.perf_counter(); vectorized_in_numpy(a, x, y)
t_vec = time.perf_counter() - t0

print(f'list comprehension: {t_loop:5.2f} s')
print(f'vectorized:         {t_vec * 1e3:5.0f} ms')
print(f'factor:             {t_loop / t_vec:5.0f}x')
```

```text
list comprehension:  6.09 s
vectorized:            79 ms
factor:                77x
```

Both return the same numbers. They do not take the same time.[^machine] The list comprehension is dozens of times slower, and the gap only widens with $n$. Listing 1.5 runs the same contest across sizes from a thousand to ten million. Figure 1.2 is its output.

[^machine]: Every figure and number in this book is produced by the companion notebooks at [github.com/joshuacook/clae-code](https://github.com/joshuacook/clae-code), run on a 4-vCPU cloud virtual machine with no GPU. Your own machine will print different numbers, and the gap will still be there, about this size.

**Listing 1.5 (the race, swept)**

```python
def best(fn, a, x, y, reps: int = 3) -> float:
    times = []
    for _ in range(reps):
        t0 = time.perf_counter(); fn(a, x, y)
        times.append(time.perf_counter() - t0)
    return min(times)

ns = np.logspace(3, 7, 9).astype(int)
t_loop = [best(list_comp_in_python, a, rng.random(n), rng.random(n))
          for n in ns]
t_vec = [best(vectorized_in_numpy, a, rng.random(n), rng.random(n))
         for n in ns]
plt.semilogx(ns, t_loop, 'o-')
plt.semilogx(ns, t_vec, 's-')
plt.show()
```

![axpy timing: loop vs vectorized](figures/fig_axpy_timing.png)

> **Figure 1.2.** Wall-clock time of `list_comp_in_python` against `vectorized_in_numpy`, swept over $n$ from a thousand to ten million, with a log x-axis and a linear y-axis. The vectorized call stays flat against the floor while the list comprehension's cost climbs away.

The loop is slow because Python is doing far more than arithmetic. For each of the ten million entries the interpreter resolves types, boxes and unboxes objects, checks bounds, and dispatches the operators. Only underneath all of that does it finally multiply and add. NumPy skips every bit of that per-entry overhead. The whole array goes to a compiled loop the interpreter never re-enters. That is where the gap comes from. It is a software win, not a hardware trick.

The operation that compiled loop is built around is axpy, and at the very bottom axpy is a single hardware instruction, the fused multiply-add, that modern processors run many of at once. So it is software the whole way down to one operation the silicon was built to do in a single step: scale, and add.

Why has this much engineering been spent on one small operation? Because nearly everything we want to compute is built out of it, and the rest of this book is the itemized receipt. Least squares finds the combination of features closest to a price. Principal component analysis finds the combinations that carry the most variation. The Kalman filter blends a prediction and a measurement into one combination and calls it an estimate. Each of those is chapters away, and each is this section's operation wearing a job title. This book teaches you to recognize the combination inside each of them, and then to choose its weights.

## 1.6 A vector is also a function

One more reading of the chapter's object, saved for last because it needed everything above it. A vector is also a function. Hand a vector in $\mathbb{R}^{10}$ an index from 1 to 10 and it hands you a number; that is precisely what a function with a ten-element domain does. The list $(1, 2, 3, \ldots, 10)$ *is* the function $f(x) = x$, tabulated. \lensmark{computational} The machine states this well, because building a vector by evaluating a function is a one-liner:

**Listing 1.13 (a function, tabulated)**

```python
idx = np.arange(1, 11)
print('f(x) = x  :', idx)
print('f(x) = x^2:', idx**2)
```

```text
f(x) = x  : [ 1  2  3  4  5  6  7  8  9 10]
f(x) = x^2: [  1   4   9  16  25  36  49  64  81 100]
```

Listing 1.14 draws both tabulations against their index; Figure 1.13 is its output, and it looks exactly like a plot of the two functions, because it is one.

**Listing 1.14 (the tabulations, drawn)**

```python
fig, (l, r) = plt.subplots(1, 2, figsize=(9, 3.2))
l.stem(idx, idx)
l.set_title('f(x) = x, tabulated')
r.stem(idx, idx**2)
r.set_title('f(x) = x^2, tabulated')
```

![two functions, tabulated as vectors](figures/fig_vector_as_function.png)

> **Figure 1.13.** The vectors of Listing 1.13 plotted against their index. Each is a function, sampled and stored, and the plot of the vector is the plot of the function.

Each array is a function of its index, sampled and stored. Read this way, `np.arange` and friends are not conveniences; they are function tabulators, and every vector in this book has been a tabulated function all along.

And Section 1.5's engine now earns a second reading. Run axpy on two tabulated functions and the output is the tabulation of the combined function, entry by entry:

**Listing 1.15 (axpy combines functions)**

```python
grid = np.linspace(0, 2*np.pi, 1_000_000)
f, g = np.sin(grid), np.cos(grid)
h = 2 * f + g   # axpy on a million samples
err = np.abs(h - (2*np.sin(grid) + np.cos(grid))).max()
print('h is the tabulation of 2 sin + cos, to', err)
```

```text
h is the tabulation of 2 sin + cos, to 0.0
```

The compiled loop that won Section 1.5's race is, on this reading, a function-combiner: it built the function $2\sin + \cos$ from samples of its parts, a million points at once. Chapter 2 will exploit exactly this, building operations on functions out of arithmetic on their samples.

Why does the reading matter? Because functions scale and add, pointwise, exactly the way vectors do entrywise. Scale $f$ by $a$ and add $g$, and $(af + g)(x) = a f(x) + g(x)$ is again a function. Both closure clauses of Definition 1.3 hold, so collections of functions form vector spaces, and every result in this chapter, span, independence, basis, coordinates, the standing questions, applies to functions with nothing re-proved.[^function] The dividends land on schedule. Chapter 2 differentiates a sampled function by multiplying a matrix into it. Chapter 5 will hand you random variables, which scale and add, and the algebra will already be waiting. And Chapter 14's Fourier analysis is a basis, made of functions, for a space of functions.

[^function]: The precise statement: a vector in $\mathbb{R}^n$ is a function from $\{1, \ldots, n\}$ to $\mathbb{R}$. Widen the domain to a continuum and the same algebra runs on functions themselves. The linearity of the derivative, $(af + g)' = af' + g'$, which Chapter 2 stands on, is exactly the statement that differentiation respects this vector-space structure.

## 1.7 Summary and exercises

One idea ran this chapter: the agreement. A vector space is a set closed under scaling and adding (Definition 1.1), a vector is anything that lives in one, and every construction that followed was the agreement paying out. The linear combination is the only move the agreement licenses (Definition 1.4), and axpy is that move at compiled speed. The span is everything the move can reach, the column space is the span wearing its matrix name (Definition 1.6), and existence asks whether a target lies inside it, answered by inspection once and broken once, both drawn. Independence separates sets whose recipes mean something from sets that manufacture rivals, uniqueness rides on it (Fact 1.1), a basis is an independent spanning set, its unique weights are coordinates, and the axes of every graph you ever drew were the standard basis in disguise. Rank counts the independent directions honestly (Definition 1.9). And a vector is also a tabulated function, so the agreement's reach extends to functions now and to random variables in Chapter 5. And the data lens is loaded: feature columns are vectors, their span is everything a linear model can predict, and Part II brings the dataset that makes both concrete.

The question the book answers is now posed. Of all the linear combinations available, which one is the estimate, and how do we earn it?

**Exercises**

A few of these are quiz-shaped on purpose.

1. *(pencil)* Compute $3(1, -1, 2) + (0, 4, -1)$ entrywise. Then write the result as a combination of $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ and check that the weights are exactly the entries.
2. *(keyboard)* Time `list_comp_in_python` against `vectorized_in_numpy` on your own machine, over a sweep of sizes. Explain the gap you measure in terms of what the interpreter does per entry and what BLAS does per array.
3. *(pencil)* Is $(5, 5)$ in the span of $(2, 1)$ and $(1, 3)$? Exhibit the recipe or show that none exists, by inspection, and verify your candidate. Name the standing question each half of your work answers.
4. *(pencil)* Show that the line $\{t\mathbf{v} : t \in \mathbb{R}\}$ through the origin is a subspace: check the origin and both closure clauses of Definition 1.3.
5. *(pencil, then keyboard)* Choose three vectors in $\mathbb{R}^3$ and decide independence: exhibit a combination equal to zero, or argue none exists. Check yourself in code by computing the combination you exhibited.
6. *(pencil)* Using the basis $\{(1, 0), (1, 1)\}$ of $\mathbb{R}^2$, find the coordinates of $(7, 2)$, and verify your recipe by expanding it.
7. *(pencil, bridge → Ch 2)* Write the claim "$\mathbf{b}$ is the combination $c_1$ of one column plus $c_2$ of another" as a rectangular array of numbers multiplying a column of weights. Which part is the combination's weights? You have just invented the next chapter.
8. *(keyboard)* Rebuild the right panel of Figure 1.10 with `w = 2 * v`, and describe what happens to the cloud. Which case of Section 1.4 did you just draw?
9. *(pencil)* For the dependent pair $(2, 1)$ and $(4, 2)$, characterize every target for which existence holds, in one sentence and one drawing. Then name a target for which it fails and prove the failure with the ratio test used in Section 1.3.
10. *(pencil)* The system $x + y = 3$, $2x + 2y = 6$ has clean numbers. Exhibit a solution by inspection, verify it, then exhibit a second solution. Which standing question just failed, and what is the rank of the columns?
11. *(keyboard)* Tabulate $f(x) = \sin(x)$ on `np.linspace(0, 2*np.pi, 12)` and confirm the closure clauses at machine precision: check that `2*f + g` computed entrywise equals the tabulation of the function $2\sin + \cos$. Say in one sentence why this had to work.
