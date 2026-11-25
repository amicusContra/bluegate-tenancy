"""
Split the monolithic FEDERAL_MASTER_PACKET_SEP18.md into modular section files.
Keeps the original monolith intact as the "assembled delivery" version.
"""
import os

SRC = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready\FEDERAL_MASTER_PACKET_SEP18.md"
DST = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready\packet"

with open(SRC, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Section boundaries (1-indexed from grep, convert to 0-indexed)
sections = [
    ("00_HEADER",                 0,    89),   # Title, blockquote, TOC
    ("01_EXECUTIVE_SUMMARY",     89,   129),   # §1
    ("02_SILOING",              129,   191),   # §2
    ("03_POWER_MAP",            191,   276),   # §3
    ("04_ACTIVE_INVESTIGATIONS",276,   501),   # §4
    ("05_BANKS_PRINCIPAL",      501,   787),   # §5
    ("06_SABREE_DYNASTY",       787,   864),   # §6
    ("07_BMF_NEXUS",            864,  1159),   # §7
    ("08_JUDGES",              1159,  1317),   # §8
    ("09_COURT_CAPTURE",       1317,  1373),   # §9
    ("10_OMBUDSMAN_DAGNOGO",   1373,  1418),   # §10
    ("11_DARK_MONEY",          1418,  1641),   # §11
    ("12_CHARTER_ENTERPRISE",  1641,  1760),   # §12
    ("13_EXTRACTION_GEOGRAPHY",1760,  1830),   # §13
    ("14_MAIL_FRAUD",          1830,  1892),   # §14
    ("15_ENTITY_MAP",          1892,  1993),   # §15
    ("16_MONEY_FLOW",          1993,  2063),   # §16
    ("17_EVIDENCE_INDEX",      2063,  2146),   # §17
    ("18_AGENCY_RECOMMENDATIONS", 2146, len(lines)),  # §18 to end
]

os.makedirs(DST, exist_ok=True)

manifest = []
for name, start, end in sections:
    chunk = lines[start:end]
    # Strip trailing blank lines
    while chunk and chunk[-1].strip() == "":
        chunk.pop()
    # Strip leading blank lines
    while chunk and chunk[0].strip() == "":
        chunk.pop(0)
    
    fname = f"{name}.md"
    path = os.path.join(DST, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(chunk)
        f.write("\n")
    
    line_count = len(chunk)
    manifest.append((fname, line_count, start+1, end))
    print(f"  {fname:45s}  {line_count:4d} lines  (src {start+1}-{end})")

# Write manifest/index
with open(os.path.join(DST, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write("# Federal Master Packet — Modular Index\n\n")
    f.write("Each file below is one section of the unified packet.\n")
    f.write("The monolith `FEDERAL_MASTER_PACKET_SEP18.md` remains the assembled delivery version.\n\n")
    f.write("| # | File | Lines | Description |\n")
    f.write("|---|------|-------|-------------|\n")
    descs = {
        "00_HEADER": "Title, framing blockquote, table of contents",
        "01_EXECUTIVE_SUMMARY": "The network in one page",
        "02_SILOING": "Why one packet, not eight — how agency silos enabled this",
        "03_POWER_MAP": "Who has institutional power to protect the enterprise",
        "04_ACTIVE_INVESTIGATIONS": "Already in your systems — active investigations & prosecutions",
        "05_BANKS_PRINCIPAL": "Brian Roderick Banks — the man at the center",
        "06_SABREE_DYNASTY": "Sabree family — Treasury, bench, FBI scrutiny",
        "07_BMF_NEXUS": "BMF/drug nexus — two published confessions",
        "08_JUDGES": "Judges who knew and didn't report",
        "09_COURT_CAPTURE": "50,000-case backlog as a weapon",
        "10_OMBUDSMAN_DAGNOGO": "Dagnogo's golden parachute — the ombudsman problem",
        "11_DARK_MONEY": "Dark money pipeline — PACs, nonprofits, campaign finance",
        "12_CHARTER_ENTERPRISE": "Charter school enterprise — how Banks inherited a school",
        "13_EXTRACTION_GEOGRAPHY": "Every dollar leaves Detroit",
        "14_MAIL_FRAUD": "Mail fraud & obstruction (USPS OIG)",
        "15_ENTITY_MAP": "All known entities",
        "16_MONEY_FLOW": "Money flow diagram + existing investigations",
        "17_EVIDENCE_INDEX": "Evidence index & exhibits",
        "18_AGENCY_RECOMMENDATIONS": "Recommendations by agency + delivery protocol",
    }
    for fname, lc, start, end in manifest:
        key = fname.replace(".md", "")
        desc = descs.get(key, "")
        f.write(f"| {key[:2]} | [{fname}]({fname}) | {lc} | {desc} |\n")
    
    f.write(f"\n**Total: {sum(lc for _, lc, _, _ in manifest)} lines across {len(manifest)} files**\n")

print(f"\nDone. {len(sections)} files written to {DST}")
print(f"Total lines across all sections: {sum(lc for _, lc, _, _ in manifest)}")
