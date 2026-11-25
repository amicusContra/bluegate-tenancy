"""Append pre-August 2026 screenshots (batch 4) + grand total summary."""
import re
from pathlib import Path
from collections import Counter, defaultdict

OUT = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\SCREENSHOT_INVENTORY_SEP16.md")
MISSING = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\_preaug_missing.txt")

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

FILE = {
    "Screenshot 2026-07-28 185306.png": (
        "PERSONAL",
        "Libre Hardware Monitor high CPU die temperatures load stats",
    ),
    "Screenshot 2026-07-28 185017.png": (
        "PERSONAL",
        "Libre Hardware Monitor G.Skill 48GB RAM timings temperature",
    ),
    "Screenshot 2026-07-11 152930.png": (
        "WEB_CAPTURE",
        "Lab.primals.eco credentials origin — redact password before share",
    ),
    "Screenshot 2026-07-14 185412.png": (
        "WEB_CAPTURE",
        "Keyoxide ecoPrimal profile secret key and hashed proofs — redact",
    ),
    "Screenshot 2026-06-24 122818.png": (
        "PERSONAL",
        "AT&T BGW320 Wi-Fi SSID Aperture Science password visible — redact",
    ),
    "Screenshot 2026-04-29 111521.png": (
        "WEB_CAPTURE",
        "GitHub fine-grained PAT plasmidbin-harvest token visible — revoke/redact",
    ),
}

HOUR = {
    ("2026-07-28", "15"): ("SOCIAL_MEDIA", "LinkedIn add project ecoPrimals modal"),
    ("2026-07-28", "11"): ("SOCIAL_MEDIA", "LinkedIn profile edit MSU Lansing 48910"),
    ("2026-07-28", "10"): ("SOCIAL_MEDIA", "LinkedIn eco Primal profile Lansing ecoPrimals"),
    ("2026-07-28", "09"): ("WEB_CAPTURE", "RustDesk network ID relay [RELAY_PUBLIC] custom key"),
    ("2026-07-26", "11"): ("WEB_CAPTURE", "crates.io API tokens dashboard Rust registry"),
    ("2026-07-21", "11"): ("WEB_CAPTURE", "Porkbun DNSSEC management primals.eco keyTag 2371"),
    ("2026-07-19", "08"): ("WEB_CAPTURE", "RustDesk ID relay server dialog [RELAY_PUBLIC]"),
    ("2026-07-19", "07"): ("WEB_CAPTURE", "sporePrint primals.eco homepage sovereign scientific computing"),
    ("2026-07-18", "17"): ("WEB_CAPTURE", "webb.primals.eco JSON-RPC esotericWebb service health"),
    ("2026-07-18", "16"): ("WEB_CAPTURE", "Garage Power JSON-RPC parse error response capture"),
    ("2026-07-18", "11"): ("WEB_CAPTURE", "sporePrint site map ecosystem ecoPrimals syntheticChemistry"),
    ("2026-07-18", "09"): ("MAP", "FootPrint GIS search [REDACTED_ADDR_2] Lansing parcel layers"),
    ("2026-07-15", "10"): ("CORRESPONDENCE", "USPS tracking delivered Detroit 48205 Jul 14 2026"),
    ("2026-07-15", "08"): ("CORRESPONDENCE", "USPS tracking or mailing status capture"),
    ("2026-07-14", "20"): ("WEB_CAPTURE", "GitHub ecoPrimal profile contributions rustChip ORCID"),
    ("2026-07-14", "19"): ("WEB_CAPTURE", "Cloudflare DNS records primals.eco Keyoxide TXT"),
    ("2026-07-14", "18"): ("WEB_CAPTURE", "Keyoxide identity setup direct proof fingerprint"),
    ("2026-07-13", "21"): ("SOCIAL_MEDIA", "Discord #general RNA-seq live.primals.eco Tamison"),
    ("2026-07-13", "18"): ("CORRESPONDENCE", "USPS delivery attempt Detroit 48205 notice left"),
    ("2026-07-13", "15"): ("WEB_CAPTURE", "Cloudflare DNS primals.eco A records DigitalOcean IPs"),
    ("2026-07-13", "14"): ("WEB_CAPTURE", "Cloudflare or primals.eco infrastructure DNS edits"),
    ("2026-07-13", "09"): ("WEB_CAPTURE", "primals.eco or lab infrastructure web capture"),
    ("2026-07-12", "09"): ("WEB_CAPTURE", "hotSpring MSU Murillo plasma physics project status page"),
    ("2026-07-12", "08"): ("WEB_CAPTURE", "MSU hotSpring or primals.eco documentation capture"),
    ("2026-07-11", "14"): ("WEB_CAPTURE", "Porkbun DNSSEC digest FAEC02C57A94 for primals.eco"),
    ("2026-07-11", "12"): ("WEB_CAPTURE", "Domain or DNS registrar settings primals.eco"),
    ("2026-07-10", "14"): ("COURT_RECORD", "3rdcc filing history 26-108221-DC approved denied Jul 10"),
    ("2026-07-10", "11"): ("COURT_RECORD", "3rdcc domestic portal pending motion pleading DaSean Mitchell"),
    ("2026-07-10", "10"): ("COURT_RECORD", "3rdcc motion denied bad scan from phone 26-108221-DC"),
    ("2026-07-10", "08"): ("COURT_RECORD", "3rdcc domestic case filings dashboard pending 26-108221-DC"),
    ("2026-07-09", "17"): ("COURT_RECORD", "FOC IV-D child support application Mitchell Smith 26-108221-DC"),
    ("2026-07-09", "12"): ("WEB_CAPTURE", "Gate mesh topology dashboard origin ironGate NUCLEUS"),
    ("2026-07-09", "10"): ("WEB_CAPTURE", "primals.eco infrastructure or gate dashboard capture"),
    ("2026-07-08", "14"): ("WEB_CAPTURE", "sporePrint philosophy essays K-NOME atlasHugged page"),
    ("2026-06-26", "11"): ("CORRESPONDENCE", "Gmail fwd DSDT College orientation DaSean Mitchell Jun 2026"),
    ("2026-06-26", "10"): ("COURT_RECORD", "3rdcc domestic filings no pending DaSean Mitchell portal"),
    ("2026-06-25", "20"): ("COURT_RECORD", "Wayne docket Shayla Smith v Dasean Mitchell Jun 17 filing"),
    ("2026-06-25", "19"): ("COURT_RECORD", "Custody case docket or portal 26-108221-DC related"),
    ("2026-06-25", "08"): ("COURT_RECORD", "Wayne Circuit custody case filing or docket capture"),
    ("2026-06-24", "16"): ("WEB_CAPTURE", "Cloudflare or server config capture Jun 24"),
    ("2026-06-24", "12"): ("PERSONAL", "Router or home network admin configuration capture"),
    ("2026-06-24", "09"): ("WEB_CAPTURE", "JupyterHub or lab.primals.eco session capture"),
    ("2026-06-22", "10"): ("WEB_CAPTURE", "Bioinformatics or primals.eco project web capture"),
    ("2026-06-20", "11"): ("COURT_RECORD", "3rdcc ePraecipe or domestic filing form Mitchell case"),
    ("2026-06-17", "09"): ("MAP", "Google Maps [REDACTED_ADDR_2] Lansing DaSean residence"),
    ("2026-06-13", "10"): ("WEB_CAPTURE", "Research or primals.eco documentation capture"),
    ("2026-06-04", "21"): ("WEB_CAPTURE", "Cloudflare DNS git lab membrane primals.eco subdomains"),
    ("2026-06-04", "12"): ("WEB_CAPTURE", "Cloudflare DNS primals.eco records Jun 4"),
    ("2026-06-04", "08"): ("WEB_CAPTURE", "Domain DNS or hosting configuration primals.eco"),
    ("2026-06-03", "10"): ("WEB_CAPTURE", "sporePrint or GitHub project web capture"),
    ("2026-05-28", "15"): ("WEB_CAPTURE", "Cloudflare or domain status primals.eco May 28"),
    ("2026-05-28", "14"): ("WEB_CAPTURE", "Domain registrar or DNS primals.eco capture"),
    ("2026-05-26", "08"): ("WEB_CAPTURE", "sporePrint or primals.eco site capture"),
    ("2026-05-24", "14"): ("WEB_CAPTURE", "Infrastructure or website monitoring capture"),
    ("2026-05-23", "19"): ("WEB_CAPTURE", "sporePrint methodology page K-NOME scyBorg licensing"),
    ("2026-05-23", "12"): ("WEB_CAPTURE", "primals.eco documentation or DNS capture"),
    ("2026-05-21", "09"): ("PERSONAL", "Bioinformatics project CPU RAM GPU requirements table"),
    ("2026-05-15", "11"): ("WEB_CAPTURE", "DigitalOcean membrane-relay droplets NYC1 [RELAY_PUBLIC]"),
    ("2026-05-13", "20"): ("WEB_CAPTURE", "Server or Cloudflare primals.eco infrastructure"),
    ("2026-05-10", "19"): ("WEB_CAPTURE", "primals.eco site error or DNS outage capture"),
    ("2026-05-10", "10"): ("WEB_CAPTURE", "Cloudflare 502 bad gateway primals.eco May 10"),
    ("2026-05-10", "09"): ("WEB_CAPTURE", "primals.eco DNS failure beside sporePrint window"),
    ("2026-05-09", "13"): ("WEB_CAPTURE", "primals.eco NXDOMAIN and sporePrint dual monitor"),
    ("2026-05-09", "12"): ("WEB_CAPTURE", "sporePrint or domain troubleshooting captures"),
    ("2026-05-08", "09"): ("WEB_CAPTURE", "primals.eco or Cloudflare configuration capture"),
    ("2026-05-07", "16"): ("WEB_CAPTURE", "JupyterLab web IDE untitled folders workspace"),
    ("2026-05-07", "10"): ("WEB_CAPTURE", "Lab or JupyterHub primals.eco compute session"),
    ("2026-05-03", "12"): ("PERSONAL", "Kevin Mok resume MSU Sandia PFAS ecoPrimal research CV"),
    ("2026-04-30", "10"): ("WEB_CAPTURE", "GitHub or primals.eco project capture Apr 30"),
    ("2026-04-29", "11"): ("WEB_CAPTURE", "GitHub personal access token creation screen"),
    ("2026-04-07", "10"): ("PERSONAL", "Cursor agent GPU nouveau vfio VRAM debug workflow"),
    ("2026-04-05", "13"): ("PERSONAL", "Cursor agent GPU driver sec2_prepare fork isolation log"),
    ("2026-03-21", "10"): ("PERSONAL", "Professional reference table MSU supervisors syntheticChemistry"),
    ("2026-03-16", "13"): ("PERSONAL", "Resume or reference document draft capture"),
    ("2026-02-27", "16"): ("PERSONAL", "LaTeX Overleaf compile errors pgfplots Dekker1971 citation"),
    ("2026-02-16", "12"): ("WEB_CAPTURE", "NOAA NCDC web service token ecoPrimal@pm.me — redact"),
    ("2026-02-12", "11"): ("WEB_CAPTURE", "Cloudflare DNS nestgate.io A record [NUCLEUS_WAN]"),
    ("2026-02-07", "15"): ("WEB_CAPTURE", "Porkbun domain dashboard Kevin Mok registrant primals.eco"),
    ("2026-01-04", "12"): ("WEB_CAPTURE", "Britannica circuit vs packet switching network diagram"),
    ("2025-06-29", "13"): ("WEB_CAPTURE", "Michigan LARA online business formation forms list CSCL"),
}

DAY = {
    "2026-07-28": ("SOCIAL_MEDIA", "LinkedIn ecoPrimal profile or project edits Lansing"),
    "2026-07-26": ("WEB_CAPTURE", "Developer account settings crates.io or GitHub"),
}


def classify(name: str) -> tuple[str, str]:
    if name in FILE:
        return FILE[name]
    parts = name.replace("Screenshot ", "").replace(".png", "").split()
    date, time = parts[0], parts[1]
    hour = time[:2]
    key = (date, hour)
    if key in HOUR:
        return HOUR[key]
    if date in DAY:
        return DAY[date]
    return ("UNKNOWN", "Needs individual review — pre-Aug batch 4")


def inventory_rows(text: str) -> list[tuple[str, str, str, str]]:
    pat = re.compile(
        r"^\| (Screenshot [^|]+) \| (\d{4}-\d{2}-\d{2}) \| ([A-Z_]+) \| ([^|]+) \|"
    )
    return [m.groups() for m in pat.finditer(text)]


def main():
    names = [
        ln.strip().lstrip("\ufeff")
        for ln in MISSING.read_text(encoding="utf-8-sig").splitlines()
        if ln.strip()
    ]
    by_day: dict[str, list] = defaultdict(list)
    counter: Counter = Counter()

    for name in names:
        parts = name.replace("Screenshot ", "").replace(".png", "").split()
        date = parts[0]
        cat, desc = classify(name)
        counter[cat] += 1
        by_day[date].append((name, date, cat, desc, MOVE[cat]))

    lines = []
    lines.append("")
    lines.append("## Inventory batch 4 (pre–August 2026)")
    lines.append("")
    lines.append(
        "All remaining `Screenshot 2025-*` and `Screenshot 2026-01` through `2026-07-*` PNGs "
        f"under `Pictures\\Screenshots` (**{len(names)}** files)."
    )
    lines.append("")

    for day in sorted(by_day.keys(), reverse=True):
        lines.append(f"### {day}")
        lines.append("")
        lines.append("| Filename | Date | Category | Description (≈10 words) | Move? |")
        lines.append("|----------|------|----------|---------------------------|-------|")
        for row in sorted(by_day[day], key=lambda x: x[0], reverse=True):
            name, date, cat, desc, move = row
            lines.append(f"| {name} | {date} | {cat} | {desc} | Yes → `{move}` |")
        lines.append("")

    n = sum(counter.values())
    unknown = counter.get("UNKNOWN", 0)
    lines.append("## Category summary — batch 4")
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
        lines.append("**UNKNOWN / needs re-review:** none in batch 4.")
    lines.append("")
    lines.append("### Batch 4 notes")
    lines.append("")
    lines.append(
        "1. **Custody case cluster (Jul 9–10, Jun 17–25):** 3rdcc portal and Wayne docket for 26-108221-DC (Mitchell v Smith)."
    )
    lines.append(
        "2. **primals.eco infrastructure:** Many DNS, Cloudflare, DigitalOcean, Gate mesh, and outage captures May–Jul 2026."
    )
    lines.append(
        "3. **Redact before share:** Keyoxide secret key (`2026-07-14 185412`), lab.primals.eco password (`2026-07-11 152930`), GitHub PAT (`2026-04-29 111521`), router Wi-Fi password (`2026-06-24 122818`), NOAA token (`2026-02-16`)."
    )
    lines.append(
        "4. **Banks-adjacent OSINT:** Jul 28 LinkedIn ecoPrimal; not Brian Banks org filings in this batch."
    )
    lines.append("")

    text = OUT.read_text(encoding="utf-8")
    if "## Inventory batch 4" in text:
        raise SystemExit("Batch 4 already present")
    anchor = "## Notes"
    if anchor not in text:
        raise SystemExit("Missing ## Notes anchor")
    idx = text.index(anchor)
    text = text[:idx] + "\n".join(lines) + text[idx:]

    # Grand total from all inventory rows in file
    all_rows = inventory_rows(text)
    grand = Counter(r[2] for r in all_rows)
    total = sum(grand.values())

    gt = []
    gt.append("## Category summary — GRAND TOTAL (all batches)")
    gt.append("")
    gt.append(f"**Total inventoried screenshot rows:** {total}")
    gt.append("")
    gt.append("| Category | Count |")
    gt.append("|----------|------:|")
    for cat, c in sorted(grand.items(), key=lambda x: (-x[1], x[0])):
        gt.append(f"| {cat} | {c} |")
    gt.append("")
    gt.append(
        "Includes pass 1 (Sep 7–15), batch 2 (Sep 1–6 + partial Aug), batch 3 (remainder Aug 2026), "
        "and batch 4 (pre–Aug 2026). Source folder: `C:\\Users\\mokke\\Pictures\\Screenshots`."
    )
    gt.append("")

    text = text[:idx] + "\n".join(lines) + "\n".join(gt) + text[idx:]
    text = text.replace(
        "**Files processed in pass 1:** 152 | **Batch 2:** 186 | **Batch 3:** 168",
        f"**Pass 1:** 152 | **Batch 2:** 186 | **Batch 3:** 168 | **Batch 4:** {n} | **Grand total:** {total}",
    )
    OUT.write_text(text, encoding="utf-8")
    print(f"Batch 4: {n} rows, UNKNOWN: {unknown}; GRAND TOTAL: {total}")


if __name__ == "__main__":
    main()
