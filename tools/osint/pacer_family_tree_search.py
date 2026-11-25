"""
PACER Family Tree Search — Smith Family Parallel vs Shared Investigation
=========================================================================
Targeted PCL searches to resolve whether Leonard T Sr's family and
Leon A's family are parallel (unrelated), shared (blood-connected),
or a BK cover (strategically separated).

Sep 7, 2026
"""

import httpx
import asyncio
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timedelta

TOOLS_DIR = Path(__file__).parent
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

CREDENTIALS_FILE = TOOLS_DIR / ".pacer_creds.json"
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"

PACER_AUTH_URL = "https://pacer.login.uscourts.gov/services/cso-auth"
PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"

FAMILY_TREE_SEARCHES = [
    # ============================================================
    # GROUP 1: Leonard T Sr's family — do they have BK filings?
    # If YES → both trees play the bankruptcy game
    # ============================================================
    {"last": "Smith", "first": "Leonard", "court": "mieb", "label": "Leonard T Smith (all) — MI East BK",
     "why": "Find Leonard T Jr's BK filings if any exist"},
    {"last": "Smith", "first": "Leonard T", "court": "mieb", "label": "Leonard T Smith — MI East BK (specific)",
     "why": "Narrow to middle initial T"},
    {"last": "Smith", "first": "Leonard", "court": "", "label": "Leonard Smith — ALL federal courts",
     "why": "Catch any civil/criminal cases nationwide"},

    # ============================================================
    # GROUP 2: The bridge — "Evelyn Smith" and family connections
    # If Evelyn connects to Leon A → families are SHARED
    # ============================================================
    {"last": "Smith", "first": "Evelyn", "court": "mieb", "label": "Evelyn Smith — MI East BK",
     "why": "Mother of Leonard T Jr. Is she connected to Leon A?"},
    {"last": "Smith", "first": "Evelyn", "court": "", "label": "Evelyn Smith — ALL federal courts",
     "why": "Broader search for bridge connection"},

    # ============================================================
    # GROUP 3: Other Tree A names from obituary
    # ============================================================
    {"last": "Smith", "first": "Nikola", "court": "mieb", "label": "Nikola Smith — MI East BK",
     "why": "Leonard T Jr's PNC mortgage co-borrower (wife?)"},
    {"last": "Smith", "first": "Denise", "court": "mieb", "label": "Denise Smith — MI East BK",
     "why": "Leonard T Jr's wife per obituary"},
    {"last": "Smith", "first": "Thomas Edward", "court": "mieb", "label": "Thomas Edward Smith — MI East BK",
     "why": "Leonard T Sr's other son"},
    {"last": "Smith", "first": "Skylar", "court": "mieb", "label": "Skylar Smith — MI East BK",
     "why": "Grandchild on Harrison Twp QCDs"},
    {"last": "Smith", "first": "Daymison", "court": "mieb", "label": "Daymison Smith — MI East BK",
     "why": "Grandchild = 'Dawson' on QCDs"},
    {"last": "Smith", "first": "Robert", "court": "mieb", "label": "Robert Smith — MI East BK",
     "why": "Grandchild on Harrison Twp QCDs"},
    {"last": "Smith", "first": "Matthew", "court": "mieb", "label": "Matthew Smith — MI East BK",
     "why": "Grandchild NOT on QCDs — any filings?"},

    # ============================================================
    # GROUP 4: Craig family (deceased daughter Ronnie's married name)
    # ============================================================
    {"last": "Craig", "first": "Veronica", "court": "mieb", "label": "Veronica Craig — MI East BK",
     "why": "Veronica Smith-Craig, Ronnie C LLC registered agent"},
    {"last": "Smith-Craig", "first": "Veronica", "court": "mieb", "label": "Veronica Smith-Craig — MI East BK",
     "why": "Hyphenated name search"},
    {"last": "Craig", "first": "Ronnie", "court": "mieb", "label": "Ronnie Craig — MI East BK",
     "why": "Deceased daughter of Leonard T Sr"},

    # ============================================================
    # GROUP 5: Walter Smith (co-purchased Merrimac with Marquita)
    # ============================================================
    {"last": "Smith", "first": "Walter", "court": "mieb", "label": "Walter Smith — MI East BK",
     "why": "Co-purchased Merrimac with Marquita 2019. Which tree?"},
    {"last": "Smith", "first": "Walter", "court": "", "label": "Walter Smith — ALL federal courts",
     "why": "Broader search"},

    # ============================================================
    # GROUP 6: Existing family — verify filing date of 17-52263
    # ============================================================
    {"last": "Smith", "first": "Leon Anthony", "court": "mieb", "label": "Leon Anthony Smith — MI East BK (re-verify)",
     "why": "Need exact filing date of 17-52263 — before or after Aug 21, 2017?"},
]


class PacerSearcher:
    def __init__(self):
        self.token = None
        self.token_expiry = None
        self.session_costs = 0.0
        self.results_log = []

    def _load_credentials(self):
        if not CREDENTIALS_FILE.exists():
            print("ERROR: No credentials found at", CREDENTIALS_FILE)
            sys.exit(1)
        return json.loads(CREDENTIALS_FILE.read_text())

    def _load_token(self):
        if TOKEN_FILE.exists():
            data = json.loads(TOKEN_FILE.read_text())
            expiry = datetime.fromisoformat(data.get("expiry", "2000-01-01"))
            if expiry > datetime.now():
                self.token = data["token"]
                self.token_expiry = expiry
                return True
        return False

    def _save_token(self, token, expires_in=3600):
        self.token = token
        self.token_expiry = datetime.now() + timedelta(seconds=expires_in - 60)
        TOKEN_FILE.write_text(json.dumps({
            "token": token,
            "expiry": self.token_expiry.isoformat(),
            "created": datetime.now().isoformat()
        }))

    async def authenticate(self):
        creds = self._load_credentials()
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                PACER_AUTH_URL,
                json={"loginId": creds["username"], "password": creds["password"]},
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                body = response.text
                if "<nextGenCSO>" in body:
                    match = re.search(r"<nextGenCSO>(.*?)</nextGenCSO>", body)
                    token = match.group(1) if match else ""
                else:
                    try:
                        data = response.json()
                        token = data.get("nextGenCSO", data.get("token", ""))
                    except Exception:
                        token = ""
                if token:
                    self._save_token(token)
                    print(f"[AUTH] Authenticated. Token cached until {self.token_expiry}")
                    return token
                else:
                    print(f"[AUTH] Response missing token: {body[:200]}")
                    sys.exit(1)
            else:
                print(f"[AUTH] Failed: {response.status_code}")
                print(response.text[:500])
                sys.exit(1)

    async def ensure_token(self):
        if not self.token or (self.token_expiry and datetime.now() >= self.token_expiry):
            if not self._load_token():
                await self.authenticate()

    async def pcl_search(self, last_name, first_name="", court=""):
        await self.ensure_token()

        search_body = {"lastName": last_name}
        if first_name:
            search_body["firstName"] = first_name
        if court:
            search_body["courtCase"] = {"courtId": [court]}

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                f"{PCL_URL}/parties/find?page=0",
                json=search_body,
                headers={
                    "X-NEXT-GEN-CSO": self.token,
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
            )

            if response.status_code == 200:
                data = response.json()
                results = data.get("content", [])
                total_pages = data.get("totalPages", 1)
                total_elements = data.get("totalElements", len(results))
                self.session_costs += 0.10
                return {
                    "results": results,
                    "total": total_elements,
                    "pages": total_pages,
                    "raw": data
                }
            elif response.status_code == 401:
                print("[AUTH] Token expired, re-authenticating...")
                self.token = None
                await self.authenticate()
                return await self.pcl_search(last_name, first_name, court)
            else:
                print(f"[ERROR] PCL search failed: {response.status_code}")
                print(response.text[:500])
                return {"results": [], "total": 0, "pages": 0, "raw": {}}

    async def run_family_tree_search(self):
        await self.ensure_token()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        output_file = RESULTS_DIR / f"FAMILY_TREE_SEARCH_{timestamp}.md"
        raw_file = RESULTS_DIR / f"FAMILY_TREE_RAW_{timestamp}.json"

        all_raw = {}
        n = len(FAMILY_TREE_SEARCHES)

        print(f"\n{'='*70}")
        print(f"SMITH FAMILY TREE — PACER Search")
        print(f"Running {n} targeted searches")
        print(f"{'='*70}\n")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Smith Family Tree — PACER Search Results\n")
            f.write(f"## Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"## Purpose: Resolve parallel vs shared vs BK cover\n\n")

            for i, search in enumerate(FAMILY_TREE_SEARCHES, 1):
                label = search["label"]
                why = search["why"]
                last = search["last"]
                first = search.get("first", "")
                court = search.get("court", "")

                court_display = court.upper() if court else "ALL"
                print(f"[{i}/{n}] {label} (court: {court_display})...")

                try:
                    data = await self.pcl_search(last, first, court)
                    results = data["results"]
                    total = data["total"]

                    f.write(f"## {i}. {label}\n")
                    f.write(f"**Search:** `{last}, {first}` | **Court:** {court_display} | **Why:** {why}\n")
                    f.write(f"**Results:** {total} total ({len(results)} returned)\n\n")

                    if results:
                        f.write("| # | Case | Court | Filed | Closed | Type | Party/Title |\n")
                        f.write("|---|------|-------|-------|--------|------|-----------|\n")
                        for j, r in enumerate(results[:50], 1):
                            case_num = r.get("caseNumberFull", r.get("caseNumber", r.get("caseId", "?")))
                            court_id = r.get("courtId", "?")
                            filed = r.get("dateFiled", "?")
                            closed = r.get("dateClosed", "OPEN")
                            case_type = r.get("caseType", r.get("caseTypeDescription", "?"))
                            party = r.get("partyName", r.get("caseTitle", "?"))
                            f.write(f"| {j} | {case_num} | {court_id} | {filed} | {closed} | {case_type} | {party} |\n")

                            if "17-52263" in str(case_num) or "1752263" in str(case_num):
                                f.write(f"\n**🔴 FOUND 17-52263! Filed: {filed}**\n\n")
                                print(f"  🔴 FOUND 17-52263! Filed: {filed}")

                        f.write("\n")
                    else:
                        f.write("*No results found.*\n\n")

                    all_raw[label] = {"search": search, "data": data["raw"]}

                    hit_str = f"{total} hits" if total > 0 else "NO HITS"
                    print(f"  -> {hit_str}")

                    await asyncio.sleep(0.5)

                except Exception as e:
                    print(f"  -> ERROR: {e}")
                    f.write(f"## {i}. {label}\n**ERROR:** {e}\n\n")
                    import traceback
                    traceback.print_exc()

            f.write(f"\n---\n")
            f.write(f"**Total searches:** {n}\n")
            f.write(f"**Estimated cost:** ${self.session_costs:.2f}\n")
            f.write(f"**Under $30 free quarterly threshold**\n")

        with open(raw_file, "w", encoding="utf-8") as f:
            json.dump(all_raw, f, indent=2, default=str)

        print(f"\n{'='*70}")
        print(f"Search complete!")
        print(f"Results: {output_file}")
        print(f"Raw JSON: {raw_file}")
        print(f"Estimated cost: ${self.session_costs:.2f}")
        print(f"{'='*70}\n")

        return output_file


async def main():
    searcher = PacerSearcher()
    await searcher.run_family_tree_search()

if __name__ == "__main__":
    asyncio.run(main())
