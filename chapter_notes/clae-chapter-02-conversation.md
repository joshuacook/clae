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

## 2026-07-11 (evening sync) — two-matrix convention + rulings applied

2.5/2.6 rebuilt: categorical three-beat arc planted (2.5 contract framing →
Ch 5 group means → Ch 11 dummy trap as null-space hygiene); BOTH matrices now
exit the chapter — Z (numerics, 1 sd) and X_g (Gelman: numerics / 2 sd,
indicators raw; 1460 × 284 on Ames). One-currency demo, real numbers:
GrLivArea $59,792 and OverallQual $87,300 per 2-sd contrast, CentralAir flip
$21,426, one regression, one denomination. Gelman 2008 cited with the
p = 1/2 → sd = 1/2 footnote (plants p(1−p) for Ch 10). 2.3 comment RESOLVED:
generic line affirmed, Ames projection held for Ch 11. Particle-in-a-box
ruling still open (claude.ai making the Ch 3 case).

## 2026-07-11 (night) — retrofitted to the anatomy

Lead: Prop 2.2 (matrices ARE the linear transformations; columns are where
the basis vectors land; two-line constructive proof closing the 1.3 recipe
loop). 16 numbered items; HONESTY box (standardization is affine; T(0)=0
violated by the shift). Hand-work: R(90) by columns; project (3,4) onto (2,1)
= (4,2) integer-clean; the 1.2 membership question revealed as a system.
Props: two-views PROVE; composition SKETCH; rotation-composition VERIFY (+ex 5
completes); running-sums VERIFY + telescoping; projection PROVE; null-space
PROVE; invertibility SKETCH. 12 tiered exercises incl. the Ch 3 bridge (K on
sin(3x) vs random: meet an eigenvector) and the dummy-trap-by-hand (ex 11).
Treks: CSE, the 2015 Leanpub paper, Gelman 2008, Harris et al. NumPy Nature
paper. Jim-website footnote also grafted into preface v4 (archive.org
citation per the never-print-a-parked-domain rule).

## 2026-07-12 — RETROFIT-2 knock-ons (light)

Receives the data-matrix material as its opening beat (container arrives,
then the verb; Definition 2.1 = conventions). All items renumbered +1;
Proposition → Claim; Ch 1 cross-refs updated (Claim 1.5, Claim 1.10); treks
to stock. Proof blocks intentionally NOT yet converted to Strang-way: that
happens at the full pass when Josh's Ch 2 ink arrives. Column-space treatment
now unambiguously Ch 2 material (resolves ink #36).
