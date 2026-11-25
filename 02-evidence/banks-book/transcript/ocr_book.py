"""
OCR all book page screenshots into chapter-by-chapter markdown files.
Uses Tesseract 5.5 via pytesseract.
"""
import os
import re
import pytesseract
from PIL import Image

BOOK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ordered list of all page image files
def get_page_files():
    files = []
    # page_NNN.png files (pages 1-59ish)
    for f in sorted(os.listdir(BOOK_DIR)):
        if f.startswith("page_") and f.endswith(".png"):
            files.append(os.path.join(BOOK_DIR, f))
    # book_user_capture_NNN.png files (pages 60-140ish)
    for f in sorted(os.listdir(BOOK_DIR)):
        if f.startswith("book_user_capture_") and f.endswith(".png"):
            files.append(os.path.join(BOOK_DIR, f))
    return files

def ocr_image(path):
    """OCR a single image, return text."""
    img = Image.open(path)
    # Crop out Kindle chrome (top ~40px header, bottom ~50px progress bar)
    w, h = img.size
    # Crop top 45px and bottom 55px to remove Kindle UI
    crop_top = 45
    crop_bottom = 55
    img_cropped = img.crop((0, crop_top, w, h - crop_bottom))
    text = pytesseract.image_to_string(img_cropped, lang='eng',
        config='--psm 6 --oem 3')
    return text.strip()

def extract_page_number(filename):
    """Try to extract page number from filename."""
    base = os.path.basename(filename)
    if base.startswith("page_"):
        num_part = base.replace("page_", "").replace(".png", "")
        return num_part
    elif base.startswith("book_user_capture_"):
        num_part = base.replace("book_user_capture_", "").replace(".png", "")
        return f"user_{num_part}"
    return base

def main():
    pages = get_page_files()
    print(f"Found {len(pages)} page images to OCR")
    
    all_text = []
    
    for i, page_path in enumerate(pages):
        page_id = extract_page_number(page_path)
        print(f"  [{i+1}/{len(pages)}] OCR: {os.path.basename(page_path)} ...", end=" ", flush=True)
        try:
            text = ocr_image(page_path)
            word_count = len(text.split())
            print(f"OK ({word_count} words)")
            all_text.append({
                'file': os.path.basename(page_path),
                'page_id': page_id,
                'text': text
            })
        except Exception as e:
            print(f"ERROR: {e}")
            all_text.append({
                'file': os.path.basename(page_path),
                'page_id': page_id,
                'text': f"[OCR ERROR: {e}]"
            })
    
    # Write single combined file
    combined_path = os.path.join(OUT_DIR, "FULL_BOOK_OCR.md")
    with open(combined_path, 'w', encoding='utf-8') as f:
        f.write("# IT HAD 2 HAPPEN: THE AGONY OF SUCCESS\n")
        f.write("## Full OCR Transcript - Brian Banks, J.D. (2020)\n")
        f.write("## OCR'd from Kindle Cloud Reader screenshots, September 16, 2026\n")
        f.write("## Source: 02-evidence/book-pages/\n\n")
        f.write("---\n\n")
        
        for entry in all_text:
            f.write(f"## --- {entry['file']} (page {entry['page_id']}) ---\n\n")
            f.write(entry['text'])
            f.write("\n\n---\n\n")
    
    print(f"\nWrote combined OCR: {combined_path}")
    print(f"Total pages: {len(all_text)}")
    total_words = sum(len(e['text'].split()) for e in all_text)
    print(f"Total words: {total_words}")

if __name__ == "__main__":
    main()
