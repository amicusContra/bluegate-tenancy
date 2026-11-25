# OSINT TOOLKIT — README
## Last Updated: September 7, 2026

---

## QUICK START

```powershell
cd c:\Users\mokke\jobHunt\bluegate-tenancy\tools\osint
```

### 1. PACER API (Federal Court Records)

```powershell
# Re-authenticate (token expires every ~4 hours)
python pacer_reauth.py

# Targeted party search (saves results to results/pacer/)
python pacer_reauth.py
# Edit the `searches` list in pacer_reauth.py for new targets

# Follow-up searches (Marquita, Leon, etc.)
python pacer_followup.py
# Edit the `searches` list for new targets

# Full RICO batch search (preconfigured targets)
python pacer_api.py batch

# Show cost tracking
python pacer_api.py costs

# Show search queue
python pacer_api.py queue
```

**Credentials:** `.pacer_creds.json` (username: ecoPrimal)
**Token:** `.pacer_token.json` (auto-refreshed by scripts)
**Cost limit:** $30/quarter free tier
**Results:** `results/pacer/`

### 2. Web Capture (Manual via Agent)

Web captures are done by the AI agent using `WebSearch` and `WebFetch` tools.
Results are saved as markdown files in:
```
02-evidence/web-captures/
```

**Naming convention:** `SOURCE_SUBJECT_DETAIL.md`
Examples:
- `IRS_LOVELIFE_EIN_043682556.md`
- `TRANSPARENCYUSA_INNER_LINK_GRAPHICS.md`
- `FREEP_BANKS_EXPOSE_JULY2022.md`

### 3. OSINT Runner (Multi-Source)

```powershell
python runner.py
```

Configured via `targets.json` and `config.py`. Sources:
- `sources/campaign_finance.py` — TransparencyUSA
- `sources/courtlistener.py` — CourtListener (federal/state cases)
- `sources/irs_teos.py` — IRS exempt org search
- `sources/lara.py` — MI LARA entity search (⚠️ SSL issues)
- `sources/opencorporates.py` — OpenCorporates
- `sources/propublica.py` — ProPublica nonprofit explorer
- `sources/state_bar.py` — MI State Bar attorney lookup
- `sources/web_search.py` — General web search

### 4. Document Processing

```powershell
# Extract text from PDF documents
python doc_extract.py <path_to_pdf>

# Rename PACER downloaded docs
python pacer_rename.py
```

---

## CAPTURED DATA LOCATIONS

| Folder | Contents |
|--------|----------|
| `02-evidence/web-captures/` | Agent-captured web intelligence (MD files) |
| `02-evidence/wayne-rod-sep2/` | Wayne County ROD documents (PDF batches) |
| `02-evidence/pacer-docs/` | PACER downloaded court documents |
| `tools/osint/results/pacer/` | PACER API search results |
| `tools/osint/results/MASTER/` | Consolidated OSINT sweep results |

---

## API KEYS & CREDENTIALS

| Service | Status | Location |
|---------|--------|----------|
| PACER | ✅ Active | `.pacer_creds.json` |
| Google Maps API | ❌ Need key | — |
| LARA API | ⚠️ SSL blocked | Use browser instead |
| CourtListener | ✅ Free tier (no key) | — |
| TransparencyUSA | ✅ Public (no key) | — |
| IRS TEOS | ✅ Public (no key) | — |
| OpenCorporates | ✅ Free tier | — |
| Macomb ROD | ❌ Portal login needed | — |
| BS&A Online (Detroit Assessor) | ✅ No account needed | bsaonline.com |

---

## SCRIPTS INVENTORY

| Script | Purpose | Status |
|--------|---------|--------|
| `pacer_api.py` | Main PACER client (auth, search, batch, costs) | ✅ Working |
| `pacer_reauth.py` | Quick re-auth + targeted searches | ✅ Working |
| `pacer_followup.py` | Follow-up searches (Marquita, Leon, etc.) | ✅ Working |
| `pacer_family_tree_search.py` | Family tree expansion searches | ✅ Working |
| `smith_deep_dive.py` | Deep dive on Smith family | ✅ Working |
| `quick_search.py` | Quick one-off PACER search | ✅ Working |
| `docket_lookup.py` | Docket detail lookup | ✅ Working |
| `pacer_pull.py` | Document download from PACER | ⚠️ Needs CM/ECF |
| `doc_extract.py` | PDF text extraction | ✅ Working |
| `pacer_rename.py` | Rename downloaded PACER docs | ✅ Working |
| `runner.py` | Multi-source OSINT runner | ✅ Working |
| `config.py` | Configuration | ✅ Working |
| `models.py` | Data models | ✅ Working |
| `targets.json` | Search targets | ✅ Working |

---

## WHAT REQUIRES USER ACTION

| Task | Why | Tool |
|------|-----|------|
| LARA entity search | SSL/TLS blocks programmatic access | Browser portal |
| Macomb ROD documents | Requires portal login | Browser portal |
| PACER doc downloads | CM/ECF requires browser auth | PACER website |
| Detroit property records | BS&A may need specific format | BS&A Online |
| Google Maps distance | Needs API key or screenshot | Browser/Maps |

---

## COST TRACKING

PACER charges $0.10 per search results page.
Free if quarterly total < $30 for individual filers.
Run `python pacer_api.py costs` to check balance.
