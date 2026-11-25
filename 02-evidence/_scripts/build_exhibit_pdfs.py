"""
Build Federal Packet Exhibit PDFs
Compiles evidence into tiered exhibit packages for each agency.
"""

import fitz  # PyMuPDF
from PIL import Image
from pathlib import Path
import io
import os
import sys

EVIDENCE = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence")
OUTPUT = Path(r"C:\Users\mokke\Desktop\FEDERAL_PACKET_DEPLOY\EXHIBITS")
OUTPUT.mkdir(parents=True, exist_ok=True)

DPI = 150  # balance quality vs file size

def img_to_pdf_page(doc, img_path, label=None):
    """Add an image as a PDF page, scaled to fit letter size with label."""
    try:
        img = Image.open(img_path)
        if img.mode == 'RGBA':
            bg = Image.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        page_w, page_h = 612, 792  # letter
        margin = 36
        label_space = 30 if label else 0
        avail_w = page_w - 2 * margin
        avail_h = page_h - 2 * margin - label_space

        iw, ih = img.size
        scale = min(avail_w / iw, avail_h / ih, 1.0)
        new_w, new_h = int(iw * scale), int(ih * scale)

        img_resized = img.resize((new_w, new_h), Image.LANCZOS)
        buf = io.BytesIO()
        img_resized.save(buf, format='JPEG', quality=85)
        buf.seek(0)

        page = doc.new_page(width=page_w, height=page_h)
        x = (page_w - new_w) / 2
        y = margin + label_space
        rect = fitz.Rect(x, y, x + new_w, y + new_h)
        page.insert_image(rect, stream=buf.read())

        if label:
            page.insert_text(
                fitz.Point(margin, margin + 14),
                label,
                fontsize=9,
                fontname="helv",
                color=(0.3, 0.3, 0.3)
            )
        return True
    except Exception as e:
        print(f"  SKIP {img_path.name}: {e}")
        return False


def pdf_to_pdf_pages(doc, pdf_path, label_prefix=None):
    """Merge pages from an existing PDF into the target doc."""
    try:
        src = fitz.open(str(pdf_path))
        start = len(doc)
        doc.insert_pdf(src)
        if label_prefix:
            for i in range(start, len(doc)):
                page = doc[i]
                page.insert_text(
                    fitz.Point(36, 20),
                    f"{label_prefix} — p.{i - start + 1}",
                    fontsize=8,
                    fontname="helv",
                    color=(0.4, 0.4, 0.4)
                )
        src.close()
        return True
    except Exception as e:
        print(f"  SKIP PDF {pdf_path.name}: {e}")
        return False


def add_section_divider(doc, title, subtitle=""):
    """Add a section divider page."""
    page = doc.new_page(width=612, height=792)
    page.insert_text(fitz.Point(72, 300), title, fontsize=24, fontname="helv", color=(0.1, 0.1, 0.1))
    if subtitle:
        page.insert_text(fitz.Point(72, 340), subtitle, fontsize=12, fontname="helv", color=(0.4, 0.4, 0.4))


def build_core_exhibits():
    """Tier 1: Core exhibits that go to ALL agencies."""
    print("\n=== BUILDING CORE EXHIBITS (Tier 1 — All Agencies) ===\n")
    doc = fitz.open()

    # --- SECTION A: Banks' Credential Fraud ---
    add_section_divider(doc, "EXHIBIT A: CREDENTIAL FRAUD",
                        "Banks claims 'J.D.' across 9+ locations — never admitted to any bar")

    # Banks LinkedIn
    linkedin_dir = EVIDENCE / "banks-linkedin"
    if linkedin_dir.exists():
        imgs = sorted(linkedin_dir.glob("*.PNG"))[:6]
        for img in imgs:
            img_to_pdf_page(doc, img, "A4 — Banks LinkedIn Profile: 'Brian Banks, J.D., Ph.D.'")
        print(f"  A4: {len(imgs)} LinkedIn pages")

    # PCA Board page
    for f in ["PCA_BOARD_PAGE_SEP5_2026.png", "PCA_BOARD_PAGE_FOOTER_SEP5_2026.png"]:
        p = EVIDENCE / "web-captures" / f
        if p.exists():
            img_to_pdf_page(doc, p, "E9 — PCA Board of Directors: Miller (Chair), Moreland (Vice Chair)")
    pca_board2 = EVIDENCE / "case-docs" / "PCA_BOARD_PAGE2_SCREENSHOT_SEP5.png"
    if pca_board2.exists():
        img_to_pdf_page(doc, pca_board2, "E9 — PCA Board continued")
    print("  E9: PCA Board pages")

    # CBC/Eventbrite
    for f in ["BANKS_CBC_RECEPTION_SEP18_EVENTBRITE.png", "BANKS_EVENTBRITE_PROFILE_SEP12.png",
              "BANKS_CBC_RECEPTION_SEP18_SEP12.png"]:
        p = EVIDENCE / "web-captures" / f
        if p.exists():
            img_to_pdf_page(doc, p, "NEW — Banks Eventbrite: CBC Parties 2023-2026")
    print("  CBC Eventbrite captures")

    # PCA Gala
    for f in ["PCA_black_tie_gala_eventbrite_may16.png", "PCA_inaugural_gala_may16_eventbrite.png"]:
        p = EVIDENCE / "screenshots-social" / f
        if p.exists():
            img_to_pdf_page(doc, p, "NEW — PCA Black Tie Gala ($161.90/ticket, sold out)")
    print("  PCA Gala captures")

    # --- SECTION B: Mail Fraud / Obstruction ---
    add_section_divider(doc, "EXHIBIT B: MAIL FRAUD & OBSTRUCTION",
                        "USPS OIG Cases #174517, #202990, #208322 — Leon Smith")

    # Signature comparison
    sig_dir = EVIDENCE / "signature-comparison"
    if sig_dir.exists():
        for f in sorted(sig_dir.glob("*.png")):
            img_to_pdf_page(doc, f, f"B4 — {f.stem}")
        print(f"  B4: {len(list(sig_dir.glob('*.png')))} signature panels")

    # Ring camera key frames (select ~8 representative frames)
    ring_dir = EVIDENCE / "ring_sep2"
    if ring_dir.exists():
        ring_frames = sorted([f for f in ring_dir.glob("ring_*.png")])
        selected = ring_frames[::max(1, len(ring_frames)//8)][:8]
        for f in selected:
            img_to_pdf_page(doc, f, f"B3 — Ring Doorbell: Leon Smith assault — {f.stem}")
        print(f"  B3: {len(selected)} Ring frames")

    # --- SECTION C: Financial Evidence ---
    add_section_divider(doc, "EXHIBIT C: FINANCIAL EVIDENCE",
                        "MacDowell: $4.9M revenue, 3% math, $0 employees, $3.9M to Banks' LLC")

    fin_dir = EVIDENCE / "screenshots-financial"
    if fin_dir.exists():
        for f in sorted(fin_dir.glob("*.png")):
            img_to_pdf_page(doc, f, "C — MacDowell Financial Records")
        print(f"  C: {len(list(fin_dir.glob('*.png')))} financial screenshots")

    # --- SECTION D: Criminal Records ---
    add_section_divider(doc, "EXHIBIT D: CRIMINAL RECORDS",
                        "Holland ICHAT + MDOC: Drug trafficking, discharged 'WITHOUT IMPROVEMENT'")

    # Holland ICHAT
    for f in ["ICHAT_HOLLAND_P1_SEARCH.png", "ICHAT_HOLLAND_P2_RECORD.png", "ICHAT_HOLLAND_P3_CONT.png"]:
        p = EVIDENCE / "case-docs" / f
        if p.exists():
            img_to_pdf_page(doc, p, f"D5 — Holland ICHAT: {f.replace('ICHAT_HOLLAND_', '').replace('.png', '')}")
    print("  D5: Holland ICHAT")

    # Holland MDOC
    for f in ["MDOC_443789_JOSEPH_HOLLAND.png", "MDOC_443789_JOSEPH_HOLLAND_FULL.png"]:
        p = EVIDENCE / "case-docs" / f
        if p.exists():
            img_to_pdf_page(doc, p, "D6 — Holland MDOC OTIS: #443789, discharged WITHOUT IMPROVEMENT")
    print("  D6: Holland MDOC")

    # Holland ICHAT PDF if available
    ichat_pdf = EVIDENCE / "case-docs" / "ICHAT_JOSEPH_HOLLAND_JR.pdf"
    if ichat_pdf.exists():
        pdf_to_pdf_pages(doc, ichat_pdf, "D5 — ICHAT Full Record")
        print("  D5: ICHAT PDF merged")

    # --- SECTION E: Property Records ---
    add_section_divider(doc, "EXHIBIT E: PROPERTY RECORDS",
                        "Wayne County ROD: Dresden QCD, $68K Mortgage, Severn Trust Transfer, HELOC")

    # Key ROD documents from batch5 (Dresden QCD + Mortgage)
    batch5 = EVIDENCE / "wayne-rod-sep2" / "batch5"
    if batch5.exists():
        pdfs = sorted(batch5.glob("*.pdf"))
        for pdf in pdfs[:10]:
            pdf_to_pdf_pages(doc, pdf, f"D2 — Wayne ROD: {pdf.stem[:40]}")
        print(f"  D2: {min(len(pdfs), 10)} ROD documents from batch5")

    # --- SECTION F: PCA/Charter Documents ---
    add_section_divider(doc, "EXHIBIT F: CHARTER SCHOOL DOCUMENTS",
                        "PCA Charter Contract, Budget, Management Agreement")

    for fname in ["PCA_DPSCD_CHARTER_CONTRACT.pdf", "PCA_BUDGET_FY2627.pdf",
                   "PCA_MANAGEMENT_AGREEMENT_AUG2025.pdf"]:
        p = EVIDENCE / "case-docs" / fname
        if p.exists():
            pdf_to_pdf_pages(doc, p, f"F — {fname.replace('.pdf', '').replace('_', ' ')}")
            print(f"  F: {fname}")

    # Save
    outpath = OUTPUT / "CORE_EXHIBITS_ALL_AGENCIES.pdf"
    doc.save(str(outpath), deflate=True, garbage=4)
    size_mb = outpath.stat().st_size / (1024 * 1024)
    print(f"\n  >>> SAVED: {outpath.name} — {len(doc)} pages, {size_mb:.1f} MB")
    doc.close()
    return outpath


def build_book_exhibit(book_dir, book_name, exhibit_id):
    """Build a book transcript exhibit from screenshots."""
    print(f"\n=== BUILDING {book_name} EXHIBIT ===\n")
    doc = fitz.open()
    add_section_divider(doc, f"EXHIBIT {exhibit_id}: {book_name}",
                        "Party admission under FRE 801(d)(2)(A)")

    if not book_dir.exists():
        print(f"  Directory not found: {book_dir}")
        return None

    # Get all image files sorted
    exts = ['*.png', '*.PNG', '*.jpg', '*.jpeg', '*.JPEG']
    imgs = []
    for ext in exts:
        imgs.extend(book_dir.rglob(ext))
    imgs = sorted(set(imgs))

    for i, img in enumerate(imgs):
        rel = img.relative_to(book_dir)
        img_to_pdf_page(doc, img, f"{exhibit_id} — {book_name} — {rel}")
        if (i + 1) % 50 == 0:
            print(f"  {i+1}/{len(imgs)} pages...")

    outpath = OUTPUT / f"EXHIBIT_{exhibit_id}_{book_name.replace(' ', '_').upper()}.pdf"
    doc.save(str(outpath), deflate=True, garbage=4)
    size_mb = outpath.stat().st_size / (1024 * 1024)
    print(f"\n  >>> SAVED: {outpath.name} — {len(doc)} pages, {size_mb:.1f} MB")
    doc.close()
    return outpath


def build_pacer_exhibit():
    """Build PACER documents exhibit."""
    print(f"\n=== BUILDING PACER DOCUMENTS EXHIBIT ===\n")
    doc = fitz.open()
    add_section_divider(doc, "EXHIBIT G: PACER DOCUMENTS",
                        "Federal court records — bankruptcy, civil rights, BMF")

    pacer_dir = EVIDENCE / "pacer-docs"
    for subdir in sorted(pacer_dir.iterdir()):
        if not subdir.is_dir():
            continue
        add_section_divider(doc, f"PACER: {subdir.name}", "")
        pdfs = sorted(subdir.glob("*.pdf"))
        for pdf in pdfs:
            pdf_to_pdf_pages(doc, pdf, f"G — PACER: {subdir.name}/{pdf.name[:50]}")
        imgs = sorted(subdir.glob("*.png")) + sorted(subdir.glob("*.PNG"))
        for img in imgs:
            img_to_pdf_page(doc, img, f"G — PACER: {subdir.name}/{img.name[:50]}")
        print(f"  {subdir.name}: {len(pdfs)} PDFs + {len(imgs)} images")

    outpath = OUTPUT / "EXHIBIT_G_PACER_DOCUMENTS.pdf"
    doc.save(str(outpath), deflate=True, garbage=4)
    size_mb = outpath.stat().st_size / (1024 * 1024)
    print(f"\n  >>> SAVED: {outpath.name} — {len(doc)} pages, {size_mb:.1f} MB")
    doc.close()
    return outpath


def build_rod_exhibit():
    """Build Wayne ROD key documents exhibit (not all 594 — just critical batches)."""
    print(f"\n=== BUILDING WAYNE ROD KEY DOCUMENTS ===\n")
    doc = fitz.open()
    add_section_divider(doc, "EXHIBIT H: WAYNE COUNTY REGISTER OF DEEDS",
                        "Property transfers, mortgages, trust documents — Dresden, Newcastle, Severn")

    rod_dir = EVIDENCE / "wayne-rod-sep2"
    for batch_name in ["batch4", "batch5"]:  # batch4=Severn/trust, batch5=Dresden/Smith
        batch = rod_dir / batch_name
        if not batch.exists():
            continue
        add_section_divider(doc, f"ROD {batch_name}", "")
        pdfs = sorted(batch.glob("*.pdf"))
        for pdf in pdfs:
            pdf_to_pdf_pages(doc, pdf, f"H — ROD {batch_name}: {pdf.stem[:50]}")
        print(f"  {batch_name}: {len(pdfs)} PDFs")

    outpath = OUTPUT / "EXHIBIT_H_WAYNE_ROD_KEY.pdf"
    doc.save(str(outpath), deflate=True, garbage=4)
    size_mb = outpath.stat().st_size / (1024 * 1024)
    print(f"\n  >>> SAVED: {outpath.name} — {len(doc)} pages, {size_mb:.1f} MB")
    doc.close()
    return outpath


def build_social_correspondence_exhibit():
    """Build text messages and correspondence exhibit."""
    print(f"\n=== BUILDING CORRESPONDENCE EXHIBIT ===\n")
    doc = fitz.open()
    add_section_divider(doc, "EXHIBIT I: COMMUNICATIONS & SERVICE PROOF",
                        "Text messages, service attempts, correspondence")

    # Text screenshots
    txt_dir = EVIDENCE / "screenshots-texts"
    if txt_dir.exists():
        add_section_divider(doc, "TEXT MESSAGES", "Kevin ↔ Smiths")
        imgs = sorted(txt_dir.glob("*.png"))
        for img in imgs:
            img_to_pdf_page(doc, img, f"I — Text: {img.name}")
        print(f"  Texts: {len(imgs)} screenshots")

    # Key correspondence (first 30)
    corr_dir = EVIDENCE / "screenshots-correspondence"
    if corr_dir.exists():
        add_section_divider(doc, "SERVICE CORRESPONDENCE", "Certified mail, fax, email proof")
        imgs = sorted(corr_dir.glob("*.png"))[:30]
        for img in imgs:
            img_to_pdf_page(doc, img, f"I — Correspondence: {img.name}")
        # Also PDFs (fax confirmations etc)
        pdfs = sorted(corr_dir.glob("*.pdf"))[:10]
        for pdf in pdfs:
            pdf_to_pdf_pages(doc, pdf, "I — Fax/Mail Confirmation")
        print(f"  Correspondence: {len(imgs)} images + {len(pdfs)} PDFs")

    outpath = OUTPUT / "EXHIBIT_I_CORRESPONDENCE.pdf"
    doc.save(str(outpath), deflate=True, garbage=4)
    size_mb = outpath.stat().st_size / (1024 * 1024)
    print(f"\n  >>> SAVED: {outpath.name} — {len(doc)} pages, {size_mb:.1f} MB")
    doc.close()
    return outpath


if __name__ == "__main__":
    print("=" * 60)
    print("FEDERAL PACKET EXHIBIT BUILDER")
    print("=" * 60)

    results = {}

    # Core exhibits (all agencies)
    results['core'] = build_core_exhibits()

    # PACER documents
    results['pacer'] = build_pacer_exhibit()

    # Wayne ROD key docs
    results['rod'] = build_rod_exhibit()

    # Correspondence / service proof
    results['corr'] = build_social_correspondence_exhibit()

    # Books (large — separate PDFs)
    results['banks_book'] = build_book_exhibit(
        EVIDENCE / "banks-book", "Banks Book - It Had 2 Happen", "A1")
    results['bmf_book'] = build_book_exhibit(
        EVIDENCE / "bmf-book", "BMF Book - Black Mafia Queen", "A11")

    print("\n" + "=" * 60)
    print("BUILD COMPLETE — EXHIBIT INVENTORY")
    print("=" * 60)
    total_size = 0
    for name, path in results.items():
        if path and path.exists():
            sz = path.stat().st_size / (1024 * 1024)
            total_size += sz
            pg = fitz.open(str(path))
            print(f"  {path.name:50s} {pg.page_count:4d} pages  {sz:6.1f} MB")
            pg.close()
    print(f"\n  TOTAL: {total_size:.1f} MB across {len([r for r in results.values() if r])} PDFs")
    print(f"\n  Output: {OUTPUT}")
