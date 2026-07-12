# Source material (not copied into this repo)

The book draws on the course at `~/working/teaching/courses/linalg/`:

- `lessons/001–014/` — lecture math notes (`*_math.md`) and Colab notebooks (`*_colab.md`, 7 of 14 lessons)
- `lessons/case-study-03-pca-tutorial/`, `case-study-05-ames/`, `case-study-wholesale-customer/` — three worked case studies (the richest assets)
- `assessments/project-1/` — full PCA project: handouts, milestones, datasets (image_features, stock_returns, sensor_readings)
- `metadata/`, `README.md` — course units, learning outcomes, essential questions

Pull clean source per chapter as it is drafted. Do **not** copy
`assessments/<NNN>/` student submissions — they contain identifiable student PII.

The course also names estimation-theory lessons (CLT, LLN, linear estimators,
MMSE) that have **no content files**; under the current outline these are Ch 8
(Convergence), Ch 11 (Least Squares), and Ch 12 (MMSE). The from-scratch chapters
are Ch 5, 8, 12, 13, 14 (Ch 7 partial); Ch 11's gap is now filled by the
`introduction_to_linear_algebra` repo. See `source/coverage-by-chapter.md` for the
authoritative per-chapter map.

## Prior-work GitHub repos (cloned to `~/working/clae-refs/`, not copied here)

Author's own repositories with reusable content. Cloned read-only as drafting
reference; pull clean content per chapter, do not bulk-copy. Chapter numbers
below follow the current outline (`outlines/clae-book-outline.md`).

| Repo | Reusable content | Feeds |
|---|---|---|
| `introduction_to_linear_algebra` | Prior LA-with-Python book manuscript: `ch07-vector-spaces`, `ch08-eigensystems`, `ch04-the-least-squares` (normal equations), `ch05-regularization` (ridge/Tikhonov), `ch09-unsupervised-learning`. Author's voice and code already drafted. | Ch 1, 3, 10, **11** |
| `housing_model_development` | Full Ames Iowa Housing pipeline: impute, categoricals, numerical-feature visualization, skew-vs-normal standardization, fit/predict. Grounds the hero dataset. | Ch 1, 2, 6, **7**, 11 |
| `a_pca_tutorial` | PCA notebooks (Shlens arXiv:1404.1100): PCA, PCA-as-visualization, data generation. Likely ancestor of the local `case-study-03-pca-tutorial`. | Ch 10 |

Note: `introduction_to_linear_algebra` ran toward NLP/deep learning, so only its
foundational half (vectors, inner product, least squares, regularization,
eigensystems, unsupervised) overlaps. Verify reusability when drafting each chapter.

**Source-coverage impact:** Ch 11 (Least Squares) was tagged scratch but
`introduction_to_linear_algebra` supplies least-squares + regularization prose and
code, so it is now adapt-from-existing. Ch 7's Gaussian-vs-skew real-data material
is grounded by the Ames notebooks (the multivariate-normal theory is still net-new).

Secondary repos scanned and skipped (no estimation/LA content): `CSDS`,
`GT_ML_Project_1`, `ucla-eda-course`, `case_studies_in_data_science`, `redhat`.

## source/course/ — the taught course (added 2026-07-12)

The full instructional content of the Caltech CTME linear algebra course:
lessons 001–014 (math notes + colab notes + session PDFs), the three case
studies (pca-tutorial, ames, wholesale-customer), syllabus, course metadata,
and one-pagers. Student assessments are deliberately absent and must never be
added (PII). This is the primary source corpus the book adapts;
`coverage-by-chapter.md` maps it to chapters.
