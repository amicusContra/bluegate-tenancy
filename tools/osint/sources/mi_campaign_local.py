"""Michigan Campaign Finance — local bulk data search.

Downloads MI SOS bulk CSV files (contributions + expenditures) and indexes
them in a SQLite database for fast local search.

First run: downloads CSVs (~500MB), builds SQLite index (~200MB).
Subsequent runs: queries instantly from local DB.

MI SOS bulk data URL pattern:
  https://miboecfr.nictusa.com/cfr/dumpall/cfrdetail/
"""

from __future__ import annotations
import csv
import io
import os
import sqlite3
import zipfile
from pathlib import Path

import httpx
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from sources.base import Source
from models import SearchResult

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DB_PATH = DATA_DIR / "mi_campaign.db"

BASE_URL = "https://miboecfr.nictusa.com/cfr/dumpall/cfrdetail"

CONTRIBUTION_FILES = [
    f"{BASE_URL}/{year}_mi_cfr_contributions.zip"
    for year in range(2018, 2027)
]

EXPENDITURE_FILES = [
    f"{BASE_URL}/{year}_mi_cfr_expenditures.zip"
    for year in range(2018, 2027)
]

SCHEMA = """
CREATE TABLE IF NOT EXISTS contributions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_seq_no TEXT,
    page_no TEXT,
    contribution_id TEXT,
    cont_detail_id TEXT,
    doc_stmnt_year TEXT,
    doc_type_desc TEXT,
    com_legal_name TEXT,
    common_name TEXT,
    cfr_com_id TEXT,
    com_type TEXT,
    can_first_name TEXT,
    can_last_name TEXT,
    contriblast_name TEXT,
    contribfirst_name TEXT,
    contriblast_or_org TEXT,
    amount REAL,
    contribution_type TEXT,
    received_date TEXT,
    aggregate REAL,
    extra_desc TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    occupation TEXT,
    employer TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS expenditures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_seq_no TEXT,
    page_no TEXT,
    expenditure_id TEXT,
    exp_detail_id TEXT,
    doc_stmnt_year TEXT,
    doc_type_desc TEXT,
    com_legal_name TEXT,
    common_name TEXT,
    cfr_com_id TEXT,
    com_type TEXT,
    can_first_name TEXT,
    can_last_name TEXT,
    lname_or_org TEXT,
    first_name TEXT,
    amount REAL,
    detail_desc TEXT,
    exp_date TEXT,
    purpose TEXT,
    extra_desc TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    supp_opp TEXT,
    source_file TEXT
);

CREATE INDEX IF NOT EXISTS idx_cont_name ON contributions(contriblast_or_org COLLATE NOCASE);
CREATE INDEX IF NOT EXISTS idx_cont_committee ON contributions(com_legal_name COLLATE NOCASE);
CREATE INDEX IF NOT EXISTS idx_cont_year ON contributions(doc_stmnt_year);
CREATE INDEX IF NOT EXISTS idx_exp_payee ON expenditures(lname_or_org COLLATE NOCASE);
CREATE INDEX IF NOT EXISTS idx_exp_committee ON expenditures(com_legal_name COLLATE NOCASE);
CREATE INDEX IF NOT EXISTS idx_exp_year ON expenditures(doc_stmnt_year);
CREATE INDEX IF NOT EXISTS idx_exp_first ON expenditures(first_name COLLATE NOCASE);
"""


def _db_ready() -> bool:
    if not DB_PATH.exists():
        return False
    conn = sqlite3.connect(str(DB_PATH))
    try:
        c = conn.execute("SELECT COUNT(*) FROM contributions")
        cont_count = c.fetchone()[0]
        c = conn.execute("SELECT COUNT(*) FROM expenditures")
        exp_count = c.fetchone()[0]
        return cont_count > 0 and exp_count > 0
    except Exception:
        return False
    finally:
        conn.close()


async def download_and_index():
    """Download MI SOS bulk CSVs and build SQLite index."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)

    async with httpx.AsyncClient(timeout=120, follow_redirects=True) as client:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            all_files = (
                [(f, "contribution") for f in CONTRIBUTION_FILES]
                + [(f, "expenditure") for f in EXPENDITURE_FILES]
            )
            task = progress.add_task("Downloading MI campaign finance data...", total=len(all_files))

            for url, file_type in all_files:
                filename = url.split("/")[-1]
                progress.update(task, description=f"Downloading {filename}...")
                try:
                    resp = await client.get(
                        url,
                        headers={"User-Agent": "Mozilla/5.0 (OSINT Research)"},
                    )
                    if resp.status_code != 200:
                        progress.update(task, advance=1)
                        continue

                    zdata = resp.content
                    try:
                        with zipfile.ZipFile(io.BytesIO(zdata)) as zf:
                            for csv_name in zf.namelist():
                                if not csv_name.lower().endswith(".csv"):
                                    continue
                                with zf.open(csv_name) as csvfile:
                                    text = csvfile.read().decode("utf-8", errors="replace")
                                    reader = csv.reader(io.StringIO(text))
                                    headers = next(reader, None)
                                    if not headers:
                                        continue
                                    _import_csv(conn, reader, headers, file_type, filename)
                    except zipfile.BadZipFile:
                        text = resp.content.decode("utf-8", errors="replace")
                        reader = csv.reader(io.StringIO(text))
                        headers = next(reader, None)
                        if headers:
                            _import_csv(conn, reader, headers, file_type, filename)

                except Exception:
                    pass
                progress.update(task, advance=1)

    conn.commit()
    conn.close()
    print(f"MI campaign finance database ready at {DB_PATH}")


def _import_csv(conn, reader, headers, file_type, source_file):
    headers_lower = [h.strip().lower().replace(" ", "_") for h in headers]

    if file_type == "contribution":
        for row in reader:
            if len(row) < 5:
                continue
            data = dict(zip(headers_lower, row))
            try:
                amount = float(data.get("amount", "0").replace(",", "").replace("$", "")) if data.get("amount") else 0
            except ValueError:
                amount = 0
            try:
                aggregate = float(data.get("aggregate", "0").replace(",", "").replace("$", "")) if data.get("aggregate") else 0
            except ValueError:
                aggregate = 0

            conn.execute("""
                INSERT INTO contributions (
                    doc_seq_no, page_no, contribution_id, cont_detail_id,
                    doc_stmnt_year, doc_type_desc, com_legal_name, common_name,
                    cfr_com_id, com_type, can_first_name, can_last_name,
                    contriblast_name, contribfirst_name, contriblast_or_org,
                    amount, contribution_type, received_date, aggregate,
                    extra_desc, address, city, state, zip,
                    occupation, employer, source_file
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                data.get("doc_seq_no", ""), data.get("page_no", ""),
                data.get("contribution_id", ""), data.get("cont_detail_id", ""),
                data.get("doc_stmnt_year", ""), data.get("doc_type_desc", ""),
                data.get("com_legal_name", ""), data.get("common_name", ""),
                data.get("cfr_com_id", ""), data.get("com_type", ""),
                data.get("can_first_name", ""), data.get("can_last_name", ""),
                data.get("contriblast_name", ""), data.get("contribfirst_name", ""),
                data.get("contriblast_or_org", ""),
                amount,
                data.get("contribution_type", ""), data.get("received_date", ""),
                aggregate,
                data.get("extra_desc", ""),
                data.get("address", ""), data.get("city", ""),
                data.get("state", ""), data.get("zip", ""),
                data.get("occupation", ""), data.get("employer", ""),
                source_file,
            ))

    elif file_type == "expenditure":
        for row in reader:
            if len(row) < 5:
                continue
            data = dict(zip(headers_lower, row))
            try:
                amount = float(data.get("amount", "0").replace(",", "").replace("$", "")) if data.get("amount") else 0
            except ValueError:
                amount = 0

            conn.execute("""
                INSERT INTO expenditures (
                    doc_seq_no, page_no, expenditure_id, exp_detail_id,
                    doc_stmnt_year, doc_type_desc, com_legal_name, common_name,
                    cfr_com_id, com_type, can_first_name, can_last_name,
                    lname_or_org, first_name, amount, detail_desc,
                    exp_date, purpose, extra_desc,
                    address, city, state, zip,
                    supp_opp, source_file
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                data.get("doc_seq_no", ""), data.get("page_no", ""),
                data.get("expenditure_id", ""), data.get("exp_detail_id", ""),
                data.get("doc_stmnt_year", ""), data.get("doc_type_desc", ""),
                data.get("com_legal_name", ""), data.get("common_name", ""),
                data.get("cfr_com_id", ""), data.get("com_type", ""),
                data.get("can_first_name", ""), data.get("can_last_name", ""),
                data.get("lname_or_org", ""), data.get("first_name", ""),
                amount,
                data.get("detail_desc", ""), data.get("exp_date", ""),
                data.get("purpose", ""), data.get("extra_desc", ""),
                data.get("address", ""), data.get("city", ""),
                data.get("state", ""), data.get("zip", ""),
                data.get("supp_opp", ""),
                source_file,
            ))


class MICampaignLocalSource(Source):
    name = "mi_campaign_local"
    requires_key = False

    def available(self) -> bool:
        return _db_ready()

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        names = [person["name"]] + person.get("aliases", [])
        seen = set()
        for name in names:
            if name in seen:
                continue
            seen.add(name)
            r = self._search_by_name(name, person["id"], person["name"])
            results.append(r)

        for eid in person.get("known_entities", []):
            from config import get_entity
            entity = get_entity(eid)
            if entity:
                r = self._search_by_name(entity["name"], person["id"], person["name"])
                results.append(r)

        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        return [self._search_by_name(entity["name"], entity["id"], entity["name"])]

    def _search_by_name(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"campaign_finance: {name}",
        )
        if not _db_ready():
            result.error = "Database not built. Run: python -m sources.mi_campaign_local --build"
            return result

        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row
        try:
            pattern = f"%{name}%"
            # Expenditure payees
            rows = conn.execute("""
                SELECT lname_or_org, first_name, amount, exp_date,
                       com_legal_name, purpose, detail_desc, doc_stmnt_year
                FROM expenditures
                WHERE lname_or_org LIKE ? OR (first_name LIKE ? AND lname_or_org LIKE ?)
                ORDER BY amount DESC LIMIT 100
            """, (pattern, pattern.split()[0] + "%" if " " in name else pattern,
                  "%" + name.split()[-1] + "%" if " " in name else pattern)).fetchall()

            for row in rows:
                result.hits.append({
                    "type": "expenditure",
                    "payee": f"{row['first_name'] or ''} {row['lname_or_org'] or ''}".strip(),
                    "amount": row["amount"],
                    "date": row["exp_date"],
                    "committee": row["com_legal_name"],
                    "purpose": row["purpose"] or row["detail_desc"],
                    "year": row["doc_stmnt_year"],
                })

            # Contribution donors
            rows = conn.execute("""
                SELECT contriblast_or_org, contribfirst_name, amount,
                       received_date, com_legal_name, occupation, employer,
                       doc_stmnt_year
                FROM contributions
                WHERE contriblast_or_org LIKE ? OR contribfirst_name LIKE ?
                ORDER BY amount DESC LIMIT 100
            """, (pattern, pattern)).fetchall()

            for row in rows:
                result.hits.append({
                    "type": "contribution",
                    "donor": f"{row['contribfirst_name'] or ''} {row['contriblast_or_org'] or ''}".strip(),
                    "amount": row["amount"],
                    "date": row["received_date"],
                    "committee": row["com_legal_name"],
                    "occupation": row["occupation"],
                    "employer": row["employer"],
                    "year": row["doc_stmnt_year"],
                })

        except Exception as e:
            result.error = str(e)
        finally:
            conn.close()
        return result


if __name__ == "__main__":
    import sys
    if "--build" in sys.argv:
        import asyncio
        asyncio.run(download_and_index())
    else:
        print("Usage: python -m sources.mi_campaign_local --build")
        print(f"DB exists: {DB_PATH.exists()}")
        print(f"DB ready: {_db_ready()}")

