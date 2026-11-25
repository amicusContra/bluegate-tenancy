"""
Mesh Bridge — Braids caseDB into the ecoPrimals evidence pipeline.

Usage:
    python braid.py hash          # BLAKE3 hash all records → provenance table
    python braid.py manifest      # Generate evidence-manifest.toml (mesh-compatible)
    python braid.py graph         # Export to graph_nodes + graph_edges (detroit site format)
    python braid.py sync-config   # Sync entities → detroit site config.toml format
    python braid.py export-edges  # Export edges.toml for detroit.primals.eco
    python braid.py full          # Run all of the above in sequence
    python braid.py status        # Show braid status summary

Maps the caseDB provenance trio:
    fossilRecord   → rhizoCrypt  (immutable epoch archive)
    CASE_REGISTRY  → loamSpine   (typed case metadata)
    GRAPH_DATA     → sweetGrass  (entity-relationship intelligence)
"""
import sqlite3
import json
import sys
import os
from datetime import datetime, timezone

try:
    import blake3
    HAS_BLAKE3 = True
except ImportError:
    import hashlib
    HAS_BLAKE3 = False
    print("WARNING: blake3 not available, falling back to hashlib blake2b")

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caseDB.sqlite")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def b3hash(data: str) -> str:
    """BLAKE3 hash a string, returning hex digest."""
    encoded = data.encode("utf-8")
    if HAS_BLAKE3:
        return blake3.blake3(encoded).hexdigest()
    else:
        return hashlib.blake2b(encoded, digest_size=32).hexdigest()

def serialize_row(row) -> str:
    """Deterministic JSON serialization of a database row."""
    d = dict(row)
    return json.dumps(d, sort_keys=True, default=str)


def cmd_hash(conn):
    """BLAKE3 hash every record in every core table → provenance table."""
    conn.execute("""CREATE TABLE IF NOT EXISTS provenance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        record_type TEXT NOT NULL, record_id TEXT NOT NULL,
        blake3 TEXT, braided_at TEXT, collection TEXT,
        merkle_root TEXT, source_gate TEXT DEFAULT 'northGate',
        verified_by TEXT, notes TEXT,
        UNIQUE(record_type, record_id))""")

    tables = {
        "entities": "id",
        "cases": "id",
        "events": "id",
        "evidence": "id",
        "documents": "id",
        "relationships": "id",
        "hearings": "id",
        "agency_referrals": "id",
        "foia_requests": "id",
    }

    now = datetime.now(timezone.utc).isoformat()
    total = 0

    for table, pk in tables.items():
        rows = conn.execute(f"SELECT * FROM {table}").fetchall()
        for row in rows:
            record_id = str(row[pk])
            serialized = serialize_row(row)
            h = b3hash(serialized)

            conn.execute("""INSERT OR REPLACE INTO provenance
                (record_type, record_id, blake3, braided_at, source_gate)
                VALUES (?, ?, ?, ?, ?)""",
                (table, record_id, h, now, "northGate"))
            total += 1

    conn.commit()
    print(f"  Hashed {total} records across {len(tables)} tables")
    print(f"  Hash algorithm: {'BLAKE3' if HAS_BLAKE3 else 'blake2b (fallback)'}")
    print(f"  Braided at: {now}")


def cmd_manifest(conn):
    """Generate evidence-manifest.toml compatible with origin pipeline."""
    evidence = conn.execute("SELECT * FROM evidence ORDER BY date").fetchall()
    provenance = {row["record_id"]: dict(row) for row in
                  conn.execute("SELECT * FROM provenance WHERE record_type='evidence'").fetchall()}

    lines = [
        "# Evidence Manifest — caseDB → origin pipeline",
        f"# Generated: {datetime.now(timezone.utc).isoformat()}",
        f"# Source: northGate caseDB (bluegate-tenancy/caseDB/caseDB.sqlite)",
        f"# Hash: {'BLAKE3' if HAS_BLAKE3 else 'blake2b'}",
        "",
    ]

    for ev in evidence:
        eid = ev["id"]
        prov = provenance.get(eid, {})
        lines.append(f"[[evidence]]")
        lines.append(f'id = "{eid}"')
        lines.append(f'title = "{ev["title"]}"')
        lines.append(f'type = "{ev["ev_type"]}"')
        if ev["date"]:
            lines.append(f'date = "{ev["date"]}"')
        if ev["source"]:
            lines.append(f'source = "{ev["source"]}"')
        if ev["file_path"]:
            lines.append(f'file_path = "{ev["file_path"]}"')
        if prov.get("blake3"):
            lines.append(f'blake3 = "{prov["blake3"]}"')
        if ev["authenticity"]:
            lines.append(f'authenticity = "{ev["authenticity"]}"')
        if ev["case_ids"]:
            cases = json.loads(ev["case_ids"])
            lines.append(f'cases = {json.dumps(cases)}')
        lines.append("")

    outpath = os.path.join(os.path.dirname(DB_PATH), "evidence-manifest.toml")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Written: {outpath} ({len(evidence)} evidence items)")


def cmd_graph(conn):
    """Populate graph_nodes and graph_edges from relational data."""
    conn.execute("""CREATE TABLE IF NOT EXISTS graph_nodes (
        id TEXT PRIMARY KEY, node_type TEXT NOT NULL, label TEXT NOT NULL,
        tier INTEGER, page TEXT, data TEXT)""")
    conn.execute("""CREATE TABLE IF NOT EXISTS graph_edges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL, target TEXT NOT NULL, edge_type TEXT NOT NULL,
        epistemic TEXT DEFAULT 'record', note TEXT, source_doc TEXT,
        temporal TEXT, amount REAL, UNIQUE(source, target, edge_type))""")

    conn.execute("DELETE FROM graph_nodes")
    conn.execute("DELETE FROM graph_edges")

    entities = conn.execute("SELECT * FROM entities").fetchall()
    for e in entities:
        node_type = e["type"]
        if node_type == "person":
            if "judge" in (e["notes"] or "").lower() or "judge" in (e["id"] or ""):
                node_type = "judge"
        tier = None
        data = {}
        if e["aliases"]:
            data["aliases"] = json.loads(e["aliases"])
        if e["addresses"]:
            data["addresses"] = json.loads(e["addresses"])

        conn.execute("INSERT OR REPLACE INTO graph_nodes (id, node_type, label, tier, data) VALUES (?,?,?,?,?)",
                     (e["id"], node_type, e["name"], tier, json.dumps(data) if data else None))

    cases_rows = conn.execute("SELECT * FROM cases").fetchall()
    for c in cases_rows:
        conn.execute("INSERT OR REPLACE INTO graph_nodes (id, node_type, label, data) VALUES (?,?,?,?)",
                     (c["id"], "case", f"{c['id']} — {c['caption']}", json.dumps({"case_type": c["case_type"], "status": c["status"]})))

    rels = conn.execute("SELECT * FROM relationships").fetchall()
    for r in rels:
        temporal = {}
        if r["start_date"]:
            temporal["start_date"] = r["start_date"]
        if r["end_date"]:
            temporal["end_date"] = r["end_date"]

        conn.execute("""INSERT OR REPLACE INTO graph_edges
            (source, target, edge_type, epistemic, note, source_doc, temporal, amount)
            VALUES (?,?,?,?,?,?,?,?)""",
            (r["entity_a"], r["entity_b"], r["rel_type"], "record",
             r["description"], r["source"],
             json.dumps(temporal) if temporal else None, r["amount"]))

    parties = conn.execute("SELECT * FROM case_parties").fetchall()
    for p in parties:
        conn.execute("""INSERT OR REPLACE INTO graph_edges
            (source, target, edge_type, epistemic, note) VALUES (?,?,?,?,?)""",
            (p["entity_id"], p["case_id"], "party-to", "record", p["role"]))

    node_count = conn.execute("SELECT COUNT(*) FROM graph_nodes").fetchone()[0]
    edge_count = conn.execute("SELECT COUNT(*) FROM graph_edges").fetchone()[0]
    conn.commit()
    print(f"  Graph: {node_count} nodes, {edge_count} edges")


def cmd_export_edges(conn):
    """Export edges in TOML format for detroit.primals.eco data/edges.toml."""
    edges = conn.execute("""SELECT ge.*, gn_s.label as source_label, gn_t.label as target_label
        FROM graph_edges ge
        LEFT JOIN graph_nodes gn_s ON ge.source = gn_s.id
        LEFT JOIN graph_nodes gn_t ON ge.target = gn_t.id
        ORDER BY ge.edge_type, ge.source""").fetchall()

    lines = [
        "# Edge data for detroit.primals.eco — auto-generated from caseDB",
        f"# Generated: {datetime.now(timezone.utc).isoformat()}",
        f"# Total edges: {len(edges)}",
        "",
    ]

    for e in edges:
        lines.append("[[edge]]")
        lines.append(f'source = "{e["source"]}"')
        lines.append(f'target = "{e["target"]}"')
        lines.append(f'type = "{e["edge_type"]}"')
        lines.append(f'epistemic_status = "{e["epistemic"] or "record"}"')
        if e["note"]:
            lines.append(f'note = """{e["note"]}"""')
        if e["source_doc"]:
            lines.append(f'source_doc = "{e["source_doc"]}"')
        if e["amount"]:
            lines.append(f'amount = {e["amount"]}')
        lines.append("")

    outpath = os.path.join(os.path.dirname(DB_PATH), "edges.toml")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Written: {outpath} ({len(edges)} edges)")


def cmd_sync_config(conn):
    """Export entity data in config.toml [extra.actors.*] format."""
    entities = conn.execute("""SELECT e.*, GROUP_CONCAT(DISTINCT cp.role) as roles,
        GROUP_CONCAT(DISTINCT cp.case_id) as case_ids
        FROM entities e
        LEFT JOIN case_parties cp ON e.id = cp.entity_id
        GROUP BY e.id ORDER BY e.type, e.name""").fetchall()

    lines = [
        "# Actor/Entity sync from caseDB — paste into detroit site config.toml",
        f"# Generated: {datetime.now(timezone.utc).isoformat()}",
        f"# Total entities: {len(entities)}",
        "",
    ]

    for e in entities:
        key = e["id"].replace("-", "_")
        section = "actors" if e["type"] in ("person",) else "entities"
        lines.append(f'[extra.{section}.{key}]')
        lines.append(f'display = "{e["name"]}"')
        if e["aliases"]:
            aliases = json.loads(e["aliases"])
            if aliases:
                lines.append(f'aliases = {json.dumps(aliases)}')
        if e["type"]:
            lines.append(f'type = "{e["type"]}"')
        if e["roles"]:
            lines.append(f'roles = "{e["roles"]}"')
        if e["case_ids"]:
            lines.append(f'cases = "{e["case_ids"]}"')
        if e["notes"]:
            safe_notes = e["notes"].replace('"', '\\"')
            lines.append(f'notes = "{safe_notes}"')
        lines.append("")

    outpath = os.path.join(os.path.dirname(DB_PATH), "config-sync.toml")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Written: {outpath} ({len(entities)} entities)")


def cmd_status(conn):
    """Braid status dashboard."""
    print(f"\n{'='*60}")
    print(f"BRAID STATUS — caseDB ↔ ecoPrimals Mesh")
    print(f"{'='*60}")

    try:
        prov_count = conn.execute("SELECT COUNT(*) FROM provenance").fetchone()[0]
        latest = conn.execute("SELECT MAX(braided_at) FROM provenance").fetchone()[0]
    except:
        prov_count = 0
        latest = "never"

    try:
        node_count = conn.execute("SELECT COUNT(*) FROM graph_nodes").fetchone()[0]
        edge_count = conn.execute("SELECT COUNT(*) FROM graph_edges").fetchone()[0]
    except:
        node_count = 0
        edge_count = 0

    ev_count = conn.execute("SELECT COUNT(*) FROM evidence").fetchone()[0]
    entity_count = conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
    case_count = conn.execute("SELECT COUNT(*) FROM cases").fetchone()[0]
    event_count = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    rel_count = conn.execute("SELECT COUNT(*) FROM relationships").fetchone()[0]

    print(f"\n  Provenance trio mapping:")
    print(f"    rhizoCrypt  → fossilRecord  : {'3 epochs' if True else 'unknown'}")
    print(f"    loamSpine   → CASE_REGISTRY : {case_count} cases, {entity_count} entities")
    print(f"    sweetGrass  → GRAPH_DATA    : {node_count} nodes, {edge_count} edges")

    print(f"\n  Braid status:")
    print(f"    Records hashed:    {prov_count}")
    print(f"    Last braided:      {latest}")
    print(f"    Hash algorithm:    {'BLAKE3' if HAS_BLAKE3 else 'blake2b (fallback)'}")
    print(f"    Source gate:       northGate")

    print(f"\n  Data surface:")
    print(f"    Evidence items:    {ev_count}")
    print(f"    Timeline events:   {event_count}")
    print(f"    Relationships:     {rel_count}")
    print(f"    Cases:             {case_count}")
    print(f"    Entities:          {entity_count}")

    manifest = os.path.join(os.path.dirname(DB_PATH), "evidence-manifest.toml")
    edges_file = os.path.join(os.path.dirname(DB_PATH), "edges.toml")
    config_file = os.path.join(os.path.dirname(DB_PATH), "config-sync.toml")

    print(f"\n  Export files:")
    for f, label in [(manifest, "evidence-manifest.toml"), (edges_file, "edges.toml"), (config_file, "config-sync.toml")]:
        if os.path.exists(f):
            size = os.path.getsize(f)
            print(f"    {label:30} {size/1024:.1f} KB")
        else:
            print(f"    {label:30} NOT GENERATED (run: python braid.py full)")

    print(f"\n  Mesh integration:")
    print(f"    Git push → relay:       Ready (token available)")
    print(f"    WireGuard mesh → origin: Not yet (northGate enrollment pending)")
    print(f"    evidence.ingest via UDS:    Not yet (cellMembrane command not built)")
    print(f"    Current path:               git push → evidence.push → braid")


def cmd_full(conn):
    """Run all braiding steps in sequence."""
    print(f"\n{'='*60}")
    print(f"FULL BRAID — caseDB → mesh pipeline")
    print(f"{'='*60}")

    print(f"\n1. Hashing all records (BLAKE3)...")
    cmd_hash(conn)

    print(f"\n2. Building graph (nodes + edges)...")
    cmd_graph(conn)

    print(f"\n3. Generating evidence manifest...")
    cmd_manifest(conn)

    print(f"\n4. Exporting edges.toml...")
    cmd_export_edges(conn)

    print(f"\n5. Syncing config.toml entities...")
    cmd_sync_config(conn)

    print(f"\n6. Status...")
    cmd_status(conn)

    print(f"\n{'='*60}")
    print(f"BRAID COMPLETE")
    print(f"{'='*60}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    conn = connect()
    cmd = sys.argv[1].lower()

    cmds = {
        "hash": lambda: cmd_hash(conn),
        "manifest": lambda: cmd_manifest(conn),
        "graph": lambda: cmd_graph(conn),
        "sync-config": lambda: cmd_sync_config(conn),
        "export-edges": lambda: cmd_export_edges(conn),
        "full": lambda: cmd_full(conn),
        "status": lambda: cmd_status(conn),
    }

    if cmd in cmds:
        cmds[cmd]()
    else:
        print(__doc__)

    conn.close()

if __name__ == "__main__":
    main()
