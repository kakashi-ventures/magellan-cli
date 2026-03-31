#!/bin/bash
# Generates MAGELLAN-Methodology-v5.pdf from methodology.html
# Requires: prince (https://www.princexml.com/)
#
# Fonts (not committed — run this once to download):
#   cd docs/pdf && mkdir -p fonts && cd fonts
#   for f in instrument-serif source-serif-4 jetbrains-mono caveat; do
#     curl -sL "https://gwfh.mranftl.com/api/fonts/$f?download=zip&subsets=latin&variants=regular,600,700" -o "$f.zip"
#     unzip -qo "$f.zip" && rm "$f.zip"
#   done
#   rm -f *.eot *.svg *.woff  # keep only .woff2 and .ttf

cd "$(dirname "$0")"

if [ ! -d fonts ] || [ -z "$(ls fonts/*.woff2 2>/dev/null)" ]; then
  echo "Fonts not found. Downloading from Google Fonts..."
  mkdir -p fonts && cd fonts
  for f in instrument-serif source-serif-4 jetbrains-mono caveat; do
    curl -sL "https://gwfh.mranftl.com/api/fonts/$f?download=zip&subsets=latin&variants=regular,600,700" -o "$f.zip"
    unzip -qo "$f.zip" 2>/dev/null && rm -f "$f.zip"
  done
  rm -f *.eot *.svg *.woff
  cd ..
  echo "Fonts downloaded."
fi

prince methodology.html -o ../MAGELLAN-Methodology-v5.pdf \
  --pdf-title="MAGELLAN — Methodology v5" \
  --pdf-author="Alberto Trivero • Kakashi Venture Accelerator" \
  --pdf-subject="Multi-Agent Scientific Discovery" \
  --pdf-creator="MAGELLAN" \
  --no-artificial-fonts \
  && echo "PDF generated: docs/MAGELLAN-Methodology-v5.pdf"
