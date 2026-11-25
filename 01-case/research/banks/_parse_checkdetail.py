"""Parse MacDowell CheckDetail-2023-24 extracted text."""
import re
import json
from collections import defaultdict

path = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_tmp_checkdetail.txt"
text = open(path, encoding="utf-8").read()

# Split into transaction blocks starting with MM/DD/YYYY
blocks = re.split(r"(?=\d{2}/\d{2}/\d{4}\s)", text)
entries = []
for block in blocks:
    block = block.strip()
    if not re.match(r"\d{2}/\d{2}/\d{4}", block):
        continue
    lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
    if not lines:
        continue
    header = lines[0]
    m = re.match(
        r"(\d{2}/\d{2}/\d{4})\s+(Expenditure|Check|Bill Payment\s*\(Check\))\s*(.*)",
        header,
        re.I,
    )
    if not m:
        continue
    date, typ, rest = m.group(1), m.group(2), m.group(3).strip()
    body = " ".join(lines[1:])
    full = header + " " + body
    # amount: last occurrence of number with cents
    amts = re.findall(r"-([\d,]+\.\d{2})", full)
    if not amts:
        continue
    amount = float(amts[-1].replace(",", ""))
    # check number
    num_m = re.search(r"\b(\d{5,6})\b", rest)
    check_num = num_m.group(1) if num_m else ""
    # payee: after check num on same line chunk
    payee = rest
    if check_num:
        payee = rest.split(check_num, 1)[-1].strip()
    payee = re.sub(r"\s+R\s+-[\d,]+\.\d{2}.*$", "", payee).strip()
    # memo from following lines before amount line
    memo_parts = []
    for ln in lines[1:]:
        if re.search(r"-[\d,]+\.\d{2}\s*$", ln):
            memo_parts.append(re.sub(r"\s+R\s+-[\d,]+\.\d{2}.*$", "", ln).strip())
            break
        memo_parts.append(ln)
    memo = " ".join(memo_parts).strip()
    entries.append(
        {
            "date": date,
            "type": typ,
            "check_num": check_num,
            "payee": payee,
            "memo": memo,
            "amount": amount,
        }
    )

by_payee = defaultdict(float)
by_count = defaultdict(int)
all_memos = []
for e in entries:
    name = e["payee"] or "(unknown)"
    by_payee[name] += e["amount"]
    by_count[name] += 1
    if e["memo"]:
        all_memos.append(e)

total = sum(e["amount"] for e in entries)

NETWORK_KEYS = [
    "brian banks",
    "purpose group",
    "holland",
    "inner link",
    "perkins",
    "meihn",
    "camper",
    "rafeal",
    "joseph",
    "banks strategy",
    "gm equity",
]

rules = [
    ("CMO / contracted leadership (Luna, Ankrum, Coggins)", ["martin luna", "raymond ankrum", "lorilyn k. coggins"]),
    ("Self-dealing / operator (Brian Banks)", ["brian banks"]),
    ("Legal counsel", ["meihn", "gregory m"]),
    ("Accounting / bookkeeping", ["yecart"]),
    ("Utilities & telecom", ["dte energy", "comcast", "goto communications", "detroit water", "industry specific"]),
    ("Insurance & banking fees", ["emc insurance", "us bank", "pitney bowes"]),
    ("Facilities / maintenance / IT", ["abm", "matrix mechanical", "gm equity", "michigan recreational", "macro connect", "applied innovation", "convergent", "good works", "american leak", "bildon", "cintas", "guardian alarm"]),
    ("Curriculum & ed-tech", ["kendall hunt", "imagine learning", "houghton mifflin", "curriculum associates", "savvas", "studies weekly", "great minds", "kiddom", "school specialty", "powerschool", "public consulting", "goguardian"]),
    ("Student services / SPED", ["detroit institute for children", "urban academy"]),
    ("Transportation", ["student transportation"]),
    ("Property tax", ["property tax", "city of detroit-property"]),
    ("Authorizer / compliance", ["detroit public", "dpscd", "national charter", "michigan association of school"]),
    ("Memberships / chamber", ["detroit regional chamber"]),
    ("Food / events / misc vendors", ["rita", "party source", "restaurant equippers", "national charter schools institute"]),
    ("Gift cards / personal", ["gift card", "camper", "rafeal"]),
    ("Payroll processor / HR", ["integrity business", "convergent"]),
]

cats = defaultdict(float)
for e in entries:
    name = (e["payee"] + " " + e["memo"]).lower()
    assigned = False
    for cat, keys in rules:
        if any(k in name for k in keys):
            cats[cat] += e["amount"]
            assigned = True
            break
    if not assigned:
        cats["Other / unclassified"] += e["amount"]

out = {
    "transaction_count": len(entries),
    "total_disbursements": round(total, 2),
    "unique_payees": len(by_payee),
    "top_payees": [
        {"payee": n, "total": round(a, 2), "count": by_count[n]}
        for n, a in sorted(by_payee.items(), key=lambda x: -x[1])[:80]
    ],
    "network_flagged": [
        {"payee": n, "total": round(a, 2), "count": by_count[n]}
        for n, a in sorted(by_payee.items(), key=lambda x: -x[1])
        if any(k in n.lower() for k in NETWORK_KEYS)
    ],
    "gift_card_lines": [
        e for e in entries if "gift" in (e["payee"] + e["memo"]).lower() or "camper" in (e["payee"] + e["memo"]).lower()
    ],
    "unusual_memos": [
        e
        for e in entries
        if any(
            w in (e["memo"] + e["payee"]).lower()
            for w in ["prayer", "gift", "reimburse", "ncsc", "camper", "staff gift"]
        )
    ],
    "categories": {k: round(v, 2) for k, v in sorted(cats.items(), key=lambda x: -x[1])},
    "all_entries": entries,
}

out_path = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\research\banks\_checkdetail_parsed.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)

print("transactions", len(entries), "total", f"{total:,.2f}")
print("written", out_path)
