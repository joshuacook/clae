# Ch 1 (Vectors and Linear Combinations) — conversation notes

## 2026-07-10 — The descent problem, and what solves it

**The detail named first (Claude, affirmed by Josh — "I think you have the right
idea chapter 1"):** the descent from §1.0 to §1.1. The hook ends at altitude
(Kalman, "the rest of the book is commentary") and §1.1 must then say "you can
multiply a vector by 2." Pitched flat, that reads remedial and betrays the
audience.

**What solves it — the audience refinement (see book-level notes, 2026-07-10):**
the target reader took linear algebra, maybe more than once, and *either never
got excited or lost the excitement*. Under that banner §1.1 is not review, it is
**re-enchantment**: we are not re-teaching scaling and adding, we are handing
back something that was taken from them by the way it was taught. The move is
"you know this — but you've never looked at it," never "let's review."

**Tone anchor for the whole chapter:** Lockhart's Lament (Josh's paraphrase:
"we make students copy sheet music for 10 years before we play them a song").
Ch 1 is where the song gets played. §1.0 already behaves this way; §1.1–1.6
must keep the promise at ground level.

**Open:** Josh to riff §1.1 in his own words (whiteboard, sharp colleague, twelve
years rusty — what do you actually say first?). Capture as near-prose here.

## 2026-07-10 (claude.ai session, synced 2026-07-11) — Option B, the contract, the two pictures

**Ch 1 lead — OPTION B, AFFIRMED (scaffold updated 2026-07-11):** Ch 1 leads
with regression by leading with the QUESTION in pure axpy vocabulary — the Ames
columns on the table, estimation's one sentence (`SalePrice ≈ w1·GrLivArea +
w2·OverallQual + …`, which IS axpy), weights unknown, the book exists to earn
them — AND shows the unearned answer: one `np.linalg.lstsq` cell, real numbers
(w = 51.87, 17604.21; house 2 actual 181,500 / predicted 171,085), "delivered
by a function you did not build and do not yet deserve; by Chapter 11 you will
have built it yourself." Play the song before teaching the instrument; the
reader has called lstsq professionally — the mystery was never the answer, it's
why it works.

**§1.1 reframe — contract first, arrows after (affirmed):** closure under the
two operations is the price of admission; honoring it buys the suite
(regression, eigen dynamics, Fourier, orbitals). The beer-table verbatim lives
in `clae-preface-conversation.md`.

**The opening line:** Josh, verbatim: "Honestly I don't know. First line the
hardest. Maybe it emerges as we write." Scaffold carries a PLACEHOLDER; do not
invent his voice.

**The two pictures (row/column duality — in-flight, reader order OPEN):** Josh:
"One axis per house or a house space with the axes being the features?" Row
picture = each house a point in feature space R^d (where humans live); column
picture = each feature a vector in observation space R^n (where estimation
lives; projection IS regression; the weights are the coordinates of the
shadow). Josh on the label: "isn't a label like a low dimensional embedding of
the house space?" — sale price as a linear functional (row) / the label vector
approximately in the span of the feature columns (column). Same fact,
transposed.

**Josh's honest phenomenology (design constraint):** "it's not landing for
« a column of data »" — nobody sees R^1460. Resolution offered (Josh: "I like
this a lot," explicit affirm as §1.2 material still pending): the
**span-of-the-question principle** — any two vectors, in R^1460 or R^googol,
span at most a plane; the reach is bounded by ingredient count, not ambient
dimension; the drawing on the page is exact, not a metaphor. The reversal is
the teach: standard books say "two vectors in R³ span a plane"; CLAE says "two
vectors in R^1460 STILL span only a plane — you were never supposed to see the
ambient space."

**Ch 1 narrative spine (re-grounded):** §1.0 axpy hook → §1.1 contract + the
question + the unearned answer → §1.2 span = the reach of the operation (the
gap is the residual, planted 200 pages before its name) → §1.3 basis &
coordinates ("the list was never the vector") → §1.4–1.6 per scaffold.
Everything else is footnote stock; the spine doesn't feel their weight. The
§1.3 "recipe" payoff may want the beer-table language.

## 2026-07-11 (synced) — three confirms, applied

Josh ("Yes yes row"): (a) **span-of-the-question is §1.2 material** — the
at-most-a-plane paragraph is now in the draft ("You were never supposed to see
the ambient space"); (b) **DFW footnotes standing**; (c) **row picture first,
column picture as the §1.5 payoff** — the draft already reads in that order.
Ch 1 stands as drafted; skim-first officially superseded in the decisions log.

## 2026-07-11 (night) — retrofitted to the anatomy

14 numbered items (Defs 1.1-1.4, 1.6-1.7, 1.9, 1.12, 1.14; Props 1.5, 1.8,
1.10, 1.11, 1.13), proofs per triage (closure PROVE teaches the pattern;
unique-recipe PROVE; bases-same-size SKETCH; span-of-question SKETCH;
Cauchy-Schwarz SKETCH + VERIFIED on Ames: |a.b| = 14,123,976 <= 14,645,262,
ratio 0.9644 = the raw cosine between GrLivArea and OverallQual). Four
hand-worked (pencil axpy; span membership (4,7) = 1v + 2w; the dependent
triple by hand, incl. an honest caught-mistake beat; angle 37.9 degrees).
12 tiered exercises; treks (Strang/OCW, Axler, Lockhart, Singer, BLAS 1979).
