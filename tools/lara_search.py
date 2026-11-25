#!/usr/bin/env python3
"""
LARA MiBusiness Registry Search Tool
Queries Michigan business entity records via the MiBusiness Registry API.

Usage:
    python lara_search.py "inner link"
    python lara_search.py "banks strategy"
    python lara_search.py 801470477          # search by entity ID
    python lara_search.py --detail 801470477  # get full entity detail
    python lara_search.py --batch names.txt   # batch search from file

API endpoint discovered via browser intercept Oct 4, 2026.
Base: https://mibusinessregistry.lara.state.mi.us
Search: /api/businessEntitySearch/webSearch
Detail: /api/businessEntitySearch/businessEntityDetail/{entityId}
"""

import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error
import ssl

BASE = "https://mibusinessregistry.lara.state.mi.us"
SEARCH_EP = "/api/businessEntitySearch/webSearch"
DETAIL_EP = "/api/businessEntitySearch/businessEntityDetail"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": f"{BASE}/search/business",
    "Origin": BASE,
}

ctx = ssl.create_default_context()


def search(term: str) -> list:
    """Search for a business entity by name or ID number."""
    encoded = urllib.parse.quote(term, safe="")
    url = f"{BASE}{SEARCH_EP}?SEARCH_VALUE={encoded}&SearchByOption=-1&QueryTypeId=1&BusinessRecordTypeId=0&BusinessStatusTypeId=0"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return data
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        if "challenge" in body.lower() or "cloudflare" in body.lower():
            print("⚠ Cloudflare challenge detected — may need browser cookies.", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []


def detail(entity_id: str) -> dict:
    """Get detailed entity info by LARA entity ID."""
    url = f"{BASE}{DETAIL_EP}/{entity_id}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return {}


def format_result(item: dict) -> str:
    """Format a single search result for display."""
    lines = []
    name = item.get("entityName", item.get("name", "?"))
    eid = item.get("entityId", item.get("id", "?"))
    status = item.get("entityStatusTypeName", item.get("status", "?"))
    etype = item.get("entityTypeName", item.get("type", "?"))
    agent = item.get("residentAgentName", item.get("agent", "?"))
    filed = item.get("initialFilingDate", item.get("filingDate", "?"))
    ar = item.get("arStandingTypeName", item.get("arStanding", "?"))
    lines.append(f"  {name}")
    lines.append(f"    ID: {eid} | Status: {status} | Type: {etype}")
    lines.append(f"    Agent: {agent} | Filed: {filed} | AR: {ar}")
    return "\n".join(lines)


def format_detail(d: dict) -> str:
    """Format detailed entity info."""
    lines = [f"{'='*60}"]
    for k, v in sorted(d.items()):
        if v and v != "null":
            lines.append(f"  {k}: {v}")
    lines.append(f"{'='*60}")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "--detail" and len(sys.argv) >= 3:
        eid = sys.argv[2]
        print(f"Fetching detail for entity {eid}...")
        d = detail(eid)
        if d:
            print(format_detail(d))
            print(json.dumps(d, indent=2))
        else:
            print("No data returned.")
        return

    if sys.argv[1] == "--batch" and len(sys.argv) >= 3:
        with open(sys.argv[2]) as f:
            terms = [line.strip() for line in f if line.strip()]
        print(f"Batch searching {len(terms)} terms...")
        for i, term in enumerate(terms):
            print(f"\n[{i+1}/{len(terms)}] Searching: {term}")
            results = search(term)
            if isinstance(results, list):
                print(f"  Found {len(results)} results")
                for r in results:
                    print(format_result(r))
            else:
                print(f"  Response: {type(results)}")
                print(f"  {json.dumps(results, indent=2)[:500]}")
            time.sleep(1)
        return

    term = " ".join(sys.argv[1:])
    print(f"Searching LARA for: {term}")
    results = search(term)

    if isinstance(results, list):
        print(f"Found {len(results)} results:\n")
        for r in results:
            print(format_result(r))
    else:
        print(f"Response type: {type(results)}")
        print(json.dumps(results, indent=2)[:2000])


if __name__ == "__main__":
    main()
