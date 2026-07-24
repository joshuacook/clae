# manuscript/ — the book

The canonical manuscript. One file per document, figures flat in
figures/ (names unique book-wide). **Versioning is git**: history via
commits, delivered draft books via tags (v12, v13, ...). No version
suffixes in filenames, no draft-state header comments, no parallel
copies.

- preface.md
- ch01.md — The Agreement: Vectors, Spaces, and Combinations
- ch02.md — Matrices as operators
- ch03.md — Solving Linear Systems (the machine)
- ch04.md — Eigenvalues, Eigenvectors, and Diagonalization
- ch05.md — Random Vectors and Probability Spaces

Josh edits these files directly (or via scribe); his diffs are the
highest-authority voice signal. Render: tools/render/ pipeline, staged
in the session scratchpad, built on Cloud Build.
