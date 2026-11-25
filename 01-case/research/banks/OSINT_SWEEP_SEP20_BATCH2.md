# OSINT SWEEP — BATCH 2 (Sep 20, 2026)
## Task 1: Eventbrite Deep Scrape (Brian Banks / Organizer 47714438313)
## Task 2: MacDowell Check Register Deep Mining (FY 2023–24)

**Analyst note:** Primary check data pulled from MacDowell’s public PDF `CheckDetail-2023-24.pdf` (posted Feb 10, 2025). Local `screenshots-financial/` folder reviewed — **no check-register screenshots present** (campaign finance, USAA, process-server, Wayne Co. tax receipt, PCA budget). `case-docs/` had **no check-register PDFs** at scrape time. Clutch Justice / Free Press captures used for cross-check only.

**Machine-readable extracts (this session):**
- `01-case/research/banks/_tmp_checkdetail.txt` — full PDF text (36 pages)
- `01-case/research/banks/_checkdetail_final.json` — parsed transactions (see coverage caveats)
- `01-case/research/banks/_eventbrite_batch2_full.json` — Eventbrite meta/OG tags

---

# TASK 1 — EVENTBRITE: BRIAN BANKS ORGANIZER + ALL 6 EVENTS

## A. Organizer profile

| Field | Value | Source |
|-------|--------|--------|
| **Organizer ID** | `47714438313` | Eventbrite |
| **Profile URL** | https://www.eventbrite.com/o/47714438313 | Live scrape Sep 20, 2026 |
| **Display name** | Brian Banks | Profile / all event pages |
| **Followers** | **212** | Profile metrics |
| **Hosting tenure** | **3 years** | Profile metrics |
| **Total events listed** | **6** | Profile metrics (all past as of Sep 20, 2026) |
| **Total attendees (platform-reported)** | **~1.1k** | Profile metrics |
| **Upcoming events** | **0** (“Nothing planned right now”) | Profile Past tab |
| **Bio / social links** | Empty (no bio text, no linked socials in JSON) | `__NEXT_DATA__` organizer block |
| **Verified / Top Organizer** | Not shown as verified badge on public profile | Browser scrape |

**Past events order (newest first on profile):**
1. Michigan CBC Reception 2026 — Kitchen + Kocktails DC — **Sales ended**
2. Monday Night Praise 2026 — Greater Emmanuel COGIC — door tickets
3. PCA Black Tie Gala 2026 — Elevate One Campus Martius — **Sold out**
4. Michigan CBC After Glow 2025 — Grand Hyatt DC — sales ended
5. Michigan CBC Party 2024 — Grand Hyatt — **Sold out** / limited door
6. Michigan CBC w/ Chubb Rock 2023 — Grand Hyatt — door tickets

---

## B. Event 1 — 2026 Michigan CBC Reception & Party

| Field | Detail |
|-------|--------|
| **URL** | https://www.eventbrite.com/e/tickets-at-the-door-michigan-cbc-reception-party-tickets-at-the-door-tickets-1998927506983 |
| **Full title** | Tickets at the Door! -Michigan CBC Reception & Party - TICKETS AT THE DOOR |
| **Organizer** | Brian Banks (212 followers; same 6 events / 1.1k attendees on event page) |
| **Status** | **EVENT ENDED** / Sales ended (Sep 20, 2026 view) |
| **Date & time** | **Friday, Sep 18, 2026, 7:00 PM – 11:59 PM** (4h 59m) | Meta: `event:start_time` / `event:end_time` |
| **Venue** | **Kitchen + Kocktails By Kevin Kelley - DC** |
| **Address** | **1300 I Street Northwest, Washington, DC 20005** |
| **Ticket pricing** | **From $55.20** (organizer past-events card); door-focused listing (“TICKETS AT THE DOOR”) — **no multi-tier breakdown visible** after sales closed |
| **Refund policy** | **No refunds** |
| **Category tags** | Washington **Business** parties / parties |

### Description (full Overview text, expanded Sep 20, 2026)

> CBC Week Reception: Celebrating Michigan Democratic nominees & honoring Donovan McKinney’s historic 13th District nomination. Live DJ & Food  
>  
> This year's reception, themed **“A Seat at the Table: Celebrating Historic Candidacies and Collective Progress,”** will take place during Congressional Black Caucus Week, when Black political leadership and representation are at the forefront of our national conversation.  
>  
> The evening will celebrate **all Michigan's Democratic nominees** and recognize leaders who have advanced equity, opportunity, and public service throughout our state. We will also provide **special recognition to Hon. Donovan McKinney** for his historic Democratic nomination in Michigan's 13th Congressional District. **Live DJ, Free Food & Open Bar (2 hours)**, and more.

### Honorees / featured names
- **Honoree (explicit):** **Hon. Donovan McKinney** — MI-13 Democratic nominee  
- **Scope:** All Michigan Democratic nominees (2026 cycle)  
- **Entertainment:** Live DJ; **2-hour open bar**; complimentary food  

### Attendance / capacity
- Platform shows **ended** sales; **no public capacity number**  
- Organizer aggregate: **1.1k attendees across 6 events** (not per-event)

### Flyer / image (Eventbrite CDN)
- OG image: `cdn.evbuc.com/.../1192457300/864959950233/1/original.20260902-103037` (promotional graphic — upscale reception / CBC branding)

### Sponsors
- **None listed** on Eventbrite page

---

## C. Event 2 — 2024 Michigan CBC Party (SOLD OUT)

| Field | Detail |
|-------|--------|
| **URL** | https://www.eventbrite.com/e/michigan-cbc-party-sold-out-limited-tickets-at-the-door-tickets-999744000217 |
| **Full title** | Michigan CBC Party - **SOLD OUT!** Limited tickets at the Door |
| **Date & time** | **Fri, Sep 13, 2024, 7:00 PM – 11:30 PM** (4h 30m) |
| **Venue** | **Grand Hyatt Washington** |
| **Address** | **1000 H Street Northwest, Washington, DC 20001** |
| **Ticket price** | **From $55.20** |
| **Attendance signal** | **SOLD OUT** (online); **limited tickets at the door** |
| **Refund policy** | No refunds |

### Description
- Short: *“Come enjoy Recording Artist **Dave Hollister** while celebrating several Michigan **Community Heroes** at the 2024 Michigan CBC Celebration.”*
- Expanded Overview (Sep 20, 2026):
  - **Honorary hosts:** **Congresswoman Debbie Dingell**, **Congresswoman Rashida Tlaib**
  - **2024 Community Hero honorees:** **Hon. Sarah Anthony**, **Mr. Marloshawn Franklin**, **Ms. Denise Brooks Williams**, **Ms. Terry Campbell**, **Mr. Jason Tinsley**
  - **Entertainment:** **Dave Hollister** & **DJ Jay Claxton**

### Co-hosts / featured
- U.S. Reps **Dingell** & **Tlaib** (honorary hosts)  
- Recording artist **Dave Hollister**; DJ **Jay Claxton**

### Flyer / image
- `cdn.evbuc.com/.../831059099/.../original.20240820-230132`

### Sponsors
- None on Eventbrite

---

## D. Event 3 — 2023 Michigan CBC Party w/ Chubb Rock

| Field | Detail |
|-------|--------|
| **URL** | https://www.eventbrite.com/e/michigan-cbc-party-wchubb-rock-tickets-available-at-the-door-tickets-712493987697 |
| **Full title** | Michigan CBC Party w/**Chubb Rock** - Tickets Available At The Door |
| **Date & time** | **Fri, Sep 22, 2023, 7:00 PM** — meta end **`2023-09-23`** (multi-session / next-day end) |
| **Venue** | **Grand Hyatt Washington** |
| **Address** | **1000 H Street Northwest, Washington, DC 20001** |
| **Ticket price** | **From $55.20** |
| **Attendance** | Door tickets available (not marked sold out) |

### Description (OG)
> The Michigan CBC Reception serves as a platform to celebrate & highlight the achievements & contributions of our Michigan residents.

### Featured entertainment
- **Chubb Rock** (headline in title)

### Flyer / image
- `cdn.evbuc.com/.../599852799/.../original.20230917-182004`

---

## E. Event 4 — 2025 Michigan CBC After Glow Party

| Field | Detail |
|-------|--------|
| **URL** | https://www.eventbrite.com/e/michigans-cbc-after-glow-party-gen-admission-tickets-only-at-door-tickets-1646216841889 |
| **Full title** | Michigan's CBC After Glow Party - **GEN ADMISSION TICKETS Only at Door** |
| **Date & time** | **Fri, Sep 26, 2025, 7:00 PM – 11:59 PM** |
| **Venue** | **Grand Hyatt Washington** |
| **Address** | **1000 H Street Northwest, Washington, DC 20001** |
| **Ticket price** | **From $56.15** |
| **Tier note** | “Gen admission” / door-only framing |

### Description (OG)
> Join us @ the 2025 Michigan Congressional Black Caucus Reception/After Glow honoring leaders, community impact, & featuring **R&B singer Tweet**

### Honorees (external corroboration)
- Prior OSINT / press: **Sherry Gay-Dagnogo** honored at 2025 event (not in OG snippet — verify against flyer in CDN image)

### Flyer / image
- `cdn.evbuc.com/.../1111517483/.../original.20250902-122511`

---

## F. Event 5 — 2026 PCA Inaugural Black Tie Gala

| Field | Detail |
|-------|--------|
| **URL** | https://www.eventbrite.com/e/inaugural-black-tie-gala-purpose-charter-academy-school-for-law-pub-svc-tickets-1979571244882 |
| **Full title** | Inaugural Black Tie Gala: **Purpose Charter Academy School for Law & Pub Svc** |
| **Date & time** | **Sat, May 16, 2026, 6:00 PM** (meta; confirm end on page) |
| **Venue** | **Elevate at One Campus Martius**, Detroit, MI |
| **Ticket price** | **From $161.90** (~$162 with fees) |
| **Status** | **SOLD OUT** on organizer profile |
| **Refund** | Not re-scraped; assume standard Eventbrite policy |

### Description (OG)
> Dress to impress & celebrate the launch of Purpose Charter Academy School for Law & Public Service at our Black Tie Inaugural Gala!

### Branding / sponsors
- **Purpose Charter Academy** / **Brian Banks** school brand throughout  
- No third-party sponsors listed

### Flyer / image
- `cdn.evbuc.com/.../1174843619/.../original.20260114-144744`

### IRS / DOE relevance
- Ticket revenue destination **unreported on Eventbrite** (PCA vs Purpose Group LLC vs Banks personally)

---

## G. Event 6 — 2026 Monday Night Praise

| Field | Detail |
|-------|--------|
| **URL** | https://www.eventbrite.com/e/monday-night-praise-tickets-available-at-the-door-tickets-1985098248298 |
| **Full title** | Monday Night Praise - TICKETS AVAILABLE AT THE DOOR |
| **Date & time** | **Mon, Aug 10, 2026, 7:00 PM** |
| **Venue** | **Greater Emmanuel Institutional Church of God in Christ**, Detroit |
| **Ticket price** | **From $28.52** |
| **Attendance** | Door tickets |

### Description (OG)
> Join us for an unforgettable evening of powerful gospel music and worship in support of **metro Detroit school children & schools**!

### Purpose branding
- “Purpose” / school-children framing ties to **Banks’ charter schools** without naming PCA/MacDowell on OG text

---

## H. Eventbrite financial summary (investigative)

| Question | Finding |
|----------|---------|
| **Gross ticket revenue** | Not public; requires **Eventbrite subpoena** or organizer payout records |
| **Rough ceiling (CBC years)** | 4× DC events × ~$55 × portion of 1.1k total attendees — **well below** open-bar + Hyatt/Kitchen costs if attendance is in hundreds |
| **Entity receiving funds** | **Unknown** — organizer is natural person “Brian Banks,” not Purpose Group LLC or either charter |
| **Political vs charitable** | CBC events are ** partisan networking** (Democratic nominees, Members of Congress hosts) hosted by **convicted-felon charter operator** |

---

# TASK 2 — MACDOWELL CHECK REGISTER (FY 2023–24)

## A. Source document

| Item | Detail |
|------|--------|
| **Title** | MacDowell Preparatory Academy — **Check Detail** |
| **Period** | **July 2023 – June 2024** |
| **Generated** | Monday, Feb 10, 2025, 05:42 PM ET |
| **URL** | https://macdowellprep.com/wp-content/uploads/2025/02/CheckDetail-2023-24.pdf |
| **Accounts shown** | Bank of America operating/savings + **Credit Union One – Operations** (manual checks) |
| **Critical gap** | **Bulk ESP pass-through to Purpose Group Michigan LLC (~$4.28M)** appears on **personnel/ESP reports**, not as itemized payee lines in this check extract — treat this register as **direct/discretionary disbursements**, not full $5.9M expenditure universe |

## B. Clutch Justice cross-check (Rita Williams, Sep 13, 2026)

Corroborated from **same public check detail**:
- **$13,970** gift-card cluster (FY 2023–24)  
- **$1,000** to **Rafeal Camper** — memo **“Prayers to you and your fam”**  
- **$23,147+** to **Gregory M. Meihn** across FY2018–19 and FY2023–24 (partial years in PDF)  
- **Superintendent pay:** **$150,000** base / **$164,070** total compensation (separate transparency PDF — not duplicated in every check line)

---

## C. Gift-card & operator self-dealing (IRS CI priority)

| Date | Check # | Payee line | Memo | Amount |
|------|---------|------------|------|--------|
| 08/08/2023 | 10056 | **Brian Banks** | Staff Gift Cards | **$1,890.00** |
| 11/20/2023 | 1026 | **Brian Banks** | Gift cards for travel | **$400.00** |
| 12/20/2023 | 1033 | **Brian Banks** | Staff gifts cards | **$9,945.00** |
| 01/11/2024 | 1035 | **Brian Banks** | Reimbursement | **$265.00** |
| 06/24/2024 | 10044 | **Brian Banks** | Staff Gift Cards, **NCSC24** | **$1,470.00** |
| 03/22/2024 | 10002 | **Chalcee Norwood** | Reimbursement for Gift Cards/Easter Egg Hunt | **$245.00** |
| 01/24/2024 | 1040 | **Rafeal Camper** | **Prayers to you and your fam** | **$1,000.00** |

**Gift-card subtotal (Banks + Norwood gift memo):** **$14,215.00**  
**Clutch headline $13,970:** matches Banks-only gift lines (**$13,970**) — Norwood **$245** is adjacent pattern.

### Who approved? Reported as compensation?
- Checks drawn on **school accounts** with **Brian Banks** as payee on gift lines → **operator self-approval** appearance  
- **No board resolution** or gift-card recipient schedule in public transparency bundle  
- **Board treasurer (budget signer):** **Artesia M. Washington** (per amended budget PDFs) — **no evidence** she approved individual $9,945 December gift check  
- **MacDowell Board Chair:** **Judge Tenisha Yancey** — governance conflict; **Chalcee Norwood** may relate to **Yancey family** (verify — **Chalena** Yancey is PCA school leader per federal packet)  
- **W-2 / 1099 reporting:** Gift cards to staff are generally **taxable compensation**; **no public 1099 schedule** for $9,945 single check  
- **NCSC24** memo ties **$1,470** to **National Charter Schools Conference** — possible legitimate PD or **personal travel slush**

---

## D. Gregory M. Meihn (legal) — FY 2023–24 lines in this PDF

| Date | Ref | Amount | Memo |
|------|-----|--------|------|
| 01/17/2024 | Bill pay 10173 | **$4,000.00** | (vendor bill) |
| 06/13/2024 | Bill pay 10040 | **$647.20** | |
| 06/26/2024 | Check 10046 | **$5,000.00** | **2024 Attorney Retainer Fee** |

**FY 2023–24 Meihn in this extract:** **$9,647.20**  
**Clutch “$23,147+”:** includes **FY2018–19** payments ($3k + $2k + $6k documented in prior OSINT) + later cycles **not in this PDF**.

---

## E. Network-adjacent / insider-pattern payees (flagged)

| Payee | FY23–24 total (register) | Flag rationale |
|-------|---------------------------|----------------|
| **Brian Banks** (gift/reimb.) | **$13,970** | **Superintendent + payee** — classic self-dealing |
| **Rafeal Camper** | **$1,000** | Non-vendor memo; **no school purpose** |
| **Martin Luna** | **$70,333.34** | Large individual payments — **CMO/payroll proxy?** (verify role) |
| **Raymond Ankrum** | **$1,847.67** | Leadership contractor (prior MacDowell admin) |
| **Lorilyn K. Coggins** | **~$18,000–22,000** | Repeated **$2,000** bill payments — insider contractor pattern |
| **GM Equity Development** | **~$25,700+** | Facilities; **“Equity”** in name — verify ownership (not Inner Link, but flag) |
| **Detroit Athletic Club** | **~$1,694** | **Private club** charges on school checks |
| **Chalcee Norwood** | **$245** (+ possible other lines) | Gift reimbursement — **Yancey network** research target |
| **Yecart Accounting Services, LLC** | **~$50,000** ($5k×~10) | Recurring bookkeeping — **who owns Yecart?** |
| **Inner Link / Holland / Purpose Group / Perkins** | **No exact payee match** in check lines | **ESP bulk** likely off this register |

**Not found:** Joseph Holland, Inner Link Graphics, Todd Perkins, or Purpose Group LLC as named payees in this check PDF (consistent with **ESP shell** structure).

---

## F. Top payees by aggregate (deduped line parse — 247 unique names)

**Parsed disbursement lines (includes bill-pay + checks + card expenditures in PDF text): ~$1.78M summed lines** — use as **relative ranking**; some QuickBooks export lines **duplicate** across wrapped rows. **Top vendors by merged name:**

| Rank | Payee (normalized) | Approx. FY23–24 total | Notes |
|------|---------------------|----------------------|--------|
| 1 | **The Detroit Institute for Children** | **~$183,448** | SPED / related services |
| 2 | **Macro Connect, Inc.** (+ monthly serv) | **~$165,000+** | IT / E-rate / managed services — **recurring** |
| 3 | **ABM** | **~$93,150+** | Janitorial / facilities — **~$10,350/mo** pattern |
| 4 | **Martin Luna** | **$70,333.34** | Two large checks — **payroll intermediary?** |
| 5 | **Imagine Learning LLC** | **~$67,180** | Curriculum |
| 6 | **DTE Energy** | **~$77,000+** (multiple IDs) | Utilities |
| 7 | **Kendall Hunt Publishing** | **~$50,323** | Curriculum |
| 8 | **Yecart Accounting Services** | **$50,000** | **$5,000** checks — **monthly** |
| 9 | **Matrix Mechanical LLC** | **~$46,900** | HVAC / mechanical |
| 10 | **EMC Insurance** | **~$35,315+** | Property/liability insurance |
| 11 | **City of Detroit – Property Tax** | **$33,015.15** | Tax |
| 12 | **School Specialty** | **~$28,357** | Supplies |
| 13 | **Student Transportation Services** | **~$28,146** | Busing |
| 14 | **DR4 Technologies** | **~$49,805** | Tech vendor |
| 15 | **GM Equity Development** | **~$25,700+** | Facilities / equity projects |
| 16 | **Industry Specific Solutions** | **Many ACH lines** | HVAC / mechanical invoices |
| 17 | **Hoekstra Leasing, LLC** | **~$16,352** | Vehicle/bus leasing |
| 18 | **Alan C. Young & Assoc.** | **~$15,725** | Professional services |
| 19 | **Detroit Regional Chamber** | **$4,207.50** | Membership / networking |
| 20 | **National Charter Schools Institute** | **~$2,300+** | Conference / membership |

*(Full alpha list of 247 payees: see `_checkdetail_final.json` → `all_payees_alpha` — verify amounts before legal filing.)*

---

## G. Spending by category (investigator model)

| Category | Est. share | Examples |
|----------|------------|----------|
| **Special ed & student services** | High | Detroit Institute for Children, Urban Academy |
| **IT / telecom** | High | Macro Connect, Presidio/DR4, PowerSchool, Comcast, GoTo |
| **Facilities / O&M** | High | ABM, Matrix Mechanical, Industry Specific HVAC, water/sewer |
| **Curriculum & supplies** | High | Imagine Learning, Kendall Hunt, Houghton Mifflin, Savvas, School Specialty |
| **Transportation** | Medium | Student Transportation Services, Hoekstra Leasing |
| **Insurance & taxes** | Medium | EMC, US Bank fees, Detroit property tax |
| **Professional & governance** | Medium | Yecart, Meihn, Alan C. Young, National Charter Schools Institute, Detroit Regional Chamber |
| **Events / catering / club** | Medium | Detroit Athletic Club, Chef JA Catering, John Arnold caterer, Blake’s Big Apple, back-to-school festival vendors |
| **Operator self-dealing** | **Critical** | Banks gift cards, Camper payment |
| **ESP / CMO pass-through** | **Not in this PDF** | Purpose Group **~$4.28M** on ESP report |

---

## H. Unusual memos & patterns (audit triggers)

| Pattern | Example | Risk |
|---------|---------|------|
| **Gift cards to superintendent payee** | $9,945 single check to **Brian Banks** | **Embezzlement / 1099 fraud / kickbacks** |
| **Personal-sounding memo** | **“Prayers to you and your fam”** → Camper | **Private inurement** |
| **Luxury club** | Detroit Athletic Club **$948 + $746** | **Non-educational** |
| **Reimbursement chains** | Ricardo Silva Costco; multiple **Reimbursement** checks | Weak documentation |
| **NCSC travel gift cards** | $1,470 **NCSC24** | Conflate PD with **cash-equivalent** |
| **Back-to-school festival cluster** | Chef JA **$2,492**, bounce house, game bus | Validate **public purpose** |
| **Repeated $5,000 Yecart** | Monthly accounting | Related-party bookkeeping? |
| **Large one-shot construction** | Michigan Recreational Construction **$89,225** (Aug 2023) | Capital vs operating classification |
| **Manual CU checks** | Credit Union One operations checks **1001–1060+** | Second payment rail — **less board visibility** |

---

## I. Recurring vendors — legitimacy checklist

| Vendor | Recurrence | Legitimacy assessment |
|--------|------------|------------------------|
| **ABM** | ~$10,350/month | Legitimate **janitorial** IF RFP on file — amount high for ~362 students |
| **Yecart** | $5,000/month | Normal **bookkeeping** rate IF arm’s-length — **need ownership** |
| **Macro Connect** | Monthly + E-rate | Common **charter IT** vendor — verify **conflict-free bidding** |
| **Industry Specific Solutions** | Frequent ACH | HVAC — legitimate; watch **duplicate billing** |
| **EMC Insurance** | Monthly | Normal |
| **DTE / Comcast / GoTo** | Monthly | Normal utilities |
| **Martin Luna** | **$34,666 + $35,666** | **Abnormal** as named individual — likely **hidden payroll** |
| **Brian Banks gift cards** | Episodic | **Not legitimate** without board approval & tax reporting |

---

## J. Banks salary vs check register (Clutch / transparency PDF)

| Component | Amount |
|-----------|--------|
| Base salary | **$150,000** |
| Employer FICA | $11,475 |
| Employer health | $2,595 |
| **Total reported comp** | **$164,070** |
| Note | Staff paid via **third-party HR/payroll** (Purpose Group pipeline) — **salary may not appear** as “Brian Banks” payroll in this check detail |

**ESP gap (prior OSINT):** Purpose Group billed **~$4.285M**; ESP staff report **~$3.937M** — **~$348k** unexplained **management fee** layer.

---

## K. Evidence gaps for IRS CI / subpoena list

1. **Eventbrite payout records** — all 6 events (merchant of record, bank account)  
2. **Gift card purchase receipts** — itemizing **recipients** for $9,945 / $1,890 / NCSC $1,470  
3. **Board minutes** — approval of gift cards, Camper payment, DAC membership  
4. **Purpose Group LLC invoices** — itemized pass-through (not in check PDF)  
5. **1099-NEC/MISC** filings for Banks, Luna, Ankrum, Coggins, Norwood  
6. **2024–25 Check Register** (listed on transparency page — not yet in repo)  
7. **Yecart, Martin Luna, Rafeal Camper** — contracts & W-9s  

---

## L. Local evidence folder review (`02-evidence/screenshots-financial/`)

| File | Content | Relevance to Task 2 |
|------|---------|---------------------|
| Screenshot 2026-09-14 083508.png | **Bank on Banks** late filing fees (~$12.5k outstanding) | Campaign finance — **Holland treasurer** pattern |
| Screenshot 2026-09-14 083520.png | Bank on Banks **$0** campaign statements | Non-reporting |
| Screenshot 2026-09-14 083529.png | Banks **2016–2017 fundraisers** (Bootleggers GP; Sinbad’s Detroit) | Historical **event revenue** |
| Screenshot 2026-09-12 102842/102850.png | **PCA FY26–27 budget** (Latisha Johnson treasurer signature) | PCA finances — not MacDowell register |
| Screenshot 2026-09-08 * | NMLS **Shayla Smith** / Lake Trust | Parallel **Smith** financial thread — not MacDowell |
| Screenshot 2026-09-08 203936.png | Wayne Co tax receipt → **Lake Trust** | Property tax payment chain |
| Screenshot 2026-08-28 202204.png | Process server invoice | Litigation cost — not school |

---

## M. Free Press expose (`FREEP_BANKS_EXPOSE_JULY2022.md`) — tie-in

- **Pattern:** bad checks, hidden money, charity irregularities → **consistent** with gift-card self-dealing and **undisclosed Eventbrite revenue**  
- **Political patrons** (Evans, Sabree, Duggan network) align with **CBC honoree strategy** (McKinney, Gay-Dagnogo, Community Heroes)

---

# SYNTHESIS — FEDERAL REFERRAL HOOKS

| Agency | Theory | This batch’s best evidence |
|--------|--------|----------------------------|
| **IRS CI** | **Tax fraud / unreported income** | $13,970+ gift cards; Eventbrite **1.1k attendees × ticket prices**; Camper **$1k** |
| **IRS CI** | **Excessive compensation / inurement** | Banks payee on gift checks while **$164k** reported salary |
| **DOE OIG** | **Misuse of charter funds** | DAC, gift cards, ** partisan CBC events** branded with school operator |
| **FBI public corruption** | **Political access** | CBC events with **Members of Congress** hosts + **Democratic nominee** honorees |
| **FinCEN** | **Unexplained payees** | Camper, Luna, cash-equivalent gift cards |

---

*Prepared: Sep 20, 2026 — Eventbrite live scrape + MacDowell CheckDetail-2023-24 PDF full text mining.*  
*Supporting JSON/text artifacts in `01-case/research/banks/_tmp_*` and `_checkdetail_final.json`.*
