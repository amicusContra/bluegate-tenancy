"""
Build federal packet PDF v2 — clean formatting, page numbers, TOC, fax broadcast.
"""
import os, re, csv
from pathlib import Path
from io import BytesIO

import markdown2
from xhtml2pdf import pisa
from pypdf import PdfWriter, PdfReader

BASE = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy")
PACKET_DIR = BASE / "01-case" / "filing-ready" / "packet"
DEPLOY = Path(r"c:\Users\mokke\Desktop\FEDERAL_DEPLOY")
DEPLOY.mkdir(exist_ok=True)
DOWNLOADS = Path(r"C:\Users\mokke\Downloads")

SECTIONS = [
    "COVER_9LINE.md", "00A_APPEAL.md", "00B_ABSTRACT.md",
    "00_HEADER.md", "01_EXECUTIVE_SUMMARY.md",
    "02_SILOING.md", "03_POWER_MAP.md", "04_ACTIVE_INVESTIGATIONS.md",
    "05_BANKS_PRINCIPAL.md", "06_SABREE_DYNASTY.md", "07_BMF_NEXUS.md",
    "08_JUDGES.md", "09_COURT_CAPTURE.md", "10_OMBUDSMAN_DAGNOGO.md",
    "11_DARK_MONEY.md", "12_CHARTER_ENTERPRISE.md",
    "13_EXTRACTION_GEOGRAPHY.md", "14_MAIL_FRAUD.md", "15_ENTITY_MAP.md",
    "16_MONEY_FLOW.md", "17_EVIDENCE_INDEX.md", "18_AGENCY_RECOMMENDATIONS.md",
]

EXHIBIT_PDFS = [
    ("brianBanksICHAT.pdf", "Banks ICHAT (9 convictions, 6 felony)"),
    ("show_temp (10).pdf", "Holland BK3 Full Petition + Schedules (14-51632) -- SCHEDULE A = NONE"),
    ("show_temp (9).pdf", "Holland BK3 Amended Schedule F ($117,149, 25 creditors)"),
    ("show_temp (7).pdf", "Holland BK1 Schedules A-J + SOFA (09-46072, 30pg)"),
    ("show_temp (5).pdf", "Holland BK1 Ch.13 Plan (09-46072)"),
    ("show_temp (6).pdf", "Holland BK1 Form 22C (09-46072)"),
    ("show_temp (8).pdf", "Holland BK1 Trustee Objection (09-46072)"),
    ("show_temp (4).pdf", "Banks BK Docket (97-45020) -- PRO SE, Judge Rhodes"),
    ("show_temp (3).pdf", "Holland BK2 Docket (14-46410) -- No docs filed"),
    ("show_temp (2).pdf", "Holland BK3 Cover Sheet (5 prior BKs listed)"),
    ("show_temp (1).pdf", "Holland BK3 Docket (14-51632)"),
    ("show_temp.pdf", "Holland BK1 Cover Sheet (09-46072)"),
    ("show_temp (11).pdf", "Holland BK3 Exhibit D (credit counseling)"),
]

FAX_NUMBERS = [
    ("3139652006", "FBI Detroit", "Federal Bureau of Investigation"),
    ("3132344055", "DEA Detroit", "Drug Enforcement Administration"),
    ("3132342505", "IRS CI Detroit", "IRS Criminal Investigation"),
    ("2022457047", "DOE OIG", "Dept of Education OIG"),
    ("3132263561", "USAO E.D. Mich", "US Attorney"),
    ("3132267952", "US Trustee Detroit", "US Trustee Region 9"),
    ("5172417074", "MI Attorney General", "Michigan AG"),
]

CSS = """
@page {
    size: letter;
    margin: 0.65in 0.7in 0.85in 0.7in;
    @frame footer_frame {
        -pdf-frame-content: page_footer;
        bottom: 0.2in;
        margin-left: 0.7in;
        margin-right: 0.7in;
        height: 0.4in;
    }
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 9pt;
    line-height: 1.35;
    color: #111;
}
h1 {
    font-size: 14pt; margin-top: 16pt; margin-bottom: 6pt;
    color: #000; border-bottom: 2pt solid #000; padding-bottom: 3pt;
    page-break-before: always;
}
h1.no-break { page-break-before: auto; }
h2 {
    font-size: 11.5pt; margin-top: 12pt; margin-bottom: 5pt;
    color: #111; border-bottom: 1pt solid #888; padding-bottom: 2pt;
}
h3 { font-size: 10pt; margin-top: 9pt; margin-bottom: 3pt; color: #222; }
h4 { font-size: 9pt; margin-top: 7pt; margin-bottom: 2pt; color: #333; }
table { width: 100%; margin: 5pt 0; border-collapse: collapse; }
th, td {
    border: 0.5pt solid #888; padding: 2pt 4pt;
    text-align: left; vertical-align: top; font-size: 8pt;
}
th { background-color: #d8d8d8; font-weight: bold; }
blockquote {
    border-left: 3pt solid #c00; padding: 4pt 0 4pt 8pt;
    margin: 6pt 0 6pt 4pt; color: #222; background-color: #fafafa;
}
code { font-family: Courier; font-size: 7.5pt; background-color: #eee; }
pre {
    background-color: #f0f0f0; padding: 5pt; border: 0.5pt solid #ccc;
    font-size: 7pt; font-family: Courier; white-space: pre-wrap;
}
hr { border: none; border-top: 1.5pt solid #000; margin: 10pt 0; }
strong { color: #000; }
ul, ol { margin: 2pt 0 2pt 0; padding-left: 14pt; }
li { margin-bottom: 1pt; }
a { color: #003; text-decoration: none; }
.cover-box {
    border: 2pt solid #000; padding: 12pt; margin: 8pt 0;
    text-align: center;
}
.section-label {
    font-size: 8pt; color: #666; margin-bottom: 2pt;
    text-transform: uppercase; letter-spacing: 1pt;
}
.page-footer {
    font-size: 7pt; color: #888; text-align: center;
    border-top: 0.5pt solid #ccc; padding-top: 3pt;
}
.toc-entry { margin: 2pt 0; font-size: 9pt; }
.toc-section { font-weight: bold; }
.exhibit-header {
    page-break-before: always; font-size: 14pt; font-weight: bold;
    text-align: center; padding: 20pt 0; border-bottom: 2pt solid #000;
}
"""


def clean_unicode(text):
    """Replace Unicode decorators with ASCII equivalents for PDF rendering."""
    replacements = {
        "\u2550": "=",   # ═
        "\u25ac": "-",   # ▬
        "\u2192": "->",  # →
        "\u2190": "<-",  # ←
        "\u2191": "^",   # ↑
        "\u2193": "v",   # ↓
        "\u2194": "<->", # ↔
        "\u2500": "-",   # ─
        "\u2502": "|",   # │
        "\u251c": "|",   # ├
        "\u25bc": "v",   # ▼
        "\u2264": "<=",  # ≤
        "\u2265": ">=",  # ≥
        "\u2605": "*",   # ★
        "\u2460": "(1)", # ①
        "\u2461": "(2)", # ②
        "\u2462": "(3)", # ③
        "\u2463": "(4)", # ④
        "\u2464": "(5)", # ⑤
        "\u2705": "[OK]",   # ✅
        "\u26a1": "[!]",    # ⚡
        "\u26a0\ufe0f": "[WARNING]",  # ⚠️
        "\u26a0": "[WARNING]",  # ⚠
        "\U0001f525": "[CRITICAL]",  # 🔥
        "\U0001f534": "[OPEN]",      # 🔴
        "\U0001f7e1": "[PENDING]",   # 🟡
        "\ufeff": "",    # BOM
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def fix_cover_9line(md_text):
    """Transform the 9-LINE cover from markdown-comment style to proper headers."""
    lines = md_text.split("\n")
    new_lines = []
    in_cover = True
    for line in lines:
        if in_cover and line.startswith("# ") and not line.startswith("## "):
            content = line[2:].strip()
            if all(c in "=-_ " for c in content) and len(content) > 10:
                new_lines.append("---")
            elif content.startswith('"') or "FEDERAL" in content or "Cash for" in content:
                new_lines.append(f"**{content}**")
                new_lines.append("")
            else:
                new_lines.append(f"*{content}*")
                new_lines.append("")
        else:
            if line.startswith("## ") and in_cover:
                in_cover = False
            new_lines.append(line)
    return "\n".join(new_lines)


def build_section_html(section_file, section_num):
    """Convert one section MD to HTML with section divider."""
    md_text = section_file.read_text(encoding="utf-8")
    md_text = clean_unicode(md_text)

    if section_file.name == "COVER_9LINE.md":
        md_text = fix_cover_9line(md_text)

    html = markdown2.markdown(
        md_text,
        extras=["tables", "fenced-code-blocks", "strike",
                "task_list", "cuddled-lists", "header-ids"]
    )
    return html


def build_toc_html():
    """Build a Table of Contents page."""
    toc_entries = [
        ("Cover", "9-LINE Federal Referral"),
        ("Appeal", "A Note to Federal Prosecutors"),
        ("Abstract", "Synopsis -- Targets, Statutes, Evidence"),
        ("Header", "Packet Header and Sender"),
        ("1", "Executive Summary -- The Network in One Page"),
        ("2", "HOW SILOING ENABLED THIS"),
        ("3", "POWER MAP -- Institutional Power"),
        ("4", "Active Investigations and Prosecutorial Angles"),
        ("5", "The Principal: Brian Roderick Banks (9 convictions)"),
        ("6", "The Sabree Dynasty (Active Federal Litigation)"),
        ("7", "BMF/Drug Nexus -- Two Published Confessions"),
        ("8", "The Bench: Judges Who Knew and Didn't Report"),
        ("9", "Court Capture: 50,000-Case Backlog"),
        ("10", "The Ombudsman Problem: Dagnogo's Golden Parachute"),
        ("11", "Dark Money Pipeline"),
        ("12", "Charter School Enterprise"),
        ("13", "Extraction Geography -- Every Dollar Leaves Detroit"),
        ("14", "Mail Fraud and Obstruction (USPS OIG)"),
        ("15", "Entity Map -- All Known Entities"),
        ("16", "Money Flow Diagram"),
        ("17", "Evidence Index and Exhibits (A-M)"),
        ("18", "Recommendations by Agency"),
    ]

    html = '<h1 class="no-break">TABLE OF CONTENTS</h1>\n'
    html += '<p style="font-size:8pt;color:#666;">Each section begins on a new page for easy reference.</p>\n'
    html += '<table style="width:100%;border:none;">\n'
    html += '<tr><th style="width:12%;border:none;">Section</th><th style="border:none;">Title</th></tr>\n'
    for num, title in toc_entries:
        style = 'font-weight:bold;' if num in ('Cover', '1', '5', '7', '18') else ''
        html += f'<tr><td style="border:none;{style}">{num}</td><td style="border:none;{style}">{title}</td></tr>\n'

    html += '</table>\n'
    html += '<br/><h2>EXHIBITS (attached after Section 18)</h2>\n'
    html += '<table style="width:100%;">\n'
    html += '<tr><th>Exhibit</th><th>Description</th><th>Pages</th></tr>\n'

    for i, (fname, desc) in enumerate(EXHIBIT_PDFS):
        letter = chr(65 + i)
        fpath = DOWNLOADS / fname
        pages = "?"
        if fpath.exists():
            try:
                pages = str(len(PdfReader(str(fpath)).pages))
            except Exception:
                pass
        html += f'<tr><td>{letter}</td><td>{desc}</td><td>{pages}</td></tr>\n'

    html += '</table>\n'
    html += '<p style="font-size:8pt;"><strong>All exhibits are public records</strong> obtained from PACER (pacer.gov) and Michigan ICHAT (apps.michigan.gov/ichat) on September 20, 2026.</p>\n'
    return html


def build_full_html():
    """Build the complete HTML document."""
    all_sections_html = []

    for i, sec_name in enumerate(SECTIONS):
        sec_path = PACKET_DIR / sec_name
        sec_html = build_section_html(sec_path, i)

        if i == 0:
            wrapper = f'<div>{sec_html}</div>'
        elif i == 1:
            toc = build_toc_html()
            wrapper = f'<div style="page-break-before:always;">{sec_html}</div>\n{toc}'
        else:
            wrapper = f'<div style="page-break-before:always;">{sec_html}</div>'

        all_sections_html.append(wrapper)

    body = "\n".join(all_sections_html)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
{body}
<div id="page_footer">
    <div class="page-footer">
        FEDERAL REFERRAL -- Cash for Kids 2: Operation Detroit Plantation -- Kevin Mok -- September 22, 2026
    </div>
</div>
</body>
</html>"""
    return full_html


def render_pdf(html_str, out_path):
    """Render HTML to PDF via xhtml2pdf."""
    with open(str(out_path), "wb") as f:
        status = pisa.CreatePDF(html_str, dest=f, encoding="utf-8")
    if status.err:
        print(f"  [!] {status.err} rendering warnings")
    reader = PdfReader(str(out_path))
    kb = out_path.stat().st_size // 1024
    print(f"  PDF: {out_path.name} -- {len(reader.pages)} pages, {kb} KB")
    return out_path


def build_exhibit_separator(letter, desc):
    """Build a one-page exhibit separator/divider."""
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{CSS}
.sep {{ text-align: center; padding-top: 200pt; }}
.sep h1 {{ border: none; page-break-before: auto; font-size: 24pt; }}
.sep h2 {{ border: none; font-size: 14pt; color: #444; }}
</style></head><body>
<div class="sep">
<h1 class="no-break">EXHIBIT {letter}</h1>
<h2>{desc}</h2>
<p style="font-size:9pt;color:#888;margin-top:20pt;">Source: PACER / Michigan ICHAT -- Public Record<br/>
Pulled September 20, 2026</p>
</div>
</body></html>"""
    buf = BytesIO()
    pisa.CreatePDF(html, dest=buf, encoding="utf-8")
    buf.seek(0)
    return PdfReader(buf)


def merge_final():
    """Build text PDF, then merge with exhibit separators + exhibit PDFs."""
    print("=" * 60)
    print("BUILDING FEDERAL PACKET PDF v2")
    print("=" * 60)

    full_html = build_full_html()

    html_path = DEPLOY / "FEDERAL_PACKET_SEP22.html"
    html_path.write_text(full_html, encoding="utf-8")
    print(f"  HTML saved: {html_path.name}")

    text_pdf = DEPLOY / "FEDERAL_PACKET_SEP22_TEXT.pdf"
    render_pdf(full_html, text_pdf)

    writer = PdfWriter()

    text_reader = PdfReader(str(text_pdf))
    for page in text_reader.pages:
        writer.add_page(page)
    text_pages = len(text_reader.pages)
    print(f"\n  + Packet text: {text_pages} pages")

    exhibit_pages = 0
    for i, (fname, desc) in enumerate(EXHIBIT_PDFS):
        letter = chr(65 + i)
        fpath = DOWNLOADS / fname

        sep_reader = build_exhibit_separator(letter, desc)
        for page in sep_reader.pages:
            writer.add_page(page)

        if fpath.exists():
            try:
                reader = PdfReader(str(fpath))
                for page in reader.pages:
                    writer.add_page(page)
                n = len(reader.pages)
                exhibit_pages += n + 1
                print(f"  + Exhibit {letter}: {desc[:50]}... ({n} pages)")
            except Exception as e:
                print(f"  ! SKIP {fname}: {e}")
                exhibit_pages += 1
        else:
            print(f"  ! MISSING: {fname}")
            exhibit_pages += 1

    fax_pdf = DEPLOY / "FEDERAL_PACKET_SEP22_COMPLETE.pdf"
    with open(str(fax_pdf), "wb") as f:
        writer.write(f)

    total = len(writer.pages)
    mb = fax_pdf.stat().st_size / (1024 * 1024)

    print(f"\n{'=' * 60}")
    print(f"COMPLETE FAX PDF: {fax_pdf}")
    print(f"  Text:     {text_pages} pages")
    print(f"  Exhibits: {exhibit_pages} pages (13 exhibits with separators)")
    print(f"  TOTAL:    {total} pages")
    print(f"  Size:     {mb:.1f} MB")
    print(f"{'=' * 60}")

    pages_per_fax = total
    num_agencies = 7
    total_fax_pages = pages_per_fax * num_agencies
    print(f"\n  FAX MATH: {pages_per_fax} pages x {num_agencies} agencies = {total_fax_pages} pages")
    print(f"  Credits needed: {total_fax_pages}")
    print(f"  Credits owned:  800")
    if total_fax_pages > 800:
        extra = total_fax_pages - 800
        print(f"  SHORTFALL:      {extra} pages -- buy more credits")
        if extra <= 100:
            print(f"  Recommendation: Buy 100 pages ($9.95)")
        elif extra <= 250:
            print(f"  Recommendation: Buy 250 pages ($19.95)")
        else:
            print(f"  Recommendation: Buy 800 pages ($49.95)")

    return fax_pdf


def build_broadcast_csv():
    """Build GotFreeFax broadcast CSV."""
    csv_path = DEPLOY / "fax_broadcast_list.csv"
    with open(str(csv_path), "w", newline="") as f:
        for fax_num, short_name, full_name in FAX_NUMBERS:
            f.write(f"{fax_num}, {short_name}, {full_name}\n")
    print(f"\n  Broadcast CSV: {csv_path}")
    print(f"  {len(FAX_NUMBERS)} recipients:")
    for fax_num, short_name, _ in FAX_NUMBERS:
        print(f"    {fax_num}  {short_name}")
    return csv_path


if __name__ == "__main__":
    merge_final()
    build_broadcast_csv()
