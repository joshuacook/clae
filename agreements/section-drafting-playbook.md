---
title: "Section Drafting Playbook"
type: process
status: draft
created: "2026-03-08"
updated: "2026-03-08"
depends_on: writing-process.md
---

# Section Drafting Playbook

This playbook defines the processing chain for producing section-level artifacts (section notes + section outline, co-produced). It specifies how to classify sections by type, how to draft each type, and which lens set applies to each type.

## The Processing Chain

```
Chapter outline section entry
  │
  ▼
Step 1: CLASSIFY — determine section type
  │
  ▼
Step 2: DRAFT — produce section notes + outline using the type's draft approach
  │
  ▼
Step 3: LENS — apply the type's lens set (pass 1 → pass 2)
  │
  ▼
Final section notes + outline
```

### Inputs to the chain

- The chapter outline (lens-reviewed) — the section's content description, page budget, and position
- The chapter notes (lens-reviewed) — decisions, narrative arc, voice notes
- All prior sections' completed notes + outlines (within the same chapter)
- The book outline (for cross-chapter context)

---

## Step 1: Section Type Classification

Every section is classified into exactly one of nine types. Classification is based on the section's **primary structural purpose** — what it does for the reader.

When a section blends types (e.g., a method section with an embedded worked problem), classify by the dominant structure. The type-specific lenses for the secondary type can be added as supplementary lenses.

### The Nine Section Types

| Type | Purpose | Structural signature | Typical length |
|------|---------|---------------------|----------------|
| **Opener** | Hook the reader, set up the chapter's motivating question | First section of every chapter. Establishes what this chapter delivers and why the reader should care. | 1–2 pages |
| **Conceptual** | Introduce ideas, history, analogies, or definitions | Narrative flow through ideas. No repeating template. May include origin stories, analogies, or intellectual context. | 2–4 pages |
| **Argument** | Make a specific claim through logical steps | Step-by-step logical chain. Has a thesis, evidence, conclusion, and hedge. The reader should be persuaded, not just informed. | 2–3 pages |
| **Framework** | Teach a model with repeating parallel structure | N items, each getting the same structural treatment. The template repeats. Items are phases, patterns, categories, or principles. | 4–6 pages |
| **Method** | Teach a specific technique the reader will use | Definition → origin → when to use → process steps → worked problem → common mistakes. Pedagogical sequence. | 4–6 pages |
| **Case study** | Analyze an existing product/system through a lens | Setup → analysis through each dimension → synthesis. Retrospective — the product already exists. Analytical, not judgmental. | 4–7 pages |
| **Worked example** | Walk through building/designing something step by step | Setup → step 1 → step 2 → ... → evaluation → reflection. Prospective — something is being created. Narrative of discovery. | 4–6 pages |
| **Closer** | Synthesize the chapter, connect forward | Artifact inventory → capability statement → forward connection. Short, reflective, no new content. | 1–2 pages |
| **Review Questions** | Assess the reader's understanding at multiple cognitive levels | Comprehension → Application → Synthesis (Bloom's taxonomy). Derived from learning objectives. | 1 page |

### Classification Decision Tree

```
Is this the first section of the chapter?
  YES → Opener
  NO ↓

Is this the review questions section?
  YES → Review Questions
  NO ↓

Is this the last section of the chapter (excluding review questions)?
  YES → Does it introduce new concepts or methods?
    YES → Classify by content (probably not a Closer)
    NO → Closer
  NO ↓

Does the section teach a specific, named technique the reader will apply?
  (empathy maps, affinity diagrams, service contracts, etc.)
  YES → Method
  NO ↓

Does the section analyze an existing product/system through a framework?
  YES → Case study
  NO ↓

Does the section walk through creating/designing something step by step?
  YES → Worked example
  NO ↓

Does the section present N items with the same structural treatment?
  (five phases, four patterns, three methodologies compared, etc.)
  YES → Framework
  NO ↓

Does the section make a specific claim and argue for it with evidence?
  YES → Argument
  NO ↓

Default → Conceptual
```

---

## Step 2: Draft Approach by Type

Each type has a specific draft approach — a template for producing the section notes + section outline pair. The drafter reads the inputs (chapter outline section entry, chapter notes, prior sections) and produces both artifacts.

### Common Base for All Section Notes

Every section notes file includes these fields, regardless of type:

```yaml
---
section_type: [opener|conceptual|argument|framework|method|case_study|worked_example|closer]
blend: [secondary type, if applicable]
has_exercise: [true|false]
---
```

- **Entry state:** What the reader knows when they arrive. Prerequisites satisfied, concepts available, vocabulary established.
- **Exit state:** What the reader knows when they leave. New concepts, new vocabulary, new capabilities.
- **Transition in:** How this section connects from the previous section. What the handoff looks like.
- **Transition out:** How this section hands off to the next section.
- **Engagement risk:** Where might the reader disengage? What prevents it?
- **Voice notes:** Any section-specific tone considerations. Defaults to chapter-level voice unless noted.

Type-specific notes templates add fields beyond this base.

### Section Outline Level of Detail

Each structural block in the section outline specifies:

- **Purpose** — What this block accomplishes for the reader (1 sentence).
- **Key points** — The specific claims, ideas, or information in this block (bulleted list).
- **Specific examples** — Named, not just described. "The Herbert Simon quote from Sciences of the Artificial" not "a quote about design."
- **Paragraph count** — Approximate number of paragraphs.
- **Exercise spec** — If this block contains an exercise: exact prompt text, expected response characteristics, evaluation criteria.

The outline should be detailed enough that a drafter could produce prose from it without referring back to the chapter outline.

---

### Opener

**Purpose:** Hook the reader. Set up the chapter's central question. Establish what this chapter delivers and why it matters.

**Section notes template** (in addition to common base):
- **Hook strategy:** What specific, concrete experience opens the section? (Not abstract — a scenario, a question, a problem the reader recognizes.)
- **Promise:** What does this chapter deliver? State it explicitly.

**Section outline template:**
1. **Hook** (1–2 paragraphs) — A concrete scenario, question, or observation that the reader immediately recognizes from their own experience. Not abstract. Not "in today's world..."
2. **Expansion** (2–3 paragraphs) — Develop the hook into the chapter's motivating question. Name the problem. Make the reader feel it.
3. **Promise** (1 paragraph) — What this chapter delivers. What the reader will be able to do at the end that they cannot do now. Be specific.
4. **Scope** (1 paragraph, if needed) — What this chapter does NOT cover. Prevent misaligned expectations.
5. **Handoff** (1 paragraph) — Transition to the next section. The handoff should feel like a natural next step, not a topic change.

---

### Conceptual

**Purpose:** Introduce ideas, history, analogies, or definitions that provide intellectual foundation.

**Section notes template** (in addition to common base):
- **Core ideas:** List the ideas this section introduces. For each: what is it, why does the reader need it, how does it connect to the chapter's argument?
- **Concrete anchors:** For each abstract idea, what concrete example makes it tangible?
- **Decisions:** Which examples to use, which analogies, what depth of historical treatment, what to defer.

**Section outline template:**
1. **Orienting statement** (1 paragraph) — What question this section answers. Why the reader needs these ideas.
2. **Idea 1** (2–4 paragraphs) — Introduce, define, illustrate with a concrete example, connect to the chapter's larger argument.
3. **Idea 2** (2–4 paragraphs) — Same structure. Transition from idea 1 should feel earned.
4. *[Repeat for additional ideas]*
5. **Convergence** (1–2 paragraphs) — How the ideas connect. What the reader sees now that they couldn't see before.
6. **Handoff** (1 paragraph) — Transition to the next section.

---

### Argument

**Purpose:** Make a specific claim through logical steps. Earn the conclusion — don't assert it.

**Section notes template** (in addition to common base):
- **Thesis:** The claim, stated plainly.
- **Steps:** The logical chain. Each step should be independently defensible.
- **Evidence:** What supports each step? (Citation, example, callback to prior material.)
- **Hedge:** Where is the argument weakest? What counterarguments exist? How are they addressed honestly?

**Section outline template:**
1. **Setup** (1–2 paragraphs) — The question the argument answers. Why it matters. What the reader currently believes.
2. **Step 1** (1–2 paragraphs) — First move of the argument. Evidence or analysis.
3. **Step 2** (1–2 paragraphs) — Builds on step 1.
4. *[Repeat for additional steps]*
5. **Conclusion** (1 paragraph) — The claim, now earned. Stated as a result of the argument, not as an assertion.
6. **Hedge** (1–2 paragraphs) — What the argument does NOT claim. Limitations. Counterarguments addressed honestly. This section earns trust.
7. **Handoff** (1 paragraph) — Transition.

---

### Framework

**Purpose:** Teach a model or set of concepts with repeating parallel structure. Each item gets the same treatment.

**Section notes template** (in addition to common base):
- **Item list:** The N items to be covered. Their ordering rationale.
- **Item template:** The repeating structure each item receives. Define this template for THIS section — the outline then applies it N times. The template is section-specific because different frameworks need different treatment. Examples:
  - Section 1.3 (five phases): {input, output, methods, done-when, risk of skipping, in-practice example}
  - Section 2.6 (AI considerations): {what it is, design implication for define, design implication for test}
  - Section 6.7 (resilience patterns): {empathy question, behavioral specification, design consideration}
- **Distinctness check:** For each pair of items — how are they different? Could the reader confuse any two?
- **Overview/synthesis plan:** How to introduce the framework before the items and synthesize after.
- **Word budget per item:** Total page budget ÷ N items + overhead for overview and synthesis.

**Section outline template:**
1. **Overview** (1–2 paragraphs) — The framework as a whole. What it contains. The organizing principle. A visual if applicable.
2. **Item 1** — Apply the item template:
   - Definition / what it is
   - Purpose / what it does
   - Example / what it looks like in practice
   - Risks / what happens when it's skipped or done badly
   - *[Any other template fields]*
3. **Item 2** — Same template.
4. *[Repeat for all items]*
5. **Synthesis** (1–2 paragraphs) — What connects the items. The pattern the reader should see across them. How the framework operates as a whole, not just as parts.
6. **Handoff** (1 paragraph) — Transition.

---

### Method

**Purpose:** Teach a specific, named technique the reader will use. The reader should be able to apply the method independently after reading this section.

**Section notes template** (in addition to common base):
- **Method definition:** Formal, precise. The reader should be able to look this up.
- **Origin/attribution:** Where this method comes from. Intellectual pedigree.
- **When to use / when not to use:** Both are necessary. Methods have scope.
- **Process steps:** The method's steps, in order. Each step has a clear input and output.
- **Worked problem plan:** What example demonstrates the method? How does it connect to the chapter's running example?
- **Common mistakes:** The 2–3 most likely failure modes when applying this method.

**Section outline template:**
1. **Framing** (1 paragraph) — What problem this method solves. Why the reader needs it now.
2. **Definition** (1–2 paragraphs) — Formal definition. Origin and attribution.
3. **When to use** (1 paragraph) — Scope. When this method helps.
4. **When it fails** (1 paragraph) — Anti-patterns. Cargo-cult applications. What the method looks like when done badly.
5. **Process** (2–4 paragraphs) — Step-by-step. Each step has an input, an action, and an output.
6. **Worked problem** (1–3 paragraphs) — The method applied to the chapter's running example. The reader sees the method producing a real artifact.
7. **Common mistakes** (1 paragraph) — The 2–3 things to watch for.
8. **Handoff** (1 paragraph) — Transition. Usually to the next method, or to the exercise.

---

### Case Study

**Purpose:** Analyze an existing product or system through the chapter's framework. Demonstrate the framework's analytical power. Retrospective.

**Section notes template** (in addition to common base):
- **Subject selection rationale:** Why this product/system? What makes it a good case?
- **Analysis dimensions:** What aspects of the framework are applied? (All phases? Specific lenses? Specific failure modes?)
- **Key findings:** What does the analysis reveal? What is the central insight?
- **Fairness commitment:** The analysis is analytical, not judgmental. What caveats are needed?
- **Evidence basis:** What is known publicly vs. what is inferred? Where is attribution needed?

**Section outline template:**
1. **Setup** (1–2 paragraphs) — Introduce the subject. What the reader already knows about it. Frame the analysis: "we're going to use [framework] to see what [subject] reveals about [topic]."
2. **Caveats** (1 paragraph) — What we know and don't know. Public evidence vs. inference. Analytical, not judgmental.
3. **Analysis dimension 1** (2–3 paragraphs) — Apply the framework to the first dimension. Finding. Evidence.
4. **Analysis dimension 2** (2–3 paragraphs) — Same structure.
5. *[Repeat for additional dimensions]*
6. **Synthesis** (1–2 paragraphs) — What the analysis reveals as a whole. The central insight. What the reader can now see that they couldn't before.
7. **Handoff** (1 paragraph) — Transition. Usually: "you've seen the framework applied — now [learn to apply it yourself / see another angle / etc.]."

---

### Worked Example

**Purpose:** Walk through building or designing something step by step. Prospective — something is being created. Narrative of discovery.

**Section notes template** (in addition to common base):
- **Scenario:** What is being built/designed? Why this scenario?
- **Process steps:** Which phases/methods are demonstrated? In what order?
- **Discovery moments:** Where do things not go as expected? (These must feel genuine, not planted.)
- **What the reader should notice:** The explicit pedagogical payoff at each step.
- **Scope boundary:** What is demonstrated vs. what is left to the reader? What is simplified for the worked example that would be more complex in practice?

**Section outline template:**
1. **Setup** (1–2 paragraphs) — The scenario. What is being built. What makes it a good demonstration. Frame as "we're going to walk through [process] for [scenario]."
2. **Step 1** (2–3 paragraphs) — First phase/method applied. What goes in, what comes out. What the reader should notice about the process.
3. **Step 2** (2–3 paragraphs) — Builds on step 1's output. Transition should feel natural.
4. *[Repeat for all steps]*
5. **Evaluation** (1–2 paragraphs) — How the result is assessed. What works, what doesn't. Discovery of gaps.
6. **Reflection** (1–2 paragraphs) — What the worked example demonstrated about the methodology. What transfers beyond this specific scenario.
7. **Handoff** (1 paragraph) — Transition.

---

### Closer

**Purpose:** Synthesize the chapter. State what the reader can now do. Connect forward.

**Section notes template** (in addition to common base):
- **Artifact inventory:** What did the reader produce or learn in this chapter?
- **Capability statement:** What can the reader do now that they couldn't before? (Must match what was actually taught — no overclaiming.)
- **Forward connection:** What comes next? Why should the reader continue?

**Section outline template:**
1. **Artifact inventory** (1–2 paragraphs) — What the reader has produced or learned. Concrete, not abstract. Name the artifacts.
2. **Capability statement** (1 paragraph) — "You can now [specific thing]." This is the chapter's payoff, stated directly.
3. **Caveat** (1 paragraph, if needed) — What this capability does not yet include. Honest about scope.
4. **Forward connection** (1 paragraph) — What the next chapter delivers. Frame as motivation: the reader should want to continue.

---

### Review Questions

**Purpose:** Assess the reader's understanding at multiple cognitive levels. Derived from the chapter's learning objectives.

**Section notes template** (in addition to common base):
- **Learning objectives:** List all chapter learning objectives (from chapter outline frontmatter).
- **Coverage map:** For each learning objective, which question(s) test it?
- **Bloom's level assignments:** For each question, which Bloom's level does it target? (Comprehension, Application, or Synthesis.)
- **Difficulty calibration:** Are the questions at a similar difficulty level to review questions in other chapters?

**Section outline template:**
1. **Comprehension** (2–3 questions) — Recall and define. "Define X and describe its components." "Distinguish between X and Y." The reader can answer these from the text directly.
2. **Application** (2–3 questions) — Apply concepts to a new scenario. "A team is designing X. They skip Y. What specific risks does this create?" The reader must transfer concepts to a novel situation.
3. **Synthesis** (1–2 questions) — Combine concepts, argue, evaluate. "Construct an argument for X. Then identify a situation where X might fail." The reader must integrate ideas and think critically.

Each question specifies:
- The learning objective(s) it tests
- The Bloom's level
- What a strong answer includes (not a rubric, but guidance for the drafter on what the question should elicit)

---

## Step 3: Lens Sets by Type

Each section type has its own lens set. Lenses are applied sequentially (pass 1, then pass 2) per the process defined in `writing-process.md`.

### Lens Ordering Principle

**Risk-first: correctness → completeness → structure → polish.**

In pass 1, each lens modifies the artifact before the next lens sees it. Fix the most damaging problems first so downstream lenses work on a better artifact. The ordering within each type's lens set follows this progression:

1. **Correctness** — Is the right reader arriving? Is the content accurate? Are claims defensible? (Entry/exit alignment, Technical accuracy, Fairness)
2. **Completeness** — Is everything that should be here present? Is anything missing? (Completeness, Example quality, Exercise completeness)
3. **Structure** — Is it organized well? Does it flow? (Internal flow, Consistency of treatment, Concrete/abstract balance)
4. **Polish** — Is it expressed well? Does it fit? (Word budget, Transition quality, Voice and pacing, Cross-section coherence)

Pass 2 mitigates ordering effects — lenses that ran late in pass 1 (whose modifications weren't reviewed by early lenses) now get reviewed by all lenses.

### Universal Lens Preamble

Before the type-specific lens set runs, every section receives a universal preamble of four lenses. These run first in both pass 1 and pass 2, then the type-specific lenses follow.

```
Universal preamble (4 lenses) → Type-specific lenses (N lenses)
├──────── pass 1 ────────────────────────────────────────────┤
Universal preamble (4 lenses) → Type-specific lenses (N lenses)
├──────── pass 2 ────────────────────────────────────────────┤
```

| # | Universal lens | What it checks |
|---|---------------|----------------|
| U1 | Entry/exit alignment | Does the reader arrive with what they need? Do they leave with what the next section expects? |
| U2 | Technical accuracy | Are facts, definitions, attributions, and claims correct? |
| U3 | Word budget discipline | Is the section's content achievable within its word budget? |
| U4 | Cross-section coherence | Do terms, examples, and references align with other sections in this chapter and book? |

These four lenses are NOT repeated in the type-specific tables below. Every section receives U1–U4 plus its type-specific lenses.

### Type-Specific Lens Sets

#### Opener

*Plus universal preamble (U1–U4). Total: 4 + 6 = 10 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Hook effectiveness | Does the opening grab attention within the first paragraph? Is it concrete, not abstract? | Correctness |
| 2 | Promise clarity | Does the reader know what this chapter delivers? Is the promise specific and honest? | Completeness |
| 3 | Internal flow | Does every sentence earn the next? No wasted motion. | Structure |
| 4 | Concrete/abstract balance | Are abstract claims grounded in concrete scenarios the reader recognizes? | Structure |
| 5 | Transition quality | Does the handoff to the first substantive section feel natural? | Polish |
| 6 | Voice and pacing | Does this section set the right tone for the chapter? The opener establishes voice. | Polish |

#### Conceptual

*Plus universal preamble (U1–U4). Total: 4 + 7 = 11 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Intellectual honesty | Are claims properly attributed? Are limitations acknowledged? | Correctness |
| 2 | Credibility building | Does this section earn the reader's trust? Authoritative without being dogmatic? | Correctness |
| 3 | Example quality | Are examples specific, well-chosen, and non-distracting? | Completeness |
| 4 | Concrete/abstract balance | Does every abstract idea get a concrete example within the section? | Completeness |
| 5 | Internal flow | Do ideas build on each other? Is the sequence logical? | Structure |
| 6 | Transition quality | Smooth handoff? | Polish |
| 7 | Voice and pacing | Professor who finds this interesting — not a textbook reciting dates? | Polish |

#### Argument

*Plus universal preamble (U1–U4). Total: 4 + 7 = 11 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Logical completeness | Does the argument earn its conclusion? Are any steps missing or weak? | Correctness |
| 2 | Counterargument awareness | Has the argument anticipated the reader's likely objections? | Correctness |
| 3 | Hedge quality | Are limitations acknowledged honestly, not dismissively? Does the hedge strengthen the argument? | Completeness |
| 4 | Concrete/abstract balance | Is each step grounded in evidence or example? | Completeness |
| 5 | Internal flow | Does each step follow from the previous? Is the chain unbroken? | Structure |
| 6 | Transition quality | Does the conclusion feed the next section? | Polish |
| 7 | Voice and pacing | Persuasive but not polemical. Analytical, not dismissive of alternatives. | Polish |

#### Framework

*Plus universal preamble (U1–U4). Total: 4 + 8 = 12 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Completeness | Does the framework cover the space? Are items missing? | Correctness |
| 2 | Distinctness | Is each item clearly distinct from the others? Could the reader confuse any two? | Correctness |
| 3 | Consistency of treatment | Does each item get the same structural treatment? Same depth? Same template? | Completeness |
| 4 | Example quality | Does each item have a clear, distinct example? Are examples parallel in scope? | Completeness |
| 5 | Internal flow | Is the ordering logical? Does each item earn the next? | Structure |
| 6 | Concrete/abstract balance | Every abstract item gets a concrete example. | Structure |
| 7 | Transition quality | Handoff to next section? | Polish |
| 8 | Voice and pacing | Repetitive structure risks monotony. Where does pacing vary? | Polish |

#### Method

*Plus universal preamble (U1–U4). Total: 4 + 8 = 12 lenses per pass. Add Exercise completeness (conditional) if section has an exercise.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Reproducibility | Could the reader follow the method independently from this description alone? | Correctness |
| 2 | Common mistake coverage | Are the likely failure modes identified and explained? | Correctness |
| 3 | Worked problem quality | Does the worked problem demonstrate the method's *value*, not just its steps? | Completeness |
| 4 | Example quality | Are examples specific, concrete, and well-chosen? | Completeness |
| 5 | Internal flow | Does the pedagogical sequence (define → demonstrate → apply) hold? | Structure |
| 6 | Concrete/abstract balance | Methods must be concrete. Is every step grounded? | Structure |
| 7 | Transition quality | Handoff? | Polish |
| 8 | Voice and pacing | Instructional without being condescending. Concrete and direct. | Polish |

#### Case Study

*Plus universal preamble (U1–U4). Total: 4 + 6 = 10 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Fairness of analysis | Is the analysis balanced? Not straw-manning or cheerleading? Are caveats present? | Correctness |
| 2 | Framework demonstration | Does the case study demonstrate the framework's analytical power? Could the reader see these things without the framework? | Completeness |
| 3 | Insight yield | Does the analysis reveal something non-obvious? Does the reader see something they couldn't see before? | Completeness |
| 4 | Internal flow | Does the analysis build cumulatively? Does each dimension deepen the picture? | Structure |
| 5 | Transition quality | Does the synthesis connect back to the chapter? Handoff? | Polish |
| 6 | Voice and pacing | Analytical, not judgmental. "This is what the lens reveals" not "they should have done better." | Polish |

#### Worked Example

*Plus universal preamble (U1–U4). Total: 4 + 6 = 10 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Process correspondence | Does each step follow from the methodology taught earlier in the chapter/book? | Correctness |
| 2 | Gap authenticity | When gaps/failures are discovered, do they feel genuine, not planted? | Correctness |
| 3 | Scope boundary clarity | Is it clear what is demonstrated vs. simplified vs. deferred? | Completeness |
| 4 | Internal flow | Does each step follow from the previous? Is the process legible? | Structure |
| 5 | Discovery tone | Does the narrative feel like the reader is discovering, not being told? | Polish |
| 6 | Transition quality | Does the reflection connect to the chapter? Handoff? | Polish |

#### Closer

*Plus universal preamble (U1–U4). Total: 4 + 4 = 8 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Capability assertion accuracy | Does the "what you can now do" statement match what was actually taught? No overclaiming. | Correctness |
| 2 | Forward connection quality | Does the next-chapter preview create motivation without spoiling? | Completeness |
| 3 | Internal flow | Reflective, not repetitive. Synthesizes, doesn't re-summarize. | Structure |
| 4 | Voice and pacing | Reflective. Earned. | Polish |

#### Review Questions

*Plus universal preamble (U1–U4). Total: 4 + 5 = 9 lenses per pass.*

| # | Lens | What it checks | Phase |
|---|------|----------------|-------|
| 1 | Learning objective coverage | Does every chapter learning objective have at least one question? Are any objectives untested? | Correctness |
| 2 | Answerability | Can each question be answered from the chapter content alone? No hidden prerequisites. | Correctness |
| 3 | Difficulty progression | Do questions progress from comprehension to application to synthesis (Bloom's taxonomy)? | Completeness |
| 4 | Question quality | Are questions unambiguous, appropriately scoped, and non-trivial? | Structure |
| 5 | Cross-chapter calibration | Is the difficulty level consistent with review questions in other chapters? | Polish |

### Conditional Lens: Exercise Completeness

When a section contains an exercise (`has_exercise: true` in section notes), add this lens to the type's lens set regardless of type. Insert it after the type's content-focused lenses, before Word budget discipline.

| Lens | What it checks |
|------|----------------|
| Exercise completeness | Is the exercise prompt clear and unambiguous? Is the scope appropriate (not too large, not trivial)? Are evaluation criteria defined or implied? Does the exercise practice the skill taught in this section, not a different skill? Does the difficulty match the reader's current capability? |

Exercises appear across all types except Closer. The lens is conditional because not every section of a given type contains an exercise.

---

## Handling Blended Sections

Some sections blend two types. Examples:
- 3.2 is **Method** with a **Worked example** embedded (worked problem within the method teaching)
- 6.4 is **Method** with implementation details
- 1.5 is **Framework** (parallel comparison of methodologies) with **Argument** elements (misapplications, when to abbreviate)

**Rule:** Classify by the dominant structure. Add supplementary lenses from the secondary type. No cap on supplementary lenses, but each must be justified.

**Process:**
1. Classify by primary type.
2. Identify the secondary type (if any).
3. Use the primary type's draft approach and full lens set.
4. Add type-specific lenses from the secondary type that address concerns not already covered by the primary set. For each supplementary lens, state in the section notes why it is needed — what concern does it address that the primary set misses?
5. Record the blend in the section notes frontmatter (`blend: [secondary type]`).

**Example:** Section 1.5 (DT in Context) is primarily **Framework** (three methodologies compared in parallel structure) with **Argument** elements (misapplications, when to abbreviate).
- Universal preamble: 4 lenses
- Primary lens set: Framework (8 lenses)
- Supplementary from Argument:
  - Logical completeness — needed because the misapplications subsection makes claims that must earn their conclusions
  - Hedge quality — needed because the "when to abbreviate" subsection must acknowledge limitations honestly
  - Counterargument awareness — needed because comparing DT to other methodologies invites reader objections
- Total: 4 + 8 + 3 = 15 lenses per pass

---

## Chapter 1 Classification

Applying the classification to textbook chapter 1 as validation:

| Section | Type | Lens count (U + T) | Rationale |
|---------|------|---------------------|-----------|
| 1.1 The Skill That Survives | **Opener** | 4 + 6 = 10 | First section. Sets up the motivating question. |
| 1.2 Two Traditions | **Conceptual** | 4 + 7 = 11 | Introduces historical ideas (intellectual + operational traditions). Narrative flow, not repeating template. |
| 1.3 The Five-Phase Cycle | **Framework** | 4 + 8 = 12 | Five phases, each getting the same structural treatment (input, output, methods, done-when, risk). |
| 1.4 ChatGPT Through the DT Lens | **Case study** | 4 + 6 = 10 | Retrospective analysis of ChatGPT through the five-phase framework. |
| 1.5 DT in Context | **Framework** + **Argument** | 4 + 8 + 3 = 15 | Adjacent methodologies compared in parallel structure. Misapplications subsection has argument characteristics. Supplementary: Logical completeness, Hedge quality, Counterargument awareness. |
| Review Questions | **Review Questions** | 4 + 5 = 9 | Comprehension, Application, Synthesis questions derived from learning objectives. |
