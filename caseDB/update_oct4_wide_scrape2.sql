-- caseDB update: Oct 4, 2026 (WIDE SCRAPE batch 2 — associates + case numbers)
-- Eric Smith: 21mo federal (Judge Parker!) + 12mo state (AG Nessel). Lost pension.
-- Chang: Education committee senator endorsing convicted felon school operator
-- JohnNae Reynolds: MacDowell board + Tim Hortons franchise owner
-- Clora: Cass Tech, WSU Mortuary, Omega Psi Phi, DSO board, voter mobilization
-- Full Macomb prosecution team: AUSA Robert Moran, Judge Parker, Judge Cleland
-- Run: sqlite3 caseDB.sqlite < update_oct4_wide_scrape2.sql

--------------------------------------------------------------
-- UPDATE: Eric Smith — DUAL conviction (federal + state)
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Former Macomb County Prosecutor (elected 2004, resigned Mar 2020). FEDERAL: Obstruction of justice, 21 months, Judge Linda V. Parker (SAME JUDGE as Area Towing wiretap case). AUSA Robert Moran. Forfeiture $69,950. Stole ~$75K from campaign fund via kickback scheme (2012-2019). Pressured friend + 2 assistant prosecutors to lie to FBI and federal grand jury. STATE (AG Nessel): Official Misconduct + Tampering with Evidence + Conspiracy to Commit Forgery. 12 months concurrent (Judge Nanci Grant). LOST PUBLIC PENSION. $25K restitution. Separately charged with $600K embezzlement from drug forfeiture funds (sump pump, home security at his residence). Co-defendants: Derrick Miller (county employee), Ben Liston (chief asst prosecutor, surrendered law license), William Weber ($23,960 restitution). 30+ year career as prosecutor/asst prosecutor — ended as convicted felon. The county''s chief law enforcement officer convicted of obstruction and evidence tampering.'
WHERE id = 'smith-eric-macomb';

--------------------------------------------------------------
-- UPDATE: Chang — Education committee
--------------------------------------------------------------

UPDATE entities SET
    notes = 'MI State Senator (D-Detroit, District 3). Endorsed Banks for Wayne County Commissioner 2022. Sits on EDUCATION COMMITTEE in Senate — endorsing a convicted felon who operates charter schools while serving on the committee with oversight authority. Senate Democratic Policy and Steering Chair. First Asian American woman elected to MI legislature. Former community engagement coordinator at James and Grace Lee Boggs School. Endorsed by Mary Sheffield. Also endorsed El-Sayed for US Senate 2026. Term-limited Dec 2026. Parts of Wayne, Oakland, Macomb counties.'
WHERE id = 'chang-stephanie';

--------------------------------------------------------------
-- NEW: JohnNae Reynolds — MacDowell board + franchise owner
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('reynolds-johnnae', 'JohnNae Reynolds', 'person',
    'MacDowell Preparatory Academy board member. Donated $100 to Banks 2022 Wayne County commissioner campaign. Tim Horton''s franchise owner at 10533 Gratiot Ave, Detroit 48213. Community entrepreneur. Board members voted UNANIMOUSLY to hire Banks per Wells Stallworth.');

--------------------------------------------------------------
-- UPDATE: Clora — community profile
--------------------------------------------------------------

UPDATE entities SET
    notes = 'President/CEO, Clora Funeral Home (3 locations: Detroit East, Detroit West, River Rouge). PURPOSE CHARTER ACADEMY BOARD ASSISTANT TREASURER. Youngest funeral home owner in MI (2008). Cass Technical High School. Wayne State University School of Mortuary Science. Omega Psi Phi Fraternity. Second Ebenezer Church. Eight Mile Boulevard Association. Michigan Chronicle 40 under 40. "Limos to the Polls" voter mobilization (2016, 2018, 2020 — 15+ limos). Clora Funeral Home Scholarship (sciences). DSO board. Children''s Hospital of Michigan Foundation. Detroit Public Television. Community leader type — question is whether he knows the full picture of what Banks is.'
WHERE id = 'clora-major';

--------------------------------------------------------------
-- FEDERAL PROSECUTION TEAM REGISTRY
--------------------------------------------------------------

-- USAO E.D. Mich — Macomb/Detroit corruption cases:
-- ═════════════════════════════════════════════════
-- AUSA Robert Moran — Eric Smith prosecution
-- AUSA David Gardey + Frances Carlson — Spivey (Operation Northern Hook)
-- AUSA Brittany D. Parling — Area Towing wiretap file production
-- Former USA Dawn Ison — oversaw Sollars conviction, now DWIHN VP
-- Current USA Jerome Gorgon Jr. — inherits all ongoing
--
-- JUDGES:
-- Judge Robert Cleland (Port Huron) — Reynolds 17yr, Rizzo 66mo, Marrocco plea
-- Judge Linda V. Parker (Detroit) — Area Towing wiretap case AND Eric Smith 21mo
-- Judge Mark Goldsmith — Sollars 71mo
-- Judge Victoria Roberts → Stephen Murphy III — Spivey 24mo
-- Judge Matthew Leitman — Bert Johnson 90 days
-- Judge Nancy Edmunds — Stanton probation (pension fraud)
--
-- FBI:
-- SA Robert Beeckman — wiretap affidavit author, "bid-rigging with Banks"
-- SAC Timothy Waters — Spivey press conference
-- SAC Cheyvoryea Gibson — Sollars press conference (Sep 2023 - ~Aug 2025)
-- SAC (current) — TBD

--------------------------------------------------------------
-- NEW: Ben Liston — surrendered law license
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('liston-ben', 'Ben Liston', 'person',
    'Former Macomb County chief assistant prosecutor. Surrendered law license as part of plea. Convicted: Willful Neglect of Duty by Public Officer (3 misdemeanors). Paid $10,000 restitution. Cooperated against Eric Smith. Participated in scheme to hide accounts and spending from county officials. Home security equipment purchased with Drug Forfeiture Account funds installed at Smith residence.');

--------------------------------------------------------------
-- RELATIONSHIPS: Judge Parker connection
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('smith-eric-macomb', 'area-towing-case', 'same-judge', 'Both before Judge Linda V. Parker', 'PACER records',
    'The Macomb prosecutor was sentenced by the same federal judge now overseeing the civil case that has the FBI wiretap files containing Banks conversations. Parker has seen this corruption network from multiple angles.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('reynolds-johnnae', 'banks-brian', 'board-member+donor', 'record', 'MacDowell board, $100 donation', 'Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('chang-stephanie', 'banks-brian', 'endorser', 'record', 'Education committee senator endorsed convicted felon school operator', 'Free Press');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('reynolds-johnnae', 'person', 'JohnNae Reynolds (MacDowell board)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('liston-ben', 'person', 'Ben Liston (surrendered law license)', 4);
