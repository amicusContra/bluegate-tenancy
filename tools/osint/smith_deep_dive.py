"""
Smith Household Deep Dive — September 3, 2026
FEAR protocol: Leon showed up and assaulted DaSean. They're hiding something.

This script pulls everything we can get for FREE from CourtListener,
then generates the PACER pull list for the paid documents.
"""

import httpx
import asyncio
import json
from pathlib import Path
from datetime import datetime

RESULTS_DIR = Path(__file__).parent / "results" / "pacer"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

CL_BASE = "https://www.courtlistener.com/api/rest/v3"


async def search_courtlistener(name: str, court: str = "mieb"):
    """Search CourtListener for a person by name in a specific court."""
    async with httpx.AsyncClient(timeout=30, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSINT Research Tool"
    }) as client:
        params = {
            "type": "d",
            "q": f'"{name}"',
            "court": court,
            "order_by": "dateFiled desc",
        }
        try:
            resp = await client.get(f"{CL_BASE}/search/", params=params)
            resp.raise_for_status()
            data = resp.json()
            return data.get("results", [])
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 403:
                print(f"  [403 — rate limited or auth required, trying delay...]")
                await asyncio.sleep(3)
                try:
                    resp = await client.get(f"{CL_BASE}/search/", params=params)
                    if resp.status_code == 200:
                        return resp.json().get("results", [])
                    else:
                        print(f"  [Still {resp.status_code} — skipping]")
                        return []
                except Exception:
                    return []
            print(f"  [HTTP {e.response.status_code} — skipping]")
            return []
        except Exception as e:
            print(f"  [Error: {e} — skipping]")
            return []


async def get_docket_entries(docket_url: str):
    """Get docket entries for a specific docket."""
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(docket_url)
        if resp.status_code == 200:
            return resp.json()
        return None


async def search_party(name: str, courts: list = None):
    """Search for a party name across multiple courts."""
    if courts is None:
        courts = ["mieb", "mied"]

    all_results = []
    for court in courts:
        results = await search_courtlistener(name, court)
        for r in results:
            all_results.append({
                "court": court,
                "case_name": r.get("caseName", ""),
                "docket_number": r.get("docketNumber", ""),
                "date_filed": r.get("dateFiled", ""),
                "date_terminated": r.get("dateTerminated", ""),
                "status": r.get("status", ""),
                "chapter": r.get("chapter", ""),
                "trustee": r.get("trusteeStr", ""),
                "judge": r.get("assignedTo", "") or r.get("referredTo", ""),
                "cl_url": f"https://www.courtlistener.com{r.get('absolute_url', '')}",
            })
    return all_results


async def run_smith_sweep():
    """Run comprehensive searches on all Smith household names."""

    targets = [
        # Core family
        ("Leon Smith", ["mieb", "mied"]),
        ("Leon A Smith", ["mieb", "mied"]),
        ("Leon A. Smith", ["mieb"]),
        ("Shayla Smith", ["mieb", "mied"]),
        ("Marquita Smith", ["mieb"]),
        ("Marquita Renea Smith", ["mieb"]),
        ("Simone Smith", ["mieb"]),
        ("Simone Renee Smith", ["mieb"]),

        # Connected names
        ("Robert Hill", ["mieb"]),
        ("Lemar Jackson", ["mieb", "mied"]),
        ("Lemar G Jackson", ["mieb"]),
        ("Tae Reed", ["mieb", "mied"]),

        # Lake Trust connection
        ("Lake Trust Credit Union", ["mieb", "mied"]),

        # Cross-reference
        ("Tunezha Crowder", ["mieb", "mied"]),
        ("Deanna Mitchell", ["mieb", "mied"]),
    ]

    all_findings = {}

    for name, courts in targets:
        print(f"\n--- Searching: {name} ---")
        results = await search_party(name, courts)

        if results:
            print(f"  FOUND {len(results)} result(s):")
            for r in results:
                terminated = r['date_terminated'] or 'OPEN'
                ch = f" Ch.{r['chapter']}" if r['chapter'] else ""
                print(f"  [{r['court'].upper()}] {r['case_name']}{ch}")
                print(f"    Filed: {r['date_filed']} | Status: {terminated}")
                print(f"    Docket: {r['docket_number']}")
                if r['trustee']:
                    print(f"    Trustee: {r['trustee']}")
                if r['judge']:
                    print(f"    Judge: {r['judge']}")
                print(f"    URL: {r['cl_url']}")
        else:
            print(f"  No results")

        all_findings[name] = results

    return all_findings


async def main():
    print("=" * 70)
    print("SMITH HOUSEHOLD DEEP DIVE — COURTLISTENER SWEEP")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    findings = await run_smith_sweep()

    outfile = RESULTS_DIR / "SMITH_CL_SWEEP_SEP3.json"
    with open(outfile, "w") as f:
        json.dump(findings, f, indent=2, default=str)
    print(f"\nRaw data saved to: {outfile}")

    report_file = RESULTS_DIR / "SMITH_CL_SWEEP_SEP3.md"
    with open(report_file, "w") as f:
        f.write(f"# Smith Household — CourtListener Sweep\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Trigger:** Leon Smith assaulted DaSean Sep 2 — FEAR protocol\n\n")

        for name, results in findings.items():
            f.write(f"## {name}\n\n")
            if not results:
                f.write("No federal court results found.\n\n")
                continue

            f.write(f"**{len(results)} result(s) found:**\n\n")
            f.write("| Court | Case | Chapter | Filed | Status | Trustee |\n")
            f.write("|-------|------|---------|-------|--------|---------|\n")
            for r in results:
                ch = r['chapter'] or '-'
                terminated = r['date_terminated'] or 'OPEN'
                trustee = r['trustee'] or '-'
                f.write(f"| {r['court'].upper()} | [{r['case_name']}]({r['cl_url']}) | {ch} | {r['date_filed']} | {terminated} | {trustee} |\n")
            f.write("\n")

        f.write("---\n\n## PACER PULL PRIORITIES — SMITH HOUSEHOLD\n\n")
        f.write("### HIGHEST PRIORITY\n\n")
        f.write("1. **26-47542** — Marquita Smith, 3rd BK (Jul 2026, ACTIVE)\n")
        f.write("   - Schedules A/B (all assets under oath)\n")
        f.write("   - Schedule D (Lake Trust mortgage as secured creditor)\n")
        f.write("   - Schedule I (income — does she disclose Leon's USPS salary?)\n")
        f.write("   - SOFA (Statement of Financial Affairs — all transfers in last 2 years)\n")
        f.write("   - **KEY QUESTION:** Did she disclose the West Point sale ($34K, May 2026)?\n\n")
        f.write("2. **25-46692** — Marquita Smith, 1st BK (Jun 30 2025, DISMISSED)\n")
        f.write("   - Filed SAME DAY as $68K Lake Trust mortgage recorded\n")
        f.write("   - Schedules will show if mortgage was disclosed\n")
        f.write("   - Dismissal order will state the reason (means test? failure to file?)\n\n")
        f.write("3. **26-49404** — Simone Renee Smith, New BK (Aug 24 2026)\n")
        f.write("   - Petition shows address — CONFIRM IF DRESDEN\n")
        f.write("   - If Dresden: two household members filing BK within 8 weeks\n\n")
        f.write("### HIGH PRIORITY\n\n")
        f.write("4. **25-47952** — Marquita Smith, 2nd BK (Aug 7 2025, Ch.13)\n")
        f.write("   - Plan: proposed payments and creditor treatment\n")
        f.write("   - Is Leon listed as co-debtor?\n\n")
        f.write("5. **18-46548** — Simone Smith (May 2018, Ch.7 discharged)\n")
        f.write("   - Petition address confirms identity\n\n")
        f.write("### NEW PARTY SEARCHES\n\n")
        f.write("Run these through PACER Case Locator (pcl.uscourts.gov):\n\n")
        f.write("| Name | Why |\n")
        f.write("|------|-----|\n")
        f.write("| Leon Smith / Leon A Smith | Is he co-debtor on any of Marquita's filings? Any civil suits? |\n")
        f.write("| Shayla Smith | Confirm zero exposure — or find hidden cases |\n")
        f.write("| Robert Hill | Appeared on forms. Possibly Marquita's father (maiden name?) |\n")
        f.write("| Lemar G Jackson | Co-taxpayer on Marquita's West Point property |\n")
        f.write("| Tae Reed | Son (Marquita's). Any court exposure? |\n")
        f.write("| Lake Trust Credit Union | Any litigation as party? Regulatory actions? |\n")

    print(f"Report saved to: {report_file}")

    print("\n" + "=" * 70)
    print("WHAT TO PULL FROM PACER (Smith household)")
    print("=" * 70)
    print("""
HIGHEST PRIORITY — Pull these FIRST:

1. Case 26-47542 (Marquita, 3rd BK, Jul 2026 — ACTIVE)
   -> Schedules A/B, D, E/F, I, J + SOFA + creditor matrix
   -> WHERE DID THE $68K GO? WHERE DID THE $34K GO?

2. Case 25-46692 (Marquita, 1st BK, Jun 30 2025 — DISMISSED)
   -> Schedules + dismissal order
   -> WAS THE LAKE TRUST MORTGAGE DISCLOSED?

3. Case 26-49404 (Simone Renee Smith, Aug 24 2026)
   -> Petition (page 1 = name, address, SSN last 4)
   -> IS THIS OUR SIMONE? IS SHE AT DRESDEN?

HIGH PRIORITY:

4. Case 25-47952 (Marquita, 2nd BK, Aug 7 2025, Ch.13)
   -> Plan + creditor matrix
   -> IS LEON A CO-DEBTOR?

5. Case 18-46548 (Simone Smith, May 2018, Ch.7)
   -> Petition only — confirm address

PARTY SEARCHES (PACER Case Locator):
   -> Leon Smith / Leon A Smith (E.D. Mich)
   -> Shayla Smith (E.D. Mich)
   -> Robert Hill (E.D. Mich)
   -> Lemar G Jackson (E.D. Mich)
""")


if __name__ == "__main__":
    asyncio.run(main())

