"""
Sep 28 2026 — Database corrections and additions.
Fixes: relationship framing, assault location, Deanna entity,
       timeline (wedding ceremonies, Feb breakup, Jun 2025 remortgage),
       benefits fraud (SNAP/EBT/FIP/Medicaid), potential IRS fraud.
Run: python update_sep28_corrections.py
"""
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "caseDB.sqlite")

def j(lst):
    return json.dumps(lst) if lst else None

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")

    # ============================================================
    # 1. ADD ENTITY: Deanna (DaSean's mom)
    # ============================================================
    conn.execute("""
        INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "mitchell-deanna", "Deanna Mitchell", "person", None,
        j([{"street": "XXXX Cornerstone Blvd", "city": "Lansing", "state": "MI", "zip": "48910",
            "source": "Ring camera / address records", "current": True}]),
        None, None,
        "DaSean's mother. Sahana and Allanna's paternal grandmother. "
        "The Sep 2 assault occurred at her house."
    ))
    print("  + Added entity: mitchell-deanna (Deanna Mitchell)")

    # ============================================================
    # 2. ADD RELATIONSHIPS for Deanna
    # ============================================================
    conn.execute("""
        INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
        VALUES (?, ?, ?, ?, ?)
    """, ("mitchell-deanna", "mitchell-dasean", "family",
          "Mother and son.", None))

    conn.execute("""
        INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
        VALUES (?, ?, ?, ?, ?)
    """, ("mitchell-deanna", "smith-shayla", "family",
          "Paternal grandmother of Sahana and Allanna. Deanna's house is where the Sep 2 assault occurred.",
          None))
    print("  + Added relationships: Deanna ↔ DaSean, Deanna ↔ Shayla")

    # ============================================================
    # 3. FIX: DaSean entity — update notes
    # ============================================================
    conn.execute("""
        UPDATE entities SET notes = ?
        WHERE id = 'mitchell-dasean'
    """, (
        "Army veteran. Father of Sahana (9) and Allanna (7). Kevin's best friend. "
        "Was in a committed relationship with Shayla — 2 wedding ceremonies but NO legal "
        "marriage certificate. Shayla ended the relationship Feb 2026. Shayla has exercised "
        "de facto sole custody of both daughters for ~9 years with no court order, claiming "
        "benefits (SNAP/EBT/FIP/Medicaid) as if she had sole legal custody.",
    ))
    print("  ~ Updated entity: mitchell-dasean (relationship + benefits detail)")

    # ============================================================
    # 4. FIX: Shayla entity — update notes
    # ============================================================
    conn.execute("""
        UPDATE entities SET notes = ?
        WHERE id = 'smith-shayla'
    """, (
        "DaSean's ex-partner. 2 wedding ceremonies, NO legal marriage certificate. "
        "Ended the relationship Feb 2026 — but groundwork laid Jun 2025 when parents "
        "(Leon + Marquita) remortgaged Dresden house. Has exercised de facto sole custody "
        "for ~9 years with NO court order. Controlled SNAP/EBT/FIP/Medicaid benefits as if "
        "she had sole legal custody. Potential IRS filing fraud (filing as head of household "
        "or claiming children without legal custody). Enrolled daughters at PCA (Banks' school) "
        "without DaSean's knowledge or consent.",
    ))
    print("  ~ Updated entity: smith-shayla (relationship + benefits + IRS detail)")

    # ============================================================
    # 5. FIX: Shayla ↔ DaSean relationship — update description
    # ============================================================
    conn.execute("""
        UPDATE relationships SET description = ?
        WHERE entity_a = 'smith-shayla' AND entity_b = 'mitchell-dasean'
        AND rel_type = 'family'
    """, (
        "Ex-partner. 2 wedding ceremonies, NO legal marriage certificate. "
        "Mother of Sahana (9) and Allanna (7). Shayla ended relationship Feb 2026. "
        "Has exercised de facto sole custody ~9 years, no court order.",
    ))
    print("  ~ Updated relationship: smith-shayla ↔ mitchell-dasean")

    # ============================================================
    # 6. FIX: Sep 2 assault event — correct location to Deanna's house
    # ============================================================
    conn.execute("""
        UPDATE events SET description = ?,
        entity_ids = ?
        WHERE date = '2026-09-02'
        AND title LIKE '%Leon assaults%'
    """, (
        "Leon physically assaults DaSean at XXXX Cornerstone Blvd — this is DEANNA'S house "
        "(DaSean's mother, the girls' paternal grandmother). Ring camera captures assault "
        "with timestamp and geolocation. Leon came to Deanna's home and assaulted DaSean. "
        "While Leon assaults DaSean, Shayla removes the children from the location.",
        j(["smith-leon", "mitchell-dasean", "smith-shayla", "mitchell-deanna"]),
    ))
    print("  ~ Updated event: Sep 2 assault — corrected location to Deanna's house")

    # ============================================================
    # 7. FIX: Sep 2 texts event — Deanna is DaSean's mom, not Shayla's contact
    # ============================================================
    conn.execute("""
        UPDATE events SET description = ?
        WHERE date = '2026-09-02'
        AND title LIKE '%Shayla coordinates%'
    """, (
        "Text messages show Shayla coordinating the pickup ahead of time with Deanna "
        "(DaSean's mother) and Sahana (9-year-old daughter). Shayla planned to take the "
        "children from Deanna's house, completely leaving DaSean out. Pre-planned removal, "
        "not spontaneous.",
    ))
    print("  ~ Updated event: Sep 2 texts — clarified Deanna is DaSean's mom")

    # ============================================================
    # 8. FIX: Ring camera evidence — correct location
    # ============================================================
    conn.execute("""
        UPDATE evidence SET source = ?,
        description = ?
        WHERE id = 'ring-camera-sep2'
    """, (
        "Ring camera at XXXX Cornerstone Blvd (Deanna Mitchell's house — DaSean's mother)",
        "Leon assaults DaSean at Deanna's house (the girls' paternal grandmother). "
        "Shayla removes children. Timestamped, geo-located.",
    ))
    print("  ~ Updated evidence: ring-camera-sep2 — corrected location")

    # ============================================================
    # 9. FIX: Shayla texts evidence — clarify Deanna
    # ============================================================
    conn.execute("""
        UPDATE evidence SET description = ?
        WHERE id = 'shayla-texts-deanna-sahana'
    """, (
        "Texts show Shayla coordinating child pickup with Deanna (DaSean's mother) and "
        "Sahana (DaSean's 9-year-old daughter) ahead of time. Shayla planned to remove the "
        "children from their paternal grandmother's house, leaving DaSean completely out. "
        "Pre-planned removal.",
    ))
    print("  ~ Updated evidence: shayla-texts — clarified Deanna = DaSean's mom")

    # ============================================================
    # 10. ADD EVENTS: Relationship timeline
    # ============================================================
    new_events = [
        # Wedding ceremonies (approximate dates — DaSean can confirm)
        ("2017-06-01", 1, "First wedding ceremony — DaSean and Shayla",
         "DaSean and Shayla held a wedding ceremony. No legal marriage certificate was "
         "obtained or filed. This is the first of two ceremonies.",
         j(["26-108221-DC"]), j(["mitchell-dasean", "smith-shayla"]),
         "DaSean's testimony", "Establishes the nature of the relationship — committed but never legally married."),

        ("2019-06-01", 1, "Second wedding ceremony — DaSean and Shayla",
         "DaSean and Shayla held a second wedding ceremony. Again, no legal marriage "
         "certificate was obtained or filed. Despite two ceremonies, they were never legally married.",
         j(["26-108221-DC"]), j(["mitchell-dasean", "smith-shayla"]),
         "DaSean's testimony", "Two ceremonies, zero legal marriages. Relevant to custody — no marital presumption applies."),

        # June 2025 — remortgage (groundwork)
        ("2025-06-24", 0, "Leon + Marquita remortgage Dresden house — groundwork for breakup",
         "Wayne ROD Doc# 2025200597: Leon QCDs Dresden St to Leon+Marquita. Same day: "
         "Doc# 2025201292: $68K mortgage. Six days before Marquita's bankruptcy filing. "
         "This is the financial groundwork for Shayla's Feb 2026 departure — her parents "
         "extracting equity and restructuring assets before the split.",
         j(["2026-4301-CZ"]),
         j(["smith-leon", "smith-marquita"]),
         "Wayne County ROD",
         "Financial premeditation. Parents remortgage 6 months before Shayla leaves DaSean."),

        # February 2026 — breakup
        ("2026-02-01", 1, "Shayla ends relationship with DaSean",
         "Shayla ends the relationship and takes the children. After ~9 years together "
         "(including 2 wedding ceremonies with no legal marriage), Shayla leaves with both "
         "daughters. No custody order exists. No legal custody was ever established. Shayla "
         "continues to control all aspects of the children's lives — school enrollment, "
         "medical care, benefits (SNAP/EBT/FIP/Medicaid) — as if she has sole legal custody.",
         j(["26-108221-DC", "26-4432-PP"]),
         j(["smith-shayla", "mitchell-dasean"]),
         "DaSean's testimony",
         "The breakup. No custody order exists. Shayla takes children unilaterally."),

        # Benefits fraud — ongoing discovery
        ("2026-09-28", 0, "Benefits fraud identified — SNAP/EBT/FIP/Medicaid",
         "Through investigation, discovered Shayla has been receiving and controlling "
         "SNAP, EBT, FIP, and Medicaid benefits for Sahana and Allanna as if she has sole "
         "legal custody. No custody order exists. DaSean was never consulted, never received "
         "benefits, and may have been excluded from IRS filings (head of household / child "
         "tax credit claims). IRS filing fraud investigation needed.",
         j(["26-108221-DC", "2026-4301-CZ"]),
         j(["smith-shayla", "mitchell-dasean"]),
         "Benefits records (to be subpoenaed)",
         "Benefits fraud + potential IRS fraud. Another layer of the de facto custody scheme."),
    ]

    for evt in new_events:
        conn.execute("""
            INSERT INTO events (date, date_approx, title, description, case_ids, entity_ids, source, significance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, evt)
    print(f"  + Added {len(new_events)} new events (wedding ceremonies, remortgage, breakup, benefits fraud)")

    # ============================================================
    # 11. ADD EVIDENCE: Benefits fraud
    # ============================================================
    conn.execute("""
        INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path,
        description, date, entity_ids, case_ids, authenticity, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "benefits-fraud-snap-ebt", "SNAP/EBT/FIP/Medicaid benefits fraud", "financial",
        "To be subpoenaed — MDHHS, IRS", None,
        "Shayla received and controlled public benefits (SNAP, EBT, FIP, Medicaid) for both "
        "children as if she had sole legal custody. No custody order exists. DaSean was "
        "excluded from all benefits decisions. Potential IRS fraud: filing head of household "
        "or claiming child tax credits without legal custody.",
        None, j(["smith-shayla", "mitchell-dasean"]),
        j(["26-108221-DC", "2026-4301-CZ"]),
        "To be authenticated via MDHHS subpoena + IRS records",
        "Need to subpoena: MDHHS benefits history, IRS transcripts for Shayla. "
        "Cross-reference with DaSean's tax filings."
    ))
    print("  + Added evidence: benefits-fraud-snap-ebt")

    # ============================================================
    # 12. ADD EVIDENCE: No marriage certificate
    # ============================================================
    conn.execute("""
        INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path,
        description, date, entity_ids, case_ids, authenticity, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "no-marriage-cert", "No legal marriage certificate — DaSean and Shayla", "public-record",
        "County clerk records", None,
        "Despite two wedding ceremonies, DaSean Mitchell and Shayla Smith never obtained or "
        "filed a legal marriage certificate. They were never legally married. This means: "
        "(1) no marital presumption of custody applies, (2) DaSean has equal parental rights "
        "as biological father, (3) Shayla has no legal basis for sole custody.",
        None, j(["mitchell-dasean", "smith-shayla"]),
        j(["26-108221-DC", "26-4432-PP"]),
        "County clerk search — no record",
        "Critical for custody: MCL 722.1003 — unmarried father has equal rights when paternity established."
    ))
    print("  + Added evidence: no-marriage-cert")

    conn.commit()

    # Print updated counts
    for table in ["entities", "events", "evidence", "relationships"]:
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count} rows")

    conn.close()
    print("\nDatabase updated with Sep 28 corrections.")

if __name__ == "__main__":
    main()
