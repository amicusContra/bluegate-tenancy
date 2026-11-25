# NETWORK ANALYSIS — Topology Findings
## September 5, 2026 | Post-LinkedIn Scrub
## 32 nodes, 68 edges | Graph data: NETWORK_TOPOLOGY.json

---

## CLUSTER ANALYSIS

### Cluster 1: BANKS ENTERPRISE (Core Hub)
**Nodes:** Banks, Holland, Ellis, Purpose Group, Purpose Foundation, Banks Strategy, PCA, MacDowell, Yecart, Banks Living Trust
**Hub node:** Banks (highest degree centrality — 10+ direct edges)
**Key:** Banks connects to every other cluster through at least 2 edges. This is the nucleus.

### Cluster 2: PCA BOARD (Governance Layer)
**Nodes:** Miller, Moreland, L. Johnson, Hutchings, Clora
**Bridge node:** Miller (connects Cluster 2 → Cluster 1 via board chair + Perkins legal link)
**Key:** Every PCA board member holds a separate day job that creates institutional conflicts:
- Miller = sitting judge
- Moreland = Asst. Attorney General
- L. Johnson = City Council
- Hutchings = SuperPAC chair
- Clora = funeral home CEO with murder acquittal

### Cluster 3: WAYNE COUNTY GOVERNMENT (Political Cover)
**Nodes:** E. Sabree, Evans, A. Sabree, Al. Sabree
**Bridge node:** E. Sabree (connects Cluster 3 → Clusters 1+2 via endorsements + tax actions)
**Key:** Family dynasty; father controls tax enforcement, son and daughter sit on the courts, all endorse Banks/Miller/Yancey.

### Cluster 4: 36TH DISTRICT COURT (Judicial Crossroads)
**Nodes:** Yancey, A. Sabree, S. Perkins
**Bridge nodes:** Yancey (→ Cluster 1 via MacDowell + campaign payments); S. Perkins (→ Cluster 1 via brother Todd)
**Key:** THREE judges on the same bench connected to the Banks network. Yancey + Adam Sabree elected same 2022 ballot.

### Cluster 5: 3RD CIRCUIT COURT (Power Bench)
**Nodes:** Miller, Al. Sabree
**Bridge node:** Miller (→ Clusters 1+2+4)
**KEY:** The judge-chair of Banks' school now shares a bench with the Treasurer's daughter. Aliyah is in Family Division—Domestic = custody cases.

### Cluster 6: FINANCIAL PIPELINE (Campaign Money)
**Nodes:** Inner Link Graphics, McCastle, Lewis, Hutchings/MI Deserves Better PAC, Banks Strategy PAC
**Hub node:** Inner Link Graphics ($98K+ entity; touches every campaign committee)
**Key:** Money flows from multiple committees through 2 vendors (Inner Link, McCastle) who both have unremarkable day jobs and no LinkedIn acknowledgment of campaign work.

### Cluster 7: CHILDREN'S CENTER (Hidden Link)
**Nodes:** Stallworth (CEO), Ellis (CFO)
**Key:** Two people from Banks' charter enterprise share a SEPARATE employer — financial and governance overlap at both MacDowell/PCA AND The Children's Center.

---

## BRIDGE ANALYSIS (Nodes That Connect Clusters)

| Bridge Node | Clusters Connected | Edge Count | Risk Level |
|-------------|-------------------|------------|------------|
| **Banks** | 1↔2↔3↔4↔6 | 12+ | CENTRAL — removing Banks disconnects most clusters |
| **Miller** | 1↔2↔5 | 7 | HIGH — judge + board chair = structural link |
| **E. Sabree** | 3↔1↔2↔4 | 8 | HIGH — tax power + endorsements + family dynasty |
| **Perkins** | 1↔4↔5 (via Miller + S. Perkins) | 4 | MEDIUM — attorney link but no public PCA tie found |
| **Stallworth** | 1↔7 | 5 | MEDIUM-HIGH — connects charter world to Children's Center |
| **Yancey** | 1↔4↔6 | 7 | HIGH — board chair + campaign money + bench |
| **Gay-Dagnogo** | 2↔1↔3 (via Holland payment) | 4 | MEDIUM — development + authorization + financial |
| **Hutchings** | 2↔6 | 4 | MEDIUM — PCA Treasurer + SuperPAC Chair |

---

## DEGREE CENTRALITY (Sorted by Connection Count)

| Rank | Node | Degree (edges) | Type |
|------|------|----------------|------|
| 1 | Banks | 12 | Person — hub |
| 2 | E. Sabree | 8 | Person — political cover |
| 3 | Miller | 7 | Person — judge |
| 4 | Yancey | 7 | Person — judge |
| 5 | Ellis | 6 | Person — financial ops |
| 6 | Stallworth | 5 | Person — governance |
| 7 | Holland | 4 | Person — trust/PAC |
| 8 | Perkins | 4 | Person — legal |
| 9 | Inner Link | 4 | Entity — money hub |
| 10 | Hutchings | 4 | Person — PAC |

---

## KEY TOPOLOGY PATTERNS

### Pattern 1: DUAL EMPLOYMENT OVERLAP
```
The Children's Center
  ├── CEO: Nicole Wells Stallworth ──→ MacDowell Board Chair
  └── CFO: Tracey D. Ellis ──→ MacDowell Business Manager + Purpose Foundation Treasurer
```
**Same people, two organizations, one money pipeline.** Ellis controls the books at both the nonprofit and the charter school. Stallworth governs both.

### Pattern 2: FAMILY DYNASTY COVERAGE
```
Eric Sabree (Treasurer)
  ├── Son: Adam Sabree (36th District Judge) — same bench as Yancey + S. Perkins
  ├── Daughter: Aliyah Sabree (3rd Circuit Judge) — same bench as Miller
  └── Tax actions on: Banks property, Miller property, Yancey property
```
**The father endorses the network. His children sit on the courts where the network's members preside.**

### Pattern 3: 36TH DISTRICT CONCENTRATION
```
36th District Court (2026)
  ├── Tenisha Yancey — MacDowell Board Chair; $15K to Banks PAC
  ├── Adam Sabree — Treasurer's son; litigated for father's dept
  └── Sean Perkins — Brother of Banks' attorney
```
**Three of the judges on one court have direct family or board ties to the Banks network.**

### Pattern 4: CAMPAIGN MONEY CIRCULATION
```
Banks for Senate ──$39K──→ Inner Link Graphics
Bank on Banks PAC ──$10K──→ Inner Link Graphics
MI Deserves Better PAC (Chair: Hutchings/PCA Treasurer) ──$37K──→ Inner Link Graphics
Yancey for State Rep ──$8K──→ Inner Link Graphics
                                     TOTAL: $98K+
```
**One vendor, multiple committees, all connected to one enterprise. Hutchings sits on the PCA board AND chairs a SuperPAC that feeds the same vendor.**

### Pattern 5: LAW SCHOOL PIPELINE
```
MSU College of Law / Detroit College of Law:
  ├── Banks (JD) ── Superintendent
  ├── Miller (JD 1996) ── PCA Board Chair
  ├── Sabree (JD 1996) ── Treasurer + endorser
  ├── Evans (JD) ── County Exec + endorser
  ├── Adam Sabree (JD 2011) ── 36th District Judge
  ├── Aliyah Sabree (JD 2010) ── 3rd Circuit Judge
  └── Moreland (education unlisted but Wayne County APA 2003)

Wayne State University Law:
  └── Perlmuter (JD 1992) ── Entity organizer

UDM Law:
  ├── Perkins (JD) ── Banks' attorney
  └── Yancey (JD) ── MacDowell Board Chair
```
**MSU Law / Detroit College of Law is the dominant pipeline. Miller and Sabree were classmates (1996).**

### Pattern 6: INCOMPATIBLE PUBLIC OFFICES (MCL 15.181)
```
PCA Board members holding public office simultaneously:
  ├── Miller: 3rd Circuit Judge + PCA Board Chair
  ├── Moreland: Asst. Attorney General + PCA Vice Chair
  └── L. Johnson: City Council + PCA Secretary

MacDowell Board Chair holding public office:
  └── Yancey: 36th District Judge + MacDowell Board Chair
```
**Four violations of MCL 15.181 on charter school boards within the same enterprise.**

---

## NEXT STEPS FOR TOPOLOGY

### Immediate (Data Collection)
- [ ] Verify Inner Link Graphics ownership: LARA search "Inner Link" + SOS entity search
- [ ] Search for Larry Thomas Jr. LinkedIn connections — does he connect to Banks?
- [ ] Pull Sean Perkins court assignment data (36th District)
- [ ] Confirm Stallworth's brother Thomas F. Stallworth III — MSU Trustee bid = governor appointment network
- [ ] Children's Center 990 filing — is MacDowell/Purpose Group a vendor?

### Graph Build (Technical)
- [ ] Export JSON to D3.js or Gephi for visualization
- [ ] Assign edge weights for financial relationships (dollar-based)
- [ ] Calculate betweenness centrality for bridge analysis
- [ ] Generate neighbor graph (2-hop connections from Banks)
- [ ] Time-series edge creation (when relationships formed)

### RICO Implications
- [ ] Map edges that constitute "pattern of racketeering activity"
- [ ] Identify which edges are financial vs. governance vs. political
- [ ] Calculate total dollar flow through enterprise ($15K Yancey→PAC + $98K Inner Link + $232K PSCU mortgage + $93K HELOC + ...)
- [ ] Identify predicate acts per node

---

## GRAPH LEGEND (for visualization)

### Node Colors
- 🔴 Red: Banks inner circle (enterprise core)
- 🟠 Orange: Judges
- 🟡 Yellow: PCA Board
- 🟢 Green: Wayne County Officials
- 🔵 Blue: Entities/Organizations
- ⚪ Gray: Extended network

### Edge Types
- ━━━ Solid thick: Financial (>$5K)
- ─── Solid: Board/governance
- --- Dashed: Political (endorsement/campaign)
- ··· Dotted: Family
- ═══ Double: Employment overlap

### Edge Weights
- 10: Primary/direct (ownership, board chair, family)
- 7-9: Strong (employment, major financial, legal representation)
- 4-6: Moderate (endorsement, social, minor financial)
- 1-3: Weak (circumstantial, unverified)

---

*Topology analysis based on LinkedIn scrub + OSINT + PACER + ROD + Campaign Finance data.*
*All edges have documented source evidence. See LINKEDIN_SCRUB_SEP5.md for profile data.*
*Kevin Mok | guerillaGorilla STRIDe Cycle 4 | September 5, 2026*
