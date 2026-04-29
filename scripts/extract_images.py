#!/usr/bin/env python3
"""Extract all embedded images from a PDF using pymupdf (fitz)."""

import sys
import os
import fitz  # pymupdf


def extract_images(pdf_path: str, output_dir: str) -> list[dict]:
    """
    Extract all images from the PDF.
    Returns a list of {page, index, filename, path, bytes_len}.
    """
    os.makedirs(output_dir, exist_ok=True)
    records = []

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        for img_idx, img in enumerate(page.get_images()):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            filename = f"page{page_num+1}_img{img_idx+1}.{ext}"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(image_bytes)
            records.append({
                "page": page_num + 1,
                "index": img_idx + 1,
                "filename": filename,
                "path": filepath,
                "size": len(image_bytes),
            })
    doc.close()
    return records


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_images.py <pdf_path> [output_dir]", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "./pdf_images"
    records = extract_images(pdf_path, out_dir)

    for r in records:
        print(f"[Page {r['page']}] {r['filename']} ({r['size']} bytes)")
    print(f"\nTotal: {len(records)} images saved to {os.path.abspath(out_dir)}")
