# Chapter anatomy — how a CLAE chapter states things

Approved 2026-07-11 (co-writing channel). All drafting follows this anatomy
from the start; Ch 1 and Ch 2 were retrofitted to it the same day.

## The concept unit

Every concept moves through the same six stations, in order:

1. **MOTIVATE.** Why the reader should care, in the running narrative (Ames,
   the weights plot, the contract). A unit never opens with a definition.
2. **DEFINE.** A boxed, numbered definition, instantly instantiated: the
   sentence after the box points at a concrete instance the reader has
   already met. Markdown form: a blockquote opening with
   `**Definition N.k (name).**` (one shared counter per chapter for
   definitions and propositions).
3. **WORK IT BY HAND.** At least once per load-bearing concept, pencil
   arithmetic small enough to check at a desk: a 2×2 system, a dot product
   on integer vectors, one projection. The reader must feel the mechanism
   before the machine hides it.
4. **STATE IT.** The numbered result (`**Proposition N.k (name).**`, boxed
   like definitions), with its proof-triage mark (below).
5. **RUN IT.** The computational realization: a cell from the companion
   notebook, a measured number, and a verdict sentence about the number.
6. **FOOTNOTES.** Digressions collect at the unit's edge per the DFW rule;
   provenance, history, stack-consciousness, deep cuts.

## Proof triage (always disclosed)

Every stated result carries exactly one mark:

- **PROVE** — full proof in the text, ending ∎. Reserved for short proofs
  that teach (closure checks, uniqueness by subtraction, idempotence).
- **SKETCH** — the idea in a paragraph, honestly labeled *Sketch.*, with a
  citation to a complete treatment.
- **VERIFY + CITE** — demonstrated computationally at real scale, labeled
  *Verified computationally; proof in [citation].* The Introduction carries
  the epistemology sentence once for the whole book: computational
  verification is evidence, not proof.

## The chapter close

Three fixtures, in order:

- **Exit state.** One paragraph: what the reader now holds (objects, named
  matrices, capabilities) and which chapter collects it.
- **EXERCISES**, tiered and labeled:
  - *(pencil)* — by hand, checkable at a desk;
  - *(keyboard)* — notebook work, real data, measured answers;
  - *(bridge → Ch N)* — reaches into a named future chapter and says so.
- **FURTHER TREKS.** Pointers out of the book (Strang 18.06/CSE, Axler,
  Lockhart, Singer, BLAS lineage, the author's Leanpub papers), each with
  one sentence on why the trek is worth it.

## Register guards

The anatomy never overrides the voice rules (`ai-tells.md`): definitions are
instantiated, not belabored; proofs end when they teach; verdict sentences
follow measurements; the courteous hand-wave (with a wink) marks every
deliberate skip.
