# CANONICAL FILE INDEX
## What to trust, what's redundant, what's archived
## Last Updated Sep 7, 2026 (Post-reorganization)

---

## DIRECTORY STRUCTURE (as of Sep 7, 2026)

```
bluegate-tenancy/
├── 01-case/                    ← All litigation work
│   ├── profiles/               ← Individual/entity OSINT profiles (12)
│   ├── research/
│   │   ├── smith/              ← Smith family research + PACER (16)
│   │   ├── banks/              ← Banks network intel + profiles (39)
│   │   └── rico/               ← RICO framework + legal theory (8)
│   ├── strategy/
│   │   ├── active/             ← Current week plans + ops (10)
│   │   └── executed/           ← Past plans, wargames, debriefs (17)
│   ├── briefs/                 ← DaSean/Deanna prep docs (13)
│   ├── evidence-analysis/      ← Exhibit work, text analysis (9)
│   ├── incidents/              ← Incident logs (3)
│   ├── outreach/               ← External comms + discord + nolan (17)
│   ├── filing-ready/           ← Production filings (323)
│   ├── evidence/               ← OIG package (19)
│   ├── archive/                ← Pre-Sep archived docs (25)
│   ├── nuclear/                ← Consent surrender draft (1)
│   └── shayla-response-aug14/  ← Raw page scans (155)
├── 02-evidence/                ← Raw evidence (1,085)
├── 02-parenting/               ← Custody journal + calendars (6)
├── 03-color/                   ← Opponent reaction / narrative (3)
├── 03-housing/                 ← Lease + housing docs (3)
├── 04-school/                  ← DaSean DSDT coursework ONLY (7 + usb-pack)
├── 05-community/               ← Parent packet (1)
├── 05-employment/              ← DaSean resume (5)
├── 06-life-build/              ← Financial planning (10)
├── tools/osint/                ← OSINT toolkit + PACER scripts (37 .py)
├── CANONICAL_FILES.md          ← THIS FILE
├── MASTER_TIMELINE.md          ← Unified chronology
└── MASTER_NETWORK_MAP.md       ← All people, entities, connections
```

---

## LIVING DOCUMENTS (single source of truth — update these)

| File | What It Covers | New Location |
|------|---------------|-------------|
| **MASTER_NETWORK_MAP.md** | All people, entities, connections | `/MASTER_NETWORK_MAP.md` |
| **MASTER_TIMELINE.md** | Unified chronology of all events | `/MASTER_TIMELINE.md` |
| **SMITH_FAMILY_TREE_INVESTIGATION.md** | Smith inheritance, Lovelife church, $200/$202 flow, compiled intel | `research/smith/` |
| **DASEAN_SMITH_INTEGRATED_TIMELINE.md** | DaSean's relationship overlaid on Smith machine + debt cycles | `research/smith/` |
| **SMITH_PROFILES_MASTER.md** | All Smith profiles, BK history, addresses | `profiles/` |
| **BK_INTERCEPT_MATRIX.md** | Active bankruptcy hearing interception points | `research/smith/` |
| **PACER_SEARCH_MATRIX.md** | Systematic all-courts PACER search tracker | `research/smith/` |
| **RICO_FRAMEWORK.md** | RICO enterprise definition, predicate acts | `research/rico/` |
| **OPERATIONAL_PLAYBOOK.md** | Theory → live cases playbook | `strategy/active/` |
| **FILING_LOG.md** | What was filed, when, where | `strategy/active/` |
| **RICO_MONITORING_TRACKER.md** | Phase 1 evidence + defendant reactions | `research/rico/` |

---

## CANONICAL PROFILES (move to `profiles/` as created)

| File | Subject | Location |
|------|---------|----------|
| `SMITH_PROFILES_MASTER.md` | Leon, Marquita, Simone, Shayla | `profiles/` |
| `SHAYLA_PROFILE.md` | Shayla comprehensive | `profiles/` |
| `CROWDER_PROFILE.md` | Tunezha Crowder LCSW | `profiles/` |
| `JUDGE_STOKES_PROFILE.md` | Hon. Wanda Stokes (Ingham) | `profiles/` |
| `OSINT_SABREE_FAMILY.md` | Eric, Adam, Aliyah Sabree | `profiles/` |
| `OSINT_LISA_CUDWORTH.md` | Lisa Cudworth (Geise) | `profiles/` |
| `OSINT_JUSTIN_BANKS.md` | Justin M. Banks | `profiles/` |
| `SABREE_PACER_PROFILE.md` | Eric Sabree PACER | `profiles/` |
| `JUDGES_OSINT_BRIEF_SEP2.md` | Miller + Yancey OSINT | `profiles/` |
| `CRIMINAL_EXPOSURE_RUNDOWN.md` | Smith family criminal exposure | `profiles/` |
| `FELONY_TALLY_PER_MEMBER.md` | Per-member felony count | `profiles/` |

### Banks Network Profiles (in `research/banks/network-profiles/`)
| File | Subject |
|------|---------|
| `01_HOLLAND_JOSEPH_JR.md` | Joseph Holland Jr |
| `02_YANCEY_TENISHA.md` | Tenisha Yancey |
| `03_MILLER_CYLENTHIA.md` | Cylenthia LaToye Miller |
| `04_STALLWORTH_NICOLE_WELLS.md` | Nicole Wells Stallworth |
| `05_VAUGHN_CORLETTA.md` | Corletta Vaughn |
| `06_DAGNOGO_SHERRY_GAY.md` | Sherry Gay-Dagnogo |
| `07_MONEY_TRAIL.md` | Financial flow analysis |
| `08_SECONDARY_NETWORK.md` | Secondary connections |
| `09_TRIPLETT_REGINA.md` | Regina Triplett (PCA) |
| `10_BANKS_ENTITY_MAP.md` | Banks entity structure |
| `11_ENEMIES_CREDITORS_ALLIES.md` | Network map |
| `12_PROFESSIONAL_HITTERS.md` | Legal/professional allies |

---

## SMITH RESEARCH (in `research/smith/`)

| File | Purpose | Status |
|------|---------|--------|
| **SMITH_FAMILY_TREE_INVESTIGATION.md** | Harrison Twp inheritance, Leonard T Sr, Lovelife church, compiled intel | **CANONICAL — living** |
| **DASEAN_SMITH_INTEGRATED_TIMELINE.md** | DaSean timeline overlaid on Smith debt cycles + trustee period | **CANONICAL — living** |
| `SMITH_ADDRESS_INVESTIGATION_SEP6.md` | Bowman St perjury, Normandy fake address | **CANONICAL** |
| `SMITH_PROPERTY_CYCLE_PROFILE.md` | BK/mortgage/property cycle mapped to relationship | **CANONICAL** |
| `MACOMB_ROD_FINDINGS_SEP6.md` | Macomb ROD findings — Lady Bird deed, QCDs | **CANONICAL** |
| `MARQUITA_PACER_BRIEF_SEP4.md` | Marquita BK deep dive (26-47542) | **CANONICAL** |
| `SIMONE_PACER_BRIEF_SEP4.md` | Simone BK analysis (26-49404) | **CANONICAL** |
| `BK_INTERCEPT_MATRIX.md` | Active BK hearing interception schedule | **CANONICAL — living** |
| `PACER_SEARCH_MATRIX.md` | All-courts PACER search tracker | **CANONICAL — living** |
| `SMITH_CROWDER_FRAUD_TIMELINE.md` | Smith + Crowder fraud chronology | **CANONICAL** |
| `SMITH_NETWORK_CONNECTION_ANALYSIS.md` | "Ocean of predators" network model | Historical |
| `SMITH_HOUSEHOLD_MAP_SEP4.md` | Three-address shell game + vehicle map | Historical (see ADDRESS_INVESTIGATION) |
| `SMITH_OSINT_BRIEF_SEP2.md` | V1 Smith OSINT — see PROFILES_MASTER | Historical |
| `LEON_SIMONE_PACER_SEARCH_SEP4.md` | Raw PACER search results | Historical |
| `DASEAN_MARQUITA_BRIEF_SEP4.md` | Marquita findings for DaSean | Historical |
| `PACER_EXPANDED_SEARCH_PLAN.md` | Beyond-bankruptcy sweep plan | Historical |

---

## BANKS NETWORK RESEARCH (in `research/banks/`)

| File | Purpose | Status |
|------|---------|--------|
| `BANKS_HOLLAND_ROD_ANALYSIS.md` | 33 OCR'd Wayne ROD documents | **CANONICAL** |
| `BRYANT_V_MILLER_BRIEF.md` | Federal case analysis | **CANONICAL** |
| `STAT_PADDING_BRIEF.md` | PCA enrollment fraud model | **CANONICAL** |
| `CROWDER_BRIDGE_ANALYSIS.md` | Crowder as Smith↔Banks bridge | **CANONICAL** |
| `BANKS_PROFILE.md` | Banks comprehensive profile | **CANONICAL** |
| `BANKS_MONEY_TRAIL.md` | Financial flow analysis | **CANONICAL** |
| `LINKEDIN_SCRUB_SEP5.md` | LinkedIn network scrub | **CANONICAL** |
| `OUR_BENCH_AND_ALLIES.md` | Friendly judges + allies list | **CANONICAL** |
| `RITA_WILLIAMS_FULL_PROFILE.md` | Rita Williams profile | **CANONICAL** |
| `NETWORK_TOPOLOGY.json` | Machine-readable network graph | **CANONICAL** |

---

## RICO / LEGAL THEORY (in `research/rico/`)

| File | Purpose | Status |
|------|---------|--------|
| `RICO_FRAMEWORK.md` | Enterprise definition + predicate acts | **CANONICAL — living** |
| `RICO_MONITORING_TRACKER.md` | Phase 1 evidence tracking | **CANONICAL — living** |
| `NODE_ISOLATION_PLAN.md` | Graph-theory network dismantling | **CANONICAL** |
| `SETTLEMENT_DOCTRINE.md` | Settlement "onion" doctrine | **CANONICAL** |
| `KEVIN_DAMAGES_FRAMEWORK.md` | Pro se damages + hourly rate | **CANONICAL** |
| `UPL_BRIEF.md` | Unauthorized practice of law | **CANONICAL** |
| `CIVIL_CRIMINAL_FEEDBACK_LOOP.md` | Civil-criminal cross-feed | **CANONICAL** |
| `CRIMINAL_REFERRAL_STRATEGY.md` | Deanna protection / referral | **CANONICAL** |

---

## FILING-READY (in `filing-ready/` — unchanged, well-organized)

### Active fronts:
- **JTC:** Miller/Yancey supplements + Adam/Aliyah Sabree/Perkins new complaints
- **Bar:** Perkins complaint
- **RICO:** Complaint draft, exhibit index, checklist, service plan
- **FOIA:** 6 requests (4 ready to send, 2 sent)
- **Trustee:** Marquita + Simone notifications
- **Subpoenas:** 20 drafted + MC11 prefill guide
- **Macomb:** DHS fraud report, prosecutor referral

---

## STRATEGY (in `strategy/`)

### Active (`strategy/active/` — 10 files)
Current operational plans, checklists, playbooks

### Executed (`strategy/executed/` — 17 files)
Past wargames, debriefs, weekly plans (Sep 1–5)

---

## TOOLS (in `tools/osint/`)

| Script | Purpose | Status |
|--------|---------|--------|
| `pacer_family_tree_search.py` | Smith family tree PACER investigation | **Active (Sep 7)** |
| `pacer_api.py` | PACER Auth + PCL search automation | **Active** |
| `runner.py` | Multi-source OSINT sweep CLI | **Active** |
| `pacer_pull.py` | Batch PACER pull (STRIDE framework) | **Active fallback** |
| `doc_extract.py` | PDF/OCR text extraction | **Active** |
| `.pacer_creds.json` | PACER credentials | **⚠️ SENSITIVE — do not commit** |

---

## CHANGES LOG

### Sep 7, 2026 — Major Reorganization
- Created subdirectories: `profiles/`, `research/{smith,banks,rico}/`, `strategy/{active,executed}/`, `briefs/`, `evidence-analysis/`, `incidents/`, `outreach/`
- Moved 97 loose files from `01-case/` root into topic subdirs
- Moved Banks intel (39 files) from `04-school/` → `research/banks/`
- `04-school/` now contains ONLY DaSean DSDT coursework (7 files + usb-pack)
- Moved `discord/` and `nolan_clean_drop/` under `outreach/`
- Cleaned workspace root: removed `scan_fix.ps1`, `scan_fix2.ps1`, `scan_probe.ps1`, `_tmp_timeline.html`
- Added new canonical files: `SMITH_FAMILY_TREE_INVESTIGATION.md`, `SMITH_ADDRESS_INVESTIGATION_SEP6.md`, `MACOMB_ROD_FINDINGS_SEP6.md`

### Sep 5, 2026 — RICO build, FOIA batch, evidence merge
### Sep 4, 2026 — PACER deep dive, Smith household mapping
### Sep 2, 2026 — Initial OSINT sweep, evidence organization
