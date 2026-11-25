import json
import re
import ssl
import urllib.request

URLS = [
    ("2026_cbc", "https://www.eventbrite.com/e/tickets-at-the-door-michigan-cbc-reception-party-tickets-at-the-door-tickets-1998927506983"),
    ("2024_cbc", "https://www.eventbrite.com/e/michigan-cbc-party-sold-out-limited-tickets-at-the-door-tickets-999744000217"),
    ("2023_cbc", "https://www.eventbrite.com/e/michigan-cbc-party-wchubb-rock-tickets-available-at-the-door-tickets-712493987697"),
    ("2025_cbc", "https://www.eventbrite.com/e/michigans-cbc-after-glow-party-gen-admission-tickets-only-at-door-tickets-1646216841889"),
    ("pca_gala", "https://www.eventbrite.com/e/inaugural-black-tie-gala-purpose-charter-academy-school-for-law-pub-svc-tickets-1979571244882"),
    ("monday_praise", "https://www.eventbrite.com/e/monday-night-praise-tickets-available-at-the-door-tickets-1985098248298"),
]

ctx = ssl.create_default_context()
out = {}
for key, url in URLS:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=45).read().decode("utf-8", "replace")
    meta = {}
    for m in re.finditer(r'<meta\s+([^>]+)>', html):
        tag = m.group(1)
        if 'property="' in tag or 'name="' in tag:
            km = re.search(r'(?:property|name)="([^"]+)"', tag)
            vm = re.search(r'content="([^"]*)"', tag)
            if km and vm:
                meta[km.group(1)] = vm.group(1)
    ld = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            ld.append(json.loads(block))
        except json.JSONDecodeError:
            pass
    event = next(
        (x for x in ld if isinstance(x, dict) and x.get("@type") in ("Event", "SocialEvent", "BusinessEvent")),
        None,
    )
    # ticket prices from page
    prices = sorted(set(re.findall(r"\$\s?(\d+\.\d{2})", html)))
    out[key] = {"url": url, "meta": meta, "json_ld_event": event, "dollar_amounts_in_html": prices}

print(json.dumps(out, indent=2)[:20000])
