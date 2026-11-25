# SCREENSHOTS FOLDER — Evidence Capture & Processing Pipeline
# September 16, 2026

## HOW TO USE THIS FOLDER

### Kevin's Workflow:
1. Take screenshot of search result
2. Save to the correct subfolder:
   - `statebar/` — State Bar of Michigan member searches
   - `lara/` — LARA entity/business searches
   - `pacer/` — PACER docket and case searches
   - `rod/` — Register of Deeds property searches
   - `campfin/` — Campaign finance (TransparencyUSA, MI SOS)
   - `courts/` — Court record searches (Wayne, Oakland, Ingham, etc.)
   - `linkedin/` — LinkedIn profile captures
   - `web/` — General website captures (school sites, news, etc.)

3. Name the file: `[DATABASE]_[TARGET]_[DATE].png`
   Examples:
   - `STATEBAR_SCHMIDTKE_SEP17.png`
   - `LARA_PURPOSE_GROUP_SEP17.png`
   - `PACER_TONESA_WELCH_SEP18.png`

4. **OPTIONAL but helpful:** Drop a quick note in `metadata/` with
   the same filename but `.md` extension:
   ```
   database: State Bar
   target: Brian Schmidtke
   result: FOUND — P12345, active
   ```

### Agent's Workflow:
1. Read screenshots from subfolders
2. Extract data → write to `01-case/research/banks/osint/[target].md`
3. Update `OSINT_MASTER_MATRIX_SEP16.md` status cells
4. Flag any findings that affect filings

### Priority Order (as of Sep 16):
🔴 BATCH 1 (today/tomorrow): State Bar verifications for bar complaints
🟡 BATCH 2 (Thu-Fri): PACER + LARA for federal packets
🟡 BATCH 3 (weekend): ROD + campaign finance deep pulls
⚪ BATCH 4 (ongoing): LinkedIn, news archives, background

---
*Matrix: 01-case/research/banks/OSINT_MASTER_MATRIX_SEP16.md*
*136 total scrape tasks across 15 databases*
