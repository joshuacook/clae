# Verified ink census: ch01-r1

Reviewed card-by-card in the ink review app; edits are Josh's.

**1. p.1 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "The architectures came and went, and the operation stayed."
*Mark:* highlight

**2. p.1 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "That it is foundational you might take on faith. That it is also the operation your computer runs faster than almost anything else, you should not. Let me show you what"
*Mark:* highlight

**3. p.1 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "deck up:"
*Mark:* highlight

**4. p.1 handwriting** — APPROVED

> each of these should be a DEFINITION

*Grounded to (sentence):* "axpy, linear combination."
*Mark:* marginal-note

**5. p.1 handwriting** — FLAGGED

*Grounded to (phrase):* "axpy,"
*Mark:* circle

**6. p.1 handwriting** — FLAGGED

*Grounded to (phrase):* "linear combination."
*Mark:* circle

**7. p.1 handwriting** — FLAGGED

*Grounded to (paragraph):* "The architectures came and went, and the operation stayed. The neural networks that read text one word at a time carried a running summary forward as a list of numbers, and every update to the summary scaled what the network held and added what it just read. The paper that ended their era was titled “Attention Is All You Need,” and the attention it announced is a weighted sum of vectors, which is a linear combination. The famous title decodes to something quieter: the linear combination is all you need."
*Mark:* circle

**8. p.1 handwriting** — APPROVED

> getting better but still TWEE.

*Grounded to (paragraph):* "The architectures came and went, and the operation stayed. The neural networks that read text one word at a time carried a running summary forward as a list of numbers, and every update to the summary scaled what the network held and added what it just read. The paper that ended their era was titled “Attention Is All You Need,” and the attention it announced is a weighted sum of vectors, which is a linear combination. The famous title decodes to something quieter: the linear combination is all you need."
*Mark:* marginal-note

**9. p.1 handwriting** — APPROVED

> BTW yellow text doesn't mean the ideas are bad. It means the voice is.

*Grounded to (paragraph):* "Whole writing process "
*Mark:* marginal-note

**10. p.1 handwriting** — APPROVED

> I mean... yes it is. Maybe "not just" ?

*Grounded to (sentence):* "Numpy is not math in Python"
*Mark:* marginal-note

**11. p.1 handwriting** — FLAGGED

*Grounded to (sentence):* "NumPy is not math in Python. Python is a high-level wrapper around C, and NumPy is a high-level wrapper around the compiled numerical libraries beneath it, BLAS and LAPACK chief among them, that the whole numerical stack rests on."
*Mark:* circle

**12. p.1 handwriting** — APPROVED

> too long make more than one sentence

*Grounded to (sentence):* "NumPy is not math in Python. Python is a high-level wrapper around C, and NumPy is a high-level wrapper around the compiled numerical libraries beneath it, BLAS and LAPACK chief among them, that the whole numerical stack rests on."
*Mark:* marginal-note

**13. p.1 handwriting** — APPROVED

> add: focus on the ideas let the machine do the computing

*Grounded to (sentence):* "NumPy is the handle that lets you hold axpy at arm’s length. You write the expression and stay in mathematics,"
*Mark:* marginal-note

**14. p.2 handwriting** — FLAGGED

*Grounded to (phrase):* "compute axpy itself"
*Mark:* circle

**15. p.2 handwriting** — APPROVED

> Right here, before python,
do it by hand. Use an \align.

*Grounded to (sentence):* "We will compute axpy itself, on real arrays: two vectors x and y of ten million
numbers each, and a single scalar 𝐿,"
*Mark:* marginal-note

**16. p.2 handwriting** — FLAGGED

*Grounded to (phrase):* "computational lens,"
*Mark:* circle

**17. p.2 handwriting** — APPROVED

> is this the first
mention of lenses? I think a robust discussion
of our lenses is good chapter one material

*Grounded to (phrase):* "computational lens,"
*Mark:* marginal-note

**18. p.2 handwriting** — APPROVED

> Use type hints

*Grounded to (code):* "def list_comp_in_python(a, x, y):"
*Mark:* circle

**19. p.2 handwriting** — APPROVED

> Use type hunts

*Grounded to (code):* "def vectorized_in_numpy(a, x, y):"
*Mark:* circle

**20. p.2 handwriting** — APPROVED

> use type hints,
but not religiously

*Grounded to (code):* "def vectorized_in_numpy(a, x, y):"
*Mark:* marginal-note

**21. p.2 handwriting** — APPROVED

> Footnote 

*Grounded to (paragraph):* "Every ﬁgure and number in this book is produced by the companion notebooks
at github.com/joshuacook/clae-code, run on a 4-vCPU cloud virtual machine with no
GPU. Your own machine will print di!erent numbers, and the gap will still be there,
about this size."
*Mark:* circle

**22. p.2 handwriting** — APPROVED

> footnote

*Grounded to (paragraph):* "Every ﬁgure and number in this book is produced by the companion notebooks
at github.com/joshuacook/clae-code, run on a 4-vCPU cloud virtual machine with no
GPU. Your own machine will print di!erent numbers, and the gap will still be there,
about this size."
*Mark:* marginal-note

**23. p.3 handwriting** — APPROVED

> New paragraph

*Grounded to (sentence):* "Least squares ﬁnds the combination of features closest to a"
*Mark:* new-paragraph

**24. p.3 handwriting** — APPROVED

> new paragraph

*Grounded to (sentence):* "Least squares ﬁnds the combination of features closest to a"
*Mark:* marginal-note

**25. p.3 handwriting** — FLAGGED

*Grounded to (phrase):* "new paragraph"
*Mark:* circle

**26. p.4 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "entire price of admission,"
*Mark:* highlight

**27. p.4 handwriting** — APPROVED

> Is this it? the lenses are doing real work. they need more.

*Grounded to (paragraph):* "Through the algebraic lens, a list. Through the geometric lens, an arrow from the origin, whenever 𝑀is small enough to draw. You have already met vectors in R10,000,000: the arrays x and y of Section 1.0. A column of 1,460 sale prices is a vector in R1460."
*Mark:* numbered-note

**28. p.4 handwriting** — FLAGGED

*Grounded to (paragraph):* "Linear algebra runs on a contract, and the contract is short. You need objects that can be scaled and added, and you need the results to stay in the family. Displayed, because everything else in the book stands on these two lines:
Property 1 (closure under scaling). For any vector v in the space and any number 𝑁, the vector 𝑁v is in the space.
Property 2 (closure under addition). For any vectors v and w in the space, the vector v + w is in the space."
*Mark:* bracket

**29. p.4 handwriting** — APPROVED

> re "family", use precise language. If you mean "subspace" say "subspace"

*Grounded to (phrase):* "stay in the family."
*Mark:* numbered-note

**30. p.4 handwriting** — APPROVED

> This whole paragraph is corny. It's like we're trying to find an original way to say an old and universal idea. DON'T.

*Grounded to (paragraph):* "Linear algebra runs on a contract, and the contract is short. You need objects that can be scaled and added, and you need the results to stay in the family. Displayed, because everything else in the book stands on these two lines:
Property 1 (closure under scaling). For any vector v in the space and any number 𝑁, the vector 𝑁v is in the space.
Property 2 (closure under addition). For any vectors v and w in the space, the vector v + w is in the space."
*Mark:* numbered-note

**31. p.4 handwriting** — APPROVED

> Corny

*Grounded to (paragraph):* "The parties to the contract need names, and here a word about how this book states things. Every deﬁnition gets looked at through more than one lens: the algebraic lens (entries and formulas), the geometric lens (arrows and pictures), the computational lens (code and clock time), and the data lens (1,460 houses, shortly). The lens in use gets named as we go, because which lens you are holding changes what a deﬁnition means to you."
*Mark:* other

**32. p.4 handwriting** — APPROVED

> Formal switch

*Grounded to (phrase):* "the algebraic lens"
*Mark:* underline

**33. p.4 handwriting** — APPROVED

> Formal switch

*Grounded to (phrase):* "the geometric lens"
*Mark:* underline

**34. p.4 handwriting** — APPROVED

> Formal switch

*Grounded to (phrase):* "the computational lens"
*Mark:* underline

**35. p.4 handwriting** — APPROVED

> phrases like "price of admission" are trite, cliché

*Grounded to (phrase):* "price of admission,"
*Mark:* numbered-note

**36. p.4 handwriting** — APPROVED

> Formal switch

*Grounded to (phrase):* "the data lens"
*Mark:* underline

**37. p.4 handwriting** — APPROVED

> we need to explain this. Assume linearity and you get to use axpy, regression, PCA/SVD, etc etc

*Grounded to (phrase):* "one application of each."
*Mark:* numbered-note

**38. p.4 handwriting** — APPROVED

> Footnote the complex numbers

*Grounded to (paragraph):* "Deﬁnition 1.1 (vector)
A vector is an ordered list of 𝑀real numbers, v = (𝑂1, . . . , 𝑂𝐿). The set of all such vectors is R𝐿."
*Mark:* other

**39. p.4 handwriting** — APPROVED

> Lenses need more treatment

*Grounded to (paragraph):* "Through the algebraic lens, a list. Through the geometric lens, an arrow from the origin, whenever 𝑀is small enough to draw. You have already met vectors in R10,000,000: the arrays x and y of Section 1.0. A column of 1,460 sale prices is a vector in R1460."
*Mark:* other

**40. p.4 handwriting** — APPROVED

> Demonstrate symbolically. Also demonstrate closure.

*Grounded to (phrase):* " remain closed under the two operations and you also get axpy, since 𝐿x + y is
one application of each. "
*Mark:* numbered-note

**41. p.4 handwriting** — APPROVED

> 6 Here are the spells

*Grounded to (paragraph):* " the whole suite: regression, eigen dynamics, Fourier analysis,
and, by Chapter 3, the fact that electron orbitals are a basis."
*Mark:* marginal-note

**42. p.4 handwriting** — APPROVED

> These lens explanations are like an ELI5 this is a serious book (and fun)

*Grounded to (paragraph):* "The parties to the contract need names, and here a word about how this book states things. Every deﬁnition gets looked at through more than one lens: the algebraic lens (entries and formulas), the geometric lens (arrows and pictures), the computational lens (code and clock time), and the data lens (1,460 houses, shortly). The lens in use gets named as we go, because which lens you are holding changes what a deﬁnition means to you."
*Mark:* numbered-note

**43. p.4 handwriting** — APPROVED

> Footnote the complex nos.

*Grounded to (phrase):* "vectors is R𝐿."
*Mark:* numbered-note

**44. p.5 handwriting** — APPROVED

> Not enough algebra. Show me small examples

*Grounded to (equation):* "𝑁v = (𝑁𝑂1, 𝑁𝑂2, . . . , 𝑁𝑂𝐿)"
*Mark:* numbered-note

**45. p.5 handwriting** — APPROVED

> formally switch to computational lens

*Grounded to (code):* "import matplotlib.pyplot as plt"
*Mark:* numbered-note

**46. p.5 handwriting** — APPROVED

> 3 formally switch to geometric

*Grounded to (code):* "v = np.array([2, 1])"
*Mark:* marginal-note

**47. p.5 handwriting** — APPROVED

> this is not algebraic. This is fiddly bits.

*Grounded to (equation):* "v + w = (𝑂1 + 𝑃1, . . . , 𝑂𝐿+ 𝑃𝐿)"
*Mark:* numbered-note

**48. p.5 handwriting** — APPROVED

> formal switch

*Grounded to (code):* "def vector_addition(v1, v2):"
*Mark:* numbered-note

**49. p.5 handwriting** — APPROVED

> Formal swatch

*Grounded to (paragraph):* "Addition, through the geometric lens, is tip to tail. Walk out along the ﬁrst arrow;"
*Mark:* marginal-note

**50. p.6 handwriting** — APPROVED

> needs a definition

*Grounded to (phrase):* "weights."
*Mark:* numbered-note

**51. p.6 handwriting** — APPROVED

> needs an align

*Grounded to (sentence):* "Scale ﬁrst: 2v = (2, 4). Add entrywise: (2 + 3, 4 + 1) = (5, 5)."
*Mark:* numbered-note

**52. p.6 handwriting** — APPROVED

> Needs its own section. We just went from arrows to Iowa. GROUND IT!

*Grounded to (heading):* "1.1.2 The claim on the table"
*Mark:* numbered-note

**53. p.6 handwriting** — FLAGGED

*Grounded to (paragraph):* "The numbers 𝑁and 𝑄are the weights. Work one by hand, once. Take v = (1, 2), w =
(3, 1), and form 2v + w. Scale ﬁrst: 2v = (2, 4). Add entrywise: (2 + 3, 4 + 1) = (5, 5).
That is the arithmetic your machine ran ten million times in Section 1.0, once per entry,
at sixty times your interpreter’s speed."
*Mark:* circle

**54. p.7 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "a function this book exists to open up. By And the prediction it powers is this chapter’s"
*Mark:* highlight

**55. p.7 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "operation, written out in full:"
*Mark:* highlight

**56. p.7 handwriting** — APPROVED

> you said "linear combination". Own it. Put more down.

*Grounded to (phrase):* "linear"
*Mark:* numbered-note

**57. p.7 handwriting** — FLAGGED

*Grounded to (phrase):* "linear"
*Mark:* circle

**58. p.7 handwriting** — APPROVED

> Do the computation algebraically (in an \align) to show it. And show real numbers next to it compare. Then a table of 10 houses. Then plot.

*Grounded to (phrase):* "actual sale."
*Mark:* numbered-note

**59. p.7 handwriting** — APPROVED

> And explicitly connect to axpy.

*Grounded to (phrase):* "actual sale."
*Mark:* numbered-note

**60. p.7 handwriting** — APPROVED

> If you use one var its easier?

*Grounded to (phrase):* "actual sale."
*Mark:* numbered-note

**61. p.8 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "computational lens draws it, and the code every 𝑁in the sweep, crossed with every 𝑄."
*Mark:* highlight

**62. p.8 handwriting** — APPROVED

> 3 This sentence doesn't make sense. Maybe comes out of nowhere?

*Grounded to (sentence):* "The computational lens draws it, and the code contains the word “every,” spelled meshgrid: every 𝑁in the sweep, crossed with every 𝑄."
*Mark:* marginal-note

**63. p.8 handwriting** — FLAGGED

*Grounded to (sentence):* "The computational lens draws it, and the code contains the word “every,” spelled meshgrid: every 𝑁in the sweep, crossed with every 𝑄."
*Mark:* bracket

**64. p.8 handwriting** — APPROVED

> 1 show the degenerate. And I wont to see degenerate with a MESHGRID, in 2D!!

*Grounded to (phrase):* "the degenerate case ﬁrst."
*Mark:* marginal-note

**65. p.8 handwriting** — FLAGGED

*Grounded to (phrase):* "the degenerate case ﬁrst."
*Mark:* circle

**66. p.8 handwriting** — APPROVED

> 2 this is great geometric language. SHOW ME RIGHT HERE with MESHGRID. BOTH. Show me a w that leaves v.

*Grounded to (phrase):* "If w points o! the line"
*Mark:* marginal-note

**67. p.8 handwriting** — FLAGGED

*Grounded to (phrase):* "If w points o! the line"
*Mark:* bracket

**68. p.8 handwriting** — FLAGGED

*Grounded to (phrase):* "adding"
*Mark:* circle

**69. p.8 handwriting** — APPROVED

> 4 I'm unclear on what this is saying and why its needed.

*Grounded to (code):* "v = np.array([2, 1]); w = np.array([1, 3])
C, D = np.meshgrid(np.linspace(-2, 2, 25), np.linspace(-2, 2, 25))
span = C.ravel()[:, None] * v + D.ravel()[:, None] * w
plt.scatter(span[:, 0], span[:, 1], s=4, alpha=0.4)
plot_vector(v, ’blue’, ’v’); plot_vector(w, ’red’, ’w’); plt.legend(); plt.show()"
*Mark:* marginal-note

**70. p.8 handwriting** — FLAGGED

*Grounded to (code):* "v = np.array([2, 1]); w = np.array([1, 3])
C, D = np.meshgrid(np.linspace(-2, 2, 25), np.linspace(-2, 2, 25))
span = C.ravel()[:, None] * v + D.ravel()[:, None] * w
plt.scatter(span[:, 0], span[:, 1], s=4, alpha=0.4)
plot_vector(v, ’blue’, ’v’); plot_vector(w, ’red’, ’w’); plt.legend(); plt.show()"
*Mark:* bracket

**71. p.8 handwriting** — APPROVED

> 3 How's your tikz? Can you show both matplotlib and tikz?

*Grounded to (code):* "v = np.array([2, 1]); w = np.array([1, 3])
C, D = np.meshgrid(np.linspace(-2, 2, 25), np.linspace(-2, 2, 25))
span = C.ravel()[:, None] * v + D.ravel()[:, None] * w
plt.scatter(span[:, 0], span[:, 1], s=4, alpha=0.4)
plot_vector(v, ’blue’, ’v’); plot_vector(w, ’red’, ’w’); plt.legend(); plt.show()"
*Mark:* marginal-note

**72. p.8 handwriting** — APPROVED

> All worked examples go in an align 

*Grounded to (paragraph):* "Membership in a span is a concrete question, so work one by hand. Is b = (4, 7) in the span of v = (2, 1) and w = (1, 3)? Asking is the same as solving for weights: ﬁnd 𝑁, 𝑄with 𝑁(2, 1) + 𝑄(1, 3) = (4, 7), which is the little system 2𝑁+ 𝑄= 4 and 𝑁+3𝑄= 7. The ﬁrst equation gives 𝑄= 4 ↑2𝑁; substitute into the second and 𝑁+ 12 ↑6𝑁= 7, so 𝑁= 1, then 𝑄= 2. The recipe exists, b = 1v+2w, and (4, 7) is in the span. Membership questions are recipe questions."
*Mark:* bracket

**73. p.8 handwriting** — FLAGGED

*Grounded to (phrase):* "origin"
*Mark:* circle

**74. p.8 handwriting** — APPROVED

> 4 this is a long-running issue. All listings need labels. And need explanatory text that points at any figures

*Grounded to (paragraph):* ""
*Mark:* marginal-note

**75. p.8 handwriting** — APPROVED

> Reads as proof lite with less clarity. Or claims in a box with their explanation

*Grounded to (paragraph):* "Claim 1.5 (a span is a subspace)
The span of any set of vectors is a subspace.

The one-breath reason: a scaled combination is a combination, a sum of two com-binations is a combination, and all-zero weights give the origin.3 Span and subspace are two descriptions of one object. Span builds it from ingredients; subspace states the property the built thing has."
*Mark:* bracket

**76. p.8 handwriting** — FLAGGED

*Grounded to (paragraph):* "The one-breath reason: a scaled combination is a combination, a sum of two com-binations is a combination, and all-zero weights give the origin.3 Span and subspace are two descriptions of one object. Span builds it from ingredients; subspace states the property the built thing has."
*Mark:* bracket

**77. p.8 handwriting** — FLAGGED

*Grounded to (phrase):* "the"
*Mark:* strikethrough

**78. p.8 handwriting** — FLAGGED

*Grounded to (paragraph):* "Two vectors span at most a plane. That stays true in three dimensions, in 1,460, in a googol: the reach of the operation is bounded by the number of ingredients, never by the size of the space the ingredients live in. Nobody can picture R1460, and nobody needs to. Every question we ask about two vectors happens inside the at-most-a-plane they span, so a drawing on this page is exact for the 1,460-dimensional case, no metaphor involved.4"
*Mark:* bracket

**79. p.8 handwriting** — FLAGGED

*Grounded to (phrase):* "so"
*Mark:* strikethrough

**80. p.8 handwriting** — APPROVED

> All worked examples go in an \align

*Grounded to (paragraph):* "Membership in a span is a concrete question, so work one by hand. Is b = (4, 7) in the span of v = (2, 1) and w = (1, 3)? Asking is the same as solving for weights: ﬁnd 𝑁, 𝑄with 𝑁(2, 1) + 𝑄(1, 3) = (4, 7), which is the little system 2𝑁+ 𝑄= 4 and 𝑁+3𝑄= 7. The ﬁrst equation gives 𝑄= 4 ↑2𝑁; substitute into the second and 𝑁+ 12 ↑6𝑁= 7, so 𝑁= 1, then 𝑄= 2. The recipe exists, b = 1v+2w, and (4, 7) is in the span. Membership questions are recipe questions."
*Mark:* numbered-note

**81. p.8 handwriting** — APPROVED

> 6 footnote, why the origin is needed

*Grounded to (paragraph):* "3 That breath was the whole argument, written small: 𝑀(𝑁v + 𝑂w) = (𝑀𝑁)v + (𝑀𝑂)w, and two combinations add weight by weight. A note about this book’s footnotes, since this is its ﬁrst claim: the fuller arguments live down here and in the references, on purpose. The text above is for you. It is not for the gatekeepers who keep mathematics behind subscript ﬁddliness, and a proof performed as ritual is gatekeeping. When a reason is cheap you will get it in a breath; when it is a real theorem you will get the name of someone who proved it properly."
*Mark:* marginal-note

**82. p.8 handwriting** — APPROVED

> Reads as proof-lite with less clarity. let's put CLAIMS in a box with their explanation

*Grounded to (paragraph):* "The one-breath reason: a scaled combination is a combination, a sum of two com-binations is a combination, and all-zero weights give the origin.3 Span and subspace are two descriptions of one object. Span builds it from ingredients; subspace states the property the built thing has."
*Mark:* numbered-note

**83. p.9 handwriting** — APPROVED

> Maybe just 1D?

*Grounded to (phrase):* "two vectors"
*Mark:* numbered-note

**84. p.9 handwriting** — APPROVED

> 
2 Whoa, buddy! 
this is out of nowhere (Column space)

*Grounded to (phrase):* "somewhere on the sheet; the subspace a set of feature columns spans is called the
column space, and it is the complete inventory of what those features can say. Can the
sheet reach y exactly?"
*Mark:* circle

**85. p.9 handwriting** — FLAGGED

*Grounded to (paragraph):* "Here is what that buys us with the houses. GrLivArea and OverallQual are two
vectors, so their span is at most a plane: a ﬂat two-dimensional sheet through the origin
of R1460. Draw it. The sheet, and the price vector y as an arrow whose tip hovers just
o! it. Every prediction the two features can make, every choice of 𝑃1 and 𝑃2, lands
somewhere on the sheet; the subspace a set of feature columns spans is called the
column space, and it is the complete inventory of what those features can say. Can the
sheet reach y exactly? Almost never. The tip hovers o! the sheet, and the gap between
the tip and the nearest point on the sheet gets its name in Chapter 11. The picture arrives
now: keep the hovering tip and the sheet below it."
*Mark:* circle

**86. p.10 highlight [YELLOW = ai speak (poorly written)]** — APPROVED

*Grounded to (phrase):* "Two ingredients reach a plane. Toss in a third: does the reach grow? Only sometimes, and the di!erence is the next idea."
*Mark:* highlight

**87. p.10 handwriting** — APPROVED

> ① ② Same sentence. Drop from end of previous paragraph.

*Grounded to (paragraph):* "Two ingredients reach a plane. Toss in a third: does the reach grow? Only sometimes, and the di!erence is the next idea."
*Mark:* marginal-note

**88. p.10 handwriting** — FLAGGED

*Grounded to (paragraph):* "Two ingredients reach a plane. Toss in a third: does the reach grow? Only sometimes, and the di!erence is the next idea."
*Mark:* circle

**89. p.10 handwriting** — FLAGGED

*Grounded to (sentence):* "Take the plane spanned by two vectors and toss in a third. Either it lands in the plane,"
*Mark:* strikethrough

**90. p.10 handwriting** — APPROVED

> ③ Formal switch. Show me an independent and a dependent use /align

*Grounded to (paragraph):* "Dependence you can exhibit. Take c1 = (1, ↑1, 0), c2 = (0, 1, ↑1), c3 = (↑1, 0, 1), and look through the geometric lens ﬁrst: Figure 1.5 draws all three living in a single plane through the origin. Three arrows, a two-dimensional reach. The algebraic lens conﬁrms what the picture says, entry by entry:"
*Mark:* marginal-note

**91. p.10 handwriting** — APPROVED

> ④ using numpy here adds nothing.

*Grounded to (code):* "c1 = np.array([1, -1, 0])
c2 = np.array([0, 1, -1])
c3 = np.array([-1, 0, 1])
print(’c1 + c2 + c3 =’, c1 + c2 + c3)

c1 + c2 + c3 = [0 0 0]"
*Mark:* marginal-note

**92. p.10 handwriting** — FLAGGED

*Grounded to (code):* "c1 = np.array([1, -1, 0])
c2 = np.array([0, 1, -1])
c3 = np.array([-1, 0, 1])
print(’c1 + c2 + c3 =’, c1 + c2 + c3)

c1 + c2 + c3 = [0 0 0]"
*Mark:* circle

**93. p.10 handwriting** — APPROVED

> ⑤ I think you need to show this. Don't be afraid of /align in footnotes.

*Grounded to (paragraph):* "The equivalent test, often easier to run: the only combination equal to the zero vector is the one with every weight zero. Move any vector across that equation and the two phrasings trade places."
*Mark:* marginal-note

**94. p.10 handwriting** — FLAGGED

*Grounded to (paragraph):* "Claim 1.8 (unique recipe)
If b1, . . . , b𝑃is a basis, every vector in its span is a combination of the basis in exactly one way."
*Mark:* circle

**95. p.10 handwriting** — FLAGGED

*Grounded to (phrase):* "vector"
*Mark:* circle

**96. p.10 handwriting** — APPROVED

> ⑥ Why do we need this?

*Grounded to (phrase):* "Claim 1.8"
*Mark:* marginal-note

**97. p.11 handwriting** — APPROVED

> 3D plots are not good visuals

*Grounded to (heading):* "Three vectors, one plane: the triple is dependent"
*Mark:* numbered-note

**98. p.11 handwriting** — APPROVED

> /align

*Grounded to (paragraph):* "Witness it small. The set {(1, 0), (1, 1)} is a basis of R2. To build (3, 5), the second
entry forces the weight on (1, 1) to be 5; the ﬁrst entry then forces the weight on (1, 0)
to be ↑2. Forced twice over: no other recipe exists. The one-breath reason it always
works: two di!erent recipes for the same vector would subtract to a zero combination
with nonzero weights, and independence forbids it."
*Mark:* numbered-note

**99. p.11 handwriting** — APPROVED

> what?

*Grounded to (paragraph):* "Claim 1.10 (span of the question)
The span of 𝑅vectors is a subspace of dimension at most 𝑅, whatever the dimension
of the ambient space.7"
*Mark:* numbered-note

**100. p.11 handwriting** — APPROVED

> what?

*Grounded to (paragraph):* "7 If the 𝑃ingredients are independent they are a basis of their span and the dimension is exactly 𝑃.
If not, discard dependent ingredients one at a time until what remains is independent; the span never
shrinks and the count only falls."
*Mark:* numbered-note

**101. p.12 handwriting** — APPROVED

> numpy adds nothing

*Grounded to (code):* "e1, e2, e3 = np.eye(3)
a, b, c = 5, -2, 7
print(a*e1 + b*e2 + c*e3)"
*Mark:* numbered-note

**102. p.12 handwriting** — APPROVED

> Unclear represent algebraically using /align

*Grounded to (paragraph):* "The list (5, -2, 7) was 5e1 - 2e2 + 7e3 all along. The list was never the vector; it was the recipe, written in a basis so familiar we forgot it was a choice."
*Mark:* numbered-note

**103. p.12 handwriting** — FLAGGED

*Grounded to (phrase):* "Watch what this does to"
*Mark:* strikethrough

**104. p.12 handwriting** — FLAGGED

*Grounded to (paragraph):* "e1, e2, e3 = np.eye(3)
a, b, c = 5, -2, 7
print(a*e1 + b*e2 + c*e3)

[ 5. -2. 7.]

The list (5, -2, 7) was 5e1 - 2e2 + 7e3 all along. The list was never the vector; it was the recipe, written in a basis so familiar we forgot it was a choice."
*Mark:* circle

**105. p.12 handwriting** — APPROVED

> I asked you to use "magnitude" and "direction" and you do, but you leave "length" and "angle" so now there are two words for each for maximum confusion !!

*Grounded to (heading):* "1.4 Length, angle, and the dot product"
*Mark:* numbered-note

**106. p.12 handwriting** — FLAGGED

*Grounded to (heading):* "1.4 Length, angle, and the dot product"
*Mark:* circle

**107. p.12 handwriting** — FLAGGED

*Grounded to (phrase):* "vectors. To estimate"
*Mark:* strikethrough

**108. p.12 handwriting** — APPROVED

> Where is my unit circle example motivating all of this

*Grounded to (paragraph):* "Work the machine by hand. Take v = (3, 1) and w = (2, 3): the score is 3·2+1·3 = 9, the lengths are 
10 and 
13, and the agreement is 9/
130 
0.789, an angle of about 38 degrees. Mostly agreeing. The machine concurs:"
*Mark:* numbered-note

**109. p.13 handwriting** — APPROVED

> ① You can't just say "orthogonality" here.

*Grounded to (phrase):* "Orthogonality"
*Mark:* marginal-note

**110. p.13 handwriting** — FLAGGED

> ①

*Grounded to (phrase):* "Orthogonality"
*Mark:* circle
