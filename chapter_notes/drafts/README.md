# drafts/ — the CURRENT book (v12)

These six files ARE the current state of the book. Josh edits these
directly; version history lives in git and in each file's header
comment, not in the filenames.

- `preface.md` — preface (v12: transfer-centered)
- `ch01.md` — Ch 1, The Agreement (V8)
- `ch02.md` — Ch 2, the operator (V8)
- `ch03.md` — Ch 3, the machine (V4)
- `ch04.md` — Ch 4, eigen
- `ch05.md` — Ch 5, random vectors (V1)

`chapter_drafts/` at the repo root is the pre-v9 (tranche-1) state and
is replaced by these at finalization. Do not edit it.

Render: preprocess each file (mode preface|chapter), pandoc, postprocess;
mains + figures stage in the session scratchpad; build via Cloud Build.
