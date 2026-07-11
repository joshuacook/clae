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
