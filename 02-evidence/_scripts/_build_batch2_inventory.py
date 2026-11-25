# One-off: append batch 2 rows to SCREENSHOT_INVENTORY_SEP16.md
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\mokke\Pictures\Screenshots")
OUT = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\SCREENSHOT_INVENTORY_SEP16.md")

# filename -> (category, description, move_target)
# Descriptions ~10 words; move uses screenshots-* folders
E = {}

def add(date, cat, desc, move, *times):
    for t in times:
        E[f"Screenshot {date} {t}.png"] = (cat, desc, move)

# --- 2026-09-06 ---
add("2026-09-06", "ROD_DEED", "Macomb ROD Leon/Simone Renee Smith party search results", "screenshots-rod/", "183441")
add("2026-09-06", "ROD_DEED", "Macomb ROD Shayla Smith quit claim deeds N River Rd", "screenshots-rod/", "183349")
add("2026-09-06", "ROD_DEED", "Macomb ROD Marquita Smith deeds liens Merrimac Cir", "screenshots-rod/", "183204", "183053")

# --- 2026-09-05 ---
add("2026-09-05", "CORRESPONDENCE", "USPS tracking Detroit North End available pickup Sep 3", "screenshots-misc/", "183844")
add("2026-09-05", "CORRESPONDENCE", "USPS tracking delivered Lansing PO Box Sep 3", "screenshots-misc/", "183500")
add("2026-09-05", "CORRESPONDENCE", "USPS tracking delivered Lansing PO Box Sep 4", "screenshots-misc/", "183440")
add("2026-09-05", "CORRESPONDENCE", "Duplicate USPS delivery status same tracking 9589070829", "screenshots-misc/", "183433")
add("2026-09-05", "PERSONAL", "Partial Steam library sidebar games count 1556", "screenshots-misc/", "092217")
add("2026-09-05", "WEB_CAPTURE", "3rdcc.org Friend of Court page 503 service unavailable", "screenshots-web/", "084607")
add("2026-09-05", "WEB_CAPTURE", "Purpose Charter Academy open meetings teleconference notice", "screenshots-web/", "084404")
add("2026-09-05", "WEB_CAPTURE", "Purpose Charter board page Judge Miller Moreland Johnson", "screenshots-web/", "084344")
add("2026-09-05", "PACER", "PACER filer list Townes v Wayne 2:09-cv-10693", "screenshots-pacer/", "060300")
add("2026-09-05", "PACER", "PCL party search Warren Evans 59 results page one", "screenshots-pacer/", "060132")
add("2026-09-05", "PACER", "PCL party search Warren Evans 255 results page one", "screenshots-pacer/", "060107")
add("2026-09-05", "PACER", "PCL party search Eric Sabree 40 federal cases", "screenshots-pacer/", "054306")
add("2026-09-05", "PACER", "Brian Roderick Banks Ch7 98-49073 case summary", "screenshots-pacer/", "054023")
add("2026-09-05", "PACER", "Banks Ch7 98-49073 party list Bohikian Friedman", "screenshots-pacer/", "053948")
add("2026-09-05", "PACER", "Banks 1998 Notice of Bankruptcy Case Filing PDF", "screenshots-pacer/", "053938")
add("2026-09-05", "PACER", "PCL party search Tenisha Yancey three cases", "screenshots-pacer/", "051709")
add("2026-09-05", "PACER", "Bryant v Miller 2:26-cv-10917 party list terminated defs", "screenshots-pacer/", "051409")
add("2026-09-05", "PACER", "Bryant v Miller parties Boyd Bryant Cavanagh counsel", "screenshots-pacer/", "051357")
add("2026-09-05", "PACER", "Bryant v Miller filer list Jeremiah Bryant docket docs", "screenshots-pacer/", "051336")

# --- 2026-09-04 (PACER Smith family + custody) ---
pacer = "screenshots-pacer/"
court = "screenshots-court/"
misc = "screenshots-misc/"
web = "screenshots-web/"

add("2026-09-04", "PACER", "Leon/Marquita Smith Ch7 12-53099 party list Sanfield", pacer, "191503")
add("2026-09-04", "PACER", "Leon/Marquita Smith 2012 Notice of Bankruptcy Filing", pacer, "191453")
add("2026-09-04", "PACER", "Case 12-53099 filer list Leon and Marquita Smith", pacer, "191221")
add("2026-09-04", "PACER", "Case 12-53099 case summary Ch7 discharged 2012", pacer, "191208")
add("2026-09-04", "PACER", "Case 12-53099 associated prior Smith bankruptcies list", pacer, "191141", "191123")
add("2026-09-04", "COURT_RECORD", "MDOC OTIS Mario Angelo Smith felony murder profile", court, "190944")
add("2026-09-04", "COURT_RECORD", "MDOC OTIS Mario D Smith probation absconder profile", court, "190932")
add("2026-09-04", "COURT_RECORD", "MDOC OTIS search Mario Smith two offender matches", court, "190922")
add("2026-09-04", "PACER", "PACER Smith v Renico habeas 2:04-cv-72864 summary", pacer, "190417")
add("2026-09-04", "PACER", "USA v Montague filer list Dana Montague 1994 MJ", pacer, "190305")
add("2026-09-04", "PACER", "Brandon/Marquita Smith LA Ch13 13-20526 party list", pacer, "190029")
add("2026-09-04", "PACER", "PCL party search Mario Smith MI courts 38 results", pacer, "185519")
add("2026-09-04", "PACER", "PCL search Simone Renee Smith bk 2:2026bk49404", pacer, "185446")
add("2026-09-04", "PACER", "PACER Marquita King LA Ch7 25-12972 case summary", pacer, "185358")
add("2026-09-04", "PACER", "PCL party search Marquita Smith 66 cases page one", pacer, "185302")
add("2026-09-04", "PACER", "PCL party search Leon Smith 427 results page one", pacer, "185211", "185204")
add("2026-09-04", "PACER", "PCL Leon Anthony Smith five bankruptcy cases MI CA", pacer, "185057")
add("2026-09-04", "PACER", "PCL Shayla Nicole Smith four bankruptcy civil cases", pacer, "185018")
add("2026-09-04", "PACER", "CM/ECF query Simone Renee Smith 26-49404 Ch7", pacer, "184810")
add("2026-09-04", "PACER", "CM/ECF query Marquita Renea Smith 26-47542 Ch13", pacer, "184720")
add("2026-09-04", "PACER", "PACER select case Marquita Smith five bankruptcies", pacer, "184641")
add("2026-09-04", "PACER", "PACER select case Leon Anthony Smith four bankruptcies", pacer, "184611")
add("2026-09-04", "PACER", "PACER name search Shayla Smith no match receipt", pacer, "184543")
add("2026-09-04", "PACER", "Shayla N Smith Ohio Ch7 08-11592 case summary", pacer, "171929")
add("2026-09-04", "PACER", "PCL party search Shayla ten OH IN TN WI cases", pacer, "171657")
add("2026-09-04", "PACER", "Simone Renee Smith 26-49404 case summary Eastpointe", pacer, "165544", "165049")
add("2026-09-04", "PACER", "Simone Renee Smith 26-49404 party list Moran trustee", pacer, "165419")
add("2026-09-04", "PACER", "PACER search Simone Smith six bankruptcy cases list", pacer, "164954")
add("2026-09-04", "PACER", "PACER search Leon/Leonard Smith 39 bankruptcy matches", pacer, "164925")
add("2026-09-04", "COURT_RECORD", "3rdcc virtual courtroom protocols Zoom email rules", court, "145827")
add("2026-09-04", "COURT_RECORD", "Judge Triplett chambers protocol ePraecipe emergency email", court, "145800")
add("2026-09-04", "COURT_RECORD", "Judge Regina Triplett contact virtual hearing buttons", court, "131751")
add("2026-09-04", "CORRESPONDENCE", "3rdcc email rejected ePraecipe case 26-108221-DC", misc, "131608")
add("2026-09-04", "COURT_RECORD", "3rdcc ePraecipe Mitchell emergency custody motion form", court, "104421", "104350", "104146")
add("2026-09-04", "CORRESPONDENCE", "Gmail fwd 3rdcc accepted domestic motion Sep 3 filing", misc, "104106", "104103")
add("2026-09-04", "CORRESPONDENCE", "Outlook snippet email trustee re Marquita Renea Smith", misc, "083606")
add("2026-09-04", "COURT_RECORD", "3rdcc filing history Mitchell emergency motion approved", court, "083405")
add("2026-09-04", "PACER", "Marquita Renea Smith 26-47542 parties Ally Sandweiss", pacer, "070704", "070711")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 Notice of Bankruptcy Filing", pacer, "070734")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 case history docket docs 1-29", pacer, "070752")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 filer list petition schedules", pacer, "070814")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 deadlines hearings 341 confirm", pacer, "070828")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 creditor list part one", pacer, "070843")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 creditor matrix incl Mario", pacer, "070852", "070858")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 attorneys Ally Bank counsel", pacer, "070927")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 case summary Macomb Ch13", pacer, "070910")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 associated prior 25-46692", pacer, "070938")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 aliases fka Marquita King", pacer, "070942")
add("2026-09-04", "PACER", "Marquita Smith 26-47542 Ally Bank filer objections", pacer, "070808")
add("2026-09-04", "COURT_RECORD", "Ingham MC11 subpoena form 2026-4349-CZ Kevin Mok", court, "064332", "061522")

# --- 2026-09-03 ---
add("2026-09-03", "COURT_RECORD", "3rdcc domestic motion confirm step Mitchell emergency", court, "205620")
add("2026-09-03", "COURT_RECORD", "3rdcc upload error motion PDF over 25MB limit", court, "204309")
add("2026-09-03", "COURT_RECORD", "3rdcc additional documents step dropdown motion", court, "205448")
add("2026-09-03", "COURT_RECORD", "3rdcc motion filing fee dropdown Motion Filing 60", court, "191651")
add("2026-09-03", "COURT_RECORD", "3rdcc Mitchell Allpaid receipt domestic motion start", court, "191236")
add("2026-09-03", "FINANCIAL", "USAA savings deposits Fidelity VA interest past 90d", misc, "160917", "160740")
add("2026-09-03", "FINANCIAL", "USAA savings header balance duplicate deposit view", misc, "160746")
add("2026-09-03", "COURT_RECORD", "CC377 PPO nondomestic Kevin Mok vs Brian Banks", court, "112824")
add("2026-09-03", "COURT_RECORD", "Wayne emergency ex parte header snippet cropped", court, "094431")
add("2026-09-03", "COURT_RECORD", "Blank CC380 nondomestic PPO order form template", court, "090815")
add("2026-09-03", "PACER", "Shayla N Smith 08-11592 creditor list Ohio Ch7", pacer, "080105")
add("2026-09-03", "COURT_RECORD", "3rdcc domestic filing emergency checkbox alert dialog", court, "070122")
add("2026-09-03", "PACER", "PACER login choose Ohio Northern bk court 08-11592", pacer, "075541", "075723", "075817", "075738")
add("2026-09-03", "COURT_RECORD", "CC375 blank domestic PPO petition PDF page one", court, "091218")
add("2026-09-03", "COURT_RECORD", "CC375 domestic PPO petition checked relief page two", court, "091831")
add("2026-09-03", "COURT_RECORD", "CC375 domestic PPO Mitchell partial respondent blank", court, "091456")
add("2026-09-03", "COURT_RECORD", "CC376 domestic PPO Mitchell vs Leon A Smith", court, "091104")
add("2026-09-03", "COURT_RECORD", "CC377 nondomestic PPO Mitchell vs Dresden address", court, "093138")
add("2026-09-03", "COURT_RECORD", "Domestic PPO petition Mitchell vs Shayla Smith header", court, "092200")
add("2026-09-03", "COURT_RECORD", "PPO form CC375/CC376/CC380 browser tabs batch", court,
    "091212", "091225", "091228", "091234", "091030", "093214", "204225", "191651")

# --- 2026-09-02 ---
add("2026-09-02", "COURT_RECORD", "Ingham summons 2026-4349-CZ Mok v Holland et al", court, "144800")
add("2026-09-02", "CORRESPONDENCE", "Draft email Michael Elrick Free Press re Banks lawyer", misc, "061856")
add("2026-09-02", "PACER", "PCL account error no search privileges message", pacer, "074459", "074326")
add("2026-09-02", "WEB_CAPTURE", "PUBREC signup property data deed API plans", web, "064021", "064028", "064033", "064035", "064037", "064120", "064127", "064333", "064440")
add("2026-09-02", "WEB_CAPTURE", "Reliaguide Thomas Nolan Butzel attorney profile P83092", web, "102233")
add("2026-09-02", "WEB_CAPTURE", "Reliaguide Todd Perkins Detroit attorney profile", web, "104512", "104437", "104538")
add("2026-09-02", "ROD_DEED", "Michigan Official Records Search advanced blank form", "screenshots-rod/", "124212", "124320", "124429", "124544", "124816", "124849", "124940", "125710")
add("2026-09-02", "CORRESPONDENCE", "Clutch Justice Rita Williams reply re JTC complaints", misc, "092846", "120140")
add("2026-09-02", "WEB_CAPTURE", "Yelp Yecart Accounting Service Southfield unclaimed", web, "140141", "140128", "140013", "140017", "142723", "142930", "144526")
add("2026-09-02", "WEB_CAPTURE", "MI licensee search Tracey Ellis accountant no results", web, "142930")

# --- 2026-09-01 ---
add("2026-09-01", "COURT_RECORD", "Summons MC01 Mok v Brian Banks case 2026-4301-CZ", court, "082002", "081956", "082520")
add("2026-09-01", "SOCIAL_MEDIA", "LinkedIn Brandi Watts search Detroit tax compliance", "screenshots-web/", "161625")
add("2026-09-01", "SOCIAL_MEDIA", "LinkedIn profile experience MacDowell RSM KPMG tax", "screenshots-web/", "165204", "165142", "164843", "164208", "164017", "163919", "162749", "162701", "162654", "161406", "161355", "161537", "161010", "161030", "161037")
add("2026-09-01", "WEB_CAPTURE", "Website phone fax 248-799-3000 contact tooltip", web, "161042")
add("2026-09-01", "SOCIAL_MEDIA", "Facebook profile Alana Mundy Olds Detroit author", "screenshots-web/", "164217")

# --- August 2026 partial ---
add("2026-08-31", "WEB_CAPTURE", "Michigan ICHAT record correction procedures page", web, "200830", "200822", "200816", "200759", "200733")
add("2026-08-31", "COURT_RECORD", "MDOC OTIS Joseph Holland discharged 2024 profile", court, "195620", "195611", "195528")
add("2026-08-31", "COURT_RECORD", "MC302 Proof of Mailing Mok v Smith 2026-4301-CZ", court, "164308", "164058")
add("2026-08-31", "WEB_CAPTURE", "SBM Reliaguide Brian Banks Detroit zero lawyer results", web, "181355", "181350", "181326")
add("2026-08-31", "WEB_CAPTURE", "Reliaguide Detroit lawyer search Darrell J Banks", web, "181508", "181503")
add("2026-08-30", "WEB_CAPTURE", "LARA filing history ten filings Articles 2017", web, "194641")

def rows_for_dates(prefix_dates):
    files = []
    for d in prefix_dates:
        files.extend(sorted(ROOT.glob(f"Screenshot {d}*.png"), key=lambda p: p.name, reverse=True))
    return files

sep_dates = [f"2026-09-{d:02d}" for d in range(6, 0, -1)]
aug_files = sorted(ROOT.glob("Screenshot 2026-08-*.png"), key=lambda p: p.name, reverse=True)

lines = []
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Inventory batch 2 (Sep 1–6, 2026 + partial Aug 2026)")
lines.append("")
lines.append("**Processed in this batch:** Sep 1–6 PNGs (newest → oldest by day); August started (newest first, partial).")
lines.append("**Status:** Inventory only — **do not move files yet**")
lines.append("")

counter = Counter()
missing = []

def emit_section(title, files):
    global lines
    lines.append(f"### {title}")
    lines.append("")
    lines.append("| Filename | Date | Category | Description (≈10 words) | Move? |")
    lines.append("|----------|------|----------|---------------------------|-------|")
    for p in files:
        name = p.name
        date = name.split()[1]
        if name in E:
            cat, desc, move = E[name]
        else:
            cat, desc, move = "UNKNOWN", "Needs individual review — not classified this pass", misc
            missing.append(name)
        counter[cat] += 1
        lines.append(f"| {name} | {date} | {cat} | {desc} | Yes → `{move}` |")
    lines.append("")

for day in sep_dates:
    day_files = sorted(ROOT.glob(f"Screenshot {day}*.png"), key=lambda p: p.name, reverse=True)
    if day_files:
        emit_section(day, day_files)

# August partial: only files we have entries for, plus note
aug_inventoried = [p for p in aug_files if p.name in E]
if aug_inventoried:
    emit_section("2026-08-31 / 2026-08-30 (partial August pass)", aug_inventoried)

lines.append("## Category summary — batch 2")
lines.append("")
lines.append(f"**Rows in this batch:** {sum(counter.values())}")
lines.append("")
lines.append("| Category | Count |")
lines.append("|----------|------:|")
for cat, n in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
    lines.append(f"| {cat} | {n} |")
lines.append("")
if missing:
    lines.append(f"**UNKNOWN / needs re-review:** {len(missing)} files (listed as UNKNOWN above).")
    lines.append("")
lines.append("### Batch 2 notes")
lines.append("")
lines.append("1. **Sep 4 PACER cluster:** Many consecutive captures of Marquita Renea Smith case 26-47542-mlo and Smith family bankruptcy searches; keep canonical copies when moving.")
lines.append("2. **Sep 3 sensitive:** USAA savings screenshots expose account numbers — redact before sharing (`160740`, `160917`, etc.).")
lines.append("3. **Sep 5 duplicate:** `183433` duplicates USPS status in `183440`.")
lines.append("4. **August:** 184 PNGs dated 2026-08-* exist; this batch inventoried **{}** August files; continue from 2026-08-30 backward.".format(len(aug_inventoried)))
lines.append("5. **Cumulative in file:** Pass 1 (152) + batch 2 ({}). Remaining before Sep 1: May 2025–Aug 2026 minus August rows done here.".format(sum(counter.values())))
lines.append("")

append = "\n".join(lines)
text = OUT.read_text(encoding="utf-8")
# Replace old notes footer
old = "## Notes\n\n1. **Duplicates:**"
if old in text:
    idx = text.index(old)
    text = text[:idx] + append + old
    text = text.replace(
        "4. **Next pass:** Continue reverse chronological from 2026-09-06 backward.\n\n**Files processed in this pass:** 152",
        "4. **Next pass:** Continue August 2026 backward from 2026-08-30; finish any UNKNOWN rows in batch 2.\n\n**Files processed in pass 1:** 152 | **Batch 2 rows:** " + str(sum(counter.values())),
    )
else:
    text = text + append

OUT.write_text(text, encoding="utf-8")
print("Wrote batch 2:", sum(counter.values()), "rows; unknown:", len(missing))
