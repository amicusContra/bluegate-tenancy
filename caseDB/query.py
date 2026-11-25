"""
Case Intelligence Query Tool

Usage:
    python query.py hearing ppo-hearing-sep29     # What exhibits do I need for this hearing?
    python query.py case 26-4432-PP               # Everything about a case
    python query.py entity banks-brian             # Full profile + relationships + cases
    python query.py timeline 2026-09-01 2026-09-30 # Events in a date range
    python query.py evidence 2026-4301-CZ          # All evidence for a case
    python query.py foia                           # FOIA dashboard
    python query.py upcoming                       # Next hearings
    python query.py search <term>                  # Full-text search across all tables
    python query.py network <entity_id>            # Relationship map for an entity
    python query.py export <hearing_id>            # Export exhibit list as markdown
    python query.py gaps                           # Find gaps and alignment issues
    python query.py mine <entity_id>               # Deep mine — all data touching an entity
    python query.py stats                          # Database statistics + coverage report
    python query.py board <org_id>                 # Board composition and connections
    python query.py chain <entity_a> <entity_b>    # Find connection chains between entities
"""
import sqlite3
import json
import sys
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caseDB.sqlite")

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def jp(val):
    """Parse JSON field or return empty list."""
    if val:
        try:
            return json.loads(val)
        except:
            return [val]
    return []

def fmt_addr(addr_json):
    """Format first current address from JSON."""
    addrs = jp(addr_json)
    for a in addrs:
        if isinstance(a, dict) and a.get("current"):
            parts = [a.get("street",""), a.get("city",""), a.get("state",""), a.get("zip","")]
            return ", ".join(p for p in parts if p)
    if addrs and isinstance(addrs[0], dict):
        a = addrs[0]
        parts = [a.get("street",""), a.get("city",""), a.get("state",""), a.get("zip","")]
        return ", ".join(p for p in parts if p)
    return ""

# ============================================================
# COMMANDS
# ============================================================

def cmd_hearing(conn, hearing_id):
    """Full briefing for a hearing — cases, parties, evidence, exhibits."""
    h = conn.execute("SELECT * FROM hearings WHERE id=?", (hearing_id,)).fetchone()
    if not h:
        print(f"No hearing found: {hearing_id}")
        return

    print(f"\n{'='*60}")
    print(f"HEARING: {h['id']}")
    print(f"{'='*60}")
    print(f"Date:      {h['date']} {h['time'] or ''}")
    print(f"Type:      {h['hearing_type']}")
    print(f"Courtroom: {h['courtroom'] or 'TBD'}")
    print(f"Address:   {h['court_address'] or 'TBD'}")
    print(f"Status:    {h['status']}")
    if h['notes']:
        print(f"Notes:     {h['notes']}")

    judge = conn.execute("SELECT * FROM entities WHERE id=?", (h['judge_id'],)).fetchone()
    if judge:
        print(f"Judge:     {judge['name']}")

    case_ids = jp(h['case_ids'])
    print(f"\n--- CASES ({len(case_ids)}) ---")
    for cid in case_ids:
        c = conn.execute("SELECT * FROM cases WHERE id=?", (cid,)).fetchone()
        if c:
            print(f"\n  {c['id']}  {c['caption']}")
            print(f"  Type: {c['case_type']}  Status: {c['status']}")
            parties = conn.execute(
                "SELECT cp.role, e.name FROM case_parties cp JOIN entities e ON cp.entity_id=e.id WHERE cp.case_id=?",
                (cid,)
            ).fetchall()
            for p in parties:
                print(f"    {p['role']:15} {p['name']}")

    print(f"\n--- RELEVANT EVIDENCE ---")
    for cid in case_ids:
        evs = conn.execute("SELECT * FROM evidence WHERE case_ids LIKE ?", (f"%{cid}%",)).fetchall()
        for e in evs:
            print(f"  [{e['ev_type']:15}] {e['title']}")
            if e['description']:
                print(f"                    {e['description'][:100]}")

    exs = conn.execute("SELECT * FROM exhibits WHERE hearing_id=?", (hearing_id,)).fetchall()
    if exs:
        print(f"\n--- EXHIBIT LIST ---")
        for ex in exs:
            desc = ex['description'] or ''
            tab = ex['tab'] or ''
            print(f"  {tab:10} {desc}")


def cmd_case(conn, case_id):
    """Everything about a case."""
    c = conn.execute("SELECT * FROM cases WHERE id=?", (case_id,)).fetchone()
    if not c:
        print(f"No case found: {case_id}")
        return

    print(f"\n{'='*60}")
    print(f"CASE: {c['id']} — {c['caption']}")
    print(f"{'='*60}")
    print(f"Court:  {c['court']}")
    print(f"Type:   {c['case_type']}")
    print(f"Filed:  {c['filed_date'] or 'Unknown'}")
    print(f"Status: {c['status']}")
    if c['notes']:
        print(f"Notes:  {c['notes']}")

    if c['judge']:
        j = conn.execute("SELECT name FROM entities WHERE id=?", (c['judge'],)).fetchone()
        if j:
            print(f"Judge:  {j['name']}")

    print(f"\n--- PARTIES ---")
    parties = conn.execute(
        "SELECT cp.role, e.name, e.id FROM case_parties cp JOIN entities e ON cp.entity_id=e.id WHERE cp.case_id=?",
        (case_id,)
    ).fetchall()
    for p in parties:
        print(f"  {p['role']:15} {p['name']}")

    print(f"\n--- EVENTS ---")
    events = conn.execute("SELECT * FROM events WHERE case_ids LIKE ? ORDER BY date", (f"%{case_id}%",)).fetchall()
    for ev in events:
        print(f"  {ev['date']}  {ev['title']}")

    print(f"\n--- EVIDENCE ---")
    evs = conn.execute("SELECT * FROM evidence WHERE case_ids LIKE ?", (f"%{case_id}%",)).fetchall()
    for e in evs:
        print(f"  [{e['ev_type']:15}] {e['title']}")

    print(f"\n--- SERVICE LOG ---")
    svc = conn.execute(
        "SELECT sl.*, e.name FROM service_log sl JOIN entities e ON sl.entity_id=e.id WHERE sl.case_id=?",
        (case_id,)
    ).fetchall()
    for s in svc:
        print(f"  {s['date']}  {s['name']}  {s['method']}  → {s['result']}")

    print(f"\n--- HEARINGS ---")
    hs = conn.execute("SELECT * FROM hearings WHERE case_ids LIKE ?", (f"%{case_id}%",)).fetchall()
    for h in hs:
        jname = ""
        if h['judge_id']:
            jn = conn.execute("SELECT name FROM entities WHERE id=?", (h['judge_id'],)).fetchone()
            jname = jn['name'] if jn else ""
        print(f"  {h['date']} {h['time'] or ''}  {h['hearing_type']}  {jname}  [{h['status']}]")


def cmd_entity(conn, entity_id):
    """Full profile for an entity."""
    e = conn.execute("SELECT * FROM entities WHERE id=?", (entity_id,)).fetchone()
    if not e:
        print(f"No entity found: {entity_id}")
        return

    print(f"\n{'='*60}")
    print(f"ENTITY: {e['name']}  ({e['type']})")
    print(f"{'='*60}")
    if e['aliases']:
        print(f"Aliases:   {', '.join(jp(e['aliases']))}")
    addr = fmt_addr(e['addresses'])
    if addr:
        print(f"Address:   {addr}")
    if e['phone']:
        print(f"Phone:     {e['phone']}")
    if e['email']:
        print(f"Email:     {e['email']}")
    if e['notes']:
        print(f"Notes:     {e['notes']}")

    print(f"\n--- CASES ---")
    cp = conn.execute(
        "SELECT cp.case_id, cp.role, c.caption FROM case_parties cp JOIN cases c ON cp.case_id=c.id WHERE cp.entity_id=?",
        (entity_id,)
    ).fetchall()
    for p in cp:
        print(f"  {p['case_id']:20}  {p['role']:15}  {p['caption']}")

    print(f"\n--- RELATIONSHIPS ---")
    rels = conn.execute(
        """SELECT r.*, ea.name as name_a, eb.name as name_b
           FROM relationships r
           JOIN entities ea ON r.entity_a = ea.id
           JOIN entities eb ON r.entity_b = eb.id
           WHERE r.entity_a=? OR r.entity_b=?""",
        (entity_id, entity_id)
    ).fetchall()
    for r in rels:
        other = r['name_b'] if r['entity_a'] == entity_id else r['name_a']
        print(f"  ↔ {other:30}  [{r['rel_type']}]  {r['description'] or ''}")

    print(f"\n--- EVIDENCE INVOLVING ---")
    evs = conn.execute("SELECT * FROM evidence WHERE entity_ids LIKE ?", (f"%{entity_id}%",)).fetchall()
    for ev in evs:
        print(f"  [{ev['ev_type']:15}] {ev['title']}")


def cmd_timeline(conn, start, end):
    """Events in a date range."""
    events = conn.execute("SELECT * FROM events WHERE date BETWEEN ? AND ? ORDER BY date", (start, end)).fetchall()
    print(f"\n{'='*60}")
    print(f"TIMELINE: {start} — {end}  ({len(events)} events)")
    print(f"{'='*60}")
    for ev in events:
        cases = ", ".join(jp(ev['case_ids'])) if ev['case_ids'] else ""
        print(f"\n  {ev['date']}  {ev['title']}")
        if ev['description']:
            print(f"           {ev['description'][:120]}")
        if cases:
            print(f"           Cases: {cases}")
        if ev['significance']:
            print(f"           WHY: {ev['significance']}")


def cmd_evidence(conn, case_id):
    """All evidence for a case with authentication details."""
    evs = conn.execute("SELECT * FROM evidence WHERE case_ids LIKE ? ORDER BY date", (f"%{case_id}%",)).fetchall()
    print(f"\n{'='*60}")
    print(f"EVIDENCE FOR: {case_id}  ({len(evs)} items)")
    print(f"{'='*60}")
    for e in evs:
        print(f"\n  {e['id']}")
        print(f"  Title:    {e['title']}")
        print(f"  Type:     {e['ev_type']}")
        print(f"  Date:     {e['date'] or 'Unknown'}")
        print(f"  Source:   {e['source'] or ''}")
        if e['authenticity']:
            print(f"  Auth:     {e['authenticity']}")
        if e['description']:
            print(f"  Desc:     {e['description'][:150]}")
        if e['file_path']:
            print(f"  File:     {e['file_path']}")


def cmd_foia(conn):
    """FOIA dashboard."""
    foias = conn.execute(
        """SELECT f.*, e.name as agency FROM foia_requests f
           JOIN entities e ON f.agency_id = e.id ORDER BY f.due_date"""
    ).fetchall()
    print(f"\n{'='*60}")
    print(f"FOIA DASHBOARD  ({len(foias)} requests)")
    print(f"{'='*60}")
    for f in foias:
        status_flag = "✓" if f['status'] == "responded" else "⏳" if f['status'] == "sent" else "⚠"
        print(f"\n  {status_flag} {f['agency']}")
        print(f"    Sent:    {f['date_sent']}")
        print(f"    Due:     {f['due_date']}")
        print(f"    Subject: {f['subject']}")
        print(f"    Status:  {f['status']}")
        if f['response_notes']:
            print(f"    Response: {f['response_notes']}")


def cmd_upcoming(conn):
    """Next hearings."""
    today = datetime.now().strftime("%Y-%m-%d")
    hs = conn.execute(
        "SELECT * FROM v_upcoming_hearings WHERE date >= ? ORDER BY date, time", (today,)
    ).fetchall()
    print(f"\n{'='*60}")
    print(f"UPCOMING HEARINGS  ({len(hs)})")
    print(f"{'='*60}")
    for h in hs:
        print(f"\n  {h['date']} {h['time'] or ''}  [{h['hearing_type']}]")
        print(f"  Judge:     {h['judge_name'] or 'TBD'}")
        print(f"  Courtroom: {h['courtroom'] or 'TBD'}")
        print(f"  Cases:     {', '.join(jp(h['case_ids']))}")


def cmd_search(conn, term):
    """Full-text search across all tables."""
    like = f"%{term}%"
    print(f"\n{'='*60}")
    print(f"SEARCH: '{term}'")
    print(f"{'='*60}")

    for table, cols in [
        ("entities", ["id", "name", "aliases", "notes"]),
        ("cases", ["id", "caption", "notes"]),
        ("events", ["title", "description", "significance"]),
        ("evidence", ["id", "title", "description", "notes"]),
        ("documents", ["id", "title", "notes"]),
        ("relationships", ["description", "notes"]),
        ("agency_referrals", ["id", "subject", "notes"]),
        ("foia_requests", ["id", "subject", "response_notes"]),
    ]:
        where = " OR ".join(f"{c} LIKE ?" for c in cols)
        params = [like] * len(cols)
        rows = conn.execute(f"SELECT * FROM {table} WHERE {where}", params).fetchall()
        if rows:
            print(f"\n  --- {table} ({len(rows)} matches) ---")
            for r in rows:
                if table == "entities":
                    print(f"    {r['id']:30} {r['name']}")
                elif table == "cases":
                    print(f"    {r['id']:20} {r['caption']}")
                elif table == "events":
                    print(f"    {r['date']}  {r['title']}")
                elif table == "evidence":
                    print(f"    {r['id']:30} {r['title']}")
                else:
                    print(f"    {dict(r)}")


def cmd_network(conn, entity_id):
    """Relationship map for an entity — up to 2 hops."""
    e = conn.execute("SELECT name FROM entities WHERE id=?", (entity_id,)).fetchone()
    if not e:
        print(f"No entity found: {entity_id}")
        return

    print(f"\n{'='*60}")
    print(f"NETWORK: {e['name']}")
    print(f"{'='*60}")

    rels = conn.execute(
        """SELECT r.*, ea.name as name_a, eb.name as name_b,
                  ea.id as id_a, eb.id as id_b
           FROM relationships r
           JOIN entities ea ON r.entity_a = ea.id
           JOIN entities eb ON r.entity_b = eb.id
           WHERE r.entity_a=? OR r.entity_b=?""",
        (entity_id, entity_id)
    ).fetchall()

    hop1_ids = set()
    print(f"\n  --- Direct (hop 1) ---")
    for r in rels:
        if r['id_a'] == entity_id:
            other_id, other_name = r['id_b'], r['name_b']
        else:
            other_id, other_name = r['id_a'], r['name_a']
        hop1_ids.add(other_id)
        amt = f"  ${r['amount']:,.2f}" if r['amount'] else ""
        print(f"    → {other_name:30} [{r['rel_type']}] {r['description'] or ''}{amt}")

    print(f"\n  --- Through connections (hop 2) ---")
    for hop1 in hop1_ids:
        rels2 = conn.execute(
            """SELECT r.*, ea.name as name_a, eb.name as name_b,
                      ea.id as id_a, eb.id as id_b
               FROM relationships r
               JOIN entities ea ON r.entity_a = ea.id
               JOIN entities eb ON r.entity_b = eb.id
               WHERE (r.entity_a=? OR r.entity_b=?) AND r.entity_a!=? AND r.entity_b!=?""",
            (hop1, hop1, entity_id, entity_id)
        ).fetchall()
        hop1_name = conn.execute("SELECT name FROM entities WHERE id=?", (hop1,)).fetchone()['name']
        for r in rels2:
            if r['id_a'] == hop1:
                other_name = r['name_b']
            else:
                other_name = r['name_a']
            print(f"    → {hop1_name} → {other_name:25} [{r['rel_type']}]")


def cmd_gaps(conn):
    """Find gaps: entities without relationships, evidence without cases, orphan references."""
    print(f"\n{'='*60}")
    print(f"GAP ANALYSIS — caseDB alignment check")
    print(f"{'='*60}")

    lonely = conn.execute("""
        SELECT e.id, e.name, e.type FROM entities e
        WHERE e.id NOT IN (SELECT entity_a FROM relationships)
          AND e.id NOT IN (SELECT entity_b FROM relationships)
          AND e.id NOT IN (SELECT entity_id FROM case_parties)
    """).fetchall()
    if lonely:
        print(f"\n  --- ORPHAN ENTITIES ({len(lonely)}) — no relationships or case roles ---")
        for e in lonely:
            print(f"    {e['id']:35} {e['name']} [{e['type']}]")

    ev_no_case = conn.execute("SELECT id, title FROM evidence WHERE case_ids IS NULL OR case_ids = '[]'").fetchall()
    if ev_no_case:
        print(f"\n  --- EVIDENCE NOT LINKED TO CASES ({len(ev_no_case)}) ---")
        for e in ev_no_case:
            print(f"    {e['id']:35} {e['title']}")

    ev_no_entity = conn.execute("SELECT id, title FROM evidence WHERE entity_ids IS NULL OR entity_ids = '[]'").fetchall()
    if ev_no_entity:
        print(f"\n  --- EVIDENCE NOT LINKED TO ENTITIES ({len(ev_no_entity)}) ---")
        for e in ev_no_entity:
            print(f"    {e['id']:35} {e['title']}")

    cases_no_party = conn.execute("""
        SELECT c.id, c.caption FROM cases c
        WHERE c.id NOT IN (SELECT DISTINCT case_id FROM case_parties)
    """).fetchall()
    if cases_no_party:
        print(f"\n  --- CASES WITH NO PARTIES ({len(cases_no_party)}) ---")
        for c in cases_no_party:
            print(f"    {c['id']:20} {c['caption']}")

    entities_no_notes = conn.execute("SELECT id, name FROM entities WHERE notes IS NULL OR notes = ''").fetchall()
    if entities_no_notes:
        print(f"\n  --- ENTITIES WITH NO NOTES ({len(entities_no_notes)}) ---")
        for e in entities_no_notes:
            print(f"    {e['id']:35} {e['name']}")

    hearings_no_judge = conn.execute("SELECT id, date FROM hearings WHERE judge_id IS NULL").fetchall()
    if hearings_no_judge:
        print(f"\n  --- HEARINGS WITHOUT JUDGE ({len(hearings_no_judge)}) ---")
        for h in hearings_no_judge:
            print(f"    {h['id']:30} {h['date']}")

    graph_orphans = conn.execute("""
        SELECT id FROM graph_nodes
        WHERE id NOT IN (SELECT source FROM graph_edges)
          AND id NOT IN (SELECT target FROM graph_edges)
    """).fetchall()
    if graph_orphans:
        print(f"\n  --- GRAPH NODES WITH NO EDGES ({len(graph_orphans)}) ---")
        for g in graph_orphans:
            print(f"    {g['id']}")

    foia_no_due = conn.execute("SELECT id, agency_id FROM foia_requests WHERE due_date IS NULL").fetchall()
    if foia_no_due:
        print(f"\n  --- FOIA REQUESTS WITHOUT DUE DATE ({len(foia_no_due)}) ---")
        for f in foia_no_due:
            print(f"    {f['id']}")

    ref_entities = set()
    for table, col in [("relationships", "entity_a"), ("relationships", "entity_b"),
                        ("case_parties", "entity_id"), ("hearings", "judge_id")]:
        rows = conn.execute(f"SELECT DISTINCT {col} FROM {table} WHERE {col} IS NOT NULL").fetchall()
        for r in rows:
            ref_entities.add(r[0])
    all_entities = set(r[0] for r in conn.execute("SELECT id FROM entities").fetchall())
    dangling = ref_entities - all_entities
    if dangling:
        print(f"\n  --- DANGLING REFERENCES ({len(dangling)}) — referenced but not in entities ---")
        for d in sorted(dangling):
            print(f"    {d}")

    if not any([lonely, ev_no_case, ev_no_entity, cases_no_party, entities_no_notes,
                hearings_no_judge, graph_orphans, foia_no_due, dangling]):
        print(f"\n  ✓ No alignment gaps found")

    total_e = conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
    total_rel = conn.execute("SELECT COUNT(*) FROM relationships").fetchone()[0]
    density = total_rel / max(total_e, 1)
    print(f"\n  DENSITY: {total_rel} relationships / {total_e} entities = {density:.2f} edges/entity")
    print(f"  TARGET: ≥1.0 edges/entity for full connectivity")


def cmd_mine(conn, entity_id):
    """Deep mine — everything touching an entity across all tables."""
    e = conn.execute("SELECT * FROM entities WHERE id=?", (entity_id,)).fetchone()
    if not e:
        print(f"No entity found: {entity_id}")
        return

    print(f"\n{'='*60}")
    print(f"DEEP MINE: {e['name']}  ({e['type']})")
    print(f"{'='*60}")

    if e['aliases']:
        print(f"Aliases:   {', '.join(jp(e['aliases']))}")
    if e['phone']:
        print(f"Phone:     {e['phone']}")
    if e['email']:
        print(f"Email:     {e['email']}")
    if e['notes']:
        print(f"Notes:     {e['notes']}")

    print(f"\n--- CASE ROLES ---")
    cp = conn.execute("""SELECT cp.case_id, cp.role, c.caption, c.status
        FROM case_parties cp JOIN cases c ON cp.case_id=c.id WHERE cp.entity_id=?""",
        (entity_id,)).fetchall()
    for p in cp:
        print(f"  {p['case_id']:20} {p['role']:18} {p['caption']} [{p['status']}]")

    print(f"\n--- RELATIONSHIPS ({entity_id} ↔ ...) ---")
    rels = conn.execute("""SELECT r.*, ea.name as name_a, eb.name as name_b
        FROM relationships r
        JOIN entities ea ON r.entity_a=ea.id
        JOIN entities eb ON r.entity_b=eb.id
        WHERE r.entity_a=? OR r.entity_b=?""", (entity_id, entity_id)).fetchall()
    for r in rels:
        other = r['name_b'] if r['entity_a'] == entity_id else r['name_a']
        amt = f"  ${r['amount']:,.2f}" if r['amount'] else ""
        dates = ""
        if r['start_date']:
            dates = f"  ({r['start_date']}"
            if r['end_date']:
                dates += f" → {r['end_date']}"
            dates += ")"
        print(f"  ↔ {other:30} [{r['rel_type']:20}] {r['description'] or ''}{amt}{dates}")

    print(f"\n--- EVIDENCE INVOLVING ---")
    evs = conn.execute("SELECT * FROM evidence WHERE entity_ids LIKE ? ORDER BY date",
                       (f"%{entity_id}%",)).fetchall()
    for ev in evs:
        print(f"  {ev['date'] or '????':10}  [{ev['ev_type']:15}] {ev['title']}")
        if ev['authenticity']:
            print(f"              Auth: {ev['authenticity']}")

    print(f"\n--- TIMELINE EVENTS ---")
    events = conn.execute("SELECT * FROM events WHERE entity_ids LIKE ? ORDER BY date",
                         (f"%{entity_id}%",)).fetchall()
    for ev in events:
        print(f"  {ev['date']}  {ev['title']}")
        if ev['significance']:
            print(f"            WHY: {ev['significance']}")

    print(f"\n--- SERVICE LOG ---")
    svc = conn.execute("""SELECT sl.*, c.caption FROM service_log sl
        LEFT JOIN cases c ON sl.case_id=c.id WHERE sl.entity_id=?""",
        (entity_id,)).fetchall()
    for s in svc:
        print(f"  {s['date']}  {s['method']:15} {s['address'] or ''} → {s['result'] or 'pending'}")

    print(f"\n--- AGENCY REFERRALS ---")
    refs = conn.execute("SELECT * FROM agency_referrals WHERE agency_id=? OR subject LIKE ?",
                       (entity_id, f"%{e['name']}%")).fetchall()
    for ref in refs:
        print(f"  {ref['date_sent']}  {ref['subject'][:80]}  [{ref['status']}]")

    print(f"\n--- FOIA REQUESTS ---")
    foias = conn.execute("SELECT * FROM foia_requests WHERE agency_id=? OR subject LIKE ?",
                        (entity_id, f"%{e['name']}%")).fetchall()
    for f in foias:
        print(f"  {f['date_sent']}  {f['subject'][:80]}  [{f['status']}]")

    print(f"\n--- GRAPH POSITION ---")
    node = conn.execute("SELECT * FROM graph_nodes WHERE id=?", (entity_id,)).fetchone()
    if node:
        in_edges = conn.execute("SELECT COUNT(*) FROM graph_edges WHERE target=?", (entity_id,)).fetchone()[0]
        out_edges = conn.execute("SELECT COUNT(*) FROM graph_edges WHERE source=?", (entity_id,)).fetchone()[0]
        print(f"  Node type: {node['node_type']}  Tier: {node['tier'] or 'unset'}")
        print(f"  Inbound edges: {in_edges}  Outbound edges: {out_edges}")
    else:
        print(f"  ⚠ NOT IN GRAPH — run: python braid.py graph")


def cmd_stats(conn):
    """Database statistics and coverage report."""
    print(f"\n{'='*60}")
    print(f"DATABASE STATISTICS")
    print(f"{'='*60}")

    tables = ["entities", "cases", "case_parties", "events", "evidence",
              "exhibits", "documents", "relationships", "properties",
              "service_log", "agency_referrals", "foia_requests", "hearings",
              "provenance", "graph_nodes", "graph_edges"]
    for t in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t:25} {count:>4} rows")

    print(f"\n--- ENTITY TYPES ---")
    types = conn.execute("SELECT type, COUNT(*) as cnt FROM entities GROUP BY type ORDER BY cnt DESC").fetchall()
    for t in types:
        print(f"  {t['type']:15} {t['cnt']:>4}")

    print(f"\n--- RELATIONSHIP TYPES ---")
    rtypes = conn.execute("SELECT rel_type, COUNT(*) as cnt FROM relationships GROUP BY rel_type ORDER BY cnt DESC").fetchall()
    for r in rtypes:
        print(f"  {r['rel_type']:20} {r['cnt']:>4}")

    print(f"\n--- EVIDENCE TYPES ---")
    etypes = conn.execute("SELECT ev_type, COUNT(*) as cnt FROM evidence GROUP BY ev_type ORDER BY cnt DESC").fetchall()
    for e in etypes:
        print(f"  {e['ev_type']:20} {e['cnt']:>4}")

    print(f"\n--- CASE STATUS ---")
    cstats = conn.execute("SELECT status, COUNT(*) as cnt FROM cases GROUP BY status ORDER BY cnt DESC").fetchall()
    for c in cstats:
        print(f"  {c['status']:20} {c['cnt']:>4}")

    print(f"\n--- FOIA STATUS ---")
    fstats = conn.execute("SELECT status, COUNT(*) as cnt FROM foia_requests GROUP BY status ORDER BY cnt DESC").fetchall()
    for f in fstats:
        print(f"  {f['status']:20} {f['cnt']:>4}")

    print(f"\n--- REFERRAL STATUS ---")
    rstats = conn.execute("SELECT status, COUNT(*) as cnt FROM agency_referrals GROUP BY status ORDER BY cnt DESC").fetchall()
    for r in rstats:
        print(f"  {r['status']:20} {r['cnt']:>4}")

    ev_range = conn.execute("SELECT MIN(date), MAX(date) FROM events WHERE date IS NOT NULL").fetchone()
    print(f"\n  Timeline span: {ev_range[0]} → {ev_range[1]}")
    prov = conn.execute("SELECT MAX(braided_at) FROM provenance").fetchone()
    print(f"  Last braided:  {prov[0] or 'never'}")


def cmd_board(conn, org_id):
    """Board composition and connection analysis for an organization."""
    org = conn.execute("SELECT * FROM entities WHERE id=?", (org_id,)).fetchone()
    if not org:
        print(f"No entity found: {org_id}")
        return

    print(f"\n{'='*60}")
    print(f"BOARD: {org['name']}")
    print(f"{'='*60}")

    members = conn.execute("""
        SELECT r.entity_a, ea.name, r.description, r.source
        FROM relationships r
        JOIN entities ea ON r.entity_a = ea.id
        WHERE r.entity_b = ? AND r.rel_type = 'board-member'
        ORDER BY ea.name
    """, (org_id,)).fetchall()

    for m in members:
        print(f"\n  {m['name']}")
        print(f"    Role: {m['description'] or 'Board member'}")

        other_rels = conn.execute("""
            SELECT r.entity_b, eb.name, r.rel_type, r.description
            FROM relationships r
            JOIN entities eb ON r.entity_b = eb.id
            WHERE r.entity_a = ? AND r.entity_b != ?
        """, (m['entity_a'], org_id)).fetchall()
        for or_ in other_rels:
            print(f"    → {or_['name']:30} [{or_['rel_type']}] {or_['description'] or ''}")

        back_rels = conn.execute("""
            SELECT r.entity_a, ea.name, r.rel_type, r.description
            FROM relationships r
            JOIN entities ea ON r.entity_a = ea.id
            WHERE r.entity_b = ? AND r.entity_a != ?
        """, (m['entity_a'], org_id)).fetchall()
        for br_ in back_rels:
            print(f"    ← {br_['name']:30} [{br_['rel_type']}] {br_['description'] or ''}")


def cmd_chain(conn, entity_a, entity_b):
    """Find connection chains between two entities (BFS up to 4 hops)."""
    ea = conn.execute("SELECT name FROM entities WHERE id=?", (entity_a,)).fetchone()
    eb = conn.execute("SELECT name FROM entities WHERE id=?", (entity_b,)).fetchone()
    if not ea or not eb:
        print(f"Entity not found: {entity_a if not ea else entity_b}")
        return

    print(f"\n{'='*60}")
    print(f"CHAIN: {ea['name']} → {eb['name']}")
    print(f"{'='*60}")

    def get_neighbors(eid):
        neighbors = {}
        rows = conn.execute("""
            SELECT entity_a, entity_b, rel_type, description
            FROM relationships WHERE entity_a=? OR entity_b=?""",
            (eid, eid)).fetchall()
        for r in rows:
            other = r['entity_b'] if r['entity_a'] == eid else r['entity_a']
            if other not in neighbors:
                neighbors[other] = []
            neighbors[other].append((r['rel_type'], r['description'] or ''))
        return neighbors

    from collections import deque
    queue = deque([(entity_a, [entity_a])])
    visited = {entity_a}
    chains_found = []

    while queue and len(chains_found) < 5:
        current, path = queue.popleft()
        if len(path) > 5:
            continue

        neighbors = get_neighbors(current)
        for nid, rels in neighbors.items():
            if nid == entity_b:
                chains_found.append(path + [nid])
            elif nid not in visited and len(path) < 5:
                visited.add(nid)
                queue.append((nid, path + [nid]))

    if not chains_found:
        print(f"\n  No connection found within 4 hops")
        return

    for i, chain in enumerate(chains_found):
        print(f"\n  Chain {i+1} ({len(chain)-1} hops):")
        for j in range(len(chain)-1):
            a, b = chain[j], chain[j+1]
            name_a = conn.execute("SELECT name FROM entities WHERE id=?", (a,)).fetchone()['name']
            name_b = conn.execute("SELECT name FROM entities WHERE id=?", (b,)).fetchone()['name']
            rels = conn.execute("""SELECT rel_type, description FROM relationships
                WHERE (entity_a=? AND entity_b=?) OR (entity_a=? AND entity_b=?)""",
                (a, b, b, a)).fetchall()
            rel_str = ", ".join(f"[{r['rel_type']}]" for r in rels)
            print(f"    {name_a} → {name_b}  {rel_str}")


def cmd_export(conn, hearing_id):
    """Export hearing briefing as markdown."""
    h = conn.execute("SELECT * FROM hearings WHERE id=?", (hearing_id,)).fetchone()
    if not h:
        print(f"No hearing found: {hearing_id}")
        return

    judge = conn.execute("SELECT name FROM entities WHERE id=?", (h['judge_id'],)).fetchone()

    lines = []
    lines.append(f"# HEARING BRIEF — {h['id']}")
    lines.append(f"**Date:** {h['date']} {h['time'] or ''}")
    lines.append(f"**Judge:** {judge['name'] if judge else 'TBD'}")
    lines.append(f"**Location:** {h['courtroom'] or ''} — {h['court_address'] or ''}")
    lines.append("")

    case_ids = jp(h['case_ids'])
    for cid in case_ids:
        c = conn.execute("SELECT * FROM cases WHERE id=?", (cid,)).fetchone()
        if c:
            lines.append(f"## {c['id']} — {c['caption']}")
            parties = conn.execute(
                "SELECT cp.role, e.name FROM case_parties cp JOIN entities e ON cp.entity_id=e.id WHERE cp.case_id=?",
                (cid,)
            ).fetchall()
            for p in parties:
                lines.append(f"- **{p['role']}:** {p['name']}")
            lines.append("")

            evs = conn.execute("SELECT * FROM evidence WHERE case_ids LIKE ?", (f"%{cid}%",)).fetchall()
            if evs:
                lines.append("### Evidence")
                for e in evs:
                    lines.append(f"- [{e['ev_type']}] **{e['title']}** — {e['description'] or ''}")
                lines.append("")

    output = "\n".join(lines)
    outfile = f"BRIEF_{hearing_id.upper().replace('-','_')}.md"
    with open(outfile, "w") as f:
        f.write(output)
    print(f"Exported: {outfile}")
    print(output)


# ============================================================
# DISPATCH
# ============================================================
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    conn = connect()
    cmd = sys.argv[1].lower()

    if cmd == "hearing" and len(sys.argv) >= 3:
        cmd_hearing(conn, sys.argv[2])
    elif cmd == "case" and len(sys.argv) >= 3:
        cmd_case(conn, sys.argv[2])
    elif cmd == "entity" and len(sys.argv) >= 3:
        cmd_entity(conn, sys.argv[2])
    elif cmd == "timeline" and len(sys.argv) >= 4:
        cmd_timeline(conn, sys.argv[2], sys.argv[3])
    elif cmd == "evidence" and len(sys.argv) >= 3:
        cmd_evidence(conn, sys.argv[2])
    elif cmd == "foia":
        cmd_foia(conn)
    elif cmd == "upcoming":
        cmd_upcoming(conn)
    elif cmd == "search" and len(sys.argv) >= 3:
        cmd_search(conn, " ".join(sys.argv[2:]))
    elif cmd == "network" and len(sys.argv) >= 3:
        cmd_network(conn, sys.argv[2])
    elif cmd == "export" and len(sys.argv) >= 3:
        cmd_export(conn, sys.argv[2])
    elif cmd == "gaps":
        cmd_gaps(conn)
    elif cmd == "mine" and len(sys.argv) >= 3:
        cmd_mine(conn, sys.argv[2])
    elif cmd == "stats":
        cmd_stats(conn)
    elif cmd == "board" and len(sys.argv) >= 3:
        cmd_board(conn, sys.argv[2])
    elif cmd == "chain" and len(sys.argv) >= 4:
        cmd_chain(conn, sys.argv[2], sys.argv[3])
    else:
        print(__doc__)

    conn.close()

if __name__ == "__main__":
    main()
