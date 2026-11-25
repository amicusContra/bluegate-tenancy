"""
PACER CM/ECF Docket Report Puller
==================================
Uses CM/ECF web interface to pull docket reports for specific cases.
This gets the actual docket sheets (which list all filed documents including schedules).

The CM/ECF docket report URL pattern for MIEB (Michigan Eastern Bankruptcy):
  https://ecf.mieb.uscourts.gov/cgi-bin/DktRpt.pl?CASE_NUMBER

For each case, we pull the docket report HTML, parse it, and identify
Schedule A/B filings (the key documents for bankruptcy fraud theory).
"""

import httpx
import asyncio
import json
import re
from pathlib import Path
from datetime import datetime

TOOLS_DIR = Path(__file__).parent
TOKEN_FILE = TOOLS_DIR / ".pacer_token.json"
RESULTS_DIR = TOOLS_DIR / "results" / "pacer"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

MIEB_BASE = "https://ecf.mieb.uscourts.gov"
MIED_BASE = "https://ecf.mied.uscourts.gov"

CRITICAL_CASES = [
    {
        "label": "Holland BK #3 (2009) — CRITICAL: Newcastle JTWRS on Schedule A/B?",
        "case_num": "09-46072",
        "court": "mieb",
        "base_url": MIEB_BASE,
        "priority": "HIGHEST",
        "look_for": ["Schedule A", "Schedule B", "Schedule A/B", "Real Property",
                      "Statement of Financial Affairs", "SOFA", "Petition"],
    },
    {
        "label": "Holland BK #4 (Apr 2014) — CRITICAL: Filed FROM PRISON",
        "case_num": "14-46410",
        "court": "mieb",
        "base_url": MIEB_BASE,
        "priority": "HIGHEST",
        "look_for": ["Schedule A", "Schedule B", "Schedule A/B", "Real Property",
                      "Statement of Financial Affairs", "SOFA", "Petition"],
    },
    {
        "label": "Holland BK #5 (Jul 2014) — 3 months after #4",
        "case_num": "14-51632",
        "court": "mieb",
        "base_url": MIEB_BASE,
        "priority": "HIGHEST",
        "look_for": ["Schedule A", "Schedule B", "Schedule A/B", "Real Property",
                      "Statement of Financial Affairs", "SOFA", "Petition"],
    },
    {
        "label": "Holland BK #2 (2008) — First post-Newcastle filing",
        "case_num": "08-65982",
        "court": "mieb",
        "base_url": MIEB_BASE,
        "priority": "HIGH",
        "look_for": ["Schedule A", "Schedule B", "Schedule A/B", "Petition"],
    },
    {
        "label": "Banks BK #0 (1997) — NEWLY DISCOVERED 3rd bankruptcy",
        "case_num": "97-45020",
        "court": "mieb",
        "base_url": MIEB_BASE,
        "priority": "HIGH",
        "look_for": ["Petition", "Schedule", "Docket"],
    },
    {
        "label": "Welch BMF (2005) — Sentencing docs",
        "case_num": "05-80955",
        "court": "mied",
        "base_url": MIED_BASE,
        "priority": "MEDIUM",
        "look_for": ["Sentencing", "Plea Agreement", "Judgment"],
    },
]


def load_token():
    if TOKEN_FILE.exists():
        data = json.loads(TOKEN_FILE.read_text())
        return data.get("token")
    return None


async def pull_docket_report(client, case, token):
    """Pull a docket report from CM/ECF."""
    base = case["base_url"]
    case_num = case["case_num"]

    cookies = {"NextGenCSO": token, "PacerPref": "receipt=Y"}

    login_url = f"{base}/cgi-bin/login.pl"
    try:
        r = await client.get(
            login_url,
            params={"login_id": "", "key": token},
            cookies=cookies,
            follow_redirects=True,
            timeout=30,
        )
    except Exception as e:
        return {"error": f"Login failed: {e}"}

    docket_url = f"{base}/cgi-bin/DktRpt.pl"
    try:
        r = await client.post(
            docket_url,
            data={
                "all_case_ids": "on",
                "case_num": case_num,
                "date_range_type": "Filed",
                "output_type": "html",
            },
            cookies=cookies,
            follow_redirects=True,
            timeout=60,
        )

        if r.status_code == 200:
            html = r.text
            return {"html": html, "url": str(r.url), "status": r.status_code}
        else:
            return {"error": f"HTTP {r.status_code}", "url": str(r.url)}

    except Exception as e:
        return {"error": f"Docket pull failed: {e}"}


def parse_docket_html(html, look_for):
    """Extract docket entries from CM/ECF HTML."""
    entries = []

    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL)

    for row in rows:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
        if len(cells) >= 3:
            text = ' '.join(cells).strip()
            text_clean = re.sub(r'<[^>]+>', ' ', text).strip()
            text_clean = re.sub(r'\s+', ' ', text_clean)

            if text_clean and len(text_clean) > 10:
                is_target = any(term.lower() in text_clean.lower() for term in look_for)
                entries.append({
                    "text": text_clean[:300],
                    "is_target": is_target,
                    "has_link": "href=" in text,
                })

    return entries


async def main():
    token = load_token()
    if not token:
        print("No PACER token. Run pacer_reauth.py first.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = RESULTS_DIR / f"CMECF_DOCKET_PULL_{timestamp}.md"

    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# CM/ECF DOCKET REPORTS — {datetime.now().strftime('%B %d, %Y %H:%M')}\n")
            f.write(f"## Holland BK Fraud Theory — Schedule A/B Check\n\n")

            for case in CRITICAL_CASES:
                label = case["label"]
                case_num = case["case_num"]
                priority = case["priority"]

                print(f"\n[{priority}] Pulling docket: {label} ({case_num})...")
                f.write(f"## [{priority}] {label}\n")
                f.write(f"**Case:** {case_num} | **Court:** {case['court'].upper()}\n\n")

                result = await pull_docket_report(client, case, token)

                if "error" in result:
                    print(f"  ERROR: {result['error']}")
                    f.write(f"**ERROR:** {result['error']}\n\n")
                elif "html" in result:
                    html = result["html"]
                    html_file = RESULTS_DIR / f"docket_{case_num.replace('-', '_')}.html"
                    html_file.write_text(html, encoding="utf-8")
                    print(f"  Saved HTML ({len(html)} chars) to {html_file.name}")

                    entries = parse_docket_html(html, case["look_for"])
                    target_entries = [e for e in entries if e["is_target"]]

                    f.write(f"**Docket entries:** {len(entries)} total\n")
                    f.write(f"**Target docs found:** {len(target_entries)}\n\n")

                    if target_entries:
                        f.write("### 🎯 TARGET DOCUMENTS:\n\n")
                        for e in target_entries:
                            f.write(f"- {e['text']}\n")
                        f.write("\n")

                    if entries:
                        f.write("### All docket entries:\n\n")
                        for e in entries[:50]:
                            marker = "🎯 " if e["is_target"] else "   "
                            f.write(f"{marker}{e['text']}\n\n")

                f.write("---\n\n")
                await asyncio.sleep(2)

    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
