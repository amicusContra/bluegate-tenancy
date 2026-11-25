# NETWORK GRAPH DATA — Topology Analysis
## Started September 5, 2026 | LinkedIn Scrub + Public Records
## Format: Nodes, Edges, Weights for graph visualization

---

## TARGET LIST — LinkedIn Scrub Queue

### Batch 1: Banks Inner Circle
| # | Name | LinkedIn Search Term | Priority |
|---|------|---------------------|----------|
| 1 | Brian Roderick Banks | "Brian Banks" Detroit Michigan charter school | HIGH |
| 2 | Joseph Holland Jr. | "Joseph Holland" Detroit Michigan | HIGH |
| 3 | Tracey D. Ellis | "Tracey Ellis" Yecart Accounting Detroit | HIGH |
| 4 | Todd J. Perkins | "Todd Perkins" attorney Inkster Michigan | HIGH |
| 5 | Gary Perlmuter | "Gary Perlmuter" attorney Farmington Hills | HIGH |

### Batch 2: Judges + PCA Board
| # | Name | LinkedIn Search Term | Priority |
|---|------|---------------------|----------|
| 6 | Cylenthia LaToye Miller | "Cylenthia Miller" judge Detroit Wayne County | HIGH |
| 7 | Tenisha R. Yancey | "Tenisha Yancey" judge Detroit 36th District | HIGH |
| 8 | Lamar Moreland | "Lamar Moreland" attorney general Michigan | HIGH |
| 9 | Latisha Johnson | "Latisha Johnson" Detroit City Council | MEDIUM |
| 10 | Devin Hutchings | "Devin Hutchings" DH Strategies Detroit | MEDIUM |
| 11 | Major Clora | "Major Clora" Clora Funeral Home Detroit | MEDIUM |
| 12 | Sherry Gay-Dagnogo | "Sherry Gay-Dagnogo" Detroit ombudsman | HIGH |

### Batch 3: Wayne County Officials + Extended
| # | Name | LinkedIn Search Term | Priority |
|---|------|---------------------|----------|
| 13 | Eric R. Sabree | "Eric Sabree" Wayne County Treasurer | HIGH |
| 14 | Warren C. Evans | "Warren Evans" Wayne County Executive | MEDIUM |
| 15 | Adam Sabree | "Adam Sabree" judge Detroit 36th District | HIGH |
| 16 | Aliyah Sabree | "Aliyah Sabree" judge Detroit 3rd Circuit | HIGH |
| 17 | Nicole Wells Stallworth | "Nicole Wells Stallworth" MacDowell Detroit | MEDIUM |
| 18 | Tunezha Crowder | "Tunezha Crowder" LCSW Michigan | MEDIUM |
| 19 | Gloria McCastle | "Gloria McCastle" Detroit Michigan | LOW |
| 20 | Latania Lewis | "Latania Lewis" Inner Link Graphics Detroit | LOW |

---

## NODE DEFINITIONS (for graph)

### Node Schema
```json
{
  "id": "string (unique)",
  "label": "string (display name)",
  "type": "person | entity | institution | case",
  "group": "banks_inner | judges | pca_board | wayne_officials | smith_household | financial | allied",
  "attributes": {
    "linkedin_url": "string | null",
    "title": "string (current position)",
    "education": ["string"],
    "location": "string",
    "bar_number": "string | null",
    "criminal_record": "boolean",
    "bankruptcy_count": "number",
    "public_office": "boolean",
    "confirmed": "boolean"
  }
}
```

### Edge Schema
```json
{
  "source": "node_id",
  "target": "node_id",
  "type": "employment | board | financial | legal | political | family | property | campaign | education | social",
  "weight": "1-10 (strength of connection)",
  "evidence": "string (source document)",
  "attributes": {
    "direction": "directed | undirected",
    "active": "boolean",
    "dollar_amount": "number | null",
    "date_range": "string",
    "description": "string"
  }
}
```

---

## KNOWN EDGES (Pre-LinkedIn — from existing OSINT)

### Employment / Board Relationships
| Source | Target | Type | Weight | Evidence |
|--------|--------|------|--------|----------|
| Banks | PCA | employment (superintendent) | 10 | DPSCD charter |
| Banks | MacDowell | employment (CAO) | 10 | MacDowell website |
| Banks | Purpose Group | ownership (RA) | 10 | LARA 803295082 |
| Banks | Purpose Foundation | board (President) | 10 | LARA |
| Banks | Banks Strategy | ownership (RA) | 10 | LARA 802070120 |
| Holland | Purpose Foundation | board (Secretary) | 9 | LARA |
| Holland | Banks Strategy | board (PAC Treasurer) | 8 | TransparencyUSA |
| Ellis | Purpose Foundation | board (CFO/Treasurer) | 9 | LARA |
| Ellis | Yecart Accounting | ownership (President) | 10 | LARA 801438906 |
| Miller | PCA | board (Chair) | 10 | keepjudgemiller.com |
| Yancey | MacDowell | board (Chair) | 10 | MacDowell website |
| Stallworth | MacDowell | board (Co-Chair) | 8 | MacDowell website |
| Moreland | PCA | board (Vice Chair) | 9 | Chalkbeat |
| L. Johnson | PCA | board (Secretary) | 8 | PCA materials |
| Hutchings | PCA | board (Treasurer) | 8 | PCA materials |
| Clora | PCA | board (Asst. Treasurer) | 7 | PCA materials |
| Gay-Dagnogo | PCA | development team | 8 | Chalkbeat |
| Gay-Dagnogo | DPSCD | board (voted to approve PCA) | 9 | DPSCD records |

### Legal Relationships
| Source | Target | Type | Weight | Evidence |
|--------|--------|------|--------|----------|
| Perkins | Banks | legal (represented) | 9 | Entity filings |
| Perkins | Miller | legal (represented — gun case) | 10 | Detroit News |
| Perkins | Evans defense | legal (Darnell Earley — Flint) | 7 | News archives |
| Perlmuter | Banks | legal (entity organizer) | 7 | LARA filings |

### Financial Relationships
| Source | Target | Type | Weight | Evidence |
|--------|--------|------|--------|----------|
| Yancey campaign | Banks Strategy | campaign payment ($15,750) | 10 | TransparencyUSA |
| Banks | PSCU | mortgage ($232K + $93.7K HELOC) | 8 | ROD |
| Yancey | PSCU | mortgage ($241K condo) | 7 | ROD |
| Holland | Banks (Severn) | property (QCD Newcastle→Banks 2007) | 8 | ROD |
| Banks | Holland (trust) | property (1st successor) | 9 | Trust doc |

### Political Relationships
| Source | Target | Type | Weight | Evidence |
|--------|--------|------|--------|----------|
| Banks | Yancey | political (predecessor in House Dist 1) | 10 | Wikipedia |
| Banks | Yancey | political (campaigned for her) | 9 | Wikipedia |
| Sabree | Banks | political (endorsed 2022 Commission bid) | 8 | Elrick |
| Sabree | Miller | political (endorsed re-election) | 8 | keepjudgemiller.com |
| Evans | Banks | political (endorsed 2022 Commission bid) | 7 | Elrick |
| Evans | Miller | political (endorsed re-election) | 7 | keepjudgemiller.com |
| Gay-Dagnogo | MI House Dist 8 | political (served 2015-2020) | 6 | Ballotpedia |
| Gay-Dagnogo | Detroit Ombudsman | political (appointed Sep 2025) | 8 | News |
| L. Johnson | Detroit City Council | political (current member) | 8 | City records |
| Moreland | MI Attorney General | employment (Asst. AG) | 9 | AG office |

### Family Relationships
| Source | Target | Type | Weight | Evidence |
|--------|--------|------|--------|----------|
| Eric Sabree | Adam Sabree | family (father-son) | 10 | Confirmed |
| Eric Sabree | Aliyah Sabree | family (father-daughter) | 10 | Confirmed |
| Banks | Justin Banks | family (brothers) | 10 | Confirmed |
| Aliyah Sabree | Miller | colleague (same 3rd Circuit bench) | 7 | Court records |
| Adam Sabree | Yancey | colleague (same 36th District bench) | 7 | Court records |

### Institutional Overlap
| Source | Target | Type | Weight | Evidence |
|--------|--------|------|--------|----------|
| Sabree (Treasurer) | Banks (Severn deed) | institutional (certified deed) | 8 | ROD |
| Sabree (Treasurer) | Miller (redemptions) | institutional (signed tax actions) | 7 | ROD |
| Sabree (Treasurer) | Yancey (forfeiture + cert) | institutional (signed tax actions) | 8 | ROD |
| Evans (Executive) | Yancey (mortgage discharge) | institutional (via Melba Fields) | 6 | ROD |

---

## LINKEDIN PROFILE DATA (to be populated)

### Template per person:
```
## [NAME] — LinkedIn Profile
- **URL:** 
- **Headline:** 
- **Location:** 
- **Current position(s):**
- **Education:**
- **Previous positions:**
- **Connections count:**
- **Notable connections visible:**
- **Endorsements/skills:**
- **Posts/activity:**
- **Groups:**
- **Screenshot saved:** [path]
- **Scrub date:**
```

---

## ⚠️ NEW NODES FROM FACEBOOK CAPTURES — September 8, 2026

### Batch 5: Facebook-Captured Connections (Sep 8)
| # | Name | Platform | Role | Evidence | Priority |
|---|------|----------|------|----------|----------|
| 30 | Ian Watts | Facebook | Banks' COUSIN | IMG_5888 | HIGH |
| 31 | Chalcee Norwood | Facebook | Dean of Ops, MacDowell + PCA | IMG_5891 | MEDIUM |
| 32 | Robin Gamble | Facebook | PCA photographer/documentarian | IMG_5889 | LOW |
| 33 | Officer R. Turner | Photo (DPD S-714) | At PCA event | IMG_5871 | MEDIUM |
| 34 | Mary Waters | Facebook | Council At-Large, promoted PCA | IMG_5890 | MEDIUM |
| 35 | Terrence Bradford Tarver | Facebook | UNCF Dir Public Policy | IMG_5913-14 | LOW |
| 36 | Karen Dumas | Facebook (verified, 18K) | PR, former Kilpatrick comms | IMG_5897-98 | MEDIUM |
| 37 | Shawny DeBerry | Facebook | Social circle, gala | IMG_5910 | LOW |
| 38 | Jared Fleischer | Gala invitation | CEO Rocket Companies, honoree | IMG_5911-12 | HIGH |
| 39 | Jehan Crump-Gibson | Gala invitation | Great Lakes Legal, honoree | IMG_5911-12 | MEDIUM |
| 40 | Bishop J. Drew Sheard | Event flyer | Greater Emmanuel COGIC pastor | IMG_5873 | LOW |

### NEW EDGES (Sep 8 Facebook captures)
| From | To | Type | Weight | Evidence |
|------|----|------|--------|----------|
| Banks | Ian Watts | BLOOD (cousin) | 10 | IMG_5888 |
| Banks | Chalcee Norwood | EMPLOYMENT (both schools) | 8 | IMG_5891 |
| Banks | Robin Gamble | VENDOR (photographer) | 4 | IMG_5889 |
| Banks | Karen Dumas | POLITICAL (PR endorsement) | 5 | IMG_5897 |
| Banks | Latisha Johnson | POLITICAL (council venue) | 6 | IMG_5915-16 |
| Banks | Mary Waters | POLITICAL (council promo) | 5 | IMG_5890 |
| Banks | Terrence Bradford Tarver | POLITICAL (UNCF/federal) | 4 | IMG_5913 |
| Banks | Jared Fleischer | FINANCIAL (Rocket sponsor) | 7 | IMG_5911 |
| Banks | Jehan Crump-Gibson | LEGAL (gala honoree) | 5 | IMG_5911 |
| Banks | Bishop Sheard | FAITH (fundraiser host) | 5 | IMG_5873 |
| Banks | Sherry Gay-Dagnogo | POLITICAL+FINANCIAL (strengthened) | 9 | IMG_5901-04 |
| Banks | Corletta Vaughn | INSTITUTIONAL (strengthened) | 9 | IMG_5850-56 |
| Shayla Smith (family) | Rocket Companies | EMPLOYMENT (7yr, 2015-22) | 7 | LinkedIn/NMLS |
| Jared Fleischer | Rocket Companies | LEADERSHIP (CEO) | 10 | IMG_5911 |
| Dagnogo | Todd Perkins | FINANCIAL ($500 PAC donation) | 6 | TransparencyUSA |

### NEW EDGES FROM MILLER FACEBOOK DUMP #2 (Sep 8 6:44 PM)
| From | To | Type | Weight | Evidence |
|------|----|------|--------|----------|
| Miller | Aliyah Sabree | SOCIAL ("Love and hugs") | 8 | IMG_5930 (May 17, 2025 — comments OFF) |
| Miller | Tenisha Yancey | PROFESSIONAL (ABJM retreat) | 9 | IMG_5926 (Apr 22, 2026 — "President Yancey") |
| Miller | William McConico | SOCIAL (congratulated) | 6 | IMG_5928 (Nov 23, 2025 — 36th Dist Chief Judge) |
| Miller | Edward Ewell | SOCIAL (congratulated) | 5 | IMG_5929 (Nov 23, 2025 — 3rd Circuit Chief Judge) |
| Miller | Helal Farhat | SOCIAL (congratulated) | 7 | IMG_5929 (Family Div Presiding Judge) |
| Miller | Marcus Williams | SOCIAL ("dear friend") | 5 | IMG_5924 (Jun 3, 2026) |
| Miller | TL Summerville | SOCIAL ("dear friend") | 5 | IMG_5924 (Jun 3, 2026) |
| Miller | Cedric McDougle | SOCIAL ("BFF/Brother") | 7 | IMG_5925 (Apr 27, 2026) |
| Miller | Mikal Ansari | SOCIAL ("BFF/Brother") | 7 | IMG_5925 (Apr 27, 2026) |
| Yancey | ABJM | LEADERSHIP (President) | 10 | IMG_5926 |
| Miller | Wolverine Bar Assoc | LEADERSHIP (Past President) | 8 | IMG_5925 |
| Nicole Wells Stallworth | MacDowell | GOVERNANCE + ADVOCACY | 7 | IMG_5920 (Gala in Pittsburgh 2023) |
| Principal Kafele | Banks/MacDowell | ENDORSEMENT (national figure) | 5 | IMG_5918 (65K followers) |
| Stacey D'Angelo Faulkner | MacDowell | VENDOR (branded merch) | 4 | IMG_5921 |

### UPDATED NODE THREAT CLASSIFICATION (Sep 8)
```
TIER 1 — CRIME FAMILY (institutional infrastructure):
  Eric R. Sabree — Wayne County Treasurer
  Aliyah Sabree — 3rd Circuit Judge
  Adam Sabree — 36th District Judge
  Badriyyah Sabree — Property buyer (6 foreclosed lots)
  Yusuf Sabree — Physician/property holder

TIER 2 — ON THE EDGE (served, panicking):
  Brian Banks — PCA superintendent, 8 felonies, lawsuit served
  ↳ BLOCKED KEVIN ON FACEBOOK = consciousness of guilt

TIER 3 — NEXT TO CUT (exposed, indefensible):
  Cylenthia Miller — PCA Board Chair, 3 ethics scandals
  ↳ OWN FACEBOOK POST proves Board Chair role (IMG_5899)

TIER 4 — THE KNOT (connects all layers):
  Todd Perkins — Attorney for Banks AND Miller
  Sean Perkins — 36th District Judge, bought from Sabree office
  ↳ Bar complaint filed, 3 BKs, $100K+ tax liens

TIER 5 — INSTITUTIONAL CAPTURE (regulators who enable):
  Corletta Vaughn — DPSCD Board PRESIDENT, authorized PCA
  Sherry Gay-Dagnogo — Detroit Ombudsman, $8K to Banks
  Tenisha Yancey — 36th District Judge, MacDowell Board

TIER 6 — POLITICAL COVER:
  Latisha Johnson — Council District 2 (meetings at PCA)
  Mary Waters — Council At-Large (promotes PCA)
  Karen Dumas — PR (former Kilpatrick comms chief)

TIER 7 — FAMILY/OPERATIONAL:
  Smith family (Leon, Shayla, Marquita, Simone) — Dresden tenancy
  Joseph Holland Jr. — Foundation treasurer, convicted drug trafficker
  Ian Watts — Banks' cousin (confirmed blood relative)
  Chalcee Norwood — Dean of Ops, both schools
```

---

## PSCU UPDATE — SEPTEMBER 8, 2026 (6:53 PM)

### NEW NODES
- PSCU (Public Service Credit Union, Charter #60683, $459M assets, 32K members)
- Dean J. Trudeau (PSCU CEO, $457K comp, MCUL Board Chair)
- Dawn Seward (PSCU AVP Consumer Lending)
- Fatjon Beshiri (PSCU Consumer Lending Manager — UNVERIFIED)
- Devin Hutchings (PCA Board Treasurer, MI Deserves Better SuperPAC Chair)
- Joseph Richert (MI Deserves Better SuperPAC Treasurer, Special Tree CEO)
- Larry Thomas Jr. (Inner Link Graphics owner)
- Member First Mortgage LLC (PSCU mortgage partner, NMLS #149532)

### NEW EDGES
- Banks → PSCU: ~$549K (purchase + 2nd mortgage + HELOC) [CONFIRMED, ROD]
- Yancey → PSCU: ~$241K (condo mortgage) [CONFIRMED, ROD]
- Watts → PSCU: auto loan (relief from stay in BK) [CONFIRMED, PACER]
- Holland → Romulus: 16004 Middlebelt, 4 miles from PSCU HQ [GEOGRAPHIC]
- Beshiri → Banks discharge: signed 12/29/2025 [UNVERIFIED]
- Hutchings → PCA: Board Treasurer [CONFIRMED, PCA website]
- Hutchings → MI Deserves Better SuperPAC: Chair [CONFIRMED, LinkedIn]
- MI Deserves Better → Inner Link Graphics: $37,151 [CONFIRMED, TransparencyUSA]
- MI Deserves Better → Right Turn Project: $24,700 [CONFIRMED, TransparencyUSA]
- Richert → Bank on Banks PAC: $1,100 [CONFIRMED, TransparencyUSA]
- Hutchings → Dagnogo PAC: $1,000 [CONFIRMED, TransparencyUSA]
- PSCU founded as Wayne County Employees FCU → Eric Sabree domain [INSTITUTIONAL]
- SuperPAC address → PO Box in Romulus (same city as PSCU HQ) [GEOGRAPHIC]

### KEY FINDINGS
1. PSCU is NOT small — $459M assets, CAMELS 1, regulatorily clean
2. Field of membership expanded to ALL Michigan residents — no barrier to Banks joining
3. No Banks-network names on PSCU board or exec team
4. No PSCU campaign donations to any Banks-network candidate
5. 990 Schedule L: "Reported conflict of interest transactions" — NEEDS FOLLOW-UP
6. Fatjon Beshiri (alleged loan officer for Banks) NOT in 990/NMLS/LinkedIn
7. Mortgages outsourced to Member First Mortgage LLC (Grand Rapids)
8. Hutchings' SuperPAC routed $61,851 to Banks orbit ($37K printer + $24.7K nonprofit)
9. SuperPAC treasurer (Richert) personally donated $1,100 to Banks PACs

### ANALYTICAL ASSESSMENT

PSCU is the **geographic and institutional crossroads** between:
- PUBLIC MONEY (Sabree/Treasurer/Wayne County)
- PRIVATE MONEY (Banks/mortgages/HELOCs)
- POLITICAL MONEY (SuperPAC/Inner Link/Right Turn)

The CU was born from Wayne County government (1951). Sabree runs Wayne County money.
Banks gets ALL his mortgages there. Yancey gets her condo mortgage there.
The SuperPAC's PO Box is in Romulus where PSCU is headquartered.
Holland's property is 4 miles from PSCU's main office.

But OSINT shows **no smoking gun** — no board overlap, no campaign money, no enforcement actions.
The nexus is INSTITUTIONAL ECOSYSTEM, not provable conspiracy from public records.

What you need subpoena power for:
1. Loan officer identity for each Banks/Yancey transaction
2. Beshiri employment verification
3. Insider lending disclosures (Reg O) for Yancey
4. Business accounts (Purpose Foundation, PCA)
5. Referral chain documentation
6. 990 Schedule L details (conflict of interest transactions)

---

*Network graph data updated with PSCU deep dig and Hutchings profile.*
*Kevin Mok, September 8, 2026*
