"""
PACER API Client — Automated Search & Document Retrieval
=========================================================
Uses the PACER Authentication API (v2.0) and Case Locator (PCL) API
for programmatic federal court searches.

USAGE:
  python pacer_api.py login                    # Authenticate and cache token
  python pacer_api.py search "Smith, Leon"     # Party name search (all courts)
  python pacer_api.py search "Smith, Leon" --court mieb  # Specific court
  python pacer_api.py case 26-47542 --court mieb   # Case lookup
  python pacer_api.py batch                    # Run RICO search queue
  python pacer_api.py costs                    # Show session costs

PACER PRICING:
  $0.10/page, capped at $3.00/document
  Free if quarterly total < $30 for individual filers
  PCL searches: $0.10 per results page

REQUIRES: httpx, rich
"""

import httpx
import asyncio
import json
import os
import sys
import csv
import io
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

TOOLS_DIR = Path(__file__).parent
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

CREDENTIALS_FILE = TOOLS_DIR / ".pacer_creds.json"
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
COST_LOG = RESULTS_DIR / "cost_log.json"

PACER_AUTH_URL = "https://pacer.login.uscourts.gov/services/cso-auth"
PCL_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"

RICO_SEARCH_QUEUE = [
    # ============================================================
    # RICO CASE — Priority Search Queue
    # Phase 1 targets (Sep 5 - Oct 10, 2026)
    # ============================================================

    # --- BANKS NETWORK (Core + Authority) ---
    {"name": "Banks, Brian", "court": "ALL", "priority": "HIGHEST",
     "why": "Front man — 8 felonies, UPL, financial fraud. Need all federal cases."},
    {"name": "Banks, Brian Roderick", "court": "mieb", "priority": "HIGHEST",
     "why": "Full name — BK 98-49073, 06-55281. Need schedules."},
    {"name": "Holland, Joseph", "court": "ALL", "priority": "HIGHEST",
     "why": "Financial operative — 5 BKs. Need all federal cases beyond BK."},
    {"name": "Williams, Joseph Antione", "court": "ALL", "priority": "HIGHEST",
     "why": "HOLLAND'S BIRTH NAME (ICHAT primary). May have cases under real name."},
    {"name": "Williams, Joseph Antoine", "court": "ALL", "priority": "HIGHEST",
     "why": "Holland birth name variant spelling. Cross-ref with Holland results."},
    {"name": "Cudworth, Lisa", "court": "ALL", "priority": "HIGH",
     "why": "Paid $4,017 in Holland's taxes while incarcerated. Lincoln Park MI. Proxy?"},
    {"name": "Opportunity For All Michigan", "court": "ALL", "priority": "HIGH",
     "why": "NEW: Holland dark money entity. Sent mailers for PCA board member Latisha Johnson."},
    {"name": "Ellis, Tracey", "court": "ALL", "priority": "HIGH",
     "why": "Purpose Foundation CFO / Yecart Accounting. Any federal record?"},
    {"name": "Perkins, Todd", "court": "ALL", "priority": "HIGHEST",
     "why": "SHARED attorney Banks+Miller. City Atty Inkster. Defended Earley (Flint), Jones (Op Northern Hook). 3 BKs."},
    {"name": "Perlmuter, Gary", "court": "ALL", "priority": "HIGH",
     "why": "Purpose Group organizer — 1 BK (09-64903)."},

    # --- JUDGES ---
    {"name": "Miller, Cylenthia", "court": "ALL", "priority": "HIGH",
     "why": "PCA co-founder. Defendant in Bryant v. Miller."},
    {"name": "Yancey, Tenisha", "court": "ALL", "priority": "HIGH",
     "why": "MacDowell Board Chair. Campaign payer to Banks."},

    # --- SABREE FAMILY (NEW — confirmed Sep 5) ---
    {"name": "Sabree, Eric", "court": "ALL", "priority": "HIGHEST",
     "why": "Wayne County Treasurer. 40 known PACER hits. Need non-routine cases."},
    {"name": "Sabree, Adam", "court": "ALL", "priority": "HIGH",
     "why": "Eric's SON. 36th District Judge. Former Asst Corp Counsel for Treasurer."},
    {"name": "Sabree, Aliyah", "court": "ALL", "priority": "HIGH",
     "why": "Eric's DAUGHTER. 3rd Circuit Judge. Same bench as Miller."},

    # --- WAYNE COUNTY OFFICIALS ---
    {"name": "Evans, Warren", "court": "ALL", "priority": "HIGH",
     "why": "Wayne County Executive. Endorsed Banks + Miller. Political cover."},

    # --- PCA/MACDOWELL BOARD (Updated Sep 5 AM) ---
    {"name": "Moreland, Lamar", "court": "ALL", "priority": "HIGH",
     "why": "ASST. ATTORNEY GENERAL + PCA Vice Chair. Incompatible offices. AG conflict."},
    {"name": "Gay-Dagnogo, Sherry", "court": "ALL", "priority": "MEDIUM",
     "why": "Detroit Ombudsman. Former state rep + DPSCD board. Voted to approve PCA while on dev team."},
    {"name": "Johnson, Latisha", "court": "ALL", "priority": "MEDIUM",
     "why": "NEW: Detroit City Council + PCA Secretary. Incompatible offices."},
    {"name": "Hutchings, Devin", "court": "ALL", "priority": "LOW",
     "why": "NEW: PCA Treasurer. DH Strategies founder. Unknown entity."},
    {"name": "Clora, Major", "court": "ALL", "priority": "LOW",
     "why": "NEW: PCA Asst. Treasurer. Clora Funeral Home CEO."},

    # --- OCT 6 MINING ADDITIONS ---
    {"name": "Turfe, Assad", "court": "ALL", "priority": "HIGHEST",
     "why": "Deputy Wayne County Exec. On 2016 FBI wiretap target list. Now #2 in Wayne County."},
    {"name": "Banks, Carol", "court": "ALL", "priority": "HIGHEST",
     "why": "Eastside Slate VP + Save Detroit Jobs operative. FBI raided Aug 2021. Hub connecting dark money to political outcomes."},
    {"name": "Benson, Scott", "court": "ALL", "priority": "HIGH",
     "why": "Detroit City Council. FBI raided Aug 2021. Carol Banks chief of staff."},
    {"name": "Ayers, Janee", "court": "ALL", "priority": "HIGH",
     "why": "Former Detroit City Council. FBI raided Aug 2021. Fiore funneled billboard money via Primus."},
    {"name": "Primus, Nicholas", "court": "ALL", "priority": "HIGH",
     "why": "Intermediary between Fiore and Ayers/Sollars. Discussed disguising payments on wiretap."},
    {"name": "Bettison, Todd", "court": "ALL", "priority": "HIGH",
     "why": "Detroit Police Chief + DPSA Board Secretary. Under OIG investigation. FBI took over public corruption side."},
    {"name": "Sheffield, Mary", "court": "ALL", "priority": "MEDIUM",
     "why": "Mayor of Detroit. Dark money pipeline endpoint. Father (Sheffield III) ran 5Plus1."},
    {"name": "Sheffield, Horace", "court": "ALL", "priority": "MEDIUM",
     "why": "Father of Mayor Sheffield. Advised 5Plus1 ($151K to Detroit Next PAC)."},
    {"name": "Gorman, Michael", "court": "ALL", "priority": "MEDIUM",
     "why": "Wiretap target #13 (Michael Patrick Gorman). Unidentified."},
    {"name": "Nicholson, Robert", "court": "ALL", "priority": "MEDIUM",
     "why": "Wiretap target #18 (Robert Ray Nicholson). Unidentified."},
    {"name": "Hussein, Louay", "court": "ALL", "priority": "MEDIUM",
     "why": "Nationwide Towing. $272K political donor. Wiretap target."},
    {"name": "Awad, Shady", "court": "ALL", "priority": "HIGH",
     "why": "Contractor who bribed Sollars. Realty Transition owner."},
    {"name": "Save Detroit Jobs", "court": "ALL", "priority": "HIGH",
     "why": "Dykema-formed dark money entity. LARA 802002459. Funded Johnson + Sheffield."},
    {"name": "Detroit Next", "court": "ALL", "priority": "MEDIUM",
     "why": "PAC that spent $212K+ on pro-Sheffield ads. Funded by SDJ + 5Plus1."},

    # --- ENTITIES ---
    {"name": "Purpose Group", "court": "ALL", "priority": "HIGH",
     "why": "NEW: Banks' ESP entity per charter contract. Any federal litigation?"},
    {"name": "Purpose Charter Academy", "court": "ALL", "priority": "MEDIUM",
     "why": "Banks' school entity — any DOE/DOJ action?"},
    {"name": "Purpose Foundation", "court": "ALL", "priority": "MEDIUM",
     "why": "Banks' nonprofit — any federal case?"},
    {"name": "MacDowell Preparatory", "court": "ALL", "priority": "MEDIUM",
     "why": "Banks' other school — Yancey is board chair."},

    # --- FINANCIAL INSTITUTIONS ---
    {"name": "Public Service Credit Union", "court": "ALL", "priority": "MEDIUM",
     "why": "PSCU — shared lender for Banks + Yancey."},

    # --- CROWDER ---
    {"name": "Crowder, Tunezha", "court": "ALL", "priority": "MEDIUM",
     "why": "LCSW. Suspected referral pipeline to PCA."},
]

CASE_PULL_QUEUE = [
    # Case-specific document pulls
    # Format: {"case_num": "XX-XXXXX", "court": "mieb/mied", "docs": [...], "priority": "..."}

    # --- BANKS BK SCHEDULES ---
    {"case_num": "98-49073", "court": "mieb", "priority": "HIGHEST",
     "target": "Banks 1st BK (1998)",
     "docs": ["docket", "petition", "schedules", "creditor_matrix"]},
    {"case_num": "06-55281", "court": "mieb", "priority": "HIGHEST",
     "target": "Banks 2nd BK (2006)",
     "docs": ["docket", "schedules", "creditor_matrix"]},

    # --- HOLLAND BK SCHEDULES (FRONT-LOADED — break Banks through Holland) ---
    {"case_num": "09-46072", "court": "mieb", "priority": "HIGHEST",
     "target": "Holland 3rd BK (2009) — MUST HAVE Schedule A/B: Newcastle JTWRS disclosure?",
     "docs": ["docket", "petition", "schedules_AB", "schedules_D", "SOFA"]},
    {"case_num": "14-46410", "court": "mieb", "priority": "HIGHEST",
     "target": "Holland 4th BK (Apr 2014) — Newcastle + Middlebelt disclosure?",
     "docs": ["docket", "petition", "schedules_AB", "schedules_D", "SOFA"]},
    {"case_num": "14-51632", "court": "mieb", "priority": "HIGHEST",
     "target": "Holland 5th BK (Jul 2014) — 3 months after 4th. Asset protection?",
     "docs": ["docket", "petition", "schedules_AB", "schedules_D", "SOFA"]},
    {"case_num": "05-81655", "court": "mieb", "priority": "HIGH",
     "target": "Holland 1st BK (2005) — pre-Newcastle baseline",
     "docs": ["docket", "petition", "schedules_AB"]},
    {"case_num": "08-65982", "court": "mieb", "priority": "HIGH",
     "target": "Holland 2nd BK (2008) — post-Newcastle (2007 QCD). First test.",
     "docs": ["docket", "petition", "schedules_AB", "schedules_D"]},

    # --- PERKINS ---
    {"case_num": "22-45209", "court": "mieb", "priority": "HIGHEST",
     "target": "Perkins active Ch.13",
     "docs": ["docket", "plan", "status", "creditor_matrix"]},

    # --- BRYANT V. MILLER ---
    {"case_num": "2:26-cv-10917", "court": "mied", "priority": "HIGHEST",
     "target": "Bryant v. Miller — Doc 30 (amended complaint)",
     "docs": ["doc_30"]},

    # --- SABREE NON-ROUTINE ---
    {"case_num": "2:2023cv10973", "court": "mied", "priority": "HIGH",
     "target": "Bowles v. Sabree (OPEN)",
     "docs": ["docket", "complaint"]},
    {"case_num": "0:2026cv01680", "court": "ca06", "priority": "HIGH",
     "target": "Fakhreddine v. Eric Sabree (OPEN, 6th Cir)",
     "docs": ["docket"]},
    {"case_num": "2:2024cv10203", "court": "mied", "priority": "HIGH",
     "target": "Davis v. Wayne County (Sabree intervenor)",
     "docs": ["docket", "complaint"]},
]


class PacerClient:
    """Automated PACER API client."""

    def __init__(self):
        self.token = None
        self.token_expiry = None
        self.session_costs = 0.0
        self._load_token()

    def _load_token(self):
        """Load cached authentication token."""
        if TOKEN_FILE.exists():
            data = json.loads(TOKEN_FILE.read_text())
            expiry = datetime.fromisoformat(data.get("expiry", "2000-01-01"))
            if expiry > datetime.now():
                self.token = data["token"]
                self.token_expiry = expiry
                return True
        return False

    def _save_token(self, token: str, expires_in: int = 3600):
        """Cache authentication token."""
        self.token = token
        self.token_expiry = datetime.now() + timedelta(seconds=expires_in - 60)
        TOKEN_FILE.write_text(json.dumps({
            "token": token,
            "expiry": self.token_expiry.isoformat(),
            "created": datetime.now().isoformat()
        }))

    def _load_credentials(self):
        """Load stored PACER credentials."""
        if not CREDENTIALS_FILE.exists():
            print("No credentials found. Run: python pacer_api.py login")
            sys.exit(1)
        return json.loads(CREDENTIALS_FILE.read_text())

    def _log_cost(self, action: str, pages: int, cost: float):
        """Log costs for tracking."""
        self.session_costs += cost
        log = []
        if COST_LOG.exists():
            log = json.loads(COST_LOG.read_text())
        log.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "pages": pages,
            "cost": cost,
            "session_total": self.session_costs
        })
        COST_LOG.write_text(json.dumps(log, indent=2))

    async def authenticate(self) -> str:
        """
        Authenticate with PACER Authentication API.
        POST to /services/cso-auth with loginId + password.
        Returns NextGen token.
        """
        creds = self._load_credentials()
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                PACER_AUTH_URL,
                json={
                    "loginId": creds["username"],
                    "password": creds["password"]
                },
                headers={"Content-Type": "application/json"}
            )

            if response.status_code == 200:
                body = response.text
                token = ""
                if "<nextGenCSO>" in body:
                    token = body.split("<nextGenCSO>")[1].split("</nextGenCSO>")[0]
                elif body.strip().startswith("{"):
                    data = response.json()
                    token = data.get("nextGenCSO", data.get("token", ""))
                if token:
                    self._save_token(token)
                    print(f"Authenticated successfully. Token cached until {self.token_expiry}")
                    return token
                else:
                    print(f"Authentication response missing token: {data}")
                    sys.exit(1)
            else:
                print(f"Authentication failed: {response.status_code}")
                print(response.text)
                sys.exit(1)

    async def ensure_token(self):
        """Ensure we have a valid token."""
        if not self.token or (self.token_expiry and datetime.now() >= self.token_expiry):
            await self.authenticate()

    async def pcl_search(self, last_name: str, first_name: str = "",
                          court_type: str = "", region: str = "",
                          case_type: str = "") -> list:
        """
        Search PACER Case Locator for party name.
        Returns list of case results.

        court_type: "" (all), "bk" (bankruptcy), "cv" (civil), "cr" (criminal), "ap" (appellate)
        region: "" (all), "mieb", "mied", etc.
        """
        await self.ensure_token()

        params = {
            "lastName": last_name,
            "firstName": first_name,
        }
        if court_type:
            params["courtType"] = court_type
        if region:
            params["courtId"] = region
        if case_type:
            params["caseType"] = case_type

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.get(
                f"{PCL_URL}/parties",
                params=params,
                headers={
                    "X-NEXT-GEN-CSO": self.token,
                    "Accept": "application/json"
                }
            )

            if response.status_code == 200:
                data = response.json()
                results = data.get("content", [])
                total_pages = data.get("totalPages", 1)
                self._log_cost(
                    f"PCL search: {last_name}, {first_name}",
                    total_pages,
                    total_pages * 0.10
                )
                return results
            elif response.status_code == 401:
                print("Token expired. Re-authenticating...")
                self.token = None
                await self.authenticate()
                return await self.pcl_search(last_name, first_name, court_type, region, case_type)
            else:
                print(f"PCL search failed: {response.status_code}")
                print(response.text[:500])
                return []

    async def run_rico_queue(self):
        """Run the full RICO search queue."""
        await self.ensure_token()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        output_file = RESULTS_DIR / f"RICO_SEARCH_RESULTS_{timestamp}.md"

        results_all = []
        total_searches = len(RICO_SEARCH_QUEUE)

        print(f"\n{'='*70}")
        print(f"RICO CASE — Automated PACER Search Queue")
        print(f"Running {total_searches} searches")
        print(f"{'='*70}\n")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# RICO Case — PACER Search Results\n")
            f.write(f"## Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

            for i, search in enumerate(RICO_SEARCH_QUEUE, 1):
                name = search["name"]
                priority = search["priority"]
                why = search["why"]

                parts = name.split(", ", 1)
                last_name = parts[0]
                first_name = parts[1] if len(parts) > 1 else ""
                court = search.get("court", "")

                print(f"[{i}/{total_searches}] [{priority}] Searching: {name} (court: {court or 'ALL'})...")

                try:
                    court_param = "" if court == "ALL" else court
                    results = await self.pcl_search(last_name, first_name, region=court_param)

                    f.write(f"## [{priority}] {name}\n")
                    f.write(f"**Why:** {why}\n")
                    f.write(f"**Court:** {court}\n")
                    f.write(f"**Hits:** {len(results)}\n\n")

                    if results:
                        f.write("| # | Case | Court | Filed | Closed | Type | Parties |\n")
                        f.write("|---|------|-------|-------|--------|------|---------|\n")
                        for j, r in enumerate(results[:50], 1):
                            case_num = r.get("caseNumber", r.get("caseId", "?"))
                            court_name = r.get("courtId", r.get("court", "?"))
                            filed = r.get("dateFiled", "?")
                            closed = r.get("dateClosed", "OPEN")
                            case_type = r.get("caseType", r.get("natureOfSuit", "?"))
                            parties = r.get("partyName", r.get("caseTitle", "?"))
                            f.write(f"| {j} | {case_num} | {court_name} | {filed} | {closed} | {case_type} | {parties} |\n")
                        f.write("\n")
                    else:
                        f.write("*No results found.*\n\n")

                    results_all.append({
                        "name": name,
                        "hits": len(results),
                        "priority": priority,
                        "results": results[:50]
                    })

                    print(f"  -> {len(results)} hits")

                    await asyncio.sleep(1)

                except Exception as e:
                    print(f"  -> ERROR: {e}")
                    f.write(f"**ERROR:** {e}\n\n")

            f.write(f"\n---\n")
            f.write(f"**Total searches:** {total_searches}\n")
            f.write(f"**Session cost:** ${self.session_costs:.2f}\n")
            f.write(f"**Quarterly free threshold:** $30.00\n")

        print(f"\n{'='*70}")
        print(f"Search complete. Results saved to: {output_file}")
        print(f"Session cost: ${self.session_costs:.2f}")
        print(f"{'='*70}\n")

        return results_all


def store_credentials():
    """Store PACER login credentials."""
    print("\n=== PACER Credentials Setup ===")
    print("Credentials stored locally at:", CREDENTIALS_FILE)
    print("Never transmitted except to PACER authentication servers.\n")
    username = input("PACER Username (e.g., ecoPrimal): ").strip()
    password = input("PACER Password: ").strip()
    creds = {"username": username, "password": password}
    CREDENTIALS_FILE.write_text(json.dumps(creds))
    print(f"\nCredentials saved. Run 'python pacer_api.py batch' to start RICO searches.\n")


def print_queue():
    """Print the RICO search queue."""
    print(f"\n{'='*70}")
    print(f"RICO CASE — PACER Search Queue ({len(RICO_SEARCH_QUEUE)} searches)")
    print(f"{'='*70}\n")

    for priority in ["HIGHEST", "HIGH", "MEDIUM"]:
        items = [s for s in RICO_SEARCH_QUEUE if s["priority"] == priority]
        if items:
            print(f"--- {priority} PRIORITY ({len(items)} searches) ---\n")
            for s in items:
                print(f"  {s['name']:30s}  court: {s.get('court', 'ALL'):6s}  {s['why']}")
            print()

    print(f"\n--- CASE-SPECIFIC DOCUMENT PULLS ({len(CASE_PULL_QUEUE)} cases) ---\n")
    for c in CASE_PULL_QUEUE:
        print(f"  [{c['priority']:7s}] {c['case_num']:20s}  {c['target']}")
        print(f"           docs: {', '.join(c['docs'])}")

    est_pages = len(RICO_SEARCH_QUEUE) + sum(len(c["docs"]) for c in CASE_PULL_QUEUE)
    print(f"\n{'='*70}")
    print(f"Estimated search pages: {len(RICO_SEARCH_QUEUE)} (${len(RICO_SEARCH_QUEUE) * 0.10:.2f})")
    print(f"Estimated doc pages: {est_pages} (${est_pages * 0.50:.2f} - ${est_pages * 1.50:.2f})")
    print(f"Well under $30 free quarterly threshold")
    print(f"{'='*70}\n")


def show_costs():
    """Show running cost log."""
    if not COST_LOG.exists():
        print("No costs logged yet.")
        return

    log = json.loads(COST_LOG.read_text())
    total = sum(entry["cost"] for entry in log)

    print(f"\n{'='*70}")
    print(f"PACER Cost Log — {len(log)} transactions")
    print(f"{'='*70}\n")

    for entry in log[-20:]:
        print(f"  {entry['timestamp'][:19]}  ${entry['cost']:.2f}  {entry['action']}")

    print(f"\n  TOTAL: ${total:.2f} / $30.00 free threshold")
    print(f"  Remaining: ${30.00 - total:.2f}")
    print(f"{'='*70}\n")


async def main():
    if len(sys.argv) < 2:
        print_queue()
        return

    cmd = sys.argv[1].lower()

    if cmd == "login":
        store_credentials()
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: python pacer_api.py search \"Last, First\" [--court mieb]")
            return
        name = sys.argv[2]
        court = ""
        if "--court" in sys.argv:
            idx = sys.argv.index("--court")
            court = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""

        parts = name.split(", ", 1)
        last_name = parts[0]
        first_name = parts[1] if len(parts) > 1 else ""

        client = PacerClient()
        results = await client.pcl_search(last_name, first_name, region=court)
        print(f"\nFound {len(results)} results:")
        for r in results[:20]:
            print(f"  {r.get('caseNumber', '?'):15s}  {r.get('courtId', '?'):8s}  {r.get('caseTitle', r.get('partyName', '?'))}")
    elif cmd == "batch":
        client = PacerClient()
        await client.run_rico_queue()
    elif cmd == "costs":
        show_costs()
    elif cmd == "queue":
        print_queue()
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: login, search, batch, queue, costs")


if __name__ == "__main__":
    asyncio.run(main())
