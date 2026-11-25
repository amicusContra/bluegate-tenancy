# bluegate-tenancy

Case workspace for Ingham County civil litigation, PPO proceedings, and Wayne County custody venue transfer.

## Quick Navigation

| Path | Purpose |
|------|---------|
| `01-case/_index/CASE_REGISTRY.md` | **Start here.** All 10 cases, parties, judges, timeline, and active document registry. |
| `01-case/_index/GRAPH_SCHEMA.md` | Reusable directed graph model for case intelligence. |
| `01-case/_index/GRAPH_DATA.md` | Concrete graph: 11 persons, 6 entities, 10 cases, 16 events, 25+ edges. |
| `01-case/filing-ready/` | **31 active documents** ready for filing or mailing. |
| `01-case/strategy/active/` | **9 active strategy docs** — current operational plans. |
| `02-evidence/` | 2,500+ evidence files organized by source type. See `EVIDENCE_SOURCE_MAP.md`. |
| `fossilRecord/` | **124 archived documents** across 3 epochs. Read-only reference. |

## Case Number Formats

| Type | Format | Example |
|------|--------|---------|
| Civil (Ingham) | `2026-XXXX-CZ` | `2026-4349-CZ` (Mok v. Banks) |
| PPO (Ingham) | `26-0000004XXX-PH/PP` | `26-0000004432-PP` (Mitchell v. Shayla) |
| Custody (Wayne) | `26-XXXXXX-DC` | `26-108221-DC` (Smith v. Mitchell) |

## Judges

- **Stokes** — Ingham 30th Circuit — Civil cases (2026-4349-CZ, 2026-4301-CZ)
- **Koenig** — Ingham 30th Circuit — All PPOs (6 cases, hearings Sep 29 + Oct 20)
- **Triplett** — Wayne 3rd Circuit — Custody (26-108221-DC, CMC Oct 9)

## Architecture

```
bluegate-tenancy/
├── 01-case/
│   ├── _index/          ← CASE_REGISTRY, GRAPH_SCHEMA, GRAPH_DATA
│   ├── filing-ready/    ← 31 active docs (motions, affidavits, demands, press)
│   │   └── packet/      ← Federal packet sections (23 modules)
│   ├── strategy/active/ ← 9 current strategy docs
│   ├── research/        ← OSINT + judge research
│   └── (other dirs)     ← briefs, incidents, outreach, profiles
├── 02-evidence/         ← 2,500+ files (screenshots, ROD, PACER, Ring, texts, etc.)
├── fossilRecord/        ← 124 archived docs in 3 temporal epochs
│   ├── epoch0_foundation_sep4-sep10/     (52 docs)
│   ├── epoch1_agency_blitz_sep10-sep16/  (58 docs)
│   └── epoch2_service_battle_sep17-sep21/ (14 docs)
├── records/             ← Education + housing records
└── tools/               ← Audit scripts, OSINT tools, Forgejo staging
```

## Related Repos

- `publicRecord-detroit/` — Public-facing Banks enterprise archive (actors, entities, patterns, judges)
- `wateringHole/fossilRecord/` — Source of the fossilRecord convention
