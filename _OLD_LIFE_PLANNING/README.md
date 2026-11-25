# DaSean Mitchell — Custody & Multi-Front Legal Portfolio

**Custody Case**: 26-108221-DC | Wayne County 3rd Circuit | Hon. Regina Triplett
**Kevin v. Smith**: 2026-4301-CZ | Ingham County Circuit | Hon. Wanda M. Stokes
**Kevin v. Banks**: 2026-4349-CZ | Ingham County Circuit | Hon. Wanda M. Stokes
**Custody Trial**: October 10, 2026
**Prepared by**: Kevin Mok

---

## Start Here

| Question | Document |
|----------|----------|
| **What's the current situation?** | [01-case/WARGAME_SEP4_UPDATE.md](01-case/WARGAME_SEP4_UPDATE.md) — Latest wargame + pressure map |
| **What's the plan for this week?** | [01-case/WEEK_AHEAD_SEP5_12.md](01-case/WEEK_AHEAD_SEP5_12.md) — Day-by-day action plan |
| **What do we know about the Smiths?** | [01-case/DEBRIEF_SEP4_EVENING.md](01-case/DEBRIEF_SEP4_EVENING.md) — Full debrief of Sep 4 findings |
| **DaSean's story (for DaSean)** | [01-case/DASEAN_SMITH_INTEGRATED_TIMELINE.md](01-case/DASEAN_SMITH_INTEGRATED_TIMELINE.md) — How the machine works |
| **What file is canonical?** | [CANONICAL_FILES.md](CANONICAL_FILES.md) — Single source of truth map |
| **Master chronology** | [MASTER_TIMELINE.md](MASTER_TIMELINE.md) — All events, all parties |
| **Network map** | [MASTER_NETWORK_MAP.md](MASTER_NETWORK_MAP.md) — People, entities, connections |
| **Evidence catalog** | [02-evidence/EVIDENCE_INDEX.md](02-evidence/EVIDENCE_INDEX.md) — Binary evidence index |
| **PACER documents** | [02-evidence/pacer-docs/INDEX.md](02-evidence/pacer-docs/INDEX.md) — Bankruptcy filings index |

---

## Directory Structure

```
bluegate-tenancy/
│
├── README.md ...................... You are here
├── CANONICAL_FILES.md ............. What to trust, what's superseded
├── MASTER_NETWORK_MAP.md .......... All people/entities/connections
├── MASTER_TIMELINE.md ............. Unified chronology (1995–present)
│
├── 01-case/ ....................... LEGAL STRATEGY & FILINGS
│   ├── WARGAME_SEP4_UPDATE.md .... Current situation report
│   ├── WEEK_AHEAD_SEP5_12.md ..... This week's plan
│   ├── DEBRIEF_SEP4_EVENING.md ... Full PACER findings debrief
│   ├── DASEAN_SMITH_INTEGRATED_TIMELINE.md . For DaSean
│   ├── SMITH_PROFILES_MASTER.md .. All Smith family profiles + SSNs
│   ├── SMITH_HOUSEHOLD_MAP_SEP4.md Three-address shell game
│   ├── MARQUITA_PACER_BRIEF_SEP4.md Marquita BK deep dive
│   ├── SIMONE_PACER_BRIEF_SEP4.md  Simone BK analysis
│   ├── LEON_SIMONE_PACER_SEARCH_SEP4.md Search results
│   ├── PACER_SEARCH_MATRIX.md .... Systematic search tracker
│   ├── filing-ready/ ............. Court-ready documents
│   │   ├── 40_FIRST_AMENDED_COMPLAINT_BANKS.txt (FILED)
│   │   ├── 36_FINAL_EMERGENCY_MOTION.txt (FILED)
│   │   ├── ppo_forms/ ........... PPO petitions (FILED Sep 4)
│   │   └── subpoenas/ ........... 20 subpoena schedules (DRAFTING)
│   ├── discord/ .................. Sanitized briefs for external sharing
│   ├── nolan_clean_drop/ ......... Attorney handoff packet
│   ├── archive/ .................. Superseded pre-September docs
│   └── shayla-response-aug14/ .... Her Aug 14 filings
│
├── 02-evidence/ ................... SINGLE CANONICAL EVIDENCE ROOT
│   ├── EVIDENCE_INDEX.md ......... Category index (updated Sep 5)
│   ├── EVIDENCE_INDEX_CUSTODY.md . Detailed custody evidence catalog
│   ├── PHOTO_GUIDE.md ............ Printable quick-reference
│   ├── pacer-docs/ ............... PACER bankruptcy filings (organized)
│   ├── wayne-rod-sep2/ ........... Wayne County ROD PDFs (7 batches)
│   ├── ring_sep2/ ................ Ring video + frames + analysis
│   ├── text-screenshots/ ......... DaSean/Shayla text messages
│   ├── banks-linkedin/ ........... Banks LinkedIn (CANONICAL, 24 PNGs)
│   ├── court-filings/ ............ DaSean, Shayla, Banks filings
│   ├── photos/ ................... Date-organized photo evidence
│   ├── osint-screenshots/ ........ PCA/social media OSINT
│   ├── social-media/ ............. Smith family social media
│   ├── comms_aug2026/ ............ August communications
│   ├── admin-screenshots/ ........ Filing workflow screenshots
│   └── [other evidence subdirs]
│
├── 02-parenting/ .................. PARENTING DOCUMENTATION
│   ├── TIMELINE.md ............... Master parenting chronology
│   ├── PARENTING_JOURNAL.md ...... Active daily log
│   └── CUSTODY_CALENDAR.md ....... Day-by-day custody tracker
│
├── 03-housing/ .................... HOUSING
├── 04-school/ ..................... SCHOOL (Banks/PCA research)
├── 05-employment/ ................. EMPLOYMENT
├── 05-community/ .................. COMMUNITY
├── 06-life-build/ ................. LIFE-BUILD & FINANCIAL PLANNING
├── 08-lansingPride/ ............... SEPARATE INCIDENT (isolated)
├── 09-labor/ ...................... LABOR
├── 10-long-term/ .................. FUTURE PLANNING
│
├── records/ ....................... DOCUMENT WAREHOUSE (partial)
│
└── tools/ ......................... OSINT TOOLKIT
    └── osint/
        ├── runner.py .............. Main OSINT sweep runner
        ├── pacer_pull.py .......... PACER case tracking + pull guide
        ├── pacer_rename.py ........ PDF metadata extractor + renamer
        ├── smith_deep_dive.py ..... Smith family investigation module
        ├── sources/ ............... 17 OSINT source modules
        └── results/ ............... Raw sweep outputs (don't edit)
```

---

## Active Fronts (as of Sep 5, 2026)

| Front | Status | Next Action |
|-------|--------|------------|
| **Emergency custody** | Filed Sep 4, before Judge Triplett | Expect response Tue Sep 8 |
| **PPOs (5)** | Filed Sep 4 at Ingham County | Ex parte review Tue-Wed |
| **Kevin v. Smith** | Served Aug 27, answer due ~Sep 17 | Default if no answer |
| **Kevin v. Banks** | Amended complaint served Sep 2, answer due ~Sep 22 | Default if no answer |
| **Marquita BK fraud** | Trustee notified Sep 4 | Confirmation hearing Sep 14 |
| **Simone BK** | Schedules due Mon Sep 8 | Monitor PACER |
| **Subpoenas (20)** | Drafted, ready to mail | Wave 1 mailing Tue Sep 8 |
| **Banks OSINT** | ROD pulled, PACER searches pending | Weekend deep dive |

---

*Portfolio started: June 18, 2026*
*Last updated: September 5, 2026*
*Prepared by: Kevin Mok*
