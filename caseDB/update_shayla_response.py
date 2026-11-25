"""Update caseDB with Shayla's Sep 22 response package."""
import sqlite3, json, os

DB = os.path.join(os.path.dirname(__file__), "caseDB.sqlite")
j = lambda lst: json.dumps(lst) if lst else None

conn = sqlite3.connect(DB)

# Events
events = [
    ("2026-09-22", 0,
     "Shayla files Answer + Motion for Summary Disposition + RFA Responses",
     "Shayla files 3 documents in 4301-CZ: "
     "(1) Responses to 41 RFAs - ADMITS no custody order (#18), went to Cornerstone/Deanna's "
     "house Sep 2 (#16-17), Leon accompanied (#20), Leon is USPS (#37). DENIES BK debtors "
     "are Marquita/Simone (#40-41, potentially false). Says PPO filed Aug 24 not Sep. "
     "(2) Motion for Summary Disposition under MCR 2.116(C)(5)+(C)(8) - argues Kevin lacks "
     "standing for DaSean's rights, unjust enrichment not adequately pleaded, conspiracy derivative. "
     "(3) Answer to First Amended Complaint - denies all coordination, says she was at WORK "
     "Aug 29 not at PCA, identifies her MOTHER (Marquita) as present at PCA that day.",
     j(["2026-4301-CZ"]), j(["smith-shayla"]),
     "Certified mail received Sep 28",
     "DEFAULT IS DEAD FOR SHAYLA. She answered within time. MSD response due ~Oct 16. "
     "BIG ADMISSIONS on custody, Cornerstone, Leon."),

    ("2026-09-28", 0,
     "All 4 Smith responses received via certified mail",
     "All 4 Smith defendants sent certified mail responses, postmarked Sep 22. "
     "Received Sep 28, hours after Kevin mailed spoliation Wave 1. "
     "Shayla: Answer + MSD + RFA responses (12 pages). Leon/Marquita/Simone: TBD.",
     j(["2026-4301-CZ"]),
     j(["smith-shayla", "smith-leon", "smith-marquita", "smith-simone"]),
     "Certified mail",
     "They answered. Default strategy must be reassessed."),
]

for evt in events:
    conn.execute(
        "INSERT INTO events (date, date_approx, title, description, case_ids, entity_ids, source, significance) "
        "VALUES (?,?,?,?,?,?,?,?)", evt)

# Update case status
conn.execute(
    "UPDATE cases SET status = 'active', notes = ? WHERE id = '2026-4301-CZ'",
    ("Shayla answered Sep 22. MSD filed. RFAs answered (11 admits, 15 denials). "
     "Response to MSD due ~Oct 16. Default strategy dead for Shayla.",))

# Add evidence
conn.execute(
    "INSERT OR REPLACE INTO evidence "
    "(id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity, notes) "
    "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
    ("shayla-response-sep22",
     "Shayla Smith Response Package (RFA + MSD + Answer)",
     "document",
     "Certified mail from Shayla Smith",
     "C:/Users/mokke/Documents/smithResponseShayla.pdf",
     "12-page package: RFA responses (41 items, 11 admits including NO CUSTODY ORDER), "
     "Motion for Summary Disposition (standing + C(8)), Answer + Affirmative Defenses.",
     "2026-09-22",
     j(["smith-shayla"]),
     j(["2026-4301-CZ"]),
     "Certified mail with certificate of service",
     None))

conn.commit()
print("DB updated:")
for t in ["events", "evidence"]:
    c = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t}: {c} rows")
conn.close()
