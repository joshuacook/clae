# Ch 10 (Principal Component Analysis) — conversation notes

## 2026-07-11 (synced) — the Shlens device, metronome phenomenon

**Affirmed:** keep Shlens's three-noisy-cameras structure; swap the phenomenon
to a **metronome**: a one-dimensional beam angle observed as six pixel
coordinates (three 2-D cameras), and PCA recovers the beat. The line: **"the
song was one-dimensional."** Cite Jonathon Shlens, "A Tutorial on Principal
Component Analysis," arXiv:1404.1100. Attribution note: the course's
a_pca_tutorial is Josh's code built on Shlens's device.

**Compare-as-we-go beat (two-matrix convention):** run the loadings exhibit on
the Gelman MIXED matrix X_g, where indicator variance is p(1−p) (planted in
Ch 2's Gelman footnote: an even split gives sd 1/2). Loadings on mixed
numeric+indicator columns are the honest hard case; do it here, not in a
footnote.

**From the axpy-reach session (2026-07-10):** the chapter's question is "which
unit c maximizes cᵀΣc" — Ch 6's quadratic form interrogated; the answer is the
top eigenvector (why Ch 3 exists).
