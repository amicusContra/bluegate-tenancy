# Graph Data — Banks/Smiths Network

Concrete instantiation of GRAPH_SCHEMA.md for the current cases.
Organized by temporal epoch for the intelligence accumulation narrative.

---

## PERSONS

| id | name | role | first_known | source | key_facts |
|----|------|------|-------------|--------|-----------|
| BANKS | Brian Banks | Defendant, school operator | 2026-07-15 | DaSean encounter at PCA | 9 felony convictions (LEIN/OTIS). No law license. BMF blood lineage. FBI wiretap associate. |
| SHAYLA | Shayla Smith | Defendant, mother | 2026-06-01 | Custody filing | Enrolled children at PCA without consent. Filed retaliatory PPO in Wayne. |
| LEON | Leon Smith | Defendant, USPS employee | 2026-08-01 | Service attempts | Intercepted certified mail. Assaulted DaSean Sep 2. Text: "see you in court." |
| MARQUITA | Marquita Smith | Defendant | 2026-08-01 | Service attempts | Named in lease at 17370 Dresden. Coordinated evasion. |
| SIMONE | Simone Smith | Defendant | 2026-08-01 | Service attempts | Named at Dresden address. Coordinated evasion. BK: filed Ch.13 first (got nothing), then Ch.7 (26-49404-lsg, Aug 24 2026). Owns 21734 Normandy, Eastpointe but lists Dresden in BK. |
| HOLLAND | Joseph Holland Jr. | Defendant, PCA finance | 2026-08-20 | OTIS/LEIN | MDOC #443789. Drug trafficking. "Discharged WITHOUT IMPROVEMENT." Handles PCA finances. |
| DASEAN | DaSean Mitchell | Petitioner, father | 2026-06-01 | Best friend | Kevin's best friend and fellow veteran (U.S. Army). Not biological brothers. Father of Sahana + Allanna. Filed PPOs and custody counter-claim. DaSean appears in person at hearings; Kevin is his authorized representative for filings, fact witness, and expert witness. |
| KEVIN | Kevin Mok | Plaintiff, witness, expert | always | Self | Military intelligence, data science, scientific background. Dual role across all cases. |
| PERKINS_TODD | Todd Perkins | Enabler | 2026-08-15 | PACER/public records | Banks associate. Sports agent. Failed mayoral candidate. Municipal attorney. |
| HUTCHINGS | Devin Hutchings | Enabler | 2026-08-20 | OSINT | Banks associate. CBC board. Former state rep. |
| MORELAND | Lamar Moreland | Enabler | 2026-09-01 | AGC complaint | Commissioner. Protective of Banks network. |
| ELLIS | Tracye Ellis | Defendant | 2026-09 | Amended complaint | Amended into CIV-BANKS (2026-4349-CZ). |

## ENTITIES

| id | name | type | controlled_by | first_known | source |
|----|------|------|---------------|-------------|--------|
| PCA | Purpose Charter Academy | School | BANKS | 2026-07-15 | DaSean encounter |
| PURPOSE_FOUND | Purpose Foundation | 501(c)(3) | BANKS | 2026-08-01 | SOS records |
| PURPOSE_GROUP | Purpose Group LLC | LLC | BANKS | 2026-08-15 | SOS records |
| BANKS_STRATEGY | Banks Strategy LLC | LLC | BANKS | 2026-09-01 | SOS/OSINT |
| MACDOWELL | MacDowell Preparatory | School (defunct) | BANKS | 2026-09-10 | MDE records |
| CBC | Congressional Black Caucus Foundation | Nonprofit | — | 2026-08-20 | Public records |

## CASES (from CASE_REGISTRY.md)

| id | case_no | court | caption | judge | filed | type |
|----|---------|-------|---------|-------|-------|------|
| CIV-BANKS | 2026-4349-CZ | Ingham 30th | Mok v. Banks et al. | Stokes | ~Aug 2026 | Civil — Defendants: Banks + Holland + Tracye Ellis (amended). Long-term. |
| CIV-SMITHS | 2026-4301-CZ | Ingham 30th | Mok v. Smith et al. | Stokes | ~Aug 2026 | Civil — Defendants: 4 Smiths + Banks (amended in). Resolves w/ custody. |
| PPO-SHAYLA | 26-0000004432-PP | Ingham 30th | Mitchell v. Shayla | Koenig | ~Aug 2026 | PPO-Domestic |
| PPO-MARQUITA | 26-0000004433-PH | Ingham 30th | Mitchell v. Marquita | Koenig | ~Aug 2026 | PPO-Stalking |
| PPO-SIMONE | 26-0000004434-PH | Ingham 30th | Mitchell v. Simone | Koenig | ~Aug 2026 | PPO-Stalking |
| PPO-BANKS | 26-0000004435-PH | Ingham 30th | Mitchell v. Banks | Koenig | ~Aug 2026 | PPO-Stalking |
| PPO-LEON | 26-0000004436-PH | Ingham 30th | Mitchell v. Leon | Koenig | ~Aug 2026 | PPO-Stalking |
| PPO-KEVIN | 26-0000004437-PH | Ingham 30th | Mok v. Banks | Koenig | ~Sep 2026 | PPO-Stalking |
| CUSTODY | 26-108221-DC | Wayne 3rd | Smith v. Mitchell | Triplett | Jun 2026 | Custody |
| PPO-WAYNE | (pending) | Wayne 3rd | Smith v. Mok | (pending) | Sep 2026 | PPO-Retaliatory |

## EVENTS (temporal chain)

| id | date | description | triggered_by | evidence |
|----|------|-------------|--------------|----------|
| EVT-PCA-BLOCK | 2026-08-29 | Kevin goes to PCA ALONE on DaSean's behalf (DaSean at work). Banks denies Kevin access, claims to be "a lawyer." First interaction. | — | Kevin witness testimony |
| EVT-PCA-DASEAN | 2026-09-xx | DaSean goes to PCA separately WITH POLICE ESCORT HE REQUESTED to see his children. Banks speaks to officers privately. Police escort DaSean OFF property — no notice about his kids. Banks then contacts DaSean repeatedly about KEVIN'S CASE, not the children. | EVT-PCA-BLOCK | DaSean testimony, police records |
| EVT-POLICE-REPORT | 2026-09-09 | Banks files retaliatory report (GPW DPS #26-0909-0176) naming KEVIN for stalking/harassment (likely re: Kevin's public LinkedIn). Kevin was NOT present during DaSean's escorted visit. Banks used DaSean's lawful police escort to manufacture complaint against Kevin. | EVT-PCA-DASEAN | GPW police report |
| EVT-CUSTODY-FILE | 2026-06-01 | Shayla files for custody in Wayne County | — | Court filing |
| EVT-CIV-FILE | 2026-08-01 | Kevin files civil complaints in Ingham | EVT-PCA-BLOCK | Court filings |
| EVT-PPO-FILE | 2026-08-15 | DaSean files PPOs in Ingham against Banks + Smiths | EVT-PCA-BLOCK | Court filings |
| EVT-SERVICE-CIV | 2026-08-20 | Certified mail service attempted on all defendants | EVT-CIV-FILE | USPS tracking |
| EVT-MAIL-INTERCEPT | 2026-08-25 | Leon intercepts certified mail at Dresden address (USPS employee) | EVT-SERVICE-CIV | USPS OIG complaints #174517, #202990, #208322 |
| EVT-LEON-TEXT | 2026-08-28 | Leon texts "see you in court" — admits actual notice but files no answer | EVT-MAIL-INTERCEPT | Text screenshot |
| EVT-ASSAULT | 2026-09-02 | Leon assaults DaSean at Dresden address | — | Ring camera footage, police report |
| EVT-CHILD-REMOVAL | 2026-09-02 | Shayla enters, removes both children after Leon's assault | EVT-ASSAULT | Ring camera footage |
| EVT-EMERGENCY-SHAYLA | 2026-09-03 | Shayla files emergency motion in Wayne | EVT-ASSAULT | Court filing |
| EVT-EMERGENCY-DASEAN | 2026-09-03 | DaSean files emergency response in Wayne with Ring evidence | EVT-ASSAULT | Court filing + Ring footage |
| EVT-AGENCY-BLITZ | 2026-09-08 | Kevin files with 8+ agencies (JTC, AGC, Bar, FBI, OIG, FOIA) | EVT-MAIL-INTERCEPT | Filing receipts |
| EVT-BANKS-7CH | 2026-09-18 | 7-channel service blast on Banks (email, fax, LinkedIn, text, mail, etc.) | EVT-SERVICE-CIV | Service affidavit |
| EVT-FORGERY-DISCOVER | 2026-09-06 | Kevin discovers forged green cards on service receipts | EVT-MAIL-INTERCEPT | Signature comparison exhibit |
| EVT-PPO-RETALIATION | 2026-09-15 | Shayla files retaliatory PPO against Kevin in Wayne | EVT-PPO-FILE | Wayne court filing |
| EVT-KOENIG-REASONABLE | 2026-08-20 | Koenig finds reasonable cause on Shayla domestic PPO (26-4432-PP) | EVT-PPO-FILE | Court order |
| EVT-FILE-SEP25 | 2026-09-25 | Consolidated filing: alt service motions, service affidavits, cross-refs, Kevin declaration, Wayne PPO response | EVT-BANKS-7CH | Filing receipts |
| EVT-HEARING-PPO | 2026-09-29 | PPO hearing — all 5 Ingham PPOs before Koenig, 1:30 PM | EVT-PPO-FILE | Court schedule |
| EVT-DEFAULT-BANKS | 2026-10-06 | Request clerk entry of default — Banks (2026-4349-CZ) | EVT-SERVICE-CIV | MCR 2.603 |
| EVT-DEFAULT-SMITHS | 2026-10-07 | Request clerk entry of default — Smiths (2026-4301-CZ) | EVT-SERVICE-CIV | MCR 2.603 |
| EVT-WAYNE-CMC | 2026-10-09 | Wayne CMC hearing, Noon — venue transfer motion | EVT-CUSTODY-FILE | Court schedule |
| EVT-HEARING-KEVIN-PPO | 2026-10-20 | Kevin PPO v. Banks — Round 2 hearing | EVT-BANKS-7CH | Court schedule |

## JUDGES

| id | name | court | assigned_cases | first_known | source |
|----|------|-------|----------------|-------------|--------|
| STOKES | Hon. Stokes | Ingham 30th Circuit | CIV-BANKS, CIV-SMITHS | 2026-08-01 | Court assignment |
| KOENIG | Hon. Koenig | Ingham 30th Circuit | PPO-SHAYLA, PPO-MARQUITA, PPO-SIMONE, PPO-BANKS, PPO-LEON, PPO-KEVIN | 2026-08-15 | Court assignment |
| TRIPLETT | Hon. Triplett | Wayne 3rd Circuit | CUSTODY | 2026-06-01 | Court assignment |

## KNOWLEDGE ACCUMULATION — BANKS

What we knew about Banks, and when:

| epoch | date_range | new_knowledge | source | confidence |
|-------|-----------|---------------|--------|------------|
| 0 | Pre Jul 2026 | Banks runs PCA, claims to be a lawyer | DaSean | medium |
| 1 | Jul 15 | Banks blocks DaSean, intercepts police, files false report | Witness, GPW PD | high |
| 2 | Aug 1-15 | Banks has NO law license (State Bar search) | State Bar | high |
| 3 | Aug 15-20 | Banks has 9 felony convictions (LEIN/OTIS) | Public records | high |
| 4 | Aug 20-Sep 1 | Banks controls Purpose Foundation, Purpose Group, Banks Strategy LLC | SOS filings | high |
| 5 | Sep 1-8 | Holland (MDOC #443789, drug trafficking) handles PCA finances | OTIS, public records | high |
| 6 | Sep 8-15 | Banks connected to CBC Foundation events, Perkins, Hutchings network | OSINT, Eventbrite, CBC | high |
| 7 | Sep 15-18 | Banks evades all 7 service channels — coordinated, not accidental | Service affidavit | high |
| 8 | Sep 18-20 | PACER reveals Bryant v. Miller — Banks previously sued for similar conduct | PACER | high |
| 9 | Sep 20-22 | BMF blood lineage confirmed (Meech Flenory family connection) | BMF book transcript, public records | medium-high |
| 10 | Sep 22 | Constitutional deprivation argument — Wayne delay = ongoing rights violation | Legal analysis | high |

## EDGES (relationships)

```
# Banks → Cases (Banks is defendant in BOTH civil cases)
BANKS --[party_to: defendant]--> CIV-BANKS       # Original filing
BANKS --[party_to: defendant]--> CIV-SMITHS      # AMENDED IN — Banks is in both civil cases
BANKS --[party_to: respondent]--> PPO-BANKS
BANKS --[party_to: respondent]--> PPO-KEVIN
BANKS --[controls]--> PCA
BANKS --[controls]--> PURPOSE_FOUND
BANKS --[controls]--> PURPOSE_GROUP
BANKS --[controls]--> BANKS_STRATEGY
HOLLAND --[party_to: defendant]--> CIV-BANKS     # Amended in
HOLLAND --[employed_by: finance]--> PCA           # HOLLAND employed_by BANKS/PCA
ELLIS --[party_to: defendant]--> CIV-BANKS       # Tracye Ellis — amended in

# Smiths → Cases
SHAYLA --[party_to: defendant]--> CIV-SMITHS
SHAYLA --[party_to: respondent]--> PPO-SHAYLA
SHAYLA --[party_to: plaintiff]--> CUSTODY
SHAYLA --[party_to: petitioner]--> PPO-WAYNE
LEON --[party_to: defendant]--> CIV-SMITHS
LEON --[party_to: respondent]--> PPO-LEON
MARQUITA --[party_to: defendant]--> CIV-SMITHS
MARQUITA --[party_to: respondent]--> PPO-MARQUITA
SIMONE --[party_to: defendant]--> CIV-SMITHS
SIMONE --[party_to: respondent]--> PPO-SIMONE

# Kevin ↔ DaSean (relationship)
KEVIN --[connected_to: veteran_brotherhood]--> DASEAN  # Best friends, fellow Army veterans. NOT biological brothers.
KEVIN --[authorized_rep_for]--> DASEAN                 # Kevin files PPO paperwork on DaSean's behalf. NOT attorney.

# Kevin → Cases (typed roles)
KEVIN --[party_to: plaintiff, pro_se]--> CIV-BANKS         # Kevin's own case. Files and appears.
KEVIN --[party_to: plaintiff, pro_se]--> CIV-SMITHS        # Kevin's own case. Files and appears.
KEVIN --[party_to: auth_rep+witness+expert]--> PPO-SHAYLA   # Files for DaSean; testifies as fact+expert witness.
KEVIN --[party_to: auth_rep+witness+expert]--> PPO-MARQUITA
KEVIN --[party_to: auth_rep+witness+expert]--> PPO-SIMONE
KEVIN --[party_to: auth_rep+witness+expert]--> PPO-BANKS
KEVIN --[party_to: auth_rep+witness+expert]--> PPO-LEON
KEVIN --[party_to: petitioner, pro_se]--> PPO-KEVIN         # Kevin's own PPO against Banks.
KEVIN --[party_to: respondent, pro_se]--> PPO-WAYNE         # Defending Shayla's retaliatory PPO.
KEVIN --[party_to: witness+expert]--> CUSTODY               # Non-party witness in Wayne.

# DaSean → Cases (typed roles)
DASEAN --[party_to: petitioner]--> PPO-SHAYLA       # DaSean's PPOs. Appears in person; Kevin handles filings.
DASEAN --[party_to: petitioner]--> PPO-MARQUITA
DASEAN --[party_to: petitioner]--> PPO-SIMONE
DASEAN --[party_to: petitioner]--> PPO-BANKS
DASEAN --[party_to: petitioner]--> PPO-LEON
DASEAN --[party_to: counter-plaintiff]--> CUSTODY   # Wayne. Constraint: works; commutes Lansing↔Detroit.

# Cross-case relationships
CIV-BANKS --[related_to]--> CIV-SMITHS     # Same network, same judge
CIV-BANKS --[related_to]--> PPO-BANKS      # Same respondent
CIV-SMITHS --[related_to]--> PPO-SHAYLA    # Same respondent
CIV-SMITHS --[related_to]--> PPO-LEON      # Same respondent
PPO-* --[related_to]--> CUSTODY            # Same children, same family
CUSTODY --[related_to: venue_transfer]--> CIV-BANKS    # Constitutional argument

# Banks → People (network)
BANKS --[connected_to: associate]--> PERKINS_TODD
BANKS --[connected_to: associate]--> HUTCHINGS
BANKS --[connected_to: political]--> MORELAND
BANKS --[connected_to: employer]--> HOLLAND

# Event chain
EVT-PCA-BLOCK --[triggered_by]--> EVT-POLICE-REPORT
EVT-PCA-BLOCK --[triggered_by]--> EVT-CIV-FILE
EVT-PCA-BLOCK --[triggered_by]--> EVT-PPO-FILE
EVT-SERVICE-CIV --[triggered_by]--> EVT-MAIL-INTERCEPT
EVT-MAIL-INTERCEPT --[triggered_by]--> EVT-LEON-TEXT
EVT-ASSAULT --[triggered_by]--> EVT-CHILD-REMOVAL
EVT-CHILD-REMOVAL --[triggered_by]--> EVT-EMERGENCY-SHAYLA
EVT-ASSAULT --[triggered_by]--> EVT-EMERGENCY-DASEAN
EVT-PPO-FILE --[triggered_by]--> EVT-PPO-RETALIATION
```
