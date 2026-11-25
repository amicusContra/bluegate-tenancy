# DAMAGES FRAMEWORK — Mok v. Banks, 2026-4349-CZ
## Quantified Lost Income, Disrupted Work, and Recoverable Costs
## Prepared: September 11, 2026 | Kevin Mok, Pro Se
## For Trial Preparation — Jury Demand Filed

---

## I. THEORY OF DAMAGES

Kevin Mok is a senior scientific software engineer, U.S. Army infantry veteran,
and MSU graduate (MS Data Science, BS Microbiology) who was actively building
a distributed scientific computing platform — ecoPrimals — while maintaining
active research collaborations with PhD faculty at Michigan State University
and consulting with domain scientists in PFAS chemistry, pharmacology, drug
discovery, and computational physics.

Defendant Brian Roderick Banks, through his unauthorized practice of law,
tortious interference with Kevin's friend DaSean Mitchell's parental rights,
and pattern of fraud and intimidation, forced Kevin to divert his full
professional capacity from productive scientific work to a multi-front legal
campaign to protect children and hold accountable a network of actors who
should have been stopped by the very institutions they serve.

Every hour Kevin spent filing complaints, drafting FOIAs, preparing exhibits,
researching case law, and coordinating service of process is an hour he did
not spend writing code, running experiments, collaborating with scientists,
or advancing toward funded research. The loss is not speculative — it is
documented by immutable timestamps across 44 public GitHub repositories
spanning 14+ months of continuous development that came to a measurable halt
when Banks' conduct forced Kevin's intervention.

---

## II. PLAINTIFF'S PROFESSIONAL PROFILE

### Education & Military Service

| Credential | Institution | Date |
|-----------|------------|------|
| MS, Data Science | Michigan State University | 2023-2025 |
| BS, Microbiology (Minor: Bioethics) | Michigan State University | 2018 |
| Infantryman, Company Intelligence Support Team (COIST) | U.S. Army, 25th Infantry Division, Schofield Barracks HI | 2012-2015 |

### Professional Experience

| Position | Employer | Period | Relevance |
|----------|----------|--------|-----------|
| Research Specialist | MSU PFAS Research Lab | Oct 2024 - Oct 2025 | Environmental chemistry, EPA protocols, data science |
| Research Fellow | Sandia National Laboratories | Summer 2024 | National lab, security clearance, bioinformatics |
| Biotechnician | MSU Bioeconomy Institute (MSUBI) | Jan 2019 - May 2024 | 5+ years BSL2 lab, fermentation, assay development |
| Research Assistant | Hausbeck Plant Pathology Lab, MSU | May 2018 - Jan 2019 | Field + lab research |
| Undergraduate Research | ROME Lab, MSU | Jan 2018 - May 2018 | UURAF presentation |

### Technical Capabilities

| Skill Area | Specifics |
|-----------|-----------|
| **Primary Language** | Rust (systems programming — millions of lines across 44 repos) |
| **Scientific Domains** | Computational physics (lattice QCD), bioinformatics (metagenomics), analytical chemistry (PFAS), pharmacology (drug discovery), precision agriculture, neuromorphic computing |
| **Infrastructure** | Distributed systems, cryptography (TLS 1.3, Ed25519, post-quantum ML-KEM), GPU compute (Vulkan, CUDA), mesh networking, content-addressed storage |
| **Hardware** | 11-node home compute cluster, 154+ CPU cores, ~1 TB RAM, 248 GB GPU VRAM, 122 TB storage, 3× neuromorphic processors, 10G backbone |
| **Also** | Python, R, SQL, Visual Basic, bioinformatics pipelines, mass spectrometry, HPLC |

---

## III. THE WORK PRODUCT — ecoPrimals ECOSYSTEM

### A. GitHub Organizations — 44 Public Repositories

#### ecoPrimals (22 repos) — Sovereign Distributed Computing
15 Pure Rust daemons for cryptography, networking, storage, GPU compute, and provenance.

| Repo | Size | Description |
|------|------|-------------|
| bearDog | 654 MB | Pure Rust cryptography — TLS 1.3, Ed25519, X25519, BLAKE3, ML-KEM post-quantum, Tor v3 |
| songBird | 378 MB | Pure Rust mesh networking — mDNS discovery, NAT traversal, WireGuard overlay |
| sporePrint | 63 MB | Website and publication infrastructure |
| toadStool | 60 MB | GPU/NPU/CPU compute dispatch — Vulkan f64, thermal-aware scheduling |
| nestGate | 42 MB | Content-addressed storage — B-tree indices, journal WAL, ZFS tiering |
| wateringHole | 37 MB | Standards and specifications (Python) |
| biomeOS | 34 MB | Orchestration kernel — process supervision, deploy graphs |
| squirrel | 29 MB | AI coordination — MCP server, multi-provider inference routing |
| barraCuda | 14 MB | GPU statistics library |
| coralReef | 14 MB | GPU compute framework |
| + 12 more | — | loamSpine, rhizoCrypt, sweetGrass, petalTongue, sourDough, skunkBat, plasmidBin, bingoCube, swarmVine, benchScale, agentReagents |

#### syntheticChemistry (12 repos) — Scientific Validation
175+ academic papers reproduced and validated on commodity GPUs.

| Repo | Size | Description |
|------|------|-------------|
| hotSpring | 114 MB | Computational physics — lattice QCD, molecular dynamics, fluid mechanics. 850+ tests, 85+ shaders, 74 experiments |
| wetSpring | 15 MB | Metagenomics, analytical chemistry, mathematical biology. 1,750+ tests, 5,700+ validation checks |
| neuralSpring | 14 MB | ML pipelines — ESN, dose-response, PK modeling |
| primalSpring | 8 MB | NUCLEUS composition validation — 942 tests, 72 scenarios |
| airSpring | 6 MB | Precision agriculture — FAO-56 evapotranspiration, Richards equation |
| groundSpring | 6 MB | Measurement noise characterization — 35+ experiments, 930+ tests |
| healthSpring | 5 MB | Drug discovery — MATRIX repurposing, Anderson localization |
| ludoSpring | 3 MB | Game engine validation |
| + 4 more | — | benchScale, agentReagents, rustChip |

#### sporeGarden (10 repos) — Deployable Products

| Repo | Description |
|------|-------------|
| projectNUCLEUS | Single-command scientific cluster deployment |
| cellMembrane | Sovereign deployment — systemd, Caddy, WireGuard, USB enrollment |
| esotericWebb | Cross-evolution CRPG — LIVE at webb.primals.eco |
| projectFOUNDATION | Scientific lineage and validation targets |
| lithoSpore | Self-proving LTEE validation artifact — 229 tests, 7 papers |
| initioChem | Ab initio quantum chemistry — Hartree-Fock, DFT on consumer GPUs |
| blueFish | PFAS analytical QC tool |
| helixVision | Genomics product |
| metalForge | Materials science |
| + 1 more | |

**Aggregate code statistics:**
- **Total repositories**: 44
- **Total size**: 1.48 GB
- **Primary language**: Rust (42 of 44 repos)
- **License**: AGPL-3.0-or-later
- **Tests**: 4,000+ across springs
- **Validation checks**: 6,600+
- **Papers reproduced**: 175+
- **Shaders written**: 85+
- **Scientific experiments coded**: 100+

### B. Hardware Infrastructure — $15,000 Invested

| Node | CPU | GPU | RAM | Role |
|------|-----|-----|-----|------|
| eastGate | i9-12900 | RTX 4070 + Akida NPU | 32 GB DDR5 | Primary overwatch, neuromorphic |
| northGate | Ryzen 9 9950X3D | RTX 5090 | 96 GB DDR5 | Gaming + remote compute + AlphaFold |
| ironGate | i9-14900K | RTX 5070 | 96 GB DDR5 | Agentic development, composition validation |
| southGate | Ryzen 5800X3D | RTX 4060 | 128 GB DDR4 | Gaming + heavy compute |
| strandGate | Dual EPYC 7452 (64c/128t) | RTX 3090 + RX 6950 XT + Akida | 256 GB ECC | Bioinformatics powerhouse |
| biomeGate | Threadripper 3970X (32c/64t) | RTX 5060 + Titan V + Tesla K80 + Akida | 256 GB DDR4 | HBM2 test bench |
| westGate | i7-4771 | RTX 2070 Super | 32 GB DDR3 | 76 TB ZFS cold storage |
| swiftGate | Ryzen 5800X | RTX 3070 FE | 64 GB DDR4 | Mobile compute |
| flockGate | i9-13900K | RTX 3070 Ti | 64 GB DDR5 | NYC WAN mesh validation |
| kinGate | i7-6700K | RTX 3070 | 32 GB DDR4 | Staging/utility |
| blueGate | TBD | — | 128 GB DDR4 | Expansion |
| origin | Ryzen 5 6600H | — | 28 GB DDR5 | Router/firewall/NUCLEUS |
| 3× Intel NUC | Celeron J3455 | — | — | Relay/discovery nodes |
| grapheneGate | Tensor G3 | — | — | Mobile mesh (Pixel 8a/GrapheneOS) |

**Work card pool**: 2× RTX 3090, 2× Titan V (HBM2), 2× AMD MI50 (HBM2), Tesla K80 — 128 GB aggregate work VRAM.

**Networking**: 10G backbone (MikroTik CRS310 + TP-Link Omada SFP+), WireGuard mesh overlay, 2× DigitalOcean VPS (NYC).

### C. Active Scientific Collaborations (Disrupted)

| # | Collaborator | Institution | Project | Status Before Disruption | Estimated Value |
|---|-------------|------------|---------|-------------------------|----------------|
| 1 | **Dr. Andrea Gonzales** | MSU Pharmacology & Toxicology | GPS platform rebuild (assigned Jun 5); NF data mining; CTF NDU grant application | Active — task assigned, meeting completed | **$125,000** (grant: $50K Y1 + $75K Y2) |
| 2 | **Prof. Murillo** | MSU CMSE | Neuromorphic computing, hardware access for research | Active — outreach sent, hardware offered | Collaboration value |
| 3 | **Dan Jones** (retired) | MSU PFAS Lab | blueFish consulting — PFAS analytical QC tool | Active — email exchange, domain guidance received | Consulting pipeline |
| 4 | **Dr. Eaves** | MSU | Compute access offer, paper review and validation targets | Active — zoom follow-up, revalidation offer | Collaboration value |
| 5 | **Dr. Chuna** | — | arXiv lattice QCD preprint, guideStone delivery | Active — review package sent, preprint in progress | Publication credit |
| 6 | **Dr. Kachkovskiy** | MSU Mathematics | Review package for lattice QCD work | Active — review package prepared | Peer validation |
| 7 | **Dr. Lisabeth** | MSU | Computational brief, binding landscape, drug discovery connection | Active | Collaboration value |
| 8 | **Dr. Huntley** | — | Cold outreach for computational collaboration | Initiated | Potential collaboration |
| 9 | **Valve / Inkfish** | Industry | Infrastructure/gaming role outreach (resume + strategy prepared) | Drafted — outreach paused | Industry opportunity |

**Key evidence**: Dr. Gonzales assigned Kevin a concrete deliverable on June 5, 2026 — rebuild the GPS drug screening platform as a sovereign "pseudoSpore." This was an active, in-progress task with a PhD faculty member at a major research university, tied to a grant application worth up to $125,000. The work stopped because Banks made Kevin fight a legal battle instead.

### D. Live Services (Running on Infrastructure)

| Service | URL | Description |
|---------|-----|-------------|
| primals.eco | https://primals.eco | Project website — papers, methodology, K-NOME |
| lab.primals.eco | https://lab.primals.eco | JupyterHub — live computational environment, browse notebooks |
| webb.primals.eco | https://webb.primals.eco | esotericWebb CRPG — live game |
| metal.md | — | Technical documentation |
| golgi VPS | — | Forgejo, relay, Caddy TLS (21 repos full-depth mirror) |

---

## IV. THE WORK STOPPAGE — TIMESTAMPED EVIDENCE

### GitHub Push History — The Cliff

All timestamps are UTC from GitHub's API (immutable, cannot be fabricated or backdated).

**Final active pushes across 44 repos:**

| Date | Repos Pushed | Activity |
|------|-------------|----------|
| Aug 18, 2026 | toadStool | GPU compute dispatch |
| Aug 17, 2026 | hotSpring, sporePrint, cellMembrane | Physics validation, website, deployment |
| Aug 16, 2026 | coralReef, biomeOS, primalSpring | GPU framework, orchestration, composition validation |
| Aug 13, 2026 | neuralSpring | ML pipeline |
| Aug 11, 2026 | wetSpring, projectNUCLEUS, esotericWebb | Biology, deployment product, game |
| Aug 10, 2026 | projectFOUNDATION, lithoSpore | Science lineage, LTEE artifact |
| Aug 08, 2026 | airSpring, groundSpring, ludoSpring, healthSpring, squirrel, skunkBat, bingoCube | 7 repos in one day |

**Then — silence.**

| Date | Event | Repos Pushed |
|------|-------|-------------|
| **Aug 14** | Shayla files response — custody crisis escalates | Work slowing |
| **Aug 18** | Last substantial code push (toadStool) | **LAST DAY** |
| Aug 29 | Banks denies DaSean access to children at PCA | — |
| **Aug 31** | Kevin files Mok v. Banks (2026-4349-CZ) + State Bar UPL + JTC ×5 | **ZERO code** |
| Sep 1-10 | 58 tracked legal items: filings, complaints, FOIAs, service coordination | **ZERO code** |
| Sep 11 | wateringHole (minor/automated — standards update) | 1 trivial push in 24 days |

**The GitHub contribution graph will show:**
- ✅ **14+ months of continuous green** (June 2025 - August 2026)
- ❌ **Cliff to near-zero** (August 18, 2026 onward)
- 📄 **Corresponding surge in legal filings** (762 files, 147 MB of legal work product)

This is the damages exhibit. A jury does not need to understand Rust or lattice QCD. They need to see green squares stop and filings start.

---

## V. BILLABLE RATE ANALYSIS

### Market Rate for Kevin's Skill Set

| Factor | Impact on Rate |
|--------|---------------|
| **Rust** (primary language) | Premium language — 10% of Rust roles pay $200K+/yr (Stack Overflow survey). Freelance Rust: $150-300/hr. |
| **Systems programming** (distributed, crypto, networking) | Senior systems engineer: $175-275/hr |
| **Scientific computing** (physics, chemistry, biology) | Domain specialization premium: +$25-50/hr |
| **GPU/HPC** (Vulkan, CUDA, HBM2, neuromorphic) | Specialized hardware expertise: +$25-50/hr |
| **National lab experience** (Sandia) | Credibility + clearance history |
| **Military veteran** | Discipline, security clearance eligibility |
| **MS + BS (MSU)** | Graduate-level credentials |

### Comparable Market Rates (2026)

| Source | Rate Range |
|--------|-----------|
| Rust freelance (Toptal, Upwork top-tier) | $150-300/hr |
| Scientific computing consultant | $175-350/hr |
| Senior systems engineer (W-2 equivalent) | $200K-350K/yr ($100-175/hr) |
| Infrastructure engineer with security specialization | $175-300/hr |

### Claimed Rate: **$200/hour (conservative)**

This is below the midpoint of Kevin's market range. A specialist Rust engineer
with scientific domain expertise, national lab credentials, military service,
and a functioning 11-node compute cluster would command $250-300/hr in the
open market. The $200/hr rate is deliberately conservative for jury credibility.

---

## VI. DAMAGES CALCULATION

### A. Lost Income — Hours Diverted from Productive Work

The disruption was progressive, not sudden. GitHub commit data shows:
- **Peak output**: Jun 2-8, 2026 (118 commits/week across 5 repos)
- **Father's Day (Jun 21)**: DaSean served — output cut in half (37 commits)
- **Late June**: 88% collapse (9 commits/week)
- **July-August**: Degraded capacity — splitting time between reduced code and legal prep
- **August 18**: Complete code stop — all 44 repos go silent
- **August 31**: Formal legal campaign begins

| Period | Days | Hours/Day Diverted | Total Hours | × $200/hr | Subtotal |
|--------|------|-------------------|-------------|-----------|----------|
| May 1 - Jun 20 (escalating disruption) | 51 | 3 (partial diversion) | 153 | $200 | **$30,600** |
| Jun 21 - Aug 17 (post-Father's Day, degraded capacity) | 57 | 6 (majority diversion) | 342 | $200 | **$68,400** |
| Aug 18 - Aug 31 (complete stop, pre-filing) | 13 | 10 | 130 | $200 | **$26,000** |
| Sep 1 - Sep 10 (filing blitz) | 10 | 12 | 120 | $200 | **$24,000** |
| Sep 11 - Oct 9 (through CMC hearing) | 29 | 8 | 232 | $200 | **$46,400** |
| Oct 10 - Dec 31 (through discovery/trial prep) | 82 | 6 | 492 | $200 | **$98,400** |
| **SUBTOTAL: Lost Income 2026** | **242 days** | — | **1,469 hours** | — | **$293,800** |

### B. Lost Grant & Research Income

| Opportunity | Value | Probability | Adjusted Value |
|------------|-------|-------------|---------------|
| Gonzales CTF NDU Grant (Y1) | $50,000 | 60% (task assigned, meeting completed, active relationship) | **$30,000** |
| Gonzales CTF NDU Grant (Y2) | $75,000 | 40% (contingent on Y1) | **$30,000** |
| Gonzales Lab Position (compound registration / AI role) | $55,000-75,000/yr | 50% (role floated, interest expressed) | **$30,000** |
| **SUBTOTAL: Lost Research Income** | | | **$90,000** |

### C. Hardware Depreciation While Idle

| Asset | Value | Annual Depreciation | Months Idle | Loss |
|-------|-------|-------------------|-------------|------|
| 11 compute towers + networking | $15,000 | 20% ($3,000/yr) | 5 months (Aug-Dec) | **$1,250** |
| Technology obsolescence premium | — | Additional 10% for GPU/NPU | 5 months | **$625** |
| **SUBTOTAL: Hardware** | | | | **$1,875** |

### D. Out-of-Pocket Costs (Recoverable)

| Category | Amount | Documentation |
|----------|--------|---------------|
| Ingham County filing fee (2026-4349-CZ) | ~$260 | Court receipt |
| Ingham County filing fee (2026-4301-CZ) | ~$260 | Court receipt |
| Process service — ABC (4 orders) | ~$2,700 | Invoices, CC statements |
| Certified mail (JTC ×10, AG, MDE) | ~$150 | USPS receipts, green cards |
| First class mail + PS Form 3665 (×2 batches) | ~$50 | USPS receipts |
| Postage (ongoing) | ~$50 | Receipts |
| PACER fees | ~$30 | PACER account |
| Police report | $10 | Receipt pending |
| Printing (600+ pages) | ~$100 | — |
| **SUBTOTAL: Out-of-Pocket** | | **~$3,610** |

### E. Lost Project Momentum (Non-Pecuniary but Demonstrable)

| Factor | Evidence |
|--------|---------|
| 14-month continuous development streak broken | GitHub contribution graph |
| 9 scientific collaborations stalled | Email chains with timestamps |
| arXiv preprint delayed | Dr. Chuna correspondence |
| Drug discovery platform rebuild paused | Gonzales Jun 5 meeting notes |
| PFAS QC tool development frozen | Jones correspondence |
| Neuromorphic computing research paused | Murillo correspondence |
| Valve/industry outreach abandoned | Drafted emails in attsi/non-anon/contact/ |
| Student/researcher access to lab.primals.eco degraded | Server logs |
| Reputation cost — collaborators left waiting | Demonstrable |

### F. Emotional Distress

| Factor | Evidence |
|--------|---------|
| Veteran forced to abandon scientific work to fight fraud | Testimony |
| Sleep disruption, sustained 2-2.5× work tempo for weeks | Documented |
| Witnessing friend's children denied to their father | Ring camera footage, testimony |
| Assault of friend and friend's mother on camera | Video evidence, police report |
| Ongoing threat and retaliation from convicted felon | Banks' emails, "harassment" claim |

---

## VII. DAMAGES SUMMARY

| Category | Amount |
|----------|--------|
| **A. Lost Income (hours diverted, May-Dec 2026)** | **$293,800** |
| **B. Lost Grant & Research Income** | **$90,000** |
| **C. Hardware Depreciation** | **$1,875** |
| **D. Out-of-Pocket Costs** | **$3,610** |
| **E. Lost Momentum** | **TBD at trial** |
| **F. Emotional Distress** | **TBD at trial** |
| **TOTAL QUANTIFIED DAMAGES** | **$389,285** |
| **With momentum + distress** | **$450,000 - $600,000** |

### Treble Damages Note

Under Michigan's consumer protection statute (MCL 445.911) and common law
fraud remedies, exemplary/treble damages may apply where defendant's conduct
was willful, wanton, or malicious. Banks' 8 prior felony convictions, his
continued UPL after being caught, and his self-incriminating reply-all
demonstrate a pattern of knowing misconduct.

**If treble damages applied to quantified losses: $1,167,855**

---

## VIII. EVIDENCE PRESERVATION CHECKLIST

| Evidence | Location | Status |
|----------|----------|--------|
| GitHub commit history (all 44 repos) | github.com/ecoPrimals, syntheticChemistry, sporeGarden | ✅ Public, immutable |
| GitHub contribution graph (visual) | GitHub profile | ✅ Screenshot needed |
| Gonzales email chain | eco.primal@pm.me | ✅ Preserve |
| Gonzales meeting notes (Jun 5) | whitePaper/attsi/non-anon/contact/gonzales/ | ✅ On disk |
| Murillo email | whitePaper/attsi/non-anon/contact/murillo/ | ✅ On disk |
| Jones emails | whitePaper/attsi/non-anon/contact/pfas/ | ✅ On disk |
| Eaves correspondence | whitePaper/attsi/non-anon/contact/eaves/ | ✅ On disk |
| Chuna correspondence | whitePaper/attsi/non-anon/contact/chuna/ | ✅ On disk |
| Hardware receipts | Purchase records | ⚠️ Compile |
| Hardware inventory | whitePaper/technical/HARDWARE_INVENTORY.md | ✅ On disk |
| Self-employment filing prep | whitePaper/concrete/SELF_EMPLOYMENT.md | ✅ On disk |
| Legal work product (762 files) | bluegate-tenancy/01-case/ | ✅ Git tracked |
| Banks' reply-all (self-incriminating) | evidence/BANKS_RESPONSE_SEP10_*.png | ✅ Preserved |
| Process service invoices | ABC Process Service emails | ✅ Email |
| USPS receipts + green cards | filing-ready/receipts/ | ✅ Physical + scanned |
| Resume | whitePaper/attsi/non-anon/resume.md | ✅ On disk |

---

## IX. JURY NARRATIVE

> *"I'm a scientist. I'm a veteran. For two years I was building something —
> a distributed computing platform for scientific research. Forty-four
> repositories. Millions of lines of code. Eleven machines in my house.
> PhD researchers at Michigan State were using my work. A grant application
> was in progress. An arXiv preprint was being reviewed.*
>
> *Then a convicted felon who calls himself a lawyer told my best friend he
> couldn't see his own daughters. And the judges on that felon's school board
> looked the other way. And the assistant attorney general on his board did
> nothing. And the attorney who represents him filed no ethics reports.*
>
> *So I stopped building and started fighting. Not because I wanted to —
> because nobody else was going to. Every hour I spent in this courtroom,
> every filing, every exhibit, every stamp on every envelope — that's an
> hour I didn't spend on the work I was put on this earth to do.*
>
> *I'm not asking you to understand Rust code or lattice QCD. I'm asking
> you to look at the timestamps. Look at the green squares on that graph.
> Watch them stop. Then look at the filing dates. Watch them start. And
> tell me who owes whom.*"

---

*DAMAGES_FRAMEWORK v1.0 — September 11, 2026*
*Sources: GitHub API, whitePaper/technical/HARDWARE_INVENTORY.md, whitePaper/attsi/non-anon/,
whitePaper/concrete/SELF_EMPLOYMENT.md, bluegate-tenancy/01-case/strategy/active/*
