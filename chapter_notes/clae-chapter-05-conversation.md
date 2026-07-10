# Ch 5 (Expectation and Conditional Probability) — conversation notes

## 2026-07-10 — The chapter's design problem, named by Josh

**Headline of the chapter (from the axpy-reach session):** expectation is a dot
product — `E[X] = Σ xᵢ pᵢ`, values · probabilities — and E is linear, so **axpy
passes through expectation untouched**. Randomness upgrades the objects; the
operation survives. This is what keeps Part II a CLAE part instead of a stats
detour.

**The design problem (Josh, verbatim):** "Yes I think this is the challenge …
How to make this property come alive." Linearity of E is usually stated as a dry
property; the chapter succeeds or fails on making it feel like the headline.

**Candidate come-alive demos (unchosen):**

- **The dependence shocker.** Linearity of E holds even when variables are wildly
  dependent — variance needs the cross terms, E doesn't care at all. Classic
  demo: expected number of fixed points of a random shuffle is exactly 1 for any
  deck size, via indicator variables that are hopelessly entangled; one line of
  math, then verify by simulation in the ch05 notebook. Feels illegal; rusty
  practitioners love it.
- (collect more candidates here as the conversation continues)

**Connection forward:** E linear → E[Ax] = A E[x] (the matrix passes through),
centering, and eventually conditional expectation as projection (the L² view) —
which sets up orthogonality-in-expectation for Ch 12.
