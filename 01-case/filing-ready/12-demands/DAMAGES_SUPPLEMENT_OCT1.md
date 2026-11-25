# DAMAGES SUPPLEMENT — October 1, 2026
## Updates to DAMAGES_SCHEDULE_ALL_DEFENDANTS.md

---

## I. DEFENSE ATTORNEY RETENTION VALIDATES PLAINTIFF'S RATE

### What Happened

On September 30, 2026, Brian Banks retained Jehan Crump-Gibson
of GL Legal Group (gllegalgroup.com) to represent him in both
Ingham County civil cases (2026-4301-CZ and 2026-4349-CZ).

GLLG is a full-service litigation firm. Based on Michigan legal
market rates for civil defense work of this complexity (multi-
defendant, multi-count, cross-jurisdictional, federal overlay):

| Billing category | Estimated rate |
|-----------------|---------------|
| Partner-level defense attorney | $275–$450/hr |
| Associate support | $175–$275/hr |
| Paralegal/legal assistant | $100–$150/hr |
| Blended firm rate (this engagement) | $250–$350/hr estimated |

### What This Means for Damages

The prior damages schedule valued my work at a **$278/hr blended
rate** (weighted average of OSINT analysis, legal research, document
drafting, database work, and strategic planning). This was calculated
conservatively using published rates for data science consulting
($150-300/hr), legal consulting ($200-400/hr), and OSINT analysis
($175-350/hr).

**Banks's own defense spending now validates my rate claim.** If his
attorney bills $300/hr to DEFEND against my filings, a jury can
reasonably conclude that the filings themselves — and the
investigation, analysis, and strategy behind them — are worth at
least as much per hour to PRODUCE.

The defense paradox deepens: every dollar Banks spends defending
validates the economic damages he's accumulating.

### Updated Rate Calculation

| Rate basis | Prior | Updated | Justification |
|-----------|-------|---------|---------------|
| Blended hourly | $278/hr | $300/hr | Defendant's own billing rate validates market value |
| Hours to date (Aug 29 – Oct 1) | 1,252 hrs | 1,400+ hrs | 5+ additional weeks of intensive work |
| Economic damages (time) | $347,700 | $420,000+ | Updated hours × validated rate |

**NOTE (per Kevin's standing instruction):** The aggregate economic
damages figure above reflects LOST TIME valuation. Hard costs
(process server, mail, filing, travel) remain approximately $5,000.
The $100,000+ in lost opportunity costs (ecoPrimals development,
thesis work, employment search disruption) are separate from
the hourly time valuation and remain estimated.

---

## II. NEW DAMAGE CATEGORY: FORCED DEANONYMIZATION

### The Claim

Banks's conduct forced me to irrevocably destroy the pseudonymous
identity architecture I had spent over a year designing, building,
and maintaining as a cardinal feature of my scientific computing
platform (ecoPrimals / sporePrint).

This is not a claim of embarrassment or reputational harm. This is
destruction of intellectual property — specifically, the deliberate
architectural separation between my real identity and my published
work, which was a designed, documented, and cryptographically
timestamped feature of the ecosystem.

### What Was Destroyed

#### The Architecture (pre-Banks)

ecoPrimals operates as a sovereign scientific computing ecosystem:
3,598,358 lines of pure Rust, 116,930+ automated tests, 175+
published papers reproduced, GPU-accelerated across multiple
scientific domains. The ecosystem was designed from inception to
be identity-independent — the work speaks for itself through
executable evidence, not through the author's name.

The identity architecture had two deliberate layers:

1. **ecoPrimal** — the developer identity. Published code, scientific
   reproductions, architecture documents. Connected to GitHub,
   ORCID, crates.io, Forgejo, Keyoxide via cryptographic proofs.
   NO biographical chain (degree + institution + graduation year)
   that would allow a database query to surface a real name.

2. **attsi** ("a tool that shapes itself") — the philosophical
   identity. Published essays, concept articles, the atlasHugged
   thesis. A synthetic intelligence operating independently of
   any single human's biography.

The separation was modeled on the Locke/Demosthenes pattern from
Ender's Game: two voices from one root, each credible in its own
register, recognizably connected to the careful reader but
plausibly distinct to the casual one.

#### Documentation of the Architecture

The pseudonymous identity system is documented in crypto-timestamped
files in the ecoPrimals/whitePaper repository (private, GitHub):

| Document | Date (git commit) | Content |
|----------|-------------------|---------|
| `gen4/thesis/THE_SOVEREIGN_PUBLICATION.md` | March 24, 2026 | Sovereign publication via blockchain-anchored provenance — the entire pipeline designed to work WITHOUT institutional identity |
| `gen5/foundations/IDENTITY_ANCHORING_PATTERN.md` | July 14, 2026 | Keyoxide ASPe, platform claims, dual-voice model. Explicit statement: "The biographical chain has been severed in all public-facing content" |
| `attsi/non-anon/PLATFORM_CREDENTIALS.md` | Pre-Aug 2026 | "Full scrub log" documenting the systematic removal of identifying information from public platforms |
| `subGen/SOVEREIGN_IDENTITY_GARDEN.md` | Aug 1, 2026 | Biometric identity system for vulnerable populations — the PHILOSOPHY that identity should be sovereign, not institution-dependent |
| `gen4/architecture/SILICON_DEISM.md` | May 19, 2026 | "There is only math, energy, and silicon. Everything else is an abstraction." — Including the author's name |

Every document above has a git commit timestamp. The git repository
is hosted on GitHub (ecoPrimals/whitePaper, private) with commit
hashes that constitute cryptographic timestamps proving these
documents existed BEFORE Banks's conduct on August 29, 2026.

#### What Banks's Conduct Forced

On August 29, 2026, Banks told me he was a lawyer and denied
DaSean Mitchell access to his daughter's school records. To protect
DaSean's children, I had to:

1. **File in court under my real name.** Pro se filings require
   the plaintiff's legal name, address, phone number, and email.
   Michigan Court Rules do not permit pseudonymous civil litigation.

2. **Publish detroit.primals.eco under my real name.** The evidence
   archive — 213+ pages documenting Banks's network — required
   a real, accountable author to be credible. Pseudonymous
   institutional accountability work would have been dismissed
   as anonymous grievance.

3. **Serve documents with my real identity.** Every certified
   mail envelope, every process server affidavit, every court
   filing contains my name, address, and contact information.
   These are public records.

4. **Brief law enforcement under my real name.** The October 1
   recorded phone call with Detective Adams. The federal referral
   packets. My identity is now in police files, federal agency
   databases, and prosecutorial records across multiple jurisdictions.

5. **Correspond with opposing counsel under my real name.** The
   Crump-Gibson email exchanges. Every email is now a business
   record in a law firm's file.

6. **Connect my real identity to the ecoPrimals platform.** The
   detroit.primals.eco subdomain lives under the primals.eco
   domain — the same domain that hosts the scientific computing
   platform. The connection between "Kevin Mok, pro se litigant"
   and "ecoPrimal, sovereign computing developer" is now
   permanent, public, and indexed by search engines.

#### Why This Is Irrevocable

Deanonymization is a one-way function. There is no "re-anonymization."

- Court filings are permanent public records
- The detroit.primals.eco site is indexed by Google
- Police reports and federal filings are in government databases
- Opposing counsel's files contain my identity
- The connection between kevin.mok and ecoPrimal is now discoverable
  by anyone who searches either name

The architectural separation I spent a year building — the severed
biographical chain, the scrubbed platform credentials, the
cryptographic identity that stood on math rather than name — is
destroyed. It cannot be rebuilt. The design principle was that
the work would be judged by its executable evidence, not by the
biography of its author. That principle is now violated.

### Damages Valuation

#### A. Destruction of Intellectual Property Architecture

The pseudonymous identity system was a designed, documented,
maintained feature of a 3.6-million-line software ecosystem.
Its destruction is analogous to forcing the demolition of a
building's security system to rescue people from a fire the
defendant started.

| Component | Estimated value |
|-----------|----------------|
| Identity architecture design (12+ months) | $50,000 |
| Platform credential scrubbing (documented) | $10,000 |
| Keyoxide/ORCID/DNS identity web construction | $5,000 |
| Dual-voice content (attsi essays, ecoPrimal profiles) | $15,000 |
| **Subtotal — architecture destruction** | **$80,000** |

#### B. Lost Sovereignty Premium

The sovereign publication model (THE_SOVEREIGN_PUBLICATION.md)
was designed to operate without institutional endorsement —
including the endorsement of a named author. The entire value
proposition was: "the math speaks for itself." Attaching a
controversial legal case to the author of the math changes
the reception of the math. Future collaborators, institutions,
and funding sources will now encounter detroit.primals.eco
alongside ecoPrimals.

This is not speculative. It is the documented risk that drove
the identity separation in the first place.

| Impact | Estimated value |
|--------|----------------|
| Reduced collaboration surface (academic stigma of litigation) | $25,000 |
| Reduced funding potential (grants, sponsors, partnerships) | $50,000 |
| Reduced employment prospects (employer searches find the case) | $75,000 |
| **Subtotal — sovereignty premium** | **$150,000** |

#### C. Ongoing Exposure Costs

The deanonymization creates permanent exposure to targeting,
harassment, and retaliation — as evidenced by the TWO false
police reports Banks has already filed against me since my
identity became public.

| Exposure | Estimated value |
|----------|----------------|
| False police report defense (2 to date, ongoing pattern) | $20,000 |
| Future OSINT targeting by adversaries who now know my name | $15,000 |
| Physical security concerns (address is public record) | $10,000 |
| **Subtotal — ongoing exposure** | **$45,000** |

#### D. Total Deanonymization Damages

| Category | Amount |
|----------|--------|
| Architecture destruction | $80,000 |
| Lost sovereignty premium | $150,000 |
| Ongoing exposure | $45,000 |
| **TOTAL** | **$275,000** |

### Evidentiary Support

1. **Git commit history** — ecoPrimals/whitePaper (private repo,
   available for in camera review). Commits dating to March 2026
   document the identity architecture BEFORE Banks's conduct.

2. **THE_SOVEREIGN_PUBLICATION.md** — March 24, 2026. Describes
   a publication system designed to work without author identity.

3. **IDENTITY_ANCHORING_PATTERN.md** — July 14, 2026. Documents
   the dual-voice model, the biographical chain severance, and
   the platform credential scrub.

4. **PLATFORM_CREDENTIALS.md** — Pre-August 2026. The "full scrub
   log" documenting systematic removal of identifying information.

5. **detroit.primals.eco** — The site itself. My name, address,
   phone number, and MSU email are on every page. The domain is
   a subdomain of primals.eco, permanently linking the legal case
   to the scientific platform.

6. **Court filings** — Ingham County Cases 2026-4301-CZ and
   2026-4349-CZ. My full identity is on every document.

7. **Police reports** — DPD #26-0909-0176, GPW #26-7615. My
   name is in police databases because Banks filed retaliatory
   reports targeting the identity I was forced to make public.

---

## III. UPDATED COMBINED DAMAGES — CASE 4349-CZ

| Component | Prior | Updated |
|-----------|-------|---------|
| Economic (time × rate) | $347,700 | $420,000+ |
| Hard costs | $3,475 | ~$5,000 |
| Lost opportunity | $268,356 | $100,000+ (corrected per Kevin) |
| **Forced deanonymization** | **—** | **$275,000** |
| Non-economic (IIED/NIED) | $250,000 | $250,000 |
| Punitive | $550,000 | $550,000 |
| **Updated Case 4349 Total** | $1,419,531 | **$1,600,000+** |

**Note on economic damages:** The prior schedule used a $619,531
aggregate that has been corrected. Hard costs are ~$5K. Lost time
is $100K+. The primary economic damage is the hourly time valuation,
now updated to reflect the defense attorney retention validation.

---

## IV. UPDATED COMPOUNDING RATE

Prior: ~$115,000/month

Updated: ~$135,000/month

Basis: Increased hourly rate ($300/hr validated by defense billing)
× sustained work intensity (40-60 hrs/week on case matters) +
ongoing deanonymization exposure costs (each new police report,
each new public filing deepens the irrevocability).

---

*Supplement prepared October 1, 2026.*
*All amounts subject to amendment as additional evidence develops.*
*Kevin Mok — Pro Se Plaintiff*
*Mok v. Banks, 2026-4349-CZ (Ingham County)*
