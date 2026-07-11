# Ch 2 (Matrices and Linear Transformations) — conversation notes

## 2026-07-10 (synced 2026-07-11) — footnote stock from the origin session

**The trig-magic deep cut (placement candidate: Ch 2 footnote and/or preface
texture):** sin(a+b) = (cos b)·sin a + (sin b)·cos a is a linear combination —
a rotation acting on the {sin, cos} basis. The reader knew a basis in high
school, and the trig identity sheet was its span. Kruidenier's calc 2 magic
(the whole sheet from a+b and a−b) is the lived version; Ch 2 is where
rotation-as-matrix makes it precise.

**numpy/pandas as the row/column duality's memory address (DFW footnote
candidate):** Josh: "maybe we're also cutting at how numpy wants to be row
oriented but pandas wants to be column oriented? Maybe … I'm not sure." numpy
C-order stores rows contiguously; pandas stores column blocks; strides decide
which picture is cheap. Pending the DFW-footnote method confirm.

## 2026-07-11 (synced) — the chapter's thesis, and the draft

**Josh, verbatim: "The matrix became a verb for me when I learned, finite
differences."** THE MATRIX IS A VERB is the chapter thesis; the difference
matrix (and `secondDiff`, from his 2015 Eloranta-lab paper) is the centerpiece
exhibit, with first-person provenance.

Drafted in full 2026-07-11 per the work order (finished prose + executed
companion notebook). Beats honored: Ax as column combination with x the recipe
(1.3 callback); row-vs-column product views (+ numpy/pandas memory footnote);
composition (+ trig-rotation footnote, the Kruidenier deep cut);
inverse-of-difference-is-running-sums (fundamental theorem cameo); projection
as the load-bearing geometry (idempotence + orthogonal residual verified at
machine precision); systems via the invertible difference vs the cyclic C
(constant vectors crushed, rank 3 vs 2); standardization as the affine bend of
the contract; the 1.1-weights-inverted payoff (GrLivArea $29,344/σ vs
OverallQual $45,415/σ). Two open items PROPOSED in draft comments: 2.3 example
(recommend generic line now, Ames projection in Ch 11); 2.5 categorical depth
(recommend the one paragraph). Exit state: Z, covariance-ready.
