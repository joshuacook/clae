<!-- PREFACE v4 (2026-07-11): Josh rewrote the opening himself (paras 1-5 are
     his, verbatim with mechanical fixes only). The route/Lockhart paragraph is
     Claude's fresh draft answering Josh's design NOTE; redline freely.
     Companion cell: clae-code/ch00/preface.ipynb (canonical 0.0031).
     SPELLING FLAG: Kruidenier / Kruideneur / Kruideneir have all appeared;
     using Josh's latest (Kruideneir) pending his final confirm. -->

# Preface

5\.

Out of twenty-five.

I was thirty-seven years old taking a night class in linear algebra at Santa Barbara City College. After ten years as high school geometry teacher, I had decided that if I can teach math, I can do math. This was the beginning of that quest. Staring at the 5, I was sure it was over.

The class let out at eight and took Jim[^jim] with it. I stayed and decoded this mystic art in which Jim was attempting to initiate us ... Linearity.

[^jim]: Professor Jim Kruideneir 25 year veteran of the SBCC math department, but no one called him Professor Kruideneir or even Professor K, we called him Jim.

I was swimming. Spans. Bases. Linear Combinations. I sat in that desk well after the janitor had emptied the trash can, working through everything I had gotten wrong. It was well into the night when I walked to the car to head home.

My route to higher math was ironically non-linear. Before I was a student of Jim's (and an acolyte of Strang's), I had been a teacher of high school geometry in South Los Angeles, some of the toughest classrooms in the country, where the focus was often structure and stability at the expense of rigor. Geometry is the outlier of high school mathematics, the one course where students are asked to reason rather than compute, the way linear algebra is the outlier of the lower division. I had chosen the outlier on purpose. Somewhere in those years I read Paul Lockhart's *A Mathematician's Lament*, a working mathematician's essay on what school does to his subject.[^lockhart] Lockhart says we teach mathematics the way we would teach music if we made children copy sheet music for a decade and never played them a song. I recognized my own classroom in the accusation and did what I could against it: real geometry, two-column proofs, in Spanish. But the Lament reads differently once you are the student. Staring at that 5, I was the one who had spent a decade copying sheet music.

[^lockhart]: Paul Lockhart, *A Mathematician's Lament: How School Cheats Us Out of Our Most Fascinating and Imaginative Art Form*, Bellevue Literary Press, 2009. The essay circulated informally from 2002 before Devlin talked him into the book.

Jim is a mystic steeped in the ways of Gilbert Strang, and if that name is new to you, it names a tradition. Strang taught linear algebra at MIT for six decades. His filmed lectures are available free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) and have probably taught this subject to more people than any classroom on earth.

There have long been two ways to teach a first course in linear algebra. One way runs on determinants; you compute your way through a semester and the geometry never quite arrives. The audacious way is Sheldon Axler's *Linear Algebra Done Right*, a beautiful second course wearing the title of a first one, which banishes determinants nearly to the last page. But Axler's way is Strang's way wearing a confrontational title, and Strang found it first: start from the columns, build the subspaces, let geometry and computation carry the argument, and keep the determinants in the drawer until they earn their keep. That is the whole creed. Pictures before procedures, actions before formulas, nothing hidden from the congregation. This book is written in that church, and Jim taught from inside it, everything in the open, nothing held back for the initiated. I never met Strang. I met Jim.

That semester I was also taking waves in physics, and partway through the term the same word surfaced in both rooms: basis. In Jim's room, the vectors underneath a list of coordinates. In the physics room, the sinusoids underneath a Fourier series. One word, both rooms meaning exactly the same thing by it, neither having asked the other's permission. Basis was the jewel. I would like to report a slow dawning. What I remember is more like being let in on something.

Strang's chapter 4 is orthogonality. There is a drawing in it: a vector hanging just off a subspace, a perpendicular dropped to the nearest point, and the whole machinery of regression falling out of that one picture. The night it clicked I cracked my knuckles and said, out loud, to a textbook: I see you, Gil. This book has one destination, and it is that drawing. You will meet it, properly earned, in Chapter 11.

The next year Jim marched us through vector calculus and then differential equations, and linear algebra kept coming back, uninvited, inside everything. Off syllabus I found Stephanie Frank Singer's book on the hydrogen atom and learned that electron orbitals are a basis. By the time I transferred to Cal State Northridge, partial differential equations felt almost easy.

At Northridge, Strang got me a second time. In the math study room on the third floor of the math building I found his *Computational Science and Engineering*, the book he built around one small matrix, second differences down the diagonal, and that is where the matrix became a verb for me. A derivative, on a grid, is a matrix:

$$D = \frac{1}{h}\begin{bmatrix} -1 & 1 & & \\ & -1 & 1 & \\ & & \ddots & \ddots \\ & & & -1 \end{bmatrix}$$

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
h = x[1] - x[0]
D = (np.eye(1000, k=1) - np.eye(1000)) / h    # -1 and 1 down the diagonals

np.abs(D @ np.sin(x) - np.cos(x))[:-1].max()  # 0.0031
```

Feed it a sampled sine and it hands back the cosine, wrong in the third decimal, and the error shrinks as the grid tightens. The matrix took the derivative. I carried that into an independent research project in Jussi Eloranta's quantum chemistry lab, where the Schrödinger equation for a particle in a box collapsed into a matrix eigenproblem, the eigenvectors came out as sines, and I spent a semester racing my own eigensolvers against LAPACK and writing up the results. Singer's hydrogen atom sat in that paper's references. I put the paper up on Leanpub, where it sits to this day, largely unbothered. Eleven years later, it grew into the book you are holding. The class that nearly ended me had become the foundation of a second career, and the kind of subject I would argue about with friends over a beer.

You took linear algebra, maybe more than once. You know the words; you may even use them at work, at arm's length, through a library call. Either nobody ever played you the song, or somebody did, once, and you have not heard it in years.

I think the principles of linearity are the coolest things we have found since Euclid wrote down five postulates and got geometry for them. This book asks for less. Two operations and a promise to stay closed under them, and fourteen chapters on what that buys. Every figure and number in it is produced by code you can run yourself, and all of it aims at one question. Of all the linear combinations available, which one is the estimate?

You have your own five out of twenty-five somewhere. Stay in the room.
