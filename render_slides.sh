#!/bin/bash
# Render both HTML and RevealJS versions of slides

FILE=$1

if [ -z "$FILE" ]; then
    echo "Usage: ./render_slides.sh <path-to-qmd-file>"
    exit 1
fi

echo "Rendering HTML version..."
quarto render "$FILE" --to html

echo "Rendering RevealJS version..."
quarto render "$FILE" --to revealjs

echo "Done! Both versions rendered."
