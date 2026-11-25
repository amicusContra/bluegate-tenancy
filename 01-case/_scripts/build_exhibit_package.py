from pypdf import PdfWriter, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os, io

BASE = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case"
FILING = os.path.join(BASE, "filing-ready")
EVIDENCE = os.path.join(BASE, "evidence")
OUTPUT = os.path.join(BASE, "evidence", "EXHIBIT_PACKAGE_FOR_FILING.pdf")

cover_path = os.path.join(FILING, "26_EXHIBITS_COMBINED.txt")
with open(cover_path, "r", encoding="utf-8") as f:
    cover_text = f.read()

styles = getSampleStyleSheet()
body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10, leading=13, fontName="Courier", spaceAfter=2)
title = ParagraphStyle("Title", parent=styles["Title"], fontSize=14, spaceAfter=12)

buf = io.BytesIO()
doc = SimpleDocTemplate(buf, pagesize=letter,
                        leftMargin=0.75*inch, rightMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

story = []
for line in cover_text.split("\n"):
    clean = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if not clean.strip():
        story.append(Spacer(1, 6))
    elif clean.startswith("===="):
        story.append(Spacer(1, 4))
        story.append(Paragraph("=" * 55, body))
    else:
        story.append(Paragraph(clean, body))

doc.build(story)
buf.seek(0)

writer = PdfWriter()

cover_reader = PdfReader(buf)
for page in cover_reader.pages:
    writer.add_page(page)

exhibit_a = r"C:\Users\mokke\Downloads\01_counterresponse_eavsdropping.pdf"
if os.path.exists(exhibit_a):
    reader_a = PdfReader(exhibit_a)
    for page in reader_a.pages:
        writer.add_page(page)
    print(f"Exhibit A: {len(reader_a.pages)} page(s)")

exhibit_b = os.path.join(EVIDENCE, "RestrictedReturnReceiptSigs.pdf")
if os.path.exists(exhibit_b):
    reader_b = PdfReader(exhibit_b)
    for page in reader_b.pages:
        writer.add_page(page)
    print(f"Exhibit B: {len(reader_b.pages)} page(s)")

with open(OUTPUT, "wb") as f:
    writer.write(f)

total = len(writer.pages)
size = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"\nCreated: {OUTPUT}")
print(f"Total pages: {total}")
print(f"File size: {size:.1f} MB")
print(f"\nPage breakdown:")
print(f"  Cover sheet: {len(cover_reader.pages)} page(s)")
print(f"  Exhibit A (eavesdropping): 1 page")
print(f"  Exhibit B (return receipts): 3 pages")
print(f"  TOTAL: {total} pages — print this file")

