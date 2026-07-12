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
   definitions and claims). **Definition economy (ruled 2026-07-12):**
   "Definitions require an economy of language. As few and as simple words
   required for rigor."

2b. **NAME THE LENS.** Every move announces which lens it is looking
   through (geometry, algebra, computation, data), in the text, per the
   lens rules in `writing-process.md`. Lenses are songs, not checkboxes:
   use the appropriate one(s) and say so; no reductive glosses, no
   mandatory coverage of all four.
3. **WORK IT BY HAND.** At least once per load-bearing concept, pencil
   arithmetic small enough to check at a desk: a 2×2 system, a dot product
   on integer vectors, one projection. The reader must feel the mechanism
   before the machine hides it.
4. **STATE IT.** The numbered result (`**Claim N.k (name).**`, boxed like
   definitions). Never "Proposition," never "Theorem" (ruled 2026-07-12:
   "Yes to claim!"). How claims get supported is the Strang way (below).
5. **RUN IT.** The computational realization: a cell from the companion
   notebook, a measured number, and a verdict sentence about the number.
6. **FOOTNOTES.** Digressions collect at the unit's edge per the DFW rule;
   provenance, history, stack-consciousness, deep cuts.

## Supporting claims: the Strang way (ruled 2026-07-12, supersedes proof triage)

In the main text a claim is supported the way Strang supports one: state it,
**witness it** (a small case the reader can check at a desk, plus the
companion-notebook run at real scale), and give the one-breath reason in
plain prose where the reason is cheap. Fuller arguments live in DFW-register
**footnotes** or in **citations** to complete treatments. Never in the text:
∎ blocks, "Proof." headers, or proof-pattern meta-teaching ("this teaches
the pattern every closure proof follows"). Proofs-as-ritual are gatekeeping;
this book is not for the gatekeepers.

The old triage vocabulary survives only as the footnote/citation decision:
a cheap complete argument goes in a footnote; a real theorem gets a
citation; a computational demonstration gets the run and the standing
epistemology sentence (Introduction 0.4): computational verification is
evidence, not proof.

**The footnote-about-footnotes.** The book declares this policy once, in a
footnote attached to the first Claim (or in Introduction 0.4), in Josh's
register: the arguments are in the footnotes and the references, not because
they do not matter, but because the text is for the reader, not for the
gatekeepers behind subscript fiddliness.

## The chapter close

Three fixtures, in order:

- **Exit state.** One paragraph: what the reader now holds (objects, named
  matrices, capabilities) and which chapter collects it.
- **EXERCISES**, tiered and labeled:
  - *(pencil)* — by hand, checkable at a desk;
  - *(keyboard)* — notebook work, real data, measured answers;
  - *(bridge → Ch N)* — reaches into a named future chapter and says so.
- **FURTHER TREKS — end of book only (ruled 2026-07-12).** Chapters do NOT
  carry treks sections. Per-chapter trek stock accumulates in
  `chapter_notes/clae-treks-stock.md` and consolidates into one annotated
  reading trail in the back matter.

## Register guards

The anatomy never overrides the voice rules (`ai-tells.md`): definitions are
instantiated, not belabored; proofs end when they teach; verdict sentences
follow measurements; the courteous hand-wave (with a wink) marks every
deliberate skip.
