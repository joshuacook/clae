# Chapter 1 (ink pass draft) ink notes (2026-07-13) — typed by Josh, anchored by Claude

Same format as preface-v6-ink-notes.md: green numbered highlights, Josh's
typed notes verbatim, anchors read from the PDF. Numbering preserved
exactly. Unnumbered yellow/pink flags at the end.

## Numbered notes

**1.** (p.1 — Definition 1.1 tail: "the vectors scaled by numbers and the
results added. The numbers c1, ..., ck are the weights.")
Show a few in R^3

**2.** (p.1 — Definition 1.2: "It is the workhorse form, and the name of
the compiled routine that runs it.")
what does this mean?

**3.** (p.1 — "The vector itself gets its formal definition in Section
1.1. For now it is what it has always been to you, a list of numbers.")
Missed opportunity to hit multiple representations early period. Say what
it is in each representation.

**4.** (p.1 — the two LLM paragraphs: "A language model, underneath the
chat window..." and "Architectures turn over every few years... The
operation is still here.")
Make this a footnote.

**5.** (p.2 — "Foundational is a big claim... Put a clock on it.")
Move this to the beginning of section 1.0.1. You will need to adjust the
narrative since it's no longer part of the previous paragraph, which is
now a footnote. The number four is about LLMs and this is about axpy

**6.** (p.2 — equation (1.1), the by-hand axpy align)
I think this align is broken

**7.** (p.2 — equation (1.1), second mark)
now show the same thing with numpy

**8.** (p.2 — "BLAS and LAPACK chief among them")
quick note explaining what these are with links

**9.** (p.2 — "a short note that says: have the fast code do this.")
Quotes: that says, "have this code do this."

**10.** (p.2 — "while the fiddly bits, allocating the memory, walking the
strides, dispatching the right kernel, calling into Fortran BLAS, happen
out of sight.")
This actually could be an emdash … "while the fiddly bits — allocating …
Fortran BLAS — happen out of sight"

**11.** (p.2 — "Listing 1.2 (the race) puts a clock on both and prints the
gap.")
Listings go before the code. Also, you need two listings one for
definition and one for execution. This should be a policy and it needs to
be applied to all listings where appropriate

**12.** (p.4 — footnote 2: "The GPU version of this sentence is the
hardware trick...")
But there, there are also software tricks… CUDA, tensor flow, PyTorch

**13.** (p.4 — "Least squares finds the combination of features closest to
a price. Principal component analysis... The Kalman filter... choose its
weights.")
Good list but needs glue. This comes from nowhere.

**14.** (p.4 — "Two operations run everything in this book. You can scale
a vector, and you can add two vectors, and both results stay in the space
you started in.")
Footnote: there's a bit of a boot strap here. A scaled vector, and added
vector stays in the vector space. But what's a vector space? The thing
that stays inside when you add or scale. It's a bit circular, but this is
the agreement and then the rest of it follows.

**15.** (p.4 — Property 1: "For any vector v in the space and any number
c, the vector cv is in the space.")
Say "vector space"

**16.** (p.4 — Properties 1 and 2)
I think these definitions are too loose

**17.** (p.4 — "Assume linearity and here are the spells:")
Note to hold on and not to act at this time: I'm not sure about this word
"spells"

**18.** (p.4 — equation (1.2), the closure demonstration)
To abstract. Need actual work examples both Symbolically and with tikZ

**19.** (p.5 — "and, by Chapter 3, the fact that electron orbitals are a
basis." — the spells list order)
Why is this last? You should put it in chapter order

**20.** (p.5 — "The four lenses from the preface start work in this
chapter, and the margin keeps the promise made there... nothing hidden.")
too far into the chapter. This is structural to how chapter 1 should be
told see my notes in the Preface

**21.** (p.5 — Definitions 1.3 (vector) and 1.4 (vector space, working
version))
Put these definitions before the properties

**22.** (p.5 — "Through the geometric lens, scalar multiplication is
stretching. Multiply a vector by c and its arrow grows or shrinks...")
Geometry lens should try to have a TIKZ diagram as often as possible

**23.** (p.5 — "Listing 1.3 (drawing scalar multiples) puts three
multiples of one vector on the same axes; Figure 1.2 is its output.")
listings need a formal heading and an explanation. We need a policy for
this.

**24.** (p.6 — "Addition, through the geometric lens, is tip to tail...")
This section in general lacks clear transitions, which is very important
because we are flipping back-and-forth between all the different lenses

**25.** (p.6 — "Listing 1.4 (tip to tail) draws a sum; Figure 1.3 is its
output.")
Same rule about listings and I don't want to say it every time we need
policies for things like this

**26.** (p.7 — "Now the data lens, and a dataset to look through it at.")
Ends with a preposition

**27.** (p.7 — "The Ames housing data records 1,460 home sales")
the records "are", you're missing a word

**28.** (p.7 — "alongside the price the home actually sold for.")
Ends with a preposition

**29.** (p.7 — "and the move we just practiced on arrows, scale and add,
is about to price real estate.")
Run-on sentence

**30.** (p.7 — "Listing 1.5 (assembling the houses) builds the table.")
missing a line break?

**31.** (p.7 — footnote 5, the De Cock citation)
Tell them where they can get it

**32.** (p.8 — "GrLivArea... is a column of 1,460 numbers, one per home: a
vector in R^1460.")
A foot note about thinking about a list of observations as a vector…
frontloading, random variable.

**33.** (p.9 — the 10-house table)
add a difference column.

**34.** (p.9 — Figure 1.4 caption: "Predicted price... against actual sale
price for all 1,460 homes...")
where is the listing for this?

**35.** (p.9 — inside the Figure 1.4 scatter)
This is a chance to connect to the point view of a vector. a vector is a
point in (Vector) Space. Show a small sub side of the house houses in
price versus square footage space using TIKZ.

**36.** (p.9 — the Figure 1.4 axes, "predicted price ($)")
this plot would be better as square footage versus actual sale price

**37.** (p.10 — "Through the geometric lens, the degenerate case first. If
w = 2v, every combination collapses onto one line")
without a TIKZ image this lands flat

**38.** (p.10 — "a stretch of v no matter what c and d do.")
This is also just a scale multiplication for a = c+2d

**39.** (p.10 — "If w points off the line, the combinations fill an entire
plane.")
Show me that with TIKZ

**40.** (p.10 — "Listing 1.7 (sweeping the span) runs the same sweep
twice...")
saying it again, though I haven't for all cases. Listings need a header
and explanatory text every time and we need a policy for

**41.** (p.10 — the span_cloud listing code)
definition and execution requires separate listings

**42.** (p.10 — equation (1.9), the membership elimination align)
This is confusing. What are you trying to convey?

**43.** (p.10 — "Now check the candidate directly... Verifying a candidate
is a licensed method in this book, and the license arrives with Claim
1.10.")
an opportunity for existence uniqueness

**44.** (p.11 — Claim 1.7 box, the one-breath-reason body)
Put claims and their reasoning literally in a box

**45.** (p.11 — "Two vectors span at most a plane... the reach of the
operation is bounded by the number of ingredients... no metaphor
involved.")
I called this paragraph out last time. What is its purpose?

**46.** (p.11 — footnote 7, the footnote-about-footnotes: "the fuller
arguments live down here and in the references, on purpose... gatekeepers
... subscript fiddliness...")
Should this make its debut here? Probably earlier

**47.** (p.12 — "Here is what that buys us with the houses, one feature
first. GrLivArea alone is a single vector in R^1460... reach the nearest
point of the line.")
I like where this is going but it's still a bit unclear. I think either
this comes later or we need to add more before this so that we're ready
for this

**48.** (p.12 — "It is the drawing from the preface, a vector hanging just
off a subspace, now with names on it.")
OK this helps 47. I think referencing figures from another chapter
shouldn't be done. They should be shown again.

**49.** (p.12 — "Add OverallQual and the span grows to a sheet... The tip
of y still hovers off it... gets its name in Chapter 11.")
But yeah still confused

**50.** (p.12 — "The span of a set of feature columns earns a permanent
name. It is called the column space... Chapter 2 stacks the columns into a
matrix and the name turns literal.")
Introducing column space earlier may help. In terms of the needs of column
space itself. This is not the way to introduce it. So… this section is
about span. I don't know why we're trying to get to projections here

**51.** (p.12 — "Take the plane spanned by two vectors and bring in a
third...")
Show with tikz

**52.** (p.12 — footnote 10, the zero-test equivalence)
Isn't this what you showed

**53.** (p.13 — equation (1.11): "1v + 2w − 1u = (2,1) + (2,6) − (4,7) =
(0,0)")
I think with this and honestly most of the concepts in the chapter we need
at least one worked problem

**54.** (p.13 — Figure 1.6, "u = 1v + 2w lands inside the span")
Listing code?

**55.** (p.14 — "the standard basis e1 = (1,0,0), e2 = (0,1,0), e3 =
(0,0,1)")
Define the standard basis

**56.** (p.14 — footnote 13, "ingredients" [yellow])
Where did ingredients come from? Not really into the metaphor

**57.** (p.15 — "Measurement starts on the unit circle")
Define the unit circle formally

**58.** (p.15 — "the vectors of magnitude one form a circle of radius one
around the origin")
This extends to n dimensions

**59.** (p.15 — equation (1.13): "(3,4) = 5·(0.6, 0.8), sqrt(0.36+0.64)=1")
As does the Pythagorean theorem. We should show both

**60.** (p.15 — "Take v = (3,4). Walk three east and four north; the
straight-line distance back to the origin is the hypotenuse, and
Pythagoras says 5.")
Too eli5

**61.** (p.15 — "Magnitude 5, direction (0.6, 0.8). Every nonzero vector
factors this way, and the factorization is the whole geometry of a
vector.")
My thought on the unit circle was to walk in to cosine similarity

**62.** (p.15 — the whole block from Definition 1.13 through Definition
1.14 and beyond, big green sweep)
I think this goes in the preface, maybe the whole unit circle but too
let's discuss. I say we drop Cauchy Schwartz altogether

## Unnumbered color flags

Color key (Josh, 2026-07-13): GREEN + number = numbered note. YELLOW =
voice flag (rewrite the delivery, keep the idea). **PINK = DELETE THIS.**

DELETE (pink):

- (p.1) "and both names deserve their definitions up front."
- (p.2) "That is the bargain. You get the speed of the compiled code
  without writing it."
- (p.4) "That is not a coincidence."
- (p.4) "The preface promised a song. These are the opening bars."
- (p.10) "and the second ingredient bought nothing."
- (p.14) "The word will do quiet work for the rest of the book, so it gets
  its footnote now."

Voice flags (yellow):

- (p.4) "and you have just watched your machine treat it as the most
  important thing it knows how to do."
- (p.4) "What the two properties buy is out of all proportion to what they
  cost."
