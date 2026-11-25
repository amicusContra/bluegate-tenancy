"""Final check-detail parse: sum every disbursement line ending in R -$."""
import re
import json
from collections import defaultdict

raw = open(
    r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_tmp_checkdetail.txt",
    encoding="utf-8",
).read()
raw = re.sub(r"---PAGE \d+---[^\n]*\n", "", raw)
raw = re.sub(r"MacDowell Preparatory Academy\nCheck Detail\nJuly 2023 - June 2024\n[^\n]*\n", "", raw)
raw = re.sub(r"DATE TRANSACTION\s*\nTYPE\s*\nNUM NAME MEMO/DESCRIPTION CLR AMOUNT\n", "", raw)

entries = []

# Checks
for m in re.finditer(
    r"(\d{2}/\d{2}/\d{4})\s+Check\s+(\d+)\s+(.+?)\s+R\s+-([\d,]+\.\d{2})",
    raw,
):
    entries.append(
        {
            "date": m.group(1),
            "type": "Check",
            "num": m.group(2),
            "payee": m.group(3).strip(),
            "amount": float(m.group(4).replace(",", "")),
        }
    )

# Bill payments: num + payee line then R -amount
for m in re.finditer(
    r"(\d{2}/\d{2}/\d{4})\s+Bill Payment\s*\(Check\)\s*\n\s*(\d{3,6})\s+(.+?)\nR\s+-([\d,]+\.\d{2})",
    raw,
    re.S,
):
    payee = re.sub(r"\s+", " ", m.group(3)).strip()
    entries.append(
        {
            "date": m.group(1),
            "type": "Bill Payment",
            "num": m.group(2),
            "payee": payee,
            "amount": float(m.group(4).replace(",", "")),
        }
    )

# Expenditures (card/ACH)
for m in re.finditer(
    r"(\d{2}/\d{2}/\d{4})\s+Expenditure\s+(.+?)\s+R\s+-([\d,]+\.\d{2})",
    raw,
):
    entries.append(
        {
            "date": m.group(1),
            "type": "Expenditure",
            "num": "",
            "payee": m.group(2).strip(),
            "amount": float(m.group(3).replace(",", "")),
        }
    )

by = defaultdict(float)
cnt = defaultdict(int)
for e in entries:
    p = e["payee"]
    by[p] += e["amount"]
    cnt[p] += 1

def bucket(payee):
    p = payee.lower()
    if any(x in p for x in ["martin luna", "raymond ankrum", "lorilyn"]):
        return "Contracted leadership / CMO-related individuals"
    if "brian banks" in p:
        return "Operator self-dealing (Brian Banks)"
    if "meihn" in p:
        return "Legal — Gregory M. Meihn"
    if "yecart" in p:
        return "Accounting — Yecart"
    if any(x in p for x in ["dte", "comcast", "goto", "water", "industry specific"]):
        return "Utilities / telecom / HVAC"
    if any(x in p for x in ["emc insurance", "us bank"]):
        return "Insurance / bank fees"
    if any(x in p for x in ["imagine", "kendall", "houghton", "curriculum", "savvas", "studies weekly", "great minds", "kiddom", "school specialty", "powerschool", "public consulting", "goguardian"]):
        return "Curriculum / ed-tech"
    if any(x in p for x in ["abm", "matrix", "gm equity", "macro connect", "michigan recreational", "applied innovation", "convergent", "guardian alarm", "bildon", "cintas"]):
        return "Facilities / IT / maintenance"
    if "student transportation" in p or "dht transportation" in p:
        return "Transportation"
    if "property tax" in p or "city of detroit" in p:
        return "Property tax / city"
    if "detroit institute for children" in p or "urban academy" in p:
        return "Student support / SPED vendors"
    if "detroit regional chamber" in p or "national charter" in p or "michigan association" in p:
        return "Memberships / governance orgs"
    if any(x in p for x in ["gift", "camper", "rafeal"]):
        return "Gift cards / unexplained personal"
    if any(x in p for x in ["detroit athletic club", "party", "cater", "restaurant", "chef", "blake", "barrymores"]):
        return "Events / catering / entertainment"
    if any(x in p for x in ["john arnold", "wanda jones", "wyatt jones", "sabrina jackson"]):
        return "Contracted PD / catering individuals"
    return "Other vendors"

cats = defaultdict(float)
for e in entries:
    cats[bucket(e["payee"])] += e["amount"]

network = []
for p, a in sorted(by.items(), key=lambda x: -x[1]):
    pl = p.lower()
    if any(
        k in pl
        for k in [
            "brian banks",
            "meihn",
            "camper",
            "holland",
            "inner link",
            "perkins",
            "purpose group",
            "martin luna",
            "raymond ankrum",
            "yancey",
            "gm equity",
        ]
    ):
        network.append({"payee": p, "total": round(a, 2), "count": cnt[p]})

gift_lines = [e for e in entries if "gift" in e["payee"].lower() or "camper" in e["payee"].lower()]

out = {
    "source": "MacDowell CheckDetail-2023-24.pdf (QuickBooks export, posted macdowellprep.com Feb 2025)",
    "coverage_note": "Reflects disbursements from listed BofA/credit-union accounts; bulk ESP pass-through to Purpose Group LLC may not appear as separate payee lines in this extract.",
    "transaction_count": len(entries),
    "total_disbursements": round(sum(e["amount"] for e in entries), 2),
    "unique_payees": len(by),
    "categories": {k: round(v, 2) for k, v in sorted(cats.items(), key=lambda x: -x[1])},
    "network_flagged_payees": network,
    "gift_card_and_related": gift_lines,
    "meihn_lines": [e for e in entries if "meihn" in e["payee"].lower()],
    "top_50_payees": [
        {"payee": p, "total": round(a, 2), "count": cnt[p]}
        for p, a in sorted(by.items(), key=lambda x: -x[1])[:50]
    ],
    "all_payees_alpha": [
        {"payee": p, "total": round(a, 2), "count": cnt[p]}
        for p, a in sorted(by.items(), key=lambda x: x[0].lower())
    ],
}

path = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_checkdetail_final.json"
json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
print("entries", len(entries), "total", out["total_disbursements"], "payees", len(by))
