import json
import re
import ssl
import urllib.request

URLS = {
    "2026_cbc": "https://www.eventbrite.com/e/tickets-at-the-door-michigan-cbc-reception-party-tickets-at-the-door-tickets-1998927506983",
    "2024_cbc": "https://www.eventbrite.com/e/michigan-cbc-party-sold-out-limited-tickets-at-the-door-tickets-999744000217",
    "2023_cbc": "https://www.eventbrite.com/e/michigan-cbc-party-wchubb-rock-tickets-available-at-the-door-tickets-712493987697",
    "2025_cbc": "https://www.eventbrite.com/e/michigans-cbc-after-glow-party-gen-admission-tickets-only-at-door-tickets-1646216841889",
    "pca_gala": "https://www.eventbrite.com/e/inaugural-black-tie-gala-purpose-charter-academy-school-for-law-pub-svc-tickets-1979571244882",
    "monday_praise": "https://www.eventbrite.com/e/monday-night-praise-tickets-available-at-the-door-tickets-1985098248298",
}

ctx = ssl.create_default_context()
out = {}
for key, url in URLS.items():
    html = urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}),
        context=ctx,
        timeout=45,
    ).read().decode("utf-8", "replace")
    m = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        html,
        re.S,
    )
    event = None
    tickets = []
    if m:
        data = json.loads(m.group(1))
        pp = data.get("props", {}).get("pageProps", {})
        event = pp.get("event") or pp.get("initialEvent") or pp.get("eventData")
        if isinstance(event, dict):
            tix = event.get("ticket_classes") or event.get("ticketClasses") or []
            for t in tix:
                if isinstance(t, dict):
                    tickets.append(
                        {
                            "name": t.get("name"),
                            "price": t.get("cost") or t.get("display_price"),
                            "free": t.get("free"),
                            "quantity_total": t.get("quantity_total"),
                            "quantity_sold": t.get("quantity_sold"),
                            "sales_end": t.get("sales_end"),
                        }
                    )
    out[key] = {
        "url": url,
        "has_next_data": bool(m),
        "event_keys": list(event.keys()) if isinstance(event, dict) else None,
        "name": event.get("name") if isinstance(event, dict) else None,
        "description": event.get("description") if isinstance(event, dict) else None,
        "summary": event.get("summary") if isinstance(event, dict) else None,
        "start": event.get("start") if isinstance(event, dict) else None,
        "end": event.get("end") if isinstance(event, dict) else None,
        "venue": event.get("venue") if isinstance(event, dict) else None,
        "tickets": tickets,
    }

path = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_eventbrite_nextdata.json"
json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
print("written", path)
for k, v in out.items():
    print(k, "tickets", len(v["tickets"]), "desc_len", len(v.get("description") or v.get("summary") or ""))
