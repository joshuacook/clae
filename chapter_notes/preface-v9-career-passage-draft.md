<!-- TRANCHE 3 DRAFT — FOR REVIEW, NOT FINALIZED (Shaw's v9 assignment,
     2026-07-17). Replaces the two flat career paragraphs of the preface
     ("The write-up was the end of school..." and "I started teaching it...")
     if approved. Built from chapter_notes/preface-v9-career-beats.md and
     Josh's words in coyote interviews 021/022/025/026. Framing rules
     honored: UCLA-forward (General Assembly unnamed, folded into the
     teaching arc), X-ray saga OUT, over-employment / wealth-extraction /
     Databricks-tax era OUT. Voice per agreements/ai-tells.md. -->

# Preface v9 — the career half, re-inflated (DRAFT for Josh's review)

*Drop-in replacement. It begins where the CSUN act ends ("...and writing up
the results.") and runs to the "You took linear algebra" turn, which is
unchanged.*

---

The write-up was the end of school and the start of the career, and the career is the half of this story that data readers will recognize. The job boards' ballads from the first page of this preface turned out to be true. The kingdom really was hiring, and I went.

The first real assignment set the tone for the decade. A parking company had acquired some mathematics the way companies do, in a folder, from someone long gone, and the brief was one sentence: somebody wrote some math in there and we don't know how it works, can you fix it? The servers were too old to run scipy. So I opened *The Elements of Statistical Learning* and wrote the spline from scratch in NumPy, which is to say, I built it out of the operations in this book's first chapter, because that is all NumPy is. That spline grew into a parking-prediction service for BMW covering twenty cities, with a store for its engineered features years before "feature store" was a product category. I filled the whiteboards in a rec room no one else walked into. From the ping-pong table it must have looked like nonsense. It was a linear model earning its keep, and nobody in the building could see it. That gap, between what the mathematics was doing and who could see it, turned out to be the job.

Then I made the best strategic move of my career, and it will sound like a step down. I went to teach. Now I have data science in my job title, and it really was that simple. What I had not priced in was what the teaching would do to me. To stand in front of working engineers and explain why regularization works, why the covariance matrix has the shape it has, why the estimator lands where it lands, I had to understand those things past the point of using them, down to where the chalk meets the board. I was teaching graduate-level mathematics I had never formally studied, and teaching it honestly amounted to another degree, earned at the front of the room. The teaching settled at UCLA, curriculum by curriculum, and the material of this book started assembling itself there.

The decade had a rhythm to it, and the rhythm was arriving early. I gave a conference talk in 2016 about running data science in containers and watched the room not have a clue what I was talking about. The book of that talk, *Docker for Data Science*, went out through this book's own publisher in 2017 and still holds up, close to a decade on, with a couple of small tweaks. I shipped a language model into an education product in late November of 2022, and ChatGPT launched at the end of that same month. I do not list these to brag. I list them because being early is the working condition of anyone who trusts the mathematics over the product cycle, and the mathematics this book teaches is precisely what there is to trust.

And everywhere the career went, the night class was waiting for me. A regression at work is the drawing, a price vector floating above the sheet of what the features can reach, with a perpendicular dropped to the best combination, and at the parking company the sheet was spanned by engineered features of place and time. Principal component analysis is the basis hunt from the waves course pointed at a covariance matrix, and at a clothing company it wore the costume of an autoencoder watching denim for defects, the same hunt for the directions that matter. Extracting structure from clinical records, blending predictions with measurements, ranking, filtering, compressing: consulting, machine learning infrastructure, a decade of it. The tools changed names when they changed buildings. The question never changed at all.

I kept teaching it. The UCLA material grew, moved with me, and landed at Caltech under something akin to this book's title, Linear Algebra and Estimation Theory, taught to rooms full of working engineers who had all taken linear algebra once and mostly remembered the bookkeeping. Fifteen years after that night at the city college, those bodies of work grew into the book you are holding. The class that nearly ended me had become the foundation of a second career, and the kind of subject I would argue about with friends over a beer.

---

## Notes for the ruling

- **Beat 1 (spline by hand)** leads because it is the best single image of the thesis: the mathematics of Chapter 1 shipping as a product under constraint. "Whiteboards no one else walked into" kept near-verbatim.
- **Beat 2 (job title / another master's degree)** framed UCLA-forward. General Assembly is never named; the teaching arc reads as "went to teach → settled at UCLA → Caltech." Dates are soft ("the teaching settled at UCLA") per the fudge-for-clean-arc rule.
- **Beat 3 (three steps ahead)** names ODSC 2016, the Docker book (with the Springer/Apress family kept as "this book's own publisher," a nice bond with the reader holding a Springer book), and the pre-ChatGPT LLM deploy. Edmentum unnamed ("an education product"), Levi's unnamed ("a clothing company"), Nash Bio/Twin Health unnamed ("clinical records") to keep the bio clean of employer lists.
- **Beat 4 (buildings grounded)** upgrades the abstract "tools changed names" list: regression → BMW features, PCA → the Levi's autoencoder, plus clinical extraction. The Kalman sentence from v8 dropped here because the blending idea now lives in the "blending predictions with measurements" clause; restore the explicit Kalman sentence if you want the Ch 13/15 promise kept verbatim.
- **Beat 5 (teaching → book)** preserves your v8 sentence "those bodies of work grew into the book you are holding" and the beer line, which read as keepers.
- **Left out, per the rules:** X-ray saga, over-employment era, Databricks taxes, General Assembly by name, dollar figures.
- **Optional add (from interview 021, #6 thread):** in the CSUN act, one clause on Fortran: "after allocating my own memory in Fortran for Jussi's helium simulations, NumPy read as luxury." Not included above; it belongs to the earlier act if you want it.
