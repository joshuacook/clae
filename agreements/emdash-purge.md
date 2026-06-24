# Em-Dash Purge Skill

## Standard

No em-dashes (—) in any chapter text. Replace with the appropriate alternative punctuation.

## Replacement Rules

1. **Parenthetical aside** → use commas or parentheses
   - "the system -- which was built last year -- failed" → "the system, which was built last year, failed"
2. **Appositive or clarification** → use a colon or comma
   - "one thing mattered -- accuracy" → "one thing mattered: accuracy"
3. **Contrast or pivot** → use a semicolon or period
   - "the test passed -- but barely" → "the test passed, but barely"
4. **List introduction** → use a colon
   - "three options -- red, green, blue" → "three options: red, green, blue"
5. **Double dashes used as em-dashes** (` -- `) → same rules apply

## Process

1. **Scan:** Search target file(s) for `—` (em-dash) and ` -- ` (double-hyphen-as-em-dash).
2. **Report:** List each instance with line number and surrounding context.
3. **Confirm:** Get user approval before making changes.
4. **Replace:** Apply the appropriate alternative punctuation per the rules above.
5. **Verify:** Re-scan to confirm no instances remain.

## Notes

- Preserve en-dashes (–) used in number ranges (e.g., "pages 1–5", "1--2 paragraphs" in exercises).
- Do not modify code blocks or shell commands.
