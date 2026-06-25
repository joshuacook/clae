---
title: "Ch 8 Source Map"
type: chapter-source-map
chapter: 8
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 8 Source Map: Convergence — Law of Large Numbers and the CLT

Source Assembly for Ch 8 (tagged **scratch** in `source/coverage-by-chapter.md`).
The two planned course lessons (L17 CLT, L18 LLN) were never written, so there are
no `NNN_math.md` content files to adapt. This map confirms that absence, catalogs
the one usable scrap (a CLT notebook in the wholesale case study), and pins down
the `stock_returns` dataset hook (the convergence demo: sample covariance
converging to a built-in ground-truth correlation matrix). It maps source to the
book-outline sections with a reuse verdict, then notes gaps. The accessibility
guardrail holds throughout: convergence is taught by simulation, no measure theory.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 8.1 Estimating from finite samples | **none** (no L17/L18) | — | **net-new**; the "why does the sample mean/covariance work?" framing is the chapter's motivating question and has no course source |
| 8.2 Modes of convergence, by simulation | **none** | — | **net-new**; must be built deliberately as simulation-only (in probability vs almost sure vs in distribution, shown by repeated draws, never via measure theory) |
| 8.3 The Law of Large Numbers | wholesale CLT notebook (repeated `sample().mean()` over 10/50/100/10000 draws, percent error to the population mean shrinking) | a runnable LLN-by-simulation skeleton on a real table | **adapt** the simulation pattern; the LLN statement and the lift to sample *covariance* are net-new |
| 8.4 The Central Limit Theorem | wholesale CLT notebook (intuitive CLT prose + sampling-distribution-of-the-mean definition + sample-size discussion) | plain-language CLT statement and the sampling-distribution histogram idea | **adapt**; reframe off the wholesale customers table, tie back to Ch 7's Gaussian as the retrospective payoff |
| 8.5 Consequences for estimation (sampling distributions; confidence) | **none** | — | **net-new**; sampling distribution, standard error, confidence framing — first-course probability level, no source |
| 8.6 *Implementation:* simulate LLN/CLT; stock_returns sample covariance converging | `assessments/project-1/generate_datasets.py` (`generate_correlated_data`); wholesale notebook simulation loop | the convergence-demo dataset's exact ground truth + a sampling-loop template | **adapt + net-new**; the dataset hook is turnkey (known true covariance), the convergence experiment over growing n is net-new |
| 8.7 **Part II capstone, Statistical Structure of a Housing Market** | Ames (recurring hero); consumes Ch 6 covariance + Ch 7 Gaussianity machinery | the integrative target (model Ames as a random vector, estimate covariance, test Gaussianity, show convergence, output covariance for Ch 10) | **net-new assembly** of prior-chapter parts; no single source, but the components exist upstream |
| 8.8 Summary and exercises | wholesale notebook "Additional resources" links | a few external pointers only | **net-new**; build the exercise set from scratch |

## The stock_returns dataset hook (the convergence engine)

`stock_returns` does not exist as a CSV in this repo (it is a synthetic dataset
the instructor *generates*; the project-1 student-submission tree under
`assessments/` is PII and was not read). Its generator is clean source:
`assessments/project-1/generate_datasets.py`, function `generate_correlated_data`.

What it provides, and why it is the ideal Ch 8 demo:

- **Known ground truth.** 1000 samples drawn from `np.random.multivariate_normal`
  with mean zero and a built-in correlation matrix `Sigma[i,j] = 0.7^|i-j|` (an
  AR(1)-style decay across 10 `feature_*` columns), seed 42. The true covariance
  is therefore *known exactly*, not estimated.
- **The convergence experiment.** Compute the sample covariance on the first n
  rows for growing n and watch it converge entrywise to the planted Sigma. This is
  LLN made visible on a *matrix*, which is exactly the Part II destination (sample
  covariance is the estimator that PCA in Ch 10 will consume).
- **CLT angle from the same table.** The per-feature returns are themselves
  Gaussian by construction, but sample means / sample covariance entries over
  repeated subsamples give the sampling-distribution-of-an-estimator picture for
  free.
- **Naming caveat.** Columns are generic `feature_1..feature_10`, not ticker
  symbols; the "stock returns / sectors" framing is narrative dressing on a
  correlated-Gaussian generator. Keep the prose honest (synthetic, known
  structure) per the dataset-strategy decision.

## Gaps and conflicts

- **L17 and L18 do not exist.** Confirmed: `lessons/017/` and `lessons/018/` are
  absent; the lessons directory holds 001-005, 007, 009-014 plus the case studies
  only. The `coverage-by-chapter.md` "scratch" tag is correct — there is no course
  prose for any convergence theory. Sections 8.1, 8.2, 8.5, and most of 8.4 are
  genuine write-from-scratch.
- **The only scrap is the wholesale CLT notebook**
  (`lessons/case-study-wholesale-customer/04-05-the-central-limit-theorem.ipynb`).
  It is intuition-first and informal: a plain-language CLT statement, a
  sampling-distribution definition, and a repeated-subsample loop showing the
  sample mean's percent error shrinking as the number of samples grows. It is
  useful as a *simulation pattern* and a tone reference, not as theory. It is built
  on the wholesale customers table; port the mechanics, reframe the narrative.
- **The notebook conflates LLN and CLT.** Its "repeatedly sample, average the
  sample means" loop is really demonstrating the LLN (means stabilizing), filed
  under a CLT header. Ch 8 must separate the two cleanly: 8.3 LLN (the estimate
  converges to the truth) vs 8.4 CLT (the *fluctuation* around the truth is
  Gaussian). Do not inherit the notebook's blur.
- **Measure-theory guardrail.** The audience has a first probability course and no
  measure theory (per the outline's audience note). 8.2 "modes of convergence" must
  stay at the simulation level — show in-probability / almost-sure / in-distribution
  by repeated draws and pictures, never via sigma-algebras or epsilon-delta limit
  proofs. This is a deliberate scope choice, not a shortcut.
- **No repo support.** None of ILA, HMD, or PCAt touches convergence/LLN/CLT (the
  only grep hits were incidental: ridge/lasso notebooks, gradient-descent
  "convergence", an iterative-eigenvector notebook). Ch 8 gets nothing from the
  cloned repos.
- **Capstone depends on upstream chapters, not on source.** 8.7 is an assembly of
  Ch 6 (sample covariance), Ch 7 (Gaussianity test), and this chapter's convergence
  result on Ames. It has no standalone source and must be authored as the
  integrative payoff that hands a covariance matrix to Ch 10.

## Implication for the chapter outline

The section sequence holds; the verdict is that Ch 8 is **almost entirely
net-new**, more so than the "scratch" tag alone conveys, with exactly one reusable
asset (a simulation pattern) and one strong dataset hook.

- **Net-new (write from blank):** 8.1, 8.2, 8.5, 8.7, 8.8, plus the LLN statement
  in 8.3 and the theory half of 8.4. This is the bulk of the chapter.
- **Adapt (thin):** the *simulation mechanics* of 8.3/8.4 from the wholesale CLT
  notebook — the repeated-subsample loop and the percent-error-shrinks display —
  re-themed and split cleanly into LLN vs CLT.
- **Dataset-driven (turnkey ground truth):** 8.6, anchored on `stock_returns` via
  `generate_correlated_data`. This is the chapter's strongest concrete asset: a
  known true covariance the sample covariance provably converges to, which is the
  precise Part II destination and the input to the Ch 10 PCA capstone.

Anchor the chapter on the `stock_returns` convergence experiment (sample covariance
→ planted Sigma) as the spine, use the wholesale loop only as a simulation
template, keep all convergence theory at the simulation/picture level, and treat
8.7 as the assembly point that outputs an Ames covariance for Ch 10. Net
assessment: Ch 8 is a genuine write-from-scratch chapter whose saving grace is an
unusually clean, ground-truth dataset hook.
