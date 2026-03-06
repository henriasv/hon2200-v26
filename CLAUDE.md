# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HON2200 is a university course website (UiO) built with Quarto. The course covers statistics/data skills (Part 1) and digital ethics (Part 2). All content is in Norwegian (bokmål). Python is used for code examples (pandas, numpy, matplotlib, scikit-learn).

## Build Commands

```bash
# Render entire site
quarto render

# Render a single file to slides
quarto render lectures/01b1_slides.qmd --to revealjs

# Preview a single file to slides
quarto preview lectures/01b1_slides.qmd --to revealjs

# Render a single file
quarto render lectures/01b1_slides.qmd

# Render slides (both HTML + RevealJS formats)
./render_slides.sh lectures/01b1_slides.qmd

# Auto-render slides on save (requires fswatch)
./watch_slides.sh lectures/01b1_slides.qmd

# Preview site locally
quarto preview
```

## Quarto Configuration

Three config files exist for different rendering scopes:
- `_quarto.yml` — **Primary/production config**. Only includes weeks currently visible to students. Weeks are progressively uncommented as the semester advances.
- `_quarto_development.yml` — Development config with more content visible.
- `_quarto-all.yml` — Full config including all weeks and materials.

Key execution settings in `_quarto.yml`: `freeze: auto` (cached output reused unless source changes), `error: true` (strict), `warning: false` (suppressed).

## Content Structure

Each week follows a naming pattern (`XX` = week number):
- `XXa_forberedelser.qmd` — Student preparation material
- `XXb_slides.qmd` — Lecture slides (dual format: HTML page with embedded RevealJS iframe)
- `XXb2_tutorial.qmd` or `XXb2_live.ipynb` — Optional tutorial/live coding
- `XXc_øvelse.qmd` — Exercises with toggleable solutions

Other directories:
- `lectures/llm/` — LLM-generated supplementary materials (clearly labeled as AI-generated)
- `lectures/data/` — Datasets used in lectures
- `oppgaver/` — Mandatory assignments and projects
- `endringslogg/` — SOTL-based change tracking for curriculum development

## Exercise Solution Toggle

Solutions are controlled via metadata in `_quarto.yml`:

```yaml
exercise_solutions:
  week_01: true   # Solutions visible
  week_04: false  # Solutions hidden
```

Exercise files use conditional blocks:
```markdown
:::: {.content-hidden unless-meta="exercise_solutions.week_01"}
::: {.callout-note collapse="true"}
### Løsningsforslag
...
:::
::::
```

## Slide Files

Slide `.qmd` files define both `html` and `revealjs` output formats. The HTML version embeds the RevealJS version via iframe. Use `{.content-hidden when-format="revealjs"}` to show the iframe only in the HTML version. Use `./render_slides.sh` to render both formats at once.

## Filters

- `remove-notes.lua` — Lua filter that strips instructor notes from student-facing output. Applied globally via `_quarto.yml`.

## Python Environment

Always use the local `.venv` in the project root. If it doesn't exist, create it. Do not use pyenv shims or global Python. Exercise and lecture `.qmd` files use `jupyter: python3` for executable code blocks.

## Progressive Content Release

The course releases content week by week. In `_quarto.yml`, future weeks are commented out in both the `render:` list and the `sidebar:` contents. To add a new week: uncomment the relevant entries in both sections and set the appropriate `exercise_solutions.week_XX` flag.

## TODO / Reminders

- **Midtveisevaluering**: Skal legges inn senere i semesteret (nettskjema: <https://nettskjema.no/a/504824>). Legg til lenke i en passende forberedelsesside når tidspunktet nærmer seg.
