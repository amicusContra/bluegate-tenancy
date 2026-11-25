"""Update caseDB with all 4 Smith response packages."""
import sqlite3, json, os, shutil

DB = os.path.join(os.path.dirname(__file__), "caseDB.sqlite")
j = lambda lst: json.dumps(lst) if lst else None

conn = sqlite3.connect(DB)

# Copy source PDFs to evidence folder
src_dir = r"C:\Users\mokke\Documents"
dst_dir = r"C:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence\court-filings"
for name in ["smithResponseLeon.pdf", "smithResponseMarquita.pdf", "smithResponseSimone.pdf"]:
    src = os.path.join(src_dir, name)
    dst = os.path.join(dst_dir, name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  Copied {name}")

# Add evidence records
evidence = [
    ("leon-response-sep22", "Leon Smith Response Package (RFA + 2x MSD)", "document",
     "Certified mail from Leon Smith",
     "C:/Users/mokke/Documents/smithResponseLeon.pdf",
     "22 pages: MSD on FAC + MSD on Original Complaint + RFA Responses (4 admits, 26 objections). "
     "Confirms: not at PCA Aug 29, Shayla at work, Marquita present with girls. "
     "Challenges FAC amendment under MCR 2.118(A). Threatens sanctions.",
     "2026-09-22", j(["smith-leon"]), j(["2026-4301-CZ"]),
     "Certified mail with certificate of service", None),

    ("marquita-response-sep22",
     "Marquita Smith Response Package (Answer + RFA + MSD)", "document",
     "Certified mail from Marquita Smith",
     "C:/Users/mokke/Documents/smithResponseMarquita.pdf",
     "28 pages: Answer to FAC + RFA Responses + MSD MCR 2.116(C)(8)+(C)(10). "
     "ADMITS: present at PCA Aug 29, made police report #26-0829-0225, owns Dresden St. "
     "KEY: Leon signed for household with consent (admits forgery). "
     "Claims NOT Marquita Renea Smith. Phone: (313)957-1802. Email: oneomega1993@gmail.com.",
     "2026-09-22", j(["smith-marquita"]), j(["2026-4301-CZ"]),
     "Certified mail, verified under penalty of perjury", None),

    ("simone-response-sep22",
     "Simone Smith Response Package (RFA + MSD + Answer)", "document",
     "Certified mail from Simone Smith",
     "C:/Users/mokke/Documents/smithResponseSimone.pdf",
     "10 pages: RFA Responses (nearly all denied) + MSD MCR 2.116(C)(8) + Answer + 7 Affirmative Defenses. "
     "Denies being BK debtor. Claims never owned property. Now at XXXXX Dresden St.",
     "2026-09-22", j(["smith-simone"]), j(["2026-4301-CZ"]),
     "Certified mail with certificate of service", None),
]

for ev in evidence:
    conn.execute(
        "INSERT OR REPLACE INTO evidence "
        "(id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity, notes) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?)", ev)

# Update contact info
conn.execute("UPDATE entities SET phone = ?, email = ? WHERE id = ?",
             ("(313) 957-1802", "oneomega1993@gmail.com", "smith-marquita"))
conn.execute("UPDATE entities SET email = ? WHERE id = ?",
             ("oneomega1970@gmail.com", "smith-leon"))

# Update Marquita notes
conn.execute("UPDATE entities SET notes = ? WHERE id = ?", (
    "Leon's wife. BK 26-47542 (disputes identity). ADMITS: present at PCA Aug 29, "
    "made police report #26-0829-0225, owns Dresden St property. ADMITS Leon signed "
    "green cards for household. Claims middle name Lashun not Renea. "
    "Phone: (313)957-1802. Email: oneomega1993@gmail.com.",
    "smith-marquita"))

# Update Simone notes
conn.execute("UPDATE entities SET notes = ? WHERE id = ?", (
    "Shayla's sister (disputed — denies Marquita is her mother). BK 26-49404-lsg (disputes identity). "
    "Claims never owned real property (contradicts Normandy Ave records). "
    "NOW lists address as XXXXX Dresden St, not Normandy Ave.",
    "smith-simone"))

# Update Leon notes
conn.execute("UPDATE entities SET notes = ? WHERE id = ?", (
    "USPS mail carrier, Harper Woods PO. Assaulted DaSean Sep 2. "
    "RFA: admitted items 1-4, objected to rest on relevance. "
    "Marquita admits Leon signed green cards for household. "
    "Phone: (313)412-4703. Email: oneomega1970@gmail.com.",
    "smith-leon"))

# Update case status
conn.execute("UPDATE cases SET status = ?, notes = ? WHERE id = ?", (
    "active",
    "ALL 4 SMITHS ANSWERED Sep 22. All filed MSDs. Default dead. "
    "MSD responses due ~Oct 16. Key admissions: no custody order, "
    "Leon signed green cards, Marquita at PCA Aug 29.",
    "2026-4301-CZ"))

# Add event for new police report
conn.execute(
    "INSERT INTO events (date, date_approx, title, description, case_ids, entity_ids, source, significance) "
    "VALUES (?,?,?,?,?,?,?,?)",
    ("2026-08-29", 0,
     "Marquita makes police report #26-0829-0225 about Kevin's PCA visit",
     "Marquita admits in her Answer that SHE (not Shayla) was at PCA on Aug 29, and that "
     "she made police report #26-0829-0225 about the events. This is a separate report from "
     "Banks' Sep 9 DPD report. Need to obtain this report.",
     j(["2026-4301-CZ", "26-4433-PH"]),
     j(["smith-marquita", "mok-kevin"]),
     "Marquita's Answer to FAC, paragraph 19",
     "New police report. Marquita admits presence at PCA. Need to obtain report."))

conn.commit()
for t in ["evidence", "events", "entities"]:
    c = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t}: {c} rows")
conn.close()
print("Done — all 4 Smith responses ingested.")
