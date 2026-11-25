"""Merge each service packet into a single PDF for the process server."""
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from fpdf import FPDF

BASE = Path(r"C:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\court-filings\banks")
HOME = BASE / "SERVICE_HOME_GPW"
SCHOOL = BASE / "SERVICE_SCHOOL_PCA"


def md_to_pdf(md_path, pdf_path):
    """Convert a markdown/text file to a simple letter-sized PDF."""
    text = md_path.read_text(encoding="utf-8")
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=25)
    pdf.add_page()
    pdf.set_font("Courier", size=9)
    for line in text.split("\n"):
        safe = line.encode("latin-1", "replace").decode("latin-1")
        pdf.cell(0, 4, safe, new_x="LMARGIN", new_y="NEXT")
    pdf.output(str(pdf_path))
    print(f"  Converted MD -> PDF: {pdf_path.name} ({pdf.pages_count} pages)")


def merge_pdfs(pdf_list, output_path):
    """Merge a list of PDF paths into one output file."""
    writer = PdfWriter()
    total = 0
    for p in pdf_list:
        if not p.exists():
            print(f"  SKIP (missing): {p.name}")
            continue
        reader = PdfReader(str(p))
        for page in reader.pages:
            writer.add_page(page)
        total += len(reader.pages)
        print(f"  + {p.name} ({len(reader.pages)} pages)")
    writer.write(str(output_path))
    writer.close()
    print(f"  => {output_path.name}: {total} pages total\n")


# --- HOME SERVICE (GPW) ---
print("=" * 60)
print("SERVICE #1 — HOME (Banks + Purpose Group LLC)")
print("1968 Severn Rd, Grosse Pointe Woods, MI 48236")
print("=" * 60)

md_file = HOME / "08_TEXT_EXHIBITS.md"
md_pdf = HOME / "08_TEXT_EXHIBITS.pdf"
if md_file.exists():
    md_to_pdf(md_file, md_pdf)

home_pdfs = [
    HOME / "01_SUMMONS_BANKS_AND_PURPOSE.pdf",
    HOME / "02_COMPLAINT.pdf",
    HOME / "08_TEXT_EXHIBITS.pdf",
    HOME / "03_IMAGE_EXHIBITS.pdf",
    HOME / "04_EXHIBIT_A_AUTHORIZATION.pdf",
    HOME / "05_EXHIBIT_I_UPL_RECEIPT.pdf",
    HOME / "06_EXHIBIT_JK_JTC_MAIL.pdf",
    HOME / "07_EXHIBIT_JK_JTC_NOTARY.pdf",
]

merge_pdfs(home_pdfs, BASE / "SERVE_HOME_GPW_COMPLETE.pdf")

# --- SCHOOL SERVICE (PCA) ---
print("=" * 60)
print("SERVICE #2 — SCHOOL (Purpose Charter Academy)")
print("10101 E. Canfield St, Detroit, MI 48214")
print("=" * 60)

school_pdfs = [
    SCHOOL / "01_SUMMONS_PCA.pdf",
    SCHOOL / "02_COMPLAINT.pdf",
]

merge_pdfs(school_pdfs, BASE / "SERVE_SCHOOL_PCA_COMPLETE.pdf")

print("DONE. Two files ready to email to process server:")
print(f"  1. {BASE / 'SERVE_HOME_GPW_COMPLETE.pdf'}")
print(f"  2. {BASE / 'SERVE_SCHOOL_PCA_COMPLETE.pdf'}")

