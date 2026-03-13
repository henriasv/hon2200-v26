#!/bin/bash
# Watch a Quarto slide file and auto-render both formats on save

FILE=$1

if [ -z "$FILE" ]; then
    echo "Usage: ./watch_slides.sh <path-to-qmd-file>"
    exit 1
fi

if ! command -v fswatch &> /dev/null; then
    echo "Error: fswatch not installed"
    echo "Install with: brew install fswatch"
    exit 1
fi

echo "Watching $FILE for changes..."
echo "Press Ctrl+C to stop"
echo ""

# Initial render
./render_slides.sh "$FILE"

# Watch for changes
fswatch -o "$FILE" | while read f; do
    echo "Change detected, re-rendering..."
    ./render_slides.sh "$FILE"
    echo "Done! $(date)"
    echo ""
done
