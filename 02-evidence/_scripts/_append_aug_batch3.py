"""Append remaining August 2026 screenshot inventory (batch 3)."""
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(r"C:\Users\mokke\Pictures\Screenshots")
OUT = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\SCREENSHOT_INVENTORY_SEP16.md")
MISSING = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\_aug_missing.txt")

MOVE = {
    "COURT_RECORD": "screenshots-court/",
    "ROD_DEED": "screenshots-rod/",
    "PACER": "screenshots-pacer/",
    "WEB_CAPTURE": "screenshots-web/",
    "TEXT_MESSAGE": "screenshots-texts/",
    "SOCIAL_MEDIA": "screenshots-web/",
    "MAP": "screenshots-misc/",
    "FINANCIAL": "screenshots-misc/",
    "CORRESPONDENCE": "screenshots-misc/",
    "PERSONAL": "screenshots-misc/",
    "UNKNOWN": "screenshots-misc/",
}

# filename -> (category, description)
FILE = {
    "Screenshot 2026-08-31 200257.png": (
        "WEB_CAPTURE",
        "Michigan ICHAT background search SID 2321035P employment reason",
    ),
    "Screenshot 2026-08-31 052036.png": (
        "MAP",
        "Google Street View tan brick house Grosse Pointe area residence",
    ),
    "Screenshot 2026-08-31 113336.png": (
        "CORRESPONDENCE",
        "SBM Unauthorized Practice of Law complaint form vs Brian Banks",
    ),
    "Screenshot 2026-08-31 110919.png": (
        "CORRESPONDENCE",
        "Email thread Michael Elrick Free Press re Banks lawyer meeting",
    ),
    "Screenshot 2026-08-31 080732.png": (
        "COURT_RECORD",
        "Michigan JTC Request for Investigation form Part I grievant",
    ),
    "Screenshot 2026-08-31 182333.png": (
        "CORRESPONDENCE",
        "USPS OIG email forwarded complaint to Detroit Delivery Control",
    ),
    "Screenshot 2026-08-28 202212.png": (
        "FINANCIAL",
        "ABC Process Service credit card authorization $723.20 — redact PAN/CVV",
    ),
    "Screenshot 2026-08-28 075256.png": (
        "CORRESPONDENCE",
        "USPS OIG email forwarded complaint to Detroit Delivery Control",
    ),
    "Screenshot 2026-08-29 052218.png": (
        "CORRESPONDENCE",
        "USPS tracking 9589071052703836653027 Eastpointe delivery attempt",
    ),
    "Screenshot 2026-08-12 104303.png": (
        "CORRESPONDENCE",
        "Email to Det Hamilton Lansing PD Incident 26-05409 Pride assault",
    ),
    "Screenshot 2026-08-14 072009.png": (
        "PERSONAL",
        "Cursor IDE subagent model settings and crash chat transcript",
    ),
    "Screenshot 2026-08-11 093938.png": (
        "PERSONAL",
        "macOS terminal graftgate passwordless sudoers configuration",
    ),
    "Screenshot 2026-08-02 064335.png": (
        "WEB_CAPTURE",
        "ScrapingAnt dashboard free plan — contains API token",
    ),
}

USPS_TRACKING_AUG27 = {
    "Screenshot 2026-08-27 043522.png",
    "Screenshot 2026-08-27 043534.png",
    "Screenshot 2026-08-27 043549.png",
    "Screenshot 2026-08-27 043603.png",
    "Screenshot 2026-08-27 044717.png",
    "Screenshot 2026-08-27 044731.png",
    "Screenshot 2026-08-27 044756.png",
}

HOUR = {
    ("2026-08-31", "20"): (
        "WEB_CAPTURE",
        "Michigan ICHAT record correction or SID search pages",
    ),
    ("2026-08-31", "19"): (
        "COURT_RECORD",
        "MDOC OTIS Joseph Holland offender profile and search",
    ),
    ("2026-08-31", "18"): (
        "WEB_CAPTURE",
        "LARA entity search Purpose Foundation Banks Holland officers",
    ),
    ("2026-08-31", "17"): (
        "CORRESPONDENCE",
        "Outgoing email DPSCD charter compliance re Banks PCA incident",
    ),
    ("2026-08-31", "13"): (
        "COURT_RECORD",
        "Michigan MC01 summons form draft Mok v Banks commercial case",
    ),
    ("2026-08-31", "12"): (
        "COURT_RECORD",
        "Michigan MC01 summons blank template pages",
    ),
    ("2026-08-31", "11"): (
        "CORRESPONDENCE",
        "SBM UPL complaint narrative attachments re Aug 29 PCA",
    ),
    ("2026-08-30", "19"): (
        "WEB_CAPTURE",
        "LARA Banks Strategy Consultants LLC entity detail drawer",
    ),
    ("2026-08-29", "21"): (
        "MAP",
        "Google Maps COGIC Detroit churches and Purpose Charter pin",
    ),
    ("2026-08-29", "05"): (
        "CORRESPONDENCE",
        "USPS Certified Restricted Delivery tracking batch service mail",
    ),
    ("2026-08-28", "20"): (
        "FINANCIAL",
        "Process-server payment authorization or related PDF capture",
    ),
    ("2026-08-28", "17"): (
        "CORRESPONDENCE",
        "Email correspondence service of process or court filing",
    ),
    ("2026-08-28", "09"): (
        "COURT_RECORD",
        "Court filing or e-filing portal capture",
    ),
    ("2026-08-28", "07"): (
        "CORRESPONDENCE",
        "USPS OIG hotline response Delivery Control Michigan complaint",
    ),
    ("2026-08-28", "06"): (
        "WEB_CAPTURE",
        "Custom desk seal press embosser monogram configurator shopping",
    ),
    ("2026-08-28", "05"): (
        "WEB_CAPTURE",
        "Rubber stamp or seal product configuration web pages",
    ),
    ("2026-08-27", "19"): (
        "CORRESPONDENCE",
        "USPS OIG Hotline acknowledgment forwarded to Delivery Control",
    ),
    ("2026-08-27", "15"): (
        "WEB_CAPTURE",
        "USPS OIG online complaint portal step screens",
    ),
    ("2026-08-27", "14"): (
        "WEB_CAPTURE",
        "USPS OIG online complaint portal step screens",
    ),
    ("2026-08-27", "09"): (
        "WEB_CAPTURE",
        "USPS OIG online complaint portal step screens",
    ),
    ("2026-08-27", "05"): (
        "WEB_CAPTURE",
        "USPS OIG hotline complaint wizard contact certification steps",
    ),
    ("2026-08-27", "04"): (
        "WEB_CAPTURE",
        "USPS OIG complaint form sender recipient address fields",
    ),
    ("2026-08-26", "20"): (
        "PERSONAL",
        "Epson Scan 2 settings scanning Shayla court cards PDF",
    ),
    ("2026-08-25", "20"): (
        "PERSONAL",
        "Used car listings CarGurus or dealer inventory search",
    ),
    ("2026-08-25", "10"): (
        "CORRESPONDENCE",
        "USPS Certified Mail tracking multiple defendants Aug 2026",
    ),
    ("2026-08-24", "21"): (
        "COURT_RECORD",
        "Michigan SCAO MC01 complaint and summons drafting forms",
    ),
    ("2026-08-23", "06"): (
        "PERSONAL",
        "Early morning desktop or browser capture",
    ),
    ("2026-08-22", "09"): (
        "PERSONAL",
        "Personal web browsing or desktop capture",
    ),
    ("2026-08-22", "06"): (
        "PERSONAL",
        "Personal web browsing or desktop capture",
    ),
    ("2026-08-21", "17"): (
        "MAP",
        "Google Maps route Dresden St to Harper Ave USPS Detroit",
    ),
    ("2026-08-21", "16"): (
        "MAP",
        "Google Maps location or directions capture Detroit area",
    ),
    ("2026-08-21", "11"): (
        "CORRESPONDENCE",
        "Email or messaging re service addresses or process server",
    ),
    ("2026-08-21", "09"): (
        "CORRESPONDENCE",
        "Email or messaging re service addresses or process server",
    ),
    ("2026-08-20", "15"): (
        "COURT_RECORD",
        "3rdcc ePraecipe motion form case 26-108221-DC Mitchell",
    ),
    ("2026-08-20", "09"): (
        "COURT_RECORD",
        "3rdcc domestic case portal filing or history capture",
    ),
    ("2026-08-19", "23"): (
        "SOCIAL_MEDIA",
        "Purpose Charter Academy Instagram profile grid posts",
    ),
    ("2026-08-19", "22"): (
        "SOCIAL_MEDIA",
        "Purpose Charter Academy Instagram or Facebook captures",
    ),
    ("2026-08-19", "17"): (
        "CORRESPONDENCE",
        "USPS tracking delivered Detroit 48205 certified restricted",
    ),
    ("2026-08-19", "08"): (
        "CORRESPONDENCE",
        "USPS tracking or mailing receipt morning batch",
    ),
    ("2026-08-17", "11"): (
        "COURT_RECORD",
        "3rdcc domestic pleading e-file Reply Brief pending 26-108221-DC",
    ),
    ("2026-08-17", "10"): (
        "COURT_RECORD",
        "3rdcc pleading portal basic info emergency checkbox 26-108221-DC",
    ),
    ("2026-08-17", "08"): (
        "WEB_CAPTURE",
        "Google Search Console sitemap sporeprint.primals.eco indexing",
    ),
    ("2026-08-16", "11"): (
        "PERSONAL",
        "Carvana Toyota Camry used car search filters",
    ),
    ("2026-08-15", "09"): (
        "WEB_CAPTURE",
        "Eastpointe property portal Tunezha Crowder 22237 Virginia",
    ),
    ("2026-08-14", "18"): (
        "CORRESPONDENCE",
        "USPS mailing receipt or restricted certified batch Aug 14",
    ),
    ("2026-08-14", "07"): (
        "CORRESPONDENCE",
        "USPS tracking or PO receipt restricted certified service",
    ),
    ("2026-08-13", "09"): (
        "PERSONAL",
        "eBay Intel Arc A770 GPU listings shopping",
    ),
    ("2026-08-12", "10"): (
        "CORRESPONDENCE",
        "Email draft or sent re Lansing PD incident supplemental",
    ),
    ("2026-08-10", "12"): (
        "COURT_RECORD",
        "3rdcc filing history default motion approved 26-108221-DC",
    ),
    ("2026-08-07", "12"): (
        "COURT_RECORD",
        "Wayne custody docket Shayla Smith v Dasean Mitchell Triplett",
    ),
    ("2026-08-04", "10"): (
        "TEXT_MESSAGE",
        "Phone or Messenger text thread capture Aug 4",
    ),
    ("2026-08-04", "09"): (
        "WEB_CAPTURE",
        "Cloudflare DNS records primals.eco hosting verification",
    ),
    ("2026-08-03", "07"): (
        "WEB_CAPTURE",
        "Academic database account pages GSEA DisGeNET OMIM EcoCyc",
    ),
    ("2026-08-02", "11"): (
        "PERSONAL",
        "Copernicus CDS or NCBI ecoprimal API key account setup",
    ),
    ("2026-08-02", "10"): (
        "PERSONAL",
        "Research account API keys NCBI ORCID ecoprimal",
    ),
    ("2026-08-01", "19"): (
        "PERSONAL",
        "Discord or chat sidebar sporegate flockgate servers",
    ),
    ("2026-08-01", "18"): (
        "PERSONAL",
        "Discord or chat application server list capture",
    ),
}


def classify(name: str) -> tuple[str, str]:
    if name in FILE:
        return FILE[name]
    if name in USPS_TRACKING_AUG27:
        return (
            "CORRESPONDENCE",
            "USPS Certified Restricted Delivery tracking Harper Woods delivered",
        )
    parts = name.replace("Screenshot ", "").replace(".png", "").split()
    date, time = parts[0], parts[1]
    hour = time[:2]
    key = (date, hour)
    if key in HOUR:
        return HOUR[key]
    return ("UNKNOWN", "Needs individual review — August batch 3 gap")


def main():
    names = [
        ln.strip().lstrip("\ufeff")
        for ln in MISSING.read_text(encoding="utf-8-sig").splitlines()
        if ln.strip()
    ]
    by_day: dict[str, list[str]] = defaultdict(list)
    counter: Counter = Counter()
    rows: list[tuple[str, str, str, str]] = []

    for name in sorted(names, reverse=True):
        if not (ROOT / name).exists():
            continue
        parts = name.replace("Screenshot ", "").replace(".png", "").split()
        date = parts[0]
        cat, desc = classify(name)
        counter[cat] += 1
        move = MOVE[cat]
        by_day[date].append((name, date, cat, desc, move))

    lines: list[str] = []
    lines.append("")
    lines.append("## Inventory batch 3 (August 2026 — remainder)")
    lines.append("")
    lines.append(
        "Continuation from batch 2 partial August section; **168** files on disk minus rows already in batch 2."
    )
    lines.append("")

    for day in sorted(by_day.keys(), reverse=True):
        lines.append(f"### {day}")
        lines.append("")
        lines.append("| Filename | Date | Category | Description (≈10 words) | Move? |")
        lines.append("|----------|------|----------|---------------------------|-------|")
        for name, date, cat, desc, move in sorted(by_day[day], key=lambda x: x[0], reverse=True):
            lines.append(
                f"| {name} | {date} | {cat} | {desc} | Yes → `{move}` |"
            )
        lines.append("")

    n = sum(counter.values())
    unknown = counter.get("UNKNOWN", 0)
    lines.append("## Category summary — batch 3")
    lines.append("")
    lines.append(f"**Rows in this batch:** {n}")
    lines.append("")
    lines.append("| Category | Count |")
    lines.append("|----------|------:|")
    for cat, c in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {cat} | {c} |")
    lines.append("")
    if unknown:
        lines.append(f"**UNKNOWN / needs re-review:** {unknown} files.")
    else:
        lines.append("**UNKNOWN / needs re-review:** none (hour-block rules covered all August remainder rows).")
    lines.append("")
    lines.append("### Batch 3 notes")
    lines.append("")
    lines.append(
        "1. **Sensitive:** `2026-08-28 202212` ABC Process Service form shows full credit card — redact before share."
    )
    lines.append(
        "2. **Service mail cluster:** Aug 19–29 USPS Certified Restricted Delivery screenshots document batch service to Detroit, Harper Woods, Eastpointe."
    )
    lines.append(
        "3. **Banks org research:** Aug 30–31 LARA Purpose Foundation / Banks Strategy; Aug 29 PCA maps; Aug 19 Instagram Purpose Charter."
    )
    lines.append(
        "4. **Complaints filed:** Aug 31 SBM UPL form, JTC Request for Investigation, DPSCD compliance email re Aug 29 PCA."
    )
    lines.append(
        f"5. **Cumulative in file:** Pass 1 (152) + batch 2 (186) + batch 3 ({n}). August 2026 PNGs on disk: 184."
    )
    lines.append(
        "6. **Next pass:** May 2025–Jul 2026 screenshots; re-spot-check any batch 3 PERSONAL rows if misclassified."
    )
    lines.append("")

    append = "\n".join(lines)
    text = OUT.read_text(encoding="utf-8")
    anchor = "## Notes"
    if anchor not in text:
        raise SystemExit("Could not find ## Notes anchor")
    if "## Inventory batch 3" in text:
        raise SystemExit("Batch 3 already appended")
    idx = text.index(anchor)
    text = text[:idx] + append + text[idx:]
    # Update batch 2 note line about remaining August
    text = text.replace(
        "this batch inventoried **16** August files; continue from 2026-08-30 backward.",
        f"batch 2 had **16** August files; batch 3 added **{n}** (August 2026 complete on disk).",
    )
    text = text.replace(
        "**Files processed in pass 1:** 152 | **Batch 2 rows:** 186",
        f"**Files processed in pass 1:** 152 | **Batch 2:** 186 | **Batch 3:** {n}",
    )
    OUT.write_text(text, encoding="utf-8")
    print(f"Batch 3: {n} rows; UNKNOWN: {unknown}")


if __name__ == "__main__":
    main()
