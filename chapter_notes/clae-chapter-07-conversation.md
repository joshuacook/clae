# Ch 7 (Gaussian Random Vectors) — conversation notes

## 2026-07-10 — The Gaussian is the fixed point of axpy (showmanship approved)

**The framing (Claude proposed, Josh approved — "let's go for showmanship"):**
the Gaussian family is *closed* under linear combination — combine jointly
Gaussian variables, get a Gaussian — and the CLT (Ch 8) says combinations of
enough independent *anythings* **become** Gaussian. So the Gaussian is the fixed
point of the book's one operation: it's what linear combinations converge to,
and once there, no combination ever leaves.

**The line:** "The Gaussian isn't a bell-shaped miracle; it's axpy's home."

**Why it matters downstream:** closure under combination is exactly what makes
linear estimation and Gaussian assumptions live so comfortably together in
Part III–IV — every linear operation on Gaussian inputs stays in the family, so
the Kalman filter can run forever without leaving it.

**Tone check (standing):** audience is rusty practitioners burned by hand-wavy
ML explanations — showmanship is approved but every flourish must cash out in a
computation they can run (notebook demo: combine Gaussians, histogram stays
Gaussian; combine uniforms repeatedly, histogram *becomes* Gaussian).

**Josh's engagement note:** "I guess I'm getting more and more excited as I read,
like chapter 7" — this chapter's identity is landing; preserve the energy in the
prose.
