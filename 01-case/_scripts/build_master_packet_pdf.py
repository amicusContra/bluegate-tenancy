"""
Convert FEDERAL_MASTER_PACKET_SEP18.md to a print-ready PDF.
Uses reportlab for clean, professional formatting.
Handles headers, tables, blockquotes, bold, code blocks, and bullets.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.colors import HexColor

PROJECT = r"C:\Users\mokke\jobHunt\bluegate-tenancy"
INPUT_MD = os.path.join(PROJECT, "01-case", "filing-ready", "FEDERAL_MASTER_PACKET_SEP18.md")
OUTPUT_PDF = os.path.join(PROJECT, "01-case", "filing-ready", "FEDERAL_MASTER_PACKET_SEP18.pdf")

PAGE_W, PAGE_H = letter
MARGIN = 0.7 * inch

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    'PacketTitle', parent=styles['Title'],
    fontSize=16, leading=20, alignment=TA_CENTER,
    spaceAfter=6, textColor=HexColor('#1a1a1a'),
    fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'PacketSubtitle', parent=styles['Normal'],
    fontSize=10, leading=13, alignment=TA_CENTER,
    spaceAfter=4, textColor=HexColor('#333333')
))
styles.add(ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontSize=14, leading=18, spaceBefore=18, spaceAfter=8,
    textColor=HexColor('#000000'), fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'H2', parent=styles['Heading2'],
    fontSize=12, leading=16, spaceBefore=14, spaceAfter=6,
    textColor=HexColor('#1a1a1a'), fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'H3', parent=styles['Heading3'],
    fontSize=10, leading=14, spaceBefore=10, spaceAfter=4,
    textColor=HexColor('#333333'), fontName='Helvetica-Bold'
))
styles.add(ParagraphStyle(
    'BodyText2', parent=styles['Normal'],
    fontSize=9, leading=12, alignment=TA_JUSTIFY,
    spaceAfter=4, textColor=HexColor('#1a1a1a')
))
styles.add(ParagraphStyle(
    'BlockQuote', parent=styles['Normal'],
    fontSize=9, leading=12, leftIndent=24, rightIndent=12,
    spaceAfter=6, spaceBefore=4,
    textColor=HexColor('#333333'), fontName='Helvetica-Oblique',
    borderColor=HexColor('#999999'), borderWidth=0, borderPadding=4
))
styles.add(ParagraphStyle(
    'BulletItem', parent=styles['Normal'],
    fontSize=9, leading=12, leftIndent=20, bulletIndent=8,
    spaceAfter=2, textColor=HexColor('#1a1a1a')
))
styles.add(ParagraphStyle(
    'CodeBlock', parent=styles['Normal'],
    fontSize=7.5, leading=10, leftIndent=12,
    spaceAfter=6, spaceBefore=4,
    fontName='Courier', textColor=HexColor('#1a1a1a'),
    backColor=HexColor('#f5f5f5')
))
styles.add(ParagraphStyle(
    'TableCell', parent=styles['Normal'],
    fontSize=7.5, leading=10, textColor=HexColor('#1a1a1a')
))
styles.add(ParagraphStyle(
    'TableHeader', parent=styles['Normal'],
    fontSize=7.5, leading=10, fontName='Helvetica-Bold',
    textColor=HexColor('#ffffff')
))
styles.add(ParagraphStyle(
    'Footer', parent=styles['Normal'],
    fontSize=7, leading=9, alignment=TA_CENTER,
    textColor=HexColor('#666666')
))


def clean_md_inline(text):
    """Convert markdown inline formatting to reportlab XML tags."""
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`', r'<font face="Courier" size="8">\1</font>', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def parse_table(lines):
    """Parse markdown table lines into a reportlab Table."""
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)

    if len(rows) < 2:
        return None

    if all(set(c.strip()) <= set('-: ') for c in rows[1]):
        rows.pop(1)

    table_data = []
    for i, row in enumerate(rows):
        style_name = 'TableHeader' if i == 0 else 'TableCell'
        table_data.append([
            Paragraph(clean_md_inline(cell), styles[style_name])
            for cell in row
        ])

    if not table_data:
        return None

    num_cols = max(len(r) for r in table_data)
    for r in table_data:
        while len(r) < num_cols:
            r.append(Paragraph('', styles['TableCell']))

    avail_w = PAGE_W - 2 * MARGIN
    col_w = avail_w / num_cols

    t = Table(table_data, colWidths=[col_w] * num_cols, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HexColor('#f8f9fa')]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    return t


def add_page_number(canvas_obj, doc):
    """Add page number and confidential footer."""
    canvas_obj.saveState()
    canvas_obj.setFont('Helvetica', 7)
    canvas_obj.setFillColor(HexColor('#666666'))
    canvas_obj.drawCentredString(
        PAGE_W / 2, 0.4 * inch,
        f"CASH FOR KIDS 2: OPERATION DETROIT PLANTATION — Page {doc.page}"
    )
    canvas_obj.drawString(
        MARGIN, 0.4 * inch,
        "Kevin Mok | (517) 420-8938"
    )
    canvas_obj.drawRightString(
        PAGE_W - MARGIN, 0.4 * inch,
        "September 22, 2026"
    )
    canvas_obj.restoreState()


def build_pdf():
    print(f"Reading: {INPUT_MD}")
    with open(INPUT_MD, 'r', encoding='utf-8') as f:
        md_lines = f.readlines()

    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.6 * inch, bottomMargin=0.6 * inch
    )

    story = []
    i = 0
    in_code_block = False
    code_lines = []
    in_table = False
    table_lines = []

    while i < len(md_lines):
        line = md_lines[i].rstrip('\n')

        if line.startswith('```'):
            if in_code_block:
                code_text = '<br/>'.join(
                    ln.replace(' ', '&nbsp;') for ln in code_lines
                )
                story.append(Paragraph(code_text, styles['CodeBlock']))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            safe = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            code_lines.append(safe)
            i += 1
            continue

        is_table_line = bool(re.match(r'^\s*\|', line))
        if is_table_line:
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            t = parse_table(table_lines)
            if t:
                story.append(Spacer(1, 4))
                story.append(t)
                story.append(Spacer(1, 4))
            in_table = False
            table_lines = []

        stripped = line.strip()

        if not stripped:
            story.append(Spacer(1, 4))
            i += 1
            continue

        if stripped == '---':
            story.append(HRFlowable(
                width="100%", thickness=0.5,
                color=HexColor('#cccccc'), spaceAfter=6, spaceBefore=6
            ))
            i += 1
            continue

        if stripped.startswith('# ') and not stripped.startswith('## '):
            text = clean_md_inline(stripped[2:])
            story.append(Paragraph(text, styles['PacketTitle']))
            i += 1
            continue

        if stripped.startswith('## '):
            text = clean_md_inline(stripped[3:])
            story.append(Spacer(1, 8))
            story.append(Paragraph(text, styles['H1']))
            i += 1
            continue

        if stripped.startswith('### '):
            text = clean_md_inline(stripped[4:])
            story.append(Paragraph(text, styles['H2']))
            i += 1
            continue

        if stripped.startswith('#### '):
            text = clean_md_inline(stripped[5:])
            story.append(Paragraph(text, styles['H3']))
            i += 1
            continue

        if stripped.startswith('> '):
            text = clean_md_inline(stripped[2:])
            story.append(Paragraph(text, styles['BlockQuote']))
            i += 1
            continue

        if stripped.startswith('- ') or stripped.startswith('* '):
            text = clean_md_inline(stripped[2:])
            story.append(Paragraph(
                f'<bullet>&bull;</bullet> {text}',
                styles['BulletItem']
            ))
            i += 1
            continue

        if re.match(r'^\d+\.\s', stripped):
            num_match = re.match(r'^(\d+)\.\s(.+)', stripped)
            if num_match:
                num = num_match.group(1)
                text = clean_md_inline(num_match.group(2))
                story.append(Paragraph(
                    f'<b>{num}.</b> {text}',
                    styles['BulletItem']
                ))
            i += 1
            continue

        text = clean_md_inline(stripped)
        story.append(Paragraph(text, styles['BodyText2']))
        i += 1

    if in_table and table_lines:
        t = parse_table(table_lines)
        if t:
            story.append(t)

    print(f"Building PDF with {len(story)} elements...")
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

    size_kb = os.path.getsize(OUTPUT_PDF) / 1024
    print(f"PDF created: {OUTPUT_PDF}")
    print(f"Size: {size_kb:.1f} KB ({size_kb/1024:.2f} MB)")
    print("Done!")


if __name__ == '__main__':
    build_pdf()
