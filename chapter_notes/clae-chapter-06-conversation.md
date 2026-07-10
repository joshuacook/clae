# Ch 6 (Covariance, Correlation, Cross-Correlation) — conversation notes

## 2026-07-10 — Σ is the answer key (Josh: "I have to hear more about this (excited voice)")

**The chapter's identity:** the covariance matrix is a machine that answers
infinitely many questions with one finite table. Form *any* combination
`cᵀX = c₁X₁ + … + cₙXₙ` of your n variables (80 Ames features; infinitely many
possible c's) — each is a new random variable with its own variance — and

    Var(cᵀX) = cᵀ Σ c

one object, computed once, answers the variance question for every combination
you will ever form. Σ is not "a table of pairwise covariances" (true but dead);
it is **the precomputed answer key for all possible portfolios.** Two-variable
gears: `Var(c₁X₁+c₂X₂) = c₁²Var(X₁) + c₂²Var(X₂) + 2c₁c₂Cov(X₁,X₂)` — squares
carry each variable's own risk, the cross term carries how they move together.

**Four payoffs that fall out (chapter beats, roughly in order):**

1. **The cross term is diversification.** Cov < 0 → the combination's variance
   drops below either ingredient alone. "Don't put all your eggs in one basket"
   has mathematical content: one off-diagonal entry. Markowitz minimized cᵀΣc
   subject to a target return — the Nobel prize was for asking our question.
2. **PSD demystified.** cᵀΣc is a variance, and no portfolio has negative risk —
   PSD-ness is not an axiom, it's "variance ≥ 0 wearing a matrix costume."
3. **The geometry is an ellipsoid whose axes are Part III.** Quadratic form →
   ellipsoid level sets → the long axis is the direction of most variance.
   "Which unit c maximizes cᵀΣc?" *is* PCA (Ch 10); the answer (top eigenvector)
   is why Ch 3 exists.
4. **Runs to Kalman.** The gain minimizes error variance — the same quadratic
   form in the weights, last chapter.

**One-sentence identity (upgraded):** the covariance matrix is the answer key for
the variance of every linear combination, and Chapters 10–14 are increasingly
ambitious ways of interrogating it.

**Grounding note:** dot-product-of-centered-columns view already planted in §1.4;
the Ames numeric columns are the natural demo matrix.

**Standing instruction (Josh, 2026-07-10):** he was excited about this material
but deliberately deferred it — "I'm not going to dig in … but you should capture
that so that when we get there, you remember my excitement." When Ch 6 drafting
begins, reopen this file first and bring the energy back.
