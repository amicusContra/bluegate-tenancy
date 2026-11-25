"""
Pull case details from PACER PCL API for all known cases.
Uses the parties/find endpoint to get filing dates + case details.
"""
import httpx
import json
import asyncio
from pathlib import Path
from datetime import datetime

TOOLS_DIR = Path(__file__).parent
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"
PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"


def load_token():
    return json.loads(TOKEN_FILE.read_text())["token"]


async def pcl_case_search(token, last_name, first_name="", court="mieb"):
    """Get all cases for a party with full details."""
    body = {"lastName": last_name}
    if first_name:
        body["firstName"] = first_name
    if court:
        body["courtCase"] = {"courtId": [court]}

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            f"{PCL_URL}/parties/find?page=0",
            json=body,
            headers={
                "X-NEXT-GEN-CSO": token,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        if r.status_code == 200:
            data = r.json()
            return data.get("content", [])
        else:
            print(f"  Error: {r.status_code}")
            return []


async def main():
    token = load_token()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = RESULTS_DIR / f"CASE_DETAILS_{timestamp}.md"
    json_file = RESULTS_DIR / f"CASE_DETAILS_{timestamp}.json"

    searches = [
        ("Smith", "Marquita", "mieb"),
        ("Smith", "Leon", "mieb"),
        ("Smith", "Simone", "mieb"),
        ("Banks", "Brian", "mieb"),
        ("Lancaster", "Kevin", "mieb"),
        ("Perkins", "Todd", "mieb"),
        ("Holland", "Joseph", "mieb"),
        ("Perlmuter", "Gary", "mieb"),
    ]

    all_cases = {}

    for last, first, court in searches:
        label = f"{last}, {first}"
        print(f"\nPulling details for {label}...")
        results = await pcl_case_search(token, last, first, court)
        await asyncio.sleep(1)

        for r in results:
            case_num = str(r.get("caseNumber", "?"))
            key = f"{court}-{case_num}"
            if key not in all_cases:
                all_cases[key] = {
                    "caseNumber": case_num,
                    "courtId": str(r.get("courtId", "?")),
                    "caseTitle": str(r.get("caseTitle", "?")),
                    "dateFiled": str(r.get("dateFiled", "?")),
                    "dateClosed": str(r.get("dateClosed", r.get("dateTerminated", "ACTIVE"))),
                    "chapter": str(r.get("chapter", "?")),
                    "caseType": str(r.get("caseType", "?")),
                    "partyRole": str(r.get("partyRole", "?")),
                    "searchedAs": label,
                }
                print(f"  {case_num}: {r.get('caseTitle', '?')} — filed {r.get('dateFiled', '?')}")

    # Sort by date
    sorted_cases = sorted(all_cases.values(), key=lambda x: x.get("dateFiled", "9999"))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# ALL CASE DETAILS — {datetime.now().strftime('%B %d, %Y %H:%M')}\n")
        f.write(f"## Source: PACER PCL API\n\n")

        # Smith family timeline
        f.write("## SMITH FAMILY — CHRONOLOGICAL FILING TIMELINE\n\n")
        f.write("| Date Filed | Case # | Case Title | Chapter | Role | Status |\n")
        f.write("|-----------|--------|-----------|---------|------|--------|\n")
        smith_cases = [c for c in sorted_cases if "smith" in c.get("searchedAs", "").lower()]
        for c in smith_cases:
            closed = c.get("dateClosed", "ACTIVE")
            status = "ACTIVE" if closed in ("ACTIVE", "None", "?") else f"Closed {closed}"
            f.write(f"| {c['dateFiled']} | {c['caseNumber']} | {c['caseTitle']} | Ch.{c['chapter']} | {c['partyRole']} | {status} |\n")

        f.write(f"\n**Total Smith family cases: {len(smith_cases)}**\n\n")

        # Banks network timeline
        f.write("---\n\n## BANKS NETWORK — CHRONOLOGICAL TIMELINE\n\n")
        f.write("| Date Filed | Case # | Case Title | Chapter | Role | Searched As |\n")
        f.write("|-----------|--------|-----------|---------|------|------------|\n")
        network_cases = [c for c in sorted_cases if "smith" not in c.get("searchedAs", "").lower()]
        for c in network_cases:
            f.write(f"| {c['dateFiled']} | {c['caseNumber']} | {c['caseTitle']} | Ch.{c['chapter']} | {c['partyRole']} | {c['searchedAs']} |\n")

        f.write(f"\n**Total network cases: {len(network_cases)}**\n\n")

        # Full JSON dump
        f.write("---\n\n## ALL CASES (Full Details)\n\n")
        f.write("```json\n")
        f.write(json.dumps(sorted_cases, indent=2))
        f.write("\n```\n")

    json_file.write_text(json.dumps(sorted_cases, indent=2))

    print(f"\nResults saved to: {output_file}")
    print(f"Total unique cases: {len(all_cases)}")


if __name__ == "__main__":
    asyncio.run(main())
