"""Robust parse: every line ending with R -amount or Check ... amount."""
import re
import json
from collections import defaultdict

text = open(
    r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_tmp_checkdetail.txt",
    encoding="utf-8",
).read()

# Remove page headers
text = re.sub(r"---PAGE \d+---.*?AMOUNT\n", "", text, flags=re.S)

entries = []
# Pattern 1: single-line Check
for m in re.finditer(
    r"(\d{2}/\d{2}/\d{4})\s+Check\s+(\d+)\s+(.+?)\s+R\s+-([\d,]+\.\d{2})",
    text,
):
    entries.append(
        {
            "date": m.group(1),
            "type": "Check",
            "check_num": m.group(2),
            "payee": m.group(3).strip(),
            "memo": "",
            "amount": float(m.group(4).replace(",", "")),
        }
    )

# Pattern 2: Bill Payment blocks ending with R -amount on own line after name lines
for m in re.finditer(
    r"(\d{2}/\d{2}/\d{4})\s+Bill Payment\s*\(Check\)\s*\n(?:.*?\n)*?\s*(\d{3,6})\s+(.+?)\s*\nR\s+-([\d,]+\.\d{2})",
    text,
    re.S,
):
    entries.append(
        {
            "date": m.group(1),
            "type": "Bill Payment (Check)",
            "check_num": m.group(2),
            "payee": m.group(3).replace("\n", " ").strip(),
            "memo": "",
            "amount": float(m.group(4).replace(",", "")),
        }
    )

# Pattern 3: Expenditure lines
for m in re.finditer(
    r"(\d{2}/\d{2}/\d{4})\s+Expenditure\s+(.+?)\s+R\s+-([\d,]+\.\d{2})",
    text,
):
    entries.append(
        {
            "date": m.group(1),
            "type": "Expenditure",
            "check_num": "",
            "payee": m.group(2).strip(),
            "memo": "",
            "amount": float(m.group(3).replace(",", "")),
        }
    )

# Dedupe by date+check+amount+payee
seen = set()
uniq = []
for e in entries:
    k = (e["date"], e["type"], e["check_num"], e["payee"][:40], e["amount"])
    if k in seen:
        continue
    seen.add(k)
    uniq.append(e)

by_payee = defaultdict(float)
by_count = defaultdict(int)
for e in uniq:
    p = re.sub(r"\s+", " ", e["payee"]).strip()
    by_payee[p] += e["amount"]
    by_count[p] += 1

# Normalize Meihn / Banks names
def norm(name):
    name = re.sub(r"^\d+\s+", "", name)
    return name.strip()

meihn = sum(a for n, a in by_payee.items() if "meihn" in n.lower())
banks = sum(a for n, a in by_payee.items() if "brian banks" in n.lower())
gift = sum(
    e["amount"]
    for e in uniq
    if "gift" in (e["payee"] + e.get("memo", "")).lower()
    or "camper" in e["payee"].lower()
)

out = {
    "transaction_count": len(uniq),
    "total_disbursements": round(sum(e["amount"] for e in uniq), 2),
    "meihn_total": round(meihn, 2),
    "brian_banks_total": round(banks, 2),
    "gift_card_cluster_total": round(gift, 2),
    "top_payees": [
        {"payee": n, "total": round(a, 2), "count": by_count[n]}
        for n, a in sorted(by_payee.items(), key=lambda x: -x[1])
    ],
    "all_entries": uniq,
}
path = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_checkdetail_parsed_v2.json"
json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
print("tx", len(uniq), "total", out["total_disbursements"], "meihn", meihn, "banks", banks, "gift", gift)
