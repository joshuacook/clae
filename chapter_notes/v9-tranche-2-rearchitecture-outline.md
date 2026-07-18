<!-- TRANCHE 2 DRAFT ARTIFACT 1 of 4 — the re-architecture outline
     (Shaw's v9 assignment, 2026-07-17). FOR REVIEW; the chapter prose
     drafts (ch1 V5, ch2 V5, ch3 V2) are built from this. Nothing here is
     folded into chapter_drafts/ until Josh rules. Source of truth:
     chapter_notes/v8-revision-punchlist.md Section 2 (RESOLVED,
     Josh confirmed 2026-07-17). -->

# v9 re-architecture — working outline (Ch 1–3 split by question, not object)

The ruling: **Ch 1 asks what the objects are and what reaching means. Ch 2 asks what a matrix does. Ch 3 asks how to compute when you cannot see.** The inverse lands twice by design (#75): an undo *operation* on recipes in Ch 1, re-landed as a *transformation* in Ch 2. Elimination's *machine* stays in Ch 3.

## Chapter 1 — Objects, spaces, and the solving question (heavy, Josh confirmed)

Existing sections 1.0–1.5 keep their arc and their tranche-1 fixes. New weight arrives after basis.

- **1.0 The Method** — unchanged (four-lens tour of the vector). Add the #51 beat: *a vector is also a function*, index in, entry out; a footnote-weight bridge that pays when random variables arrive (Part II) and when sampled signals arrive (Ch 2's D). Placed at the algebraic-lens paragraph.
- **1.1 In axpy we trust** — unchanged.
- **1.2 The contract** — unchanged, except #24: the two closure clauses inside Definition 1.4 get their own bold run-in headings (already bold in the box; the *prose walk* below the box gains matching **Closure under scaling.** / **Closure under addition.** leads, replacing the current run-together demonstration paragraph).
- **1.3 The houses** — unchanged (random-variable thread landed in tranche 1).
- **1.4 Span and subspace** — keeps the sweep and the drawings. The membership solve MOVES OUT (to new 1.6) so this section ends on the reach question posed, not answered. The data beat stays.
- **1.5 Independence, basis, and the recipe** — keeps definitions, the two verdicts, coordinates, standard basis. Claim 1.10 (unique recipe) stays here with its license story (#44: the license paragraph is already unburied; it becomes the section's closing beat, headlined **The license**).
- **1.6 NEW — The solving question** *(the chapter's destination; #36 lands here so existence/uniqueness stop being abrupt)*
  - Open by assembling the question from parts already built: a target $\mathbf{b}$, a set of columns, and the membership question of 1.4, now named: does a recipe exist (existence), and is it the only one (uniqueness)?
  - **Rank named here (#42):** dimension of the span of the columns, the honest measure of reach. Definition + the two-column houses example (rank 2 in $\mathbb{R}^{1460}$). No nullity yet, no ledger; the ledger theorem stays Ch 3.
  - **Column space and null space named here** (moved from ch2 §2.5): column space = the span wearing its matrix name, the reach; null space = the crush, what solving must fear, defined as the solutions of $A\mathbf{x} = \mathbf{0}$ — presented through recipes (combinations summing to zero = dependence with live weights, tying straight back to 1.5's nontrivial solutions). The C exhibit (cyclic differences crushing constants) MOVES here from ch3 §3.1 as the standing example of a crush.
  - **Seeing small solutions** (moved from ch3 §3.3): integer systems read off by eye, verified by hand, legitimized by the license. The method box: see, verify, and uniqueness does the rest.
  - Existence/uniqueness diagnosis table on small cases. The three fates *preview* in one paragraph (full three-panel treatment stays Ch 3).
- **1.7 NEW — The inverse as an undo (#75, first landing)**
  - Operation framing only, no transformation language: differencing a vector and running-summing it back, the (1,4,9) → (1,3,5) → (1,4,9) hand computation (moved from ch2 §2.3 "identity and undo," stripped of matrix-of-the-transformation talk — here it is an operation on lists, done entrywise, undone entrywise).
  - The payoff sentence: when the recipe is unique, an undo exists in principle, and Ch 2 will meet it as an object.
  - The roundtrip figure (fig_undo_roundtrip) moves with it.
- **1.8 Summary and exercises** — updated ledger; exercises gain a see-and-verify integer solve and a null-space-by-recipes item (both currently ch3 exercises).

## Chapter 2 — The verb

- **2.0 LEAD: one product, two views (#50).** The chapter OPENS on the two-views framing: the data-matrix conventions (Def 2.1, rows/samples, columns/features, RV thread) fused with the matrix-vector product's two readings. The current §2.3 material moves to the front and becomes the frame for everything.
- **2.1 The verb that differentiates.** D built and tested (current §2.1 back half), THEN **the stone (#57)**: an explicit way-station paragraph between the D exhibit and the formal definition — what exactly did we just witness, what would it mean for *any* matrix to act this way — so Definition 2.2 (linear transformation) arrives as the name of something already seen twice, not as a decree.
- **2.2 What made it possible.** Linearity, Claim 2.3 (columns are landings), the stretch witness. Unchanged in substance.
- **2.3 The product, three ways (#61).** Row view, column view, **and the outer-product view**, promoted from the preface's third way into a chapter citizen: $A\mathbf{x}$ as $\sum_j x_j \mathbf{a}_j$ seen as slabs; sets up SVD (Ch 10) and the projection formula's $\mathbf{u}\mathbf{u}^{\mathsf T}$ shape. The two-views bar figure stays; a small outer-product display joins it.
- **2.4 Composition.** K = Db·Df, unchanged (tranche-1 drawn listing included).
- **2.5 The stretch.** Diagonal verbs + circle probe (TikZ), unchanged.
- **2.6 The shadow, whole (#69, #72, #73).** Projection gets the freed room and a complete arc with no imports: the picture (noon sun), the pencil (score, calibrate, stretch), **the transpose summoned honestly (#71 resolved: it enters here, where the score needs rows from columns, presented as the bookkeeping operation that makes $\mathbf{u}^{\mathsf T}\mathbf{v}$ writable, with a promissory note that its deeper meaning — the four subspaces' right angles — arrives in Ch 12)**, the projection matrix via the outer product of 2.3, properties measured, the at-scale drawing, and the Ch 12 promise. Nothing arrives out of nowhere: dot product from the preface, outer product from 2.3, transpose introduced in place.
- **2.7 The inverse, re-landed (#75 second landing).** Now with transformation language: the identity as the do-nothing verb, invertibility as undo-ability of the *verb*, the running-sum matrix as the inverse *matrix*, non-invertibility tied to the crush (null space, named in Ch 1). The FTC-as-triangles beat stays here.
- **2.8 Standardization.** Unchanged.
- **2.9 Summary and exercises.**

## Chapter 3 — Elimination and factorization (the machine)

Loses its opening exhibits to Ch 1 (C-crush, see-and-verify) and tightens around the method:

- **3.0** The equation, restated with Ch 1's vocabulary already in hand (existence = column space, uniqueness = null space; one paragraph, no re-teaching).
- **3.1 The ledger.** Rank/nullity definitions recalled (rank from Ch 1; nullity defined here), **Claim: rank + nullity = n** (FTLA first installment) with the C witness recalled in one line and the machine audit (Listing: matrix_rank). This is where the ledger *theorem* lives; Ch 1 only named the players.
- **3.2 Three fates, diagnosed.** The three-panel TikZ and the diagnosis discipline, unchanged.
- **3.3 Elimination owned.** Unchanged (the windmill made rigorous).
- **3.4 A = LU.** Unchanged.
- **3.5 The machine verified.** Unchanged.
- **3.6 The door.** Two houses exact, third house knocks, lstsq band, unchanged (tranche-1 market listing included).
- **3.7 Summary and exercises** minus the items that moved to Ch 1.

## Cross-cutting

- **Preface (#1):** splits the church act into a dedicated **two-roads** section and a dedicated **four-lenses** section (mechanical split of the existing act at "That creed is not decoration"). #4: one seed sentence at the three-ways display — the column way is a preview of the column *space*, the row way of the row space, names Ch 1 and Ch 12 will earn.
- **Numbering:** all Definition/Claim/Listing/Figure numbers recut per chapter after the moves; the promise ledger and system map refresh afterward (standing queue).
- **Displaced stock:** nothing new displaced; ch2 §2.5's backwards material is *absorbed* by ch1 §1.6 rather than deleted.
- **#71 RESOLVED (Shaw's ruling, 2026-07-18): standalone interlude.** The transpose is its own section, "Interlude: the transpose," placed directly after the product's three ways (where the slab notation first writes a check against it) and before the stretch. The shadow section uses the notation without pausing. Framed alongside the determinant as a bookkeeping instrument, with the Ch 7 ($Z^\mathsf{T}Z$) and Ch 12 (right angles) promissory notes.

## Draft artifacts of this tranche

1. This outline (artifact 1).
2. `drafts-v9/ch01-v5-draft.md` — full prose (artifact 2).
3. `drafts-v9/ch02-v5-draft.md` — full prose (artifact 3).
4. `drafts-v9/ch03-v2-draft.md` — full prose (artifact 4).

Drafts live under `chapter_notes/drafts-v9/`, NOT `chapter_drafts/`, until ruled.
