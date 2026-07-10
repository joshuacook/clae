# CLAE — book-level conversation notes

Running notes from conversational co-writing sessions. Book-wide theses, arcs, and
process live here; chapter-specific material goes to
`clae-chapter-NN-conversation.md`. Dated entries, newest last.

## 2026-07-10 — The reach of axpy; what this process is

**Process (Josh, verbatim intent):** writing this book is "the process of me both
teaching myself and learning more deeply the subject that I'm writing" — Claude
augments on the teaching side; "we're creating a narrative of me understanding a
subject much deeper." Also capturing voice: "how I think about things, how I say
things. I like to think that I'm funny — even a little bit of humor too." Practice:
quote Josh's good phrasings verbatim in these notes; don't paraphrase the funny out.

**Thesis examined:** does "the linear combination is all you need" (planted in
§1.0) carry through the whole book? Conclusion so far (Claude's proposal, awaiting
Josh's reaction): yes — it is the skeleton, not just the hook.

**The reach, part by part:**

- **Part I.** Ch 2: `A @ x` is a combination of columns, x is the recipe; BLAS
  hierarchy = axpy at three scales (level 1 axpy, level 2 = n axpys, level 3 = n²).
  Ch 3: `A^k x = Σ cᵢ λᵢᵏ vᵢ` — powers of a matrix remain a weighted combination;
  only the weights evolve.
- **Part II — the operation survives the object upgrade.** Ch 5: **expectation is
  a dot product** (values · probabilities) and E is linear — axpy passes through
  E untouched; build the chapter around this. Ch 6: Σ is the lookup table for
  variances of all combinations — `Var(cᵀX) = cᵀΣc` is the chapter in one
  sentence. Ch 7: **the Gaussian is the fixed point of axpy** — closed under
  combination (jointly Gaussian in, Gaussian out) and the CLT says combinations
  of enough independent anythings *become* Gaussian; "the Gaussian isn't a
  bell-shaped miracle; it's axpy's home." Ch 8: LLN/CLT are statements about one
  particular axpy (the equal-weights combination).
- **Part III — the arc is "who chooses the weights?"** Ch 1: weights given (you
  write the recipe). Ch 11: weights chosen by geometry (orthogonality picks the
  combination of columns closest to y). Ch 12: weights chosen by statistics
  (min MSE; orthogonality principle in expectation). One line: **an estimate is a
  linear combination whose weights you had to earn.**
- **Part IV — it recurses in time.** The Kalman update `x̂ = x̂_pred + K(y − ŷ_pred)`
  is *literally* axpy; the whole book computes one number, the `a` (=K) in one
  axpy run once per tick. Candidate last page: end where we began — "In axpy we
  trust," except now you know what it costs to deserve the `a`.

**One-breath book arc:** Part I combine arrows; Part II combine random variables
(operation survives the upgrade); Part III earn the weights; Part IV run it
through time. Four parts, one operation, and the plot is the weights.

**Honest strain (say it in the book; the audience will smell overclaim):** Ch 4's
measure-theoretic floor (events, conditioning, distributions) is not combination
material — E rescues it, but the stretch is real. And *finding* eigenvectors /
the gain is nonlinear: the thesis is everything is *built from* combinations,
not that everything *is* one (same caveat as softmax in §1.0).

**Open to Josh:** react to the "who chooses the weights" arc as the book's spine;
if affirmed, per-chapter notes get seeded from this entry (Ch 5, 6, 7, 8, 12, 14
each have a one-sentence identity above).
