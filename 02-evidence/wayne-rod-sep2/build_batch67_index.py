"""OCR batch6_miller / batch7_yancey page-1 PNGs and build INDEX.md for each."""
import json
import re
from pathlib import Path

import pytesseract
from PIL import Image

TESS = r"C:\Users\mokke\miniconda3\Library\bin\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESS

BASE = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\wayne-rod-sep2")
IMG_DIR = BASE / "images"

BATCHES = {
    "batch6_miller": {
        "prefix": "batch6_miller",
        "account": "XXXX8653",
        "subject": "Judge Cylenthia LaToye Miller",
        "out_dir": BASE / "batch6_miller" / "extracted",
        "index_path": BASE / "batch6_miller" / "INDEX.md",
    },
    "batch7_yancey": {
        "prefix": "batch7_yancey",
        "account": "XXXX8663",
        "subject": "Judge Tenisha R. Yancey",
        "out_dir": BASE / "batch7_yancey" / "extracted",
        "index_path": BASE / "batch7_yancey" / "INDEX.md",
    },
}


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
    hm2 = re.search(
        r"\b(COF|COR|QCD|WD|MTG|DIS|MSR|SD|UCC1|UCC3|IRS|ASG|AFF|LIS|POA|JDG|ORD|LIS)\b",
        upper,
    )
    if hm2 and (not doc_type or doc_type == "TAX"):
        doc_type = hm2.group(1)

    type_patterns = [
        ("UCC FINANCING STATEMENT AMENDMENT", "UCC3"),
        ("UCC FINANCING STATEMENT", "UCC1"),
        ("ASSIGNMENT OF MORTGAGE", "ASG"),
        ("SATISFACTION PIECE", "DIS"),
        ("SATISFACTION / DISCHARGE OF MORTGAGE", "MSR"),
        ("SATISFACTION OF MORTGAGE", "MSR"),
        ("DISCHARGE OF MORTGAGE", "DIS"),
        ("SHERIFF'S DEED", "SD"),
        ("QUIT CLAIM DEED", "QCD"),
        ("QUITCLAIM DEED", "QCD"),
        ("WARRANTY DEED", "WD"),
        ("REVOLVING CREDIT MORTGAGE", "MTG"),
        ("MORTGAGE", "MTG"),
        ("CERTIFICATE OF FORFEITURE", "COF"),
        ("CERTIFICATE OF REDEMPTION", "COR"),
        ("NOTICE OF FEDERAL TAX LIEN", "IRS"),
        ("RELEASE OF FEDERAL TAX LIEN", "IRS"),
        ("AFFIDAVIT", "AFF"),
        ("LIS PENDENS", "LIS"),
        ("POWER OF ATTORNEY", "POA"),
        ("JUDGMENT", "JDG"),
        ("PROPERTY TAX", "TAX"),
        ("TREASURER", "TAX"),
        ("DEED", "DD"),
    ]
    if not doc_type or doc_type == "TAX":
        for pat, t in type_patterns:
            if pat in upper:
                doc_type = t
                break

    parties = ""
    if "QUIT CLAIM" in upper or "QUITCLAIM" in upper or doc_type == "QCD":
        m = re.search(
            r"(?:Quit-claims to Grantee\(s\):|quit claims? to|Quit Claim\(s\) to|QUITCLAIMS TO)\s+(.{5,120}?)"
            r"(?:\s*,|\s+whose|\s+Whose|\s+for|\s+whosever|\n)",
            text,
            re.I,
        )
        grantee = clean(m.group(1)) if m else ""
        if "DETROIT LAND BANK" in upper:
            grantor = "Detroit Land Bank Authority"
        else:
            m = re.search(
                r"(?:Grantor\(s\):|GRANTOR[,:]?\s*|That,?\s+|PRESENTS THAT\s+)(.{5,100}?)"
                r"(?:\s+quit|\s+Whose|\s+WHOSE|\s+for and|\s+does|\s+hereby|\n)",
                text,
                re.I,
            )
            grantor = clean(m.group(1)) if m else ""
        if grantor and grantee:
            parties = f"{grantor} → {grantee}"
        elif grantee:
            parties = f"? → {grantee}"
        elif grantor:
            parties = grantor
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
    elif "MORTGAGE" in upper and doc_type not in ("DIS", "MSR", "SD", "ASG"):
        m = re.search(
            r"(?:THIS MORTGAGE is made on[^,]*,\s*Between the Mortgagor,\s*|THIS MORTGAGE is made on[^,]*,\s*between the Mortgagor,\s*)"
            r"(.{5,100}?)(?:\s+whose address|\s+whose marital|\n)",
            text,
            re.I,
        )
        if not m:
            m = re.search(
                r"(?:THIS MORTGAGE is made on|Between\s+|Mortgagor,?\s*|Borrower\(s\):\s*|executed by\s+)"
                r"(.{5,100}?)(?:\s+(?:to|whose|whosever|and the Mortgagee|,|\n|whose address))",
                text,
                re.I,
            )
        mortgagor = clean(m.group(1)) if m else ""
        m = re.search(
            r"(?:and the Mortgagee,\s*|Mortgagee,?\s*)([A-Z][^\n,]{5,80}?)"
            r"(?:\s*,|\s+whose|\s+a corporation|\s+whosever|\s+dated|\s+and|\n)",
            text,
            re.I,
        )
        if not m:
            m = re.search(
                r"(?:Mortgagee,?\s*|to\s+)([A-Z][^\n,]{5,80}?)"
                r"(?:\s*,|\s+whose|\s+whosever|\s+dated|\s+and|\n)",
                text,
                re.I,
            )
        mortgagee = clean(m.group(1)) if m else ""
        if mortgagor:
            parties = f"{mortgagor[:80]} → {mortgagee[:80] if mortgagee else '?'}"
    elif doc_type == "ASG":
        m = re.search(r"Borrower\(s\):\s*(.{5,100}?)(?:\n|Date of Mortgage)", text, re.I)
        mortgagor = clean(m.group(1)) if m else ""
        m = re.search(r"Original Lender:\s*(.{5,80})", text, re.I)
        assignor = clean(m.group(1)) if m else ""
        if mortgagor:
            parties = f"{mortgagor} (assignment by {assignor or 'holder'})"
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

    prop = ""
    m = re.search(r"Common(?:ly)?\s*(?:Address|address)\s*[:\s]*([^\n]{5,80})", text, re.I)
    if m:
        prop = clean(m.group(1).rstrip("."))
    else:
        for pat in [
            r"(\d{4,5}\s+[A-Za-z][^\n]{5,60}(?:Detroit|Westland|Taylor|Dearborn|Redford|Romulus|Grosse Pointe|Harper Woods|Eastpointe|Roseville|Southfield|Livonia|Farmington|Inkster|Highland Park)[^\n]{0,25})",
            r"(Lot \d+[^\n]{10,100})",
            r"(\d{4,5}\s+[A-Za-z\s]+(?:St|Street|Ave|Rd|Dr|Blvd|Lane|Way|Court|Ct)[^\n]{0,40})",
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

    notes = detect_notes(text, upper, parties, prop, doc_type)

    return {
        "file_id": file_id,
        "doc_num": doc_num,
        "type": doc_type,
        "date": date,
        "parties": parties[:200],
        "property": prop[:150],
        "amount": amount,
        "notes": notes,
    }


def detect_notes(text: str, upper: str, parties: str, prop: str, doc_type: str) -> str:
    notes = []
    sovereign_patterns = [
        "SOVEREIGN",
        "LIVING SOUL",
        "NATURAL PERSON",
        "ALL CAPS NAME",
        "UCC 1-308",
        "WITHOUT PREJUDICE",
        "STRAWMAN",
        "SECURED PARTY",
        "DEBTOR",
        "AFFIDAVIT OF TRUTH",
        "COMMON LAW LIEN",
        "NOTICE OF LIEN",
        "COPYRIGHT",
        "C/o ",
        "C/O ",
        ":TENANT",
        "TRAVELING",
        "PRESUMPTION",
        "FICTITIOUS NAME",
        "LEGAL NAME",
        "BIRTH CERTIFICATE",
        "REDEMPTION",
        "ACCEPT FOR VALUE",
        "A4V",
        "HJR 192",
        "UNITED STATES OF AMERICA",
        "Michigan, a state",
        "STATE OF MICHIGAN",
        "PERSONAL PROPERTY",
        "REAL PROPERTY",
        "NON-RECORDED",
        "UNRECORDED",
    ]
    for pat in sovereign_patterns:
        if pat.upper() in upper:
            notes.append(f"sovereign-citizen language: {pat}")
            break

    judge_names = [
        ("MILLER", "Judge Miller name in document"),
        ("YANCEY", "Judge Yancey name in document"),
        ("CYLENTHIA", "Judge Miller first name"),
        ("TENISHA", "Judge Yancey first name"),
        ("LATOYE", "Judge Miller middle name"),
    ]
    for name, label in judge_names:
        if name in upper:
            notes.append(label)
            break

    if doc_type == "QCD" and ("$1" in text or "$1.00" in text or "ONE DOLLAR" in upper):
        notes.append("nominal $1 QCD (possible intra-family transfer)")

    if doc_type in ("WD", "QCD") and parties.count("→") == 1:
        parts = parties.split("→")
        if len(parts) == 2:
            g1, g2 = parts[0].strip().upper(), parts[1].strip().upper()
            # same surname flip
            s1 = g1.split()[-1] if g1.split() else ""
            s2 = g2.split()[-1] if g2.split() else ""
            if s1 and s2 and s1 == s2 and g1 != g2:
                notes.append("same-surname transfer (family flip)")

    if "LAND BANK" in upper or "DLBA" in upper:
        notes.append("Detroit Land Bank involvement")

    if "FORECLOSURE" in upper or doc_type == "SD":
        notes.append("foreclosure-related")

    if "TRUST" in upper and ("FAMILY TRUST" in upper or "LIVING TRUST" in upper):
        notes.append("trust entity in parties")

    if "PERKINS" in upper or "BANKS" in upper:
        notes.append("connected party: Banks/Perkins network")

    if "FEDERAL" in upper and ("TAX LIEN" in upper or "IRS" in upper):
        notes.append("federal tax lien/release")

    if len(notes) > 3:
        notes = notes[:3] + [f"+{len(notes)-3} more flags"]
    return "; ".join(notes)


def ocr_batch(batch_key: str, cfg: dict):
    cfg["out_dir"].mkdir(parents=True, exist_ok=True)
    prefix = cfg["prefix"]
    files = sorted(IMG_DIR.glob(f"{prefix}_*_p1.png"))
    for i, fp in enumerate(files):
        # batch6_miller_18608653_245455210_docimage_actual_p1.png
        stem = fp.stem.replace(f"{prefix}_", "").replace("_p1", "")
        ocr_path = cfg["out_dir"] / f"{stem}_p1_ocr.txt"
        if ocr_path.exists():
            continue
        print(f"[{batch_key}] OCR {i + 1}/{len(files)}: {fp.name}...", flush=True)
        img = Image.open(fp)
        text = pytesseract.image_to_string(img, lang="eng")
        ocr_path.write_text(text, encoding="utf-8")


def build_from_ocr(batch_key: str, cfg: dict):
    account = cfg["account"]
    results = []
    for fp in sorted(cfg["out_dir"].glob("*_p1_ocr.txt")):
        file_id = fp.name.replace("_p1_ocr.txt", "")
        img_num = file_id.replace(f"{account}_", "").replace("_docimage_actual", "")
        text = fp.read_text(encoding="utf-8", errors="replace")
        parsed = parse_doc(text, img_num)
        parsed["image"] = f"{cfg['prefix']}_{file_id}_p1.png"
        parsed["pdf"] = f"{file_id}.pdf"
        parsed["ocr_text"] = text
        results.append(parsed)
    return results


def write_index(batch_key: str, cfg: dict, results: list):
    results_sorted = sorted(
        results,
        key=lambda r: (r["date"] or "0000/00/00", r["doc_num"] or "0"),
        reverse=True,
    )

    cfg["out_dir"].joinpath("parsed_index.json").write_text(
        json.dumps(
            [{k: v for k, v in r.items() if k != "ocr_text"} for r in results_sorted],
            indent=2,
        ),
        encoding="utf-8",
    )

    flagged = [r for r in results_sorted if r.get("notes")]
    type_counts = {}
    for r in results_sorted:
        t = r["type"] or "UNK"
        type_counts[t] = type_counts.get(t, 0) + 1

    lines = [
        f"# Wayne County ROD — {batch_key.replace('_', ' ').title()} Index",
        "",
        f"**Subject:** {cfg['subject']}",
        f"**Search account:** {cfg['account']} (Wayne ROD pull, Sep 2 2026)",
        f"**Documents indexed:** {len(results)}",
        "**Source:** Page 1 OCR of scanned ROD images (Tesseract 5.5)",
        f"**OCR cache:** `{batch_key}/extracted/*_p1_ocr.txt`",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Document types | {', '.join(f'{k} ({v})' for k, v in sorted(type_counts.items(), key=lambda x: -x[1]))} |",
        f"| Flagged / notable | {len(flagged)} of {len(results)} |",
        "",
    ]

    if flagged:
        lines.extend([
            "### Notable findings",
            "",
        ])
        for r in flagged:
            lines.append(
                f"- **{r['file_id']}** ({r['type'] or '?'}, Doc# {r['doc_num'] or '—'}, {r['date'] or '—'}): {r['notes']}"
            )
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Full Index",
        "",
        "Sorted by recording date (newest first). *File ID* = ROD image number from filename.",
        "",
        "| File ID | Doc# | Type | Date | Parties | Property | Amount | Notes |",
        "|---------|------|------|------|---------|----------|--------|-------|",
    ])

    for r in results_sorted:
        lines.append(
            f"| {r['file_id']} | {r['doc_num'] or '—'} | {r['type'] or '—'} | "
            f"{r['date'] or '—'} | {r['parties'] or '—'} | {r['property'] or '—'} | "
            f"{r['amount'] or '—'} | {r['notes'] or '—'} |"
        )

    lines.extend([
        "",
        "### Type key",
        "",
        "| Code | Meaning |",
        "|------|---------|",
        "| QCD | Quit Claim Deed |",
        "| WD | Warranty Deed |",
        "| MTG | Mortgage |",
        "| DIS / MSR | Discharge / Satisfaction of Mortgage |",
        "| SD | Sheriff's Deed (foreclosure) |",
        "| COF / COR | Certificate of Forfeiture / Redemption (tax) |",
        "| ASG | Assignment of Mortgage |",
        "| IRS | Federal tax lien notice or release |",
        "| AFF | Affidavit |",
        "| LIS | Lis Pendens |",
        "",
        "---",
        "",
        f"*Generated Sep 7, 2026. Re-run: `python build_batch67_index.py`*",
    ])

    cfg["index_path"].write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {cfg['index_path']} ({len(results)} docs, {len(flagged)} flagged)")


def main():
    for batch_key, cfg in BATCHES.items():
        ocr_batch(batch_key, cfg)
        results = build_from_ocr(batch_key, cfg)
        write_index(batch_key, cfg, results)


if __name__ == "__main__":
    main()
