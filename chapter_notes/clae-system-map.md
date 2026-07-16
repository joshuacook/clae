# CLAE system map (standing instrument, created 2026-07-16)

The mathematical dependency structure of the live documents. Three edge
types: **builds-on** (must point backward or to a declared windmill),
**arrives-for** (the narrative need that summoned the node), and
**promises** (forward reference with a named paying chapter). New chapters
must attach their nodes here. Violations move to the math-review census
for ruling; this file records the system as it stands.

## Declared assumptions (the windmills, preface act 3)

- W1. Solving a linear system by elimination + back substitution
  (equations and matrix form).
- W2. Matrix multiplication, three ways (entry, column, outer product).
- W3. (Implicit, via the pipeline narrative) school calculus: the
  difference quotient and limits, used by the preface's D derivation.
- W4. (UNDECLARED — census finding F7) mean and standard deviation,
  used by Ch 2 standardization.

## Node inventory and builds-on edges

### Preface devices

- CREED (the church's sentence) → unpacks into the four mathematical
  lenses + ordering law. Arrives-for: the book's method.
- THE QUESTION ("which combination...") → planted at each act's stop.
- D, the derivative-taker → builds on W2, W3. Promises: Ch 2 (matrix as
  verb, PAID), eigen material (Ch 3, via Eloranta act).
- The destination drawing (b, p, b−p) → promises Ch 11.

### Chapter 1

- D1.1 vector ← (none; first object). Arrives-for: The Method.
- D1.2 linear combination, weights ← D1.1.
- D1.3 axpy ← D1.2.
- D1.4 vector space (closure clauses) ← D1.1, D1.2.
- D1.5 span ← D1.2.
- D1.6 subspace ← D1.4, D1.5.
- C1.7 span is a subspace ← D1.5, D1.6.
- D1.8 independence ← D1.2.
- D1.9 basis, dimension ← D1.5, D1.8 (size theorem in footnote, declared).
- C1.10 unique recipe ← D1.9. Carries THE LICENSE (verify-and-done).
- D1.11 coordinates ← C1.10.
- D1.12 standard basis ← D1.9.
- C1.13 span of the question ← D1.9. Ambient-space footnote.
- D1.14 unit vector, unit circle ← **D1.15 norm — FORWARD EDGE,
  violation, census F1.**
- D1.15 norm, magnitude/direction ← D1.1 (+ Pythagoras, school geometry).
- D1.16 dot product, direction agreement, orthogonality ← D1.15;
  well-definedness of the ratio parked in the Cauchy–Schwarz footnote
  (declared debt).
- Devices: the membership solve (existence/uniqueness named) ← W1;
  meshgrid-as-every; cosine similarity ← D1.16.

### Chapter 2

- D2.1 data-matrix conventions ← D1.1 (rows-as-points via Method tour).
- D2.2 linear transformation ← D1.2, D1.4.
- C2.3 matrices are the linear transformations ← D1.12, D2.2, W2
  (column way). **Statement understates domain/codomain — census F2.**
- D2.4 product, both views ← W2, D1.16 (row view = dot products).
- C2.5 views agree ← D2.4.
- D2.6 matrix-matrix product ← D2.4.
- C2.7 composition works ← D2.6, D2.2.
- C2.8 rotations compose ← C2.3, D2.6 (trig identities to exercise,
  declared).
- D2.9 identity ← C2.3.
- D2.10 transpose ← D2.1. Used notationally by D2.13; meaning promised
  to Ch 6. **Arrives-for edge weak — census F5.**
- D2.11 inverse ← D2.9, D2.6.
- C2.12 differencing/summing inverse ← D2.11, D (preface).
- D2.13 projection onto a line ← D1.16, D2.10 (outer product ← W2).
  **"Closest point" asserted, established nowhere until Ch 11 — census
  F3.**
- C2.14 projection properties ← D2.13.
- D2.15 column space ← D1.5, D2.1. Pays Ch 1's unnamed-span debt.
- D2.16 null space ← D2.2.
- C2.17 null space is a subspace ← D2.16, D1.6.
- C2.18 invertibility ⟺ trivial null space ← D2.16, D1.8, C1.13
  (dimension count leans on the D1.9 footnote theorem — declared level).
- Device: **rank — USED (matrix_rank listing, reach language, exercise
  9) BUT NEVER DEFINED — census F4.**
- Standardization z = (x − μ)/σ ← **W4 undeclared — census F7**; affine
  honesty box ← D2.2.
- One-hot encoding ← D1.1; dummy-trap ← D2.16 (promised to Ch 11).
- Gelman convention ← standardization (binary-sd argument in footnote).

## Promise ledger (every forward edge and its paying chapter)

| Promise | Made in | Paid by |
|---|---|---|
| Matrix as verb (D exhibit) | Preface | Ch 2 ✓ PAID |
| Row/point pair "made official" | Ch 1 §1.3 | Ch 2 ✓ PAID |
| Ch 1's unnamed span gets its name | Ch 1 §1.4 | Ch 2 (D2.15) ✓ PAID |
| Electron orbitals are a basis | Preface, Ch 1 spells | Ch 3 |
| K's eigenvectors "known by name" | Ch 2 exit, ex 12 | Ch 3 |
| Feature column = realizations of a random variable | Ch 1 footnote | Ch 4 |
| Indicator weight = group mean | Ch 2 §2.5 | Ch 5 |
| Transpose's deeper meaning | Ch 2 D2.10 | Ch 6 |
| Centered direction agreement = correlation | Ch 1 §1.6, ex 8 | Ch 6 |
| Z's column dot products = covariances | Ch 2 exit | Ch 6 |
| Outer-product slabs, largest first | Preface act 3 | Ch 9 |
| The symphony | Preface (Lockhart act) | Ch 10 |
| Directions that carry variation; shadow-catching lines | Ch 1 spells, Ch 2 | Ch 10 |
| The destination drawing; lstsq from parts; the gap's name | Preface, Ch 1, Ch 2 | Ch 11 |
| Projection = closest point, proven | Ch 2 D2.13 (implicit) | Ch 11 (census F3: make explicit) |
| Rank + nullity; the other two subspaces; dummy-trap hygiene | Ch 2 | Ch 11 |
| Complex exponentials; Fourier | Preface footnote, Ch 1 spells | Ch 13 |
| Cauchy–Schwarz, dwelt on never | Ch 1 footnote | (parked permanently — confirm) |
| Treks / annotated reading trail | (stock accumulating) | Back matter |
