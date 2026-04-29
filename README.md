# PDF Translator — Claude Code Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Translate academic/scholarly PDFs into side-by-side bilingual HTML documents
(English ↔ Chinese), preserving the original paper structure, all figures,
tables, equations, and nomenclature.

## Quick Start

1. **Install the skill in Claude Code:**

   Add to your `~/.claude/settings.json` or project `.claude/settings.json`:

   ```json
   {
     "plugins": [
       "github:KimTentap/pdf-translator"
     ]
   }
   ```

   Or install via CLI:
   ```bash
   claude plugins install github:KimTentap/pdf-translator
   ```

2. **Install Python dependencies:**

   ```bash
   pip3 install pdfplumber pymupdf
   ```

3. **Run the skill:**

   In Claude Code:
   ```
   /pdf-translate
   ```

   Or with a specific file:
   ```
   /pdf-translate path/to/paper.pdf
   ```

## What You Get

```
your-directory/
├── paper_translation.html   ← Open in any browser
└── pdf_images/              ← All figures from the PDF
```

The HTML features:
- **Two-column layout** — English (left) / Chinese (right)
- **All figures** — Extracted and placed in their original context
- **Bilingual tables** and figure captions
- **Equations** preserved inline
- **Print-friendly** styling

## Example

| Original PDF | Generated HTML |
|:---:|:---:|
| 12-page academic paper | Bilingual side-by-side pages |

![example](docs/example.png)

## Manual Script Usage

The Python extraction scripts work standalone:

```bash
# Extract all text from PDF
python3 scripts/extract_text.py paper.pdf --json > text.json

# Extract all embedded images
python3 scripts/extract_images.py paper.pdf ./images
```

## Tech Stack

| Component | Tool |
|-----------|------|
| PDF text extraction | [pdfplumber](https://github.com/jsvine/pdfplumber) |
| Image extraction | [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF) |
| Translation | Claude (via Claude Code) |
| Output format | HTML5 + CSS3 |

## Contributing

Bug reports and PRs welcome. Areas for improvement:
- Support for more language pairs
- LaTeX equation rendering (MathJax)
- DOCX output format
- Figure description translation for screen readers

## License

MIT © 2025
