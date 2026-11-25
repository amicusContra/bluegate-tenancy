"""
Generate direct CM/ECF URLs for Kevin to pull Holland's Schedule A/B documents.
Also uses PACER PCL API to get case metadata (filing dates, chapters, etc.)
for all critical cases.
"""

import httpx
import asyncio
import json
from pathlib import Path
from datetime import datetime

TOOLS_DIR = Path(__file__).parent
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"

CRITICAL_CASES = {
    "HOLLAND_BK": [
        {"num": "05-81655", "year": "2005", "label": "Holland BK #1 — Pre-Newcastle baseline", "priority": "HIGH"},
        {"num": "08-65982", "year": "2008", "label": "Holland BK #2 — 1st post-Newcastle (Jun 2007 QCD)", "priority": "HIGH"},
        {"num": "09-46072", "year": "2009", "label": "Holland BK #3 — Post-arrest. Newcastle MUST be on Schedule A/B ★", "priority": "CRITICAL"},
        {"num": "14-46410", "year": "2014", "label": "Holland BK #4 — Filed FROM PRISON (Apr). Newcastle + Middlebelt? ★★", "priority": "CRITICAL"},
        {"num": "14-51632", "year": "2014", "label": "Holland BK #5 — Filed FROM PRISON (Jul). 3 months after #4 ★★", "priority": "CRITICAL"},
    ],
    "BANKS_BK": [
        {"num": "97-45020", "year": "1997", "label": "Banks BK #0 — NEWLY DISCOVERED 3rd bankruptcy", "priority": "HIGH"},
        {"num": "98-49073", "year": "1998", "label": "Banks BK #1 — Known", "priority": "MEDIUM"},
        {"num": "06-55281", "year": "2006", "label": "Banks BK #2 — Known", "priority": "MEDIUM"},
    ],
    "PERKINS_BK": [
        {"num": "03-45986", "year": "2003", "label": "Perkins BK #1", "priority": "MEDIUM"},
        {"num": "06-46764", "year": "2006", "label": "Perkins BK #2 — Joint with Diane C.", "priority": "MEDIUM"},
        {"num": "22-45209", "year": "2022", "label": "Perkins BK #3 — Joint with Diane C. ACTIVE Ch.13", "priority": "HIGH"},
    ],
    "BMF": [
        {"num": "05-80955", "year": "2005", "label": "USA v. Flenory et al — Tonesa Welch D-22", "priority": "MEDIUM", "court": "mied"},
    ],
}


def generate_cmecf_urls(case_num, court="mieb"):
    """Generate direct CM/ECF URLs for a case."""
    if court == "mieb":
        base = "https://ecf.mieb.uscourts.gov"
    elif court == "mied":
        base = "https://ecf.mied.uscourts.gov"
    else:
        base = f"https://ecf.{court}.uscourts.gov"

    return {
        "login": f"{base}/cgi-bin/login.pl",
        "docket_query": f"{base}/cgi-bin/DktRpt.pl",
        "case_search": f"{base}/cgi-bin/iquery.pl",
        "case_number": case_num,
        "instructions": f"1. Go to {base}/cgi-bin/login.pl and log in with PACER credentials\n"
                        f"2. Go to Query → Case Number: {case_num}\n"
                        f"3. Click Docket Report\n"
                        f"4. Check 'Include terminated parties' and 'Include links to docket entries'\n"
                        f"5. Look for: Schedule A/B (Real Property), Statement of Financial Affairs (SOFA)\n"
                        f"6. Click document links to view PDFs\n"
                        f"7. SCREENSHOT the Schedule A/B page showing real property interests",
    }


async def pcl_case_lookup(client, token, case_num, court="mieb"):
    """Look up case details in PCL."""
    num_only = case_num.split("-")[-1] if "-" in case_num else case_num

    search_body = {
        "caseNumber": num_only,
        "courtCase": {"courtId": [court]},
    }

    try:
        r = await client.post(
            f"{PCL_URL}/cases/find?page=0",
            json=search_body,
            headers={
                "X-NEXT-GEN-CSO": token,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            timeout=30,
        )
        if r.status_code == 200:
            data = r.json()
            content = data.get("content", [])
            if content:
                return content[0]
    except Exception as e:
        print(f"  PCL lookup error: {e}")
    return None


async def main():
    token_data = json.loads(TOKEN_FILE.read_text())
    token = token_data["token"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = RESULTS_DIR / f"KEVIN_CMECF_PULL_LIST_{timestamp}.md"

    async with httpx.AsyncClient(timeout=30) as client:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# PACER CM/ECF PULL LIST FOR KEVIN\n")
            f.write(f"## Generated: {datetime.now().strftime('%B %d, %Y %H:%M')}\n")
            f.write("## Login: https://ecf.mieb.uscourts.gov/cgi-bin/login.pl\n\n")
            f.write("---\n\n")

            f.write("## WHAT TO LOOK FOR:\n\n")
            f.write("For each Holland BK case, pull **Schedule A/B** (Real Property).\n")
            f.write("Look for:\n")
            f.write("- **21456 Newcastle Rd, Harper Woods** (JTWRS with Banks since Jun 2007)\n")
            f.write("- **Middlebelt Rd, Romulus** (Holland's property, Cudworth paid taxes)\n")
            f.write("- Any other real property interests\n\n")
            f.write("**If Newcastle is NOT on Schedule A/B for cases filed AFTER June 2007,**\n")
            f.write("**that is federal bankruptcy fraud (18 U.S.C. § 152).**\n\n")
            f.write("Estimated PACER cost: $0.10/page, capped at $3.00/document.\n")
            f.write("Budget: ~$27-45 total for all pulls.\n\n")
            f.write("---\n\n")

            total_cost_est = 0

            for category, cases in CRITICAL_CASES.items():
                f.write(f"## {category.replace('_', ' ')}\n\n")

                for case in cases:
                    court = case.get("court", "mieb")
                    urls = generate_cmecf_urls(case["num"], court)
                    priority = case["priority"]
                    emoji = "🔴" if priority == "CRITICAL" else "🟡" if priority == "HIGH" else "⚪"

                    f.write(f"### {emoji} [{priority}] {case['label']}\n\n")
                    f.write(f"**Case:** {case['num']} | **Court:** {court.upper()} | **Year:** {case['year']}\n\n")

                    print(f"Looking up {case['num']} on PCL...")
                    pcl_data = await pcl_case_lookup(client, token, case["num"], court)
                    await asyncio.sleep(0.5)

                    if pcl_data:
                        case_title = pcl_data.get("caseTitle", "?")
                        date_filed = pcl_data.get("dateFiled", "?")
                        date_closed = pcl_data.get("dateClosed", "?")
                        chapter = pcl_data.get("chapter", "?")
                        judge = pcl_data.get("assignedTo", pcl_data.get("judge", "?"))

                        f.write(f"| Field | Value |\n")
                        f.write(f"|-------|-------|\n")
                        f.write(f"| Title | {case_title} |\n")
                        f.write(f"| Filed | {date_filed} |\n")
                        f.write(f"| Closed | {date_closed} |\n")
                        f.write(f"| Chapter | {chapter} |\n")
                        f.write(f"| Judge | {judge} |\n\n")

                        print(f"  OK: {case_title} — filed {date_filed}, ch.{chapter}")
                    else:
                        f.write("*PCL metadata not available — case may be too old for PCL index*\n\n")
                        print(f"  Not in PCL index")

                    f.write(f"**Steps:**\n")
                    f.write(f"```\n{urls['instructions']}\n```\n\n")

                    if priority == "CRITICAL":
                        f.write("**⚡ THIS IS THE MONEY SHOT.** If Newcastle (JTWRS with Banks)\n")
                        f.write("is not on Schedule A/B, Holland committed federal bankruptcy fraud.\n")
                        f.write("Screenshot the Schedule A/B page whether it lists Newcastle or not.\n\n")
                        total_cost_est += 6
                    else:
                        total_cost_est += 3

                    f.write("---\n\n")

            f.write(f"\n## ESTIMATED TOTAL PACER COST: ~${total_cost_est}\n")
            f.write(f"## All under the $30 free quarterly threshold\n")

    print(f"\nPull list saved to: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
