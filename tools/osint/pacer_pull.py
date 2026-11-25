"""
PACER Batch Pull Script
========================
Automates searching PACER for bankruptcy and civil case data.

PACER charges $0.10/page, capped at $3.00 per document.
Free if total charges < $30/quarter for individual users.

This script uses the PACER Case Locator API (PCL) for cross-district searching,
and the individual court CM/ECF systems for document retrieval.

USAGE:
  python pacer_pull.py --login          # Store credentials
  python pacer_pull.py --search         # Run all queued searches
  python pacer_pull.py --pull <case>    # Pull specific case docket
  python pacer_pull.py --costs          # Show running cost estimate

REQUIRES: httpx, rich
"""

import httpx
import asyncio
import json
import os
import sys
from pathlib import Path
from datetime import datetime

RESULTS_DIR = Path(__file__).parent / "results" / "pacer"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

CREDENTIALS_FILE = Path(__file__).parent / ".pacer_creds.json"

SEARCH_QUEUE = [
    # ============================================================
    # STRIDE FRAMEWORK — Center Out
    # Ring 0: Marquita (DONE — pulled Sep 4)
    # Ring 1: Leon + Simone (immediate family, same household)
    # Ring 2: Mario Smith, Lemar Jackson (connected names from filings)
    # Ring 3: King family (maiden name), creditors, employers
    # Ring 4: Banks network (separate track)
    # ============================================================

    # --- RING 0: MARQUITA (already pulled 26-47542; remaining cases) ---
    {
        "type": "bankruptcy",
        "court": "mieb",
        "ring": 0,
        "searches": [
            {"name": "Smith, Marquita", "case_numbers": ["25-46692", "25-47952"]},
        ]
    },

    # --- RING 1: LEON + SIMONE (immediate household) ---
    # LEON SEARCH DONE Sep 4 — 33 persons, 39 cases. 6 match our Leon Anthony Smith.
    # SIMONE SEARCH DONE Sep 4 — 5 persons, 6 cases. 4 likely match our Simone.
    {
        "type": "bankruptcy",
        "court": "mieb",
        "ring": 1,
        "searches": [
            # --- LEON (6 cases identified) ---
            {"name": "Smith, Leon A", "case_numbers": ["95-45679"]},
            {"name": "Smith, Leon", "case_numbers": ["96-44109"]},
            {"name": "Smith, Leon Anthony", "case_numbers": ["97-45493", "02-44026", "12-53099", "17-52263"]},
            # --- SIMONE (3 cases — 96-55926 ELIMINATED, different Simone) ---
            {"name": "Smith, Simone", "case_numbers": ["09-72077", "18-46548"]},
            {"name": "Smith, Simone Renee", "case_numbers": ["26-49404"]},
        ]
    },
    {
        "type": "party_search",
        "court": "mieb",
        "ring": 1,
        "status": "DONE — searched Sep 4",
        "names": [
            "Smith, Leon",
            "Smith, Leon A",
            "Smith, Leon Anthony",
            "Smith, Simone",
            "Smith, Simone R",
            "Smith, Simone Renee",
            "Smith, Shayla",
            "Smith, Shayla Nicole",
        ]
    },
    {
        "type": "party_search",
        "court": "mied",
        "ring": 1,
        "names": [
            "Smith, Leon",
            "Smith, Leon A",
            "Smith, Leon Anthony",
            "Smith, Shayla",
            "Smith, Shayla Nicole",
            # "Smith, Lee E",  # ELIMINATED — 96-55926 = different Simone
        ]
    },

    # --- RING 2: MARIO, LEMAR, CONNECTED NAMES ---
    {
        "type": "party_search",
        "court": "mieb",
        "ring": 2,
        "names": [
            "Smith, Mario",
            "Smith, Mario L",
            "Smith, Mario Ledon",
            "Jackson, Lemar",
            "Jackson, Lemar G",
            "Jackson, Brandon Lemar",
            "Mager, Josephine",
            "Hill, Robert",
        ]
    },
    {
        "type": "bankruptcy",
        "court": "mieb",
        "ring": 2,
        "searches": [
            {"name": "Jackson, Brandon Lemar", "case_numbers": ["13-56513"]},
        ]
    },
    {
        "type": "party_search",
        "court": "mied",
        "ring": 2,
        "names": [
            "Smith, Mario",
            "Smith, Mario L",
            "Jackson, Lemar",
            "Lake Trust Credit Union",
        ]
    },

    # --- RING 3: MAIDEN NAME, CREDITORS, PROFESSIONALS ---
    {
        "type": "party_search",
        "court": "mieb",
        "ring": 3,
        "names": [
            "King, Marquita",
            "King, Marquita Renea",
            "Reed, Tae",
            "Nelson Property Management",
            "Cherokee Land LC",
            "Michigan Trusted Title Agency",
            "Sandweiss, Stuart",
        ]
    },
    {
        "type": "party_search",
        "court": "mied",
        "ring": 3,
        "names": [
            "King, Marquita",
            "Nelson Property Management",
            "Cherokee Land LC",
        ]
    },

    # ===========================================================
    # EXPANDED: ALL-COURT SEARCHES (civil, criminal, appellate)
    # Use PCL with NO court type selected = searches everything
    # ===========================================================

    # --- SMITH FAMILY — ALL FEDERAL COURTS (not just BK) ---
    {
        "type": "party_search",
        "court": "ALL",
        "ring": 1,
        "note": "PCL search with NO court type filter — catches civil, criminal, appellate",
        "names": [
            "Smith, Leon Anthony",
            "Smith, Marquita",
            "Smith, Marquita Renea",
            "Smith, Simone Renee",
            "Smith, Shayla",
            "Smith, Shayla Nicole",
            "Smith, Mario",
            # "Smith, Lee E",  # ELIMINATED — different Simone
            "King, Marquita",
        ]
    },

    # --- DEFENSIVE SEARCHES (clean record = credibility) ---
    {
        "type": "party_search",
        "court": "ALL",
        "ring": 0,
        "note": "Defensive — confirm clean federal record for custody",
        "names": [
            "Mitchell, DaSean",
            "Mitchell, Deanna",
        ]
    },

    # --- LAKE TRUST + FINANCIAL (all courts) ---
    {
        "type": "party_search",
        "court": "ALL",
        "ring": 2,
        "note": "Institutional — any federal litigation history",
        "names": [
            "Lake Trust Credit Union",
            "Lake Trust",
            "Cherokee Land LC",
            "Nelson Property Management",
            "Michigan Trusted Title Agency",
        ]
    },

    # --- BANKS NETWORK — ALL COURTS (not just BK) ---
    {
        "type": "party_search",
        "court": "ALL",
        "ring": 4,
        "note": "Banks network — civil/criminal beyond bankruptcy",
        "names": [
            "Banks, Brian",
            "Purpose Charter Academy",
            "Purpose Foundation",
            "Holland, Joseph",
            "Perkins, Todd",
            "Perlmuter, Gary",
            "Miller, Tracy",
            "Yancey, Regina",
            "Crowder, Tunezha",
            "MacDowell Preparatory",
            "Banks Strategy",
            "Workforce Asset",
        ]
    },

    # --- RING 4: BANKS NETWORK (separate track) ---
    {
        "type": "bankruptcy",
        "court": "mieb",
        "ring": 4,
        "searches": [
            {"name": "Banks, Brian", "case_numbers": ["98-49073", "06-55281"]},
            {"name": "Holland, Joseph", "case_numbers": ["05-81655", "08-65982", "09-46072", "14-46410", "14-51632"]},
            {"name": "Perkins, Todd", "case_numbers": ["03-45986", "06-46764", "22-45209"]},
            {"name": "Perlmuter, Gary", "case_numbers": ["09-64903"]},
        ]
    },
    {
        "type": "civil",
        "court": "mied",
        "ring": 4,
        "searches": [
            {"name": "Bryant v. Miller", "case_number": "2:26-cv-10917"},
        ]
    },
    {
        "type": "party_search",
        "court": "mieb",
        "ring": 4,
        "names": [
            "Crowder, Tunezha",
            "Ellis, Tracey",
            "Banks, Justin",
            "Cudworth, Lisa",
        ]
    },
    {
        "type": "party_search",
        "court": "mied",
        "ring": 4,
        "names": [
            "Purpose Charter Academy",
            "Purpose Foundation",
            "MacDowell Preparatory",
            "Banks Strategy",
            "Workforce Asset",
        ]
    },
]

PULL_PRIORITY = {
    # ============================================================
    # STRIDE RING 0 — MARQUITA (center, mostly DONE)
    # 26-47542 already pulled Sep 4 — schedules A-J, SOFA, plan
    # ============================================================
    "26-47542": {
        "target": "Marquita Smith — 3rd BK (Jul 2026, ACTIVE)",
        "ring": 0,
        "status": "DONE — pulled Sep 4",
        "why": "PULLED. Schedules show: no Dresden, no Lake Trust, $69K Jeep, lives with Mario in Roseville. Perjury confirmed.",
        "docs": ["DONE"],
        "priority": "DONE"
    },
    "25-46692": {
        "target": "Marquita Smith — 1st BK (Jun 30 2025, DISMISSED)",
        "ring": 0,
        "why": "Filed SAME DAY as $68K Lake Trust mortgage recording. Schedule A will show if the mortgage was disclosed. SOFA will show recent transfers. Dismissed after 34 days — WHY? Means test failure or fraud finding?",
        "docs": ["docket", "schedules_AB", "schedules_D", "SOFA", "dismissal_order"],
        "priority": "HIGHEST"
    },
    "25-47952": {
        "target": "Marquita Smith — 2nd BK (Aug 7 2025, Ch.13)",
        "ring": 0,
        "why": "Filed 4 days after 1st dismissed. KEY DOCS: Doc 36 (363b sale of West Point for $34K), Doc 25 (creditor objection — who?), Doc 42 (address change), Doc 44 (amendments). Did she list Lake Trust?",
        "docs": ["docket", "doc_8_schedules", "doc_10_plan", "doc_25_objection", "doc_36_363b_sale", "doc_38_sale_objection", "doc_42_address_change", "doc_43_plan_mod", "doc_44_amendments", "creditor_matrix"],
        "priority": "HIGHEST"
    },

    # ============================================================
    # STRIDE RING 1 — LEON + SIMONE (immediate household)
    # Searched Sep 4: Leon = 6 cases confirmed. Simone = 4 cases.
    # BOMBSHELL: Leon + Marquita filed JOINTLY twice (2012, 2017).
    # Household total: ~13 bankruptcies across 3 people over 31 years.
    # ============================================================

    # --- LEON + MARQUITA JOINT FILINGS (highest value) ---
    "17-52263": {
        "target": "Leon Anthony Smith AND Marquita Lashun Smith — Joint Ch.13 (Aug 2017, closed Jun 2023)",
        "ring": 1,
        "why": "🔴 JOINT FILING. 6-year Ch.13 plan closed June 2023 — 2 years before Dresden mortgage scheme. Schedule A MUST show Dresden (Leon owned since 2015). If listed here but hidden in Marquita's 2026 solo BK = PROVEN concealment. Creditor matrix shows who they owed. Plan shows what they paid. SOFA shows transfers.",
        "docs": ["docket", "petition_page1", "schedules_AB", "schedules_D", "schedules_EF", "schedules_IJ", "SOFA", "plan", "creditor_matrix", "discharge"],
        "priority": "HIGHEST"
    },
    "12-53099": {
        "target": "Leon Anthony Smith AND Marquita Lashon Smith — Joint Ch.7 (May 2012, discharged Sep 2012)",
        "ring": 1,
        "why": "🔴 JOINT FILING. What did they own and owe together? Pre-Dresden property snapshot. Confirms Marquita Lashon = our Marquita (SSN match). Address confirms household history.",
        "docs": ["docket", "petition_page1", "schedules_AB", "schedules_D", "discharge"],
        "priority": "HIGHEST"
    },

    # --- SIMONE (new cases discovered) ---
    "26-49404": {
        "target": "Simone Renee Smith — New BK (Aug 24 2026, Ch.7 ACTIVE)",
        "ring": 1,
        "why": "Filed 11 days ago. Filed EXACTLY 8 years + 14 days after her 2018 discharge (§727 refiling bar). Petition confirms address = Dresden. Two household members in BK within 8 weeks.",
        "docs": ["docket", "petition_page1"],
        "priority": "HIGHEST"
    },
    # "96-55926": ELIMINATED — different Simone R. Smith (confirmed DaSean Sep 4)
    "09-72077": {
        "target": "Simone Smith — Solo Ch.7 (Oct 2009, discharged Feb 2010)",
        "ring": 1,
        "why": "NEW — not in our prior records. Falls between 1996 joint and 2018 solo. Address locks identity. What did she discharge?",
        "docs": ["docket", "petition_page1"],
        "priority": "HIGH"
    },
    "18-46548": {
        "target": "Simone Smith — Solo Ch.7 (May 2018, discharged Aug 2018)",
        "ring": 1,
        "why": "Identity lock. Petition address confirms Dresden connection. Debts discharged 8 years before current filing — she waited the exact statutory period.",
        "docs": ["docket", "petition_page1", "schedules_EF"],
        "priority": "HIGH"
    },

    # --- LEON SOLO FILINGS ---
    "95-45679": {
        "target": "Leon A. Smith — 1st BK (Ch.13, May 1995)",
        "ring": 1,
        "why": "Leon's FIRST known BK. Petition = address confirmation. Ch.13 plan = what did he owe at age ~30?",
        "docs": ["docket", "petition_page1"],
        "priority": "HIGH"
    },
    "96-44109": {
        "target": "Leon Smith — 2nd BK (Ch.7, Mar 1996)",
        "ring": 1,
        "why": "Filed immediately after Ch.13 closed. Ch.7 wipe = couldn't sustain plan payments. Pattern: file Ch.13, fail, convert/refile Ch.7.",
        "docs": ["docket", "petition_page1"],
        "priority": "HIGH"
    },
    "97-45493": {
        "target": "Leon Anthony Smith — 3rd BK (Ch.7, Apr 1997)",
        "ring": 1,
        "why": "Third BK in 2 years. Full name 'Leon Anthony Smith' confirmed. What debt kept regenerating?",
        "docs": ["docket", "petition_page1"],
        "priority": "MEDIUM"
    },
    "02-44026": {
        "target": "Leon Anthony Smith — 4th BK (Ch.7, Feb 2002, closed Apr 2006)",
        "ring": 1,
        "why": "Solo Ch.7 filed 02/19/02. Ran 4 years before closing — unusual for Ch.7. Conversion? Reopened? Petition confirms identity + address.",
        "docs": ["docket", "petition_page1"],
        "priority": "MEDIUM"
    },

    # ============================================================
    # STRIDE RING 2 — MARIO, LEMAR, CONNECTED NAMES
    # ============================================================
    "13-56513": {
        "target": "Brandon Lemar Jackson — BK (Aug 2013)",
        "ring": 2,
        "why": "Likely relative of Lemar G Jackson (co-taxpayer on Marquita's West Point property). Address confirms connection. Debts may overlap with Smith household.",
        "docs": ["docket", "petition_page1"],
        "priority": "MEDIUM"
    },
    # Mario Smith — party searches only (no known case numbers yet)
    # Josephine Mager — party search (Marquita's Roseville landlord/creditor)
    # King family — party search (Marquita's maiden name)

    # ============================================================
    # STRIDE RING 4 — BANKS NETWORK (separate track, ongoing)
    # ============================================================
    "22-45209": {
        "target": "Perkins, Todd — 3rd BK (Jun 2022, Ch.13)",
        "ring": 4,
        "why": "Is Banks' attorney still in active Ch.13 bankruptcy? Who are the creditors? Is Banks paying his plan?",
        "docs": ["docket", "plan", "status", "creditor_matrix"],
        "priority": "HIGHEST"
    },
    "2:26-cv-10917": {
        "target": "Bryant v. Miller",
        "ring": 4,
        "why": "Full complaint — what did plaintiff allege against Judge Miller?",
        "docs": ["docket", "complaint_doc1", "order_appointing_counsel"],
        "priority": "HIGHEST"
    },
    "05-81655": {
        "target": "Holland, Joseph — 1st BK",
        "ring": 4,
        "why": "Schedule A — what properties did Holland list under oath?",
        "docs": ["docket", "schedules", "discharge"],
        "priority": "HIGH"
    },
    "06-55281": {
        "target": "Banks, Brian — 2nd BK",
        "ring": 4,
        "why": "Creditor matrix — who did Banks owe? Any network overlap?",
        "docs": ["docket", "schedules", "creditor_matrix"],
        "priority": "HIGH"
    },
    "14-46410": {
        "target": "Holland — 4th BK (Apr 2014)",
        "ring": 4,
        "why": "Why two BKs in 3 months? What changed?",
        "docs": ["docket", "schedules"],
        "priority": "MEDIUM"
    },
    "14-51632": {
        "target": "Holland — 5th BK (Jul 2014)",
        "ring": 4,
        "why": "Filed 3 months after 4th — compare schedules",
        "docs": ["docket", "schedules"],
        "priority": "MEDIUM"
    },
}


def store_credentials():
    """Store PACER login credentials locally."""
    print("\n=== PACER Credentials Setup ===")
    print("Your credentials are stored locally and never transmitted except to PACER.")
    username = input("PACER Username: ").strip()
    password = input("PACER Password: ").strip()

    creds = {"username": username, "password": password}
    CREDENTIALS_FILE.write_text(json.dumps(creds))
    print(f"Credentials saved to {CREDENTIALS_FILE}")
    print("Run with --search to begin pulling data.\n")


def load_credentials():
    """Load stored PACER credentials."""
    if not CREDENTIALS_FILE.exists():
        print("No credentials found. Run with --login first.")
        sys.exit(1)
    return json.loads(CREDENTIALS_FILE.read_text())


def print_search_plan():
    """Print the full search plan with cost estimates."""
    print("\n" + "=" * 70)
    print("PACER SEARCH PLAN — September 2026")
    print("=" * 70)

    total_docs = 0
    for group in SEARCH_QUEUE:
        if group["type"] == "bankruptcy":
            print(f"\n--- {group['court'].upper()} BANKRUPTCY ---")
            for s in group["searches"]:
                for cn in s["case_numbers"]:
                    info = PULL_PRIORITY.get(cn, {})
                    priority = info.get("priority", "STANDARD")
                    why = info.get("why", "")
                    docs = info.get("docs", ["docket"])
                    print(f"  [{priority}] Case {cn} — {s['name']}")
                    if why:
                        print(f"           Why: {why}")
                    print(f"           Pull: {', '.join(docs)}")
                    total_docs += len(docs)

        elif group["type"] == "civil":
            print(f"\n--- {group['court'].upper()} CIVIL ---")
            for s in group["searches"]:
                cn = s["case_number"]
                info = PULL_PRIORITY.get(cn, {})
                priority = info.get("priority", "STANDARD")
                why = info.get("why", "")
                docs = info.get("docs", ["docket"])
                print(f"  [{priority}] Case {cn} — {s['name']}")
                if why:
                    print(f"           Why: {why}")
                print(f"           Pull: {', '.join(docs)}")
                total_docs += len(docs)

        elif group["type"] == "party_search":
            print(f"\n--- {group['court'].upper()} PARTY SEARCHES ---")
            for name in group["names"]:
                print(f"  [NEW] Search: \"{name}\"")
                total_docs += 1

    min_cost = total_docs * 0.10
    max_cost = total_docs * 3.00
    print(f"\n{'=' * 70}")
    print(f"Estimated documents: {total_docs}")
    print(f"Cost range: ${min_cost:.2f} — ${max_cost:.2f}")
    print(f"Most likely: ${total_docs * 0.50:.2f} — ${total_docs * 1.50:.2f}")
    print(f"(Docket sheets are usually $0.30-$0.90; schedules are $1-$3)")
    print(f"{'=' * 70}\n")


def generate_manual_urls():
    """Generate direct PACER URLs for manual browser access."""
    print("\n" + "=" * 70)
    print("PACER MANUAL PULL GUIDE")
    print("=" * 70)

    print("""
STEP 1: Log in to PACER
  https://pacer.uscourts.gov

STEP 2: For BANKRUPTCY cases, go to:
  https://ecf.mieb.uscourts.gov/cgi-bin/login.pl
  (E.D. Michigan Bankruptcy Court)

STEP 3: For CIVIL cases, go to:
  https://ecf.mied.uscourts.gov/cgi-bin/login.pl
  (E.D. Michigan District Court)

STEP 4: Use "Query" to look up each case number below.
""")

    print("\n--- HIGHEST PRIORITY (pull these first) ---\n")
    for cn, info in sorted(PULL_PRIORITY.items(), key=lambda x: {"HIGHEST": 0, "HIGH": 1, "MEDIUM": 2}.get(x[1]["priority"], 3)):
        if info["priority"] in ("HIGHEST", "HIGH"):
            court = "mieb" if "cv" not in cn else "mied"
            base = "ecf.mieb.uscourts.gov" if court == "mieb" else "ecf.mied.uscourts.gov"
            print(f"  Case: {cn}")
            print(f"  Target: {info['target']}")
            print(f"  Why: {info['why']}")
            print(f"  Pull: {', '.join(info['docs'])}")
            print(f"  Court: https://{base}")
            print()

    print("\n--- NEW PARTY SEARCHES ---\n")
    print("  Go to PACER Case Locator: https://pcl.uscourts.gov")
    print("  Search type: Party Name")
    print("  Court: E.D. Michigan (both bankruptcy and district)\n")
    for group in SEARCH_QUEUE:
        if group["type"] == "party_search":
            for name in group["names"]:
                print(f"  Search: \"{name}\" in {group['court'].upper()}")
    print()

    print("\n--- WHAT TO SAVE ---\n")
    print("""
  For each case pulled:
  1. Save the DOCKET SHEET as PDF (Print -> Save as PDF)
  2. For bankruptcy: download SCHEDULES (look for "Schedules" in docket)
     - Schedule A/B = Property (CRITICAL)
     - Schedule D = Secured creditors (mortgages)
     - Schedule E/F = Unsecured creditors (everyone else)
     - Schedule I = Income
     - Schedule J = Expenses
  3. For civil: download the COMPLAINT (usually Doc #1)
  4. Save everything to: """)
    print(f"     {RESULTS_DIR}")
    print()

    outfile = RESULTS_DIR / "PACER_PULL_GUIDE.md"
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("# PACER Pull Guide — Generated " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n\n")
        f.write("## Login\n")
        f.write("- PACER: https://pacer.uscourts.gov\n")
        f.write("- E.D. Mich Bankruptcy: https://ecf.mieb.uscourts.gov\n")
        f.write("- E.D. Mich District: https://ecf.mied.uscourts.gov\n")
        f.write("- Case Locator: https://pcl.uscourts.gov\n\n")

        f.write("## Priority Pulls\n\n")
        for cn, info in sorted(PULL_PRIORITY.items(), key=lambda x: {"HIGHEST": 0, "HIGH": 1, "MEDIUM": 2}.get(x[1]["priority"], 3)):
            f.write(f"### [{info['priority']}] Case {cn} — {info['target']}\n")
            f.write(f"- **Why:** {info['why']}\n")
            f.write(f"- **Documents:** {', '.join(info['docs'])}\n\n")

        f.write("## New Party Searches (PACER Case Locator)\n\n")
        for group in SEARCH_QUEUE:
            if group["type"] == "party_search":
                f.write(f"### {group['court'].upper()}\n")
                for name in group["names"]:
                    f.write(f"- {name}\n")
                f.write("\n")

        f.write("## What to Save\n\n")
        f.write("For each case:\n")
        f.write("1. Docket sheet (PDF)\n")
        f.write("2. Bankruptcy schedules A/B, D, E/F, I, J\n")
        f.write("3. Civil complaints (Doc #1)\n")
        f.write("4. Any orders, plans, or creditor matrices\n")
        f.write(f"\nSave to: {RESULTS_DIR}\n")

    print(f"\n  Guide also saved to: {outfile}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_search_plan()
        generate_manual_urls()
    elif sys.argv[1] == "--login":
        store_credentials()
    elif sys.argv[1] == "--search":
        print_search_plan()
        generate_manual_urls()
    elif sys.argv[1] == "--costs":
        print_search_plan()
    else:
        print(f"Unknown argument: {sys.argv[1]}")
        print("Usage: python pacer_pull.py [--login | --search | --costs]")

