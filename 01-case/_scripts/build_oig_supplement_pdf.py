"""
Build a single COMPRESSED PDF combining ALL OIG supplement evidence.
Target: under 5MB for OIG online upload.
"""

import os
import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from io import BytesIO

PROJECT = r"C:\Users\mokke\jobHunt\bluegate-tenancy"
EVIDENCE = os.path.join(PROJECT, '02-evidence')
SIGS = os.path.join(EVIDENCE, 'signature-comparison')
TEXTS = os.path.join(EVIDENCE, 'screenshots-correspondence')
RING_PDF = os.path.join(PROJECT, '01-case', 'evidence', 'RING_EXHIBIT_KEYFRAMES_SEP2.pdf')
PPO_PDF = r'C:\Users\mokke\Documents\ppoHearingServed.pdf'
OUTPUT = os.path.join(os.path.expanduser('~'), 'Desktop',
                      'SIGNATURE_COMPARISON_SEP17',
                      'OIG_SUPPLEMENT_COMPLETE_SEP17.pdf')

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch

# Compression settings
IMG_MAX_W = 1200  # pixels max width for embedded images
IMG_QUALITY = 55  # JPEG quality for compression


def compress_image(img_path, max_w=IMG_MAX_W, quality=IMG_QUALITY):
    """Compress an image and return as JPEG bytes in a BytesIO."""
    img = Image.open(img_path)
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    w, h = img.size
    if w > max_w:
        ratio = max_w / w
        img = img.resize((max_w, int(h * ratio)), Image.LANCZOS)

    buf = BytesIO()
    img.save(buf, format='JPEG', quality=quality, optimize=True)
    buf.seek(0)
    return buf, img.size


def draw_header(c, title, subtitle=None):
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 0.6 * inch, title)
    if subtitle:
        c.setFont("Helvetica", 9)
        c.drawCentredString(PAGE_W / 2, PAGE_H - 0.82 * inch, subtitle)


def draw_footer(c, page_num):
    c.setFont("Helvetica", 8)
    c.drawCentredString(PAGE_W / 2, 0.4 * inch,
                        f"OIG Supplement - Case #174517 / Ref #202990 - Page {page_num}")
    c.drawRightString(PAGE_W - MARGIN, 0.4 * inch, "September 17, 2026")


def add_image_page(c, img_path, title, subtitle, page_num):
    """Add a page with a compressed image."""
    c.showPage()
    draw_header(c, title, subtitle)
    draw_footer(c, page_num)

    buf, (iw, ih) = compress_image(img_path)
    aspect = iw / ih

    avail_w = PAGE_W - 2 * MARGIN
    avail_h = PAGE_H - 1.5 * inch - MARGIN

    if aspect > avail_w / avail_h:
        draw_w = avail_w
        draw_h = avail_w / aspect
    else:
        draw_h = avail_h
        draw_w = avail_h * aspect

    x = (PAGE_W - draw_w) / 2
    y = PAGE_H - 1.3 * inch - draw_h

    img_reader = ImageReader(buf)
    c.drawImage(img_reader, x, y, draw_w, draw_h,
                preserveAspectRatio=True, anchor='n')


def build_cover_pages(c):
    """Build the cover/narrative pages."""
    page = 1
    draw_header(c, "SUPPLEMENT TO USPS OIG COMPLAINT",
                "Case #174517 | Reference #202990")
    draw_footer(c, page)

    y = PAGE_H - 1.2 * inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN, y, "RE: Mail Interception, Signature Forgery, and Retaliation")
    y -= 16
    c.drawString(MARGIN, y, "Employee: Leon A. Smith, USPS Mail Carrier, Harper Woods PO")
    y -= 24

    lines = [
        ("I. IDENTITY OF THE FORGER", True),
        ("", False),
        ("Handwriting comparison of forged return receipts (PS Form 3811) against", False),
        ("notarized Wayne County Register of Deeds records and federal bankruptcy", False),
        ("petitions proves that LEON A. SMITH forged ALL FIVE green card signatures.", False),
        ("", False),
        ("Key evidence: Lake Trust CU mortgage (Doc# 2025201292, June 24, 2025) --", False),
        ("Leon and Marquita signed the SAME document before a notary. Their 'S' in", False),
        ("Smith tails in OPPOSITE directions. All green cards match Leon's direction.", False),
        ("Green cards do NOT match Marquita's or Simone's authenticated signatures.", False),
        ("", False),
        ("II. LEON'S RESPONSE -- CONSCIOUSNESS OF GUILT", True),
        ("", False),
        ("Sep 16, 2026: Kevin Mok sent Leon photos of OIG complaint + sig findings.", False),
        ("Sep 17, 2026 at 11:37 AM: Leon responded: 'Good luck.'", False),
        ("He did NOT deny intercepting mail. He did NOT deny forging signatures.", False),
        ("", False),
        ("III. RETALIATION -- PHYSICAL ASSAULT", True),
        ("", False),
        ("Sep 2, 2026 (12 days after interception): Leon physically assaulted", False),
        ("DaSean Mitchell at XXXX Cornerstone Blvd, Detroit. Captured on Ring", False),
        ("doorbell camera. DPD Report #26-0909-0176. The assault was retaliation", False),
        ("for the civil lawsuits contained in the intercepted letters.", False),
        ("", False),
        ("IV. ONGOING CONCERN -- NEW MAIL AT RISK", True),
        ("", False),
        ("PPO hearing documents and assault evidence are now being sent via", False),
        ("certified mail to the same family at the same address. Leon remains", False),
        ("employed at Harper Woods PO. Tracking numbers for the new wave are", False),
        ("included in Exhibit C. I request Leon's facility access be reviewed.", False),
        ("", False),
        ("V. VIOLATIONS", True),
        ("", False),
        ("18 U.S.C. 1708 -- Theft/receipt of stolen mail", False),
        ("18 U.S.C. 1702 -- Obstruction of correspondence", False),
        ("18 U.S.C. 1341 -- Mail fraud (forged postal documents to obstruct litigation)", False),
        ("18 U.S.C. 1001 -- False statements on official USPS documents", False),
        ("", False),
        ("VI. EXHIBITS IN THIS DOCUMENT", True),
        ("", False),
        ("Exhibit A (p.2-3): Text messages -- Leon's 'Good luck' response", False),
        ("Exhibit B-1 (p.4): All 5 green card signatures -- same hand visible", False),
        ("Exhibit B-2 (p.5): Leon & Marquita authentic sigs vs. green cards", False),
        ("Exhibit B-3 (p.6): Simone authentic sigs vs. green card", False),
        ("Exhibit C (p.7-9): PPO hearing service receipts (new tracking #s)", False),
        ("Exhibit D (p.10+): Ring doorbell assault evidence -- key frames", False),
    ]

    c.setFont("Helvetica", 9)
    for text, is_bold in lines:
        if is_bold:
            c.setFont("Helvetica-Bold", 10)
        if text == "":
            y -= 8
        else:
            c.drawString(MARGIN, y, text)
            y -= 13
        if is_bold:
            c.setFont("Helvetica", 9)

        if y < MARGIN + 0.5 * inch:
            c.showPage()
            page += 1
            draw_header(c, "SUPPLEMENT (continued)")
            draw_footer(c, page)
            y = PAGE_H - 1.2 * inch

    return page


def compress_existing_pdf(pdf_path, target_dpi=100):
    """Re-render an existing PDF with compressed images."""
    src = fitz.open(pdf_path)
    result = fitz.open()

    for page in src:
        # Get page as a pixmap at reduced DPI
        mat = fitz.Matrix(target_dpi / 72, target_dpi / 72)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        # Convert to JPEG
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        buf = BytesIO()
        img.save(buf, format='JPEG', quality=IMG_QUALITY, optimize=True)
        buf.seek(0)

        # Create new page with same dimensions
        new_page = result.new_page(width=page.rect.width, height=page.rect.height)
        rect = new_page.rect
        new_page.insert_image(rect, stream=buf.getvalue())

    src.close()
    return result


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

    # Build reportlab pages (cover + image exhibits)
    tmp = BytesIO()
    c = canvas.Canvas(tmp, pagesize=letter)
    c.setTitle("OIG Supplement - Case #174517 - September 17, 2026")
    c.setAuthor("Kevin Mok")

    print("Building cover pages...")
    page = build_cover_pages(c)

    exhibit_images = [
        (os.path.join(TEXTS, 'LEON_TEXT_SIGNATURE_COMPARISON_GOOD_LUCK_SEP17.png'),
         "EXHIBIT A -- Text Message Exchange (1/2)",
         "Leon responds 'Good luck' after receiving OIG complaint + signature findings"),
        (os.path.join(TEXTS, 'LEON_TEXT_SIGNATURE_COMPARISON_FULL_SEP17.png'),
         "EXHIBIT A -- Text Message Exchange (2/2)",
         "Full thread showing OIG complaint photos sent to Leon"),
        (os.path.join(SIGS, 'EXHIBIT_B1_GREEN_CARD_SIGNATURES_ALL.png'),
         "EXHIBIT B-1 -- All 5 Green Card Signatures",
         "Same hand: identical pen pressure, S formation, and slant across all cards"),
        (os.path.join(SIGS, 'EXHIBIT_B2_LEON_MARQUITA_AUTHENTIC_VS_GREEN_CARDS.png'),
         "EXHIBIT B-2 -- Leon & Marquita Authentic vs. Green Cards",
         "Lake Trust mortgage (notarized 6/24/2025): S tails opposite. Green cards match LEON."),
        (os.path.join(SIGS, 'EXHIBIT_B3_SIMONE_AUTHENTIC_VS_GREEN_CARD.png'),
         "EXHIBIT B-3 -- Simone Authentic vs. Green Card",
         "20 years of mortgage sigs bear NO resemblance to green card 'S Smith'"),
    ]

    for img_path, title, subtitle in exhibit_images:
        page += 1
        if os.path.exists(img_path):
            print(f"  Adding {title}...")
            add_image_page(c, img_path, title, subtitle, page)
        else:
            print(f"  SKIP: {img_path} not found")

    c.save()
    rl_bytes = tmp.getvalue()

    # Merge everything with PyMuPDF
    print("\nMerging and compressing PDFs...")
    result = fitz.open()

    # Add reportlab pages
    rl_doc = fitz.open(stream=rl_bytes, filetype="pdf")
    result.insert_pdf(rl_doc)
    rl_doc.close()

    # Compress and add PPO PDF
    if os.path.exists(PPO_PDF):
        print("  Compressing Exhibit C (PPO receipts)...")
        compressed = compress_existing_pdf(PPO_PDF, target_dpi=120)
        result.insert_pdf(compressed)
        print(f"    Added {compressed.page_count} pages")
        compressed.close()

    # Compress and add Ring PDF (the big one)
    if os.path.exists(RING_PDF):
        print("  Compressing Exhibit D (Ring assault frames)...")
        compressed = compress_existing_pdf(RING_PDF, target_dpi=96)
        result.insert_pdf(compressed)
        print(f"    Added {compressed.page_count} pages")
        compressed.close()

    # Save with garbage collection and deflation
    result.save(OUTPUT, garbage=4, deflate=True, deflate_images=True,
                deflate_fonts=True)

    final_size = os.path.getsize(OUTPUT)
    size_mb = final_size / (1024 * 1024)
    print(f"\nDONE: {OUTPUT}")
    print(f"Total pages: {len(result)}")
    print(f"File size: {size_mb:.2f} MB")

    if size_mb > 10:
        print("WARNING: Still over 10MB. May need lower quality.")
    elif size_mb > 5:
        print("NOTE: 5-10MB range. Should work if OIG limit is 10MB.")
    else:
        print("GOOD: Under 5MB. Should upload fine.")

    result.close()


if __name__ == "__main__":
    main()
