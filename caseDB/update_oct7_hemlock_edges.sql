-- ============================================================
-- OCT 7, 2026 — HEMLOCK CROSS-SUBGRAPH EDGES
-- Connections between Hemlock investigation and other subgraphs
-- These edges are what make tuebor more than the sum of its parts
-- Run: sqlite3 caseDB.sqlite < update_oct7_hemlock_edges.sql
-- ============================================================

-- ============================================================
-- CROSS-SUBGRAPH: Hemlock ↔ Detroit
-- ============================================================

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('williams-rita', 'detroit-node', 'primary analytical reference',
    'Rita Williams / Clutch Justice is the primary analytical reference for detroit.primals.eco. She independently confirmed key findings in the Banks investigation. Her journalism on the Detroit side is what Ellison targeted with the SLAPP suit. The Hemlock harassment campaign is motivated by the Detroit investigation.'),

('ellison-philip', 'detroit-node', 'cross-county SLAPP pattern',
    'Ellison''s SLAPP against Rita mirrors the Banks/Holland PPO against Rita. Same target, different counties, different weapons. Banks uses PPOs and employer contact. Ellison uses defamation suits, fabricated witnesses, and domain campaigns. Both suppress the same journalism.'),

('foiaworks', 'detroit-node', 'intelligence collection nexus',
    'If Ellison operates FOIAworks as a surveillance platform, any FOIA request submitted through it about the Detroit investigation gives Ellison advance notice of what journalists are looking for. The FOIAworks → Detroit pathway is the intelligence leak vector.');

-- ============================================================
-- CROSS-SUBGRAPH: Hemlock ↔ Statewide Oversight
-- ============================================================

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('case-agc-25-2363', 'agc-statewide', 'same institution failing',
    'AGC dismisses 94% of complaints. Ellison AGC 25-2363 = OPEN but Ellison told Saginaw Circuit it was closed. AGC has not corrected the court record. Same AGC handles Banks/Moreland complaints from Detroit subgraph.'),

('gafkay-julie', 'scao-statewide', 'same oversight failure',
    'SCAO was notified of structural failures in Barry County (took years). SCAO has NOT been notified of the Gafkay/Ellison structural conflict in Saginaw. SCAO notification = next action item.'),

('case-slapp-williams', 'upepa-statewide', 'anti-SLAPP precedent',
    'UPEPA effective March 29, 2026. Rita filed UPEPA special motion May 6. Ellison ALSO invoked UPEPA in Consumers Energy case — judicial estoppel. The Hemlock SLAPP case is among the first UPEPA cases in Michigan. Precedent value for the entire state.');

-- ============================================================
-- OVERSIGHT CYCLES: Hemlock-specific
-- ============================================================

-- Cycle 1: School Board → FOIA → Court
-- Katie Ellison is VP of boards that control FOIA compliance
-- Philip Ellison operates FOIAworks (FOIA intelligence platform)
-- Philip Ellison files cases in court where Judge Gafkay (his colleague) presides
-- Gafkay signs orders based on evidence that Ellison may have obtained via surveillance
-- The school board that Katie controls promoted Philip as "Human of Hemlock"
-- RESULT: The board that should provide oversight is run by the wife of the attorney
--         whose surveillance platform collects intelligence on the journalists
--         who file FOIA requests about the board

-- Cycle 2: SVSU → Bar → Court
-- Ellison teaches at SVSU (adjunct professor since Aug 2017)
-- Gafkay teaches at SVSU (adjunct professor, overlapping 6+ years)
-- Gafkay is past president of SCBA (Saginaw County Bar Association)
-- Ellison is SCBA member
-- Gafkay is Chief Judge of 10th Circuit (where Ellison has 3 simultaneous cases)
-- RESULT: Colleague relationship at university → professional relationship at bar
--         → judge-attorney relationship at court. All the same two people.

-- Cycle 3: ISP → FOIA → Surveillance
-- Ellison's office IP = LakeNet (162.247.150.54, AS11910)
-- Quagmire Solutions served "Internet service companies" 2000-2007
-- LakeNet started 2010 in the same town of 2,000 people
-- FOIAworks collects who is requesting what records about which agencies
-- If Ellison has any administrative access to LakeNet infrastructure,
--   he can correlate FOIA requesters' browsing with their FOIAworks activity
-- RESULT: Infrastructure access + FOIA intelligence + legal weaponization
--         creates a complete surveillance-to-litigation pipeline

-- ============================================================
-- HEMLOCK COMMUNITIES (for Louvain detection)
-- ============================================================
-- Community 0: Ellison Family (Philip, Katie, Calvin, Edgecomb)
-- Community 1: Judicial / Academic (Gafkay, Borrello, SVSU, SCBA, Saginaw Circuit)
-- Community 2: School Boards (Saginaw ISD, Hemlock PS, Katie as VP of both)
-- Community 3: ISP / Infrastructure (LakeNet, Fabiens, Air Advantage)
-- Community 4: Surveillance Layer (FOIAworks, Quagmire Solutions, 153 domains)
-- Community 5: Cases (SLAPP, Garcia sanctions, AGC, IC3, Taylor, Howard)
-- Community 6: Properties (530/529 W Saginaw, 4522 Higgins Lake, 16690 Gratiot)
-- Community 7: Wronged (Rita Williams, Clutch Justice)

-- ============================================================
-- HEMLOCK ADDRESS CLUSTERS
-- ============================================================

-- Cluster 1: 530 W Saginaw St / PO Box 107, Hemlock MI 48626
-- Members: OLC PLC (HQ), Philip Ellison (attorney)
-- Notes: Primary law office. Across street from 529 W Saginaw.

-- Cluster 2: 529 W Saginaw St, Hemlock MI 48626
-- Members: South Brennan Property LLC (registered address)
-- Notes: 2 entities registered per CompaniesMI. Across from OLC HQ.

-- Cluster 3: South Brennan Rd area, Hemlock MI 48626
-- Members: Quagmire Solutions LLC (registered address), Calvin Lee Ellison (residence)
-- Notes: Family property. Quagmire entity still ACTIVE per LARA despite
--        LinkedIn saying it ended Aug 2007. Calvin = family member at same address.

-- Cluster 4: 4522 W Higgins Lake Dr, Roscommon MI 48653
-- Members: OLC PLC (Up North Office), FOIAworks (mailing address)
-- Notes: Former bank building. Purchased Nov 7, 2024 for $150K.
--        Buyer unknown — Roscommon County Register of Deeds needed.
--        Both law firm AND surveillance platform share same physical address.

-- Cluster 5: 16690 Gratiot Rd, Hemlock MI 48626
-- Members: LakeNet LLC (HQ)
-- Notes: ISP headquarters. MPSC, FCC, ARIN registered.
--        Same town as Ellison. Population ~2,000.

-- ============================================================
-- HEMLOCK BENCH DATA
-- ============================================================

-- Bench: 10th Judicial Circuit (Saginaw County)
-- Division: Civil
-- Total judges: ~5 (small court)
-- Captured: Gafkay (structural conflict — SVSU colleague, SCBA member, 3 simultaneous cases)
-- Recused: Borrello (signed contempt, then recused May 2026, no stated reasons)
-- Case types: civil, SLAPP, class action, UPEPA
-- Capture ratio: at minimum 1/5 = 20% (Gafkay only)
--   But Gafkay is CHIEF JUDGE — her capture has outsized impact
--   Chief judges control case assignment, administrative orders, court procedures
--   One captured chief judge > multiple captured regular judges
