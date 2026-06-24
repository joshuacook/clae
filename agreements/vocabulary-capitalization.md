# Vocabulary Boldface Skill

## Standard

When a term is introduced as a vocabulary/technical concept, boldface it at its introduction point. Subsequent uses remain plain text. The term keeps its natural casing — no added capitalization.

## What counts as an introduction

- "has a name: X" patterns
- "X is a [definition]" patterns
- "two modes: X or Y" patterns
- Dash-delimited definitions: "X -- [definition]"
- Colon-delimited definitions: "X: [definition]"
- Parenthetical definitions: "X (definition)"
- Terms given their own subsection or clearly being defined for the reader

## Process

1. **Discover:** Scan the target file(s) for terms introduced with definitional patterns (see above). Also check for terms already bolded. Compile a deduplicated vocabulary list.
2. **Report:** Present the vocabulary term list with file, line number, and introduction context. Flag any terms that are already bolded (no action needed) and any that are not yet bolded (action needed).
3. **Confirm:** Get user approval before making changes.
4. **Apply:** Boldface each unbolded introduction, preserving original casing.
5. **Verify:** Re-scan to confirm all introductions are bolded.

## Exclusions

- Do not boldface subsequent uses — only the introduction.
- Do not boldface terms in headings (already styled).
- Do not boldface terms inside exercises/blockquotes.
- Do not boldface proper nouns, external methodology names (Agile, Lean Startup, HCD), people, or organizations.
