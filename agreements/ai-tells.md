# AI tells — the blocklist

Claude drafts the prose; Josh edits. This file is the standing guard against the
draft reading like a language model wrote it. Check every drafting pass against
it. When Josh's edits reveal a new tell, add it here.

## Punctuation and structure

- **Em-dashes.** Banned repo-wide (see `emdash-purge.md`). Use commas, periods,
  or parentheses.
- **"not X, but Y" / "It's not just X, it's Y" / "isn't just" / "more than
  just."** The single most recognizable LLM sentence shape. Say what the thing
  is, directly.
- **Rule-of-three padding** ("fast, simple, and powerful"). Triads are fine when
  the content is genuinely three things; reflexive triads are filler. Two items
  or one strong one usually beats three weak ones.
- **Anaphora triads** ("It means X. It means Y. It means Z."). Same disease,
  sentence-scale.
- **Colon headline constructions** ("Span: Why It Matters"). Headings say the
  thing itself.
- **Perfectly parallel bullet lists in prose contexts.** If it can be a
  paragraph, it's a paragraph.
- **Bold-term-then-definition rhythm** repeated more than the material demands.
- **Chiasmus / "the X-ing was the Y-ing"** ("the deciding was the staying").
  Josh's catch (first scribe redline, 2026-07-11): "Awkward AI metaphor.
  Hidden not this that." The contrastive epigram is the not-X-but-Y tell in
  formalwear. Say the plain version: "That was the decision."

## Vocabulary (never)

delve, dive into, deep dive, unpack, explore (as filler), journey, landscape,
tapestry, realm, testament to, game-changer, supercharge, seamless, robust
(as praise), leverage (as verb), harness (as verb), elegant (self-applied),
powerful (as filler), crucial, pivotal, vital (stacked as intensifiers),
foster, empower, elevate, streamline, cutting-edge, state-of-the-art,
comprehensive (self-applied), rich (as in "rich insights"), nuanced
(self-applied), myriad, plethora, holistic, paradigm (outside its technical
sense), synergy.

## Sentence-level habits (avoid)

- **Throat-clearing openers:** "In this chapter, we will…", "Before we begin…",
  "Let's take a moment to…". Start with the thing.
- **Hedge phrases:** "It's worth noting that", "Importantly,", "Notably,",
  "Interestingly,", "Note that" (repeated). If it's worth noting, note it.
- **Empty kickers:** "In summary", "In conclusion", "At the end of the day",
  "Ultimately," (as a paragraph starter).
- **Stance fillers:** "At its core", "Essentially,", "Fundamentally,",
  "Simply put," as sentence openers.
- **"serves as" / "acts as" / "stands as."** Things ARE.
- **Formulaic rhetorical question + immediate answer** ("So what is a basis?
  A basis is…"). Josh asks real questions and lets them hang; the tell is the
  self-answering setup.
- **Both-sides hedging:** "While X is true, it's important to remember Y."
- **Excessive signposting:** "As we saw in the previous section…", "As
  mentioned earlier…". Trust the reader's memory or restate the fact itself.
- **Audience pandering:** "Whether you're a data scientist or a curious
  beginner…".
- **"The beauty of X is…"** Show the beauty; don't announce it.
- **"Think of X as…"** Analogies are welcome; the reflexive "think of" frame is
  the tell. Just make the analogy.
- **Uniform sentence length.** LLM prose hums at one rhythm. Vary it. Land
  short sentences.

## What the voice DOES sound like (from Josh's own text)

Anchors: §1.0 as edited by Josh; his verbatim quotes in
`chapter_notes/clae-*-conversation.md`; *Docker for Data Science*.

- **Short declarative punches after buildup.** "That is the whole of the
  operation." "Look at it."
- **Grand claim, then immediately a concrete number.** "Fundamental truths of
  the nature of existence" lives one page from "$51.87 per square foot." The
  register ceiling is Euclid; the floor is a timing table. Move between them
  fast.
- **Second person, peer-to-peer.** The reader is a sharp colleague, twelve
  years rusty. Never lecture down, never pander.
- **Dry, specific humor.** "Delivered by a function you did not build and do
  not yet deserve." "In axpy we trust." The joke is always load-bearing.
- **Compressed aphorisms as section landings.** "The plot is the weights."
  "The list was never the vector; it was the recipe." "Learn to see linear
  combinations everywhere, and the rest of the book is commentary."
- **Honest about cost and measurement.** Real numbers, real machine, "your own
  machine will print different numbers; the shape of the gap will not."
- **Enthusiasm shown by exactness,** not exclamation points. (Exception: a
  quoted "Like what?" is his; keep quoted energy verbatim.)
- **The fragment cold open** (from his own preface rewrite, 2026-07-11):
  "5. / Out of twenty-five." Two fragments, then the scene.
- **One-word sentence bursts** for overwhelm or inventory: "Spans. Bases.
  Linear Combinations."
- **The footnote as a joke with a payoff:** "no one called him Professor
  Kruideneir, or even Professor K. We called him Jim."
- **Self-aware irony, one per scene, dry:** "My route to higher math was
  ironically non-linear."
- **Concrete scene furniture over abstraction:** the janitor and the trash
  can, not "late into the evening."
- **One-line charters:** "if I can teach math, I can do math."

## Handling Josh's own prose (standing rules, 2026-07-11)

- **Verbatim means verbatim.** When Josh writes or rewrites prose, it is final
  text. Do not smooth grammar, add articles, repunctuate, or normalize his
  footnotes. The only permitted touches are markdown-mechanical (escaping
  "5\." so it doesn't render as a list, converting \footnote{} syntax).
- **His bursts are blows, not notes.** "Spans. Bases. Linear Combinations."
  lands as is; short fragments in his text are punches, never placeholders
  for Claude to expand.
- **The cuteness threshold.** A hinge line that winks at its own cleverness is
  "too cute" (his verdict on "The night class was the first time anyone
  played me the song"). End on the plain blow instead ("…I was the one who
  had spent a decade copying sheet music."). Callbacks may resolve quietly at
  the end of the book, not preen mid-page.
- **Narrator stance:** an initiate showing you openly, not a magician hoarding
  ("It was no secret").

## Voice additions mined from Josh's prior papers (2026-07-11)

From *Computational Methods in Molecular Quantum Mechanics* (2015) and *The
Zernike Polynomials* (2014):

- **Verdict sentences after a measurement.** State the number, then pass
  judgment on it in a short sentence: "This last result is astounding."
- **The courteous hand-wave, with a wink.** When skipping rigor, say so with
  manners: "Please understand that we are liberal with our implicit
  understanding…" Aligns with the assume-GE policy.
- **In-line editorial self-critique.** He audits his own work in the text: "I
  am not pleased with this particular test… It is very 'numerical'." Honest,
  disarming, keep it.
- **Antique verbs as spice,** sparingly: "behoove."
- **Constructive genesis framing.** Explain objects by how they were built:
  "created by subtracting lower order polynomials to create this orthogonality
  relationship."
- **Stack-consciousness as identity.** He cares which layer of the software
  stack a thing happens in, and jokes about it (Leanpub bio: "always willing to
  discuss orthogonality or to explain why Fortran is the language of the future
  over a warm or cold beverage").

Blocklist additions from the same papers (his old academic habits he has since
shed; do not resurrect):

- **Passive result-reporting:** "It is shown that…"
- **"We have written the following function"** throat-clearing before code.
  Show the code; let it introduce itself.

## THE APHORISM TIC (ruled 2026-07-12 — the big one)

The self-pleased closer: a sentence that exists to admire its own compression.
Josh's inked pass of Ch 1 yellow-flagged 25 of them (yellow = AI voice). The
full inventory, verbatim, as negative exemplars. The BEAT under each may
survive; the DELIVERY may not.

1. "the shape of the gap will not."
2. "Learn to see linear combinations everywhere, and the rest of the book is
   commentary."
3. "Hold that last one; it returns in Section 1.5 with money attached."
4. "But there is no reason you should wait two hundred pages to hear the song"
5. "and do not yet deserve."
6. "Most readers of this book have called lstsq or one of its cousins
   professionally; the mystery was never getting the answer, it is why the
   answer works and when to trust it."
7. "This chapter starts the collection."
8. "you have the only move this book ever makes:"
9. "You have seen this sentence before; it priced a house a page ago."
10. "so the machine never gets to hide the mechanism from you"
11. "the mechanism is this one."
12. "The set we just built has structure worth naming."
13. "and it teaches the pattern every closure proof in this book follows"
14. "One more thing before the data, because it decides whether you can trust
    your own drawings."
15. "You were never supposed to see the ambient space"
16. "and the name is two hundred pages away;"
17. "The two phrasings are the same test worn two ways:"
18. "and the equivalence closes."
19. "Independence tells us when a vector earns its place. Now for the kit
    that has no freeloaders and no gaps."
20. "nothing wasted, nothing missing."
21. "Instantiate it by hand before the machine does."
22. "we will lean on that compatibility constantly and mostly without comment"
23. "and the one sentence estimation ever says at the top of it."
24. "A basis is the minimal kit" / "which is what a list of numbers secretly
    was all along." / "and hands us orthogonality" (three flags, one summary
    paragraph)
25. "You exit this chapter holding:" / "the minimal kit and" / "Chapter 2
    takes the matrix out of storage and runs it." (three flags, one exit
    paragraph)

**BLUE exemplar (liked, write toward this):** "the reach of the operation is
bounded by the number of ingredients."

## More standing rules (ruled 2026-07-12)

- **Definition economy.** "Definitions require an economy of language. As few
  and as simple words required for rigor."
- **Footnotes over parentheticals.** A parenthetical aside that runs past a
  few words is a footnote wearing the wrong clothes. Move it down.
- **Code: well-named functions over comments.** `list_comp_in_python` needs
  no comment; `by_hand  # pure Python` did. Delete comments a good name makes
  redundant.
- **Preview-closer ban (confirmed).** No section may end by advertising a
  future chapter's payoff as its exit line.
- **No line-broken inline code.** If an expression matters enough to risk a
  line break, it is display math.
- **Proofs are the Strang way** (see chapter-anatomy.md): witness + one-breath
  reason; arguments to footnotes/citations; no ∎, no "Proof." headers, no
  proof-pattern meta-teaching. "Proofs are just gatekeeping" when performed
  in the text.

## From the preface v5 ink (2026-07-12)

- **The colon tic.** "Colons starting to replace emdashes" (Josh). The em-dash
  ban squeezed the same rhetorical move into colons: "X: the Y, the Z,
  everything except W." Same disease, new punctuation. His fix: "can you just
  write a second sentence?" Write the second sentence.
- **Flagged prose never resurfaces.** Josh: "I just flagged these as bad prose
  and here they are again" — v5 reused sentences yellow-flagged in v4. Once a
  phrase is yellow-flagged, it is dead in ALL future drafts, not just the one
  under review. Check new drafts against prior flags.
- **"Too cheeky"** joins "too cute": a promise that winks ("by Chapter 10 you
  will hear a full symphony") gets tempered to the plain promise.
- **SHOW, don't tell** is ink-enforceable: if prose describes a computation
  ("make triangles, then climb down them"), show the computation.
