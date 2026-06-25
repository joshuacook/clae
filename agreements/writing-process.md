---
title: "Writing Process"
type: process
status: active
created: "2026-03-08"
updated: "2026-03-08"
---

# Writing Process

## Artifact Classes

Seven classes of artifact, produced in sequence. Each class feeds the next.

1. **Book Outline** — one per book. The whole structure.
2. **Part Notes** — per part (optional). The *why* at part scale: how the part's chapters hang together, thematic arc, key decisions spanning multiple chapters. Not always produced; most useful for books with strong part-level structure.
3. **Chapter Notes** — per chapter. Working decisions, project choices, narrative arc, code plan. The *why*.
4. **Chapter Outline** — per chapter. Detailed section structure, content plan. The *what*.
5. **Section Notes** — per section. Decisions specific to this section, examples, transitions, pedagogical intent. The *why* at section scale.
6. **Section Outline** — per section. Paragraph-level structure, specific examples detailed, exercise specs, exact key term definitions. The *what* at section scale.
7. **Chapter Draft** — per chapter. Actual manuscript prose.

Chapter notes and chapter outlines are co-produced — you can't outline the structure without making decisions, and the decisions shape the structure. They are drafted together, reviewed together, and passed through lenses together as a pair.

Section notes and section outlines are also co-produced pairs, following the same logic at section scale.

### Optional: Pre-Section Working Documents

Between chapter-level and section-level artifacts, working notes and outlines may accumulate at chapter scope before formal per-section pairs are produced. These are **optional** — they are not required by the process and do not go through lens passes. They serve as a staging area for section-level thinking.

- **Pre-section notes** — chapter-scoped working notes containing section-level content (entry/exit states, scope decisions, engagement risks, tone notes) before it has been split into formal per-section artifacts.
- **Pre-section outlines** — chapter-scoped working outlines containing section-level structure before formal per-section outline pairs are produced.

These live in `chapter_notes/` and `chapter_outlines/` with a `-presection` suffix:

```
chapter_notes/hmm-chapter-1-the-trait-trap-presection.md
chapter_outlines/hmm-chapter-1-the-trait-trap-presection.md
```

When formal per-section pairs are produced, content from the pre-section documents feeds them and the pre-section documents are retired (deleted or archived).

## The Sequential Lens Process

Every artifact class goes through the same process:

1. **Draft** — produce the artifact (or artifact pair, for notes + outline)
2. **Lens pass 1** — the artifact passes through each lens reviewer in sequence. Each lens receives the artifact, reviews through its specific perspective, modifies, and passes to the next lens. The artifact accumulates modifications as it moves through the sequence.
3. **Lens pass 2** — same lenses, same sequence, same process. The second pass reduces the importance of order — modifications made by late lenses in pass 1 get reviewed by early lenses in pass 2.

```
Artifact
  draft → L1 → L2 → L3 → ... → LN → L1 → L2 → ... → LN → final
          ├─────── pass 1 ──────────┤  ├─────── pass 2 ──────────┤
```

Each lens is a reviewer. It reads through its specific perspective, makes changes to the artifact, and hands off to the next lens. The artifact is the living document — it changes as it moves.

## Production Flow

```
BOOK OUTLINE
  draft → lens passes
           │
           ▼
    ┌──────────────────────────────────────────────────────────┐
    │  per chapter                                             │
    │                                                          │
    │  CHAPTER NOTES + OUTLINE (co-produced pair)              │
    │    draft → lens passes                                   │
    │               │                                          │
    │               ▼                                          │
    │    ┌────────────────────────────────────────────┐        │
    │    │  per section (sequential within chapter)   │        │
    │    │                                            │        │
    │    │  SECTION NOTES + OUTLINE (co-produced pair)│        │
    │    │    draft → lens passes                     │        │
    │    │    (each section needs prior sections)     │        │
    │    └────────────────────────────────────────────┘        │
    │               │                                          │
    │               ▼                                          │
    │         CHAPTER DRAFT                                    │
    │           draft → lens passes → style gate 1             │
    │                                      │                   │
    │                                      ▼                   │
    │                              DIAGRAM PASS                │
    │                                      │                   │
    │                                      ▼                   │
    │                              AUTHOR REVIEW               │
    │                                      │                   │
    │                                      ▼                   │
    │                              POST-REVIEW LENS PASS       │
    │                              (whole-chapter scope)        │
    │                                      │                   │
    │                                      ▼                   │
    │                              STYLE GATE 2                │
    │                                      │                   │
    │                                      ▼                   │
    │                              BUILD VALIDATION            │
    │                              (claude -p replay)           │
    │                                      │                   │
    │                                      ▼                   │
    │                              PDF RENDERING               │
    └──────────────────────────────────────────────────────────┘
```

## Source Assembly (CLAE source-first modification)

CLAE is source-heavy (course lessons, case studies, project-1, and the prior-work
repos in `~/working/clae-refs/`). For this book, a **Source Assembly** phase runs
per chapter *before* the chapter notes+outline, so the chapter outline is built
from an understanding of the source rather than top-down.

For each chapter, in order:

1. **Gather** — collect every source for the chapter. `source/coverage-by-chapter.md`
   is the index of where to look (lessons, case studies, datasets, repo chapters).
   Pull clean source only; never copy `assessments/` student submissions (PII).
2. **Organize against the outline** — map each source fragment to the chapter's
   book-outline sections: what it provides (derivation, code, figure, worked
   example, dataset) and a reuse verdict (adapt / rewrite / net-new).
3. **Assess** — note quality, redundancies, conflicts, and gaps (sections with no
   source are genuinely scratch).
4. **Build the chapter outline from the map** — validate and adjust the section
   structure against what the source actually supports. The book outline's section
   breakdown is provisional for strong chapters and may be reshaped here.

Output: a chapter source map, `chapter_notes/clae-chapter-NN-source-map.md`, with a
section-to-source table and a short gaps-and-conflicts note. It feeds the chapter
notes+outline.

Modified dependency: **book outline + chapter source map → chapter notes+outline**.

## Dependency Rules

### Chapter-level dependencies
Chapter notes+outlines are produced **sequentially across the writing order**. Each chapter receives all prior chapters' completed notes+outlines as context, along with the book outline.

### Section-level dependencies
Section notes+outlines are **sequential within a chapter** — section N needs sections 1 through N-1 as context. But sections in different chapters can be produced **in parallel**, since all chapter-level artifacts are already complete.

### What feeds what
- Book outline → chapter notes+outline
- Chapter notes+outline (all prior chapters) → next chapter's notes+outline
- Chapter notes+outline (this chapter) + book outline → section notes+outlines for this chapter
- Section notes+outlines (all sections in this chapter) → chapter draft

## Section Notes + Outline: What They Contain

### Section Notes
- **Decisions** specific to this section: which examples to use, what analogies, what to cut or defer
- **Entry state:** what the reader knows when they arrive at this section
- **Exit state:** what the reader should know when they leave
- **Transitions:** how this section connects to the previous and next sections
- **Pedagogical intent:** what this section teaches and how (definition, example, exercise, synthesis)
- **Engagement strategy:** where the reader might disengage and how to prevent it
- **Voice notes:** any section-specific tone considerations

### Section Outline
- **Paragraph-level structure:** the sequence of ideas at sub-section or paragraph granularity
- **Specific examples:** fully detailed, not just named — what the example shows, how it's presented, what it demonstrates
- **Exercise specifications** (if this section contains an exercise): exact prompt, expected response characteristics, evaluation criteria
- **Key terms:** exact definitions as they'll appear in the prose
- **Code examples** (Pro book): described concretely — what the code does, what the reader sees, what they learn from it
- **Figures/diagrams:** described if this section needs visual elements
- **Word budget:** estimated word count for this section (derived from the chapter's page budget)

## File Organization

Section-level files are stored alongside chapter-level files with a section suffix:

```
chapter_notes/
  textbook-chapter-2-dt-applied-to-ai.md                    # chapter-level
  textbook-chapter-2-dt-applied-to-ai--s01-ai-dev-problem.md  # section 2.1
  textbook-chapter-2-dt-applied-to-ai--s02-pm-analogy.md      # section 2.2
  textbook-chapter-2-dt-applied-to-ai--s03-reframe.md         # section 2.3
  ...

chapter_outlines/
  textbook-chapter-2-dt-applied-to-ai.md                    # chapter-level
  textbook-chapter-2-dt-applied-to-ai--s01-ai-dev-problem.md  # section 2.1
  textbook-chapter-2-dt-applied-to-ai--s02-pm-analogy.md      # section 2.2
  ...
```

The `--sNN-slug` suffix identifies the section number and a short descriptive slug.

## Lens Sets

Each artifact class has its own lens set — the perspectives that matter differ by artifact type. Lenses are defined before production begins for each artifact class.

### Book Outline Lenses (established)

Used for the Pro Agentic AI outline and the textbook outline:

1. Pedagogical
2. Engagement
3. Storytelling
4. Market
5. Technical accuracy
6. Scope
7. Accessibility
8. Completeness
9. Voice
10. Competitive differentiation

### Chapter Notes + Outline Lenses (established)

1. Learning objectives alignment — every section serves an objective; every objective has a section
2. Narrative arc — does the chapter tell a coherent story from open to close? Does each section earn the next?
3. Pedagogical scaffolding — difficulty gradient, concept dependencies, prerequisites satisfied within or before the chapter
4. Exercise design — quality, placement, difficulty, coverage of objectives, formative value
5. Technical accuracy — are frameworks, citations, historical claims, and definitions correct?
6. Scope discipline — page budget realism, no creep into other chapters, no missing promised content
7. Case study rigor — fair analysis, well-supported claims, demonstrates the framework without straw-manning
8. Reader engagement — hooks, pacing, abstract-concrete balance, where might the reader disengage?
9. Cross-chapter coherence — sets up later chapters correctly, consistent terminology, no orphaned promises
10. Voice consistency — matches book's established voice, appropriate tone for artifact type

### Section Notes + Outline Lenses (established)

1. Entry/exit alignment — does the reader arrive with what they need? Do they leave with what the next section expects?
2. Internal flow — does the section tell a coherent micro-story? Does each paragraph earn the next?
3. Example quality — are examples specific, concrete, and well-chosen? Do they demonstrate the concept without distraction?
4. Exercise completeness — if this section contains an exercise, is the prompt clear, the scope appropriate, and the evaluation criteria defined?
5. Technical accuracy — are definitions, claims, code descriptions, and citations correct at the detail level?
6. Word budget discipline — is the section's content achievable within its word budget? What gets cut if it's over?
7. Transition quality — does the section connect smoothly to its neighbors? Is the handoff explicit, not assumed?
8. Concrete/abstract balance — does every abstract concept get a concrete example within the same section?
9. Cross-section coherence — do terms, examples, and references align with other sections in this chapter and with chapter-level decisions?
10. Voice and pacing — does the prose rhythm match the section's purpose (definition sections are precise, example sections are vivid, synthesis sections are reflective)?

### Chapter Draft Lenses (established)

1. Outline correspondence — does each section deliver what the chapter outline promised?
2. Code listing integrity — listings correct, numbered sequentially, all referenced in prose
3. Claude Code prompt quality — describe → evaluation criteria → reference listing pattern, mode labels on all prompts, specificity
4. Pedagogical sequence — concepts introduced before use, prerequisites satisfied, difficulty scaffolded
5. Core Pattern treatment — named, introduced early, threaded consistently through the chapter
6. Checkpoint completeness — every checkpoint has concrete, binary, verifiable questions
7. Figure and listing continuity — sequential numbering across sections, no gaps, all referenced in prose
8. Technical accuracy — API calls, SDK methods, package versions, shell commands correct
9. Narrative arc — coherent story across sections, each section earns the next, opening promise kept by close
10. Voice and pacing — direct and specific, pace matches section purpose (method sections are crisp, concept sections are precise, synthesis sections are reflective)

## Parallelization Strategy

Given completed chapter-level artifacts for all chapters in scope:

- **Within a chapter:** Sections are produced sequentially (section N depends on sections 1..N-1)
- **Across chapters:** Sections can be produced in parallel (one agent per chapter, each processing its sections sequentially)
- **Scale:** ~54 section-level pairs across 9 chapters (averaging 6 sections each). Up to 9 parallel agents, each running its chapter's sections sequentially.

## Diagram Pass

After lens passes and before author review, Claude reads each section and identifies concepts that benefit from visual reinforcement. For each candidate, Claude creates an SVG diagram in the chapter's `figures/` directory, adds a `**Figure X.Y**` reference in the prose, and adjusts listing/figure numbering as needed.

### What Gets a Diagram

- **Processes with multiple steps**: workflows, pipelines, loops (e.g., the agent loop, the tool-use loop, the human research process)
- **Comparisons**: side-by-side contrasts where spatial layout clarifies the difference (e.g., single-step vs. multi-step)
- **Architectures**: how components connect and data flows between them (e.g., messages.parse() pipeline)
- **State transitions**: how something changes over time or across iterations

### What Does Not Get a Diagram

- Concepts already clear from a code listing
- Simple enumerations (a list of five categories does not need a diagram)
- Anything that would just restate the prose in boxes

### Style

All diagrams use the same visual language established in Chapter 1: monospace font (`SF Mono`, `Fira Code`, `Consolas`), `#fafafa` background, colored boxes with rounded corners (`rx="8"`), muted palette (`#6378a8` blue, `#5a9e72` green, `#b8943e` amber, `#9a6aad` purple), dashed zone dividers, `#9ca3af` annotations. SVG format for vector quality.

### Process

1. Read each section looking for diagram candidates
2. Create SVGs in `chapter_drafts/pro-chapter-N/figures/`
3. Insert `**Figure X.Y**` references in the prose
4. Renumber listings and figures for continuity
5. Note any downstream renumbering needed in later sections

The diagram pass is proactive: Claude identifies candidates without waiting for author feedback. The author may request additional diagrams, remove ones that do not add value, or adjust placement during review.

## Author Review Phase

After the diagram pass, the chapter draft enters author review. This is a distinct phase with its own rhythm. The author reads sequentially and gives feedback. Claude edits in real time. The chapter improves through conversation.

### The Rhythm

The author reviews sections in order (1.1, 1.2, 1.3, ...). For each section:

1. **Author reads** the current draft
2. **Author gives feedback** as comments, concerns, or ideas (typically 2-6 items per section)
3. **Claude addresses each item** immediately: edits the file, creates a companion artifact, or proposes an alternative
4. **Author confirms or refines** until the section is done
5. **Move to the next section**

This is not a single pass. A section might get 3 rounds of feedback before the author says "done." But the progression through sections is sequential: finish 1.1 before starting 1.2.

### Types of Feedback

Author feedback falls into five categories. Each is handled differently.

**Structural.** Heading changes, section reorganization, subsection splits or merges. These change the skeleton of the section. Example: renaming "Wiring to the API" to "Connecting to `messages.parse()`" because "API" was ambiguous.

**Content.** Adding, removing, or reframing concepts. Threading a term through a section so a diagram lands better. Rewriting a subsection to reflect a different interaction pattern. Example: threading "constrained generation" through section 1.3 in four places before the diagram.

**Style.** Tone adjustments, formatting changes, prompt restructuring. Example: reformatting a Claude Code prompt from a run-on sentence to a bulleted list using shift-enter.

**Cross-cutting.** Concerns that affect all sections, not just the one under review. These are applied retroactively across the full chapter (or both chapters). Example: adding Designer/Operator/Debugger mode labels to every Claude Code prompt. Example: enforcing 80-character line width on all code listings.

**Companion artifacts.** New things created alongside the prose. SVG diagrams for key concepts. Website articles for "dig deeper" topics. Cross-book references to the textbook. Example: creating Figure 1.5 (messages.parse() pipeline) and deploying companion articles to joshuacook.net.

### Cross-Cutting Concerns

When a review comment on section N reveals a pattern that should apply everywhere, apply it immediately across all sections. Do not wait until reviewing each section individually.

Process for cross-cutting concerns:

1. Author identifies the pattern (e.g., "every Claude Code prompt should have a mode label")
2. Audit all sections to find every instance
3. Apply the fix across all sections in one pass
4. If the pattern is durable, codify it in `agreements/markdown-style.md`

Cross-cutting concerns discovered during Chapter 1 review:

- **Mode labels**: Every Claude Code prompt gets a bold **(Designer)**, **(Operator)**, or **(Debugger)** label. Applied to all 31 prompts across both chapters.
- **80-character line width**: All code listings must be 80 characters wide or less. Added to `agreements/markdown-style.md` and fixed 30 violations across 9 files.
- **Claude Code interaction pattern**: Major build moments use the pattern: describe what to tell Claude Code, evaluation criteria ("Claude Code should:"), reference code listing. Codified in `agreements/markdown-style.md`.

### Style Rules Emerge From Review

Review comments often reveal implicit style rules. When a pattern appears:

1. Address it in the current section
2. Check if it applies broadly
3. If it does, add it to `agreements/markdown-style.md`
4. Apply retroactively to all existing sections

Style rules codified during Chapter 1 review: paragraph sizing, em-dash purge, vocabulary boldface, 80-character line width, Claude Code interaction pattern, mode labels, listing/figure continuity, "by the end" bookend.

### "By the End" Bookend Pattern

Every chapter introduction includes a "By the end of this chapter, you will..." paragraph listing concrete, verifiable outcomes ("you have a working CLI task manager" not "you understand agents"). The closing section of the chapter revisits this list item by item, confirming each promise was fulfilled: "We said we would X. You did X in section 1.N." This is an explicit accountability check, not a vague summary. If a promised outcome was not delivered, it surfaces here.

### Companion Artifacts

Three types of companion artifacts are produced during review:

**SVG diagrams.** Created when a concept needs visual reinforcement. Stored in `chapter_drafts/pro-chapter-N/figures/`. Referenced with `**Figure X.Y**` labels. Examples: agent loop, iterative cycle, messages.parse() pipeline, tool-use loop.

**Website articles.** Written for "dig deeper" topics that deserve more space than the book allows. Stored in `section_drafts/website-*.md` during drafting, then deployed to joshuacook.net. Referenced as inline links in the prose. Examples: system prompts, uv, designer/operator/debugger, agent loop, Pydantic models, prototyping, CRUD tools.

**Cross-book references.** When the Pro book and textbook intersect, add references in both directions. Example: Pro book 1.3's rapid iteration connects to textbook Chapter 4's prototype fidelity spectrum. Added a paragraph in the Pro book and a cross-reference in the textbook chapter notes.

### Continuity Maintenance

Throughout review, maintain:

- **Listing numbers**: Sequential across sections within a chapter. When a section adds or removes a listing, renumber downstream sections.
- **Figure numbers**: Same rule as listings.
- **Forward/back references**: When content changes, verify that all cross-references still point to the right thing.
- **Term threading**: When a new term is introduced, verify it appears at its introduction point in bold and in plain text thereafter.

### Chapter 1 Review Summary

The Chapter 1 review produced these changes:

| Section | Edit scope | Key changes |
|---------|-----------|-------------|
| 1.1 | Major rewrite | Expanded Claude Code introduction, Designer/Operator/Debugger roles, project setup via Claude Code |
| 1.2 | Moderate | "Your Code Will Not Match the Listing" teaching moment, experienced engineer mindset shift, SVG diagrams |
| 1.3 | Major | "Constrained generation" threaded throughout, Schema Design rewritten as prototyping, Figure 1.5, DT cross-reference |
| 1.4 | Moderate | CRUD pattern connection, Claude Code reminder, Figure 1.6 |
| 1.5 | Light | Mode labels, Chapter 9 forward reference for test cost optimization |

Cross-cutting: mode labels on all 31 prompts, 80-char enforcement on all listings, 7 website articles written, 4 SVG diagrams created.

## Post-Review Lens Pass

After author review, the chapter goes through one final lens pass at **whole-chapter scope**. This is not section-by-section. The lenses read the entire chapter as a single document and check for coherence problems that author review may have introduced.

Author review changes things at different scales: threading terms, adding diagrams, restructuring subsections, applying cross-cutting fixes. Each change is locally correct but may break chapter-level coherence. The post-review pass catches these.

### Why This Pass Is Necessary

Pre-review lens passes operate on individual sections before the author has seen them. Author review then modifies those sections based on feedback. Some modifications are surgical (rename a heading). Others are structural (rewrite a subsection as a different interaction pattern, thread a term through four locations). The chapter that emerges from review is not the same chapter that went into it. It needs a coherence check.

### Post-Review Lens Set

One pass through all eight lenses. Each lens reads the full chapter.

| # | Lens | What it checks |
|---|------|----------------|
| 1 | Narrative arc | Does the chapter still tell one coherent story from open to close? Do sections earn each other in sequence? |
| 2 | Voice consistency | After multiple editing sessions with different focuses, does the chapter read like one author wrote it in one sitting? |
| 3 | Term consistency | Are introduced terms used consistently throughout? Bold at introduction, plain text after. No term introduced in one section and used differently in another. |
| 4 | Listing/figure continuity | Are numbers sequential across sections? Do all labels match content? Are there gaps or duplicates? |
| 5 | Cross-reference integrity | Do forward/back references still point to the right things? Do website links match the prose around them? Do chapter/section references reflect current content? |
| 6 | Scope discipline | Did author review add too much? Does each section still stay in its lane, or did feedback push content into the wrong section? |
| 7 | Transition quality | Do section boundaries still work after edits? Does the end of each section hand off naturally to the next? |
| 8 | Style compliance | Do all sections comply with every rule in `agreements/markdown-style.md`? The full checklist, applied uniformly. |

### Process

```
Full chapter (all sections concatenated)
  │
  ▼
L1 → L2 → L3 → L4 → L5 → L6 → L7 → L8 → final chapter
├──────────── single pass, whole-chapter scope ────────────┤
```

One pass is sufficient. The pre-review process runs two passes to mitigate ordering effects across 10+ lenses. The post-review set has eight lenses and operates on a chapter that has already been through multiple rounds of review. A single pass catches coherence issues without over-polishing.

## Build Validation (`claude -p`)

After the post-review lens pass, validate that the chapter's Claude Code prompts produce working code by replaying them in a fresh project directory using `claude -p` (pipe mode).

### Why This Step Exists

The book's instructions are its product. If a reader follows the prompts in order and the resulting code does not work, the chapter is broken regardless of how well the prose reads. Build validation is an end-to-end smoke test of the chapter's build sequence.

### Process

1. Create a fresh temporary directory (simulating a reader starting from scratch)
2. Extract the Claude Code prompts from the chapter in order (every blockquote)
3. Feed each prompt to `claude -p` sequentially, maintaining session context
4. After each prompt, verify the output meets the "Claude Code should:" criteria
5. At each checkpoint, run the verification command (e.g., `uv run pytest tests/ -v`)
6. Report any failures: which prompt produced unexpected results, what diverged from the reference listings

### Command Pattern

```bash
# Create a fresh project directory
mkdir /tmp/chapter-N-validation && cd /tmp/chapter-N-validation

# Feed prompts sequentially
echo "Initialize a Python project with uv..." | claude -p
echo "Create a function called agent..." | claude -p --continue
echo "Update the agent function to use..." | claude -p --continue
# ... each prompt from the chapter in order

# At checkpoints, verify
uv run python src/task_agent/agent.py
uv run pytest tests/ -v
```

### What to Check

- **Project structure**: Does `tree` output match the expected figures?
- **Code runs**: Do the operator commands (`uv run python ...`) execute without errors?
- **Tests pass**: Does `uv run pytest tests/ -v` pass at the end?
- **Behavioral correctness**: Does the agent categorize, prioritize, and persist tasks as described?

### When Validation Fails

A validation failure means one of three things:

1. **The prompt is underspecified.** Claude Code produces something different from what the book expects. Fix the prompt to be more precise.
2. **The reference listing is wrong.** The code in the book does not match what a well-specified prompt produces. Update the listing.
3. **The criteria are wrong.** The "Claude Code should:" list does not match what Claude Code actually does. Update the criteria.

In all three cases, the fix is in the chapter content, not in Claude Code. The validation step catches these before the reader does.

## PDF Rendering

After build validation, render the chapter as a PDF for review and sharing.

### Process

1. Convert SVG figures to PDF format using `rsvg-convert` (vector-to-vector, no quality loss)
2. Concatenate all section files in order (intro, 1.1, 1.2, ..., 1.N)
3. Swap `.svg` references to `.pdf` in the markdown stream
4. Render with pandoc using xelatex (required for Unicode support in tree diagrams)

### Command

```bash
# Convert SVGs to PDF (one-time per figure)
cd chapter_drafts/pro-chapter-N/figures
for f in *.svg; do
    rsvg-convert -f pdf -o "${f%.svg}.pdf" "$f"
done

# Render the chapter
cd chapter_drafts/pro-chapter-N
cat intro.md 1.1-*.md 1.2-*.md ... | \
    sed 's/\.svg)/.pdf)/g' | \
    pandoc -f markdown -o chapter-N.pdf \
        --pdf-engine=xelatex \
        -V geometry:margin=1in \
        -V fontsize=11pt \
        -V documentclass=article \
        --highlight-style=tango \
        -V colorlinks=true \
        -V mainfont="Helvetica" \
        -V monofont="Menlo" \
        --metadata title="Chapter N: Title"
```

### Requirements

- `pandoc` (installed via Homebrew or package manager)
- `xelatex` (from a TeX distribution like MacTeX or TeX Live)
- `rsvg-convert` (from `librsvg`, installed via `brew install librsvg`)

### Notes

- Use xelatex, not pdflatex. pdflatex cannot handle Unicode box-drawing characters (├, └, │) used in tree output figures.
- SVGs must be converted to PDF (not PNG) to preserve vector quality in the final output.
- The `sed` swap is applied to the markdown stream before pandoc sees it, so the source files are not modified.

## Applying the Process Across the Ecosystem

The process is the same for all four books. The lens sets may differ per book (the textbook's lenses may weight pedagogical rigor differently than the Pro book's), but the structure (draft, pass 1, pass 2, diagram pass, author review, post-review lens pass, build validation, PDF rendering) is invariant.
