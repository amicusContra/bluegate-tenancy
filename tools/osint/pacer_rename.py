"""
PACER PDF Rename Tool
Extracts case metadata from downloaded PACER PDFs and generates a rename map.
Run this to identify what each 'show_temp' file actually contains.
"""
import fitz
import os
import re
import json

PACER_DIRS = [
    r"C:\Users\mokke\Documents\marquitaPACER",
    r"C:\Users\mokke\Documents\simonePACER",
    r"C:\Users\mokke\Documents\leon_marquita_joint_PACER",
]

def extract_metadata(filepath):
    """Extract case number, document type, and party info from a PACER PDF."""
    try:
        doc = fitz.open(filepath)
        first_pages_text = ""
        for i in range(min(3, len(doc))):
            first_pages_text += doc[i].get_text() + "\n"
        doc.close()

        info = {
            "file": os.path.basename(filepath),
            "size": os.path.getsize(filepath),
            "pages": len(fitz.open(filepath)),
        }

        case_match = re.search(r'(\d{2}-\d{4,5})-?(\w{2,3})?', first_pages_text)
        if case_match:
            info["case_number"] = case_match.group(0)

        if "Case Summary" in first_pages_text:
            info["doc_type"] = "case_summary"
        elif "Associated Cases" in first_pages_text or "Other Filings" in first_pages_text:
            info["doc_type"] = "associated_cases"
        elif "Filers" in first_pages_text and "Added" in first_pages_text:
            info["doc_type"] = "filer_list"
        elif "Parties" in first_pages_text and "represented by" in first_pages_text:
            info["doc_type"] = "party_list"
        elif "Notice of Bankruptcy" in first_pages_text:
            info["doc_type"] = "notice_of_filing"
        elif "Schedule A" in first_pages_text or "Schedule B" in first_pages_text:
            info["doc_type"] = "schedules"
        elif "Schedule D" in first_pages_text:
            info["doc_type"] = "schedule_d"
        elif "Schedule I" in first_pages_text or "Schedule J" in first_pages_text:
            info["doc_type"] = "schedule_ij"
        elif "Statement of Financial Affairs" in first_pages_text or "SOFA" in first_pages_text:
            info["doc_type"] = "sofa"
        elif "Chapter 13 Plan" in first_pages_text:
            info["doc_type"] = "ch13_plan"
        elif "Voluntary Petition" in first_pages_text or "Official Form" in first_pages_text:
            info["doc_type"] = "petition"
        elif "Creditor" in first_pages_text and "Matrix" in first_pages_text:
            info["doc_type"] = "creditor_matrix"
        elif "Docket" in first_pages_text:
            info["doc_type"] = "docket"
        elif "Claims Register" in first_pages_text:
            info["doc_type"] = "claims_register"
        elif "Motion" in first_pages_text:
            info["doc_type"] = "motion"
        elif "Order" in first_pages_text:
            info["doc_type"] = "order"
        else:
            info["doc_type"] = "unknown"

        for name in ["Leon Anthony Smith", "Marquita Lash", "Marquita Renea",
                      "Simone Renee Smith", "Simone Smith", "Simone R Smith"]:
            if name.lower() in first_pages_text.lower():
                info.setdefault("parties", []).append(name)

        chapter_match = re.search(r'Chapter[:\s]+(\d+)', first_pages_text)
        if chapter_match:
            info["chapter"] = chapter_match.group(1)

        info["text_preview"] = first_pages_text[:500].replace('\n', ' ').strip()

        return info
    except Exception as e:
        return {"file": os.path.basename(filepath), "error": str(e)}


def suggest_filename(info, folder_name):
    """Generate a descriptive filename from extracted metadata."""
    case = info.get("case_number", "unknown_case").replace("-", "_")
    doc_type = info.get("doc_type", "unknown")
    chapter = info.get("chapter", "")
    ch_str = f"_ch{chapter}" if chapter else ""

    party_hint = ""
    parties = info.get("parties", [])
    if any("Leon" in p for p in parties) and any("Marquita" in p for p in parties):
        party_hint = "_leon_marquita_joint"
    elif any("Leon" in p for p in parties):
        party_hint = "_leon"
    elif any("Marquita" in p for p in parties):
        party_hint = "_marquita"
    elif any("Simone" in p for p in parties):
        party_hint = "_simone"

    return f"MIEB_{case}{ch_str}{party_hint}_{doc_type}.pdf"


def main():
    all_results = {}

    for dirpath in PACER_DIRS:
        folder_name = os.path.basename(dirpath)
        print(f"\n{'='*70}")
        print(f"DIRECTORY: {dirpath}")
        print(f"{'='*70}")

        results = []
        for f in sorted(os.listdir(dirpath)):
            if f.endswith('.pdf'):
                filepath = os.path.join(dirpath, f)
                info = extract_metadata(filepath)
                suggested = suggest_filename(info, folder_name)
                info["suggested_name"] = suggested
                results.append(info)

                print(f"\n  {f} ({info.get('size', 0):,} bytes, {info.get('pages', '?')} pages)")
                print(f"    Case: {info.get('case_number', 'NOT FOUND')}")
                print(f"    Type: {info.get('doc_type', 'unknown')}")
                print(f"    Parties: {', '.join(info.get('parties', ['unknown']))}")
                print(f"    → Rename to: {suggested}")

        all_results[folder_name] = results

    outfile = os.path.join(os.path.dirname(PACER_DIRS[0]), "PACER_RENAME_MAP.json")
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\n\nRename map saved to: {outfile}")

    md_outfile = os.path.join(os.path.dirname(PACER_DIRS[0]), "PACER_RENAME_MAP.md")
    with open(md_outfile, "w", encoding="utf-8") as f:
        f.write("# PACER PDF Rename Map\n")
        f.write(f"## Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        for folder, results in all_results.items():
            f.write(f"## {folder}\n\n")
            f.write("| Current Name | Case | Type | Pages | Suggested Name |\n")
            f.write("|-------------|------|------|:-----:|----------------|\n")
            for r in results:
                f.write(f"| `{r.get('file', '')}` | {r.get('case_number', '?')} | {r.get('doc_type', '?')} | {r.get('pages', '?')} | `{r.get('suggested_name', '')}` |\n")
            f.write("\n")
    print(f"Markdown map saved to: {md_outfile}")


if __name__ == "__main__":
    main()
