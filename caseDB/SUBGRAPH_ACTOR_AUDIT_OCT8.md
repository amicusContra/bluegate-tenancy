# SUBGRAPH ACTOR AUDIT — October 8, 2026
## New actors, entities, and edges identified from today's subgraph analysis

---

## STATUS KEY

- ✅ **ADDED TO DETROIT** — New page created, graph data updated, pushed
- 🔲 **TUEBOR CANDIDATE** — Statewide/cross-spectrum, belongs on tuebor.primals.eco
- 📋 **EXISTING PAGE** — Already documented, updated references
- 🔍 **RESEARCH NEEDED** — Identified but insufficient sourcing for a page

---

## I. NEW ACTOR PAGES ON DETROIT (pushed Oct 8)

| Actor | Page | Type | Key Connections |
|-------|------|------|----------------|
| **Tom Barrett** | `/network/political/tom-barrett/` | Political | Dykema PAC ($4K), MI-7, "convicted felon" attack while funded by felon infrastructure |
| **Bishop J. Drew Sheard** | `/network/institutional/sheard-drew/` | Institutional | COGIC Presiding Bishop (6.5M members), endorsed Banks for State Rep, Banks is his congregant |
| **Dykema Gossett PLLC** | `/network/entities/dykema-gossett/` | Entity | PA 362 (1993 charter law), SDJ formation, Barrett PAC ($4K), Miller former attorney, Ellison sanctions ($73K) |
| **Alexis Ramsey** | `/network/institutional/alexis-ramsey/` | Institutional | HP School Board Pres, gateway to MacDowell via Promise Schools, Judge Ramsey's daughter, 3 Ramseys on payroll |

## II. GRAPH DATA UPDATES (network-data.js v8)

### New Nodes (6)
| Node ID | Label | Community |
|---------|-------|-----------|
| `barrett` | Barrett | Dark Money (SDJ) |
| `sheard` | Bp. Sheard | Banks Enterprise |
| `alexis_ramsey` | A. Ramsey | MacDowell / CMU |
| `cogic` | COGIC | Banks Enterprise |
| `promise_schools` | Promise Schools | MacDowell / CMU |
| `dykema` | (updated — now has URL, expanded detail) | Dark Money (SDJ) |

### New Edges (12)
| Source → Target | Type | Flow |
|----------------|------|------|
| Dykema → Barrett | financial | $4,000 PAC donation |
| Dykema → SDJ | controls | formed entity (compliance@dykema.com) |
| Dykema → Miller | associate | former Dykema attorney |
| Sheard → Banks | political | endorsed for State Rep |
| Banks → COGIC | associate | congregant at Greater Emmanuel |
| Sheard → COGIC | controls | Presiding Bishop |
| Alexis Ramsey → Promise Schools | controls | "strongly suggested" hire Banks |
| Promise Schools → Banks | associate | hired via Ramsey push |
| Promise Schools → MacDowell | controls | operated 2015-2019 |
| Ramsey → Alexis Ramsey | family | daughter |
| Barrett → Banks | indirect | Dykema triangle — same infrastructure |

### About Page Updates
- **Jesus quote billboard** added: Mark 12:40 + Jeremiah 23:1
- **ecoPrimal Reading List** added: *Microbe Hunters* (de Kruif), *Eighth Day of Creation* (Judson), *Ones Who Walk Away from Omelas* (Le Guin)

### Network Index Updates
- Dykema Triangle section with table
- "Shepherds Who Scatter the Flock" section (Sheard, Alexis Ramsey)
- Updated Tiers listing with new actor links

---

## III. TUEBOR CANDIDATES — Statewide Actors for tuebor.primals.eco

These actors span beyond Detroit and belong on the statewide site:

### Cross-Spectrum (MSU Law 2010)
| Actor | Current Status | Tuebor Role |
|-------|---------------|-------------|
| **Philip L. Ellison** | On hemlock subgraph (caseDB SQL) | Statewide lattice node — MSU Law 2010 cohort with Banks |
| **Katie Ellison** | On hemlock subgraph | SISD President + Hemlock PS VP — education board capture |
| **Judge Gafkay** | On hemlock subgraph | 10th Circuit Chief Judge — SVSU adjunct overlap |

### Charter School Infrastructure
| Actor/Entity | Current Status | Tuebor Role |
|-------------|---------------|-------------|
| **CMU (charter authorizer)** | Detroit graph node (no page) | Statewide authorizer — Ellison MBA + MacDowell authorization |
| **SVSU (charter authorizer)** | Not on site | Authorizes charters + employs Ellison + employs Gafkay |
| **GVSU** | Detroit graph node | Largest Detroit charter authorizer (152 mi away) |
| **NHA** | Detroit graph node | 103 schools, 9 states, $1B+ revenue, Grand Rapids HQ |
| **Pahara Institute** | Referenced, no page | DC-based fellowship — validated Banks without background check |
| **Walden University** | Referenced, no page | Banks PhD — dissertation lists fake J.D. on cover page |

### Political/Federal
| Actor/Entity | Current Status | Tuebor Role |
|-------------|---------------|-------------|
| **Renae Moore** | Not on site | SDJ Asst Secretary + Dykema employee + Duggan compliance |
| **W. Alan Wilk** | Not on site | SDJ formation attorney + Dykema + Our Neighborhoods First + Duggan |
| **Kenneth Daniels** | Detroit graph node (no page) | SDJ director, Kilpatrick appointee, convicted |

### Religious/Nonprofit
| Actor/Entity | Current Status | Tuebor Role |
|-------------|---------------|-------------|
| **Greater Emmanuel Institutional COGIC** | Referenced | Sheard's church, Banks's congregation, event venue |
| **Go Tell It Evangelistic Ministry** | Not on site | Vaughn's ministry — DPSCD Board Pres + pastor dual role |
| **Great Lakes Vision for Evangelism** | Referenced | Banks-controlled religious entity — LARA 802210862 |

### Out-of-State
| Actor/Entity | State | Connection |
|-------------|-------|------------|
| **Pacific Legal Foundation** | CA (Sacramento) | Partnered with Ellison on Howard v. Macomb SCOTUS petition |
| **Tonesa Welch** | GA/MI | BMF "First Lady," Banks's aunt, BET+ film |
| **OD Banks** | Federal (BMF) | BMF Defendant #22, Banks's biological father |
| **Matthew Gronda** | MI (Saginaw) | Ellison's co-counsel, sanctioned in Garcia |

---

## IV. CHURCH LEADERS AND COMMUNITY ORGANIZERS — "Eating Their Own Flocks"

### Documented on detroit.primals.eco

| Person | Title | How They Consume the Flock |
|--------|-------|---------------------------|
| **Bp. J. Drew Sheard** | COGIC Presiding Bishop (6.5M) | Endorsed Banks for office — congregants' institutional weight lent to a felon |
| **Bp. Corletta Vaughn** | DPSCD Board Pres + Go Tell It Pastor | Authorized Banks's charter while leading a ministry — dual role, zero recusal |
| **Nicole Wells-Stallworth** | MacDowell Board Pres + CEO The Children's Center | Killed MDE investigation in 2hr 24min — the children's charity CEO protecting a felon who runs children's schools |

### Research Targets (unconfirmed, need verification)

| Person/Entity | Question |
|--------------|----------|
| **City Hill Church** (Banks) | What services does this church provide? Who attends? Is it operational or a LARA shell? |
| **Great Lakes Vision for Evangelism** (Banks) | Same questions. Two church entities at a felon's address with zero regulatory scrutiny. |
| **Other COGIC jurisdictional bishops** | Did the endorsement propagate through COGIC's hierarchy? |
| **BCF Michigan board** | "Mission: decrease drug use among youth" — board includes 3 convicted felons |

---

## V. PROPHETIC QUOTES ON THE BILLBOARD

Added to `about/_index.md` as epigraph:

> *"They devour widows' houses, and for a pretense make long prayers. These will receive the greater condemnation."* — **Mark 12:40**

> *"Woe to the shepherds who destroy and scatter the sheep of my pasture!"* — **Jeremiah 23:1**

### Additional quotes for future use:

| Quote | Source | Application |
|-------|--------|-------------|
| "Beware of false prophets, who come to you in sheep's clothing but inwardly are ravenous wolves." | Matthew 7:15 | Credential-washing pattern |
| "I hate, I despise your feasts... But let justice roll down like waters." | Amos 5:21-24 | CBC Week galas funded by school extraction |
| "Woe to you, scribes and Pharisees, hypocrites! For you are like whitewashed tombs." | Matthew 23:27 | Professional credential veneer over criminal record |
| "Is not this the fast that I choose: to loose the bonds of injustice?" | Isaiah 58:6 | The prophetic tradition vs. institutional self-preservation |

---

## VI. ecoPRIMAL READING LIST — Added to About page

| Book | Author | Year | Why It Matters |
|------|--------|------|----------------|
| ***Microbe Hunters*** | Paul de Kruif | 1926 | Citizen-scientist narrative. Leeuwenhoek was a cloth merchant. Koch was a country doctor. Discovery belongs to the person who looks, not the person with the title. |
| ***The Eighth Day of Creation*** | Horace Freeland Judson | 1979 | History of molecular biology. When the data contradicts the model, the model must change — regardless of who built the model. |
| ***The Ones Who Walk Away from Omelas*** | Ursula K. Le Guin | 1973 | Philosophical foundation of ecoPrimals. The child in the basement. What if you went back? (atlasHugged Ch. 1) |

Future additions to consider: *Silent Spring* (Carson), *The Structure of Scientific Revolutions* (Kuhn), *The Double Helix* (Watson), *Chance and Necessity* (Monod).

---

*Built: October 8, 2026 — ecoPrimal*
