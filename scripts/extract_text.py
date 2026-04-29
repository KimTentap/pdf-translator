#!/usr/bin/env python3
"""Extract full text from each page of a PDF using pdfplumber."""

import sys
import json
import pdfplumber


def extract_text(pdf_path: str) -> dict:
    """Return {page_num: text} for all pages in the PDF."""
    pages_text = {}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            pages_text[i + 1] = text if text else ""
    return pages_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_text.py <pdf_path> [--json]", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    as_json = "--json" in sys.argv
    result = extract_text(path)

    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for pn, text in result.items():
            print(f"\n{'='*60}")
            print(f"PAGE {pn}")
            print(f"{'='*60}")
            print(text)
