<!-- PREFACE v3.2 (affirmed via the co-writing channel, 2026-07-11; committed on
     sync). Both texture gaps resolved from Josh's answers ("oblivion"; "Jim
     left at 8"); those two renderings are fresh and await his redline in
     scribe. Companion cell: clae-code/ch00/preface.ipynb (canonical 0.0031). -->

# Preface

The first quiz came back with a five on it. Five out of twenty-five, in a linear algebra night class at Santa Barbara City College, 2013. I was thirty-seven years old, back in school for a second bachelor's degree, this one in applied mathematics, and I remember the thought exactly: this is the end for me. This quixotic quest ends here. What it would have ended to, I couldn't have said. There was no other plan. Oblivion.

The class let out at eight and took my professor Jim Kruideneur with it. I stayed, quiz flat on the desk, working back through everything I had gotten wrong, and when I looked up it was ten o'clock. Nobody watched me do it. The deciding was the staying ##n: Awkward AI metaphor. Hidden not this that##. 

I had taught high school geometry, real geometry, two-column proofs, in Spanish #n this sentence has a lot of commas is this was necessary? #n, to students the system had been failing for years. Paul Lockhart says we teach mathematics the way we would teach music if we made children copy sheet music for a decade and never played them a song.[^lockhart] I had built a teaching life against that sentence. Then I sat down in a community college linear algebra class and drowned anyway.

[^lockhart]: Paul Lockhart, *A Mathematician's Lament: How School Cheats Us Out of Our Most Fascinating and Imaginative Art Form*, Bellevue Literary Press, 2009. The essay circulated informally from 2002 before Devlin talked him into the book.

The teacher was Jim Kruidenier. Jim is a mystic steeped in the ways of Gilbert Strang, and if that name is new to you, it names a tradition. Strang taught linear algebra at MIT for six decades, and the filmed lectures of his course, 18.06, free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/), have probably taught this subject to more people than any classroom on earth. There have long been two ways to teach a first course. The old way runs on determinants; you compute your way through a semester and the geometry never quite arrives. The audacious way is Sheldon Axler's *Linear Algebra Done Right*, a beautiful second course wearing the title of a first one, which banishes determinants nearly to the last page. Strang found the third way, and found it first: start from the columns, build the subspaces, let geometry and computation carry the argument, and keep the determinants in the drawer until they earn their keep. Strang is the precursor to Axler, without the audacity. This book is written in his church. Jim had read the book, absorbed the lectures, and taught everything he found completely in the open, nothing held back for the initiated. I never met Strang. I met Jim.

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