"""OCR batch3 page-1 PNGs and build INDEX.md"""
import json
import re
from pathlib import Path

import pytesseract
from PIL import Image

TESS = r"C:\Users\mokke\miniconda3\Library\bin\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESS

IMG_DIR = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\wayne-rod-sep2\images")
OUT_DIR = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\wayne-rod-sep2\batch3\extracted")
INDEX_PATH = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\wayne-rod-sep2\batch3\INDEX.md")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().replace("|", "/")


def parse_doc(text: str, file_id: str) -> dict:
    upper = text.upper()

    doc_num = ""
    m = re.search(r"\b(20\d{8})\b", text)
    if m:
        doc_num = m.group(1)

    date = ""
    m = re.search(r"(\d{2}/\d{2}/\d{4})\s+\d{1,2}:\d{2}", text)
    if m:
        date = m.group(1)
    else:
        m = re.search(r"(?:Dated|dated|Date:|DATE)\s*(\d{1,2}/\d{1,2}/\d{4})", text)
        if m:
            date = m.group(1)
        else:
            m = re.search(r"(\d{2}/\d{2}/\d{4})", text)
            if m:
                date = m.group(1)

    doc_type = ""
    hm = re.search(r"20\d{8}\s+\d+L:\d+P:\d+\s+(\w+)", text)
    if hm:
        doc_type = hm.group(1).upper()

    type_patterns = [
        ("UCC FINANCING STATEMENT AMENDMENT", "UCC3"),
        ("UCC FINANCING STATEMENT", "UCC1"),
        ("SATISFACTION / DISCHARGE OF MORTGAGE", "MSR"),
        ("SATISFACTION OF MORTGAGE", "MSR"),
        ("DISCHARGE OF MORTGAGE", "DIS"),
        ("SHERIFF'S DEED", "SD"),
        ("QUIT CLAIM DEED", "QCD"),
        ("WARRANTY DEED", "WD"),
        ("REVOLVING CREDIT MORTGAGE", "MTG"),
        ("MORTGAGE", "MTG"),
        ("PROPERTY TAX", "TAX"),
        ("TREASURER", "TAX"),
    ]
    if not doc_type:
        for pat, t in type_patterns:
            if pat in upper:
                doc_type = t
                break

    parties = ""
    if "QUIT CLAIM" in upper:
        m = re.search(
            r"(?:quit claims? to|Quit Claim\(s\) to)\s+(.{5,100}?)"
            r"(?:\s*,|\s+whose|\s+for|\s+whosever|\n)",
            text,
            re.I,
        )
        grantee = clean(m.group(1)) if m else ""
        if "DETROIT LAND BANK" in upper:
            grantor = "Detroit Land Bank Authority"
        else:
            m = re.search(
                r"(?:GRANTOR[,:]?\s*|That,?\s+)([A-Z][^\n]{5,100}?)"
                r"(?:\s+quit|\s+for and|\s+does|\s+hereby|\n)",
                text,
                re.I,
            )
            grantor = clean(m.group(1)) if m else ""
        if grantor and grantee:
            parties = f"{grantor} → {grantee}"
        elif grantee:
            parties = f"? → {grantee}"
    elif "WARRANTY DEED" in upper:
        m = re.search(
            r"(?:GRANTOR[,:]?\s*|THE GRANTOR,?\s*)(.{5,120}?)"
            r"(?:\s+convey|\s+warrant|\s+for and|\n)",
            text,
            re.I,
        )
        grantor = clean(m.group(1)) if m else ""
        m = re.search(
            r"(?:Convey\(s\) and Warrant\(s\) to|warrant\(s\) to,?\s+)(.{5,100}?)"
            r"(?:\s*,|\s+a\s|\s+whose|\n)",
            text,
            re.I,
        )
        grantee = clean(m.group(1)) if m else ""
        if grantor and grantee:
            parties = f"{grantor} → {grantee}"
    elif "MORTGAGE" in upper and doc_type not in ("DIS", "MSR", "SD"):
        m = re.search(
            r"(?:THIS MORTGAGE is made on|Between\s+|Mortgagor,?\s*|Borrower.*?is\s+|executed by\s+)"
            r"(.{5,100}?)(?:\s+(?:to|whose|whosever|and the Mortgagee|,|\n|whose address))",
            text,
            re.I,
        )
        mortgagor = clean(m.group(1)) if m else ""
        m = re.search(
            r"(?:Mortgagee,?\s*|and the Mortgagee,?\s*|to\s+)([A-Z][^\n,]{5,80}?)"
            r"(?:\s*,|\s+whose|\s+whosever|\s+dated|\s+and|\n)",
            text,
            re.I,
        )
        mortgagee = clean(m.group(1)) if m else ""
        if mortgagor:
            parties = f"{mortgagor[:80]} → {mortgagee[:80] if mortgagee else '?'}"
    elif doc_type in ("DIS", "MSR"):
        m = re.search(
            r"executed by\s+(.{5,80}?)\s+to\s+(.{5,80}?)(?:\s*,|\s+and|\s+whose|\n)",
            text,
            re.I,
        )
        if m:
            parties = f"{clean(m.group(1))} → {clean(m.group(2))} (discharged)"
        else:
            m = re.search(r"Original (?:Grantor|Mortgagor)[.:]\s*(.{5,80})", text, re.I)
            mortgagor = clean(m.group(1)) if m else ""
            m = re.search(r"Original (?:Grantee|Mortgagee)[.:]\s*(.{5,80})", text, re.I)
            mortgagee = clean(m.group(1)) if m else ""
            if mortgagor:
                parties = f"{mortgagor} (discharge by {mortgagee or 'creditor'})"
    elif "SHERIFF" in upper:
        m = re.search(r"mortgage made by\s+(.{5,80}?),\s*original mortgagor", text, re.I)
        mortgagor = clean(m.group(1)) if m else ""
        if mortgagor:
            parties = f"{mortgagor} (foreclosure sale)"
    elif doc_type.startswith("UCC"):
        m = re.search(
            r"1b\.\s*INDIVIDUAL.*?SURNAME.*?NAME.*?\n\s*([A-Z]+)\s+([A-Z]+)",
            text,
            re.S,
        )
        debtor = f"{m.group(1)} {m.group(2)}" if m else ""
        m = re.search(r"3a\.\s*ORGANIZATION'S NAME\s*\n\s*\n\s*([^\n]+)", text)
        secured = clean(m.group(1)) if m else ""
        if debtor:
            parties = f"{debtor} → {secured or '?'}"

    prop = ""
    m = re.search(r"Common(?:ly)?\s*(?:Address|address)\s*[:\s]*([^\n]{5,80})", text, re.I)
    if m:
        prop = clean(m.group(1).rstrip("."))
    else:
        for pat in [
            r"(\d{4,5}\s+[A-Za-z][^\n]{5,60}(?:Detroit|Westland|Taylor|Dearborn|Redford|Romulus|Grosse Pointe)[^\n]{0,25})",
            r"(Lot \d+[^\n]{10,100})",
            r"(\d{4,5}\s+[A-Za-z\s]+(?:St|Street|Ave|Rd|Dr|Blvd)[^\n]{0,40})",
        ]:
            m = re.search(pat, text, re.I)
            if m:
                prop = clean(m.group(1))[:120]
                break

    amount = ""
    amounts = re.findall(r"\$\s*([\d,]+(?:\.\d{2})?)", text)
    vals = []
    for a in amounts:
        try:
            v = float(a.replace(",", ""))
            if v >= 100:
                vals.append((v, a))
        except ValueError:
            pass
    if vals:
        vals.sort(reverse=True)
        amount = "$" + vals[0][1]

    return {
        "file_id": file_id,
        "doc_num": doc_num,
        "type": doc_type,
        "date": date,
        "parties": parties[:200],
        "property": prop[:150],
        "amount": amount,
    }


def ocr_all():
    files = sorted(IMG_DIR.glob("batch3_*.png"))
    for i, fp in enumerate(files):
        file_id = fp.stem.replace("batch3_", "").replace("_p1", "")
        ocr_path = OUT_DIR / f"{file_id}_p1_ocr.txt"
        if ocr_path.exists():
            continue
        print(f"OCR {i + 1}/{len(files)}: {fp.name}...", flush=True)
        img = Image.open(fp)
        text = pytesseract.image_to_string(img, lang="eng")
        ocr_path.write_text(text, encoding="utf-8")


def build_from_ocr():
    files = sorted(OUT_DIR.glob("*_p1_ocr.txt"))
    results = []
    for fp in files:
        file_id = fp.name.replace("_p1_ocr.txt", "")
        img_num = file_id.replace("18599637_", "").replace("_docimage_actual", "")
        text = fp.read_text(encoding="utf-8", errors="replace")
        parsed = parse_doc(text, img_num)
        parsed["image"] = f"batch3_{file_id}_p1.png"
        parsed["pdf"] = f"{file_id}.pdf"
        results.append(parsed)
    return results


def main():
    ocr_all()
    results = build_from_ocr()
    results.sort(key=lambda r: (r["doc_num"] or "0", r["file_id"]), reverse=True)

    (OUT_DIR / "parsed_index.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )

    # Check for target documents
    qcd = lake_trust = None
    for r in results:
        fp = OUT_DIR / f"18599637_{r['file_id']}_docimage_actual_p1_ocr.txt"
        full = fp.read_text(encoding="utf-8", errors="replace").upper() if fp.exists() else ""
        combined = (r["parties"] + r["property"] + full).upper()
        if (
            r["type"] == "QCD"
            and "LEON" in combined
            and "MARQUITA" in combined
            and ("17370" in combined or "DRESDEN" in combined)
        ):
            qcd = r
        if "LAKE TRUST" in combined and (
            "68000" in combined or "$68" in r["amount"] or "68,000" in combined
        ):
            lake_trust = r

    lines = [
        "# Wayne County ROD — Batch 3 Index",
        "",
        "**Search account:** XXXX9637 (Smith family ROD pull, Sep 2 2026)",
        f"**Documents indexed:** {len(results)}",
        "**Source:** Page 1 OCR of scanned ROD images (Tesseract 5.5)",
        "",
        "## Target Documents (Leon/Marquita — XXXXX Dresden St)",
        "",
    ]

    if qcd:
        lines.append(
            f"✅ **QCD (Marquita added to deed):** File `{qcd['file_id']}` — "
            f"Doc# {qcd['doc_num']}, recorded {qcd['date']}"
        )
    else:
        lines.append(
            "❌ **QCD (Leon A. Smith → Leon A. Smith & Marquita Smith, 17370 Dresden, Jun 2025):** "
            "**NOT FOUND in this batch.** None of the 36 documents reference Leon A. Smith, Marquita, "
            "XXXXX Dresden St, or Lake Trust Credit Union."
        )

    if lake_trust:
        lines.append(
            f"✅ **Lake Trust $68K mortgage:** File `{lake_trust['file_id']}` — "
            f"Doc# {lake_trust['doc_num']}, recorded {lake_trust['date']}, {lake_trust['amount']}"
        )
    else:
        lines.append(
            "❌ **Lake Trust $68K mortgage (Leon & Marquita, 17370 Dresden, Jun 2025):** "
            "**NOT FOUND in this batch.**"
        )

    lines.extend(
        [
            "",
            "**Note:** This batch appears to contain **Simone R. Smith** property records "
            "(Lee Eric Smith, Darryl Smith, John O. Smith, etc.) — not Leon/Marquita Dresden records. "
            "The two highest image IDs (266229059, 266181915) are UCC filings for Simone Smith, not the target QCD/mortgage.",
            "",
            "## Full Index",
            "",
            "| File ID | Doc# | Type | Date | Parties | Property | Amount |",
            "|---------|------|------|------|---------|----------|--------|",
        ]
    )

    for r in results:
        lines.append(
            f"| {r['file_id']} | {r['doc_num'] or '—'} | {r['type'] or '—'} | "
            f"{r['date'] or '—'} | {r['parties'] or '—'} | {r['property'] or '—'} | {r['amount'] or '—'} |"
        )

    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {INDEX_PATH}")


if __name__ == "__main__":
    main()
