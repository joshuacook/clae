#!/usr/bin/env bash
# Render the book in Springer dress (SNmono) via Cloud Build.
# Usage: tools/render/render.sh   (from the clae repo root)
# Needs: pandoc locally; SNmono.cls in ~/working/clae-private/springer-template/book/;
#        scribe gcloud config for the cooksfleet-apps Cloud Build submit.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
STAGE="${STAGE:-/tmp/clae-springer-stage}"
mkdir -p .render "$STAGE/render/figures/ch01" "$STAGE/render/figures/ch02"

clae-py tools/render/preprocess.py chapter_drafts/clae-chapter-00-preface/0-preface.md .render/preface.md .render/preface-figs.json preface
clae-py tools/render/preprocess.py chapter_drafts/clae-chapter-01/1-vectors-and-linear-combinations.md .render/ch01.md .render/ch01-figs.json chapter
clae-py tools/render/preprocess.py chapter_drafts/clae-chapter-02/2-matrices-and-linear-transformations.md .render/ch02.md .render/ch02-figs.json chapter
for f in preface ch01 ch02; do
  pandoc -f markdown+raw_tex -t latex --no-highlight --top-level-division=chapter .render/$f.md -o .render/$f.tex
done
clae-py tools/render/postprocess.py .render/preface.tex .render/preface-figs.json figures/ch00
clae-py tools/render/postprocess.py .render/ch01.tex .render/ch01-figs.json figures/ch01 --section-zero
clae-py tools/render/postprocess.py .render/ch02.tex .render/ch02-figs.json figures/ch02

cp .render/{preface,ch01,ch02}.tex tools/render/book.tex "$STAGE/render/"
cp ~/working/clae-private/springer-template/book/SNmono.cls "$STAGE/render/"
cp chapter_drafts/clae-chapter-01/figures/*.png "$STAGE/render/figures/ch01/"
cp chapter_drafts/clae-chapter-02/figures/*.png "$STAGE/render/figures/ch02/"
cp tools/render/cloudbuild.yaml "$STAGE/"

export CLOUDSDK_CONFIG="$HOME/.config/gcloud-proj/scribe"
(cd "$STAGE" && gcloud builds submit --config cloudbuild.yaml --project cooksfleet-apps \
  --service-account projects/cooksfleet-apps/serviceAccounts/scribe-sa@cooksfleet-apps.iam.gserviceaccount.com .)
gcloud storage cp gs://cooksfleet-apps_cloudbuild/clae-render/book.pdf /tmp/clae-springer-draft.pdf
echo "PDF: /tmp/clae-springer-draft.pdf"
