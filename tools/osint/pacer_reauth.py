"""Quick PACER re-auth and targeted search script."""
import httpx
import json
import asyncio
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timedelta

TOOLS_DIR = Path(__file__).parent
CREDS = json.loads((TOOLS_DIR / ".pacer_creds.json").read_text())
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"


async def reauth():
    """Re-authenticate with PACER and cache token."""
    url = "https://pacer.login.uscourts.gov/services/cso-auth"
    payload = {
        "loginId": CREDS["username"],
        "password": CREDS["password"],
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=payload)
        ct = r.headers.get("content-type", "")
        raw = r.text

        token = None
        if "xml" in ct or raw.strip().startswith("<"):
            root = ET.fromstring(raw)
            ngs = root.find(".//{http://services.uscourts.gov/v1.0}nextGenCSO")
            if ngs is None:
                ngs = root.find(".//nextGenCSO")
            if ngs is not None:
                token = ngs.text
        elif "json" in ct:
            data = r.json()
            token = data.get("nextGenCSO")

        if token:
            now = datetime.now()
            TOKEN_FILE.write_text(json.dumps({
                "token": token,
                "expiry": (now + timedelta(hours=4)).isoformat(),
                "created": now.isoformat(),
            }))
            print(f"Token refreshed: {token[:20]}...")
            return token
        else:
            print(f"Auth failed. Response: {raw[:300]}")
            return None


async def pcl_party_search(token, last_name, first_name="", court=""):
    """Search PACER Case Locator by party name."""
    search_body = {"lastName": last_name}
    if first_name:
        search_body["firstName"] = first_name
    if court:
        search_body["courtCase"] = {"courtId": [court]}

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            f"{PCL_URL}/parties/find?page=0",
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
            print(f"  {r.text[:300]}")
            return {"results": [], "total": 0, "pages": 0}


async def main():
    token = await reauth()
    if not token:
        print("Auth failed, cannot proceed.")
        return

    searches = [
        # HOLLAND FRONT-LOADED — Break Banks through Holland
        ("Holland", "Joseph", "mieb", "Holland 5 BKs — Schedule A/B: Newcastle/Middlebelt disclosed?"),
        ("Holland", "Joseph", "", "Holland ALL courts — any civil/criminal beyond BK?"),
        ("Williams", "Joseph Antione", "", "HOLLAND BIRTH NAME (ICHAT primary) — additional cases?"),
        ("Williams", "Joseph Antoine", "", "Holland birth name variant — cross-ref"),
        ("Cudworth", "Lisa", "", "Paid $4,017 Holland taxes while incarcerated. Lincoln Park MI."),
        # BANKS CORE
        ("Banks", "Brian", "mieb", "Banks BK 98-49073, 06-55281"),
        ("Banks", "Brian", "", "Banks ALL courts — civil/criminal"),
        # ENTITIES
        ("Purpose Charter Academy", "", "", "PCA — any DOE/DOJ action?"),
        ("Purpose Foundation", "", "", "Banks nonprofit — any federal case?"),
        ("Opportunity For All", "", "", "Holland dark money entity — Latisha Johnson mailers"),
        # SABREE
        ("Sabree", "Eric", "", "Wayne County Treasurer — 40 known PACER hits"),
        # KEY ENABLERS
        ("Perkins", "Todd", "", "Todd Perkins — shared attorney Banks+Miller, 3 BKs"),
        ("Welch", "Tonesa", "", "BMF Defendant #22, Banks step-aunt. 2:05-cr-80955"),
    ]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = RESULTS_DIR / f"TARGETED_SEARCH_{timestamp}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# PACER TARGETED SEARCH — {datetime.now().strftime('%B %d, %Y %H:%M')}\n\n")

        for last, first, court, why in searches:
            label = f"{last}, {first}" if first else last
            court_display = court.upper() if court else "ALL"
            print(f"\nSearching: {label} (court: {court_display})...")
            f.write(f"## {label}\n")
            f.write(f"**Court:** {court_display} | **Why:** {why}\n\n")

            data = await pcl_party_search(token, last, first, court)
            results = data["results"]
            total = data["total"]

            print(f"  Found {total} results")
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

                # If there are more pages, note it
                if data["pages"] > 1:
                    f.write(f"⚠️ **{data['pages']} pages of results — only page 1 shown**\n\n")
            else:
                f.write("*No results found*\n\n")

            f.write("---\n\n")

    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
