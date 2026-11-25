# CASE REGISTRY — Relational Index

All case numbers, parties, judges, and key dates in one place.
Documents reference cases by `case_id` — never duplicate this data.

## CASE NUMBER FORMATS

| Type | Canonical Format | Example | Notes |
|------|-----------------|---------|-------|
| Civil (Ingham) | `2026-XXXX-CZ` | `2026-4349-CZ` | Full year, no leading zeros |
| PPO (Ingham) | `26-0000004XXX-PP/PH` | `26-0000004432-PP` | 2-digit year + 10-digit serial. NO hyphen after zeros. |
| Custody (Wayne) | `26-XXXXXX-DC` | `26-108221-DC` | |
| Shorthand (informal) | `Case 4349` / `26-4435-PH` | — | OK in internal docs, NOT in filings |

**Legacy formats (do NOT use):** `26-000004349-CZ`, `4301-DM`, `26-000000-4432-PP`

---

## CASES

| case_id | court | case_no | caption | judge | type | status |
|---------|-------|---------|---------|-------|------|--------|
| CIV-BANKS | Ingham 30th Circuit | 2026-4349-CZ | Mok v. Banks et al. | Stokes | Civil — UPL/Fraud | Defendants: Banks, Holland, Tracye Ellis (amended). No answer. Default deadline Oct 6. Long-term — Kevin not settling. |
| CIV-SMITHS | Ingham 30th Circuit | 2026-4301-CZ | Mok v. Smith et al. | Stokes | Civil — Damages | Defendants: 4 Smiths + Banks (amended in). No answer. Default deadline Oct 7. Resolves when custody resolves. |
| PPO-SHAYLA | Ingham 30th Circuit | 26-0000004432-PP | Mitchell v. Shayla Smith | Koenig | PPO — Domestic | STRONGEST. Reasonable cause found. Hearing Sep 29. |
| PPO-MARQUITA | Ingham 30th Circuit | 26-0000004433-PH | Mitchell v. Marquita Smith | Koenig | PPO — Stalking | Hearing Sep 29. |
| PPO-SIMONE | Ingham 30th Circuit | 26-0000004434-PH | Mitchell v. Simone Smith | Koenig | PPO — Stalking | Hearing Sep 29. |
| PPO-BANKS | Ingham 30th Circuit | 26-0000004435-PH | Mitchell v. Brian Banks | Koenig | PPO — Stalking | 7-channel service attempted Sep 18. Hearing Sep 29. |
| PPO-LEON | Ingham 30th Circuit | 26-0000004436-PH | Mitchell v. Leon Smith | Koenig | PPO — Stalking | Leon text: "see you in court." Hearing Sep 29. |
| PPO-KEVIN | Ingham 30th Circuit | 26-0000004437-PH | Mok v. Banks | Koenig | PPO — Stalking | Kevin's PPO. Hearing Oct 20. |
| CUSTODY | Wayne 3rd Circuit | 26-108221-DC | Smith v. Mitchell | Triplett | Custody/Domestic | CMC Oct 9. Venue transfer pending. |
| PPO-WAYNE | Wayne 3rd Circuit | (pending) | Smith v. Mok | (pending) | PPO — Retaliatory | Shayla's retaliatory PPO against Kevin. Filed but NOT SERVED — Kevin notified of filing only. No deadline until served. Assume Shayla holding service vindictively. Kevin can appear whenever. |

---

## PARTIES

| party_id | name | role | cases |
|----------|------|------|-------|
| KEVIN | Kevin Mok | Plaintiff (CIV); Witness+Expert (PPO, CUSTODY); Petitioner (PPO-KEVIN); Respondent (PPO-WAYNE) | CIV-BANKS, CIV-SMITHS, PPO-* (witness+expert+auth rep), CUSTODY (witness+expert), PPO-KEVIN (petitioner), PPO-WAYNE (respondent) |
| DASEAN | DaSean Mitchell | Petitioner (PPO); Defendant/Counter-plaintiff (CUSTODY) | PPO-SHAYLA, PPO-MARQUITA, PPO-SIMONE, PPO-BANKS, PPO-LEON, CUSTODY |
| BANKS | Brian Banks | Defendant (CIV-BANKS, CIV-SMITHS — amended in); Respondent (PPO-BANKS, PPO-KEVIN) | CIV-BANKS, CIV-SMITHS, PPO-BANKS, PPO-KEVIN |
| SHAYLA | Shayla Smith | Defendant (CIV-SMITHS); Respondent (PPO-SHAYLA); Plaintiff (CUSTODY, PPO-WAYNE) | CIV-SMITHS, PPO-SHAYLA, CUSTODY, PPO-WAYNE |
| LEON | Leon Smith | Defendant (CIV-SMITHS); Respondent (PPO-LEON) | CIV-SMITHS, PPO-LEON |
| MARQUITA | Marquita Smith | Defendant (CIV-SMITHS); Respondent (PPO-MARQUITA) | CIV-SMITHS, PPO-MARQUITA |
| SIMONE | Simone Smith | Defendant (CIV-SMITHS); Respondent (PPO-SIMONE) | CIV-SMITHS, PPO-SIMONE |
| HOLLAND | Joseph Holland Jr. | Defendant (CIV-BANKS) | CIV-BANKS |
| ELLIS | Tracye Ellis | Defendant (CIV-BANKS — amended in) | CIV-BANKS |

## KEVIN-DASEAN RELATIONSHIP

> **Not biological brothers.** Best friends and fellow U.S. Army veterans who served together.
> Kevin refers to DaSean as "brother" — bond forged in service, not blood.

### Kevin's Roles Per Case

| case_id | court | kevin_role | role_type | appears | files_on_behalf |
|---------|-------|------------|-----------|---------|-----------------|
| CIV-BANKS | Ingham (Stokes) | **Plaintiff** | party — pro se | in person | self |
| CIV-SMITHS | Ingham (Stokes) | **Plaintiff** | party — pro se | in person | self |
| PPO-SHAYLA | Ingham (Koenig) | Authorized rep + fact witness + expert witness | non-party representative | in person | DaSean (petitioner appears in person) |
| PPO-MARQUITA | Ingham (Koenig) | Authorized rep + fact witness + expert witness | non-party representative | in person | DaSean |
| PPO-SIMONE | Ingham (Koenig) | Authorized rep + fact witness + expert witness | non-party representative | in person | DaSean |
| PPO-BANKS | Ingham (Koenig) | Authorized rep + fact witness + expert witness | non-party representative | in person | DaSean |
| PPO-LEON | Ingham (Koenig) | Authorized rep + fact witness + expert witness | non-party representative | in person | DaSean |
| PPO-KEVIN | Ingham (Koenig) | **Petitioner** | party — pro se | in person | self |
| CUSTODY | Wayne (Triplett) | Fact witness + expert witness | non-party witness | in person | DaSean (defendant/counter-plaintiff) |
| PPO-WAYNE | Wayne (pending) | **Respondent** | party — pro se | in person | self (defending) |

### DaSean's Roles Per Case

| case_id | court | dasean_role | appears | constraint |
|---------|-------|-------------|---------|------------|
| PPO-SHAYLA thru PPO-LEON | Ingham (Koenig) | **Petitioner** | in person (Sep 29) | Works; commutes Lansing↔Detroit. Kevin handles filings as authorized rep. |
| CUSTODY | Wayne (Triplett) | **Defendant / Counter-plaintiff** | in person (Oct 9) | Shayla has kids; DaSean's mom in Detroit. Venue transfer pending. |

### Kevin's Expert Qualifications (MRE 702 / FRE 702)

| Domain | Credential | Application |
|--------|-----------|-------------|
| Military intelligence | U.S. Army 11B, 25th Infantry Division. COIST analyst — OSINT, network modeling, link analysis, threat assessment | Hub-and-spoke network identification; Banks enterprise structure |
| Data science | M.S. Data Science, Michigan State University — 4.0 GPA. Graph theory, NLP, machine learning | Entity resolution, financial pattern analysis, graph centrality |
| Scientific methods | B.S. Microbiology (Bioethics minor), MSU. 5 years BSL2 contract lab | Chain-of-evidence methodology, contamination tracing |
| National security research | 2024 Sandia National Laboratories Graduate Fellow (1 of 11 nationally) | Independent research capacity, peer-reviewed |
| Technical systems | Founder, ecoPrimals — 3.6M lines Rust, 175+ papers, 93,700+ tests, 7-node compute mesh | Infrastructure for the network analysis presented in filings |

### What Kevin Is NOT

- **Not an attorney.** Explicitly stated in every sworn filing.
- **Not DaSean's biological brother.** Relationship is veteran friendship — defined upfront in Declaration.
- **Not DaSean's legal representative in the attorney sense.** Authorized representative for filing purposes only. DaSean makes his own decisions and appears in person.

---

## JUDGES

| judge_id | name | court | assigned_cases |
|----------|------|-------|----------------|
| STOKES | Hon. Stokes | Ingham 30th Circuit | CIV-BANKS, CIV-SMITHS |
| KOENIG | Hon. Koenig | Ingham 30th Circuit | PPO-SHAYLA, PPO-MARQUITA, PPO-SIMONE, PPO-BANKS, PPO-LEON, PPO-KEVIN |
| TRIPLETT | Hon. Triplett | Wayne 3rd Circuit | CUSTODY |

---

## TIMELINE

| date | event | cases | docs |
|------|-------|-------|------|
| **Sep 23 (Wed)** | **FILE @ Ingham: Alt service motions + service affidavits + cross-refs + declaration + nonappearance** | CIV-BANKS, CIV-SMITHS, PPO-* | ALT-SVC-BANKS, ALT-SVC-SMITHS, SVC-AFF-BANKS, SVC-AFF-SMITHS, XREF-NOTICE, CERT-MAIL, DECL-KEVIN, NONAPPEAR |
| Sep 23 (Wed) | MAIL copies to parties (Banks ×3, Smiths ×4) + email/fax Banks | CIV-BANKS, CIV-SMITHS, PPO-* | — |
| Sep 24 (Thu) | SEND: Election notification packets (8 targets) | — | ELECTION_NOTIFICATION_PACKETS_SEP24 |
| Sep 26 (Sat) | MAIL: Demand letters to Smiths (4301) + Banks (4349) | CIV-BANKS, CIV-SMITHS | DEMAND_LETTER_SMITHS_SEP19, DEMAND_LETTER_BANKS_SEP19 |
| Sep 26–28 | MAIL + POST: Notice and Demand to all parties | CIV-BANKS, CIV-SMITHS | NOTICE_AND_DEMAND_ALL_PARTIES_SEP22 |
| **Sep 29 (Mon)** | **HEARING: All 5 PPOs — Koenig, 1:30 PM** | PPO-* | DECL-KEVIN, NONAPPEAR |
| Sep 30 (Tue) | DUE: DaSean response to Shayla emergency motion | CUSTODY | (pending — may be moot after Sep 15 denial) |
| After hearing | SEND: Credibility notices (MSU Law, Walden, Morse, Pahara, NCC) — LAST ROUND | — | CREDIBILITY_NOTICES_SEP21 |
| Oct 6 (Mon) | REQUEST: Clerk Entry of Default — Banks | CIV-BANKS | DEFAULT_JUDGMENT_MOTION_4349_BANKS |
| **Oct 7 (Tue) 11:15 AM** | **FOC HEARING — Referee Biggar, Wayne** — Pre-Judgment Custody ×2 (both parties). DaSean brings Ring tape + PPO results + PCA evidence. Biggar sees full file incl. GAL motion. | CUSTODY | DASEAN_FOC_PREP (draft) |
| Oct 7 (Tue) | REQUEST: Clerk Entry of Default — Smiths | CIV-SMITHS | DEFAULT_JUDGMENT_MOTION_4301_SMITHS |
| **Oct 9 (Thu) 12:00 PM Zoom** | **CMC + MOTION HEARING — Triplett, Wayne** — Triplett has Biggar's recommendation. Rules on standing motions: GAL, venue transfer, custody. | CUSTODY | VENUE-XFER, GAL follow-up |
| ~Oct 10 | MAIL: Banks Oct 20 PPO via alt service order | PPO-KEVIN | (pending) |
| Oct 20 (Tue) | HEARING: Kevin PPO v. Banks — Round 2 | PPO-KEVIN | (pending) |
| Nov 3 (Tue) | ELECTION DAY — Miller + Aliyah Sabree on ballot | — | ELECTION_NOTIFICATION_PACKETS_SEP24 |
| WATCH | Wayne PPO (Shayla v. Kevin) — filed but NOT SERVED. No deadline until served. | PPO-WAYNE | PPO_RESPONSE_SHAYLA_V_MOK_SEP19 (ready when needed) |

---

## DOCUMENT REGISTRY

Active documents only. Fossilized docs are in `fossilRecord/` with their epoch READMEs.

| doc_id | filename | location | cases | status |
|--------|----------|----------|-------|--------|
| ALT-SVC-BANKS | MOTION_ALT_SERVICE_BANKS_SEP21.md | filing-ready | CIV-BANKS | file Sep 23 |
| ALT-SVC-SMITHS | MOTION_ALTERNATIVE_SERVICE_SEP17.md | filing-ready | CIV-SMITHS | file Sep 23 |
| SVC-AFF-BANKS | SERVICE_AFFIDAVIT_BANKS_PPO_SEP25.md | filing-ready | PPO-BANKS | file Sep 23 |
| SVC-AFF-SMITHS | SERVICE_AFFIDAVIT_SMITH_PPOS_SEP25.md | filing-ready | PPO-SHAYLA, PPO-MARQUITA, PPO-SIMONE, PPO-LEON | file Sep 23 |
| XREF-NOTICE | CROSS_REFERENCE_NOTICE_SEP25.md | filing-ready | ALL | file Sep 23 |
| CERT-MAIL | CERTIFICATE_OF_MAILING_PPO_SEP25.md | filing-ready | PPO-* | file Sep 23 |
| DECL-KEVIN | DECLARATION_KEVIN_MOK_WITNESS_EXPERT_SEP25.md | filing-ready | PPO-*, CUSTODY | file Sep 23 / bring Sep 29 |
| PPO-RESP | PPO_RESPONSE_SHAYLA_V_MOK_SEP19.md | filing-ready | PPO-WAYNE | file when served |
| DEFAULT-BANKS | DEFAULT_JUDGMENT_MOTION_4349_BANKS.md | filing-ready | CIV-BANKS | file Oct 6 |
| DEFAULT-SMITHS | DEFAULT_JUDGMENT_MOTION_4301_SMITHS.md | filing-ready | CIV-SMITHS | file Oct 7 |
| VENUE-XFER | MOTION_CHANGE_VENUE_WAYNE_TO_INGHAM.md | filing-ready | CUSTODY | file before Oct 9 |
| CONSOLIDATE | MOTION_CONSOLIDATION_INGHAM.md | filing-ready | CIV-BANKS, CIV-SMITHS | file after Sep 29. NOTE: consolidates 2 civils + cross-refs PPOs for judicial notice — NOT consolidating PPOs. Re-examine scope post-hearing. |
| DEMAND-BANKS | DEMAND_LETTER_BANKS_SEP19.md | filing-ready | CIV-BANKS | mail Sep 26 |
| DEMAND-SMITHS | DEMAND_LETTER_SMITHS_SEP19.md | filing-ready | CIV-SMITHS | mail Sep 26 |
| NOTICE-ALL | NOTICE_AND_DEMAND_ALL_PARTIES_SEP22.md | filing-ready | CIV-BANKS, CIV-SMITHS | mail Sep 26 / post Sep 27-28 |
| OIG-SUPP | OIG_SUPPLEMENT_FORGERY_SEP17.md | filing-ready | — | agency supplement |
| FED-PACKET | FEDERAL_PACKET_SEP22_MONOLITH.md | filing-ready | — | federal referral |
| FED-MASTER | FEDERAL_MASTER_PACKET_SEP18.md | filing-ready | — | federal referral |
| PPO-BLAST | BANKS_PPO_SERVICE_BLAST_SEP18.md | filing-ready | PPO-BANKS | reference (completed) |
| AGC-RICO | AGC_RICO_SUPPLEMENT_SEP21.md | filing-ready | — | agency supplement |
| JTC-RICO | JTC_RICO_SUPPLEMENT_SEP21.md | filing-ready | — | agency supplement |
| FOIA-BATCH | FOIA_BATCH1_SEP21.md | filing-ready | — | foia batch |
| FOIA-EMAIL | FOIA_EMAILS_SEP21.md | filing-ready | — | foia emails |
| CRED-NOTICE | CREDIBILITY_NOTICES_SEP21.md | filing-ready | — | credibility challenges |
| PRESS-RELEASE | PRESS_RELEASE_1_SEP21.md | filing-ready | — | media |
| PRESS-PITCH | PRESS_PITCH_INVESTIGATIVE_SEP21.md | filing-ready | — | media |
| PRESS-KIT | PRESS_KIT_NEWMEDIA_SEP21.md | filing-ready | — | media |
| PRESS-HEAD | PRESS_HEADSUP_SEP20.md | filing-ready | — | media |
| COVER-EMAIL | COVER_EMAIL_8AGENCY.md | filing-ready | — | agency cover |
| BK-ATTY | BK_ATTORNEY_NOTICE_EMAIL.md | filing-ready | — | notice |
| JOURNALIST | JOURNALIST_PACKET_SEP22.md | filing-ready | — | media |
| NONAPPEAR | NOTICE_NONAPPEARANCE_SUPPLEMENTAL_SEP25.md | filing-ready | PPO-* | file Sep 23 — warns court of expected no-shows, cites Banks bench warrant history, attaches OIG + Ring + ROD evidence |
