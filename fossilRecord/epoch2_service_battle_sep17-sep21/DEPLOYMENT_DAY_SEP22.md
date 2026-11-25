# DEPLOYMENT DAY — MONDAY SEPTEMBER 22, 2026
# Simultaneous Multi-Agency Federal Packet Delivery
# + Journalist Distribution

---

## MATERIALS READY

| Item | File | Format | Pages | Size |
|------|------|--------|-------|------|
| Federal Master Packet | `FEDERAL_MASTER_PACKET_SEP18.pdf` | PDF | 41 | 131KB |
| Journalist Briefing Packet | `JOURNALIST_PACKET_SEP22.pdf` | PDF | 7 | 22KB |
| Banks PPO Email (for reference) | `BANKS_PPO_EMAIL_READY.txt` | TXT | 1 | — |
| Banks PPO Fax Cover | `BANKS_PPO_FAX_COVERTEXT.txt` | TXT | 1 | — |

---

## PHASE 0: FORGEJO PUBLIC RECORD PUSH (Monday 7:00 AM)

Push all filings to the self-hosted public record repository BEFORE contacting anyone.
This establishes cryptographic timestamps (SHA-256 git hashes) proving when documents existed.

**Repo:** https://git.primals.eco/publicRecord/detroit
**Local clone:** `/home/sporegate/Development/detroit`

```bash
# SSH into server
ssh sporegate@primals.eco
cd ~/Development/detroit

# Transfer staged files from Windows
# (or scp from Windows: scp -r staged/* sporegate@primals.eco:~/Development/detroit/)

# Commit each file with descriptive messages
git add filings/2026-09-22_federal_master_packet.pdf
git commit -m "filing: Federal Multi-Agency Intelligence Packet — Banks Network RICO pattern"
git add filings/2026-09-22_journalist_briefing_packet.pdf
git commit -m "filing: Journalist briefing packet — 7 investigative story angles"
git add -A
git commit -m "batch: all prior filings, evidence, correspondence"
git push
```

**Verify public access:** https://git.primals.eco/publicRecord/detroit

Staged files (8 total, 13.5 MB):
| Category | File | Size |
|----------|------|------|
| filings | federal_master_packet.pdf | 144 KB |
| filings | journalist_briefing_packet.pdf | 22 KB |
| filings | oig_supplement_forgery.md | 9 KB |
| filings | complaint_chain_master.md | 11 KB |
| filings | motion_alternative_service.md | 12 KB |
| evidence | oig_supplement_proof_package.pdf | 1.1 MB |
| evidence | ring_exhibit_keyframes.pdf | 12.2 MB |
| correspondence | banks_ppo_service_email.txt | 2 KB |

**Why this matters:** Every journalist and agency can independently verify timestamps.
`git log --oneline` shows immutable SHA-256 hashes for each filing.

---

## PHASE 1: ONLINE PORTALS (Monday 8:00 AM)

Submit simultaneously to all portals that accept online tips.

| # | Agency | Portal | What to Upload |
|---|--------|--------|----------------|
| 1 | **FBI Detroit** | [tips.fbi.gov](https://tips.fbi.gov) | Federal Master Packet PDF |
| 2 | **DEA Detroit** | [dea.gov/submit-tip](https://www.dea.gov/submit-tip) | Federal Master Packet PDF (reference BMF case 2:05-cr-80955) |
| 3 | **IRS CI** | IRS Form 3949-A (mail) + narrative | Master Packet; check if online submission available |
| 4 | **DOE OIG** | [oighotline.ed.gov](https://oighotline.ed.gov) | Federal Master Packet PDF (supplement to existing complaint) |
| 5 | **FinCEN** | FinCEN Tips Form | Master Packet PDF (SAR reference) |

**IMPORTANT:** For each submission, screenshot the confirmation page. Save to `02-evidence/screenshots-correspondence/deployment-sep22/`.

---

## PHASE 2: EMAIL BLAST (Monday 9:00 AM)

### Federal Agencies — Email with PDF Attachment

| # | Agency | Email | Subject Line |
|---|--------|-------|-------------|
| 1 | FBI Detroit | detroit@fbi.gov | SUPPLEMENT: Multi-Agency Intelligence Packet — Banks Network — RICO Pattern |
| 2 | DOE OIG | oig.hotline@ed.gov | SUPPLEMENT TO COMPLAINT: Brian Banks / MacDowell Prep / Purpose Charter Academy |
| 3 | USAO E.D. Mich | USAMI.Complaints@usdoj.gov | Cross-Reference Request: Banks Network — BMF Connection — Active Cases in Your Docket |
| 4 | MI AG | ag@michigan.gov | SUPPLEMENT: UPL + Campaign Finance + Charitable Trust Violations — Banks/Holland Network |
| 5 | US Trustee | USTP.Region09.DET.ECF@usdoj.gov | Bankruptcy Fraud Referral: Holland (MDOC #443789) — Undisclosed JTWRS Property |

### Journalists — Email with Journalist Packet PDF

| # | Contact | Outlet | Email (find/confirm) | Subject Line |
|---|---------|--------|---------------------|-------------|
| 1 | Robert Elrick | Detroit Free Press | (confirm via newsroom) | EXCLUSIVE: Cash for Kids 2 — 7 Story Angles — Full Evidence Packet |
| 2 | Rita | Clutch Justice | (via clutchjustice.com contact) | Follow-Up to MacDowell Story — Federal Packet Going to 8 Agencies Monday |
| 3 | Jim Schaefer | Detroit Free Press | (confirm via newsroom) | Investigative Tip: Institutional Capture Across Detroit — Schools/Courts/Treasury |
| 4 | WXYZ I-Team | Channel 7 | (tips@wxyz.com or newsroom) | Tips: Convicted Felon Running Detroit Charter Schools — 3% Math Proficiency — Judges on Board |
| 5 | Chalkbeat Detroit | Chalkbeat | detroit@chalkbeat.org | Charter School Accountability: $4.3M Public Funds, 3% Math Proficiency, Fake Credentials |

**EMAIL BODY TEMPLATE FOR JOURNALISTS:**

```
Subject: [see above]

Dear [Name],

I am simultaneously submitting the attached intelligence packet to FBI Detroit, 
DEA Detroit, IRS Criminal Investigation, DOE OIG, USAO Eastern District of Michigan,
FinCEN, the Michigan Attorney General, and the US Trustee.

You are receiving it because two network judges face the November 3 ballot, and 
independent journalism is the only mechanism with the speed to inform voters before then.

The packet documents institutional capture across Detroit's schools, courts, treasury,
and oversight bodies. At the center is a convicted felon running two charter schools.
Around him: six sitting judges with undisclosed ties, a county treasurer whose family
exploits the foreclosure pipeline he administers, and a drug trafficker handling
school money.

Every claim is sourced from public records. I am available for an interview at your 
convenience.

The full evidence archive with cryptographic provenance is publicly available at:
  https://git.primals.eco/publicRecord/detroit

Anyone can clone it (git clone https://git.primals.eco/publicRecord/detroit.git).
Every document has an immutable SHA-256 hash and timestamp. Deletions are visible
in the git history. The repository is self-hosted on sovereign infrastructure — 
no platform can take it down.

Kevin Mok
(517) 420-8938
kevin@kevmok.com
Signal preferred for sensitive communications

Attachment: JOURNALIST_PACKET_SEP22.pdf (7 pages)
Public Archive: https://git.primals.eco/publicRecord/detroit
```

---

## PHASE 3: FAX BLITZ (Monday 10:00 AM)

Fax the master packet to every agency that accepts fax.

| # | Agency | Fax Number | Notes |
|---|--------|-----------|-------|
| 1 | FBI Detroit | (313) 965-2006 | Include cover: "Attn: Supervisory Special Agent — Cross-Agency Intelligence Packet" |
| 2 | DEA Detroit | (313) 234-4055 | Include cover: "Attn: Group Supervisor — BMF Nexus Intelligence" |
| 3 | IRS CI Detroit | (313) 234-2505 | Include cover: "Attn: Special Agent in Charge — Tax Fraud / Dark Money" |
| 4 | DOE OIG | (202) 245-7047 | Include cover: "SUPPLEMENT TO EXISTING COMPLAINT — Brian Banks / MacDowell / PCA" |
| 5 | USAO E.D. Mich | (313) 226-3561 | Include cover: "Attn: Criminal Chief — Cross-Reference Request" |
| 6 | USTP Detroit | (313) 226-7952 | Include cover: "Attn: Bankruptcy Fraud Unit — Holland Serial BK + Undisclosed Asset" |
| 7 | MI AG | (517) 241-7074 | Include cover: "SUPPLEMENT: Banks/Holland — UPL + Campaign Finance + Charitable Trust" |

**FAX COVER TEMPLATE:**

```
TO: [Agency Name]
FAX: [Number]
FROM: Kevin Mok | (517) 420-8938
DATE: September 22, 2026
RE: CASH FOR KIDS 2 — Multi-Agency Intelligence Packet
PAGES: 41 + cover

This packet is being sent simultaneously to FBI, DEA, IRS CI, DOE OIG, 
USAO E.D. Mich, FinCEN, MI AG, and US Trustee. Each agency has jurisdiction 
over a different piece of this network. This document gives every agency 
the complete map.

Please cross-reference the names in this packet against your existing cases:
Banks, Holland, Sabree, Welch, Perkins, Inner Link Graphics, Right Turn Project,
Purpose Group, Metro Property Group.

CONFIDENTIAL — LAW ENFORCEMENT SENSITIVE
```

**After each fax:** Screenshot the confirmation page → save to `02-evidence/screenshots-correspondence/deployment-sep22/`

---

## PHASE 4: CERTIFIED MAIL (Monday afternoon — Post Office)

Print the master packet (41 pages) × 8 copies + covers.

| # | Agency | Address | Certified? |
|---|--------|---------|-----------|
| 1 | FBI Detroit | 477 Michigan Ave, Suite 1900, Detroit MI 48226 | YES |
| 2 | DEA Detroit | 431 Howard St, Detroit MI 48226 | YES |
| 3 | IRS CI Detroit | XXX Michigan Ave, Detroit MI 48226 | YES |
| 4 | DOE OIG | 400 Maryland Ave SW, Washington DC 20202 | YES |
| 5 | USAO E.D. Mich | 211 W. Fort St, Suite 2001, Detroit MI 48226 | YES |
| 6 | FinCEN | P.O. Box 39, Vienna VA 22183 | YES |
| 7 | MI AG | 525 W. Ottawa St, Lansing MI 48909 | YES |
| 8 | USTP Detroit | 211 W. Fort St, Suite 700, Detroit MI 48226 | YES |

**Estimated cost:** ~$50-60 for certified mail × 8

**Track all tracking numbers** in a spreadsheet or note doc.

---

## PHASE 5: PHONE FOLLOW-UP (Monday Sep 29 — One Week Later)

Call each agency to confirm receipt and get case/reference numbers.

| # | Agency | Phone | Ask For |
|---|--------|-------|---------|
| 1 | FBI Detroit | (313) 965-2323 | "I submitted a tip online and sent a packet by mail. Can I get a reference number?" |
| 2 | DOE OIG Hotline | (800) 647-8733 | "I have an existing complaint about Brian Banks / MacDowell Prep. I sent a supplement." |
| 3 | USAO | (313) 226-9100 | "I sent a cross-reference packet regarding cases already in your docket." |
| 4 | MI AG | (517) 335-7622 | "I sent a supplement to the UPL complaint regarding Brian Banks." |

---

## COORDINATION NOTES

### Timing:
- Banks returned from DC Sunday evening
- PPO blast hit his inbox/fax/mail while he was gone
- Round 3 JTC/Bar filings faxed Saturday
- By Monday morning, Banks is reacting to the PPO while federal agencies receive the full packet
- He cannot coordinate a response because everyone is learning simultaneously

### Information Asymmetry:
- Banks does not know this packet exists
- Banks does not know about the October intelligence from Tonesa's book
- Banks does not know that both his and Welch's books have been cross-referenced
- Banks does not know the journalist packet is going out same day
- The JTC/Bar supplements from Saturday are already in process

### Defensive Posture:
- Save ALL sent emails (with timestamps)
- Screenshot ALL online portal confirmations
- Save ALL fax confirmations
- Keep ALL certified mail tracking numbers
- Document the sequence and timing
- This documentation proves the packet was filed, in case of retaliation claims

---

*Deployment Day: Monday September 22, 2026*
*Everything moves simultaneously. No one gets advance warning.*
*"You each have jurisdiction over a piece of this. I have the map of all of it."*
