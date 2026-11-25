"""
doc_extract.py — Unified document text extraction + page viewer
Handles: PDF (text-based + scanned/OCR), DOCX, images
Dependencies: fitz (PyMuPDF), pytesseract, pdfplumber, python-docx, Pillow

Usage:
    python doc_extract.py <file_or_dir> [--pages 1-5] [--ocr] [--render] [--outdir DIR]

Modes:
    Default:    Try text extraction first (fast), fall back to OCR if low yield
    --ocr:      Force OCR on all pages
    --render:   Render pages as PNG images (for visual inspection)
    --pages:    Specify page range (e.g., "1-5", "1,3,7", "10-")

Output:
    <filename>_text.txt     — Extracted text (one file per input)
    <filename>_p001.png     — Rendered page images (if --render)
    <filename>_summary.txt  — Quick summary: page count, text/scan detection, key metadata
"""

import argparse
import fitz
import os
import re
import sys
import json
from pathlib import Path

TESSERACT_CMD = r"C:\Users\mokke\miniconda3\Library\bin\tesseract.exe"

# Minimum chars per page to consider "text-based" vs "scanned"
TEXT_THRESHOLD = 50


def parse_page_range(spec, total_pages):
    """Parse page range spec like '1-5', '1,3,7', '10-' into list of 0-based indices."""
    if not spec:
        return list(range(total_pages))
    
    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            parts = part.split("-", 1)
            start = int(parts[0]) - 1 if parts[0] else 0
            end = int(parts[1]) if parts[1] else total_pages
            pages.update(range(max(0, start), min(end, total_pages)))
        else:
            idx = int(part) - 1
            if 0 <= idx < total_pages:
                pages.add(idx)
    return sorted(pages)


def extract_text_pymupdf(filepath):
    """Extract text using PyMuPDF (fast, works for text-based PDFs)."""
    doc = fitz.open(filepath)
    results = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        results.append({
            "page": i + 1,
            "text": text,
            "char_count": len(text),
            "is_scanned": len(text) < TEXT_THRESHOLD
        })
    doc.close()
    return results


def extract_text_pdfplumber(filepath):
    """Extract text using pdfplumber (better for tables/layouts)."""
    import pdfplumber
    results = []
    with pdfplumber.open(filepath) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            tables = page.extract_tables() or []
            table_text = ""
            for table in tables:
                for row in table:
                    table_text += " | ".join(str(c or "") for c in row) + "\n"
            
            combined = text.strip()
            if table_text:
                combined += "\n\n[TABLES]\n" + table_text
            
            results.append({
                "page": i + 1,
                "text": combined,
                "char_count": len(combined),
                "has_tables": len(tables) > 0,
                "is_scanned": len(combined) < TEXT_THRESHOLD
            })
    return results


def ocr_page(filepath, page_idx, dpi=300):
    """OCR a single PDF page using Tesseract."""
    import pytesseract
    from PIL import Image
    import io
    
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
    
    doc = fitz.open(filepath)
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=dpi)
    img_data = pix.tobytes("png")
    doc.close()
    
    img = Image.open(io.BytesIO(img_data))
    text = pytesseract.image_to_string(img, lang="eng")
    return text.strip()


def ocr_image(filepath):
    """OCR a standalone image file."""
    import pytesseract
    from PIL import Image
    
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
    img = Image.open(filepath)
    text = pytesseract.image_to_string(img, lang="eng")
    return text.strip()


def extract_docx(filepath):
    """Extract text from a .docx file."""
    from docx import Document
    doc = Document(filepath)
    results = []
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    # Also extract tables
    table_text = []
    for table in doc.tables:
        for row in table.rows:
            row_text = " | ".join(cell.text for cell in row.cells)
            table_text.append(row_text)
    
    combined = "\n".join(full_text)
    if table_text:
        combined += "\n\n[TABLES]\n" + "\n".join(table_text)
    
    return [{
        "page": 1,
        "text": combined,
        "char_count": len(combined),
        "is_scanned": False
    }]


def render_pages(filepath, page_indices, outdir, dpi=200):
    """Render specified pages as PNG images."""
    doc = fitz.open(filepath)
    stem = Path(filepath).stem
    rendered = []
    for i in page_indices:
        if i >= len(doc):
            continue
        page = doc[i]
        pix = page.get_pixmap(dpi=dpi)
        outpath = os.path.join(outdir, f"{stem}_p{i+1:03d}.png")
        pix.save(outpath)
        rendered.append(outpath)
    doc.close()
    return rendered


def process_pdf(filepath, pages_spec=None, force_ocr=False, do_render=False, outdir=None):
    """Full PDF processing pipeline."""
    doc = fitz.open(filepath)
    total_pages = len(doc)
    doc.close()
    
    page_indices = parse_page_range(pages_spec, total_pages)
    stem = Path(filepath).stem
    
    if outdir is None:
        outdir = str(Path(filepath).parent)
    os.makedirs(outdir, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Processing: {Path(filepath).name}")
    print(f"Pages: {total_pages} total, processing {len(page_indices)}")
    print(f"{'='*60}")
    
    # Initialize results list
    results = [{"page": i+1, "text": "", "char_count": 0, "is_scanned": True} for i in range(total_pages)]
    
    # Step 1: Try text extraction first
    if not force_ocr:
        print("Phase 1: Text extraction (PyMuPDF)...", end=" ")
        results = extract_text_pymupdf(filepath)
        scanned_count = sum(1 for r in results if r["is_scanned"])
        text_count = total_pages - scanned_count
        print(f"{text_count} text pages, {scanned_count} scanned")
        
        # If mostly text, also try pdfplumber for better table extraction
        if scanned_count < total_pages * 0.5:
            print("Phase 1b: Table extraction (pdfplumber)...", end=" ")
            try:
                plumber_results = extract_text_pdfplumber(filepath)
                tables_found = sum(1 for r in plumber_results if r.get("has_tables"))
                print(f"{tables_found} pages with tables")
                
                # Merge: use pdfplumber text if it's longer (better extraction)
                for i in range(min(len(results), len(plumber_results))):
                    if plumber_results[i]["char_count"] > results[i]["char_count"]:
                        results[i]["text"] = plumber_results[i]["text"]
                        results[i]["char_count"] = plumber_results[i]["char_count"]
                        results[i]["is_scanned"] = plumber_results[i]["is_scanned"]
            except Exception as e:
                print(f"skipped ({e})")
        
        # If high scan ratio, auto-OCR
        if scanned_count > total_pages * 0.5:
            print(f"  → {scanned_count}/{total_pages} pages are scanned. Switching to OCR...")
            force_ocr = True
    
    # Step 2: OCR if needed
    if force_ocr:
        print(f"Phase 2: OCR (Tesseract 5.5) on {len(page_indices)} pages...")
        for idx in page_indices:
            if idx >= total_pages:
                continue
            # Skip if we already have good text for this page
            if not force_ocr and idx < len(results) and not results[idx]["is_scanned"]:
                continue
            
            print(f"  OCR page {idx+1}/{total_pages}...", end=" ", flush=True)
            try:
                text = ocr_page(filepath, idx)
                # Ensure results list is big enough
                while len(results) <= idx:
                    results.append({"page": len(results)+1, "text": "", "char_count": 0, "is_scanned": True})
                results[idx]["text"] = text
                results[idx]["char_count"] = len(text)
                results[idx]["is_scanned"] = False
                results[idx]["ocr"] = True
                print(f"{len(text)} chars")
            except Exception as e:
                print(f"ERROR: {e}")
    
    # Step 3: Render pages if requested
    rendered = []
    if do_render:
        print(f"Phase 3: Rendering {len(page_indices)} pages as PNG...")
        rendered = render_pages(filepath, page_indices, outdir)
        print(f"  → {len(rendered)} images saved")
    
    # Step 4: Write output
    # Filter to requested pages
    page_results = [results[i] for i in page_indices if i < len(results)]
    
    # Full text output
    text_outpath = os.path.join(outdir, f"{stem}_text.txt")
    with open(text_outpath, "w", encoding="utf-8") as f:
        for r in page_results:
            f.write(f"\n{'='*60}\n")
            f.write(f"PAGE {r['page']}")
            if r.get("ocr"):
                f.write(" [OCR]")
            f.write(f"\n{'='*60}\n\n")
            f.write(r["text"])
            f.write("\n")
    
    # Summary
    total_chars = sum(r["char_count"] for r in page_results)
    ocr_pages = sum(1 for r in page_results if r.get("ocr"))
    text_pages = sum(1 for r in page_results if not r["is_scanned"] and not r.get("ocr"))
    still_empty = sum(1 for r in page_results if r["char_count"] < TEXT_THRESHOLD)
    
    summary = {
        "file": Path(filepath).name,
        "total_pages": total_pages,
        "processed_pages": len(page_results),
        "text_extracted_pages": text_pages,
        "ocr_pages": ocr_pages,
        "low_content_pages": still_empty,
        "total_characters": total_chars,
        "avg_chars_per_page": total_chars // max(len(page_results), 1),
        "text_file": text_outpath,
        "rendered_pages": rendered
    }
    
    summary_path = os.path.join(outdir, f"{stem}_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nResults:")
    print(f"  Text: {text_outpath} ({total_chars:,} chars)")
    print(f"  Summary: {summary_path}")
    if rendered:
        print(f"  Images: {len(rendered)} PNGs in {outdir}")
    
    return summary


def process_image(filepath, outdir=None):
    """Process a standalone image file with OCR."""
    if outdir is None:
        outdir = str(Path(filepath).parent)
    
    stem = Path(filepath).stem
    print(f"\nOCR image: {Path(filepath).name}...", end=" ", flush=True)
    
    text = ocr_image(filepath)
    print(f"{len(text)} chars")
    
    text_outpath = os.path.join(outdir, f"{stem}_text.txt")
    with open(text_outpath, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"  → {text_outpath}")
    return {"file": Path(filepath).name, "chars": len(text), "text_file": text_outpath}


def process_file(filepath, **kwargs):
    """Route to appropriate processor based on extension."""
    ext = Path(filepath).suffix.lower()
    
    if ext == ".pdf":
        return process_pdf(filepath, **kwargs)
    elif ext == ".docx":
        results = extract_docx(filepath)
        outdir = kwargs.get("outdir") or str(Path(filepath).parent)
        stem = Path(filepath).stem
        text_outpath = os.path.join(outdir, f"{stem}_text.txt")
        with open(text_outpath, "w", encoding="utf-8") as f:
            f.write(results[0]["text"])
        print(f"DOCX: {Path(filepath).name} → {results[0]['char_count']:,} chars → {text_outpath}")
        return {"file": Path(filepath).name, "chars": results[0]["char_count"], "text_file": text_outpath}
    elif ext in (".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp"):
        return process_image(filepath, outdir=kwargs.get("outdir"))
    else:
        print(f"Unsupported format: {ext}")
        return None


def process_directory(dirpath, **kwargs):
    """Process all supported files in a directory."""
    supported = {".pdf", ".docx", ".png", ".jpg", ".jpeg", ".tiff", ".tif"}
    files = [f for f in Path(dirpath).iterdir() if f.suffix.lower() in supported]
    
    print(f"\nDirectory: {dirpath}")
    print(f"Found {len(files)} supported files")
    
    results = []
    for f in sorted(files):
        try:
            r = process_file(str(f), **kwargs)
            if r:
                results.append(r)
        except Exception as e:
            print(f"  ERROR processing {f.name}: {e}")
            results.append({"file": f.name, "error": str(e)})
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Extract text from PDFs, DOCX, and images")
    parser.add_argument("path", help="File or directory to process")
    parser.add_argument("--pages", help="Page range (e.g., '1-5', '1,3,7', '10-')")
    parser.add_argument("--ocr", action="store_true", help="Force OCR on all pages")
    parser.add_argument("--render", action="store_true", help="Render pages as PNG")
    parser.add_argument("--outdir", help="Output directory (default: same as input)")
    parser.add_argument("--dpi", type=int, default=200, help="DPI for rendering (default: 200)")
    
    args = parser.parse_args()
    
    target = args.path
    kwargs = {
        "pages_spec": args.pages,
        "force_ocr": args.ocr,
        "do_render": args.render,
        "outdir": args.outdir
    }
    
    if os.path.isdir(target):
        results = process_directory(target, **kwargs)
    elif os.path.isfile(target):
        results = process_file(target, **kwargs)
    else:
        print(f"Error: {target} not found")
        sys.exit(1)
    
    print("\n✓ Done")


if __name__ == "__main__":
    main()
