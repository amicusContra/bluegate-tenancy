"""Follow-up PACER searches — Marquita retry + Leon + new targets."""
import httpx
import json
import asyncio
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timedelta

TOOLS_DIR = Path(__file__).parent
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"


def load_token():
    data = json.loads(TOKEN_FILE.read_text())
    return data["token"]


async def pcl_party_search(token, last_name, first_name="", court="", page=0):
    """Search PACER Case Locator by party name."""
    search_body = {"lastName": last_name}
    if first_name:
        search_body["firstName"] = first_name
    if court:
        search_body["courtCase"] = {"courtId": [court]}

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            f"{PCL_URL}/parties/find?page={page}",
            json=search_body,
            headers={
                "X-NEXT-GEN-CSO": token,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        if r.status_code == 200:
            data = r.json()
            content = data.get("content", [])
            total = data.get("totalElements", 0)
            pages = data.get("totalPages", 0)
            return {"results": content, "total": total, "pages": pages}
        else:
            print(f"  PCL search failed: {r.status_code}")
            return {"results": [], "total": 0, "pages": 0}


async def main():
    token = load_token()

    searches = [
        ("Smith", "Marquita", "mieb", "Marquita Smith — retry (502 last time)"),
        ("Smith", "Leon", "mieb", "Leon Smith — need all BK cases"),
        ("King", "Marquita", "mieb", "Marquita King — maiden name?"),
        ("Harrison", "Shayla", "mieb", "Shayla Harrison — custody defendant"),
        ("Mager", "Josephine", "mieb", "Josephine Mager — Marquita's alleged landlord"),
        ("Perlmuter", "Gary", "", "Gary Perlmuter — Banks' attorney"),
    ]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = RESULTS_DIR / f"FOLLOWUP_SEARCH_{timestamp}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# PACER FOLLOW-UP SEARCH — {datetime.now().strftime('%B %d, %Y %H:%M')}\n\n")

        for last, first, court, why in searches:
            label = f"{last}, {first}" if first else last
            court_display = court.upper() if court else "ALL"
            print(f"\nSearching: {label} (court: {court_display})...")
            f.write(f"## {label}\n")
            f.write(f"**Court:** {court_display} | **Why:** {why}\n\n")

            await asyncio.sleep(2)

            data = await pcl_party_search(token, last, first, court)
            results = data["results"]
            total = data["total"]

            print(f"  Found {total} results ({len(results)} returned)")
            f.write(f"**Total hits:** {total}\n\n")

            if results:
                f.write("| Case # | Court | Case Title | Party Role | Date Filed |\n")
                f.write("|--------|-------|------------|-----------|------------|\n")
                for r in results:
                    case_num = str(r.get("caseNumber", r.get("caseNumberFull", "?")))
                    court_id = str(r.get("courtId", "?"))
                    title = str(r.get("caseTitle", r.get("partyName", "?")))
                    role = str(r.get("partyRole", "?"))
                    date = str(r.get("dateFiled", "?"))
                    print(f"  {case_num:15s}  {court_id:8s}  {title}")
                    f.write(f"| {case_num} | {court_id} | {title} | {role} | {date} |\n")
                f.write("\n")

                if data["pages"] > 1:
                    f.write(f"**{data['pages']} pages of results — only page 1 shown**\n\n")
            else:
                f.write("*No results found*\n\n")

            f.write("---\n\n")

    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
