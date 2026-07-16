# Math review census — 2026-07-16 (findings for discussion, no prose touched)

Per Josh's frame: not mistake-hunting. Two questions. (1) Clear objectives
and achieving them. (2) Does the system build on itself in both an
intuitive and complete way. Companion instrument:
chapter_notes/clae-system-map.md (dependency map + promise ledger).
Rulings requested are marked **RULE**.

## Part 1 — Objectives

### Proposed per-chapter objective sets (extracted from the drafts; RULE each set)

**Preface** — after reading it, the reader:

- P1. knows the two roads and the church this book is written in, and
  holds the creed.
- P2. holds the four mathematical lenses, the ordering law, and the
  margin-tag device.
- P3. has the windmill machinery restored at working strength (solve a
  small system by elimination + back substitution; multiply matrices
  three ways).
- P4. knows the book's two subjects, linearity and estimation, and THE
  question that joins them.
- P5. has seen the destination drawing and knows it waits in Chapter 11.
- P6. has watched a matrix be a verb once (D took a derivative).

**Chapter 1** — the reader can:

- 1a. see one vector four ways (arrow, list, array, column).
- 1b. form and recognize linear combinations and axpy, by hand and at
  machine scale, and say why the machine is fast.
- 1c. state the closure contract and say what assuming linearity buys.
- 1d. decide span membership by solve-and-verify, naming existence and
  uniqueness.
- 1e. take a vector apart into coordinates against a basis, and say why
  the recipe is unique (the license).
- 1f. factor a vector into magnitude and direction, compute direction
  agreement (cosine similarity), and recognize orthogonality.
- 1g. read a two-feature regression as a linear combination, price a
  house by hand, and read the misses.

**Chapter 2** — the reader can:

- 2a. read a matrix as container (both readings) and as verb, and
  reconstruct any linear transformation from where the basis lands.
- 2b. compute the matrix-vector product both ways and say which view is
  for computing and which for understanding.
- 2c. compose transformations, and use the identity/inverse pair
  (transpose held as notation).
- 2d. read the geometric verbs, and work a projection by hand (score,
  calibrate, stretch) with its two properties.
- 2e. run the verb backwards: existence via the column space, uniqueness
  via the null space, and name the two non-square regimes.
- 2f. standardize honestly (affine, disclosed), one-hot encode, and put
  numerics and indicators in one currency (Gelman).

### Achievement audit (objectives vs the anatomy stations)

Mostly clean. The exceptions:

- A1. **2d "closest point" is stated, never shown** (see F3). The
  objective as written overpromises what the chapter establishes.
- A2. **2c has no undo exercise.** The inverse is defined, worked
  (telescoping), and run, but no exercise asks the reader to undo
  anything. Cheap fix at the next pass. **RULE: add one?**
- A3. **1c closure has no RUN station** (no machine beat). Likely fine,
  closure is not computational; flag for completeness. **RULE: declare
  n/a?**
- A4. **Preface P3 has no exercise station by design** (prefaces don't
  carry exercises). Declared n/a.

### In-book objectives (RULED: objectives live in the book AND the outline)

Proposed in-book form: a short chapter-opening passage in the book's
voice, prose not bullets, placed between the chapter title and the first
section; essentially the exit state promoted to the front. Draft for
Chapter 1 (for ruling, then same treatment for Ch 2; preface likely
exempt since it IS the book's objectives):

> One operation runs this chapter. By its end you can see a vector four
> ways, build anything a set of vectors can reach, say when a target is
> reachable and when its recipe is one of a kind, take a list of numbers
> apart into coordinates, and measure how strongly two directions agree.
> Chapter 2 will put the same operation inside a matrix.

**RULE: form (prose vs bullets), placement, and whether the preface gets
one.** Ledger copy: the objective set heads each chapter's
paragraph-outline file, which becomes the chapter outline proper.

### Course confrontation (both sources, per ruling 3)

- Lesson 001 (Define Vector Spaces / Perform Vector Operations /
  Visualize Vector Operations) → all three land in Ch 1 (1.2, 1.1–1.2,
  the TikZ+figure program). ✓
- Lesson 002 (Matrices as Column Vector Collections / Matrix-Vector
  Multiplication / Solve Linear Systems / Interpret Geometrically) →
  first, second, fourth land in Ch 2 (2.1, 2.2, 2.3). **Delta D1: "Solve
  Linear Systems Using Matrices" was a taught APPLY objective; the book
  deliberately makes solving a windmill (assume-GE policy). RULE: is
  solving an objective anywhere in the book, or permanently assumed?**
- Lesson 003 (four subspaces, per the coverage note) → the book staggers:
  column space and null space arrive in Ch 2, the other two are promised
  to Ch 11. **Delta D2: the course taught all four together, the book
  splits 2+2. Flag as deliberate; RULE to confirm.**
- Course-level outcome "Master the principles of vector spaces, matrices,
  and linear transformations" → jointly Ch 1 + Ch 2. ✓ The remaining
  course outcomes belong to Parts II–III and go to the ledger as each
  chapter arrives.

## Part 2 — The build (completeness and intuitiveness findings)

- **F1 (ORDERING).** Def 1.14 (unit vector) builds on the norm; the norm
  is Def 1.15, one definition later. Fix at next pass: swap the two
  definitions, or fold "norm one" into 1.15 and let the unit circle
  follow. **RULE the shape.**
- **F2 (UNSTATED HYPOTHESIS).** Claim 2.3 says "every linear
  transformation on R^n is given by exactly one matrix"; the chapter's
  own D is a map between different-sized spaces the moment the grid ends
  differ, and the honest statement is R^n → R^m with an m×n matrix.
  One-clause fix.
- **F3 (OVERCLAIM / UNDECLARED PROMISE).** Def 2.13 asserts projection
  "sends each vector to its closest point on that line." Closest is
  established nowhere in Ch 2 (C2.14 gives idempotence + orthogonal
  residual, not nearest). Ch 11 proves it. Fix: promise-tag it ("Chapter
  11 earns the word closest") or add the one-breath nearest argument.
  **RULE which.**
- **F4 (STEALTH CONCEPT).** Rank is used (matrix_rank listing, "measures
  the reach," exercise 9's rank + nullity) but never defined. Options:
  define it in 2.4 (it is one sentence given D2.15: the dimension of the
  column space), or declare it a named debt to Ch 11 like the others.
  Defining it is cheap and the machinery (dimension) already exists.
  **RULE.**
- **F5 (WEAK ARRIVES-FOR).** The transpose arrives in the "toolkit" trio
  with no summoning need; its first real use is two pages later inside
  the projection formula. Intuitive-build fix: introduce it where the
  projection needs it. **RULE.**
- **F6 (LOOSE, probably fine).** "Angle between directions" in Def 1.16
  is, in n dimensions, defined BY the ratio rather than measurable
  independently; the Cauchy–Schwarz footnote is what makes the
  definition well-posed. At the ruled rigor this is acceptable and
  already parked; recorded so the system map is honest.
- **F7 (UNDECLARED WINDMILL).** Ch 2's standardization uses mean and
  standard deviation, which the book has neither defined nor declared
  assumed. The preface's windmill act covers elimination and
  multiplication only. Fix: one sentence in the windmill act declaring
  the practitioner's statistics (mean, standard deviation) assumed until
  Part II rebuilds them. **RULE.**
- **F8 (DEBT TO WATCH, no action).** "Vector" is defined as a list in
  R^n, but the spells paragraph and the orbitals/Fourier promises need
  vector spaces whose vectors are functions. The bootstrap footnote
  gestures at this; Ch 3 will have to widen the definition or the
  promise quietly breaks. Recorded on the map; owner: Ch 3 drafting.

## Verdicts on Josh's two questions, as of these three documents

1. **Objectives**: implicitly present and mostly achieved; not yet
   stated anywhere ruleable. This census proposes the sets; the two
   achievement gaps that matter are A1 (closest-point) and D1 (is
   solving an objective).
2. **The build**: sound at the spine — every claim's supports exist and
   point backward, the promise ledger balances, and the arrives-for
   discipline is strong post-rewrite. The eight findings above are the
   complete list of violations; F1/F2 are mechanical, F3/F4/F7 are the
   substantive ones, F5 is the one intuitiveness repair, F6/F8 are
   recorded debts.
