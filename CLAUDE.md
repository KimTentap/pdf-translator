# PDF Translator Plugin for Claude Code

A Claude Code skill that translates academic/scholarly PDFs into
side-by-side bilingual HTML documents (English ↔ Chinese), preserving
the original paper structure, all figures, tables, and equations.

## Quick Start

```bash
# 1. Install the plugin
claude plugins install git@github.com:USER/pdf-translator.git

# 2. Drop a PDF in your working directory
cp ~/Downloads/paper.pdf .

# 3. Run the skill
/pdf-translate
```

## What it does

Given an academic PDF, this skill:
1. Extracts all text (via pdfplumber) and embedded images (via pymupdf)
2. Translates the content using Claude's built-in translation capabilities
3. Generates a print-ready HTML file with two-column bilingual layout
4. Preserves the original paper structure: title page, abstract, sections,
   figures, tables, equations, nomenclature, and references

## Generated output

```
working-directory/
├── paper_translation.html   ← open in any browser
└── pdf_images/              ← extracted figures (referenced by HTML)
```

## Features

- **Two-column comparison** — English on the left, Chinese on the right
- **Figure preservation** — All embedded images extracted and placed in context
- **Bilingual tables** — Table headers show both English and Chinese
- **Equation preservation** — Display equations rendered in the flow
- **Nomenclature grid** — Symbols with bilingual descriptions
- **Print-friendly** — `@media print` styles for paper output
- **Responsive** — Works on desktop and tablet screens

## Requirements

- Claude Code
- Python 3.8+
- Python packages: `pdfplumber`, `pymupdf`

## Structure

```
pdf-translator/
├── CLAUDE.md                    # Plugin manifest
├── README.md                    # This file
├── skills/
│   └── pdf-translate.md         # Skill definition (workflow instructions)
├── scripts/
│   ├── extract_text.py          # Extracts text from PDF pages
│   ├── extract_images.py        # Extracts embedded images from PDF
│   └── requirements.txt         # Python dependencies
└── template/
    └── base.css                 # Standard CSS styles for the output HTML
```

## Manual usage (without Claude Code)

The Python scripts can also be used standalone:

```bash
# Extract text
python3 scripts/extract_text.py paper.pdf

# Extract images
python3 scripts/extract_images.py paper.pdf ./pdf_images
```

Then use any LLM to translate the text and generate HTML following the
CSS classes defined in `template/base.css`.

## License

MIT
