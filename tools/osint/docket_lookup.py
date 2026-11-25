"""Look up specific dockets on CourtListener."""
import httpx
import json
import asyncio
import sys


async def lookup_dockets(docket_numbers, court="mieb"):
    async with httpx.AsyncClient(timeout=30) as client:
        for dn in docket_numbers:
            resp = await client.get(
                "https://www.courtlistener.com/api/rest/v4/dockets/",
                params={"docket_number": dn, "court": court},
                headers={"User-Agent": "OSINT-Toolkit/1.0"},
            )
            resp.raise_for_status()
            data = resp.json()
            print(f"=== Docket {dn} ({court}) ===")
            count = data.get("count", 0)
            print(f"Count: {count}")
            for item in data.get("results", []):
                info = {
                    "id": item.get("id"),
                    "case_name": item.get("case_name"),
                    "date_filed": item.get("date_filed"),
                    "date_terminated": item.get("date_terminated"),
                    "docket_number": item.get("docket_number"),
                    "assigned_to_str": item.get("assigned_to_str"),
                    "referred_to_str": item.get("referred_to_str"),
                    "chapter": item.get("chapter"),
                    "trustee_str": item.get("trustee_str"),
                    "nature_of_suit": item.get("nature_of_suit"),
                    "cl_url": f"https://www.courtlistener.com{item['absolute_url']}" if item.get("absolute_url") else None,
                }
                print(json.dumps(info, indent=2))

                # Try to fetch docket entries
                docket_id = item.get("id")
                if docket_id:
                    entry_resp = await client.get(
                        f"https://www.courtlistener.com/api/rest/v4/docket-entries/",
                        params={"docket": docket_id, "order_by": "entry_number"},
                        headers={"User-Agent": "OSINT-Toolkit/1.0"},
                    )
                    if entry_resp.status_code == 200:
                        entries = entry_resp.json()
                        print(f"\nDocket entries: {entries.get('count', 0)}")
                        for entry in entries.get("results", [])[:25]:
                            desc = entry.get("description", "")[:120]
                            print(f"  [{entry.get('date_filed')}] #{entry.get('entry_number')} - {desc}")
                    print()
            print("---\n")


if __name__ == "__main__":
    docket_nums = sys.argv[1:]
    if not docket_nums:
        print("Usage: python docket_lookup.py 18-46548 26-49404")
        sys.exit(1)
    asyncio.run(lookup_dockets(docket_nums))

