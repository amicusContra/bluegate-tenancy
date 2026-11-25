# ecoPrimals Dev Team Briefing — Public Evidence Library + Open Letter Series
## September 20, 2026
## Priority: Build after federal packet deployed (~Oct 1)

---

## WHAT WE'RE BUILDING

A **public evidence library and open letter series** hosted on ecoPrimals infrastructure,
backed by the Forgejo repo at `git.primals.eco/publicRecord/detroit`. Think of it as
the **Sporeprint model** applied to a federal racketeering investigation — every document
cryptographically timestamped, every fact cited, everything verifiable by anyone.

**Two layers:**
1. **Forgejo repo** (already exists): tamper-proof backend, git-signed commits, the evidentiary spine
2. **Public website** (NEW — this briefing): SEO-optimized, human-readable front door at `detroit.primals.eco` (or subdomain TBD)

---

## WHY THIS MATTERS

Kevin has compiled a federal racketeering packet ("Cash for Kids 2: Operation Detroit Plantation")
targeting a network of convicted felons, corrupt judges, and captured institutions that are
extracting millions in public education dollars from Detroit's most vulnerable children.

The packet goes to **8 federal agencies** simultaneously. But federal investigations are slow.
The **public site** creates:

1. **Parallel pressure**: Politicians, celebrities, and institutions named in the letters face
   public accountability even if feds move slowly
2. **Discoverability**: SEO means other harmed parties (parents, litigants, teachers) find the
   evidence library when searching for the school names, judge names, or network actors
3. **Validation**: Anyone can clone the repo and verify every claim against public records
4. **Media pipeline**: Journalists get pre-packaged, sourced material without FOIA delays
5. **Witness recruitment**: A contact form lets new victims come forward and add to the record

---

## SITE ARCHITECTURE

```
detroit.primals.eco/
│
├── /                           HOME — "Cash for Kids 2: A Public Record"
│   ├── Hero: DaSean's story (humanizing), 3% stat, 8 agencies notified
│   ├── Quick stats bar: $4.9M revenue, 3% proficiency, 6 judges, 0 victims named
│   └── CTAs: "Read the Letters" | "See the Evidence" | "Verify Everything"
│
├── /open-letters/              THE OPEN LETTER SERIES
│   ├── index.html              — all letters listed with send dates + response status
│   ├── to-curtis-jackson/      — the 50 Cent letter (dual voice: Curtis + 50)
│   ├── to-vivica-fox/          — "A beacon of hope for whom?"
│   ├── to-congresswoman-dingell/
│   ├── to-congresswoman-tlaib/
│   ├── to-donovan-mckinney/
│   ├── to-kensington-publishing/ — Son of Sam law inquiry
│   ├── to-msu-college-of-law/   — degree revocation request
│   ├── to-baker-college/         — HLC accreditation challenge
│   └── to-walden-university/     — dissertation fraud
│
├── /evidence/                  PUBLIC-RECORD EVIDENCE LIBRARY
│   ├── index.html              — categorized evidence index
│   ├── credential-fraud/       — fake JD, LinkedIn, conference bios, book covers
│   ├── financial/              — check registers, management fees, gift card self-dealing
│   ├── criminal-records/       — OTIS, MDOC, Oakland County records
│   ├── property/               — ROD documents, JTROS deed, foreclosure history
│   ├── charter-documents/      — LARA filings, 990s, board compositions
│   └── correspondence/         — attorney notices, demand letters (redacted as needed)
│
├── /books/                     BOOK ANALYSIS: ZERO VICTIMS, ZERO REMORSE
│   ├── bmf-book-analysis/      — Tonesa Welch: "not one victim named in 400 pages"
│   ├── banks-book-analysis/    — Brian Banks: "autobiography of fraud"
│   └── comparison/             — side by side: both books, zero accountability
│
├── /network/                   INTERACTIVE POWER MAP
│   ├── index.html              — visual network graph (D3.js or similar)
│   ├── actors/                 — individual profile pages for each network member
│   ├── institutions/           — PCA, MacDowell, Purpose Group, Inner Link, etc.
│   └── judges/                 — each judge's connections, boards, conflicts
│
├── /timeline/                  SCROLLABLE CHRONOLOGY
│   └── index.html              — every event, every filing, every discovery, dated
│
├── /about/                     WHO IS BEHIND THIS
│   ├── kevin-mok/              — military service, MSU, Sandia, career
│   ├── dasean-mitchell/        — veteran, father, the human cost
│   └── methodology/            — "one person, public records, 30 days"
│
├── /validate/                  "VERIFY EVERYTHING YOURSELF"
│   ├── index.html              — links to every public source
│   ├── lara.html               — how to search LARA for LLC filings
│   ├── otis.html               — how to search MDOC/OTIS for criminal records
│   ├── pacer.html              — how to search federal court records
│   ├── rod.html                — how to search Wayne County ROD
│   └── transparency.html       — how to search campaign finance records
│
├── /wronged/                   WRONGED PARTIES REGISTER
│   ├── index.html              — master list: institutions + individuals believed harmed by association
│   ├── institutions/           — Pahara, NCC, Walden, MSU, Baker/HLC
│   ├── individuals/            — Hutchings, Reed-Hendon, others
│   └── methodology.html        — "assume good faith, reclassify with evidence, git tracks everything"
│   NOTE: Default posture = wronged. If evidence shows active participation, page is updated.
│         Git history preserves original assumption + reclassification reason permanently.
│         Self-sorting mechanism: clean actors investigate and distance. Dirty ones stay silent.
│
├── /contact/                   FOR HARMED PARTIES + MEDIA
│   └── index.html              — secure contact form, PGP key option
│
└── /repo/                      LINK TO FORGEJO
    └── redirect → git.primals.eco/publicRecord/detroit
```

---

## THE OPEN LETTER SERIES — WORKFLOW

Each letter follows this lifecycle:

```
DRAFT → SEND PRIVATELY → WAIT 72h → PUBLISH ON SITE → UPDATE WITH RESPONSE
```

1. **Draft**: Letter is written and committed to Forgejo (timestamp: draft date)
2. **Send**: Letter is delivered to recipient (DM, email, certified mail, etc.)
3. **Wait 72 hours**: Give recipient time to respond privately
4. **Publish**: Letter goes live on the website with a banner:
   > "This letter was sent to [Recipient] on [Date] via [Method].
   >  As of [Publish Date], no response has been received."
5. **Update**: If recipient responds, their response is published alongside in full.
   If no response after 30 days, banner updates to reflect that.

**This is journalism-grade transparency.** Nobody can claim they weren't told.
Nobody can claim the letters were unfair. The full text is public.

---

## SEO STRATEGY

### Priority Keyword Targets

| Page | Target Queries | Search Intent |
|------|---------------|---------------|
| Home | "Purpose Charter Academy Detroit" | Parent researching school |
| Home | "Brian Banks Detroit schools" | Journalist or parent |
| Home | "MacDowell Preparatory Academy" | Parent or teacher |
| 50 Cent Letter | "50 Cent BMF Detroit school" | Fan + news crossover |
| 50 Cent Letter | "Curtis Jackson BMF family" | Media/entertainment |
| Fox Letter | "Vivica Fox Tonesa Welch" | Entertainment/book news |
| Fox Letter | "Black Mafia Queen book review" | Reader research |
| MSU Letter | "MSU Law Brian Banks" | Alumni + academic |
| Baker/HLC | "Baker College accreditation" | Education watchdogs |
| Evidence | "Joseph Holland drug trafficker charter school" | Investigative |
| Network | "Detroit charter school judges" | Policy/media |
| Network | "Cylenthia Miller PCA Board" | Voter research (Nov 3!) |
| Books | "BMF book victims" | Cultural criticism |

### Technical SEO Requirements
- **Static site generator** (Hugo, Eleventy, or Next.js static export)
- **Server-side rendering** for meta tags — critical for social sharing
- **Open Graph + Twitter Card tags** on every page — especially the open letters
- **Schema.org structured data**: `Article`, `Person`, `Organization`, `LegalForceStatus`
- **Sitemap.xml** submitted to Google Search Console immediately
- **Canonical URLs** pointing to the website (not the Forgejo raw files)
- **robots.txt**: Allow all. This is a public record. We WANT indexing.
- **HTTPS**: Required. Let's Encrypt via ecoPrimals infrastructure.
- **Performance**: Static files, CDN if available. Fast loads = better SEO.

### Social Sharing Optimization

Each open letter page needs **custom OG images** that work on Twitter/X, Instagram, LinkedIn:

```html
<!-- Example for the 50 Cent letter -->
<meta property="og:title" content="An Open Letter to Curtis Jackson (50 Cent)" />
<meta property="og:description" content="A U.S. Army veteran writes to Curtis Jackson about BMF's family running Detroit charter schools with 3% math proficiency." />
<meta property="og:image" content="https://detroit.primals.eco/og/to-curtis-jackson.png" />
<meta property="og:type" content="article" />
```

---

## AUTO-PUBLISH PIPELINE

```
Kevin commits to Forgejo
    │
    ▼
Webhook fires to build server
    │
    ▼
Static site rebuilds (Hugo/Eleventy)
    │
    ▼
Deploy to detroit.primals.eco
    │
    ▼
Google re-indexes (sitemap ping)
```

Every new document Kevin commits → site auto-rebuilds → public within minutes.
This means Kevin can keep investigating and the site stays current automatically.

---

## CONTENT ALREADY IN REPO (READY TO PORT)

From `git.primals.eco/publicRecord/detroit`:

| File | Maps To | Status |
|------|---------|--------|
| `filings/2026-09-22_federal_master_packet.pdf` | /evidence/federal-packet/ | Needs redaction pass |
| `evidence/*` | /evidence/ (various subcategories) | Ready to organize |
| `correspondence/*` | /evidence/correspondence/ | Ready |

**New content to create for the site:**
| Content | Source | Priority |
|---------|--------|----------|
| Open Letters (9 total) | POST_PACKET_EXCORIATION_STRATEGY.md | HIGH — these are the SEO magnets |
| Book analysis pages | TRANSCRIPT_CHAP*.md + analysis notes | HIGH — "zero victims" is a powerful phrase |
| Network map data | Federal packet Section 3-7 + subgraphs | HIGH — visual = shareable |
| Timeline | All dated events from investigation | MEDIUM — builds credibility |
| Validate page | Links to LARA, OTIS, PACER, ROD | MEDIUM — "don't trust us, check yourself" |
| About / Kevin's story | LinkedIn, resume, military record | MEDIUM — humanizes the investigator |
| About / DaSean's story | Custody briefing, PPO defense | HIGH — humanizes the WHY |

---

## DESIGN PRINCIPLES

1. **Sober, not sensational.** Black/white/dark blue. No red banners, no ALL CAPS headlines.
   This is a public record, not a tabloid. The facts are sensational enough.

2. **Mobile-first.** Detroit parents searching "Purpose Charter Academy" are on phones.

3. **Cite everything.** Every factual claim links to its source document in the Forgejo repo.
   "Brian Banks was convicted of 8+ felonies" → link to OTIS screenshot in /evidence/.

4. **Let the letters speak.** The Open Letter pages should be clean, readable, full-text.
   No sidebars, no pop-ups, no ads. Just the letter, the date, the delivery method,
   and the response status.

5. **Git provenance visible.** Each page footer shows: "This document was committed to the
   public record on [date] (commit: [hash]). Verify at git.primals.eco/publicRecord/detroit"

6. **Accessibility.** Alt text on images. Semantic HTML. Screen-reader friendly.
   The people this site serves are the community — make it accessible to everyone.

---

## TIMELINE FOR DEV TEAM

| Phase | When | Deliverable |
|-------|------|-------------|
| **Phase 0** | Now (Sep 20) | Review this briefing, confirm stack choice, set up subdomain |
| **Phase 1** | Sep 22-28 | Scaffold site, home page, /about, /validate, /repo redirect |
| **Phase 2** | Oct 1-3 | Port first batch of open letters (after they're sent privately) |
| **Phase 3** | Oct 3-7 | Evidence library pages, book analysis, network map (static v1) |
| **Phase 4** | Oct 7-14 | Auto-publish pipeline, SEO submission, social OG images |
| **Phase 5** | Ongoing | New content auto-publishes. Response updates. New letters. |

**The site doesn't need to be perfect at launch.** It needs to be **live, indexed, and
hosting the open letters** by the time the 72-hour private response windows expire.
Everything else builds iteratively.

---

## SECURITY CONSIDERATIONS

- **No PII in public documents.** Kevin's contact info is public (he chose that). No other
  personal addresses, SSNs, or non-public information.
- **Redaction pass** on all evidence before public posting. Court documents may contain
  addresses or case numbers that need partial redaction.
- **DDoS protection** — this site may attract attention from the network. CloudFlare or
  equivalent.
- **No login system.** This is a public record. No accounts, no tracking, no cookies beyond
  analytics (privacy-respecting: Plausible or similar, not Google Analytics).
- **Backup**: Forgejo IS the backup. The site is generated from it. Destroy the server,
  rebuild from repo.

---

## SUMMARY FOR TEAM

Kevin compiled a federal racketeering case against a network of convicted felons running
Detroit charter schools under judicial protection. He's sent the evidence to 8 federal
agencies. Now we build the **public front door** — an SEO-optimized site where:

- **Open Letters** to public figures (50 Cent, Vivica Fox, Congress members, MSU, Baker College)
  are published after private delivery, creating searchable public accountability
- **Evidence** is browsable and verifiable against Forgejo's git-signed commits
- **Harmed parties** (parents, litigants, teachers) can find the library and add their stories
- **Media** gets pre-packaged, sourced material ready to run

The Forgejo repo is the proof. The website is the megaphone.

Build it like the Sporeprint: clean, factual, verifiable, and impossible to ignore.

---

*"Every fact is cited. Every document is timestamped. Every letter is open. Verify everything."*
