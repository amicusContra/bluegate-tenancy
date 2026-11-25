# OSINT MASTER MATRIX v3.0 — September 16, 2026
# Complete Rebuild: All names from book + Round 1-3 + new orgs
# Structured for systematic scraping (PACER, LARA, ROD, CampaignFin, State Bar, etc.)
#
# WORKFLOW: Screenshot → screenshots/ with metadata → agent processes
# FORMAT: Database × Target = status cell
# LEGEND: ✅ done | 🔄 partial | ❌ not started | N/A | ⏳ queued

---

## HOW THIS FILE WORKS

1. **Kevin screenshots** → dumps to `02-evidence/screenshots/` with
   filename convention: `[DATABASE]_[TARGET]_[DATE].png`
   Example: `LARA_BANKS_STRATEGY_SEP17.png`

2. **Agent reads screenshots** → extracts data → updates this matrix
   and writes detail files to `01-case/research/banks/osint/`

3. **Each cell** in the matrix below tracks: status + source file
   If ✅, the source file contains the extracted data.

4. **Priority** = filing dependency. 🔴 = needed for Friday filings.
   🟡 = needed for Monday federal packets. ⚪ = background/ongoing.

---

## SECTION 1: PEOPLE × DATABASES

### 1A. JUDGES (7 targets — all have JTC/Bar filings)

| # | Name | State Bar | LARA | PACER | ROD/Property | CampaignFin | Courts | LinkedIn | Book Ref | Priority |
|---|------|-----------|------|-------|-------------|-------------|--------|----------|----------|----------|
| J1 | **Denise Langford Morris** | ✅ P#34884, Active (JAMS) | ❌ | ❌ | ❌ Oakland County | ❌ 2010 SC campaign | ❌ Oakland County | ❌ JAMS profile ✅ | Ch.5 (origin) | 🔴 |
| J2 | **Vonda Evans** | ✅ Active, Southfield MI (Vonda's Law) | ❌ | ❌ | ❌ Wayne County | ❌ all campaigns | ❌ | ❌ | Ack+Ch.9+Ch.12 | 🔴 |
| J3 | **Cylenthia Miller** | 🔄 known active | ❌ entities? | ✅ prior | ❌ Flat Rock | 🔄 2026 campaign | ✅ 3 incidents | ✅ LinkedIn post | Ack+Ch.9+Ch.13 | 🔴 |
| J4 | **Tenisha Yancey** | ✅ active | ❌ | ✅ none | 🔄 Harper Woods | ✅ $15,750 Banks | ✅ COC residency | ❌ | Ch.13 childhood | 🔴 |
| J5 | **Aliyah Sabree** | ✅ active | ❌ | ✅ none | ❌ | ✅ $80K raised | ❌ | 🔄 | Ch.8 "Aliyah" BLSA | 🔴 |
| J6 | **Adam Sabree** | ✅ active | ✅ Woodward Prop | ✅ none | 🔄 | ❌ | ❌ | 🔄 | Father endorsed | ⚪ |
| J7 | **Sean Perkins** | ✅ active | ✅ SP Enterprises | ✅ none | 🔄 2 props from Treas | ✅ $0 campaign | ❌ tax lien | 🔄 | Brother Todd | ⚪ |
| J8 | **E. Lynise Bryant** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Ack (friend) | ⚪ |
| J9 | **Regina Thomas** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Ack (friend) | ⚪ |

**FRIDAY PRIORITY:** Verify bar status for J1 (Langford Morris) and J2 (Evans) — needed for bar complaints.

---

### 1B. ATTORNEYS (Active bar complaints — 10 targets)

| # | Name | Bar # / Status | LARA | PACER | CampaignFin | LinkedIn | Book Ref | Priority |
|---|------|---------------|------|-------|-------------|----------|----------|----------|
| A1 | **Todd Perkins** (P55623) | ✅ active | ✅ Perkins Law | ✅ **4 BKs** (not 3!) | ✅ $15K+ donated | ✅ | Client's book | 🔴 |
| A2 | **Lamar Moreland** (AAG) | ✅ active | ❌ | ❌ | ❌ | ❌ | NOT in book | ⚪ |
| A3 | **Gary Perlmuter** | ✅ active (1992) | ❌ agent search! | ❌ | ❌ | ❌ | Formed Purpose Group | 🟡 |
| A4 | **Brian Schmidtke, Esq.** | ✅ Active, Haslett MI | ❌ | ❌ | ❌ | ❌ | Ack p.4 (staff) | 🔴 |
| A5 | **Rebecca Fadel (King), J.D.** | ✅ P#57290 (inactive, now NC) | ❌ | ❌ | ❌ | ❌ | Ack p.4 (staff→Leg Dir) | 🔴 |
| A6 | **Kyle Giallonardo, J.D.** | ❌ NOT MI BAR (PA only) | ❌ | ❌ | ❌ | ❌ | Ack p.4 (MSU undergrad) | ⚪ |
| A7 | **Jillian Martin, Esq.** | ❌ NOT MI BAR (MD/DC/IL) | ❌ | ❌ | ❌ | ❌ | Ack+Ch.8+Ch.13 (classmate) | ⚪ |
| A8 | **Kristine Longstreet, Esq.** | ❌ VERIFY | ❌ | ❌ | ❌ | ❌ | Ack p.4 (friend) | ⚪ |
| A9 | **Dondré Ewing, Esq.** | ❌ VERIFY | ❌ | ❌ | ❌ | ❌ | Ack p.4 (law friend) | ⚪ |
| A10 | **Jehan Crump-Gibson** (P73178) | ✅ active | ✅ GLLG | ✅ none | ❌ | ✅ | Gala honored | ⚪ |
| A11 | **Brandi Neal** | ❌ VERIFY (cousin) | ❌ | ❌ | ❌ | ❌ | Ch.8 (cousin, Wayne Law) | ⚪ |
| A12 | **"Roeiah"** (last name unknown) | ❌ FIND | ❌ | ❌ | ❌ | ❌ | Ch.5 (intermediary) | ⚪ |

**FRIDAY PRIORITY:** State Bar directory search for A4-A7 (Schmidtke, Fadel, Giallonardo, Martin).

---

### 1C. BANKS INNER CIRCLE (6 targets)

| # | Name | PACER | LARA | ROD/Property | MDOC/OTIS | CampaignFin | LinkedIn | Book Ref | Priority |
|---|------|-------|------|-------------|-----------|-------------|----------|----------|----------|
| IC1 | **Brian Banks** | ✅ **3 BKs** (not 2!) — 97-45020 NEW | ✅ 5 entities | 🔄 Severn | N/A | ✅ $167K+ | ✅ | All chapters | 🟡 |
| IC2 | **Joseph Holland Jr** | ✅ 5 BKs + 2 Dinardo | ✅ | ❌ PULL Middlebelt+Newcastle | ✅ MDOC 443789 | ✅ PAC treas | ✅ | Ack+Ch.7+12+13 | 🟡 |
| IC3 | **Tonesa Welch (née Banks)** | ✅ BMF + 2 CA BKs + RE case | ❌ | ❌ | ❌ BOP? | ❌ | ❌ | Ch.2 "Toni"/BMF | 🟡 |
| IC4 | **Justin Banks** (brother) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Ch.12 (considered for HD-1) | ⚪ |
| IC5 | **Joyce Banks** (mother) | ❌ | ❌ | ❌ | ❌ | ❌ | N/A | Various | ⚪ |
| IC6 | **O.D. Banks** (grandfather, deceased) | N/A | ❌ | ❌ guardianship records | N/A | N/A | N/A | Ch.9 death | ⚪ |

**MONDAY PRIORITY:** IC3 (Tonesa Welch) PACER pull = federal packet evidence.

---

### 1D. POLITICIANS & GOVERNMENT OFFICIALS (12 targets)

| # | Name | PACER | LARA | CampaignFin | LinkedIn | Book Ref | Priority |
|---|------|-------|------|-------------|----------|----------|----------|
| P1 | **Thomas Stallworth IV** | ❌ | ❌ | ❌ FULL PULL | ❌ | Ack (mentor); Ch.12-13 | 🟡 |
| P2 | **Thomas Stallworth III** | ❌ | ❌ | ❌ FULL PULL | ❌ | Father of IV | 🟡 |
| P3 | **Eric Sabree** | ✅ **40+ cases** (Bowles class action, Fakhreddine active) | ✅ US Dev Svc | ✅ | 🔄 | Endorsed Banks+Miller | 🟡 |
| P4 | **Sherry Gay-Dagnogo** | ✅ | ✅ | ✅ $473K | ✅ | Ack+Ch.12+Ch.13 | ⚪ (known) |
| P5 | **Mike Duggan** | ❌ | ❌ | ❌ cross-ref Banks | ❌ | Ch.5 "the mayor" | 🟡 |
| P6 | **Warren Evans** (Co Exec) | ❌ | ❌ | ❌ | ❌ | Endorsed Banks+Miller | ⚪ |
| P7 | **Stephanie Chang** (Senator) | ❌ | ❌ | ❌ | ❌ | Endorsed Banks 2022 | ⚪ |
| P8 | **Jewel Ware** (Commissioner) | ❌ | ❌ | ❌ | ❌ | Ack (friend) | ⚪ |
| P9 | **Cathy Garrett** (Wayne Clerk) | ❌ | ❌ | ❌ | ❌ | Ack (friend) | ⚪ |
| P10 | **Karen Dumas** | ❌ | ✅ Images&Ideas | ❌ | ❌ | Ack (friend) | 🟡 |
| P11 | **Alexis Ramsey** (HP Schools) | ❌ | ❌ | ❌ | ❌ | Recommended Banks | ⚪ |
| P12 | **Tim Bowlin** (House CFO) | ❌ | ❌ | ❌ | ❌ | $0.44 cover | ⚪ |

---

### 1E. PCA/MacDowell BOARD & STAFF (8 targets)

| # | Name | PACER | LARA | CampaignFin | LinkedIn | Book Ref | Priority |
|---|------|-------|------|-------------|----------|----------|----------|
| B1 | **Devin Hutchings** | ❌ | ❌ DH Strategies | ✅ SuperPAC $37K ILG | ❌ | Ack+Ch.13 (first client) | 🟡 |
| B2 | **Kevin McKinney** | ❌ | ❌ | ❌ | ❌ | Ack+Ch.13 ("Devin and Kevin") | ⚪ |
| B3 | **Latisha Johnson** | ✅ none | ✅ MECCA Corp | ✅ ILG $850 | ✅ | Ack (friend) → Board Sec | ⚪ |
| B4 | **Major Clora** | ❌ | ❌ Clora Funeral | ❌ | ❌ | NOT in book | ⚪ |
| B5 | **Nicole Wells Stallworth** | ❌ | ❌ | ❌ | ❌ | Stallworth family | ⚪ |
| B6 | **Dr. Chalena Yancey Beasley** | ❌ | ❌ | ❌ | ❌ | Yancey's sister → PCA School Leader | ⚪ |
| B7 | **Martez Williams** (MacDowell VP) | ❌ | ❌ | ❌ | ❌ | "$5M contract management" | ⚪ |
| B8 | **Verkeydia Hall** (MacDowell Board) | ❌ | ✅ Hall Law PLLC | ❌ | ❌ | 615 Griswold = Perkins bldg | ⚪ |

---

### 1F. CAMPAIGN VENDORS & FINANCIAL NODES (7 targets)

| # | Name/Entity | PACER | LARA | CampaignFin | IRS/Tax | Book Ref | Priority |
|---|------------|-------|------|-------------|---------|----------|----------|
| V1 | **Inner Link Graphics / Larry Thomas Jr** | ✅ none | 🔄 blocked | ✅ $118K+ | ❌ | Not in book | 🟡 |
| V2 | **Gloria McCastle** | ❌ | ❌ | ✅ $20K+ payee | ❌ | Not in book | ⚪ |
| V3 | **Venus Coleman** | ❌ | ❌ | ✅ $7.3K payee | ❌ | Not in book | ⚪ |
| V4 | **Carles Whitlow / Nine Thirty Marketing** | ❌ | ❌ LARA search | ✅ $9.4K payee | ❌ | Ack p.4 (media team) | ⚪ |
| V5 | **Latania Lewis** | ❌ | ❌ | ✅ $9.5K payee | ❌ | Not in book | ⚪ |
| V6 | **DeShon Gale / DG Creative Studios** | ❌ | ❌ LARA search | ❌ | ❌ | Ack p.4 (cover designer) | ⚪ |
| V7 | **Tracey Ellis / Yecart Accounting** | ✅ | ✅ active LARA | ❌ | ❌ CPA license? | MacDowell bookkeeper | ⚪ |

---

### 1G. LAW SCHOOL / ACADEMIC (5 targets)

| # | Name | State Bar | LinkedIn | MSU Records | Book Ref | Priority |
|---|------|-----------|----------|------------|----------|----------|
| LS1 | **Dean Connell Alsup** | N/A (academic) | ❌ | ❌ | Ch.8 (hooded Banks) | ⚪ |
| LS2 | **Mary Ferguson** | N/A (admissions) | ❌ | ❌ | Ch.7 (LEO Program) | ⚪ |
| LS3 | **Roeiah** (last name unknown) | ❌ | ❌ | ❌ LEO Program list | Ch.5+7 (intermediary) | 🟡 |
| LS4 | **"Mr. Condino"** (defense atty) | ❌ VERIFY full name | ❌ | N/A | Ch.5 (felony defense) | 🟡 |
| LS5 | **Ben Gonek** (AG defense atty) | ❌ VERIFY | ❌ | N/A | Ch.12 (AG prosecution) | ⚪ |

---

### 1H. BMF CONNECTION (3 targets)

| # | Name | PACER | BOP | LARA | News | Book Ref | Priority |
|---|------|-------|-----|------|------|----------|----------|
| BMF1 | **Tonesa Welch (née Banks)** | ✅ BMF 05-80955 + CA 05-2208 + 2 CA BKs + RE suit 18-3334 | ❌ | ❌ | ✅ confirmed | Ch.2 "Toni" | 🟡 |
| BMF2 | **"T" (boyfriend)** | ❌ likely Terry Flenory | ❌ | N/A | ✅ BMF leaders | Ch.2 | ⚪ |
| BMF3 | **Tonesa Welch 2026 book** | N/A | N/A | N/A | ✅ "Black Mafia Queen" Kensington Publishing, w/ son H. Corey Mills (owns "BMF LLC") | Banks endorsed it | 🟡 |
| BMF4 | **Darry Price** | ❌ | ❌ | ❌ | ❌ | Co-defendant w/ Tonesa RE suit | 🟡 |
| BMF5 | **John Thomas Dinardo Jr.** | ✅ Holland adversary 18-48263 | ❌ | ❌ | ❌ | Holland sued him in BK | 🟡 |

---

### 1I. CREDENTIAL ENDORSERS (7 targets)

| # | Name/Org | Website | Wayback | Contact | Status | Priority |
|---|---------|---------|---------|---------|--------|----------|
| CE1 | **Pahara Institute** | ✅ captured | ❌ archive | ❌ | Active — Banks listed | 🔴 |
| CE2 | **NAPCS** | ✅ captured | ❌ archive | ❌ | Active — Banks speaker bio | 🔴 |
| CE3 | **Baker College** | 🔄 HuffPost+PowerVoter | ❌ archive | ❌ GC email | Adjunct history | 🔴 |
| CE4 | **Mike Morse Law Firm** | ✅ ep85 captured | ❌ archive | ❌ | Called Banks "attorney" | 🔴 |
| CE5 | **National Charter Collaborative** | ❌ capture | ❌ archive | ❌ | Cohort Three listing | ⚪ |
| CE6 | **Power Voter** | ✅ captured | ❌ archive | ❌ | Lists Banks as "Attorney" at Rodnick | ⚪ |
| CE7 | **Manati Fellow** | ❌ investigate | ❌ | ❌ | LinkedIn listing | ⚪ |

---

### 1J. SMITH FAMILY (Custody case — 4 targets)

| # | Name | PACER | Wayne Circuit | ROD/Property | LARA | NMLS | Priority |
|---|------|-------|-------------|-------------|------|------|----------|
| S1 | **Leon A. Smith** | ❌ | ❌ | ✅ 17370 Dresden | ❌ | N/A | ⚪ |
| S2 | **Marquita L. Smith** | ❌ | ❌ | ✅ Dresden co-owner | ❌ | N/A | ⚪ |
| S3 | **Shayla Smith** | ✅ | 🔄 | ❌ no property | ❌ | ✅ NMLS 2649162 | ⚪ |
| S4 | **Simone R. Smith** | ✅ BK 24-50543 | ❌ | ❌ | ❌ | N/A | ⚪ |

---

## SECTION 2: ENTITIES × DATABASES

### 2A. BANKS-CONTROLLED ENTITIES

| # | Entity | LARA ID | Type | Agent | Status | LARA Pull | IRS | CampaignFin | Priority |
|---|--------|---------|------|-------|--------|-----------|-----|-------------|----------|
| E1 | Banks Strategy & Consultants LLC | 802070120 | LLC | Banks | ❌ verify | ❌ filing history | N/A | ✅ $15.7K+ | ⚪ |
| E2 | Purpose Foundation | 803294855 | Nonprofit | Banks | ✅ Active (Dec 2024) | ❌ pull 4 directors | ✅ EIN 33-3537910, 501(c)(3) | N/A | 🟡 |
| E3 | The Purpose Group LLC | (formed 11/14/2024) | LLC/CMO | Banks | ✅ Active | ✅ website: thepurposegroupmichigan.com | N/A | N/A | 🟡 |
| E4 | Bank on Banks PAC | N/A | PAC | Banks | ❌ | N/A | N/A | ✅ $14.5K fines | 🟡 |
| E5 | The Right Turn Project | EIN 47-2441160 | Nonprofit | Banks | IRS Dissolved 2019 | ✅ At 21456 Newcastle (HOLLAND'S HOUSE!) | ✅ IRS dissolved, never filed with MI AG | N/A | 🔴 |
| E6 | MacDowell Preparatory Academy | (find ID) | Charter | Banks | ❌ | ❌ FIND | ❌ | N/A | 🟡 |
| E7 | Purpose Charter Academy | (find ID) | Charter | Banks | ❌ | ❌ FIND | ❌ | N/A | 🟡 |

### 2B. NETWORK ENTITIES

| # | Entity | LARA ID | Connection | LARA Pull | Priority |
|---|--------|---------|-----------|-----------|----------|
| E8 | Perkins Law Group PLLC | (find) | Todd Perkins — Banks' attorney | ❌ | ⚪ |
| E9 | Sean Perkins Enterprises LLC | (find) | Sean Perkins — judge | ❌ | ⚪ |
| E10 | The-Inner-Link LLC | (find) | Larry Thomas Jr — $118K vendor | ❌ | 🟡 |
| E11 | Woodward Property Group | (find) | Adam Sabree connection | ❌ | ⚪ |
| E12 | U.S. Development Services | (find) | Eric Sabree / Badriyyah | ✅ partial | ⚪ |
| E13 | Metro Property Group | (find) | Adam Sabree — in-house counsel | ❌ | ⚪ |
| E14 | MECCA Corp | (find) | Latisha Johnson | ❌ | ⚪ |
| E15 | Images & Ideas | (find) | Karen Dumas | ✅ | ⚪ |
| E16 | DH Strategies | (find) | Devin Hutchings | ❌ | ⚪ |
| E17 | Nine Thirty Marketing | (find) | Carles Whitlow | ❌ | ⚪ |
| E18 | DG Creative Studios | (find) | DeShon Gale | ❌ | ⚪ |
| E19 | Yecart Accounting Services | 801438906 | Tracey Ellis — MacDowell bookkeeper | ✅ | ⚪ |
| E20 | Verkeydia Hall Law PLLC | (find) | MacDowell Board — 615 Griswold | ✅ found | ⚪ |
| E21 | Great Lakes Legal Group PLLC | (find) | Crump-Gibson — ADB panelist | ✅ | ⚪ |
| E22 | Clora Funeral Home | (find) | Major Clora — PCA Board | ❌ | ⚪ |
| E23 | True Vine Publishing Co. | (find) | Banks' book publisher | ❌ | ⚪ |

---

## SECTION 3: PROPERTIES × ROD/ASSESSOR

| # | Address | Owner(s) | County | ROD Pull | Assessor | Mortgage | Priority |
|---|---------|----------|--------|----------|----------|----------|----------|
| PR1 | 1968 Severn Rd, GPW 48236 | Banks (+ Holland uses) | Wayne | ❌ deed chain | ❌ SEV/PRE | ❌ | ⚪ |
| PR2 | Holland Middlebelt property | Holland | Wayne | ❌ Lisa Cudworth tax payment | ❌ | ❌ | 🟡 |
| PR3 | Holland Newcastle JTWRS | Holland/Banks? | Wayne | ❌ | ❌ | ❌ | 🟡 |
| PR4 | Yancey Harper Woods address | Yancey | Wayne | ❌ | ❌ PRE status! | ❌ | ⚪ |
| PR5 | Yancey Detroit address | Yancey? | Wayne | ❌ | ❌ | ❌ | ⚪ |
| PR6 | Miller Flat Rock address | Miller | Monroe | ❌ | ❌ | ❌ | ⚪ |
| PR7 | 10101 E. Canfield (PCA bldg) | DPSCD? | Wayne | ❌ chain of title | ❌ | ❌ | 🟡 |
| PR8 | MacDowell school building | Unknown | Wayne | ❌ | ❌ | ❌ $719K balloon | 🟡 |
| PR9 | 17370 Dresden, Detroit | Leon/Marquita Smith | Wayne | ✅ | ✅ | ✅ Lake Trust $68K | ⚪ |
| PR10 | Sean Perkins 2 properties | Sean Perkins → SP Enterprises | Wayne | ❌ | ❌ | ❌ tax lien | ⚪ |

---

## SECTION 4: CAMPAIGN FINANCE CROSS-REFERENCE

### 4A. COMMITTEES TO PULL (TransparencyUSA / MI SOS)

| # | Committee | Principal | Status | Priority |
|---|-----------|-----------|--------|----------|
| CF1 | Banks for Senate | Brian Banks | ✅ pulled | ⚪ |
| CF2 | Bank on Banks PAC | Brian Banks | ✅ pulled | ⚪ |
| CF3 | Committee to Elect Tenisha Yancey | Yancey | ✅ pulled | ⚪ |
| CF4 | MI Deserves Better SuperPAC | Hutchings | ✅ pulled | ⚪ |
| CF5 | Strong Women Lead PAC | Dagnogo | ✅ pulled | ⚪ |
| CF6 | **Langford Morris 2010 SC campaign** | Langford Morris | ❌ PULL | 🔴 |
| CF7 | **Miller 2026 re-election** | Miller | ❌ PULL | 🟡 |
| CF8 | **Stallworth III all campaigns** | Stallworth | ❌ PULL | 🟡 |
| CF9 | **Stallworth IV all campaigns** | Stallworth | ❌ PULL | 🟡 |
| CF10 | **Duggan all campaigns** | Duggan | ❌ cross-ref only | 🟡 |
| CF11 | **Aliyah Sabree** | Sabree | ✅ $80K | ⚪ |
| CF12 | **Eric Sabree all campaigns** | Sabree | ❌ PULL | 🟡 |

### 4B. CROSS-REFERENCE: Shared Payees

| Payee | Banks Campaign | Yancey Campaign | Dagnogo Campaign | SuperPAC | Total | Status |
|-------|---------------|----------------|-----------------|----------|-------|--------|
| Inner Link Graphics | $39,315 | $30,200 | ❌ check | $37,151 | $118K+ | 🔄 |
| Gloria McCastle | $9,450 | ❌ check | ❌ check | ❌ | $20K+ | ❌ |
| Latania Lewis | $6,675 | ❌ check | ❌ check | ❌ | $9.5K+ | ❌ |
| Venus Coleman | $7,350 | ❌ check | ❌ check | ❌ | $7.3K+ | ❌ |
| Carles Whitlow | $8,500 | ❌ check | ❌ check | ❌ | $9.4K+ | ❌ |

**TASK:** Cross-reference EVERY payee across ALL network committees to find the full closed-loop.

---

## SECTION 5: FEDERAL DATABASES

| # | Database | Target | Case/ID | Status | Priority |
|---|----------|--------|---------|--------|----------|
| F1 | PACER — BMF | Tonesa Welch | 2:05-cr-80955 (D-22) + CA 05-2208 | ✅ LOCATED | 🔴 pull docket |
| F2 | PACER — Holland BK3 | Joseph Holland | 09-46072 | ✅ LOCATED | 🔴 pull Schedule A/B |
| F3 | PACER — Holland BK4 | Joseph Holland | 14-46410 | ✅ LOCATED | 🔴 pull Schedule A/B |
| F4 | PACER — Holland BK5 | Joseph Holland | 14-51632 | ✅ LOCATED | 🔴 pull Schedule A/B |
| F5 | PACER — Bryant v Miller | Miller | 2:26-cv-10917 | ✅ docket | ⚪ |
| F6 | PACER — Ian Watts BK | Watts | 21-40794 | ❌ schedules | ⚪ |
| F7 | BOP Inmate Locator | Tonesa Welch | ✅ BOP #32373-112, released ~2012 | ✅ DONE | ⚪ |
| F8 | IRS TEOS | Purpose Foundation | ✅ EIN 33-3537910, 501(c)(3) active | ✅ DONE | ⚪ |
| F9 | IRS TEOS | Right Turn Project | ✅ EIN 47-2441160, dissolved 2019 | ✅ DONE | ⚪ |
| F10 | SBA EIDL | Banks | (FOIA) | 🔄 $1K advance found | ⚪ |
| F11 | **PACER — Banks BK #0** | **Brian Banks** | **97-45020** | ✅ LOCATED | 🔴 **NEW — 3rd BK!** |
| F12 | ~~PACER — Derenobe v Banks~~ | ~~Banks~~ | ~~25-2031~~ | ❌ FALSE POSITIVE | ~~ELIMINATED~~ (different Brian A. Banks, Gagetown MI) |
| F13 | **PACER — Holland v Dinardo** | **Holland (plaintiff)** | **18-4413** | ✅ LOCATED | 🟡 who is Dinardo? |
| F14 | **PACER — Tonesa CA BK#1** | **Tonesa Welch** | **08-16922 (cacbk)** | ✅ LOCATED | 🟡 post-BMF assets |
| F15 | **PACER — Tonesa CA BK#2** | **Tonesa Welch** | **09-13518 (cacbk)** | ✅ LOCATED | 🟡 post-BMF assets |
| F16 | **PACER — Tonesa RE suit** | **Tonesa Welch** | **18-3334 (cacdc)** | ✅ LOCATED | 🟡 RE activity post-prison |
| F17 | **PACER — Perkins BK #3** | **Todd Perkins** | **14-44292** | ✅ LOCATED | 🟡 **4th BK discovered** |
| F18 | **PACER — Holland BK1** | **Joseph Holland** | **05-81655** | ✅ LOCATED | ⚪ pre-Newcastle |
| F19 | **PACER — Holland BK2** | **Joseph Holland** | **08-65982** | ✅ LOCATED | 🟡 1st post-Newcastle |
| F20 | **PACER — Bowles v Sabree** | **Eric Sabree** | **23-10973** | ✅ LOCATED | 🟡 class action |
| F21 | **PACER — Belle v Wayne** | **Eric Sabree** | **26-11509** | ✅ LOCATED | 🟡 May 2026 filing |

---

## SECTION 6: STATE DATABASES

| # | Database | Target | Status | Priority |
|---|----------|--------|--------|----------|
| ST1 | MI SOS — Candidate filings | Banks 2012, 2014, 2018, 2022 | ❌ need addresses | 🟡 |
| ST2 | MI SOS — Bureau of Elections | Bank on Banks PAC referral | ❌ | ⚪ |
| ST3 | MDE Educator Lookup | Banks cert AD0000048782 | 🔄 known | ⚪ |
| ST4 | MDOC OTIS | Holland #443789 | ✅ | ⚪ |
| ST5 | LARA Professional License | Tracey Ellis CPA? | ❌ | ⚪ |
| ST6 | MI AG Charitable Trust | Purpose Foundation | ❌ | 🟡 |
| ST7 | ICHAT | Banks full criminal history | ❌ (paid/$10) | ⚪ |
| ST8 | Oakland County Court | Banks ~1999 case + Condino | ❌ | 🟡 |

---

## SECTION 7: SCRAPING PRIORITY QUEUE

### BATCH 1 — TODAY Sep 17 (Filing Dependencies)
```
🔴 State Bar directory: Schmidtke, Fadel, Giallonardo, Martin
🔴 State Bar directory: Langford Morris (active?)
🔴 State Bar directory: Vonda Evans (active?)
🔴 TransparencyUSA: Langford Morris 2010 SC campaign
🔴 Wayback Machine: Archive ALL credential URLs before letter
✅ PACER Party Search: Holland, Banks, Sabree, Welch, Perkins — DONE Sep 17
```

### BATCH 2 — THURSDAY-FRIDAY Sep 18-19 (Federal Packet Prep — PACER DOCUMENT PULLS)
```
🔴 PACER PULL: Holland BK Schedule A/B — 09-46072 (Newcastle/Middlebelt?)
🔴 PACER PULL: Holland BK Schedule A/B — 14-46410 (filed from prison)
🔴 PACER PULL: Holland BK Schedule A/B — 14-51632 (filed from prison)
🔴 PACER PULL: Banks BK — 97-45020 (NEWLY DISCOVERED 3rd BK)
🔴 PACER PULL: Derenobe v Banks — 25-2031 (ACTIVE adversary — who is suing Banks?)
🔴 PACER PULL: BMF docket — 05-80955 (Tonesa Welch sentencing docs)
🟡 PACER PULL: Holland BK — 08-65982 (1st post-Newcastle BK)
🟡 PACER PULL: Perkins BK — 14-44292 (NEWLY DISCOVERED 4th BK)
🟡 PACER PULL: Perkins BK — 22-45209 (BK during Banks representation)
🟡 PACER PULL: Tonesa RE case — 18-3334 (post-prison real estate activity)
🟡 PACER PULL: Holland v Dinardo — 18-4413 (who is Dinardo?)
🟡 LARA: Purpose Group LLC (find ID + pull)
🟡 LARA: Perlmuter agent search (all entities he organized)
🟡 LARA: Right Turn Project (dissolved — get filing history)
🟡 LARA: Opportunities For All Michigan
🟡 IRS TEOS: Purpose Foundation + Right Turn Project + 87-2342269
🟡 BOP Inmate Locator: Tonesa Welch (released? supervised release?)
```

### BATCH 3 — WEEKEND Sep 20-21 (Deep Investigation + Federal Packet Assembly)
```
🟡 TransparencyUSA: Stallworth III + IV all campaigns
🟡 TransparencyUSA: Eric Sabree all campaigns
🟡 TransparencyUSA: Miller 2026 re-election
🟡 TransparencyUSA: Cross-ref all payees across committees
🟡 Wayne ROD: Holland Middlebelt + Newcastle (current status)
🟡 Wayne ROD: Lisa Cudworth — any other properties?
🟡 Wayne ROD: SABREE all variants (900+ target)
🟡 Wayne ROD: 10101 E. Canfield (PCA building chain of title)
🟡 Wayne ROD: MacDowell building
🟡 Oakland County: Banks ~1999 case number
🟡 MI SOS: Banks candidate filing addresses (all races)
🟡 LARA: All 23 entities in Section 2B
🟡 PACER PULL: Bowles v Sabree — 23-10973 (class action complaint)
🟡 PACER PULL: Belle v Wayne — 26-11509 (May 2026 class action)
```

### BATCH 4 — ONGOING (Background)
```
⚪ LinkedIn: All new book names (Schmidtke, Fadel, etc.)
⚪ LARA: Nine Thirty Marketing, DG Creative Studios
⚪ PACER: Ian Watts BK schedules
⚪ PACER: Tonesa Welch CA BKs (08-16922, 09-13518) — asset concealment?
⚪ News archives: Langford Morris, Evans, Stallworth
⚪ BoardDocs: DPSCD July 2025 PCA vote
⚪ MacDowell budgets: Download all public docs
⚪ OSINT: John Thomas Dinardo Jr. — Holland adversary
⚪ OSINT: "Derenobe" — who is suing Banks in 25-2031?
⚪ OSINT: Darry Price — co-defendant with Tonesa in RE case
⚪ OSINT: Tonya Bowles — 5+ years fighting Sabree (potential ally?)
⚪ OSINT: Fadi Fakhreddine — active 6th Cir appellant vs Sabree
```

---

## SECTION 8: SCREENSHOT PROTOCOL

### Filename Convention
```
[DATABASE]_[TARGET_SHORTNAME]_[DATE].png
```

### Examples
```
STATEBAR_SCHMIDTKE_SEP17.png
STATEBAR_FADEL_SEP17.png
LARA_PURPOSE_GROUP_SEP17.png
PACER_TONESA_WELCH_SEP18.png
TRANSUSA_LANGFORD_MORRIS_2010_SEP17.png
ROD_HOLLAND_MIDDLEBELT_SEP19.png
```

### Metadata File
For each screenshot, create a companion `.md` file:
```
STATEBAR_SCHMIDTKE_SEP17.md
---
database: State Bar of Michigan
target: Brian Schmidtke
search_term: "Brian Schmidtke"
url: member.michbar.org
date: 2026-09-17
result: [FOUND/NOT_FOUND/PARTIAL]
p_number: [if found]
status: [active/inactive/suspended]
notes: [any additional context]
---
```

### Folder Structure
```
02-evidence/
  screenshots/
    statebar/       ← State Bar searches
    lara/           ← LARA entity searches
    pacer/          ← PACER docket pulls
    rod/            ← Register of Deeds
    campfin/        ← Campaign finance
    courts/         ← Court record searches
    linkedin/       ← LinkedIn profiles
    web/            ← Website captures
    metadata/       ← .md companion files for all screenshots
```

---

## SECTION 9: TOTALS

| Category | Targets | Done | Partial | Not Started |
|----------|---------|------|---------|-------------|
| Judges (1A) | 9 | 0 | 4 | 5 |
| Attorneys (1B) | 12 | 3 | 1 | 8 |
| Inner Circle (1C) | 6 | 2 | 3 | 1 |
| Politicians (1D) | 12 | 3 | 2 | 7 |
| Board/Staff (1E) | 8 | 1 | 0 | 7 |
| Vendors (1F) | 7 | 2 | 1 | 4 |
| Law School (1G) | 5 | 0 | 0 | 5 |
| BMF (1H) | 5 (+2) | 1 | 1 | 3 |
| Endorsers (1I) | 7 | 4 | 1 | 2 |
| Smith Family (1J) | 4 | 2 | 1 | 1 |
| Entities (2A+2B) | 23 | 3 | 3 | 17 |
| Properties (3) | 10 | 1 | 2 | 7 |
| Campaign Finance (4A) | 12 | 5 | 0 | 7 |
| Federal DBs (5) | **21** (+11) | **13** | 1 | **7** |
| State DBs (6) | 8 | 2 | 1 | 5 |
| **TOTAL** | **149 scrape tasks** | **55** (+13) | **18** | **76** |

### Sep 17 PACER Search Updates:
- **+11 new PACER cases located** (need document pulls)
- **Banks: 3 BKs** (was 2) — new 97-45020 discovered
- **Perkins: 4 BKs** (was 3) — new 14-44292 discovered  
- **Tonesa Welch: 5 federal cases** (BMF MI + BMF CA + 2 CA BKs + RE suit)
- **Sabree: 40+ cases** — massive litigation footprint mapped
- **Holland: 7 MIEB cases** (5 BKs + 2 Dinardo adversary)
- **New names: Dinardo, Derenobe, Darry Price, Tonya Bowles, Fakhreddine**
- Full sorted analysis: `SUBGRAPH_PACER_INTELLIGENCE_SEP17.md`

---

## AGENTIC HANDOFF NOTES

When this gets too large for manual tracking:

1. **Each batch** becomes a Task with subagent_type: generalPurpose
2. **WebSearch** handles TransparencyUSA, Ballotpedia, news archives
3. **Browser** handles LARA portal, BSA Online, BoardDocs (JS-heavy)
4. **Kevin screenshots** PACER (paywalled), ROD (some paywalled), State Bar
5. **Agent processes** screenshots from `02-evidence/screenshots/`
6. **Detail files** go to `01-case/research/banks/osint/[target].md`
7. **This matrix** gets updated after every batch

---

*Kevin Mok — September 16, 2026*
*136 total scrape tasks across 15 databases*
*"We don't guess. We verify."*
