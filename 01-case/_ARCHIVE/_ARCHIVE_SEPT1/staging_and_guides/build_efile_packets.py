"""
Build the 2 e-filing PDFs for Wayne County 3rdcc.org Domestic Case Filings.

Upload 1: PLEADING.pdf  -> "Pleading" button
Upload 2: MOTION.pdf    -> "Motion" button

Uses scanned, signed documents from scans/ directory.

Run: python build_efile_packets.py
Requires: pip install PyPDF2 fpdf2 Pillow
"""

from fpdf import FPDF
import os

try:
    from PyPDF2 import PdfMerger
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

FILING_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(FILING_DIR, "scans")
UPLOAD_DIR = os.path.join(FILING_DIR, "efile_uploads")
EVIDENCE_DIR = os.path.join(os.path.dirname(FILING_DIR), "..", "02-evidence", "photos")


def image_to_pdf(image_path, pdf_path, label=None):
    """Convert an image (jpeg/png) to a single-page PDF."""
    pdf = FPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    if label:
        pdf.set_font("Courier", "B", 11)
        pdf.cell(0, 8, label, new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 3, "", new_x="LMARGIN", new_y="NEXT")

    margin = 15
    max_w = 215.9 - 2 * margin
    max_h = 279.4 - 2 * margin - (15 if label else 0)

    from PIL import Image
    img = Image.open(image_path)
    w_px, h_px = img.size
    aspect = h_px / w_px

    if aspect > max_h / max_w:
        h = max_h
        w = h / aspect
    else:
        w = max_w
        h = w * aspect

    x = margin + (max_w - w) / 2
    pdf.image(image_path, x=x, y=pdf.get_y(), w=w, h=h)
    pdf.output(pdf_path)
    return pdf_path


def md_to_pdf(md_path, pdf_path):
    """Convert a text file to a simple PDF."""
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    pdf = FPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=25)
    pdf.add_page()
    pdf.set_font("Courier", size=10)

    for line in text.split("\n"):
        line = line.replace("\u2014", "--").replace("\u2013", "-")
        line = line.replace("\u201c", '"').replace("\u201d", '"')
        line = line.replace("\u2018", "'").replace("\u2019", "'")
        pdf.cell(0, 5, line.rstrip(), new_x="LMARGIN", new_y="NEXT")

    pdf.output(pdf_path)
    return pdf_path


def merge_pdfs(pdf_list, output_path):
    """Merge multiple PDFs into one."""
    if not HAS_PYPDF2:
        print("  ERROR: PyPDF2 not installed. Run: pip install PyPDF2")
        return False
    merger = PdfMerger()
    for p in pdf_list:
        if os.path.exists(p):
            merger.append(p)
            print(f"    + {os.path.basename(p)}")
        else:
            print(f"    MISSING: {p}")
    merger.write(output_path)
    merger.close()
    return True


def main():
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    print("=" * 60)
    print("BUILDING E-FILE PACKETS (2 uploads)")
    print("=" * 60)

    # Verify scans exist
    scans = {
        "answer":     os.path.join(SCANS_DIR, "complaintResponse.pdf"),
        "motion":     os.path.join(SCANS_DIR, "tempOrder.pdf"),
        "mc416":      os.path.join(SCANS_DIR, "jurisdiictionAffidaviit.pdf"),
        "foc23":      os.path.join(SCANS_DIR, "verifiedStatement.pdf"),
        "ivd":        os.path.join(SCANS_DIR, "childSupportIV-D.pdf"),
        "lease":      os.path.join(SCANS_DIR, "bluegateLease.pdf"),
        "dd214":      os.path.join(SCANS_DIR, "dd214Mitchell.pdf"),
    }

    print("\n[1] Checking scanned documents...")
    all_found = True
    for name, path in scans.items():
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            print(f"    {name:15s} -> {size_kb:>7.0f} KB  OK")
        else:
            print(f"    {name:15s} -> MISSING!")
            all_found = False

    if not all_found:
        print("\n  Some scans are missing. Add them to scans/ and re-run.")
        return

    # Build exhibit PDFs from images
    print("\n[2] Converting image exhibits to PDF...")
    exhibit_pdfs = {}

    # Exhibit B: DSDT enrollment email screenshot
    dsdt_screenshot = os.path.join(SCANS_DIR, "dsdt_enrollment_email.png")
    dsdt_txt = os.path.join(UPLOAD_DIR, "exhibit_C_dsdt_enrollment.txt")
    if os.path.exists(dsdt_screenshot):
        out = os.path.join(UPLOAD_DIR, "exhibit_B_dsdt_screenshot.pdf")
        image_to_pdf(dsdt_screenshot, out,
                     label="EXHIBIT B -- DSDT College Enrollment Email (VET TEC 2.0)")
        exhibit_pdfs["B_dsdt_img"] = out
        print(f"    Exhibit B (DSDT screenshot): CONVERTED")
    if os.path.exists(dsdt_txt):
        out = os.path.join(UPLOAD_DIR, "exhibit_B_dsdt_text.pdf")
        md_to_pdf(dsdt_txt, out)
        exhibit_pdfs["B_dsdt_txt"] = out
        print(f"    Exhibit B (DSDT text): CONVERTED")

    # Exhibit C: Shayla's Verified Statement (IMG_5397)
    img5397 = os.path.join(EVIDENCE_DIR, "custody_papers", "IMG_5397.jpeg")
    if os.path.exists(img5397):
        out = os.path.join(UPLOAD_DIR, "exhibit_C_shayla_verified.pdf")
        image_to_pdf(img5397, out,
                     label="EXHIBIT C -- Plaintiff's Verified Statement (blank income/employer)")
        exhibit_pdfs["C_verified"] = out
        print(f"    Exhibit C (Shayla Verified Statement): CONVERTED")
    else:
        print(f"    Exhibit C (IMG_5397): MISSING")

    # --- UPLOAD 1: PLEADING ---
    print("\n[3] Building UPLOAD 1: PLEADING.pdf")
    pleading_parts = [
        scans["answer"],       # Answer + Counterclaim (8 pages, signed)
        scans["foc23"],        # FOC 23 Verified Statement (2 pages, signed)
        scans["mc416"],        # MC 416 UCCJEA (2 pages, notarized)
        scans["ivd"],          # DHS-1201D IV-D (1 page, signed)
    ]
    pleading_output = os.path.join(UPLOAD_DIR, "UPLOAD_1_PLEADING.pdf")
    merge_pdfs(pleading_parts, pleading_output)
    print(f"    -> {pleading_output}")

    # --- UPLOAD 2: MOTION ---
    print("\n[4] Building UPLOAD 2: MOTION.pdf")
    motion_parts = [
        scans["motion"],       # Temp Order Motion (4 pages, signed)
        scans["lease"],        # Exhibit A: Lease (5 pages)
    ]
    if "B_dsdt_txt" in exhibit_pdfs:
        motion_parts.append(exhibit_pdfs["B_dsdt_txt"])
    if "B_dsdt_img" in exhibit_pdfs:
        motion_parts.append(exhibit_pdfs["B_dsdt_img"])
    if "C_verified" in exhibit_pdfs:
        motion_parts.append(exhibit_pdfs["C_verified"])
    motion_parts.append(scans["dd214"])  # Exhibit D: DD-214

    motion_output = os.path.join(UPLOAD_DIR, "UPLOAD_2_MOTION.pdf")
    merge_pdfs(motion_parts, motion_output)
    print(f"    -> {motion_output}")

    # Summary
    print("\n" + "=" * 60)
    print("E-FILE UPLOAD SUMMARY")
    print("=" * 60)
    for f in sorted(os.listdir(UPLOAD_DIR)):
        if f.startswith("UPLOAD_"):
            fpath = os.path.join(UPLOAD_DIR, f)
            size_kb = os.path.getsize(fpath) / 1024
            print(f"  {f:45s} {size_kb:>8.1f} KB")

    print("\nREADY TO UPLOAD:")
    print("  1. Go to www.3rdcc.org -> Outside Agency Web Access")
    print("  2. Click 'Pleading' -> upload UPLOAD_1_PLEADING.pdf")
    print("  3. Click 'Motion'   -> upload UPLOAD_2_MOTION.pdf")
    print("  4. Pay fees at allpaid.com (code 6223)")


if __name__ == "__main__":
    main()

