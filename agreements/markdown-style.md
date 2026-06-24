# Markdown Style Guide

## Heading Levels

- `##` — Section number (e.g., `## 1.1 Setup`). One per section file.
- `###` — Major subsections (e.g., `### Claude Code`, `### Build the Project`). The primary structural unit within a section.
- `####` — Minor subsections. Use liberally for scannability. Any time a `###` subsection covers two or more distinct topics, break them into `####` headings.

Use headings to create breathing room. If a reader would skim past a wall of prose to find the part they need, that prose needs a heading to break it up.

## Blockquotes (`>`)

Reserved exclusively for Claude Code prompts the reader types. Nothing else uses blockquotes.

```markdown
> "Initialize a Python project with uv. The project is called task-agent."
```

## Bold Labels

- `**Listing 1.X**` — Before code blocks (install commands, scripts, configuration). Numbered per chapter: `1.1`, `1.2`, etc.
- `**Figure 1.X**` — Before tree outputs, diagrams, and SVG references. Numbered per chapter.
- `**Table 1.X**` — Before tables. Numbered per chapter.
- `**IMPORTANT**` — Callouts that the reader must not skip. Bold label on its own line, followed by the text as a regular paragraph. Not a blockquote.
- `⊹ **Checkpoint**` — Self-check moments where the reader verifies understanding. Framed as questions, not instructions. The reader should be able to answer from what they just built. Bulleted list of questions. Not a to-do list.

```markdown
**IMPORTANT**

Claude Code is generative, not deterministic. It will not produce
identical output every time you run it.
```

## Horizontal Rules (`---`)

Do not use, except for blocks that take the reader out of the main flow. These get `---` before and after. Currently three types:

- `⊹ **Checkpoint**` — Self-check moments. Questions, not instructions.
- `⛭ **Setup**` — External service configuration (API keys, accounts, installs). Steps to complete before continuing.
- `**Core Pattern: [Name]**` — Named, reusable architectural pattern introduced at the start of a chapter. Bold label, then bolded field labels (**Problem:**, **Pattern:**, **This chapter:**, **Forward:**), each on its own line as a plain paragraph.

## Claude Code Interaction Pattern (Pro book)

Every Claude Code prompt gets a label line, the prompt in a blockquote, and evaluation guidance.

### Prompt Label

`❯ **Prompt Claude:** Short description of what to do (Role)`

The label goes on its own line before the blockquote. Role is one of Designer, Operator, Debugger, or Researcher. The description is a short phrase, not a full sentence.

### Full Pattern

Four elements appear for each Claude Code prompt:

1. **The label** — `❯ **Prompt Claude:**` with description and role
2. **The prompt** — blockquote with the reader's words
3. **"Claude Code should:"** — bulleted list of expected tool calls / actions
4. **"What matters is..."** — prose sentence(s) stating what the reader should check. Not a formal requirements checklist; a judgment call the reader learns to make.

Operator prompts (run this command) may omit the "Claude Code should:" and "What matters is..." elements when the expected behavior is obvious.

```markdown
❯ **Prompt Claude:** Initialize the project (Designer)

> "Initialize a Python project with uv..."

Claude Code should:

- Run `uv init` to create the project with a `src/` layout
- Run `uv add` to install runtime dependencies

What matters is that `pyproject.toml` lists `anthropic` and `pydantic`
as dependencies and the directory structure uses `src/task_agent/`.
```

## Code Blocks

Every code block must have a `**Listing X.Y**` label. No exceptions. If it contains code, a shell command, or an install instruction, it gets a listing number.

- ` ```bash ``` ` — Shell commands the reader or Claude Code runs
- ` ```python ``` ` — Python source code
- ` ``` ``` ` (no language) — Tree output, plain text, non-code content

### Line Width

All code listings must be 80 characters wide or less. No exceptions. This ensures readability in print, ebook, and code editor contexts. When a line exceeds 80 characters:

- Break long strings across multiple lines
- Use intermediate variables to shorten expressions
- Break long function signatures with one parameter per line
- Break long dictionary literals with one key per line

## Links

All web references must be working markdown links: `[display text](https://url)`. Never use bare URLs or unlinked domain names in prose. If you mention a website, link it.

## Prose Conventions

### Paragraphs

Target 75-125 words. Hard ceiling of 150 words; split at a natural seam. Minimum 50 words; merge up or leave as a deliberate one-liner. See `agreements/paragraph-sizing.md` for split heuristics.

### Em-dashes

No em-dashes (—) or double-hyphens-as-em-dashes (` -- `). Replace with commas, colons, semicolons, periods, or parentheses depending on function. See `agreements/emdash-purge.md` for replacement rules.

### Vocabulary Boldface

Boldface a term at its introduction point only. Subsequent uses are plain text. Preserve original casing. Do not boldface in headings, exercises, or blockquotes. Do not boldface proper nouns or external methodology names. See `agreements/vocabulary-capitalization.md` for full rules.

## Designer / Operator / Debugger (Pro book)

Three roles the reader plays when working with Claude Code. These are not Claude Code features or modes; they describe what the reader is doing.

- **Designer** — The reader describes intent ("create a task manager that..."). Claude Code decides the implementation. Designer prompts should be specific about *what*, not *how*.
- **Operator** — The reader gives a specific command ("run uv run python src/task_agent/agent.py"). Claude Code executes it. Operator prompts should be specific about *exactly what to run*.
- **Debugger** — Something broke. The reader describes the problem ("that failed, fix it"). Claude Code diagnoses the cause and proposes a fix. The reader stays in the session and lets Claude Code use its context.
- **Researcher** — The reader asks Claude Code to find information ("what is the latest model version?"). Claude Code searches, reads, or fetches. The reader evaluates the result and decides what to do with it.

Introduce designer and operator in section 1.1. Introduce debugger in the same section (troubleshooting). Use the vocabulary consistently throughout both Pro chapters.

## Style Pass Checklist

Apply this checklist when editing any Pro book section:

1. **Listing numbers**: Every code block gets `**Listing X.Y**`. No exceptions.
2. **Figure numbers**: Every tree output or diagram gets `**Figure X.Y**`.
3. **Working links**: All URLs become `[text](url)` markdown links. No bare URLs.
4. **Blockquotes**: Reserved for Claude Code prompts only. Move callouts to `**IMPORTANT**` format.
5. **Claude Code interaction pattern**: Each prompt gets "Claude Code should:" list + "What matters is..." prose.
6. **`####` headings**: Use liberally for scannability within `###` subsections.
7. **Designer/operator/debugger/researcher**: Use vocabulary consistently. Designer prompts describe intent. Operator prompts give specific commands. Debugger prompts describe failures. Researcher prompts ask Claude Code to find information.
8. **Paragraph sizing**: 75-125 word target, 150 ceiling, 50 minimum.
9. **Em-dash purge**: No `—` or ` -- `. Replace per rules in `agreements/emdash-purge.md`.
10. **Vocabulary boldface**: Bold at introduction only, plain text after. Per `agreements/vocabulary-capitalization.md`.
11. **No horizontal rules**: Use headings for visual separation.
12. **Listing continuity**: Numbering is sequential across sections within a chapter (1.1 starts at Listing 1.1, 1.2 continues from where 1.1 left off, etc.).
13. **Line width**: All code listings are 80 characters wide or less. No exceptions.

## Things This Guide Does Not Cover

- Voice and tone (handled by lens passes)
- Content structure and pedagogy (handled by `agreements/writing-process.md`)
- Section-level planning (handled by section notes + outlines)
