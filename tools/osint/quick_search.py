"""Quick targeted search script."""
import httpx
import json
import asyncio
import sys


async def search_courtlistener(name, court=None):
    params = {"q": name, "type": "r", "order_by": "score desc"}
    if court:
        params["court"] = court
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(
            "https://www.courtlistener.com/api/rest/v4/search/",
            params=params,
            headers={"User-Agent": "OSINT-Toolkit/1.0"},
        )
        resp.raise_for_status()
        data = resp.json()
        print(f"Count: {data.get('count')}")
        for item in data.get("results", []):
            print(json.dumps({
                "case": item.get("caseName"),
                "court": item.get("court"),
                "court_citation": item.get("court_citation_string"),
                "date_filed": item.get("dateFiled"),
                "docket_number": item.get("docketNumber"),
                "chapter": item.get("chapter"),
                "trustee_str": item.get("trustee_str"),
                "url": f"https://www.courtlistener.com{item['absolute_url']}"
                if item.get("absolute_url") else None,
                "snippet": (item.get("snippet") or "")[:300],
            }, indent=2))
            print("---")


async def search_docket(docket_id):
    """Fetch full docket details by CourtListener docket ID."""
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(
            f"https://www.courtlistener.com/api/rest/v4/dockets/{docket_id}/",
            headers={"User-Agent": "OSINT-Toolkit/1.0"},
        )
        resp.raise_for_status()
        data = resp.json()
        print(json.dumps({
            "case_name": data.get("case_name"),
            "court": data.get("court"),
            "date_filed": data.get("date_filed"),
            "date_terminated": data.get("date_terminated"),
            "docket_number": data.get("docket_number"),
            "assigned_to_str": data.get("assigned_to_str"),
            "referred_to_str": data.get("referred_to_str"),
            "chapter": data.get("chapter"),
            "trustee_str": data.get("trustee_str"),
            "nature_of_suit": data.get("nature_of_suit"),
            "cause": data.get("cause"),
            "source": data.get("source"),
            "absolute_url": data.get("absolute_url"),
        }, indent=2))

        # Get docket entries
        entries_url = data.get("docket_entries")
        if entries_url:
            resp2 = await client.get(
                entries_url,
                headers={"User-Agent": "OSINT-Toolkit/1.0"},
            )
            if resp2.status_code == 200:
                entries = resp2.json()
                print(f"\nDocket entries: {entries.get('count', 0)}")
                for entry in entries.get("results", [])[:20]:
                    print(f"  [{entry.get('date_filed')}] #{entry.get('entry_number')} - {entry.get('description', '')[:150]}")


async def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "cl_search":
        name = sys.argv[2]
        court = sys.argv[3] if len(sys.argv) > 3 else None
        await search_courtlistener(name, court)
    elif cmd == "cl_docket":
        docket_id = sys.argv[2]
        await search_docket(docket_id)
    else:
        print("Usage:")
        print("  python quick_search.py cl_search 'name' [court_code]")
        print("  python quick_search.py cl_docket DOCKET_ID")
        print("")
        print("Court codes: mieb (E.D. Michigan), miwb (W.D. Michigan)")


if __name__ == "__main__":
    asyncio.run(main())

