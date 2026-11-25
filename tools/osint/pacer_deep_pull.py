"""
Deep PACER pull — get details for all Smith family + network BK cases.
Uses both PACER PCL API and CourtListener free API.
"""
import httpx
import json
import asyncio
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

TOOLS_DIR = Path(__file__).parent
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"
PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"
CL_URL = "https://www.courtlistener.com/api/rest/v4"

# All cases we need details on
CASES = [
    # SMITH FAMILY
    ("Marquita BK #1", "46692", "mieb", "Marquita Smith — solo, date unknown"),
    ("Marquita BK #2", "47952", "mieb", "Marquita R. Smith — solo, date unknown"),
    ("Leon+Marquita Joint #1", "53099", "mieb", "Leon Anthony + Marquita Lashun joint"),
    ("Leon+Marquita Joint #2 (known)", "52263", "mieb", "Leon Anthony + Marquita Lashun — 2017, have schedules"),
    ("Marquita Current", "47542", "mieb", "Marquita Renea Smith — 2026, ACTIVE"),
    ("Leon Solo #1", "44026", "mieb", "Leon Anthony Smith — solo"),
    ("Leon Solo #2", "45493", "mieb", "Leon Anthony Smith — solo"),
    ("Leon Solo #3", "45679", "mieb", "Leon A. Smith — solo"),
    ("Leon Solo #4", "44109", "mieb", "Leon Smith — verify identity"),
    ("Simone Current", "49404", "mieb", "Simone Renee Smith — 2026, ACTIVE"),
    ("Simone Prior #1", "46548", "mieb", "Simone Smith — 2018"),
    ("Simone Prior #2", "72077", "mieb", "Simone Smith — 2009"),

    # BANKS NETWORK
    ("Banks BK #0", "45020", "mieb", "Brian Banks — 1997 — NEWLY DISCOVERED 3rd BK"),
    ("Banks BK #1", "49073", "mieb", "Brian Roderick Banks — 1998"),
    ("Banks BK #2", "55281", "mieb", "Brian Roderick Banks — 2006"),
    ("Banks Adversary", "2031", "mieb", "Derenobe and Banks — 2025 defendant"),
    ("Lancaster BK #1", "81712", "mieb", "Kevin W Lancaster — 2005"),
    ("Lancaster BK #2", "40388", "mieb", "Kevin Scott Lancaster — 2012"),
    ("Perlmuter BK", "64903", "mieb", "Gary E. Perlmuter"),

    # PERKINS
    ("Perkins BK #1", "45986", "mieb", "Todd Perkins — 2003"),
    ("Perkins BK #2", "46764", "mieb", "Todd J. + Diane C. Perkins — 2006"),
    ("Perkins BK #3", "45209", "mieb", "Todd J. + Diane C. Perkins — 2022"),

    # HOLLAND
    ("Holland BK #1", "81655", "mieb", "Joseph Holland Jr. — 2005"),
    ("Holland BK #2", "65982", "mieb", "Joseph Holland — 2008"),
    ("Holland BK #3", "46072", "mieb", "Joseph Holland Jr. — 2009"),
    ("Holland BK #4", "46410", "mieb", "Joseph Holland Jr. — 2014 (Apr)"),
    ("Holland BK #5", "51632", "mieb", "Joseph Holland Jr. — 2014 (Jul)"),
]


async def cl_lookup(client, case_num, court="mieb"):
    """Look up case on CourtListener (free, no auth)."""
    try:
        r = await client.get(
            f"{CL_URL}/dockets/",
            params={"docket_number": case_num, "court": court},
            headers={"User-Agent": "OSINT-Toolkit/1.0"},
            timeout=15,
        )
        if r.status_code == 200:
            data = r.json()
            results = data.get("results", [])
            if results:
                item = results[0]
                return {
                    "source": "CourtListener",
                    "case_name": item.get("case_name"),
                    "date_filed": item.get("date_filed"),
                    "date_terminated": item.get("date_terminated"),
                    "chapter": item.get("chapter"),
                    "trustee": item.get("trustee_str"),
                    "judge": item.get("assigned_to_str"),
                    "cl_url": f"https://www.courtlistener.com{item['absolute_url']}" if item.get("absolute_url") else None,
                    "docket_entries": data.get("count", 0),
                }
    except Exception as e:
        pass
    return None


async def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = RESULTS_DIR / f"DEEP_PULL_{timestamp}.md"

    async with httpx.AsyncClient(timeout=30) as client:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# DEEP CASE PULL — {datetime.now().strftime('%B %d, %Y %H:%M')}\n")
            f.write(f"## Source: CourtListener API (free)\n\n")

            # Group by category
            categories = {}
            for label, case_num, court, note in CASES:
                cat = label.split(" ")[0]
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append((label, case_num, court, note))

            all_results = []

            for cat, cases in categories.items():
                f.write(f"## {cat.upper()} CASES\n\n")
                f.write("| Label | Case # | Filed | Terminated | Chapter | Trustee | Judge |\n")
                f.write("|-------|--------|-------|-----------|---------|---------|-------|\n")

                for label, case_num, court, note in cases:
                    print(f"Looking up {label} ({case_num})...")
                    result = await cl_lookup(client, case_num, court)
                    await asyncio.sleep(0.5)

                    if result:
                        filed = result.get("date_filed") or "?"
                        term = result.get("date_terminated") or "ACTIVE"
                        ch = result.get("chapter") or "?"
                        trustee = result.get("trustee") or "?"
                        judge = result.get("judge") or "?"
                        name = result.get("case_name") or "?"
                        f.write(f"| {label} | {case_num} | {filed} | {term} | Ch.{ch} | {trustee} | {judge} |\n")
                        all_results.append({
                            "label": label,
                            "case_num": case_num,
                            "note": note,
                            **result,
                        })
                        print(f"  OK {name} -- filed {filed}, ch.{ch}")
                    else:
                        f.write(f"| {label} | {case_num} | — | — | — | — | *Not on CL* |\n")
                        all_results.append({
                            "label": label,
                            "case_num": case_num,
                            "note": note,
                            "source": "NOT_FOUND",
                        })
                        print(f"  -- Not found on CourtListener")

                f.write("\n")

            # Summary
            found = [r for r in all_results if r.get("source") != "NOT_FOUND"]
            not_found = [r for r in all_results if r.get("source") == "NOT_FOUND"]

            f.write("---\n\n")
            f.write(f"## SUMMARY\n\n")
            f.write(f"- **Found on CourtListener:** {len(found)}/{len(all_results)}\n")
            f.write(f"- **Not found (need PACER CM/ECF):** {len(not_found)}\n\n")

            if not_found:
                f.write("### Cases needing PACER CM/ECF pull:\n\n")
                for r in not_found:
                    f.write(f"- {r['label']} ({r['case_num']}) — {r['note']}\n")

            # Timeline
            f.write("\n---\n\n## CHRONOLOGICAL FILING TIMELINE\n\n")
            dated = [(r.get("date_filed", "9999"), r) for r in found if r.get("date_filed")]
            dated.sort()
            f.write("| Date | Case # | Name | Chapter | Who |\n")
            f.write("|------|--------|------|---------|-----|\n")
            for date, r in dated:
                f.write(f"| {date} | {r['case_num']} | {r.get('case_name', '?')} | Ch.{r.get('chapter', '?')} | {r['label']} |\n")

    # Save raw JSON
    json_file = RESULTS_DIR / f"DEEP_PULL_{timestamp}.json"
    json_file.write_text(json.dumps(all_results, indent=2))

    print(f"\nResults saved to: {output_file}")
    print(f"JSON saved to: {json_file}")


if __name__ == "__main__":
    asyncio.run(main())
