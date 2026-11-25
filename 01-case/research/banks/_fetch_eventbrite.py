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
    "organizer": "https://www.eventbrite.com/o/47714438313",
}

ctx = ssl.create_default_context()
out = {}
for key, url in URLS.items():
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, context=ctx, timeout=45).read().decode("utf-8", "replace")
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    parsed = []
    for block in blocks:
        try:
            parsed.append(json.loads(block))
        except json.JSONDecodeError:
            pass
    event = next(
        (
            x
            for x in parsed
            if isinstance(x, dict) and x.get("@type") in ("Event", "SocialEvent", "BusinessEvent")
        ),
        None,
    )
    profile = next(
        (x for x in parsed if isinstance(x, dict) and x.get("@type") == "ProfilePage"),
        None,
    )
    # ticket prices from embedded data
    prices = sorted(set(re.findall(r'"value"\s*:\s*"(\d+\.\d{2})"', html)))
    og_desc = re.search(r'<meta property="og:description" content="([^"]*)"', html)
    og_title = re.search(r'<meta property="og:title" content="([^"]*)"', html)
    out[key] = {
        "url": url,
        "og_title": og_title.group(1) if og_title else None,
        "og_description": og_desc.group(1) if og_desc else None,
        "json_ld_event": event,
        "json_ld_profile": profile,
        "embedded_prices": prices,
    }

path = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_eventbrite_batch2.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)
print("wrote", path)
for k, v in out.items():
    ev = v.get("json_ld_event") or {}
    print(k, ":", ev.get("name") or v.get("og_title"))
