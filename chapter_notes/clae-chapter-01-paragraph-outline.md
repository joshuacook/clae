# Chapter 1 V3 — paragraph outline (regenerated 2026-07-14)

One line per paragraph, themed and tagged. Tags: {method} lens machinery ·
{def} definition box · {claim} claim box · {math} align/display · {code}
listing · {fig} figure · {data} Ames beat · {blow} landing line.

## 1.0 The Method

1. Opener: promises kept immediately; the first object through all four lenses. {method}
2. Geometric: a vector is an arrow. {method} + Fig 1.1 (TikZ arrow). {fig}
3. Algebraic hand-off. {method} → Def 1.1 (vector) + complex footnote. {def}
4. R³ examples; past three dimensions the list keeps going. {math}
5. Computational: an array in memory. {method} → Listing 1.1. {code}
6. Data: a column of measurements; Ames preview. {data}
7. Tour summary; every concept makes it; creed order. {method}{blow}
8. The operation; LLM footnote. {method}
9. Def 1.2 (linear combination, weights) + R³ concrete example. {def}{math}
10. Def 1.3 (axpy); BLAS credential in plain words; measurable claim hands to 1.1. {def}

## 1.1 In axpy we trust

11. By-hand axpy, scale then add. {math}
12. Listing 1.2, the same axpy in NumPy; machine agrees. {code}
13. The NumPy stack (BLAS/LAPACK footnote, GPU footnote); fiddly-bits list; focus on ideas. {method}
14. The measurement; Listing 1.3 (defined) + Listing 1.4 (the race) + output; machine footnote. {code}
15. Listing 1.5 (swept, self-contained best()). {code} + Fig 1.2 (timing). {fig}
16. Why the loop is slow; software win. {method}
17. Fused multiply-add; software all the way down. {method}
18. Why the engineering: the itemized receipt (LS, PCA, Kalman); recognize and choose. {blow}

## 1.2 The contract

19. Transition; Def 1.4 (vector space, closure clauses inside) + bootstrap footnote. {def}
20. axpy comes free: symbolic align, numbers, Fig 1.3 (closure walk TikZ). {math}{fig}
21. Two clauses in, Definition 1.2 out; the spells in chapter order. {blow}

### Scaling and adding, drawn

22. Stretch: Fig 1.4 (TikZ), algebraic align, Listing 1.6 (helper) + Listing 1.7 (multiples) + Fig 1.5. {fig}{math}{code}
23. Tip to tail: prose, align, Listing 1.8 + Fig 1.6. {math}{code}{fig}
24. 2v + w worked; the 77x callback. {math}{blow}

## 1.3 The claim on the table

25. Ames introduced; De Cock footnote with data source links. {data}
26. Listing 1.9 (assembling the houses). {code}
27. Features as vectors (observations footnote); rows as points; Fig 1.7 (houses TikZ). {data}{fig}
28. Both readings held; Chapter 2 makes the pair official. {method}
29. The claim, displayed; read against Def 1.2; Listing 1.10 (weights). {data}{math}{code}
30. House 2 worked term by term; the miss; the 10-house table with miss column. {math}{data}
31. Listing 1.11 (the market, drawn) + Fig 1.8 (price vs sqft). {code}{fig}

## 1.4 Span and subspace

32. The question; Def 1.5 (span). {def}
33. Degenerate case Fig 1.9 (TikZ); the a = c + 2d algebra; full case Fig 1.10 (TikZ). {fig}{math}
34. meshgrid as the word every; Listing 1.12 (sweeper) + Listing 1.13 (both cases) + Fig 1.11. {code}{fig}
35. Membership = the two standing questions named; elimination align; verify; license forward-tie. {math}{blow}
36. Def 1.6 (subspace) + origin footnote; Claim 1.7 boxed with reason + footnote-about-footnotes. {def}{claim}
37. The drawings are general: reach set by count, not ambient size. {method}
38. Data lens: the span is the reachable set; existence at housing scale already answered no. {data}{blow}

## 1.5 Independence, basis, and the recipe

39. Third vector in or out; Fig 1.12 (TikZ); Def 1.8 (independence) + zero-test footnote. {fig}{def}
40. One verdict of each: independent align, dependent align; Listing 1.14 + Fig 1.13. {math}{code}{fig}
41. Def 1.9 (basis, dimension) + same-size footnote. {def}
42. Claim 1.10 (unique recipe) boxed with witness. {claim}
43. The license paragraph: Jim's first lecture; guess and check made legal. {blow}
44. Def 1.11 (coordinates); Def 1.12 (standard basis). {def}
45. The payoff align; the list was never the vector. {math}{blow}
46. Claim 1.13 (span of the question) + ambient footnote. {claim}

## 1.6 Magnitude, direction, and the dot product

47. Def 1.14 (unit vector, unit circle); factor (3,4); Fig 1.14 (TikZ); the align. {def}{fig}{math}
48. Def 1.15 (norm); n-dimensional extension, sphere + Pythagoras stacked. {def}{math}
49. Disagreement; orthogonality earned before named; Def 1.16 (dot product, direction agreement, orthogonality); cosine similarity named; Cauchy-Schwarz parked in a footnote. {def}{method}
50. Hand align; Listing 1.15 (concurs) + Listing 1.16 (housing scale); the 0.9644 finding; correlation forward-tie. {math}{code}{data}
51. Orthogonality return; measured, exploited. {blow}

## 1.7 Summary and exercises

52. Summary paragraph; the question posed; 11 exercises, a few quiz-shaped. {blow}
