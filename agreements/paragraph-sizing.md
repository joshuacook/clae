# Paragraph Sizing Skill

## Standard

- **Target range:** 75-125 words per paragraph
- **Hard ceiling:** 150 words — anything above gets split at a natural seam
- **Minimum:** 50 words — anything below gets merged up or is a deliberate one-liner (e.g., a single-sentence transition)

## Exclusions

These are NOT paragraphs for sizing purposes:
- Headings
- Blockquotes / exercises
- Numbered and bulleted lists
- Image references
- Code blocks
- Shell commands

## Process

1. **Analyze:** Count words and sentences for every qualifying paragraph in the target file(s). Identify all paragraphs over 150 words and any under 50 words.
2. **Report:** Show the distribution (buckets: 0-50, 51-100, 101-150, 151-200, 201-250, 251+) and list the specific paragraphs that need splitting or merging.
3. **Confirm:** Get user approval before making changes.
4. **Split:** For each over-150 paragraph, find the natural seam — typically one of:
   - A shift from concept introduction to application/example
   - A shift from general claim to specific evidence
   - A shift from enumeration setup to the enumeration itself
   - A transition from one sub-idea to another within the same topic
5. **Add transitions only when necessary.** Most splits need no added text — the seam is already there. Only add a transitional sentence when the split would feel abrupt without one.
6. **Verify:** Re-count to confirm all paragraphs are now within the 75-125 target range (150 hard ceiling).

## Split Heuristics

When choosing where to split a long paragraph:
- Prefer splitting after a period that ends a complete thought
- Prefer splitting before a sentence that introduces a new angle ("But," "The risk of," "This is also," "Three patterns...")
- Never split in the middle of an example or enumeration
- Never split a paragraph into two pieces that are both under 50 words
