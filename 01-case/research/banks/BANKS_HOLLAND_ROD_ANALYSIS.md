# Banks & Holland — Wayne County Register of Deeds Analysis
## Civil fraud investigation | OCR completed September 5, 2026

**Case context:** Investigation of fraud and corruption in charter school administration. Brian Banks holds 8 felony convictions and, under his Michigan school administrator certificate, is forbidden from handling cash. Joseph Holland Jr. (MDOC #443789, 5 bankruptcies) serves as PAC Treasurer, Purpose Foundation Secretary, and Banks Living Trust successor trustee.

**Sources:**
- Wayne County Official Records Search (pulled September 2, 2026; certified through August 3, 2026)
- 33 PDFs OCR'd via `doc_extract.py` (Tesseract 5.5) — all scanned images, zero native text
- Prior visual analysis: `tools/osint/results/WAYNE_ROD_BANKS_SEP2.md`
- Related judge analysis: `tools/osint/results/WAYNE_ROD_JUDGES_SEP2.md`
- Page images: `02-evidence/wayne-rod-sep2/images/` (batch1 + batch2 PNGs)

---

## 1. Source Inventory

### Batch 1 — Banks search (14 PDFs)

| File | Size | Instrument # | Type | Key Subject |
|------|------|-------------|------|-------------|
| `18599315_256075472_docimage_actual.pdf` | 79.7 KB | 2018023312 | Warranty Deed | Banks buys 1968 Severn — **$232,000** |
| `18599315_253965168_docimage_actual.pdf` | 1.3 MB | 2018023313 | Mortgage | PSCU purchase loan — **$214,600** |
| `18599315_254586298_docimage_actual.pdf` | 56.7 KB | 2007402847 | Quit Claim Deed | Holland → Banks+Holland JTWRS, 21553 Newcastle — **$1** |
| `18599315_252236876_docimage_actual.pdf` | 38.2 KB | 2009283689 | State Tax Lien | Banks at 21553 Newcastle — **$1,071.81** |
| `18599315_252319452_docimage_actual.pdf` | 37.1 KB | 2010032175 | Tax Lien Release | Lien #1560983 released |
| `18599315_245242124_docimage_actual.pdf` | 29.7 KB | (L.58592 P.1326) | Claim of Lien | Red Baron Enterprises — **$209.77** |
| `18599315_245564311_docimage_actual.pdf` | 26.0 KB | 2020201341 | Lien Discharge | Red Baron satisfied |
| `18599315_245749076_docimage_actual.pdf` | 417.3 KB | 2022081643 | Mortgage | PSCU refi — **$61,700** |
| `18599315_245688365_docimage_actual.pdf` | 21.6 KB | 2022278271 | State Tax Lien | Banks at 1968 Severn — **$6,078.35** |
| `18599315_245713745_docimage_actual.pdf` | 20.8 KB | 2024192364 | Tax Lien Release | Lien #2022278271 released |
| `18599315_246956512_docimage_actual.pdf` | 30.3 KB | 2024223261 | Quit Claim Deed | Banks → Brian Banks Living Trust — **$0** |
| `18599315_268838451_docimage_actual.pdf` | 91.7 KB | 2025307266 | Certificate of Trust | Successor trustees: Holland Jr., Justin Banks |
| `18599315_268838455_docimage_actual.pdf` | 487.8 KB | 2025307267 | Revolving Credit Mortgage | PSCU HELOC — **$93,700 max** |
| `18599315_270405267_docimage_actual.pdf` | 44.8 KB | 2026019497 | Discharge of Mortgage | 2022 PSCU mortgage satisfied |

**Extracted text:** `02-evidence/wayne-rod-sep2/batch1/extracted/`

### Batch 2 — Holland search (19 PDFs)

| File | Size | Instrument # | Type | Key Subject |
|------|------|-------------|------|-------------|
| `18599425_261325731_docimage_actual.pdf` | 43.5 KB | (1989) | Warranty Deed | Joseph & Seretta Holland buy 5737 Drexel — **$8,000** |
| `18599425_259436173_docimage_actual.pdf` | 76.2 KB | (1990) | Mortgage | Kay-Bee Construction — **$9,974.16** |
| `18599425_259288580_docimage_actual.pdf` | 24.0 KB | (1995) | State Tax Lien | Joseph & Seretta Holland — **$545.40** |
| `18599425_259323793_docimage_actual.pdf` | 72.1 KB | (1996) | Tax Lien Release | Drexel lien released |
| `18599425_258588897_docimage_actual.pdf` | 74.3 KB | D468955 | UCC-1 Financing | Joseph H. & Mary Ellen Holland, 5143 S. Telegraph |
| `18599425_258584824_docimage_actual.pdf` | 63.1 KB | — | UCC-3 Continuation | First of America, Jul 1995 |
| `18599425_251574661_docimage_actual.pdf` | 101.4 KB | — | UCC-3 Continuation | National City Bank, Jun 2000 |
| `18599425_251545359_docimage_actual.pdf` | 59.5 KB | — | UCC-3 Termination | National City Bank, Oct 2000 |
| `18599425_256620431_docimage_actual.pdf` | 86.2 KB | — | Note Release | Mary Ellen released; Joseph H. liable — Apr 1992 |
| `18599425_251301873_docimage_actual.pdf` | 48.2 KB | — | Discharge of Mortgage | Coach Dr satisfied — Oct 2000 |
| `18599425_251301876_docimage_actual.pdf` | 48.5 KB | — | Discharge Assignment | Coach Dr assignment — Oct 2000 |
| `18599425_257842169_docimage_actual.pdf` | 156.8 KB | 20-C-7359 | Writ of Restitution | Roy & Melba Holland vs. Micallefs — 1982 |
| `18599425_264805359_docimage_actual.pdf` | 166.8 KB | (1978) | Family Mortgage | Holland family, Taylor — **$26,770** |
| `18599425_248801446_docimage_actual.pdf` | 35.5 KB | 2010142679 | Tax Forfeiture | Joseph Holland, 16004 Middlebelt — 2008 taxes |
| `18599425_249910923_docimage_actual.pdf` | 33.5 KB | 2010274708 | Tax Redemption | Holland pays — **$3,404.15** |
| `18599425_247152694_docimage_actual.pdf` | 34.7 KB | 2012195671 | Tax Forfeiture | Middlebelt — 2010 taxes |
| `18599425_247683350_docimage_actual.pdf` | 33.2 KB | 2012299455 | Tax Redemption | **Lisa Cudworth** pays — **$2,903.22** |
| `18599425_247204344_docimage_actual.pdf` | 35.1 KB | 2014199796 | Tax Forfeiture | Middlebelt — 2012 taxes |
| `18599425_249631255_docimage_actual.pdf` | 33.5 KB | 2015215322 | Tax Redemption | **Lisa Cudworth** pays — **$1,113.75** |

**Extracted text:** `02-evidence/wayne-rod-sep2/batch2/extracted/`

**Note:** The Holland name search returned documents for at least four distinct Joseph Hollands across three generations. Section 4 disambiguates them.

---

## 2. Brian Banks — Property Portfolio Map

```
BRIAN BANKS — WAYNE COUNTY PROPERTY NETWORK
═══════════════════════════════════════════════

21456 Newcastle Rd, Harper Woods 48225
├── Pre-2017 mailing address (warranty deed, trust cert)
├── Justin Banks (successor trustee #2) lists this address
└── One house north of Holland's Newcastle property

21553 Newcastle Rd, Harper Woods 48225  [Tax ID 42004030110000]
├── Joint tenancy with Joseph Holland Jr. since Jun 1, 2007 ($1 QCD)
├── Banks used this address for state income tax lien (2008–2010)
├── Holland Jr. was sole grantor; added Banks as JTWRS for $1
└── STATUS UNKNOWN — no disposition recorded in this batch

1968 Severn Rd, Grosse Pointe Woods 48236  [Tax ID 40015010325000]
├── PRIMARY RESIDENCE — purchased Nov 3, 2017 for $232,000
├── Held in Brian Banks Living Trust since Aug 12, 2024
├── Holland Jr. lists THIS as his address (trust cert, Nov 2025)
├── Purpose Foundation registered here (LARA — not ROD)
├── Current recorded encumbrances:
│   ├── 2017 PSCU purchase mortgage: $214,600 (Loan #XXXX6470)
│   ├── 2025 PSCU HELOC: $93,700 max revolving (LoanLINER)
│   └── 2022 PSCU mortgage ($61,700): DISCHARGED Dec 29, 2025
└── Total recorded debt exposure: ~$308,300 on $232K purchase
```

### Banks — Document Detail

| # | Date | Event | Amount | Parties |
|---|------|-------|--------|---------|
| 1 | Jun 1, 2007 | QCD — Newcastle JTWRS | $1.00 | Grantor: Joseph Holland Jr. → Grantees: Holland Jr. + Banks (JTWRS) |
| 2 | Nov 21, 2008 | State income tax assessment | — | Banks at 21553 Newcastle |
| 3 | Aug 4, 2009 | State tax lien filed | $1,071.81 | Lien #1560983 |
| 4 | Jan 22, 2010 | Tax lien released | — | Mary G. MacDowell, Treasury |
| 5 | Nov 3, 2017 | Warranty deed — Severn purchase | **$232,000** | Valentics → Banks; prior addr 21456 Newcastle |
| 6 | Nov 3, 2017 | PSCU purchase mortgage | **$214,600** | Maturity Dec 1, 2047; Title Connect LLC |
| 7 | Dec 3, 2019 | Red Baron construction lien | $209.77 | 20315 E 9 Mile Rd, St. Clair Shores |
| 8 | Feb 12, 2020 | Lien recorded | — | Jonathan Redziniak, Red Baron Enterprises LLC |
| 9 | Jul 9, 2020 | Red Baron lien discharged | — | — |
| 10 | Mar 11, 2022 | PSCU second mortgage | **$61,700** | Maturity Mar 28, 2032 |
| 11 | Sep 7, 2022 | State tax lien #3 | **$6,078.35** | Income tax 2021–2022; Lien #2022278271 |
| 12 | Jun 25, 2024 | Tax lien #3 released | — | Katina Litterini, Treasury |
| 13 | Aug 12, 2024 | QCD to Living Trust | $0 | Banks → Brian Banks Living Trust |
| 14 | Oct 29, 2025 | PSCU HELOC on trust | **$93,700 max** | 15-year revolving; LOANLINER |
| 15 | Nov 7, 2025 | Trust certificate recorded | — | Successor trustees named |
| 16 | Dec 29, 2025 | 2022 mortgage discharged | — | Fatjon Beshiri, PSCU |

**Lender concentration:** Public Service Credit Union (7665 Merriman Rd, Romulus, MI 48174) is Banks' exclusive recorded Wayne County lender — 2017 purchase, 2022 refi, 2025 HELOC.

**Attorneys/notaries on Banks documents:**
- Jehan Crump-Gibson (Great Lakes Legal Group PLLC, Southfield) — trust QCD and trust certificate
- Eric R. Sabree (Wayne County Treasurer) — certified no delinquent taxes on Severn purchase (Nov 30, 2017)
- Fatjon Beshiri — PSCU Consumer Lending Manager (2025 discharge)

---

## 3. Joseph Holland — Property Portfolio Map

The "HOLLAND JOSEPH" ROD search returns multiple individuals. They must be separated before drawing conclusions about Holland Jr.

### 3A. Joseph Holland Jr. — Banks Associate (HIGH RELEVANCE)

```
JOSEPH HOLLAND JR. — INFERRED PORTFOLIO
════════════════════════════════════════

21553 Newcastle Rd, Harper Woods 48225
├── Joint tenant with Brian Banks since Jun 2007 ($1 QCD)
├── Holland Jr. was sole owner; added Banks for $1
└── Banks' 2008–2009 tax lien used this address

1968 Severn Rd, Grosse Pointe Woods 48236
├── Lists as HIS address on Banks Living Trust cert (Nov 2025)
├── First successor trustee — controls property if Banks incapacitated
└── Physically residing at Banks' trust property (per trust cert)

16004 Middlebelt, Romulus 48174  [Parcel 80137990018000]
├── 5 acres, N 5 ac of S 10 ac, Sec 35 T3S R9E
├── Tax forfeiture 3 times (2008, 2010, 2012 tax years)
├── Redemptions: Holland ($3,404) + Lisa Cudworth ($4,017)
└── STATUS UNKNOWN — no deed transfer in this batch
```

| Date | Event | Amount | Paid By |
|------|-------|--------|---------|
| Mar 1, 2010 | Forfeiture (2008 taxes) | — | — |
| Apr 16, 2010 | Redemption | $3,404.15 | Joseph Holland |
| Mar 1, 2012 | Forfeiture (2010 taxes) | — | — |
| Apr 5, 2012 | Redemption | $2,903.22 | **Lisa Cudworth** |
| Mar 1, 2014 | Forfeiture (2012 taxes) | — | — |
| Dec 30, 2014 | Redemption | $1,113.75 | **Lisa Cudworth** |

**Assessment:** Middlebelt pattern (2008–2014 chronic tax default, 5 bankruptcies 2005–2014) matches Holland Jr.'s profile. Romulus is the same city as PSCU's headquarters — geographic overlap with Banks' lender.

### 3B. Joseph Holland & Seretta Holland — Possible Early Household

| Property | Event | Date | Amount |
|----------|-------|------|--------|
| 5737 Drexel, Detroit 48213 | Warranty deed from O'Neals | Jul 11, 1989 | **$8,000** |
| 5737 Drexel | Mortgage to Kay-Bee Construction | Sep 28, 1990 | **$9,974.16** |
| 5737 Drexel | State income tax lien | Dec 26, 1995 | **$545.40** |
| 5737 Drexel | Tax lien release | Oct 31, 1996 | — |

**Assessment:** Detroit east side (48213), 1989–1996 timeline could be Holland Jr. in early adulthood with partner Seretta. If confirmed, adds another property and tax lien to Jr.'s record. Drafted by LeRoy B. McInally, attorney, Grosse Pointe Farms.

### 3C. Joseph H. Holland & Mary Ellen Holland — Father's Generation

| Property | Documents | Era |
|----------|-----------|-----|
| 32690 Coach Dr, New Baltimore 48047 | Mortgage Aug 1990; discharged Oct 2000 | 1990–2000 |
| 5143 S. Telegraph, Dearborn Heights 48125 | UCC-1 Sep 1990; continuations 1995, 2000; termination Oct 2000 | 1990–2000 |

**Key finding — Note Release (Apr 29, 1992):** Security Bank released **Mary Ellen Holland** from personal liability on the promissory note but **Joseph H. Holland was NOT released**. Mortgage lien remained. Suggests marital separation or divorce negotiation.

**SSNs from UCC filings:** Joseph H. 386-46-XXXX; Mary Ellen 371-48-XXXX

### 3D. Holland Family — Elder Generation (1978–1984)

| Property | Event | Date | Amount |
|----------|-------|------|--------|
| Lots 86–95, Patterson's Telreka Sub, Taylor (26640 Goddard Rd) | Inter-family mortgage | Dec 28, 1978 | **$26,770** (0% interest) |
| XXXX N. Gulley Rd, Dearborn Heights | Writ of restitution — Roy & Melba Holland vs. Joseph & Kathy Micallef | Oct 18, 1982 | Vacant lot eviction |

**1978 mortgage parties:** Marvin Holland ($23,187 to himself), Roy W. & Wilma Holland, Evelyn Riedel, Joseph H. & Jill Holland. Marvin Holland is both mortgagor and mortgagee — financing his own family at 0% interest.

---

## 4. Banks ↔ Holland — Overlap & Connections

### Direct Property Connections

| Connection | Evidence | Significance |
|------------|----------|--------------|
| **Same street, adjacent houses** | 21456 Newcastle (Banks/Justin) and 21553 Newcastle (Holland/Banks JTWRS) | Neighbors before formalized financial tie |
| **$1 joint tenancy** | QCD Jun 1, 2007 — Holland adds Banks to Newcastle deed | Banks acquires survivorship interest in Holland's home for nominal consideration |
| **Shared tax address** | Banks' 2008–2009 state tax lien at 21553 Newcastle | Banks treated Holland's house as his legal address |
| **Successor trustee** | Trust cert Nov 2025 — Holland Jr. #1, Justin Banks #2 | Holland controls Banks' primary asset if Banks dies/incapacitated |
| **Holland at Severn** | Trust cert lists Holland Jr. at 1968 Severn | Holland physically occupies Banks' trust property |
| **Romulus geography** | Holland's Middlebelt parcel + PSCU headquarters both in Romulus | Same municipality; possible additional connection |

### Financial Dependency Timeline

| Year | Holland Event | Banks Connection |
|------|--------------|-----------------|
| 2005 | 1st bankruptcy (Ch. 7) | Already neighbors on Newcastle |
| 2007 | QCDs Newcastle to Banks as JTWRS | Banks gets equity for $1 |
| 2008–2009 | 2nd/3rd bankruptcies | Banks tax lien at Holland's address |
| 2008–2014 | Middlebelt chronic tax forfeiture | Lisa Cudworth pays $4,017 to save property |
| 2014 | 4th & 5th bankruptcies (Ch. 7) | — |
| 2017 | — | Banks buys Severn ($232K) |
| 2024 | Named successor trustee | Trust created 2 months before Purpose Foundation |
| 2024–present | PAC Treasurer, Foundation Secretary | Running Banks' financial operations |

### No Direct ROD Connection Found

The following network members do **not** appear in any of the 33 OCR'd documents:
- Tracey D. Ellis (Purpose Foundation Treasurer — connected via LARA/corporate records, not ROD)
- Todd Perkins (Banks attorney)
- Cylenthia LaToye Miller (PCA co-founder)
- Tenisha Yancey (campaign payer to Banks)
- Shayla Smith / Smith household
- Any "Moreland" name

Ellis and Purpose Foundation are linked to **1968 Severn** through corporate filings, not through these deed records.

---

## 5. Master Timeline — Both Portfolios

```
1978 ─── Holland family inter-mortgage, Taylor ($26,770)
1982 ─── Roy & Melba Holland eviction, Dearborn Heights
1989 ─── Joseph & Seretta Holland buy 5737 Drexel ($8,000)
1990 ─── Joseph H. & Mary Ellen Holland: Coach Dr mortgage + Telegraph UCC
1992 ─── Mary Ellen released from note; Joseph H. remains liable
1995 ─── Joseph & Seretta state tax lien, Drexel ($545.40)
1996 ─── Drexel tax lien released
2000 ─── Coach Dr mortgage satisfied; Telegraph UCC terminated
2005 ─── Holland Jr. 1st bankruptcy
2007 ─── ★ Holland QCDs Newcastle to Banks+Holland JTWRS ($1)
2008 ─── Banks state tax assessment at 21553 Newcastle
2009 ─── Banks state tax lien ($1,071.81); Holland 2nd/3rd bankruptcies
2010 ─── Banks tax lien released; Holland Middlebelt forfeiture #1
2010 ─── Holland redeems Middlebelt ($3,404.15)
2012 ─── Holland Middlebelt forfeiture #2; Cudworth redeems ($2,903.22)
2014 ─── Holland Middlebelt forfeiture #3; Holland 4th/5th bankruptcies
2014 ─── Cudworth redeems Middlebelt ($1,113.75)
2017 ─── ★ Banks buys 1968 Severn ($232,000); PSCU mortgage ($214,600)
2019 ─── Red Baron construction lien on Severn ($209.77)
2020 ─── Red Baron lien discharged
2022 ─── Banks PSCU refi mortgage ($61,700); state tax lien #3 ($6,078.35)
2024 ─── ★ Banks transfers Severn to Living Trust ($0)
2024 ─── Banks tax lien #3 released (Jun 25)
2024 ─── Purpose Foundation incorporated (Dec — LARA, not ROD)
2025 ─── ★ Trust cert recorded; PSCU HELOC ($93,700 max)
2025 ─── 2022 PSCU mortgage discharged (Dec 29)
```

---

## 6. Red Flags

### 6.1 Asset Protection Engineering (Banks)

1. **Trust timing:** Severn transferred to revocable living trust (Aug 12, 2024) approximately **two months before** Purpose Foundation incorporation (Dec 9, 2024) and Purpose Group LLC formation — classic pre-litigation asset shielding pattern.

2. **HELOC after school launch:** $93,700 revolving credit line recorded Nov 7, 2025 — approximately **one month after** Purpose Charter Academy opened. Trust property used as cash extraction vehicle while Banks is forbidden from handling school cash.

3. **Revocable trust with compromised successor:** Trust is revocable during Banks' lifetime (he retains control), but successor trustee #1 is a 5-time bankrupt with MDOC record who already lives at the property. Creates appearance of legitimate estate planning while ensuring Holland maintains access.

4. **Over-leveraging:** ~$308,300 in recorded mortgage obligations against a $232,000 purchase price (133% LTV at origination, before appreciation). Serial state tax liens ($1,071 + $6,078) indicate chronic income tax nonpayment.

### 6.2 Straw Purchase / Nominal Transfer Patterns

1. **$1 QCD joint tenancy (2007):** Holland transferred half-interest in 21553 Newcastle to Banks for $1 with full rights of survivorship. No market consideration. Banks' subsequent use of this address for tax purposes suggests it functioned as his residence, not an investment.

2. **$0 trust transfer (2024):** Severn moved to trust for no consideration — removes property from Banks' individual name while he retains control as settlor/trustee.

### 6.3 Holland Financial Dysfunction

1. **Three tax forfeitures in six years** on Middlebelt — pattern of chronic nonpayment, not one-time hardship.
2. **Third-party bailout:** Lisa Cudworth paid $4,016.97 total (2012 + 2014) to prevent foreclosure — unexplained financial dependency.
3. **Generational pattern:** Father (Joseph H.) had note liability after wife released; elder family had inter-family 0% mortgages and eviction proceedings going back to 1978.

### 6.4 Construction Lien Anomaly

Red Baron Enterprises LLC (Jonathan Redziniak, St. Clair Shores) filed a **$209.77** construction lien for labor/material on Severn (Dec 3, 2019). Discharged within 5 months. Amount is trivial relative to property value — may indicate dispute over minor work or placeholder lien. Entity identity unverified (LARA search needed).

### 6.5 Certificate / Cash-Handling Conflict

Banks is forbidden by his administrator certificate from handling cash, yet:
- He is settlor/trustee of a revocable trust with HELOC access
- Holland (successor trustee, Foundation Secretary, PAC Treasurer) handles financial operations
- PSCU HELOC provides direct cash line against trust property

This structure separates Banks from paper cash handling while preserving access to extracted equity.

---

## 7. Connections to Network Members

### 7.1 Public Service Credit Union — Shared Lender (Banks + Yancey)

| Person | PSCU Relationship | Amount |
|--------|------------------|--------|
| **Brian Banks** | All Wayne County mortgages (2017, 2022, 2025) | $214.6K + $61.7K (discharged) + $93.7K HELOC |
| **Tenisha Yancey** | Harbortown condo mortgage (Oct 2024) | $241,200 (Loan #XXXX5601) |

PSCU (7665 Merriman Rd, **Romulus**) is a small credit union. Both the convicted felon school operator and the judge who paid him $15,750 in campaign funds use the same lender. Subpoena drafted: `SUBPOENA_15_PSCU_YANCEY.txt`, `SUBPOENA_06_PSCU.txt`.

**Holland geographic note:** Holland Jr.'s Middlebelt property is also in Romulus — same city as PSCU, though no direct Holland-PSCU mortgage appears in this batch.

### 7.2 Eric R. Sabree — Wayne County Treasurer

Sabree certified no delinquent taxes on Banks' Severn warranty deed (Nov 30, 2017). Sabree also signed Yancey's 2025 tax forfeiture certificate and Miller's redemption documents. Sabree endorsed Miller on keepjudgemiller.com.

### 7.3 1968 Severn — Operational Hub

| Entity/Person | Connection to Severn |
|---------------|---------------------|
| Brian Banks Living Trust | Property held in trust |
| Joseph Holland Jr. | Successor trustee; lists as residence |
| Justin Banks | Successor trustee #2 |
| Purpose Foundation | Registered address (LARA) |
| Tracey D. Ellis | Foundation Treasurer; Yecart Accounting |
| Purpose Charter Academy | Banks is founder/administrator |

One address serves as home, trust property, nonprofit headquarters, and school nexus.

### 7.4 Parallel Pattern — Smith Household (not in ROD batch)

| Pattern | Banks Network | Smith Household |
|---------|--------------|-----------------|
| Credit union lending | PSCU (all mortgages) | Lake Trust CU (Shayla employer; family mortgage) |
| Serial bankruptcy | Holland (5 BK), Perkins (3 BK) | Marquita (3 BK), Simone (1–2 BK) |
| Property shielding | Severn in Living Trust | Dresden in Marquita/Leon name |
| Compromised associates | Holland (MDOC), Perkins | Marquita, Simone |

### 7.5 Miller / Bryant Case Convergence

Judge Miller (PCA co-founder, defendant in Bryant v. Miller 2:26-cv-10917) does not appear in these ROD documents. Connection is through PCA/Purpose Foundation corporate structure, not property records. Perkins (Miller's attorney, 3 bankruptcies) also absent from ROD.

---

## 8. New Names Identified — Search Targets

| Name | Context | Priority | Recommended Search |
|------|---------|----------|-------------------|
| **Justin Banks** | Successor trustee #2; 21456 Newcastle | **HIGH** | Wayne ROD, LARA, PACER, social media — son? brother? |
| **Lisa Cudworth** | Paid $4,017 in Holland Middlebelt tax redemptions | **HIGH** | Wayne ROD, PACER, bankruptcy, relationship to Holland |
| **Jonathan Redziniak / Red Baron Enterprises LLC** | Construction lien on Severn ($209.77) | **MEDIUM** | LARA entity search, additional ROD |
| **Seretta Holland** | Co-owner 5737 Drexel; state tax lien | **MEDIUM** | Confirm if Holland Jr.; court, bankruptcy |
| **Jehan Crump-Gibson** | Drafted trust QCD + trust cert (Great Lakes Legal Group) | **MEDIUM** | Other clients; Purpose Foundation connection? |
| **Fatjon Beshiri** | PSCU lending manager signing discharge | **LOW** | Context only |
| **LeRoy B. McInally** | Attorney on 1989 Drexel deed | **LOW** | Context only |
| **Marvin / Roy / Joseph H. Holland** | Elder family, Taylor/Dearborn Heights | **LOW** | Genealogical context |

---

## 9. Questions Needing Answers

### Property Status
- [ ] **21553 Newcastle** — Still Banks + Holland JTWRS? Any QCD, mortgage, or forfeiture since 2007?
- [ ] **16004 Middlebelt, Romulus** — Does Holland Jr. still hold title? Did it eventually foreclose after 2014?
- [ ] **5737 Drexel, Detroit** — Is "Joseph Holland & Seretta Holland" the same person as Holland Jr.? Current ownership?
- [ ] **21456 Newcastle** — Who holds title now? Justin Banks' relationship to Brian?

### Financial / Legal
- [ ] **Lisa Cudworth** — Who is she? Partner, relative, business associate of Holland or Banks?
- [ ] **Red Baron Enterprises LLC** — LARA entity search; what work was performed for $209.77?
- [ ] **PSCU relationship** — How did Banks and Yancey both become PSCU members? Employee referral? Shared broker?
- [ ] **Trust beneficiaries** — Full trust agreement (not in ROD — need discovery/subpoena) — who inherits beyond successor trustees?
- [ ] **HELOC disbursement** — Where did the $93,700 credit line proceeds go? School operations? Personal use?

### Network / Case
- [ ] **Ellis at Severn** — Any unrecorded lease, POA, or occupancy arrangement connecting Ellis to the property?
- [ ] **Purpose Foundation use of Severn** — Is the nonprofit paying rent to the trust? At what rate?
- [ ] **Holland cash handling** — What financial records connect Holland's property interests to PAC/Foundation disbursements?
- [ ] **State tax liens #1–#4** — Full assessment history for Banks; any liens not yet released?
- [ ] **2017 purchase source of down payment** — $232K purchase with $214.6K mortgage = ~$17.4K down. Source?

### Disambiguation
- [ ] Confirm Joseph Holland on Middlebelt forfeiture records is Holland Jr. (not father) — compare DOB/SSN if available from other records
- [ ] Seretta Holland identity — marriage/divorce records for Holland Jr.

---

## 10. Document-to-Evidence Index

For exhibit preparation, each PDF maps to:

| Exhibit Candidate | PDF File | Instrument | Description |
|-------------------|----------|------------|-------------|
| Newcastle QCD | batch1/254586298 | 2007402847 | Holland-Banks joint tenancy formation |
| Severn Warranty Deed | batch1/256075472 | 2018023312 | Banks purchase $232K |
| Severn Trust QCD | batch1/246956512 | 2024223261 | Asset transfer to trust |
| Trust Certificate | batch1/268838451 | 2025307266 | Holland as successor trustee |
| HELOC | batch1/268838455 | 2025307267 | $93.7K revolving credit |
| Tax Lien (Newcastle) | batch1/252236876 | 2009283689 | Banks at Holland address |
| Tax Lien (Severn) | batch1/245688365 | 2022278271 | $6,078.35 |
| Cudworth Redemption | batch2/247683350 | 2012299455 | Third party pays Holland taxes |
| Middlebelt Forfeitures | batch2/248801446, 247152694, 247204344 | Various | Pattern of tax default |

OCR text files and PNG page images are available for all documents listed in Section 1.

---

## 11. Summary Assessment

Brian Banks and Joseph Holland Jr. share a property relationship dating to at least 2007, when Holland added Banks as joint tenant on 21553 Newcastle for $1. Banks subsequently used Holland's address for tax purposes, confirming cohabitation or financial interdependence. After Banks purchased 1968 Severn in 2017, Holland moved to Banks' property and was named first successor trustee of the Brian Banks Living Trust in 2025 — giving a 5-time bankrupt felon control over Banks' primary asset.

Banks' financial pattern shows serial state tax liens, aggressive leverage through a single credit union (PSCU), and a trust/HELOC structure created in 2024–2025 that coincides with charter school entity formation and opening. The trust shields Severn from individual judgments while preserving Banks' control and Holland's occupancy.

Holland's separate portfolio (Middlebelt, possibly Drexel) shows chronic tax default and dependence on third-party bailouts (Lisa Cudworth). The Holland family has generational property distress spanning 1978–present across Wayne County.

No direct ROD evidence connects Ellis, Miller, Yancey, Perkins, or Moreland to these specific documents — but PSCU (shared by Banks and Yancey), Eric R. Sabree (Treasurer certifying multiple network properties), and 1968 Severn (operational hub for Foundation/school) provide indirect network links requiring follow-up through subpoenas and corporate records.

---

*Analysis compiled September 5, 2026*
*OCR: doc_extract.py / Tesseract 5.5*
*Kevin Mok*
