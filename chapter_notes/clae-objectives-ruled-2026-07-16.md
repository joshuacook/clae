# Objectives — ruled board for the linear-algebra piece (2026-07-16)

Scope per Josh: "focus on the linear algebra piece right now... we will
revisit the later chapters after we get the linear algebra piece solid."
Ruled: Preface + Chapters 1-4. Chapters 5+ carry derived sets in the
2026-07-16 math census, parked.

Session rulings folded in: preface objectives made mathematical; 1f
(measurement) to the preface; 1g (the regression claim) to Ch 3's door;
new Ch 3 (Solving), chapters renumbered (15 total, flag for Springer);
Ch 2 D-led; rotations cut to the drawer (pay: Ch 10 SVD rotate-stretch-
rotate); composition witnessed by K built from D; FTLA staged (first
installment Ch 3, full theorem Ch 12); determinant declared a windmill
(procedure everyone has seen; used matter-of-factly at Ch 4, never
taught); one-hot/Gelman/X_g move to the estimation part, standardization
keeps its Ch 2 job as a live affine transformation (REC, accepted in
discussion); scaling survives in Ch 2 (diagonal matrices pay immediately
and again at Lambda).

## Preface

- P1. knows the two roads and the church; holds the creed.
- P2. holds the four mathematical lenses, the ordering law, the margin
  device.
- P3. solves a small system by elimination + back substitution, equations
  and matrix form.
- P4. multiplies matrices three ways and says what each way is for.
- P5. factors any vector into magnitude x direction on the unit circle;
  computes direction agreement (cosine similarity); recognizes
  orthogonality as agreement zero. [plants correlation promise -> Ch 7]
- P6. holds THE question and the destination drawing. [the D story stays
  as witness; the capability belongs to Ch 2]

## Chapter 1 — Vectors and Linear Combinations

- 1a. see one vector four ways.
- 1b. form/recognize linear combinations and axpy, by hand and at
  machine scale; say why the machine is fast.
- 1c. state the closure contract and what assuming linearity buys.
- 1d. decide span membership by solve-and-verify, naming existence and
  uniqueness.
- 1e. take a vector apart into coordinates against a basis; the license
  planted.
[Data lens stays at Method weight: columns are vectors, homes are points.
No regression claim. One arc: combinations -> span -> basis ->
coordinates.]

## Chapter 2 — Matrices and Linear Transformations (D-led)

- 2a. read a matrix as container (both readings) and as verb, LED BY D:
  watch a matrix differentiate; read the difference quotient inside it.
- 2b. say what property made 2a possible (the derivative is linear);
  reconstruct any linear transformation from where the basis lands
  (witnessed by a diagonal matrix and by D, not a rotation).
- 2c. compute the product both ways; which view computes, which
  understands.
- 2d. compose transformations, witnessed by building K from D; the
  identity/inverse pair (differencing undone by summing).
- 2e. work a projection by hand with its two properties; read a diagonal
  matrix as per-axis scaling.
- 2f. run the verb backwards structurally: existence via column space,
  uniqueness via null space; the two non-square regimes.
- 2g. recognize standardization as an affine transformation, disclosed
  honestly. [Z-building -> Ch 7 front porch; one-hot/Gelman/X_g -> the
  estimation part]

## Chapter 3 — Solving Linear Systems (new)

- 3a. answer both standing questions structurally before computing; the
  FIRST INSTALLMENT of the fundamental theorem (rank-nullity; reach and
  crush as the complete accounting). [full FTLA w/ orthogonality -> Ch 12]
- 3b. the license as a method: see integer solutions, verify, done.
- 3c. elimination as the systematic fallback, owned.
- 3d. elimination as matrices acting; A = LU.
- 3e. diagnose one/none/infinitely-many, drawn.
- 3f. call solve, know it is LU, verify the machine with a residual.
- 3g. read a two-feature regression as a linear combination, price a
  house by hand, read the misses; watch exactness die at the third
  house. The door to estimation. [absorbs old 1g; Josh flagged this may
  split — carries two loads]

## Chapter 4 — Eigenvalues, Eigenvectors, and Diagonalization

- 4a. recognize eigenvectors as directions a verb merely stretches; find
  small cases by hand via the null space of A - lambda I (Ch 3 machinery
  pointed at a new target; det used as a windmill procedure, never
  taught).
- 4b. verify any claimed eigenpair by multiply-and-check: the license's
  home turf.
- 4c. diagonalize; read A = X Lambda X^-1 as change of basis.
- 4d. show K's eigenvectors are sines (waves-room theorem; eigensolver
  race exhibit).
- 4e. run the power method: guess-and-check made an algorithm.
- 4f. say why electron orbitals are a basis (preface promise, paid).

## The chapter list (15; Springer proposal says 14 — flag)

Preface · I: 1 Vectors and Linear Combinations · 2 Matrices and Linear
Transformations · 3 Solving Linear Systems · 4 Eigenvalues, Eigenvectors,
and Diagonalization · II: 5 Random Vectors and Probability Spaces · 6
Expectation and Conditional Probability · 7 Covariance, Correlation, and
Cross-Correlation · 8 Gaussian Random Vectors · 9 Convergence (LLN/CLT) ·
III: 10 SVD · 11 PCA (capstone) · 12 Least Squares Estimation · 13
Linear MMSE (capstone) · IV: 14 Estimation in Signal Processing · 15
Advanced Filtering and Modern Applications.

Ledger updates carried to the system map: rotations -> drawer, paid at
Ch 10 (SVD geometric story; angle-sum footnote candidate); determinant ->
windmill class; FTLA two installments (3, 12); measurement promise
(preface P5 -> Ch 7 correlation); one-hot/Gelman -> estimation part;
renumbered promise targets (destination drawing/lstsq/gap -> Ch 12;
symphony/PCA -> Ch 11; slabs/SVD -> Ch 10; orbitals/K-eigenvectors ->
Ch 4; complex/Fourier -> Ch 14).
