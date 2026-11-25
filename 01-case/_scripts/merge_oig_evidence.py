from pypdf import PdfWriter, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from PIL import Image as PILImage
import os, io

BASE = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case"
EVIDENCE = os.path.join(BASE, "evidence")
FILING = os.path.join(BASE, "filing-ready")
OUTPUT = os.path.join(BASE, "evidence", "OIG_COMPLAINT_FULL_PACKAGE.pdf")

complaint_path = os.path.join(FILING, "31_USPS_OIG_COMPLAINT.txt")
with open(complaint_path, "r", encoding="utf-8") as f:
    complaint_text = f.read()

styles = getSampleStyleSheet()
body_style = ParagraphStyle(
    "ComplaintBody",
    parent=styles["Normal"],
    fontSize=9,
    leading=11,
    fontName="Courier",
    spaceAfter=2,
)
heading_style = ParagraphStyle(
    "ComplaintHeading",
    parent=styles["Heading2"],
    fontSize=11,
    spaceAfter=6,
)
title_style = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    fontSize=14,
    spaceAfter=12,
)

buf = io.BytesIO()
doc = SimpleDocTemplate(buf, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

story = []

story.append(Paragraph("USPS OIG COMPLAINT — FULL EVIDENCE PACKAGE", title_style))
story.append(Paragraph("Filed: August 27, 2026 | Kevin Mok | eco.primal@pm.me | [REDACTED_PHONE]", body_style))
story.append(Spacer(1, 12))

story.append(Paragraph("SECTION 1: WRITTEN COMPLAINT", heading_style))
story.append(Spacer(1, 6))

for line in complaint_text.split("\n"):
    clean = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if not clean.strip():
        story.append(Spacer(1, 6))
    elif clean.startswith("===="):
        story.append(Spacer(1, 8))
        story.append(Paragraph("=" * 60, body_style))
    else:
        story.append(Paragraph(clean, body_style))

story.append(PageBreak())

story.append(Paragraph("SECTION 2: USPS TRACKING SCREENSHOTS", heading_style))
story.append(Spacer(1, 6))
story.append(Paragraph("Screenshots captured from USPS.com on August 27, 2026, showing all 6 tracking numbers, service type (Certified Mail Restricted Delivery), delivery locations, and dates.", body_style))
story.append(Spacer(1, 12))

for i in range(1, 4):
    img_path = os.path.join(EVIDENCE, f"tracking_screenshot_{i}.png")
    if os.path.exists(img_path):
        img = PILImage.open(img_path)
        w, h = img.size
        aspect = h / w
        display_w = 6.5 * inch
        display_h = display_w * aspect
        if display_h > 9 * inch:
            display_h = 9 * inch
            display_w = display_h / aspect
        story.append(RLImage(img_path, width=display_w, height=display_h))
        story.append(Spacer(1, 12))

story.append(PageBreak())

doc.build(story)
buf.seek(0)

writer = PdfWriter()

complaint_reader = PdfReader(buf)
for page in complaint_reader.pages:
    writer.add_page(page)

sigs_path = os.path.join(EVIDENCE, "RestrictedReturnReceiptSigs.pdf")
if os.path.exists(sigs_path):
    sigs_reader = PdfReader(sigs_path)
    for page in sigs_reader.pages:
        writer.add_page(page)

receipts_path = os.path.join(EVIDENCE, "RestrictedReturnReceipt.pdf")
if os.path.exists(receipts_path):
    receipts_reader = PdfReader(receipts_path)
    for page in receipts_reader.pages:
        writer.add_page(page)

with open(OUTPUT, "wb") as f:
    writer.write(f)

total_pages = len(writer.pages)
file_size = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"Created: {OUTPUT}")
print(f"Total pages: {total_pages}")
print(f"File size: {file_size:.1f} MB")

