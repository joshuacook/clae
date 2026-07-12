<!-- PREFACE v6 (2026-07-12): Josh's verified v5 ink census applied
     (chapter_notes/preface-v5-ink-verified.md, 61 approved marks): deletes,
     paragraph splits, colon purge, mixed-metaphor fix, 3x3 elimination shown,
     three ways shown, TikZ projection figure, uniqueness paragraph MOVED to
     Ch 1, Singer to a footnote, honesty beat resolved (he saw it and said it).
     Companion cell: clae-code/ch00/preface.ipynb (canonical 0.0031).
     Words: 2021 prose / 2274 total (auto: tools/wordcount.py)-->

# Preface

Five.

Out of twenty-five.

I was thirty-seven years old taking a night class in linear algebra at Santa Barbara City College. After ten years as a high school geometry teacher, I had decided that if I can teach math, I can do math. It was the era when every job board sang the ballads of data science, heraldry for a kingdom that wanted mathematicians and would settle for the retrained. I heard the songs. I enrolled. This was the beginning of that quest, me atop my donkey with a newly acquired Pythonic lance. Staring at the 5, I was sure the quest was over, dashed by a windmill named after Strang's ways of seeing matrix multiplication.

The class let out at eight and took our professor, Jim,[^jim] with it. I stayed and worked at this mystic art into which Jim was attempting to initiate us ... Linearity.

[^jim]: Professor Jim Kruidenier 25 year veteran of the SBCC math department, but no one called him Professor Kruidenier or even Professor K, we called him Jim.

I was unhorsed. Spans. Bases. Linear Combinations. I sat in that desk well after the janitor had emptied the trash can, working through everything I had gotten wrong. It was well into the night when I walked to the car to head home.

&nbsp;

The windmills deserve their names, because you will not fight them in this book. The quiz was the machinery of Strang's opening chapters: solving a linear system by Gaussian elimination, back substitution, and the several ways of multiplying two matrices. Elimination first. Subtract a multiple of one equation from another to kill an unknown, repeat until the system is triangular.

$$\begin{aligned} x + 2y + z &= 5 \\ 2x + 5y + 4z &= 13 \\ x + 3y + 5z &= 12 \end{aligned}
\quad\longrightarrow\quad
\begin{aligned} x + 2y + z &= 5 \\ y + 2z &= 3 \\ 2z &= 4 \end{aligned}$$

Then climb down the triangle. The bottom row gives $z = 2$. Carry it up: $y = 3 - 2(2) = -1$. Carry both up: $x = 5 - 2(-1) - 2 = 5$. Every unknown falls in turn.

And matrix multiplication, which Strang teaches three ways. Take one small product and watch it three times:

$$AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

Entry by entry, each number is a row dotted with a column: the $19$ is $(1, 2) \cdot (5, 7) = 5 + 14$. Column by column, $A$ acts on each column of $B$: the first column of $AB$ is $5$ copies of $(1, 3)$ plus $7$ copies of $(2, 4)$, which lands on $(19, 43)$. And as a sum of outer products, column times row, the matrix built from rank-one slabs:

$$\begin{bmatrix} 1 \\ 3 \end{bmatrix}\begin{bmatrix} 5 & 6 \end{bmatrix} + \begin{bmatrix} 2 \\ 4 \end{bmatrix}\begin{bmatrix} 7 & 8 \end{bmatrix} = \begin{bmatrix} 5 & 6 \\ 15 & 18 \end{bmatrix} + \begin{bmatrix} 14 & 16 \\ 28 & 32 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

Three views of one multiplication. This book assumes the windmills. Elimination will be used and never taught; the three ways will be named when needed and never drilled. If they are rusty, twenty minutes with Strang's first two chapters restores them. The quest in this book begins where that quiz ended, with what the machinery means.

&nbsp;

My route to higher math was ironically non-linear, given that once there, my path became an obsession with linearity. Before I was a student of Jim's (and an acolyte of Strang's), I had been a teacher of high school geometry in South Los Angeles, some of the toughest classrooms in the country, where the focus was often structure and stability at the expense of rigor.

Geometry is the outlier of high school mathematics, the one course where students are asked to reason rather than compute. The rest of the sequence is a pipeline: algebra into precalculus into calculus, every course a taller stack of procedures, every answer a number at the end of a computation. Geometry interrupts the pipeline.

For one year the question changes from what is the value to why is this true, and the answer is an argument you build and defend, the way Euclid built them: two triangles, side angle side, therefore. Then the pipeline resumes and runs three semesters of calculus deep into the university.

Linear algebra interrupts the university sequence the way geometry interrupted high school. The objects come with structure. The claims come with reasons. What a thing is carries more weight than how to evaluate it. I taught the high school interruption for ten years, and when I went back to school, its university counterpart was waiting for me.

Somewhere in those teaching years, I read Paul Lockhart's *A Mathematician's Lament*, a working mathematician's essay on what school does to his subject.[^lockhart] Lockhart's thesis deserves stating in full, because this book is an attempt to act on it. Mathematics, he says, is an art, the art of pattern and imagination, and the most misunderstood subject in the curriculum, because school teaches its paperwork instead. The notation, the procedures, the answer-getting; everything except the experience of doing the thing.

His famous figure is musical. Imagine teaching music by making children copy sheet music for a decade, grading their clefs and their stem directions, and never once playing them a song. I recognized my own classroom in the accusation, and I fought it with real geometry and two-column proofs. But the Lament reads differently once you are the student. Staring at that 5, the decade of sheet music was mine. Nobody had played me the song either. This book intends to play the song. Chapter 10 is the symphony.

[^lockhart]: Paul Lockhart, *A Mathematician's Lament: How School Cheats Us Out of Our Most Fascinating and Imaginative Art Form*, Bellevue Literary Press, 2009. The essay circulated privately from 2002 until Keith Devlin, who wrote the MAA's Devlin's Angle column, published it there in 2008 and talked Lockhart into the book.

&nbsp;

Jim is a mystic steeped in the ways of Gilbert Strang, and if that name is new to you, it names a tradition. Strang taught linear algebra at MIT for six decades. His filmed lectures for the course, 18.06, are free to anyone,[^ocw] and have probably taught this subject to more people than any classroom on earth.

[^ocw]: [MIT OpenCourseWare, 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/).

There have long been two roads through a first course in linear algebra. The old road runs on determinants. You compute your way through a semester, and the truth never quite arrives. The determinant people are still out there, computing. The audacious road is Sheldon Axler's *Linear Algebra Done Right*, a beautiful second course wearing the title of a first one, which banishes determinants nearly to the last page. But Axler's road is Strang's road wearing a confrontational title, and Strang cut it first. Start from the columns, build the subspaces, let geometry and computation carry the argument, and keep the determinants in the drawer until they earn their keep. Pictures before procedures, actions before formulas, nothing hidden from the congregation. This book is written in that church, and Jim taught from inside it, everything in the open, nothing held back for the initiated.[^jimsite] Strang I know only from the page and the screen. Jim I knew on Tuesday and Thursday nights, chalk in hand.

[^jimsite]: The receipts survive. Jim's course site posted every lecture twice, blank notes and completed notes, plus an archive of every old exam. The domain, mathjimk.com, has since gone dark, but the Internet Archive holds a copy: [web.archive.org/web/20180806081310/http://mathjimk.com/](https://web.archive.org/web/20180806081310/http://mathjimk.com/) (captured August 6, 2018).

That semester I was also taking waves in physics. Partway through the term the same word surfaced in both rooms: basis. In Jim's room, the vectors underneath a list of coordinates. In the physics room, the sinusoids underneath a Fourier series, though physics never said the word out loud. I saw it, and I said it. Basis was the jewel, and it would keep resurfacing for years, all the way to the electron, whose orbitals are built from a basis too, Laguerre polynomials dressed in spherical harmonics.[^singer]

[^singer]: The whole story of that basis, told through one atom: Stephanie Frank Singer, *Linearity, Symmetry, and Prediction in the Hydrogen Atom*, Springer, 2005. I read it off syllabus that year, and it sits behind Chapter 3 of this book.

Strang's chapter 4 is orthogonality, and there is a drawing in it: a vector hanging just off a subspace, a perpendicular dropped to the nearest point, the whole machinery of regression falling out of one picture.

\begin{center}
\begin{tikzpicture}[scale=1.15]
  \draw[fill=gray!12, draw=gray!55] (-0.6,-0.4) -- (3.6,-0.4) -- (4.7,0.7) -- (0.5,0.7) -- cycle;
  \node[gray] at (4.0,-0.15) {\small the subspace};
  \coordinate (O) at (0.9,0.05);
  \coordinate (B) at (2.7,2.2);
  \coordinate (P) at (2.83,0.28);
  \draw[->, very thick] (O) -- (B) node[above] {$\mathbf{b}$};
  \draw[->, very thick] (O) -- (P) node[below right] {$\mathbf{p}$};
  \draw[dashed, thick] (B) -- (P) node[midway, right=2pt] {$\mathbf{b}-\mathbf{p}$};
  \draw (2.66,0.30) -- (2.68,0.47) -- (2.85,0.45);
\end{tikzpicture}
\end{center}

This book has one destination, and it is that drawing. You will meet it in Chapter 11.

The next year Jim marched us through vector calculus, where the gradient turned out to be a vector living in the same algebra we had just learned, and then differential equations, where solutions superpose, which is to say the solution set is a span wearing a trench coat. Linear algebra kept coming back, inside everything.

By the time I transferred to Cal State Northridge, partial differential equations felt almost easy, and I could finally say why: every technique in the course was the same move, expand the unknown in the right basis and watch the equation fall apart.

At Northridge, Strang got me a second time. In the math study room on the third floor of the math building I found his *Computational Science and Engineering*, the book he built around one small matrix, second differences down the diagonal. CSE is Strang with his sleeves rolled up, heir to the working tradition of *Numerical Recipes* and the Fortran libraries that still sit at the bottom of the modern stack. Those are not throwaway references. That tradition was about to become my daily work, and it is where the matrix became a verb for me. A derivative, on a grid, is a matrix:

$$D = \frac{1}{h}\begin{bmatrix} -1 & 1 & & \\ & -1 & 1 & \\ & & \ddots & \ddots \\ & & & -1 \end{bmatrix}$$

**Listing P.1** builds $D$ on a thousand-point grid, applies it to a sampled sine, and measures the worst error against the true derivative:

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
h = x[1] - x[0]
D = (np.eye(1000, k=1) - np.eye(1000)) / h    # -1 and 1 down the diagonals

np.abs(D @ np.sin(x) - np.cos(x))[:-1].max()
```

```text
0.0031
```

Feed it a sampled sine and it hands back the cosine, wrong in the third decimal, and the error shrinks as the grid tightens. The matrix took the derivative.

I carried that into an independent research project in Jussi Eloranta's quantum chemistry lab, where the Schrödinger equation for a particle in a box collapsed into a matrix eigenproblem and the eigenvectors came out as sines. The waves room again, years later, now as a theorem.

I spent that semester racing my own eigensolvers against LAPACK and writing up the results. The write-up did not sit still. It became a course bearing something akin to this book's title, Linear Algebra and Estimation Theory, which I taught at Caltech and taught again at UCLA. Eleven years after that night at the city college, the course grew into the book you are holding. The class that nearly ended me had become the foundation of a second career, and the kind of subject I would argue about with friends over a beer.

&nbsp;

You took linear algebra, maybe more than once. You know the words; you may even use them at work, at arm's length, through a library call. Either nobody ever played you the song, or somebody did, once, and you have not heard it in years.

Notice what every stop on my road had in common. The waves course asked which combination of sinusoids is this signal. The differential equations asked which combination of solutions fits these conditions. The orbitals asked which combination of basis states is this electron. The lab asked which combination of eigenvectors is the ground state. The same question, fifteen years running. Data asks it too, and calls it estimation. Of all the linear combinations available, which one is the estimate?

I think the principles of linearity are the coolest things we have found since Euclid wrote down five postulates and got geometry for them. This book asks for less than Euclid did. Two operations and a promise to stay closed under them. Everything else, fourteen chapters of it, every figure and number produced by code you can run yourself, is what that promise turns out to contain.

You have your own five out of twenty-five somewhere. Stay in the room.
