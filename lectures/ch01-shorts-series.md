# Chapter 1 as a Shorts series — "Linear algebra, recomputed"

> **STATUS (2026-07-11): parked.** Deprioritized to a prose-generation
> contingency; no production-format decision was made and no further scripts
> get written for now. The plan below is preserved as-is for whenever the
> book work wants a promotional or teaching spinoff.

**Audience.** People who already took linear algebra and know the words — span, basis, dot
product — but learned it abstractly (axioms/proofs) or through an ML/"kernel" lens, and never
got the constructive, geometric, *runnable* picture. We assume the vocabulary and sell the
intuition plus the code. Tone: "you've heard this — here's the version that shows you what it
actually is." Fast, concrete, a little irreverent.

**Format conventions (each Short).**

- 30–90 sec, vertical 9:16; the longer ones (demo, the reveal) earn their length.
- Hook in the first ~2 seconds — a claim or a moving timer, never a title card.
- One idea only. If a second idea wants in, it's a second Short.
- Code runs *on screen* (real output), and figures *build* (animate) rather than appear.
- End on a button: an "oh" or a cliffhanger into the next Short.
- Recurring tag the audience can finish for you: **"…which is a linear combination."**

**The arc (14 Shorts, 5 mini-playlists).** Ship in order; each stands alone but they compound.

### Arc A — The one operation

1. **"All of modern AI is one operation."** Hook: "Every neural network you've ever used runs
   on this one line." Show `a*x + y`; name it *axpy*; name it *the linear combination*. Button:
   "Everything else is decoration."
2. **"Watch Python lose to one line of NumPy."** The live speed demo — 10M-element axpy, loop
   vs vectorized, timer on screen. Payoff: the ~30–50× gap, "and it's software, not a hardware
   trick." *(full script below)*
3. **"'Attention is all you need' — decoded."** RNN step = a combination of state + input;
   attention = a weighted sum of vectors. Button: "so the linear combination is all you need."

### Arc B — The two operations (geometry first)

4. **"Scalar multiplication is just… stretching."** Animate `v → 2v → -v` sliding along one
   line. Button: negative flips it to the far side.
5. **"Vector addition you already know: tip to tail."** Animate the triangle — walk the first
   arrow, then the second. Button: "that's it. That's the whole rule."
6. **"Put them together and you get the only move that matters."** `c·v + d·w`; name `c, d` the
   weights. Cliffhanger: "what if you let the weights be *anything*?"

### Arc C — What combinations build

7. **"Two arrows can fill an entire plane."** Animate the span cloud filling as the weights
   run. Button: "that set has a name — the span."
8. **"A subspace is just a span wearing a different hat."** Closed under scale-and-add, always
   contains the origin. Button: "same object, two descriptions."
9. **"When does a vector earn its place?"** The third-arrow test: lands in the plane (redundant)
   or points out (independent). Button: defines independence in one breath.
10. **"A basis is the smallest kit that builds everything."** Independent + spans → and its size
    is the dimension. Button: "no waste, nothing missing."
11. **"You've been writing vectors as recipes this whole time."** THE REVEAL: `(5,-2,7)` was
    `5·e1 − 2·e2 + 7·e3` all along. "The list was never the vector — it was the instructions,
    in a basis so familiar you forgot it was a choice." *(full script below — this is the
    flagship Short)*

### Arc D — Measuring

12. **"One operation measures length AND angle."** The dot product → `‖v‖ = √(v·v)`, `cosθ`.
    Button: "multiply matching entries, add. One number, two facts."
13. **"Perpendicular has a secret — it's the whole of least squares."** Dot product zero =
    orthogonal; tease that the best estimate leaves an error orthogonal to everything reachable
    (Ch 11), and the same dot product on centered data is covariance (Ch 6).

### Arc E — Data

14. **"Your dataset is just a stack of vectors — read two ways."** Rows = homes (points in Rⁿ),
    columns = features (vectors in Rᵐ); the columns' combinations are *exactly* the predictions
    a linear model can make. Button: "so which combination is the *estimate*? That's the series."

---

## Sample script — Short #2: "Watch Python lose to one line of NumPy" (~55s)

| t | On screen | Voiceover |
|---|---|---|
| 0:00 | Big timer at 0.00s; two arrays of numbers scrolling | "Ten million numbers. I'm going to scale one list and add another — the same math, two ways. Watch the clock." |
| 0:06 | `by_hand` cell — the list comprehension; hit run; timer climbs | "Pure Python, one entry at a time." |
| 0:12 | Timer lands near **4 s**; freeze-frame it | "Four seconds." |
| 0:16 | `vectorized` cell — `a * x + y`; hit run | "Same answer. Now NumPy — the whole array at once." |
| 0:20 | Timer blips to **~0.1 s**; both times side by side | "A tenth of a second. Dozens of times faster." |
| 0:26 | Split: "interpreter overhead" vs "one compiled loop" | "The loop is slow because Python checks types and boxes objects ten million times. NumPy hands the whole array to compiled code that never comes back up." |
| 0:40 | Caption: **software win, not a hardware trick** | "Same CPU. Same arithmetic. The speed is *escaping the interpreter*." |
| 0:48 | The line `a*x + y` glows; tag appears | "And that operation — scale a vector, add another — is a linear combination. Hold that thought." |
| 0:54 | End card → "Next: the title that decoded the whole field" | — |

## Sample script — Short #11: "You've been writing vectors as recipes" (~70s, the flagship)

| t | On screen | Voiceover |
|---|---|---|
| 0:00 | Just the text `(5, -2, 7)` | "You've written a thousand vectors like this. You've been writing recipes and didn't notice." |
| 0:07 | Three unit arrows e1, e2, e3 light up on axes | "Here are the three directions everyone starts from — one step along x, y, z." |
| 0:14 | `5·e1` stretches out, then `−2·e2`, then `7·e3`, tip to tail | "Five steps this way. Two steps back that way. Seven steps up." |
| 0:26 | The combination resolves to the point `(5,-2,7)` | "Where do you land? Five, minus two, seven." |
| 0:32 | Overlay: `(5,-2,7) = 5·e1 − 2·e2 + 7·e3` | "The list *was* the linear combination. The numbers were never the vector — they're the instructions." |
| 0:44 | Same arrow, a tilted (different) basis fades in; coordinates change | "Change the basis and the instructions change. The arrow doesn't move at all." |
| 0:54 | Caption: **the list is a choice of basis** | "A coordinate list is a recipe written in a basis so familiar we forgot we chose it." |
| 1:02 | Tease: a matrix with highlighted columns | "Next chapter: a matrix does this same trick with its columns — and your input is the recipe." |
| 1:09 | End card → "You already understand matrices. You just don't know it yet." | — |

---

**On "any number."** This is built to be open-ended: 14 is the natural Ch 1 set, but Arc A
alone (3 Shorts) is a complete teaser you could ship first to test the format, and #2 and #11
are the two most likely to travel on their own. Later chapters extend the same playlist —
"Linear algebra, recomputed" becomes the channel's spine.

**What I'd need from you to script the rest:** a yes on the format from the two samples, and
whether you're on camera + whiteboard, voiceover over screen-recorded notebook, or fully
animated (changes how I write the on-screen column).
