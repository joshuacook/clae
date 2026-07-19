<!-- DRAFT V4 (2026-07-19): the v11 pass per the v10 ink census +
     rulings. Null space Def now lives in Ch2 (at projection); 3.2
     recalls it and MEASURES it (nullity + ledger). The door (Ames /
     market data) OUT to Part II stock (.render/ch3_door_block.md,
     census 14); chapter closes on the abstract overdetermined pointer.
     R1 language sweep: no "crush" coinage, technical language
     throughout. Base: V3. -->

# Chapter 3: Solving Linear Systems

## 3.0 The equation of Part I

Every road in this book runs through one equation:

\begin{align}
A\mathbf{x} = \mathbf{b}
\end{align}

A matrix acts on an unknown input, a known output sits on the right, and the job is to run the verb backwards. Chapter 1 posed this question and its two halves, loudly: **existence** (a solution exists exactly when $\mathbf{b}$ lies in the column space) and **uniqueness** (the recipe is one of a kind exactly when the columns are independent). Chapter 2 built the verb the question is about. This chapter answers it, and here is its plan.

First, the fast method: solving **by inspection** under the license, worked and drawn in full. Second, the null space of Chapter 2 gets its number, the nullity, and the dimensions of reach and loss are proved to balance. Third, the diagnosis discipline: every system's fate read off before any solving. Fourth, the machine: elimination, owned and then read as a factorization, $A = LU$, with the computer held to the same standard of proof as your own pencil. Last, the door out of the exact world, where the data of this book actually lives.

## 3.1 Solving by inspection

The first method is the fastest one mathematics has, and Chapter 1 already paid for it. The license: when the diagnosis says the solution is unique, any verified candidate *is* the solution. So the working method for small systems is to produce the candidate **by inspection**, the technical name for looking at the system until you see the answer, and then to verify. The verification is not a courtesy. It is the entire proof, and the license is what makes it sufficient.

\lensmark{algebraic} **Seen from the numbers.** The columns of this system are independent (check: they are not multiples), so the license holds:

\begin{align}
\begin{aligned} x + y &= 5 \\ x - y &= 1 \end{aligned}
\end{align}

Two numbers that sum to 5 and differ by 1. You can *see* $(3, 2)$. Verify: $3 + 2 = 5$ and $3 - 2 = 1$. Solved, with full rigor, and nothing was eliminated.

**Seen from the structure.** The next system rewards reading before writing:

\begin{align}
\begin{aligned} 2x + y &= 7 \\ x + y &= 4 \end{aligned}
\end{align}

The two equations differ by exactly $x$, so subtracting them in your head gives $x = 3$, and then $y = 1$. Verify: $6 + 1 = 7$ and $3 + 1 = 4$. Structure produced the candidate; the check made it law.

**Seen from Chapter 1.** The third system is one you have already solved without a matrix in sight:

\begin{align}
\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} 4 \\ 7 \end{bmatrix}
\end{align}

In column language this asks for Chapter 1's membership recipe, and the recipe $c = 1$, $d = 2$ was exhibited and verified there. A system of equations, a membership question, and a matrix-vector equation are one object in three notations, and by inspection works on all three.

\lensmark{geometric} Each two-unknown system also draws, and the drawing is the **row picture**: each equation is a line in the plane, and a solution is a point every line passes through. Figure 3.1 draws the first two systems this way, and the seen candidates are visibly the crossings.

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.6]
  \begin{scope}[shift={(0,0)}]
    \draw[gray!30, ->] (-0.8,0) -- (6.2,0);
    \draw[gray!30, ->] (0,-0.8) -- (0,6.2);
    \draw[thick] (-0.5,5.5) -- (5.5,-0.5) node[below right] {\scriptsize $x + y = 5$};
    \draw[thick, gray] (0.5,-0.5) -- (6.0,5.0) node[above right] {\scriptsize $x - y = 1$};
    \fill (3,2) circle (3.5pt);
    \node[below right] at (3.05,2.0) {$(3, 2)$};
    \node[anchor=north] at (2.8,-1.2) {\small sum 5, differ 1: see the crossing};
  \end{scope}
  \begin{scope}[shift={(10.5,0)}]
    \draw[gray!30, ->] (-0.8,0) -- (6.2,0);
    \draw[gray!30, ->] (0,-0.8) -- (0,6.2);
    \draw[thick] (0.8,5.4) -- (3.4,0.2) node[below] {\scriptsize $2x + y = 7$};
    \draw[thick, gray] (-0.5,4.5) -- (4.5,-0.5) node[below right] {\scriptsize $x + y = 4$};
    \fill (3,1) circle (3.5pt);
    \node[above right] at (3.05,1.05) {$(3, 1)$};
    \node[anchor=north] at (2.8,-1.2) {\small the equations differ by $x$};
  \end{scope}
\end{tikzpicture}
\caption{Solving by inspection, drawn in the row picture. Each equation is a line; the solution is the crossing. Left, the seen candidate $(3,2)$ sits where the sum-is-5 and differ-by-1 lines meet. Right, $(3,1)$ sits where the two lines meet, and subtracting one equation from the other leaves $x = 3$ on sight, which is what made the candidate visible.}
\end{figure}

Hold both pictures. Chapter 1 drew the **column picture**, recipes reaching a target tip to tail. The row picture drawn here is the other geometry of the same equation, and elimination, two sections from now, is nothing but row-picture surgery. The discipline in one line: **diagnose, see, verify.** Diagnose independence so the license holds, produce a candidate by inspection, verify it against every original equation. When any of the three steps fails to go through, and past three unknowns it usually does, the machine of Section 3.4 takes over with the same guarantees.

## 3.2 The null space, measured

Chapter 2 defined the null space at the scene of its first destruction, the projection, and tied invertibility to it. This section measures it. \lensmark{computational} Listing 3.1 builds two specimens: the difference matrix $A_3$ from Chapter 2, and a new **cyclic** difference matrix $C$, whose differences wrap around.

**Listing 3.1 (the two specimens)**

```python
import numpy as np

A3 = np.array([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])  # difference
C = np.array([[1, 0, -1], [-1, 1, 0], [0, -1, 1]])  # cyclic
```

Feed $C$ a constant vector and watch what it does.

**Listing 3.2 (a nontrivial null space, exhibited)**

```python
print('C @ (3,3,3):', C @ np.array([3, 3, 3]))
```

```text
C @ (3,3,3): [0 0 0]
```

$C$ sends $(3, 3, 3)$ to zero, and it sends every constant vector to zero the same way: shift a sequence by a constant and its wrapped differences never notice. The whole line of constant vectors lies in $C$'s null space, two different inputs map to one output, and Chapter 2's Claim 2.6 already says what that costs: no inverse, and uniqueness dead on arrival for any system built on $C$. It draws. Listing 3.3 feeds $C$ two inputs that differ by a constant shift and plots both against their outputs; Figure 3.2 is its output.

**Listing 3.3 (two inputs, one output, drawn)**

```python
import matplotlib.pyplot as plt

x1 = np.array([3., 5, 6])
x2 = x1 + 4
fig, (l, r) = plt.subplots(1, 2, figsize=(9, 3.5))
l.plot(x1, 'o-', label='x')
l.plot(x2, 's-', label='x + 4')
l.set_title('two different inputs')
l.legend()
r.plot(C @ x1, 'o-', lw=3, label='C @ x')
r.plot(C @ x2, 's--', label='C @ (x + 4)')
r.set_title('one output')
r.legend()
```

![two inputs, one output](figures/fig_crush.png)

> **Figure 3.2.** Two different inputs, one output. The shift by a constant lies in $C$'s null space, so the matrix cannot tell the two inputs apart. Uniqueness dies here: given one solution of $C\mathbf{x} = \mathbf{b}$, adding the shift gives another.

The null space of $A_3$, by contrast, is $\{\mathbf{0}\}$ alone, which is exactly why Chapter 2 could invert it. Both of the standing questions now have a space: the column space holds existence, the null space holds uniqueness, and the two keep a joint ledger.

The column space and the null space are not independent bookkeeping. They are two entries in one ledger, and the ledger balances. The bookkeeping needs two numbers.

> **Definition 3.1 (nullity; rank recalled).** The **rank** of a matrix (Definition 1.10, now in matrix clothes) is the dimension of its column space, the number of dimensions the operator can reach. The **nullity** is the dimension of its null space (Definition 2.7), the number of independent directions the operator sends to zero.

> **Claim 3.1 (rank and nullity balance the ledger).** For an $m \times n$ matrix, rank $+$ nullity $= n$. Every input dimension either survives into the column space or dies in the null space. None goes missing.
>
> Witness it on $C$: three input dimensions, a plane of reach (rank 2), a line sent to zero (nullity 1), and $2 + 1 = 3$. The one-breath reason: pick a basis for the null space and extend it to a basis of $\mathbb{R}^n$; the extension vectors map to a basis of the column space, because anything their images failed to reach would trace back to more of the null space.[^ftla]

[^ftla]: This is the first installment of what Strang calls the fundamental theorem of linear algebra. The full theorem has four subspaces and a pair of right angles between them, and it arrives with the machinery that needs it, in Chapter 12.

\lensmark{computational} The machine keeps this ledger on request. Listing 3.4 audits $C$ against the well-behaved difference matrix from Chapter 2.

**Listing 3.4 (the ledger, audited)**

```python
for name, M in [('A3', A3), ('C ', C)]:
    r = np.linalg.matrix_rank(M)
    print(f'{name}: rank {r}, nullity {M.shape[1] - r}')
```

```text
A3: rank 3, nullity 0
C : rank 2, nullity 1
```

Rank 3 of 3 means the column space is everything and the null space is trivial. Rank 2 of 3 means a plane of reach and a line sent to zero. Everything this chapter does flows from that one audit.

## 3.3 Three outcomes, diagnosed

Cross the two questions and $A\mathbf{x} = \mathbf{b}$ has exactly three possible fates. \lensmark{geometric} Each one draws:

\begin{figure}[!htb]
\centering
\begin{tikzpicture}[scale=0.72]
  \begin{scope}[shift={(0,0)}]
    \fill[gray!12] (-1.5,-0.9) -- (1.7,-0.9) -- (2.5,0.7) -- (-0.7,0.7) -- cycle;
    \draw[->, very thick] (0,0) -- (1.4,0.25) node[right] {$\mathbf{b}$};
    \node[anchor=north] at (0.5,-1.1) {\scriptsize one solution};
    \node[gray, anchor=south] at (0.5,0.75) {\tiny full reach, trivial null space};
  \end{scope}
  \begin{scope}[shift={(5.6,0)}]
    \fill[gray!12] (-1.5,-0.9) -- (1.7,-0.9) -- (2.5,0.7) -- (-0.7,0.7) -- cycle;
    \draw[->, very thick] (0,0) -- (0.7,1.6) node[above] {$\mathbf{b}$};
    \node[anchor=north] at (0.5,-1.1) {\scriptsize no solution};
    \node[gray, anchor=south] at (0.5,0.75) {\tiny $\mathbf{b}$ off the reach};
  \end{scope}
  \begin{scope}[shift={(11.2,0)}]
    \fill[gray!12] (-1.5,-0.9) -- (1.7,-0.9) -- (2.5,0.7) -- (-0.7,0.7) -- cycle;
    \draw[->, very thick] (0,0) -- (1.4,0.25) node[right] {$\mathbf{b}$};
    \draw[gray, thick, dashed] (-0.9,-0.6) -- (1.1,1.1);
    \node[anchor=north] at (0.5,-1.1) {\scriptsize infinitely many};
    \node[gray, anchor=south] at (0.5,0.75) {\tiny reached, null space to spare};
  \end{scope}
\end{tikzpicture}
\caption{The three fates of $A\mathbf{x} = \mathbf{b}$. Left, the target is reachable and the null space is trivial, so exactly one recipe exists. Middle, the target lies off the column space and no recipe exists. Right, the target is reachable but the null space (dashed) is nontrivial, so a whole family of recipes reaches it.}
\end{figure}

The diagnosis runs on the audit, before any solving. If $\mathbf{b}$ is outside the column space, stop: no solution, and Chapter 12 will teach you to get close instead. If $\mathbf{b}$ is inside and the nullity is zero, exactly one solution exists, and the hunt is licensed. If $\mathbf{b}$ is inside and the nullity is positive, solutions form a family, one particular solution plus anything from the null space.

Run all three on the two matrices in hand. The difference matrix $A_3$ reaches everything and sends only $\mathbf{0}$ to zero: one solution for every target. The cyclic $C$ with $\mathbf{b} = (1, 3, 5)$: the target is off the plane, no solution. The same $C$ with a target on the plane, say $\mathbf{b} = C(1, 2, 3) = (-2, 1, 1)$: reached, but the constants come free, so $(1, 2, 3) + t(1, 1, 1)$ solves for every $t$.

## 3.4 Elimination, owned

Section 3.1's method is real and this book reaches for it first everywhere. But it has a working range. Big systems, ugly numbers, and machine-scale data refuse to be seen, and for those you need a procedure that cannot lose, run by hand or by machine. The preface restored elimination as a windmill. This section makes it yours, because from here on the book uses it without narration. The method: subtract multiples of one equation from the others to kill unknowns, march the zeros in below the diagonal, then climb back up. \lensmark{algebraic} The full 3×3, worked in matrix form:

\begin{align}
\begin{bmatrix} 1 & 2 & 1 \\ 2 & 5 & 4 \\ 1 & 3 & 5 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
= \begin{bmatrix} 5 \\ 13 \\ 12 \end{bmatrix}
\end{align}

Row 2 minus twice row 1, and row 3 minus row 1, kill the first column below the pivot. Then row 3 minus the new row 2 kills the second:

\begin{align}
\begin{bmatrix} 1 & 2 & 1 \\ 2 & 5 & 4 \\ 1 & 3 & 5 \end{bmatrix}
\;\longrightarrow\;
\begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 4 \end{bmatrix}
\;\longrightarrow\;
\begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 2 \end{bmatrix},
\qquad
\mathbf{b} \longrightarrow \begin{bmatrix} 5 \\ 3 \\ 4 \end{bmatrix}
\end{align}

Triangular, so back substitution climbs: $2z = 4$ gives $z = 2$; then $y = 3 - 2(2) = -1$; then $x = 5 - 2(-1) - 2 = 5$. And per Chapter 1's discipline, verify the candidate against the original system: $5 + 2(-1) + 2 = 5$, and $2(5) + 5(-1) + 4(2) = 13$, and $5 + 3(-1) + 5(2) = 12$. All three hold. The recipe is $(5, -1, 2)$, and the diagnosis (three independent columns, rank 3) says it is the only one.

## 3.5 The algorithm is a factorization

Here is the payoff Chapter 2 set up, and it is the reason this chapter sits after the matrix and not before it. Every move elimination made was itself a linear transformation, so by Claim 2.3 every move is a matrix. "Row 2 minus twice row 1" is the identity with a $-2$ planted below the diagonal. Elimination is not a procedure that happens *to* matrices. It *is* matrices, composed.

Run the bookkeeping. Each elimination step is a matrix multiplying $A$ from the left, and undoing the whole sequence collects the multipliers, exactly the numbers you used, into a lower triangle $L$. What remains after elimination is the upper triangle $U$. The record reads:

> **Claim 3.2 (elimination is a factorization).** When elimination runs without row exchanges, it factors the matrix: $A = LU$, with $U$ the triangle elimination produced and $L$ the lower triangle holding the multipliers, ones on its diagonal.[^pivot]
>
> Witness it on the worked example. The multipliers were $2$, $1$, and $1$:
>
> $$L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 2 \end{bmatrix}, \quad LU = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 5 & 4 \\ 1 & 3 & 5 \end{bmatrix} = A$$
>
> The one-breath reason: each step is invertible (add back what you subtracted), and the product of the undo-steps is lower triangular with the multipliers sitting where they acted.

[^pivot]: When a zero lands in a pivot position, elimination swaps rows first, and the honest factorization is $PA = LU$ with $P$ a permutation matrix. Production code pivots even when it does not strictly have to, for numerical stability, which is why the machine's $L$ and $U$ for this very matrix look different from ours and multiply back to a row-swapped $A$. Same theorem, defensive driving.

\lensmark{computational} Listing 3.5 multiplies the hand factorization back together.

**Listing 3.5 (the record, verified)**

```python
A = np.array([[1., 2, 1], [2, 5, 4], [1, 3, 5]])
L = np.array([[1., 0, 0], [2, 1, 0], [1, 1, 1]])
U = np.array([[1., 2, 1], [0, 1, 2], [0, 0, 2]])
print('max |L @ U - A|:', np.abs(L @ U - A).max())
```

```text
max |L @ U - A|: 0.0
```

Why care that the algorithm is a factorization? Because the factorization is reusable. Solving $A\mathbf{x} = \mathbf{b}$ through $LU$ is two triangular solves, one forward and one back, and when a second target $\mathbf{b}'$ arrives, the expensive part, the elimination, is already done and stored. That observation is worth more in practice than any single solve, and it is precisely what the machine does on your behalf.

## 3.6 The machine, verified

`np.linalg.solve` is the production solver, and underneath it is LAPACK running exactly the factorization of Section 3.4, pivots and all. This book's epistemology does not exempt the machine. A solver returns a candidate, and candidates get verified. The verification even has a name, the **residual**, the vector $\mathbf{b} - A\hat{\mathbf{x}}$ that measures how far the returned answer is from doing its job. Listing 3.6 solves the worked system and holds the answer to Chapter 1's standard.

**Listing 3.6 (solve, then verify the machine)**

```python
b = np.array([5., 13, 12])
x_hat = np.linalg.solve(A, b)
print('x_hat   :', x_hat)
print('residual:', np.abs(b - A @ x_hat).max())
```

```text
x_hat   : [ 5. -1.  2.]
residual: 0.0
```

The machine found the same $(5, -1, 2)$ the pencil did, and the residual certifies it. Make the residual check a habit. It costs one multiplication, it catches everything from a mistyped matrix to a genuinely ill-behaved system, and it is the license's discipline applied to code: never trust a candidate you have not verified, no matter who produced it.

## 3.7 The edge of the exact world

Everything in this chapter assumed a square system, as many independent equations as unknowns, and inside that square world the machine is complete: diagnose, solve, verify. Real measurement does not live there. Observe the same small set of quantities many times and the system stacks far more equations than unknowns, it is **overdetermined**, and a target assembled from real observations has no reason to lie in the column space of a thin matrix. Existence fails not by accident but as the normal condition, and the two standing questions return with a sharpened edge: when no combination is exactly right, which one is *best*, and what precisely does *best* mean?

Nothing in Part I can define *best*. The word needs a way to measure how wrong a miss is and a reason to prefer one distribution of misses over another, and that is probability's department. Part II builds that equipment, on data, starting in Chapter 5, and Chapter 12 walks back through this door with the word *best* fully licensed and the drawing from the preface in hand. Everything between here and there is learning to say it precisely.

## 3.8 Summary and exercises

The equation is $A\mathbf{x} = \mathbf{b}$, and the two standing questions have spaces and now numbers: rank measures the column space, nullity measures the null space, and the ledger balances (Claim 3.1, the fundamental theorem's first installment). Diagnosis precedes solving, and the three fates are one, none, or a family. When uniqueness holds, the license is a method: see a candidate, verify it, done. When seeing fails, elimination is the systematic fallback, and elimination is not just a procedure but a factorization, $A = LU$ (Claim 3.2), reusable across targets. The machine runs the same factorization and gets held to the same standard: solve, then check the residual. And the square world has an edge: real measurement is overdetermined, existence fails as the normal condition, and *best* is a word Part I cannot define. Part II builds the equipment; Chapter 12 walks back through with it.

**Exercises**

1. *(pencil)* Diagnose before solving: for the cyclic matrix $C$ and target $(2, -1, -1)$, decide existence and uniqueness from rank and nullity, then exhibit either the family of solutions or the obstruction.
2. *(pencil)* See it: $x + y = 10$ and $x - y = 4$. Write the answer down without eliminating, then verify. State what licenses the method.
3. *(pencil)* See this one too: $3x + y = 10$, $x + y = 6$. What structural feature hands you $x$ immediately?
4. *(pencil)* Eliminate the system $x + y + z = 6$, $x + 2y + z = 8$, $x + y + 3z = 10$ in matrix form, watching the zeros arrive. Back-substitute, then verify your candidate against all three original equations.
5. *(pencil)* Collect your multipliers from exercise 4 into $L$, write down your $U$, and confirm $LU$ rebuilds the matrix by hand.
6. *(keyboard)* Verify exercise 5's factorization in code, then solve the same system with `np.linalg.solve` and print the residual.
7. *(keyboard)* Ask `scipy.linalg.lu` for the factorization of Section 3.4's matrix and compare its $L$ and $U$ to ours. They differ. Read the permutation matrix $P$ and explain why (the footnote to Claim 3.2 is the hint).
8. *(pencil)* A $4 \times 4$ matrix has rank 2. State its nullity, describe the solution set of $A\mathbf{x} = \mathbf{b}$ when $\mathbf{b}$ is reachable, and name the fate when it is not.
9. *(pencil)* Stack a third equation onto the system of exercise 4 that no solution of the first three satisfies, and diagnose the enlarged system: what happened to existence, and in which space did it happen?
10. *(pencil, bridge → Ch 12)* An overdetermined system $A\mathbf{x} = \mathbf{b}$ has no solution. Chapter 12 will replace $\mathbf{b}$ with a vector that does have one. Using Chapter 2's operators, guess which vector, and which operator produces it. One sentence.
11. *(pencil, bridge → Ch 4)* The eigenvector equation is $A\mathbf{x} = \lambda\mathbf{x}$, which rearranges to $(A - \lambda I)\mathbf{x} = \mathbf{0}$. Say which of this chapter's spaces $\mathbf{x}$ must live in, and why $\lambda$ must be chosen to make that space nontrivial. You have just set up the next chapter.
