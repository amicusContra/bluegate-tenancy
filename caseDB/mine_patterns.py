"""
Pattern Mining — Surfaces protection layers, hub entities, 
dynasty connections, and institutional shields across the network.

Usage: python mine_patterns.py
"""
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caseDB.sqlite")

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def main():
    conn = connect()

    print("=" * 70)
    print("PATTERN ANALYSIS: INSTITUTIONAL PROTECTION LAYERS")
    print("=" * 70)

    # ---------------------------------------------------------------
    # Pattern 1: Board seats — who controls what
    # ---------------------------------------------------------------
    print("\n--- PATTERN 1: BOARD SEATS (governance control) ---")
    boards = conn.execute("""
        SELECT r.entity_a as person_id, ea.name as person, 
               r.entity_b as org_id, eb.name as org, r.description
        FROM relationships r
        JOIN entities ea ON r.entity_a = ea.id
        JOIN entities eb ON r.entity_b = eb.id
        WHERE r.rel_type = 'board-member'
        ORDER BY r.entity_b, ea.name
    """).fetchall()
    
    current_org = None
    for b in boards:
        if b['org'] != current_org:
            current_org = b['org']
            count = sum(1 for x in boards if x['org'] == current_org)
            print(f"\n  {current_org} ({count} members tracked):")
        print(f"    {b['person']:35} {b['description'] or ''}")

    # ---------------------------------------------------------------
    # Pattern 2: Financial flow + ownership
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 2: MONEY FLOW + OWNERSHIP ---")
    financial = conn.execute("""
        SELECT r.entity_a, ea.name as from_name, r.entity_b, eb.name as to_name, 
               r.rel_type, r.description, r.amount
        FROM relationships r
        JOIN entities ea ON r.entity_a = ea.id
        JOIN entities eb ON r.entity_b = eb.id
        WHERE r.rel_type IN ('owner','employer','campaign-payment','co-owner','registrar')
        ORDER BY r.rel_type, ea.name
    """).fetchall()
    for f in financial:
        amt = f"  ${f['amount']:,.2f}" if f['amount'] else ""
        print(f"  [{f['rel_type']:18}] {f['from_name']:35} -> {f['to_name']}{amt}")

    # ---------------------------------------------------------------
    # Pattern 3: Hub entities (most connections = most power/risk)
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 3: HUB ENTITIES (most connections) ---")
    hubs = conn.execute("""
        SELECT e.id, e.name, e.type,
            (SELECT COUNT(*) FROM relationships 
             WHERE entity_a=e.id OR entity_b=e.id) as rel_count
        FROM entities e
        ORDER BY rel_count DESC
        LIMIT 20
    """).fetchall()
    for h in hubs:
        bar = "█" * h['rel_count']
        print(f"  {h['rel_count']:3} {bar:30} {h['name']:40} [{h['type']}]")

    # ---------------------------------------------------------------
    # Pattern 4: Attorney shields
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 4: ATTORNEY/LEGAL SHIELDS ---")
    attorneys = conn.execute("""
        SELECT ea.name as atty, eb.name as client, r.description, r.start_date
        FROM relationships r
        JOIN entities ea ON r.entity_a = ea.id
        JOIN entities eb ON r.entity_b = eb.id
        WHERE r.rel_type = 'attorney'
        ORDER BY r.entity_b
    """).fetchall()
    for a in attorneys:
        dt = f"  (since {a['start_date']})" if a['start_date'] else ""
        print(f"  {a['atty']:35} -> {a['client']:30} {a['description'] or ''}{dt}")

    # ---------------------------------------------------------------
    # Pattern 5: Family dynasties
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 5: FAMILY DYNASTIES ---")
    families = conn.execute("""
        SELECT ea.name as person_a, eb.name as person_b, r.description
        FROM relationships r
        JOIN entities ea ON r.entity_a = ea.id
        JOIN entities eb ON r.entity_b = eb.id
        WHERE r.rel_type IN ('family', 'domestic-partner')
        ORDER BY ea.name
    """).fetchall()
    for f in families:
        print(f"  {f['person_a']:30} <-> {f['person_b']:30} {f['description'] or ''}")

    # ---------------------------------------------------------------
    # Pattern 6: PROTECTION LAYERS — for each defendant, what 
    # institutional shields do they have?
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 6: PROTECTION LAYERS (per defendant) ---")
    defendants = conn.execute("""
        SELECT DISTINCT cp.entity_id, e.name
        FROM case_parties cp
        JOIN entities e ON cp.entity_id = e.id
        WHERE cp.role IN ('defendant', 'respondent')
        ORDER BY e.name
    """).fetchall()
    
    for d in defendants:
        rels = conn.execute("""
            SELECT r.rel_type, r.description,
                CASE WHEN r.entity_a = ? THEN eb.name ELSE ea.name END as connected_to,
                CASE WHEN r.entity_a = ? THEN eb.type ELSE ea.type END as connected_type
            FROM relationships r
            JOIN entities ea ON r.entity_a = ea.id
            JOIN entities eb ON r.entity_b = eb.id
            WHERE r.entity_a = ? OR r.entity_b = ?
            ORDER BY r.rel_type
        """, (d['entity_id'], d['entity_id'], d['entity_id'], d['entity_id'])).fetchall()
        
        shields = {"legal": [], "institutional": [], "financial": [], "family": [], "political": []}
        for r in rels:
            if r['rel_type'] in ('attorney',):
                shields["legal"].append(f"{r['connected_to']} ({r['description'] or ''})")
            elif r['rel_type'] in ('board-member', 'employer', 'enabler', 'mentor', 'therapist', 'evaluator'):
                shields["institutional"].append(f"{r['connected_to']} [{r['rel_type']}]")
            elif r['rel_type'] in ('owner', 'co-owner', 'trust-successor', 'campaign-payment', 'registrar'):
                shields["financial"].append(f"{r['connected_to']} [{r['rel_type']}]")
            elif r['rel_type'] in ('family', 'domestic-partner'):
                shields["family"].append(f"{r['connected_to']} ({r['description'] or ''})")
            elif r['connected_type'] in ('judge', 'agency'):
                shields["political"].append(f"{r['connected_to']} [{r['rel_type']}]")
        
        total = sum(len(v) for v in shields.values())
        if total == 0:
            continue
            
        print(f"\n  {d['name']} ({total} protection layers):")
        for category, items in shields.items():
            if items:
                print(f"    {category.upper()}:")
                for item in items:
                    print(f"      • {item}")

    # ---------------------------------------------------------------
    # Pattern 7: Cross-institution overlap — people who appear in 
    # multiple orgs simultaneously
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 7: CROSS-INSTITUTION OVERLAP ---")
    overlaps = conn.execute("""
        SELECT ea.name as person, GROUP_CONCAT(eb.name, ' | ') as orgs,
               COUNT(*) as org_count
        FROM relationships r
        JOIN entities ea ON r.entity_a = ea.id
        JOIN entities eb ON r.entity_b = eb.id
        WHERE r.rel_type IN ('board-member', 'employer', 'owner')
        AND ea.type = 'person'
        GROUP BY r.entity_a
        HAVING COUNT(*) >= 2
        ORDER BY org_count DESC
    """).fetchall()
    for o in overlaps:
        print(f"  {o['person']:35} ({o['org_count']} orgs): {o['orgs']}")

    # ---------------------------------------------------------------
    # Pattern 8: The Stallworth dynasty reach
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 8: STALLWORTH DYNASTY REACH ---")
    stallworths = conn.execute("""
        SELECT e.id, e.name FROM entities e
        WHERE e.name LIKE '%Stallworth%' OR e.name LIKE '%stallworth%'
        ORDER BY e.name
    """).fetchall()
    for s in stallworths:
        rels = conn.execute("""
            SELECT r.rel_type, 
                CASE WHEN r.entity_a = ? THEN eb.name ELSE ea.name END as connected_to,
                r.description
            FROM relationships r
            JOIN entities ea ON r.entity_a = ea.id
            JOIN entities eb ON r.entity_b = eb.id
            WHERE r.entity_a = ? OR r.entity_b = ?
        """, (s['id'], s['id'], s['id'])).fetchall()
        print(f"\n  {s['name']}:")
        for r in rels:
            print(f"    [{r['rel_type']:18}] {r['connected_to']:35} {r['description'] or ''}")

    # ---------------------------------------------------------------
    # Pattern 9: Entities NOT YET on detroit site
    # ---------------------------------------------------------------
    print("\n\n--- PATTERN 9: ENTITIES NEEDING SITE PAGES ---")
    # These are entities with 2+ relationships that should have network pages
    candidates = conn.execute("""
        SELECT e.id, e.name, e.type,
            (SELECT COUNT(*) FROM relationships WHERE entity_a=e.id OR entity_b=e.id) as rels
        FROM entities e
        WHERE e.type = 'person'
        AND (SELECT COUNT(*) FROM relationships WHERE entity_a=e.id OR entity_b=e.id) >= 2
        ORDER BY rels DESC
    """).fetchall()
    
    existing_pages = {
        "banks-brian", "holland-joseph", "wells-stallworth-nicole", "meihn-gregory",
        "vitti-nicolai", "shulman-terrence", "leno-michele", "judge-yancey",
        "stallworth-alma", "stallworth-thomas-iii", "stallworth-keith",
        "stallworth-west-misha"
    }
    
    for c in candidates:
        status = "✓ HAS PAGE" if c['id'] in existing_pages else "⚠ NEEDS PAGE"
        print(f"  {status}  {c['rels']:2} rels  {c['name']:40} [{c['type']}]")

    conn.close()

if __name__ == "__main__":
    main()
