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

## 2026-07-10 (synced 2026-07-11) — this chapter is the conversion image

**Confirmed:** Strang's Chapter 4 projection picture is THE image that converted
the author in 2012 — Josh, verbatim: "4 is WHERE IT CLICKED where I cracked my
knuckles and said « I see you Gil »." The preface tells the moment; this chapter
IS the drawing. They hold hands across the book — the chapter should knowingly
land the same picture the preface promised.

**Projection is the regression (Josh: "So the column picture is that the
projection is the regression ?" — confirmed):** ŷ = the shadow of y on
span(feature columns); residual = the perpendicular (why residuals ⊥ fitted
values); normal equations = orthogonality conditions; **the weights are the
COORDINATES of the projection** — "regression as discovering the weights" and
"the projection is the regression" are the same sentence in two registers. Row
picture: the same computation reads as a hyperplane through a point cloud. One
computation, two stories; the column story is the enchanted one.

**Payoff planted in Ch 1 (Option B):** the unearned `lstsq` cell — "by Chapter
11 you will have built it yourself." This chapter pays that debt.

## 2026-07-11 — beats planted from Ch 2

- **One coefficient currency:** regressions here run on X_g (Gelman matrix,
  exits Ch 2); every coefficient is dollars per typical contrast, numerics and
  indicators alike (Ch 2's demo: 59,792 / 87,300 / 21,426).
- **Dummy trap as null-space hygiene:** a full indicator block sums to the
  ones vector; with an intercept, the design matrix has a null space. Ch 2
  planted it; this chapter teaches the hygiene (drop a level or drop the
  intercept) as applied null-space reasoning, not ritual.
