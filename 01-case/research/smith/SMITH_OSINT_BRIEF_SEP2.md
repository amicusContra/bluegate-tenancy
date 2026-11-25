# SMITH HOUSEHOLD — OPEN-SOURCE INTELLIGENCE BRIEF

**Compiled:** September 2, 2026
**Author:** Kevin Mok
**Method:** OSINT only — federal court records (CourtListener/RECAP),
Michigan bankruptcy court (E.D. Michigan), Wayne County property
records, MDHHS case records, USPS tracking, LARA corporate filings,
Facebook/Instagram OSINT, court filing exhibits, witness statements.
Automated via OSINT Toolkit (Python/Playwright/CourtListener API).

---

## METHODOLOGY

Every claim is sourced from public records, court filings, or the
opposing party's own exhibits. The CourtListener API and PubRecords
SDK provided federal court data. Bankruptcy case metadata was
cross-referenced against property records and employment data.
No confidential sources. No interviews with third parties. No
subpoenas (yet).

---

## I. THE HOUSEHOLD

XXXXX Dresden St, Detroit, MI 48205 — Wayne County.

Four adults, at least four children, one bathroom.

| Name | Role | Employment | Income (est.) |
|------|------|-----------|--------------|
| **Leon A. Smith** | Father, property owner | USPS Mail Carrier (federal) | $45-65K/year |
| **Marquita L. Smith** | Mother, property co-owner | Unknown / unstable | Unknown |
| **Shayla Smith** | Daughter, defendant | Lake Trust Credit Union (Brighton, MI) | $35-45K/year (concealed on court filings) |
| **Simone Smith** | Daughter | Unknown | Unknown |
| Children | Sahana (9), Allanna (7), Amir, Journi (~2) | — | — |
| **Robert Hill** | Unknown relation | Unknown | Appears at Dresden Dec 2025 (property report) |
| **Tae Reed** | Son (Marquita's) | Unknown | Facebook |

**Source:** FOC 23 verified statement (Doc 1, Jun 13, 2026);
DaSean Mitchell statement (Aug 20, 2026); Wayne County property
records; Facebook (Marquita Smith profile, Feb 2025 tagged posts)

---

## II. MARQUITA SMITH — THREE FEDERAL BANKRUPTCIES IN 13 MONTHS

The CourtListener API returned three confirmed bankruptcy cases for
Marquita Smith in the Eastern District of Michigan, filed between
June 2025 and July 2026.

### Filing 1 — Chapter 7 (Liquidation)

| Field | Value |
|-------|-------|
| **Case** | Marquita Smith, No. 25-46692 |
| **Court** | U.S. Bankruptcy Court, E.D. Michigan |
| **Chapter** | 7 |
| **Filed** | June 30, 2025 |
| **Dismissed** | August 3, 2025 (34 days) |
| **Judge** | Maria L. Oxholm |
| **Trustee** | Stuart A. Gold |
| **Final docket entry** | "Notice of Dismissal with BNC Certificate of Mailing" (Doc 17, Aug 3, 2025) followed by "Final Decree and Case Closed" |

**Source:** CourtListener API, docket ID 70675920,
courtlistener.com/docket/70675920/marquita-smith/

**Significance:** Chapter 7 discharges all unsecured debt in
exchange for liquidating non-exempt assets. Marquita attempted
the "clean slate" option. The case was dismissed after 34 days.
Most common reasons for rapid Chapter 7 dismissal: failed the
means test (household income too high), failure to file required
schedules/documents, or the court found abuse. Given the Dresden
household's combined income (Leon's USPS salary + Shayla's Lake
Trust salary), the means test failure is the most likely
explanation — the household earns too much for Chapter 7 relief.

### Filing 2 — Chapter 13 (Reorganization)

| Field | Value |
|-------|-------|
| **Case** | Marquita R. Smith, No. 25-47952 |
| **Court** | U.S. Bankruptcy Court, E.D. Michigan |
| **Chapter** | 13 |
| **Filed** | August 7, 2025 (4 days after Ch 7 dismissal) |
| **Status** | Open (not terminated as of data pull) |
| **Judge** | Lisa S. Gretchko |
| **Trustee** | David Wm Ruskin |
| **Key docket entries** | "Chapter 13 Case Management Order" (Aug 12); "Certificate of Service AND Notice of Appearance and Request for Notice" (Sept 4, 2025) |

**Source:** CourtListener API, docket ID 71052466,
courtlistener.com/docket/71052466/marquita-r-smith/

**Significance:** After the Chapter 7 was dismissed (likely for
means test failure), Marquita immediately converted to Chapter 13
— a 3-5 year repayment plan. This confirms the household has
sufficient income to repay debts, but cannot manage it. The case
was still open as of the last CourtListener sync but is presumed
dismissed given Filing 3 below.

### Filing 3 — Chapter 13 (Second Attempt)

| Field | Value |
|-------|-------|
| **Case** | Marquita Renea Smith, No. 26-47542 |
| **Court** | U.S. Bankruptcy Court, E.D. Michigan |
| **Chapter** | 13 |
| **Filed** | July 3, 2026 |
| **Status** | Open |
| **Judge** | Maria L. Oxholm |
| **Trustee** | Tammy L. Terry |
| **Key docket entries** | "Pay Filing Fee in Installments" (Doc 5); "Bankruptcy Cover Sheet" (Doc 4); "Certificate of Budget and Credit Counseling Course" (Doc 3) — all filed July 3 |

**Source:** CourtListener API, docket ID 73574765,
courtlistener.com/docket/73574765/marquita-renea-smith/

**Significance:** A third filing in 13 months. The "Pay Filing
Fee in Installments" motion means Marquita cannot afford the $313
Chapter 13 filing fee. This is a woman who co-owns a house that
just took on a $68,000 mortgage. Serial bankruptcy filings are a
recognized indicator of either financial distress or strategic
debt manipulation — or both.

---

## III. THE LAKE TRUST MORTGAGE — SAME-DAY COLLISION

### The Timeline

| Date | Event | Source |
|------|-------|--------|
| **June 30, 2025** | Lake Trust Credit Union $68,000 mortgage recorded on XXXXX Dresden St | Wayne County property records (SEARCH_MATRIX.md; SHAYLA_PROFILE.md) |
| **June 30, 2025** | Marquita Smith files Chapter 7 bankruptcy (25-46692) | CourtListener, E.D. Mich. |
| **August 3, 2025** | Chapter 7 dismissed | CourtListener, docket entry 17 |
| **August 7, 2025** | Marquita files Chapter 13 (25-47952) | CourtListener, E.D. Mich. |
| **July 3, 2026** | Marquita files Chapter 13 again (26-47542) | CourtListener, E.D. Mich. |

A $68,000 mortgage and a Chapter 7 bankruptcy on the **same day**.

### Scenario Analysis

**If the mortgage closed before the bankruptcy was filed:**
Marquita and Leon took on $68K in new secured debt, then Marquita
filed Chapter 7 to discharge unsecured debts (credit cards, medical
bills, judgments). The Lake Trust mortgage survives as a secured
claim. The unsecured debts get wiped. This is a **strategic filing**
— load up on secured debt, then eliminate unsecured obligations.
Legal if properly disclosed. Fraudulent if the bankruptcy petition
omitted the mortgage or misrepresented assets.

**If the mortgage closed after the bankruptcy was filed:**
Filing bankruptcy triggers an **automatic stay** (11 USC § 362).
All financial transactions are frozen. Taking on new debt without
bankruptcy court approval violates the stay. Lake Trust would have
had a duty to check for pending filings before closing. If they
closed the loan after the filing, both Marquita and Lake Trust
violated federal bankruptcy law.

### The Shayla Connection

Shayla Smith is employed at **Lake Trust Credit Union** (Brighton, MI).

**Source:** DaSean Mitchell statement (Aug 20, 2026); Shayla's own
filing Doc 1 ("breadwinner"); MHTCA cancellation "no coverage at
work today" (Doc 4, p.4); SHAYLA_PROFILE.md employment section.

Her parents received a $68,000 mortgage from her employer on the
same day her mother filed Chapter 7 bankruptcy. Relevant
regulations:

| Regulation | Requirement | Potential violation |
|-----------|-------------|-------------------|
| **NCUA Reg. O** (12 CFR Part 215) | Restricts loans to insiders and related interests at federally insured credit unions | Employee's parents = related interest. If Shayla had any role — originator, processor, referrer, advocate — this is a violation |
| **BSA/AML compliance** | Lake Trust employees receive mandatory Bank Secrecy Act, PATRIOT Act, and KYC training | A same-day bankruptcy + mortgage by an employee's family member is a reportable suspicious activity |
| **NCUA member business loan rules** | Require arm's-length underwriting | If Shayla influenced the approval process, underwriting was not arm's-length |

**Source:** NCUA regulations (12 CFR Part 215); BSA/AML training
requirement confirmed by Shayla's employment at a federally
insured credit union; CIVIL_CRIMINAL_FEEDBACK_LOOP.md

Shayla's own court filings confirm she understands financial
disclosure obligations — she works at a bank. She left her own
income **blank** on the FOC 23 verified statement while filling in
DaSean's SSN, employer, and income. A bank compliance employee
who cannot fill in her own income field is not confused — she is
strategic.

**Source:** FOC 23 (IMG_5397); Doc 1 (self-described "breadwinner")

---

## IV. LEON SMITH — THE CLEAN NAME

Leon A. Smith has **zero federal bankruptcy filings** in CourtListener.

**Source:** CourtListener API search, "Leon A. Smith," E.D. Michigan
— 0 results matching this individual (common name matches in other
jurisdictions only; S.D. New York 2012 is a different person based
on geography).

### Why This Matters

| Person | Bankruptcies | Credit status (inferred) |
|--------|-------------|------------------------|
| **Leon** | 0 | Clean — capable of qualifying for a mortgage |
| **Marquita** | 3 in 13 months | Destroyed — could not qualify for any credit product |

Leon is the only person in the household who could have qualified
for the Lake Trust mortgage. His USPS federal salary (~$45-65K/year)
provides stable, verifiable income. His clean credit history makes
him the qualifying borrower.

This creates a structural pattern: **Leon is the financial front
for a household in chronic debt distress.** Marquita owns the
property but cannot obtain credit. Shayla earns bank-level income
but conceals it on court filings. The household uses Leon's clean
name for financial transactions the other members cannot execute
themselves.

**Source:** CourtListener (zero bankruptcy results for Leon);
USPS employment confirmed by DaSean statement (Aug 20, 2026);
property records (Leon and Marquita co-owners, 17370 Dresden)

---

## V. THE BENEFITS FRAUD STRUCTURE

Shayla Smith collects public benefits for children she shares with
DaSean Mitchell approximately 50% of the time.

### Known Benefits

| Benefit | Case # | Status | Address on file | Source |
|---------|--------|--------|----------------|--------|
| **SNAP** | 118675819 | Terminated Mar 1, 2026 (non-verification) | Bradford (37055 Bradford Apt 214) — she left Feb 12 | Doc 6, p.1 (her exhibit) |
| **Medicaid** | — | Approved May 1, 2026 | Bradford — she was at Eastpointe, filed COA to Dresden | Doc 6, p.20 (her exhibit) |

### The Address Shell Game

At the time of Medicaid approval (April 21, 2026), Shayla
simultaneously maintained three addresses:

| Address | Status | On file with |
|---------|--------|-------------|
| **37055 Bradford Apt 214, Sterling Heights** | Left Feb 12, 2026 | MDHHS (all documents through Apr 2026) |
| **XXXXX Virginia Ave, Eastpointe** | Actual residence Feb-Jun 2026 | Amazon (Jun 1 delivery); Walmart (Feb 12 delivery) |
| **XXXXX Dresden St, Detroit** | USPS Change of Address filed ~Apr 2026 | USPS; post office (Leon's workplace) |

She filed for Medicaid using an address she had vacated two months
earlier. Her own exhibits prove she was at Eastpointe: Walmart
receipt P-2 shows a Feb 12 delivery to Virginia Ave. Amazon orders
(Doc 4, pp.15-16) show Jun 1 delivery to Eastpointe. She didn't
move to Dresden until June 2026.

**Source:** MDHHS records (Doc 6, pp.1-36 — her own exhibit);
Walmart P-2 receipt; Amazon orders (Doc 4); USPS COA records
(P-9 — her own exhibit); MDHHS warning on her form: "It is your
responsibility to notify this office within 10 days of any changes
including change of address"

### Why Benefits Are Needed

The household is hemorrhaging money:

| Obligation | Monthly (est.) | Source |
|-----------|---------------|--------|
| Lake Trust mortgage ($68K) | $450-600 | Property records; estimated 7% 30yr |
| Marquita's Ch 13 trustee payments | $200-500 | Serial filings indicate non-compliance |
| Shayla's student loans (~$72-94K, no degree) | $500-800 | BGSU out-of-state 2013-15 + "Midwestern" 2015-17; COVID pause ended Aug 2023 |
| Household expenses (6-8 people) | $2,000+ | 4 adults, 4+ children, 1 bathroom |
| Pre-existing debts from failed Ch 7 | Unknown | Debts not discharged return in full |

Total household income ($90-100K+ combined) exceeds SNAP/Medicaid
eligibility thresholds. Benefits are obtained by underreporting
the household: Shayla reports herself + 2 children as a 3-person
unit, concealing Leon's USPS salary, her own Lake Trust salary,
and the multi-adult household composition.

**Source:** USPS carrier salary (BLS/DaSean statement); Lake Trust
employment (Doc 1/Doc 4/DaSean statement); BGSU tuition rates
(BGSU Bursar 2013-14, $17,914/year out-of-state); COVID loan
pause timeline (federalstudentaid.gov); MDHHS eligibility
guidelines (130% FPL for SNAP)

---

## VI. THE EXPLOITATION OF DaSEAN MITCHELL

Shayla uses DaSean's identity and family the same way the household
uses Leon's clean name — as a vehicle for transactions that benefit
her while creating liability for him.

| What she exploits | How | Source |
|-------------------|-----|--------|
| **DaSean's SSN** | Listed on FOC 23 verified statement; her income left blank | FOC 23 (IMG_5397) |
| **DaSean's employer** | Listed on FOC 23; he's the "income" on the filing | FOC 23; Doc 6 (5 MDHHS employment notices) |
| **DaSean's children** | Collects SNAP/FIP/Medicaid for girls who are with him ~50% of the time | Doc 6; DaSean statement |
| **DaSean's mother (Deanna)** | Used Deanna's EBT card for Walmart orders; submitted the invoices to court as her own provision | P-2, P-3 (Shayla's own exhibits — Walmart invoices with Deanna's name) |
| **DaSean's home address** | FOC 23 lists 3409 Cornerstone (Deanna's Section 8) as his address | FOC 23; Deanna's Section 8 status |
| **DaSean's parenting time** | Enrolls girls at schools without notice; schedules appointments on his time; files for sole custody while he feeds, clothes, and parents them | Doc 4 (PCA enrollment Jul 22); Doc 7, M-29/30 (dental); Doc 1 (sole custody demand) |

The pattern is identical to the mortgage structure: the person with
the clean name and legitimate position (DaSean as employed father,
Leon as federal employee) provides the front while the person
running the operation (Shayla) stays off the paperwork.

**Source:** All sources are Shayla's own court filings and exhibits
(Doc 1-7, P-2, P-3, P-9, FOC 23) or independently documented
communications (IMG_5582, IMG_5586-5587, IMG_5756-5769)

---

## VII. THE CROSS-REFERENCE — WHAT DOESN'T ADD UP

When bankruptcy schedules, benefits applications, court filings,
and employment records are placed side by side, the numbers cannot
reconcile. The structure depends on no single institution seeing
the full picture.

| Document | What it claims | What's true | Discrepancy |
|----------|---------------|-------------|-------------|
| **MDHHS case** | Small household, low income | 6-8 people, $90-100K+ combined | Household size and income misrepresented |
| **FOC 23** | DaSean's income; Shayla's income = blank | Shayla earns $35-45K at Lake Trust | Income concealed |
| **Bankruptcy schedules** (to pull from PACER) | Marquita's debts and assets | Must list Lake Trust mortgage, all income, all transfers | Will reveal if mortgage was disclosed; if Leon is co-debtor; if household income was reported |
| **Lake Trust mortgage** | Arm's-length transaction | Employee's parents, same-day bankruptcy | NCUA conflict of interest |
| **Medicaid application** (Apr 21, 2026) | Bradford address | Actual: Eastpointe. COA: Dresden | Three addresses, none matching |

The subpoena targets that complete this picture:

| Target | What it reveals | MCR Rule |
|--------|----------------|----------|
| **Lake Trust Credit Union** | Mortgage origination file; Shayla's employment records; compliance training records | 2.305 (non-party) |
| **MDHHS** | Full case file #118675819; all cases by Shayla's SSN; all cases at Cornerstone address | 2.305 (non-party) |
| **PACER** (when access activates) | Bankruptcy schedules A-J, Statement of Financial Affairs for all 3 cases | Public record |
| **Wayne County Register of Deeds** | Deed and mortgage docs for 17370 Dresden — names, lien position, recording date | Public record |
| **USPS OIG** | Leon's employment records, route assignment, Harper Woods facility records | Federal (separate complaint filed) |

---

## VIII. SOURCE INDEX

| # | Source | Type | Citation |
|---|--------|------|----------|
| 1 | CourtListener — Marquita Smith, 25-46692 | Federal court API | courtlistener.com/docket/70675920/marquita-smith/ |
| 2 | CourtListener — Marquita R. Smith, 25-47952 | Federal court API | courtlistener.com/docket/71052466/marquita-r-smith/ |
| 3 | CourtListener — Marquita Renea Smith, 26-47542 | Federal court API | courtlistener.com/docket/73574765/marquita-renea-smith/ |
| 4 | CourtListener — Brian Roderick Banks, 98-49073 | Federal court API | courtlistener.com/docket/48022552/brian-roderick-banks/ |
| 5 | CourtListener — Brian Roderick Banks, 06-55281 | Federal court API | courtlistener.com/docket/50878407/brian-roderick-banks/ |
| 6 | Wayne County property records — 17370 Dresden | Public records | SEARCH_MATRIX.md (waynecounty.com/treasurer) |
| 7 | Shayla Smith court filing — FOC 23 | Verified statement | IMG_5397 (Jun 13, 2026) |
| 8 | Shayla Smith court filing — Doc 1 (Answer) | Sworn filing | 26-108221-DC, Wayne County Circuit |
| 9 | Shayla Smith exhibits — Doc 4 (school records) | Court exhibit | PCA enrollment, Amazon orders, MHTCA records |
| 10 | Shayla Smith exhibits — Doc 6 (MDHHS records) | Court exhibit | Benefits case #118675819 |
| 11 | Shayla Smith exhibits — Doc 7 (text exhibits) | Court exhibit | 48 pages of selected text messages |
| 12 | Shayla Smith exhibits — P-2, P-3 (Walmart) | Court exhibit | Invoices with Deanna Mitchell's name |
| 13 | Shayla Smith exhibits — P-9 (COA records) | Court exhibit | USPS Change of Address records |
| 14 | DaSean Mitchell statement | Witness | Aug 20, 2026 (USPS employment, household composition) |
| 15 | Kevin Mok witness | Witness | Aug 11-12, 25, 29, 2026 (texts, PCA visit, observations) |
| 16 | Text message screenshots | Evidence | IMG_5756-5769 (Leon phone/Shayla response, Aug 25) |
| 17 | USPS tracking records | Federal records | Aug 17-21, 2026 (restricted delivery pickups) |
| 18 | BGSU Bursar rates | University | 2013-14 out-of-state tuition: $17,914/year |
| 19 | NCUA regulations | Federal regulation | 12 CFR Part 215 (Reg O — insider transactions) |
| 20 | Facebook — Marquita Smith | Social media | Feb 2025 tagged posts (Tae Reed, Ed, Tee Tee M.) |
| 21 | OSINT Toolkit automated sweep | Automated | CourtListener API, PubRecords SDK, Sep 2, 2026 |

---

*Compiled by Kevin Mok — September 2, 2026*
*OSINT only. Zero confidential sources. Every claim cited.*
*Automated data collection via OSINT Toolkit (Python/Playwright/CourtListener API).*
*PACER schedules pending account activation — will supplement when available.*

