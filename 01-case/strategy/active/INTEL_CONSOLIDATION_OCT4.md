# Intelligence Consolidation — Data Validation + Target Grouping
## October 4, 2026 — Pause-and-Braid Phase
## 4,024 lines SQL / 25 files / 16 batches (Oct 3-4)

---

## PURPOSE

Stop scraping. Clean the data. Validate sources. Braid connections. 
Group remaining targets into mining sets so the next passes are efficient
and every FOIA/OSINT batch pulls multiple threads simultaneously.

---

## I. MASTER NODE ROSTER — Validation Status

### TIER 1: Power Principals (published, verified)
| Node | Role | Source Verified | Gaps |
|------|------|-----------------|------|
| Brian Banks | Subject | ✅ ICHAT, TCR, Free Press, MDOC | None |
| Mayor Mary Sheffield | Political nexus | ✅ Wikipedia, BridgeDetroit | Full donor PDF needed |
| Police Chief Todd Bettison | Enforcement nexus | ✅ BridgeDetroit, detroitmi.gov, OIG | OIG investigation status TBD |
| Fmr Mayor Mike Duggan | Bridge node | ✅ michigan.gov, press coverage | — |
| Warren Evans (WC Exec) | Wayne County nexus | ✅ Free Press, TransparencyUSA | Endorsement specifics TBD |

### TIER 2: Institutional Capture Board
| Node | Role | Source Verified | Gaps |
|------|------|-----------------|------|
| Judge Miller (PCA Chair) | Credential-wash | ✅ purposecharteracademy.com, 3rdcc.org | Canon 4(C) SCAO filing TBD |
| AAG Moreland (PCA Vice Chair) | Credential-wash | ✅ SBM P55993, PCA board page | AG response to complaint TBD |
| CM Latisha Johnson (PCA Sec) | Credential-wash | ✅ PCA board page, TransparencyUSA | Dark money total TBD |
| Devin Hutchings (PCA Treas) | PAC co-chair | ✅ MI Deserves Better FEC, PCA board | Full PAC→school pipeline TBD |
| Major Clora (PCA Asst Treas) | Community bridge | ✅ PCA board page, InsuranceNewsNet | Omega Psi Phi network TBD |
| Nicole Wells Stallworth (MPA Chair) | Credential-wash | ✅ MacDowell board, Bridge MI, LinkedIn | Children's Center departure TBD |
| Thomas Stallworth III | Political dynasty | ✅ MLive, Detroit News, TransparencyUSA | AG campaign finance referral TBD |
| Gay-Dagnogo (Ombudsman) | Quid pro quo | ✅ TransparencyUSA, Chalkbeat | Current ombudsman duties TBD |
| Bedrock / Fleisher | Corporate bridge | ✅ Banks LinkedIn (gala), BridgeDetroit | PCA gala full honoree list TBD |

### TIER 3: Federal Case Network (convictions verified)
| Node | Case # | Sentence | Source Verified | Gaps |
|------|--------|----------|-----------------|------|
| Gasper Fiore | 16-cr-20732 | Pled guilty, bribery | ✅ DOJ, PACER, Free Press | Sentencing details TBD |
| Andre Spivey | 2:21-cr-20490 | 24 months | ✅ DOJ press release | Northern Hook status TBD |
| Rick Sollars | 19-cr-20836 | 71 months | ✅ DOJ, PACER | — |
| Bert Johnson | (TBD docket) | 90 days → 7yr total | ✅ DOJ, Elrick | Cooperator Thornton status TBD |
| Gabe Leland | (state plea) | Pled guilty bribery | ✅ Free Press, Fox 2 | — |
| Eric Smith (Macomb) | (TBD docket) | 21mo fed + 12mo state | ✅ DOJ, Free Press, AG | Judge Parker = Area Towing ✅ |
| Marrocco | (Sep 2022 plea) | Attempted extortion | ✅ Detroit News | Sentence details TBD |
| Reynolds | (TBD docket) | 17 years | ✅ Elrick | Which Reynolds (corruption) TBD |
| Rizzo | (TBD docket) | 66 months/$4M | ✅ Elrick | — |
| Alan C. Young | (TBD docket) | 9 years (auditor) | ✅ Elrick | — |

### TIER 4: Operational Network (campaign/vendor)
| Node | Role | Source Verified | Gaps |
|------|------|-----------------|------|
| Gloria McCastle | $20K+ operative | ✅ TransparencyUSA (5 committees) | Identity beyond payee TBD |
| Rebecca Fadel | Legislative staff + payee | ✅ TransparencyUSA, SBM | AGC complaint status TBD |
| Latania Lewis | Shared payee $8,575 | ✅ TransparencyUSA, LinkedIn | Central City Health role only |
| Venus Coleman | Payee $7,350 + fed case | ✅ TransparencyUSA, PACER 2:91-cr-80936 | Case details TBD |
| Carles Whitlow | Payee $8,500 | ✅ TransparencyUSA | Identity UNKNOWN |
| JohnNae Reynolds | MPA board + $100 | ✅ Free Press, Better Block Detroit | Tim Hortons franchise confirmed |
| Inner Link Graphics | $98K vendor | ✅ TransparencyUSA (multiple ctes) | Owner identity UNKNOWN |
| Custom Promotions | $10.5K + UAW probe | ✅ TransparencyUSA, ASI Central | Jason Gordon investigation status TBD |
| Ross Catering | $35K cross-campaign | ✅ TransparencyUSA | Owner TBD |
| Rafeal Camper | $1K "Prayers" | ⚠️ MacDowell check register only | Identity UNKNOWN |

### TIER 5: Dark Money / Suppression Apparatus
| Node | Role | Source Verified | Gaps |
|------|------|-----------------|------|
| Carol Banks | Benson COS / FBI raid | ✅ Free Press, Fox 2, Deadline Detroit | Northern Hook closure confirmed ✅ |
| Scott Benson | Council / FBI raid | ✅ Free Press, TransparencyUSA | Still on council — current activities TBD |
| Save Detroit Jobs / Detroit Leaders | Dark money | ✅ Deadline Detroit (3 articles) | Full donor list TBD (501c4 no disclosure) |
| Eastside Slate | Endorsement-for-hire | ✅ Deadline Detroit | Full candidate payments TBD |
| Janeé Ayers | Former council / FBI raid | ✅ Free Press, Detroit News | Lost re-election 2021 ✅ |
| Robert Carmack | FBI informant | ✅ Fox 2, Free Press, Metro Times | Malicious prosecution suit status TBD |

### TIER 6: Wiretap Network (2017 document)
| Target | Status | Source Verified | Gaps |
|--------|--------|-----------------|------|
| Brian Banks | Named | ✅ Beeckman affidavit, Area Towing | — |
| Gasper Fiore | Convicted | ✅ DOJ 16-cr-20732 | — |
| Sam Marrocco | Convicted | ✅ Detroit News Sep 2022 | Sentence details TBD |
| Bernard Napoleon | Named | ✅ Beeckman affidavit | Current status TBD |
| Warren Evans / Turfe | Named | ✅ Beeckman affidavit | Current status TBD |
| Gabe Leland | Convicted | ✅ State plea | — |
| Lee Wild | Named | ✅ Beeckman affidavit | Identity/status UNKNOWN |
| Jewel Ware (Tinsley-Talabi) | Named | ✅ Beeckman affidavit | Current status TBD |
| "Casab" | Named | ⚠️ Beeckman affidavit only | Identity COMPLETELY UNKNOWN |

---

## II. VALIDATION PRIORITIES (fix before next scrape)

### A. Must Resolve — Blocking
1. ~~**Inner Link Graphics owner**~~ — ✅ RESOLVED: **LARRY THOMAS JR**, 17515 W 9 Mile Rd Ste 100, Southfield MI 48075 (LARA Entity ID 801470477, filed 2008)
2. **Carles Whitlow** — $8,500 payee, zero identity
3. **"Casab"** — Beeckman affidavit target, unknown person
4. **Lee Wild** — wiretap target, unknown person
5. **Venus Coleman case details** — 2:91-cr-80936, what was she convicted of?

### A-PLUS. LARA Bombshells (Oct 4 2:29 PM)
6. **Holland LIVES AT BANKS HOME** — 1968 Severn, Grosse Pointe Woods. LARA confirms.
7. **Carlton Ross = Ross Catering = Right Turn Project treasurer** — PAC→charity→catering MONEY LOOP
8. **Save Detroit Jobs officers ALL at 13560 E. McNichols** — shell nonprofit confirmed
9. **Custom Promotions dissolved→reformed 3mo later** — Gordon family dodged investigation closure
10. **Purpose Group LLC filed Nov 2024** — management company less than 1 year old, at school address
11. **Banks Strategy AR overdue** — noncompliant with LARA filing requirements

### B. Should Confirm — Strengthens Existing
6. **Holland MDOC 443789** — confirmed via OTIS, but need full criminal record text
7. **Bert Johnson federal docket number** — have conviction, need case number
8. **Eric Smith federal docket number** — AUSA Moran, Judge Parker
9. **Marrocco sentence** — pled guilty Sep 2022, sentence unknown
10. **Reynolds (corruption) first name** — 17yr sentence, which Reynolds?

### C. Nice to Have — Enrichment
11. **Fleisher at PCA gala** — Banks LinkedIn post May 25 2026, need full honoree list
12. **Wells Stallworth departure from Children's Center** — stepped down 2024
13. **Sheffield full donor PDF** — Outlier Media has itemized list
14. **Bettison OIG investigation status** — Sep 16, 2026 report
15. **Tom Casperson** — R-Escanaba senator in MDOT/Fiore wiretap

---

## III. TARGET GROUPING — Mining Sets

### SET 1: PACER Deep Pull (federal docket numbers)
**Method:** CourtListener + PACER lookup
**Targets:**
- [ ] Eric Smith federal case number (E.D. Mich, Judge Linda V. Parker)
- [ ] Bert Johnson federal case number (E.D. Mich, Judge Matthew Leitman)
- [ ] Venus Coleman case 2:91-cr-80936 — docket details + charges
- [ ] Marrocco case number + sentence (pled Sep 2022)
- [ ] Area Towing 2:19-cv-10989 — check for new filings since Sep 2025
- [ ] Sollars 19-cr-20836 — appeal status
- [ ] Spivey 2:21-cr-20490 — release status, Northern Hook remaining targets
**Yield:** 7 case numbers, multiple sentencing details

### SET 2: Michigan Business Entity Search (LARA)
**Method:** LARA corporation search
**Targets:**
- [ ] Inner Link Graphics — registered agent, owner, address
- [ ] Banks Strategy and Consultants — formation docs, registered agent
- [ ] Purpose Group LLC — Banks sole agent, confirmation
- [ ] Purpose Foundation — Crump-Gibson attorney-in-fact docs
- [ ] Drew's Girl Productions — Kierra Sheard LLC status
- [ ] Custom Promotions — Jason Gordon companies (also Idea Consultants, Organization Services of Michigan)
- [ ] Right Turn Project — charity registration (IRS dissolved, never MI registered)
- [ ] Save Detroit Jobs / Detroit Leaders — 501c4 formation, officers
**Yield:** Owner names for major vendor, formation chain for Banks entities

### SET 3: TransparencyUSA Exhaustive Pull
**Method:** TransparencyUSA payee/contributor cross-reference
**Targets:**
- [ ] Carles Whitlow — any other committees paid by or donating
- [ ] McCastle full committee list (beyond Banks/Yancey/Gay-Dagnogo/Knezek)
- [ ] Bank on Banks PAC contributor details (Joseph Richert, Maurice Morton, Paul Zapatka, Sue Jurcak, Charles Nolen, "Cornack")
- [ ] Bank on Wayne County contributors
- [ ] Sheffield donor list (itemized)
- [ ] Latisha Johnson contributor list (full)
- [ ] Bettison campaign finance (if any office sought)
**Yield:** Identification of unknown payees, complete money flow map

### SET 4: FOIA Batch — State Agencies
**Method:** Written FOIA requests, first class mail
**Targets:**
| Agency | Request | Expected Yield |
|--------|---------|----------------|
| DPSCD | MacDowell + PCA board meeting minutes 2022-2026 | Banks hiring vote, §5.2 approval |
| DPSCD | Authorization contracts for MacDowell + PCA | Management agreement terms |
| MDE | Banks educator certificate application + supporting docs | What he disclosed to MDE |
| MDE | MacDowell + PCA annual reports 2022-2026 | Financial data, enrollment, test scores |
| Michigan AG | Any open investigation files re: Banks (likely denied) | Confirm/deny response itself is evidence |
| DNR | Belle Isle PAC appointment records for Banks | Who recommended, what was vetted |
| EMU | DPSA board reappointment records for Bettison Oct 2023 | Parallel charter board governance |
| Wayne County | Commission records re: $425K Saunders contract | Evans/Turfe authorization docs |
| City of Detroit IG | Any investigation records re: Carol Banks dual salary | 2015 investigation outcome |

### SET 5: FOIA Batch — Federal (longer timeline)
**Method:** Written FOIA to FBI/DOJ
**Targets:**
| Agency | Request | Expected Yield |
|--------|---------|----------------|
| FBI Detroit | Records re: 2017-2018 wiretap investigation (partially public via Area Towing) | Additional names, scope |
| USAO E.D. Mich | Operation Northern Hook: status of remaining targets | Active/closed determinations |
| FBI FOIA | Robert Carmack informant file (may be denied) | Chain of cooperation |
| IRS-CI | Right Turn Project 501c3 application + dissolution | Charity fraud documentation |

### SET 6: MDOC / Court Records Pull
**Method:** OTIS + court clerk requests
**Targets:**
- [ ] Holland MDOC 443789 — full criminal record printout
- [ ] Banks ICHAT — updated record (any new entries since Sep 2026)
- [ ] Napoleon — current status/employment
- [ ] "Lee Wild" — OTIS search by name
- [ ] "Casab" — phonetic variations search (Kasab, Cassab, Kazab)
- [ ] Leland — probation compliance status
**Yield:** Criminal record confirmations, unknown identity resolution

### SET 7: Public Records / Web OSINT (next scrape batch)
**Method:** Web search, LinkedIn, public databases
**Priority targets when scraping resumes:**
- [ ] Kenneth Daniels — Detroit Leaders officer, Mercedes/drug dealer charge
- [ ] Bernard Napoleon — wiretap target, current activities
- [ ] Jewel Ware / Tinsley-Talabi — wiretap target, current status
- [ ] Tom Casperson — R-Escanaba senator, MDOT connection to Fiore
- [ ] Jason Gordon — Custom Promotions, UAW probe resolution
- [ ] Wayne County vendor corruption case (Turfe/Commission references)
- [ ] More Clutch Justice articles (Rita has published multiple since Sep 2026)
- [ ] MacDowell board members not yet scraped (beyond Wells Stallworth, Hall, Reynolds)
- [ ] PCA board meeting minutes (if posted publicly per Open Meetings Act)
- [ ] Dawn Ison — DWIHN VP role, why she left USAO

---

## IV. DATA QUALITY ISSUES

### A. Entity ID Conflicts
- `wells-stallworth-nicole` vs `wellsstallworth-nicole` — may have both in SQL, need to reconcile
- `carmack-robert` — inserted in BOTH pacer_dockets.sql AND operation_northern_hook.sql (INSERT OR IGNORE handles this, but notes may differ)
- `holland-joseph` vs `holland-reginald` — early files used different first names (confirmed: first name is ambiguous in sources)

### B. Source Confidence Levels
- **RECORD** (verified in official documents): ICHAT, PACER, OTIS, LARA, TransparencyUSA, SBM directory, DOJ press releases
- **JOURNALISM** (verified by named reporters): Elrick (Free Press/Fox 2), Clutch Justice, BridgeDetroit, Detroit News, Metro Times
- **SOCIAL MEDIA** (lower confidence): Banks LinkedIn posts (may be deleted), campaign websites
- **INFERENCE** (needs upgrade): Some TransparencyUSA payee identities inferred from name matching to public records

### C. Missing Federal Case Numbers
| Person | Have | Need |
|--------|------|------|
| Fiore | 16-cr-20732 | ✅ Complete |
| Spivey | 2:21-cr-20490 | ✅ Complete |
| Sollars | 19-cr-20836 | ✅ Complete |
| Area Towing | 2:19-cv-10989 | ✅ Complete |
| Bert Johnson | Conviction confirmed | ❌ Docket # needed |
| Eric Smith | Conviction confirmed | ❌ Docket # needed |
| Marrocco | Plea confirmed | ❌ Docket # needed |
| Venus Coleman | 2:91-cr-80936 | ✅ Have # but need charge details |
| Stanton | Probation (pension) | ❌ Docket # needed |
| Banks (if any) | Named in wiretap, not charged | N/A |

---

## V. BRAIDED STRUCTURAL FINDINGS

### Finding 1: The 12-Step Suppression Loop
Elrick → Carol Banks exposure → DPS fires her → Benson triples pay → 
Save Detroit Jobs pays $18K → Renames Detroit Leaders → Funds Johnson vs Elrick → 
Johnson wins → Johnson on PCA board → PCA is Banks school → 
Banks named with Carol Banks in 2018 probe → Investigation closed by Dawn Ison → 
Ison now DWIHN VP

**Validation:** Every step sourced to Fox 2, Free Press, Deadline Detroit, TransparencyUSA, or purposecharteracademy.com. Strongest structural finding.

### Finding 2: Gay-Dagnogo Full Circle
$9,750 PAC → Banks for Senate → DPSCD board authorized his schools → 
Announced Purpose Charter → Moved to City Ombudsman → 
Paid McCastle $1K from same PAC → Donated to Sheffield $1K → Donated to Perkins $750

**Validation:** Every financial link in TransparencyUSA. Board actions in Chalkbeat. Quid pro quo language is inference but timeline is record.

### Finding 3: Credential-Washing Board = AGC Complaint Targets
| Board Seat | AGC Complaint | School |
|------------|--------------|--------|
| Miller (Chair) | SCAO notification pending | PCA |
| Moreland (Vice Chair) | Sep 10 + Oct 4 supplement | PCA |
| Johnson (Secretary) | Not yet — dark money complicates | PCA |
| Meihn (Counsel) | Oct 4 NEW complaint | MacDowell |
| Hall (Director) | Oct 4 NEW complaint | MacDowell |
| Perlmuter (former counsel) | Sep 10 complaint | Banks defense |

**Validation:** Board positions from school websites. AGC complaints filed by Kevin. Each AGC filing cites specific MRPC rules with factual basis.

### Finding 4: Same Labor PACs Fund Everything
| PAC | → Banks | → Sheffield | → MI Deserves Better | → Bank on Banks |
|-----|---------|-------------|---------------------|-----------------|
| Carpenters | $10,000 | $20-30K | TBD | $10,000 |
| Operating Engineers | $10,000 | TBD | TBD | $2,500 |
| MI Assn for Justice | $11,500 | TBD | $50,000 | $500 |
| Health Plans PAC | $13,000 | TBD | TBD | $1,000 |

**Validation:** All TransparencyUSA. Pattern is structural — same funders across political and education entities.

### Finding 5: Judge Parker Sees Both Sides
- **Eric Smith sentencing** (21 months) — Macomb prosecutor corruption
- **Area Towing v. Sollars** — civil case holding FBI wiretap files with Banks conversations
- One federal judge has seen this network from the prosecution side AND the civil discovery side

**Validation:** PACER records + DOJ press release. Parker assigned to both cases confirmed.

---

## VI. NEXT ACTIONS (in order)

1. **NOW:** Commit this consolidation document
2. **TONIGHT:** Send going-dark email to GLLG (already drafted)
3. **MONDAY AM:** Print + mail AGC complaints (Meihn, Hall, Moreland supp, Crump-Gibson notification) to AGC Troy MI 48084
4. **MONDAY AM:** File motions electronically via 3rdcc.org ($100 allpaid.com code 6223)
5. **MONDAY AM:** DaSean calls FOC 1-844-785-7593
6. **MONDAY-TUESDAY:** Execute SET 2 (LARA) + SET 3 (TransparencyUSA exhaustive pull)
7. **TUESDAY:** Draft FOIA batch (SET 4 — state agencies) for Wednesday mailing
8. **WEDNESDAY 11:15 AM:** FOC hearing, Referee Biggar
9. **WEDNESDAY:** F.A.M.E. investigation (#1 priority)
10. **FRIDAY 12:00 PM:** CMC with Judge Triplett via Zoom
11. **NEXT WEEK:** Execute SET 1 (PACER deep pull) + SET 6 (MDOC/court records)
12. **NEXT WEEK:** Push consolidated findings to detroit.primals.eco institutional capture graph
13. **ONGOING:** SET 7 (web OSINT) resumes after FOIA batch is mailed

---

## VII. FOIA BATCH TEMPLATE

All FOIAs to be sent first class mail (per Kevin's standard):

```
[Date]
[Agency Name]
[Address]

RE: Freedom of Information Act Request

Dear FOIA Coordinator:

Pursuant to the Michigan Freedom of Information Act, MCL 15.231 et seq.,
I hereby request the following records:

[SPECIFIC REQUEST]

I am willing to pay reasonable copying and search fees up to $25.00.
If costs exceed this amount, please contact me before processing.

I request a response within five (5) business days per MCL 15.235(2).

Sincerely,
Kevin Mok
[Address]
eco.primal@pm.me
[REDACTED_PHONE]
```

For federal FOIAs, substitute 5 U.S.C. § 552 and 20 business day response.

---

*"We are building a massive intel net before we do the deeper scrapes.
Allows us to post it all online and fill depth as we go." — Kevin, Oct 4 2026*
