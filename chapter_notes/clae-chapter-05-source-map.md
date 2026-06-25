---
title: "Ch 5 Source Map"
type: chapter-source-map
chapter: 5
status: active
created: "2026-06-25"
updated: "2026-06-25"
---

# Chapter 5 Source Map: Expectation and Conditional Probability

Source Assembly for Ch 5, tagged **scratch** in `source/coverage-by-chapter.md`
(course lessons: none; case studies: Ames conditional mean of price; repos: none).
This map confirms the scratch reality: the *conditioning* spine of the chapter
(conditional probability, conditional distributions, conditional expectation, the
tower property, the conditional mean as best predictor) has **no source anywhere**.
The one reusable scrap is the expectation-operator material in course L9 (already
the Ch 4 source), and the one dataset asset is the Ames ANOVA group-means as a
conditional-mean-of-price hook. Maps source to the book-outline sections with a
reuse verdict, then notes gaps. Feeds the Ch 5 notes+outline.

## Section-to-source map

| Outline section | Source | Provides | Verdict |
|---|---|---|---|
| 5.1 The expectation operator (linearity; expectation of a random vector) | L9 (expected value definition discrete/continuous; linearity E[aX+b]=aE[X]+b, E[X+Y]=E[X]+E[Y]; the vector forms E[aX+bY]=aE[X]+bE[Y] and **E[AX]=AE[X]**, worked with a 2x2 example; mean vector mu = E[X]) | the full operator foundation, already vector-valued and worked | **adapt (strong scrap)**; this is the one genuinely sourced section. Note L9 is the Ch 4 source, so coordinate to avoid duplicating mean-vector material between Ch 4 and Ch 5.1 |
| 5.2 Conditional probability and conditional distributions | **none** | — | **net-new** (no lesson, no ILA chapter, no repo mentions "conditional" at all) |
| 5.3 Conditional expectation (E[Y|X] as a function of X; the tower property) | **none** | — | **net-new** (tower property / law of total expectation appears nowhere in any source) |
| 5.4 The best predictor (conditional mean minimizes MSE; **MMSE seed**) | **none** | — | **net-new** (the orthogonality/best-predictor result is the Ch 12 LMMSE seed and has no upstream source; sets up Ch 12.1) |
| 5.5 *Implementation:* conditional mean of Ames price given features; predict from a partial record | Ames case study `05-04-Analysis_Of_Variance_ANOVA-r.ipynb` (group means of SalePrice by categorical: ExterQual, MoSold via `tapply(SalePrice, ExterQual, mean)` / `aggregate`); Ames data load (HMD `Ames_Iowa_Housing_Prices-*`, case-study ingest) | a concrete E[SalePrice | category] computation = empirical conditional mean; the data pipeline to load Ames | **adapt + reframe + port**; reframe ANOVA group-means explicitly as the *empirical conditional mean* E[Price | feature]; port the R notebook to Python (numpy/pandas `groupby().mean()`); extend to "predict from a partial record" which is net-new |
| 5.6 Summary and exercises | **none** | — | **net-new** (no exercise seed; L9's practice problems are covariance/transformation-flavored, not conditioning) |

## Gaps and conflicts

- **The conditioning spine (5.2-5.4) is entirely net-new.** A repo-wide and
  course-wide search for "conditional" returns **zero hits** in every course lesson
  `*_math.md`, every ILA chapter (`introduction_to_linear_algebra/ch/*`), and every
  clae-refs notebook. Conditional probability, conditional distributions,
  conditional expectation, the tower property, and the conditional-mean-as-best-
  predictor result all must be written from scratch. This is the chapter's
  substantive load and it is genuinely net-new.
- **5.1 is the lone scrap, and it lives in the Ch 4 source.** L9 ("Random Vectors")
  carries a clean, already-vectorized expectation treatment: the discrete/continuous
  definition, full linearity, **E[AX]=AE[X]** worked with a 2x2 example, and the mean
  vector mu=E[X]. But L9 is the primary source for Ch 4, and Ch 4.4 ("how the mean
  transforms") already claims the linear-transformation-of-the-mean result. **Conflict
  to resolve at outline time:** decide whether E[AX]=AE[X] lives in Ch 4.4 or Ch 5.1.
  Recommend Ch 5.1 owns the expectation *operator* (definition + linearity) and Ch 4
  refers forward; otherwise 5.1 risks being a restatement.
- **The dataset hook is ANOVA group-means, relabeled.** The only Ames asset that
  computes a conditional quantity is the ANOVA notebook, which reports mean SalePrice
  within categorical groups (ExterQual, MoSold). That table *is* the empirical
  conditional mean E[SalePrice | category]; the chapter's job is to relabel it as such
  rather than as a hypothesis test. The notebook is in **R**; it must be ported to
  Python to match the book's stack.
- **"Predict from a partial record" (5.5) has no source.** Computing E[Price | known
  features] for a record with missing fields is the implementation payoff and is
  net-new; it foreshadows imputation (Ch 7/8) and LMMSE (Ch 12).
- **No exercise seed.** L9's practice problems are about covariance and linear
  transformations, not conditioning, so 5.6 is write-from-scratch.

## Implication for the chapter outline

The section sequence holds; the scratch tag is accurate and slightly understated by
the coverage table, which lists only "Ames (cond. mean of price)" and omits that
L9's expectation material is reusable for 5.1. Net read:

- **5.1** is adapt-from-L9 (the only sourced section), with a Ch 4 coordination
  decision: let Ch 5 own the expectation operator and linearity; have Ch 4 point
  forward, so the two chapters do not duplicate E[AX]=AE[X].
- **5.2-5.4** are the chapter's true content and are fully net-new. 5.4 is load-
  bearing: the conditional mean as the MSE-optimal predictor is the **MMSE seed**
  that pays off in Ch 12.1, so write it with that forward link explicit.
- **5.5** anchors on the Ames ANOVA group-means, reframed as the empirical
  conditional mean and ported R to Python, then extended to the net-new
  partial-record prediction.

Net assessment: Ch 5 is a real scratch chapter. One adaptable section (5.1, borrowed
from the Ch 4 source) and one dataset hook (Ames ANOVA group-means, reframed and
ported); everything that makes the chapter about *conditioning* (5.2, 5.3, 5.4, 5.6)
is write-from-blank. It is the first chapter where the book's estimation destination
starts paying source debt, and the conditional-mean-as-best-predictor result (5.4) is
the seed the Ch 12 LMMSE capstone collects on.
