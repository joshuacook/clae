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

2b. **MARK THE LENS.** The lens framework is introduced in the preface
   (ruling 1, 2026-07-12); chapters use lenses the reader inherited.
   Every lens switch is marked with the margin tag (ruling 2):
   `\lensmark{geometric|algebraic|computational|data}` at the switch
   point, book-wide (command in tools/render/spreamble.tex). Lenses are
   songs, not checkboxes: use the appropriate one(s); no reductive
   glosses, no mandatory coverage of all four.
3. **WORK IT BY HAND.** At least once per load-bearing concept, pencil
   arithmetic small enough to check at a desk: a 2×2 system, a dot product
   on integer vectors, one projection. The reader must feel the mechanism
   before the machine hides it.
4. **STATE IT.** The numbered result (`**Claim N.k (name).**`, boxed like
   definitions). Never "Proposition," never "Theorem" (ruled 2026-07-12:
   "Yes to claim!"). **The box holds the claim AND its explanation**
   (ruled 2026-07-12, census #75/#82: bare claim-box + loose one-breath
   prose "reads as proof-lite with less clarity"): the witness and the
   one-breath reason live inside the box with the statement, as one unit.
   How claims get supported is the Strang way (below).
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

## Listing policy (Josh, 2026-07-13 ink; header form re-ruled 2026-07-14)

- **The listing header is a STANDALONE header, nothing else in it.**
  Josh, 2026-07-14: "listing as a header, that's it... there's no prose
  in the header." The format, every listing, every time:

  ```
  <prose paragraph, which references the listing by number and explains
  it if necessary>

  **Listing N.k (name)**

  <code block>
  ```

  The header is its own paragraph immediately above the code block, with
  a blank line on both sides. NEVER run the listing name into the tail of
  a prose paragraph (the 2026-07-13 drafts did exactly that and the
  headers vanished into the prose — the failure Josh caught on the page).
  No trailing period, no sentence after the name. Explanation lives in
  the prose, before the header, referencing the listing by number.
- Every code block gets one (ch01 notes 11, 23, 25, 40); output-only
  text blocks are the sole exception.
- **Definition and execution are separate listings** (ch01 notes 11, 41):
  one listing defines the function(s), a second listing runs them. Never
  fold a `def` and its invocation into one block where the split is
  meaningful.
- **Every figure has a listing** (ch01 note 34): if a figure appears, the
  code that made it appears, and that code is SELF-CONTAINED within the
  chapter (every name it uses is defined in a listing of the same
  chapter). No helper may arrive from another chapter's code.
- **Every code block is a headed listing** (re-ruled 2026-07-14 after
  violations): no bare code blocks, period. Even a three-line
  demonstration gets `**Listing N.k (name).**` and a sentence of
  explanation. Output-only text blocks are the sole exception.
- **Every figure has a caption and a number, TikZ included** (re-ruled
  2026-07-14): in-text TikZ drawings are wrapped in a raw
  `\begin{figure}[!htb] ... \caption{...} \end{figure}` environment, not
  dropped inline in a `center` block. TikZ and matplotlib figures share
  the chapter's figure counter in document order.

## Worked problems and TikZ (Josh, 2026-07-13 ink)

- **At least one worked problem per concept** (ch01 note 53), pencil-scale,
  in a numbered align.
- **The geometric lens carries a TikZ diagram as often as possible**
  (ch01 notes 22, 37, 39, 51). Geometric prose without a picture "lands
  flat."
- **Never reference a figure from another chapter — re-show it** (ch01
  note 48).
- **Clear transitions at every lens flip** (ch01 note 24): the margin tag
  marks the switch; the prose must still hand off cleanly.
- **Definitions come before the properties/claims that use them** (ch01
  note 21), and definitions are tight, not loose (ch01 note 16).
- **Claims and their reasoning go in a literal, visibly framed box**
  (ch01 note 44) — the render must draw the frame, not just italicize.

## Display math and listings (ruled 2026-07-12, double-census)

- **Every worked example and multi-step derivation is a numbered align**
  (raw `\begin{align}` in the markdown; the Springer class numbers per
  chapter), introduced by a sentence that says what the align shows.
  Entrywise formulas alone are "not algebraic, this is fiddly bits":
  the align carries the actual work, small numbers the reader can check.
  Aligns are welcome in footnotes ("Don't be afraid of \align in
  footnotes").
- **Every code listing is numbered and titled**: a bold run-in line
  `**Listing N.k (name).**` immediately before the block, plus
  explanatory text that says what the listing does and points at any
  figure it produces (census #74: "a long-running issue"). Preface
  listings number P.1, P.2, …
- **Code style:** type hints on function signatures, "but not
  religiously" (census #18–20). NumPy only where it earns its place; a
  three-line integer computation the reader can do in their head shows
  the algebra, not `np.array` (census #91/#101).
- **Figures:** no 3-D plots (census #97: "3D plots are not good
  visuals"). Geometry drawings in TikZ; data plots in matplotlib from
  the companion notebooks.

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
