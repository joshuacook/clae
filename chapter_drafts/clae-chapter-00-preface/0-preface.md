<!-- PREFACE v5 (2026-07-12): drafted by claude.ai from Josh's verified ink
     census + rulings (five-act braid; windmill review interlude; Lockhart
     full thesis; guess-and-check license; earned closing question; yellows
     rewritten). NOT yet line-affirmed: awaiting Josh's scribe redline.
     Companion cell: clae-code/ch00/preface.ipynb (canonical 0.0031).
     Words: 2066 prose / 2199 total (auto: tools/wordcount.py) -->

# Preface

Five.

Out of twenty-five.

I was thirty-seven years old taking a night class in linear algebra at Santa Barbara City College. After ten years as a high school geometry teacher, I had decided that if I can teach math, I can do math. It was the era when every job board sang the ballads of data science, heraldry for a kingdom that wanted mathematicians and would settle for the retrained. I heard the songs. I enrolled. This was the beginning of that quest, me atop my donkey with a newly acquired Pythonic lance. Staring at the 5, I was sure the quest was over, dashed by a windmill named after Strang's ways of seeing matrix multiplication.

The class let out at eight and took Jim[^jim] with it. I stayed and worked at this mystic art into which Jim was attempting to initiate us ... Linearity.

[^jim]: Professor Jim Kruidenier 25 year veteran of the SBCC math department, but no one called him Professor Kruidenier or even Professor K, we called him Jim.

I was swimming. Spans. Bases. Linear Combinations. I sat in that desk well after the janitor had emptied the trash can, working through everything I had gotten wrong. It was well into the night when I walked to the car to head home.

&nbsp;

The windmills deserve naming, because you will not fight them in this book. The quiz was Strang's opening chapters, the machinery of solving. Gaussian elimination first: subtract a multiple of one equation from another to kill an unknown, repeat until the system is triangular, then read the answers from the bottom up.

$$\begin{aligned} x + 2y &= 5 \\ 3x + 4y &= 11 \end{aligned}
\quad\longrightarrow\quad
\begin{aligned} x + 2y &= 5 \\ -2y &= -4 \end{aligned}$$

So y = 2, then x = 1. That is the whole method: make triangles, then climb down them. And matrix multiplication, which Strang teaches three ways: entry by entry, each number a row dotted with a column; column by column, the product AB assembled by letting A act on each column of B; and as a sum of outer products, column times row, the matrix built from rank-one slabs. Three views of one multiplication, and I could not hold even the first one steady under quiz conditions. This book assumes the windmills. Elimination will be used and never taught; the three ways will be named when needed and never drilled. If they are rusty, twenty minutes with Strang's first two chapters, or Jim's archived notes, restores them. The quest in this book begins where that quiz ended: with what the machinery means.

&nbsp;

My route to higher math was ironically non-linear, given that once there, my path became an obsession with linearity. Before I was a student of Jim's (and an acolyte of Strang's), I had been a teacher of high school geometry in South Los Angeles, some of the toughest classrooms in the country, where the focus was often structure and stability at the expense of rigor.

Geometry is the outlier of high school mathematics, the one course where students are asked to reason rather than compute. The rest of the sequence is a pipeline: algebra into precalculus into calculus, every course a taller stack of procedures than the one before, every answer a number at the end of a computation. Geometry interrupts the pipeline. For one year the question changes from what is the value to why is this true, and the answer is an argument you build and defend, the way Euclid built them: two triangles, side angle side, therefore. Then the pipeline resumes and runs three semesters of calculus deep into the university, procedures all the way down.

Linear algebra is the same interruption on a higher shelf. It is the first university course where the objects have structure, where the claims want reasons, where what a thing is matters more than how to evaluate it. I had taught the lower interruption for a decade. When I came back to school I was looking for the upper one, though I could not have said so at the time. Twice now I have chosen the outlier on purpose.

Somewhere in those teaching years I read Paul Lockhart's *A Mathematician's Lament*, a working mathematician's essay on what school does to his subject.[^lockhart] Lockhart's thesis deserves stating in full, because this book is an attempt to act on it. Mathematics, he says, is an art, the art of pattern and imagination, and the most misunderstood subject in the curriculum, because school teaches its paperwork instead: the notation, the procedures, the answer-getting, everything except the experience of doing the thing. His famous figure is musical. Imagine teaching music by making children copy sheet music for a decade, grading their clefs and their stem directions, and never once playing them a song. I recognized my own classroom in the accusation and did what I could against it: real geometry, two-column proofs, in Spanish. But the Lament reads differently once you are the student. Staring at that 5, the decade of sheet music was mine. Nobody had played me the song either. This book intends to play it, and by Chapter 10 you will hear a full symphony.

[^lockhart]: Paul Lockhart, *A Mathematician's Lament: How School Cheats Us Out of Our Most Fascinating and Imaginative Art Form*, Bellevue Literary Press, 2009. The essay circulated privately from 2002 until Keith Devlin, who wrote the MAA's Devlin's Angle column, published it there in 2008 and talked Lockhart into the book.

Jim is a mystic steeped in the ways of Gilbert Strang, and if that name is new to you, it names a tradition. Strang taught linear algebra at MIT for six decades. His filmed lectures are available free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) and have probably taught this subject to more people than any classroom on earth.

There have long been two roads through a first course in linear algebra. The old road runs on determinants: you compute your way through a semester, and the truth never quite arrives. The determinant people never left that road; the word compute is doing all the work in that sentence. The audacious road is Sheldon Axler's *Linear Algebra Done Right*, a beautiful second course wearing the title of a first one, which banishes determinants nearly to the last page. But Axler's road is Strang's road wearing a confrontational title, and Strang cut it first: start from the columns, build the subspaces, let geometry and computation carry the argument, and keep the determinants in the drawer until they earn their keep. Pictures before procedures, actions before formulas, nothing hidden from the congregation. This book is written in that church, and Jim taught from inside it, everything in the open, nothing held back for the initiated.[^jimsite] Strang I know only from the page and the screen. Jim I knew on Tuesday nights, marker in hand.

[^jimsite]: The receipts survive. Jim's course site posted every lecture twice, blank notes and completed notes, plus an archive of every old exam. The domain, mathjimk.com, has since gone dark, but the Internet Archive holds a copy: [web.archive.org/web/20180806081310/http://mathjimk.com/](https://web.archive.org/web/20180806081310/http://mathjimk.com/) (captured August 6, 2018).

Jim's first lecture made a promise I did not understand for years. Before teaching us to solve anything, he showed us when solutions are unique. It seemed like a strange place to start. It is the perfect place to start, because uniqueness is a license: if the answer is one of a kind, then any way of finding it is legitimate, including the oldest and most poo-pooed method in mathematics, guess and check. Find a candidate however you like, verify it, and uniqueness does the rest. This book runs on that license.

That semester I was also taking waves in physics, the course the catalogs call oscillations and waves, the one where mechanics quietly trades Newton's computations for Fourier's intuition. Partway through the term the same word surfaced in both rooms: basis. In Jim's room, the vectors underneath a list of coordinates. In the physics room, the sinusoids underneath a Fourier series. One word, both rooms meaning the same thing by it, neither having asked the other's permission. I honestly cannot tell you whether the physics course said it out loud or whether I saw it on my own; the memory keeps no receipt. What I remember is the feeling of being let in on something. Basis was the jewel, and it would keep resurfacing for years, all the way to the electron, whose orbitals are built from a basis too, Laguerre polynomials dressed in spherical harmonics.

I started reading Strang ahead of the syllabus after that, hunting the next jewel. Strang's chapter 4 is orthogonality, and there is a drawing in it: a vector hanging just off a subspace, a perpendicular dropped to the nearest point, the whole machinery of regression falling out of one picture. The night it clicked I cracked my knuckles and said, out loud, to a textbook: I see you, Gil. This book has one destination, and it is that drawing. You will meet it, properly earned, in Chapter 11.

The next year Jim marched us through vector calculus, where the gradient turned out to be a vector living in the same algebra we had just learned, and then differential equations, where solutions superpose, which is to say the solution set is a span wearing a trench coat. Linear algebra kept coming back, uninvited, inside everything.

Off syllabus I found Stephanie Frank Singer's book on the hydrogen atom, and the jewel returned at atomic scale: electron orbitals are a basis, the atom's own coordinate system.

By the time I transferred to Cal State Northridge, partial differential equations felt almost easy, and I could finally say why: every technique in the course was the same move, expand the unknown in the right basis and watch the equation fall apart.

At Northridge, Strang got me a second time. In the math study room on the third floor of the math building I found his *Computational Science and Engineering*, the book he built around one small matrix, second differences down the diagonal. CSE is Strang with his sleeves rolled up, the tradition that runs back through Numerical Recipes to the Fortran libraries still sitting at the bottom of the modern stack, and it is where the matrix became a verb for me. A derivative, on a grid, is a matrix:

$$D = \frac{1}{h}\begin{bmatrix} -1 & 1 & & \\ & -1 & 1 & \\ & & \ddots & \ddots \\ & & & -1 \end{bmatrix}$$

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
h = x[1] - x[0]
D = (np.eye(1000, k=1) - np.eye(1000)) / h    # -1 and 1 down the diagonals

np.abs(D @ np.sin(x) - np.cos(x))[:-1].max()  # 0.0031
```

Feed it a sampled sine and it hands back the cosine, wrong in the third decimal, and the error shrinks as the grid tightens. The matrix took the derivative.

I carried that into an independent research project in Jussi Eloranta's quantum chemistry lab, where the Schrödinger equation for a particle in a box collapsed into a matrix eigenproblem and the eigenvectors came out as sines. The waves room again, years later, now as a theorem.

I spent that semester racing my own eigensolvers against LAPACK and writing up the results. Singer's hydrogen atom sat in the paper's references. I put the paper up on Leanpub, where it sits to this day, largely unbothered.

Eleven years later, it grew into the book you are holding. The class that nearly ended me had become the foundation of a second career, and the kind of subject I would argue about with friends over a beer.

&nbsp;

You took linear algebra, maybe more than once. You know the words; you may even use them at work, at arm's length, through a library call. Either nobody ever played you the song, or somebody did, once, and you have not heard it in years.

Notice what every stop on my road had in common. The waves course asked which combination of sinusoids is this signal. The differential equations asked which combination of solutions fits these conditions. The orbitals asked which combination of basis states is this electron. The lab asked which combination of eigenvectors is the ground state. One question, wearing different clothes for fifteen years. Data asks it too, and calls it estimation. Of all the linear combinations available, which one is the estimate?

I think the principles of linearity are the coolest things we have found since Euclid wrote down five postulates and got geometry for them. This book asks for less than Euclid did. Two operations and a promise to stay closed under them. Everything else, fourteen chapters of it, every figure and number produced by code you can run yourself, is what that promise turns out to contain.

You have your own five out of twenty-five somewhere. Stay in the room.
