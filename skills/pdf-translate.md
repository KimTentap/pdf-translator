---
name: pdf-translate
description: Translate an academic/scholarly PDF into side-by-side bilingual HTML (English + Chinese). Extracts text and images from the PDF, translates all content while preserving the original structure, and generates a print-ready HTML file with two-column comparison layout.
version: 1.0.0
author: Claude Code Plugin
tags: [pdf, translation, academic, bilingual, html]
---

# PDF Translate — 中英对照学术论文翻译

Translate an academic PDF into a side-by-side bilingual HTML document
(English original | Chinese translation), preserving the original paper
structure, all figures, tables, equations, and nomenclature.

## Prerequisites

Before starting, ensure the Python dependencies are available:

```bash
pip3 install pdfplumber pymupdf
```

If `pymupdf` fails, try:
```bash
pip3 install pymupdf --no-cache-dir
```

---

## Workflow

Perform these steps in order.

### Step 1 — Discover the PDF

The user will provide a PDF path or there will be one in the working directory.
Run `ls *.pdf` to find it. If there are multiple, ask the user which one.

Store the PDF path as `$PDF`.

### Step 2 — Extract text from all pages

```bash
python3 scripts/extract_text.py "$PDF" > /tmp/pdf_text.txt
```

Read `/tmp/pdf_text.txt` to get the full text content. Note:
- Page boundaries are marked with `==== PAGE N ====`
- Some PDFs extract text with missing spaces; mentally rejoin words
- Math symbols may appear garbled (e.g., `(cid:2)` = ×, `(cid:3)` = °C, `(cid:4)` = −)

### Step 3 — Extract all images

```bash
python3 scripts/extract_images.py "$PDF" ./pdf_images
```

This creates the `pdf_images/` directory next to the output HTML.
Note the page number for each image (encoded in the filename: `page{N}_img{M}.ext`).

### Step 4 — Plan the translation structure

Skim the extracted text to identify:
1. **Paper sections** — Title, Abstract, Nomenclature, Introduction (I, II, III...), Conclusion, References
2. **Figures** — Where each figure appears (by page number) and its caption
3. **Tables** — Their content and location
4. **Equations** — Numbered equations that need to be preserved

### Step 5 — Generate the bilingual HTML

Create a single HTML file at `./paper_translation.html`.

**CRITICAL LAYOUT RULES:**
- Use `<div class="page">` to simulate PDF pages
- Each section uses `<div class="bilingual">` → two columns:
  - `<div class="col-en">` (English, left)  
  - `<div class="col-zh">` (Chinese, right)
- All CSS is embedded in `<style>` (reference `template/base.css` for the standard styles)
- Images use relative paths: `<img src="pdf_images/pageN_imgM.ext">`
- Figures are wrapped in `<div class="figure-container">` with bilingual captions
- Tables use `<table class="data-table">` with bilingual headers (English / Chinese)
- Equations are centered in `<div class="equation">`

**TRANSLATION RULES:**
- Translate ALL text content to Chinese — abstracts, body text, figure captions, table content, nomenclature descriptions
- Preserve ALL English original text in the left column
- Keep proper nouns consistent: technical terms, author names, journal names
- For references: translate titles into Chinese but keep author names and journal info bilingual
- Use proper Chinese technical terminology:
  - exergy → 㶲
  - parabolic trough → 抛物槽式
  - double reheat → 二次再热
  - feedwater heater → 给水加热器
  - superheated steam → 过热蒸汽
  - extraction steam → 抽汽
  - aperture area → 集热面积

**CSS CLASS REFERENCE:**

| Class | Purpose |
|-------|---------|
| `.page` | Simulated printed page |
| `.bilingual` | 2-column grid container |
| `.col-en` / `.col-zh` | English / Chinese columns |
| `.col-label` | Column header ("English" / "中文") |
| `.section-title` | Section heading |
| `.section-title-zh` | Chinese section sub-heading |
| `.figure-container` | Figure wrapper |
| `.figure-caption` | Figure caption (EN) |
| `.figure-caption-zh` | Figure caption (ZH) |
| `.figure-row` | Side-by-side figures |
| `.data-table` | Data table |
| `.nomen-grid` | Nomenclature grid |
| `.equation` | Display equation |
| `.highlight-box` | Callout / key point box |
| `.abstract-label` | Abstract heading |
| `.page-header` | Page top journal info |

**IMAGE PLACEMENT:**
- Match images to the page where they appear in the extracted text
- The filename pattern `page{N}_img{M}` tells you the original page number
- Place images at the same logical position within the bilingual flow

### Step 6 — Verify the output

- Check that all extracted images are referenced in the HTML
- Verify the HTML file can be opened in a browser (`open paper_translation.html`)
- Confirm the two-column layout renders correctly

---

## Example

Input: `Energy and exergy evaluations of solar-aided double reheat coal-fired power generation system.pdf`

Output: `paper_translation.html` + `pdf_images/`

This produces a 12-page equivalent HTML with:
- Title page with journal info
- Abstract (bilingual)
- Nomenclature table (symbol + description in both languages)
- Sections I–V with full bilingual translation
- 10 figures with bilingual captions
- Tables II and III with bilingual headers
- References with translated titles
