# Ch 11 (Least Squares Estimation) — conversation notes

## 2026-07-10 — The inversion, and Breiman

**Part III framing (Josh, verbatim — epigraph candidate):** "It's the supervised
learning problem — when you're in high school you're given f(x) and x and asked
to compute y. Now you're given X and y and asked to compute [f]." The answer
sheet is handed to you; the function becomes the unknown.

**Breiman anchor (Josh):** connect the function-being-unknown to Leo Breiman,
"Statistical Modeling: The Two Cultures" (Statistical Science, 2001) — this book's
framing sits in the **algorithmic/black-box school**: nature's mechanism is
unknown, judge f by predictive performance, not by fidelity to a posited data
model. Good on-ramp for the chapter; also tonally aligned — Breiman was writing
to re-enchant a stuck discipline, which is this book's mission for its reader.

**From the axpy-reach session:** Ch 11 is where the weights stop being given and
are first *earned* — chosen by geometry: the combination of X's columns closest
to y, with orthogonality doing the choosing. (Ch 12 re-earns them by statistics.)
