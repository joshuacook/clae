# [Shaw] CLAE v8 Revision Punch List

Josh's 76 v8 notes grounded against the actual green highlight each marks (book pages, printed numerals). Read the top section first: several notes are not local fixes, they are **global policies**. Josh did not tag every instance, so the worker must **audit the entire book** against each policy, not just the spots called out.

Buckets: **G** global policy (audit book-wide) · **A** structural (gated on Josh) · **R** random-variable thread · **V** voice/rigor · **L** local fix.

---

## Section 1 — GLOBAL POLICIES (audit the WHOLE book, every chapter, not just tagged spots)

These are standing rules. The tagged notes below are only the instances Josh happened to mark; the worker sweeps every listing and every figure in the book and brings all of them into compliance.

- **G1 — Code never exceeds the text measure.** No listing may bleed past the text column in the rendered PDF, ever. Audit every code listing book-wide and reflow (wrap args, shorten names, break lines) until none overflow. Add it to the build so it cannot regress. *(Tagged instances: #23 Listing 1.3, #28 Listing 1.6, #49 Listing 2.1; Josh notes these are a fraction — also seen bleeding: Listings 2.2, 2.3, 2.4, 2.7, 2.11, 2.12, and any others the audit finds.)*
- **G2 — Every figure is legible.** Adequate size, no superimposed/overlapping labels, not horizontally compressed. Audit every figure book-wide. *(Tagged: #32 Fig 1.7, #47 Fig 2.1, #70 Fig 2.5 superimposed labels, #35 Fig 1.9 w reads as orthogonal.)*
- **G3 — Every code run gets a plot, wherever at all possible.** If a listing produces output or demonstrates a result, accompany it with a plot; prefer showing over stating. Audit every listing book-wide. *(Tagged: #8, #9, #53, #54, #55/#56, #60, #63, #65, #66, #67.)*
- **G4 — Conceptual/hand diagrams render as TikZ.** Prefer TikZ for the drawn-by-hand conceptual figures. *(Tagged: #68 Fig 2.4; apply to comparable figures book-wide.)*

---

## Section 2 — TARGET ARCHITECTURE (RESOLVED — Josh confirmed 2026-07-17)

Split by **question, not object**. Ch1 runs heavy (Josh confirmed). Concepts move forward; the elimination *machine* stays in Ch3. The inverse lands twice by design (#75): an undo *operation* in Ch1, re-landed as a *transformation* in Ch2.

- **Ch 1 — Objects, spaces, and the solving question.** Vectors (4 lenses) → combinations/axpy → vector space/closure → span/subspace → independence/basis/dimension → **rank** (#42) → **column space** + **null space** named here → existence/uniqueness as the span-membership question (#36, no longer abrupt) → *seeing* small solutions → the **inverse as an undo operation** (#75). No elimination machinery yet. "A vector is also a function" lands here (#51). Uniqueness-as-license is not buried (#44).
- **Ch 2 — The verb.** LEAD with the two-views framing (#50) → matrix as transformation, with the stone between the difference matrix and the formal definition (#57) → matrix-vector product row/column/**outer**, three ways not two (#61) → composition (K) → the stretch → **projection done fully on its own** (#69, gets the freed room) → the **inverse re-landed as a transformation** (#75).
- **Ch 3 — Elimination and factorization (the machine).** Elimination, LU, rank-nullity — the method for when you cannot just see the solution.
- **Ch 4 — Eigen.** Unchanged.

Preface (#1) splits into a dedicated two-roads section and a dedicated four-lenses section. #4 (matrix-mult motivates column + row space) seeds the preface and pays off in Ch1's spaces. #13 (regression and PCA are two songs) holds across the preface and downstream chapters. #24 (closure clauses get their own headings) is a Ch1 local. The old §2.4 sequencing worry (#74) dissolves: the solving question is in Ch1, projection is whole in Ch2, elimination is Ch3.

---

## Section 3 — RANDOM-VARIABLE-AS-VECTOR THREAD (weave throughout)

- **#19** §1.3 (p2) — say "random variable," "more on that later."
- **#33** §1.3 (p10) fn 8 — a random variable is a subspace, so AXPY and the rest apply.
- **#39** §1.4 (p13) — the houses are random-variable measurements, not a raw R^1460 subspace.
- **#45** §2.0 (p19) — "or a random variable, depending on row vs column."
- **#46** §2.0 (p19) Def 2.1 — the feature column is a random variable.

## Section 4 — VOICE / RIGOR-NOT-COLLOQUIAL (thread; state things unequivocally, never colloquially, without demanding formal proof)

- **#38** §1.5 (p13) Claim 1.7 — if a proof is simpler, just prove it; drop colloquial phrasing.
- **#40** §1.5 (p14) — motivate why the set-to-zero elimination is done this way.
- **#41** §1.5 (p14) — reframe: av+bw=cu has only the trivial solution (independent) vs a nontrivial one (dependent).
- **#43** §1.5 (p15) Claim 1.10 — hardest explanation; check how Strang handles it.
- **#59** §2.1 (p22) Claim 2.3 — state unequivocally; "not a formal proof" must not mean colloquial.

## Section 5 — LOCAL FIXES

- **#2** Preface (p vii) — compute all four product entries.
- **#3** Preface (p vii) — show both columns of the column view.
- **#7** Preface (p x) — "b is not in the sheet" → add "aka the span."
- **#11+#12** Preface (p xii) — rephrase to "in which combination of basis states does this electron lie."
- **#15** §1.0 (p1) Fig 1.1 caption — the figure already shows two lenses (arrow + list); say so.
- **#16** §1.0 (p1) — if the figure is annotated, the algebraic-lens sentence belongs in the caption.
- **#18** §1.0 (p2) Listing 1.1 — delete the "# a vector in R^3" comment.
- **#20** §1.1 (p2) "AI rests on a single, simple move" — add video gaming (GPUs) beside AI.
- **#21** §1.1 (p2) — put the linear-combination equation in an align environment.
- **#22** §1.1 (p3) — write the axpy computation as column vectors?
- **#25** §1.2 (p6) — add: agree to operate only on vector-space objects and you get AXPY and all its magic.
- **#26** §1.2 (p6) fn 6 — address that the eight properties constitute a field.
- **#27** §1.2 (p7) — note "the spells" are a sampling of the techniques linearity enables.
- **#29** §1.2.1 (p7) — add: scaling cannot change a vector's direction.
- **#30** §1.2.1 (p8) — boldface/subhead the move from scaling to addition; apply the same to scalar multiplication.
- **#31** §1.2.1 (p8) — refer to "the closure drawing above" by figure number (Fig 1.3).
- **#34** §1.2.1 (p11) — note a = c + 2d is a scalar (a member of the reals).
- **#37** §1.4 (p12) — add: the point is that if we find it, we have found the solution.
- **#48** §2.0 (p20) — add "in two dimensions"; confirm point ≡ vector is established by here.
- **#52** §2.0.1 (p21) — fold "Listing 2.2 constructs..." into the previous paragraph.
- **#58** §2.1 (p22) — the squaring map reads like 2×; clarify it is (x1^2, x2^2).
- **#62** §2.2 (p25) — curiosity: does NumPy favor row or column view in execution time (exercise/footnote).
- **#64** §2.2 (p25) fn 2 — curiosity: row-vs-column timing across NumPy/Pandas, re .apply.
- **#71** §2.3 (p29) Def 2.11 transpose — does it belong here, or is it a special operation like the determinant?
- **#72** §2.3 (p29) Def 2.12 projection — arrives out of nowhere; sequence it within the section.
- **#73** §2.3 (p30) Listing 2.12 — the projection thread is lost; it jumps into NumPy from nowhere.
