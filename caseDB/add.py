"""
Quick-add tool for the case database.

Usage:
    python add.py event 2026-10-01 "Default motion filed" --cases 2026-4301-CZ,2026-4349-CZ --desc "Filed via TrueFiling."
    python add.py evidence forged-qcd "Forged QCD document" document --source "Wayne ROD" --cases 2026-4301-CZ
    python add.py service 2026-4301-CZ smith-leon 2026-09-28 first-class "17370 Dresden" --result delivered
    python add.py foia foia-dpscd-oct "dpscd" 2026-10-01 2026-10-08 "Board minutes request"
    python add.py exhibit ppo-hearing-sep29 "Tab 3A" --evidence ring-camera-sep2 --desc "Ring camera assault video"
    python add.py hearing new-hearing-id 2026-11-01 13:00 judge-koenig motion --cases 26-4432-PP --room "Courtroom 4"
"""
import sqlite3
import json
import sys
import os
import argparse

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caseDB.sqlite")

def j(val):
    if val and "," in val:
        return json.dumps(val.split(","))
    elif val:
        return json.dumps([val])
    return None

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def add_event(args):
    conn = connect()
    conn.execute(
        """INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
           VALUES (?,?,?,?,?,?,?)""",
        (args.date, args.title, args.desc, j(args.cases), j(args.entities), args.source, args.significance)
    )
    conn.commit()
    print(f"Added event: {args.date} — {args.title}")
    conn.close()

def add_evidence(args):
    conn = connect()
    conn.execute(
        """INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity, notes)
           VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        (args.id, args.title, args.type, args.source, args.filepath, args.desc, args.date, j(args.entities), j(args.cases), args.auth, args.notes)
    )
    conn.commit()
    print(f"Added evidence: {args.id} — {args.title}")
    conn.close()

def add_service(args):
    conn = connect()
    conn.execute(
        """INSERT INTO service_log (case_id, entity_id, date, method, address, tracking, result, notes)
           VALUES (?,?,?,?,?,?,?,?)""",
        (args.case_id, args.entity_id, args.date, args.method, args.address, args.tracking, args.result, args.notes)
    )
    conn.commit()
    print(f"Added service: {args.entity_id} on {args.date} via {args.method}")
    conn.close()

def add_foia(args):
    conn = connect()
    conn.execute(
        """INSERT OR REPLACE INTO foia_requests (id, agency_id, date_sent, due_date, subject, status)
           VALUES (?,?,?,?,?,?)""",
        (args.id, args.agency, args.sent, args.due, args.subject, "sent")
    )
    conn.commit()
    print(f"Added FOIA: {args.id} — {args.subject}")
    conn.close()

def add_exhibit(args):
    conn = connect()
    conn.execute(
        """INSERT INTO exhibits (hearing_id, tab, evidence_id, document_id, description)
           VALUES (?,?,?,?,?)""",
        (args.hearing_id, args.tab, args.evidence, args.document, args.desc)
    )
    conn.commit()
    print(f"Added exhibit: {args.tab} → {args.hearing_id}")
    conn.close()

def add_hearing(args):
    conn = connect()
    conn.execute(
        """INSERT OR REPLACE INTO hearings (id, case_ids, date, time, judge_id, courtroom, hearing_type, status)
           VALUES (?,?,?,?,?,?,?,?)""",
        (args.id, j(args.cases), args.date, args.time, args.judge, args.room, args.type, "scheduled")
    )
    conn.commit()
    print(f"Added hearing: {args.id} on {args.date}")
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Quick-add to case database")
    sub = parser.add_subparsers(dest="command")

    p_ev = sub.add_parser("event")
    p_ev.add_argument("date")
    p_ev.add_argument("title")
    p_ev.add_argument("--desc", default=None)
    p_ev.add_argument("--cases", default=None)
    p_ev.add_argument("--entities", default=None)
    p_ev.add_argument("--source", default=None)
    p_ev.add_argument("--significance", default=None)

    p_evi = sub.add_parser("evidence")
    p_evi.add_argument("id")
    p_evi.add_argument("title")
    p_evi.add_argument("type")
    p_evi.add_argument("--source", default=None)
    p_evi.add_argument("--filepath", default=None)
    p_evi.add_argument("--desc", default=None)
    p_evi.add_argument("--date", default=None)
    p_evi.add_argument("--entities", default=None)
    p_evi.add_argument("--cases", default=None)
    p_evi.add_argument("--auth", default=None)
    p_evi.add_argument("--notes", default=None)

    p_svc = sub.add_parser("service")
    p_svc.add_argument("case_id")
    p_svc.add_argument("entity_id")
    p_svc.add_argument("date")
    p_svc.add_argument("method")
    p_svc.add_argument("address", nargs="?", default=None)
    p_svc.add_argument("--tracking", default=None)
    p_svc.add_argument("--result", default=None)
    p_svc.add_argument("--notes", default=None)

    p_foia = sub.add_parser("foia")
    p_foia.add_argument("id")
    p_foia.add_argument("agency")
    p_foia.add_argument("sent")
    p_foia.add_argument("due")
    p_foia.add_argument("subject")

    p_ex = sub.add_parser("exhibit")
    p_ex.add_argument("hearing_id")
    p_ex.add_argument("tab")
    p_ex.add_argument("--evidence", default=None)
    p_ex.add_argument("--document", default=None)
    p_ex.add_argument("--desc", default=None)

    p_h = sub.add_parser("hearing")
    p_h.add_argument("id")
    p_h.add_argument("date")
    p_h.add_argument("time")
    p_h.add_argument("judge")
    p_h.add_argument("type")
    p_h.add_argument("--cases", default=None)
    p_h.add_argument("--room", default=None)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    {
        "event": add_event,
        "evidence": add_evidence,
        "service": add_service,
        "foia": add_foia,
        "exhibit": add_exhibit,
        "hearing": add_hearing,
    }[args.command](args)

if __name__ == "__main__":
    main()
