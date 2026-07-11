# Ch 2 (Matrices and Linear Transformations) — conversation notes

## 2026-07-10 (synced 2026-07-11) — footnote stock from the origin session

**The trig-magic deep cut (placement candidate: Ch 2 footnote and/or preface
texture):** sin(a+b) = (cos b)·sin a + (sin b)·cos a is a linear combination —
a rotation acting on the {sin, cos} basis. The reader knew a basis in high
school, and the trig identity sheet was its span. Kruidenier's calc 2 magic
(the whole sheet from a+b and a−b) is the lived version; Ch 2 is where
rotation-as-matrix makes it precise.

**numpy/pandas as the row/column duality's memory address (DFW footnote
candidate):** Josh: "maybe we're also cutting at how numpy wants to be row
oriented but pandas wants to be column oriented? Maybe … I'm not sure." numpy
C-order stores rows contiguously; pandas stores column blocks; strides decide
which picture is cheap. Pending the DFW-footnote method confirm.
