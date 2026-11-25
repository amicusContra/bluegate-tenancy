import sqlite3, os

conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "caseDB.sqlite"))
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
views = conn.execute("SELECT name FROM sqlite_master WHERE type='view' ORDER BY name").fetchall()

print("TABLES:")
for t in tables:
    count = conn.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()[0]
    print(f"  {t[0]:25} {count:>4} rows")

print(f"\nVIEWS:")
for v in views:
    print(f"  {v[0]}")

size = os.path.getsize(os.path.join(os.path.dirname(__file__), "caseDB.sqlite"))
print(f"\nDB size: {size/1024:.1f} KB")
conn.close()
