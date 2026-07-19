# [Shaw] CLAE v9 Revision Punch List

All 43 of Josh's v9 notes, grounded against the actual green/pink highlight each marks (book pages, printed numerals), with the fix and a bucket tag. **Nothing here is a summary — every note is captured with its location so the worker never re-guesses.** Ink key: green+number = note, yellow = voice, blue = liked, **pink = delete**.

Read order: **Section 0 (the structural redraw)** and **Section 1 (global passes)** first — most of the pain (#28–43) traces to those two. Then the per-note lists.

Buckets: **STRUCT** structural/sequencing (gated on Josh) · **GLOBAL** standing editorial pass · **FIG** figure/show-don't-tell · **VOICE** voice/rigor · **LOCAL** local fix · **PREF-FRAME** preface framing.

---

## Section 0 — STRUCTURAL REDRAW (gated on Josh; the top item)

Josh's "Jackson Pollock math" (#43) traces to three concrete sequencing failures, not vibes. The re-architecture's *idea* (split by question) is right; the *execution* let the three chapters bleed together.

**Problem 1 — Ch1 and Ch3 both "solve"; the boundary is mush (#41, #29, #30, #28).** Ch1 §1.6 does existence/uniqueness + see-and-verify + the crush, §1.7 does the inverse; then Ch3 re-opens with Ax=b + rank/nullity + three-outcomes. The reader meets solving twice.
**Fix:** Ch1 *poses* the question, Ch3 *grinds* it. End Ch1 on the posed question (loud); move the crush + see-and-verify *mechanics* to Ch3; move §1.7 "the undo/inverse" into Ch2 (where inverse-as-matrix already lives). Ch3 stops re-introducing concepts and just runs elimination.

**Problem 2 — Ch2 has no spine; it's a tour (#38, #40).** It zigzags: matrix-as-data → D-derivative → operator theory (2.1) → *back* to matrix multiplication (2.2) → transpose interlude → stretch → projection → inverse → standardization. No organizing question.
**Fix:** organize Ch2 on the dual identity Josh keeps asking for (#36): do the matrix as **data** fully (container, conventions, transpose as the data-flip), then the matrix as **operator** fully (linear transformation, the product, the named verbs stretch/projection/inverse). One then the other, equal footing, stated up front. The transpose interlude stops interrupting because it lives in the data half.

**Problem 3 — load-bearing concepts not landed (#25, #32, #33, #34).** Existence/uniqueness introduced quietly, the "loud" attempt is twee (#26); the new Ch1 sections (§1.6, §1.7) have no worked examples/geometry ("lazy").
**Fix:** klaxons on existence/uniqueness at first mention; a genuine worked-and-drawn investigation of solving, not stubs.

**Net redraw — one job per chapter:** Ch1 = objects + spaces + the *posed* question · Ch2 = the matrix on its two identities (data, then operator) · Ch3 = the solving machine (elimination). Ch4 unchanged.

---

## Section 1 — GLOBAL PASSES (standing rules; audit the WHOLE book)

Carried from v8 (still in force): **G1** code never exceeds the text measure · **G2** figures legible (size, no superimposed labels, not compressed) · **G3** a plot with every code run · **G4** conceptual diagrams as TikZ.

New in v9 (audit book-wide, not just the tagged instance):

- **P1 — Paragraph rule (#1).** No paragraph over ~5 sentences; every paragraph has a clear topic sentence. Exceptions are allowed but must be *deliberate stylistic choices*, not sprawl. Figure out how to enforce this in the automated eval.
- **P2 — Every chapter and section intro states what it does (#37).** The Ch2 intro must say "here is what Ch2 does"; so must Ch1 and every chapter. Global pass.
- **P3 — Ambiguous-language pass (#35).** No vague "its object" / "the object" where you mean "the vector." State things as specifically as possible. Review ALL ambiguous language book-wide, not just the one instance.
- **P4 — Concept-sequencing pass (#38).** Review the order of concepts across chapters for pedagogical soundness (this is what Section 0 does for Ch1–3; apply the same scrutiny throughout).
- **P5 — Kill colloquial/twee explanations (#42, #26).** "Not a formal proof" must not mean colloquial. State unequivocally and clearly. Reinforces the ai-tells agreement.
- **P6 — Everyday name + technical term, always paired (#31).** "The undo" must also say "inversion"; "guess and check" is "by inspection" (#27). Never the everyday name alone.
- **P7 — Existence/uniqueness is LOUD (#25).** At first mention and every anchor, klaxons — it is the load-bearing concept for the non-computational approach. Standing emphasis rule.

---

## Section 2 — PREFACE (notes #1–#18)

- **#1** p.v, "I can do math. It was the era…" — new paragraph break at "It was the era"; and the trigger for the P1 paragraph rule. [STRUCT/GLOBAL]
- **#2** the spot where the Quixote metaphor returns after being dropped for a section — the return lands jarring; smooth or reconsider. [VOICE]
- **#3** the "scalar multiplication" mention — footnote it: multiplying a vector by a number, which shows up in Ch1. [LOCAL]
- **#4** p.viii, "Magnitude 5, direction (0.6, 0.8)" — show a TikZ plot of these including the angle between them. [FIG]
- **#5** p.viii, "Mostly agreeing" (cosine similarity) — show a few more with different cosine values, plotted + algebra. [FIG]
- **#6** p.viii, "the word for it is orthogonal" — show an orthogonal pair. [FIG]
- **#7** the windmill-review intro / Strang-ch4-regression paragraph (p.iv/x) — what if we move "the review" later in the preface. Pairs with #17. [STRUCT/flow]
- **#8** p.ix, "Linear algebra is where the pipeline breaks open for good" — good line (liked; ties to *Linear Algebra Done Right*). Keep. [liked]
- **#9** the figure that isn't referenced — reference the figure by number. [LOCAL]
- **#10** p.viii, "estimation" — boldface. [LOCAL]
- **#11** p.xii, "tightening the grid shrinks it" — Josh: "I've sent this a few times, don't just say this, show it": add a second listing that shows error as a function of granularity. [FIG]
- **#12** p.xii, "Jussi Eloranta's" — link in footnote to his lab. [LOCAL]
- **#13** the spot wanting diagrams — get some diagrams here. [FIG]
- **#14** p.xiii, the spline/BMW/"the gap … turned out to be the job" passage — the point: linear algebra is useful on the job and thumbs its nose at "when will I use this in real life." [PREF-FRAME]
- **#15** p.xiii, the Docker/career-rhythm paragraph — ground more in the math, less in working experience. **PINK DELETES:** "Now I have data science in my job title, and it really was that simple" and "under something akin to this book's title, Linear Algebra and Estimation Theory." [PREF-FRAME + delete]
- **#16** p.xiii, "And everywhere the career went … A regression at work is the drawing …" — the grounding is happening here but a bit hand-wavy; tighten. [PREF-FRAME]
- **#17** p.xiii, end of the career passage ("with friends over a beer") — a good location for "the review." Pairs with #7. [STRUCT/flow]
- **#18** p.xiv, "Of all the linear combinations available, which one is the estimate?" — boldface; and raise "which one is the *best* estimate? what does *best* mean?" [LOCAL + content]

---

## Section 3 — CHAPTER 1 (notes #19–#34)

- **#19** p.2, "a vector is also a function…" — this is also computational: the list 1,2,…,10 is f(x)=x; show it in numpy. [FIG/compute]
- **#20** p.2, Listing 1.1 / the vector-as-function passage — not the right place early in Ch1; move it toward the END of Ch1, ground it in a discussion AND in the linearity of functions. [STRUCT placement]
- **#21** p.6, the two closure clauses — make these a bulleted list. [LOCAL]
- **#22** p.11, Fig 1.7 — the x-axis label "GrLivArea (thousand sq ft)" sits on top of the tick marks. [FIG]
- **#23** p.12, Fig 1.9 — make the w vector land ON the gray plane so it doesn't look orthogonal to / coming up from the plane. (Recurs from v8 #35.) [FIG]
- **#24** p.15, the grey box after Def 1.9 (basis/dimension) — what is this grey box? (stray/empty — remove or fill). [LOCAL/bug]
- **#25** p.16, Claim 1.10 / first mention of uniqueness — existence AND uniqueness with KLAXONS, loud; load-bearing for the non-computational approach. Trigger for P7. [STRUCT/emphasis]
- **#26** p.16, "The license" paragraph (Jim opened his first lecture with uniqueness) — this was the attempt at the loud explanation but it's twee; redo without the twee. [VOICE]
- **#27** p.17, "guess and check" — we called this "by inspection"; use that term. [LOCAL/terminology, P6]
- **#28** p.17, "1.6 The solving question" — frame it: the overall objective is to find the vector that is *most* right; here we start with finding the vector that *is* right, then later look at where the right vector isn't in the subspace. [STRUCT/framing]
- **#29** p.18, Def 1.16 (null space) — not sure null space lands here. What we want now is where a solution *doesn't exist*: if it exists it's in the column space, the only other case is it doesn't. Define *those two* spaces here; the other spaces (row space, etc.) come later. [STRUCT/space placement]
- **#30** p.18–19, Listing 1.13 (the crush) — you lose me with the crush; what are you showing, and why HERE? [STRUCT/confusion]
- **#31** p.20, "1.7 The undo" — don't only use the everyday name; say "inversion" too. [LOCAL/terminology, P6]
- **#32** p.19, "See it, then verify it" (the solving section) — want a few worked examples of solutions + the geometric view + images: a full investigation of solving. [under-developed]
- **#33** p.20, "The original vector came back" (the undo/telescoping) — no work-up, no worked examples, no diagrams; lazy. [under-developed]
- **#34** Ch1 overall — the sequencing is better now, but the new things added are not fully fleshed out. [under-developed, overall]

---

## Section 4 — CHAPTER 2 (notes #35–#40, #42) + CH3/overall (#41, #43)

- **#35** p.23 (parked), "Chapter 1 opened on its first object…" — the ambiguity: "its object"/"the object" instead of "the vector." Trigger for the P3 global ambiguity pass. [GLOBAL P3]
- **#36** p.23, "2.0 The matrix is a verb" — **the repeated frustration**: matrix = dataset AND operator; explicit from the very beginning, equal footing, don't blend (do one fully, then the other); the chapter intro must state "this is what we're going to do." **PINK DELETE:** "Chapter 1's random-variable flag flying over each one." Drives the Section-0 Ch2 redraw. [STRUCT]
- **#37** p.23 (parked) — the Ch2 intro must clearly state what Ch2 does; ensure Ch1 and all chapters do the same. Trigger for P2. [GLOBAL P2]
- **#38** p.28, "2.2 One product, three ways" — didn't we cover this in the preface review? Odd to go into operator theory (2.1) then flip back to matrix multiplication (2.2). Trigger for P4 concept-sequencing pass. [STRUCT/sequencing, P4]
- **#39** p.30, Fig 2.4 (bar plot of the column-view combination) — what even is this? A bar plot of vector values is weird; replace with a better figure. [FIG]
- **#40** p.33, "2.3 Interlude: the transpose" — can't go on; Ch2 has serious sequencing issues; what is the chapter's objective beyond a haphazard tour of the matrix? Drives the Section-0 Ch2 redraw. [STRUCT]
- **#41** p.43, "Chapter 3 / Solving Linear Systems" — didn't we do this at the end of Ch1? Confused by the overall sequencing. Drives the Section-0 Ch1/Ch3 boundary fix. [STRUCT]
- **#42** the deeper Ch2/Ch3 material — the deeper we go, the more I hate these colloquial explanations. Trigger for P5. [GLOBAL P5]
- **#43** overall (Josh's closing) — skimmed the first four chapters, "Jackson Pollock math"; wants (a) a human-synthesizable outline of Ch1–4 [delivered], (b) a review of the sequence [Section 0]. [meta]

---

## Execution order (recommendation)

1. **Section 0 redraw** first — gated on Josh's go, because it moves where ~10 notes land (#20, #25, #28, #29, #30, #31, #32, #33, #36, #40, #41). No point fixing a figure in a section that's relocating.
2. **Global passes (P1–P7 + G1–G4)** — book-wide audits, mechanical where possible.
3. **Local/figure notes** — once the section they sit in is settled.
4. **Preface framing (#14–#17)** — the career-passage trim + the review-placement move, collaborative with Josh (his memoir).
