-- caseDB update: Oct 4, 2026 (FBI wiretap affidavit details + Purpose Charter Academy)
-- FBI SA Beeckman: "Fiore is involved in BID-RIGGING with legislator Brian Banks"
-- 18 wiretap targets: extortion, wire fraud, bribery, marijuana conspiracy
-- Jennifer Fiore wrote MDOT amendment eliminating Fiore competition
-- Area Towing has FBI wiretap files in civil record (produced Sep 2025)
-- Purpose Charter Academy: SECOND Banks school authorized Jul 2025
-- MacDowell: bottom 3% statewide, 3% math proficiency, $15,217/student
-- Dawn Ison → DWIHN with former Police Chief James White
-- Run: sqlite3 caseDB.sqlite < update_oct4_wiretap_purpose.sql

--------------------------------------------------------------
-- CRITICAL: FBI affidavit literally says "BID-RIGGING"
--------------------------------------------------------------

-- FBI Special Agent Robert Beeckman, 2016 affidavit:
-- "Fiore is involved in bid-rigging with legislator Brian Banks"
-- Source: Free Press Dec 29, 2017 (documents briefly unsealed then resealed)
-- This is NOT "target subject" — this is an affirmative statement by FBI
-- that Banks was involved in BID-RIGGING with a convicted briber.
--
-- The wiretap targeted 18 people for:
--   - Extortion
--   - Wire fraud
--   - Bribery
--   - Conspiracy to distribute marijuana
--
-- Jennifer Fiore wrote the MDOT amendment that would eliminate
-- Fiore's competition (Integral Blue) from Emergency Road Response contracts.
-- Banks discussed this amendment on the wiretap.

--------------------------------------------------------------
-- UPDATE: Fiore — bid-rigging language
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Towing consultant/businessman. CONVICTED: bribery conspiracy (Clinton Township Trustee Dean Reynolds, 16-cr-20732). Sentenced 21 months (2018). FBI wiretap on his phone 2016. FBI SA Bob Beeckman affidavit: "FIORE IS INVOLVED IN BID-RIGGING WITH LEGISLATOR BRIAN BANKS." Wiretap targeted 18 people for extortion, wire fraud, bribery, marijuana conspiracy. Banks discussed MDOT contract + "high-ranking police official" on tape. Jennifer Fiore (daughter) wrote MDOT amendment eliminating Fiore''s competitor. Area Towing obtained FBI wiretap files via federal subpoena (Sep 2025) — Banks conversations in civil record. Fiore tried to seal → DENIED by Judge Parker. Fiore deposed Dec 29, 2025 — pled Fifth to everything. Court ordered to answer by Mar 6, 2026. Donated $500 to Todd Perkins mayoral campaign.'
WHERE id = 'fiore-gasper';

--------------------------------------------------------------
-- NEW: Purpose Charter Academy — SECOND Banks school
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('purpose-charter', 'Purpose Charter Academy', 'org',
    'SECOND Banks school. Authorized by DPSCD July 2025 — citing "claimed improvement at MacDowell" (which ranks bottom 3% statewide). Opening 2026-27. PK-8. Located in former Detroit Lions Academy building, 10101 E. Canfield St, Detroit 48214. Projected enrollment: 225 (year 1) → 400 (by 2029-30). Mission: "law and public service" curriculum for underserved youth. DPSCD receives 3% authorization fee (~$81K year 1). Lease: 9% of per-pupil funding by 2028-29 with purchase option. Management by The Purpose Group. A convicted felon''s SECOND taxpayer-funded school authorized while FIRST school has 3% math proficiency.');

--------------------------------------------------------------
-- UPDATE: MacDowell — Clutch Justice data
--------------------------------------------------------------

-- Clutch Justice (Sep 13, 2026):
-- - $15,217 per student per year
-- - 3% math proficiency
-- - 10-14% reading proficiency
-- - Ranked 1,443 out of 1,488 elementary schools in Michigan (bottom 3%)
-- - MCL 380.507 closure trigger: bottom 5% for 3 consecutive years
-- - Operated through The Purpose Group Michigan LLC
-- - Banks listed as sole registered agent

--------------------------------------------------------------
-- NEW: The Purpose Group Michigan LLC
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('purpose-group', 'The Purpose Group Michigan LLC', 'org',
    'Michigan LLC. Banks is sole registered agent. Operates MacDowell Preparatory Academy AND Purpose Charter Academy. Management company receiving taxpayer education funds for a 9-time convicted felon''s school network.');

--------------------------------------------------------------
-- NEW: Dawn Ison — former USAO, now DWIHN
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ison-dawn', 'Dawn Ison', 'person',
    'Former U.S. Attorney, Eastern District of Michigan (Dec 2021 - Jan 19, 2025). First Black woman in the position. Biden nominee. Resigned ahead of Trump inauguration. Oversaw Sollars conviction, UAW corruption cases, public corruption unit. Now interim VP of Compliance at DWIHN (Detroit Wayne Integrated Health Network) as of May 2026 — same org where former Police Chief James White is CEO. Previously directed Public Corruption Unit investigations. Her USAO office has Kevin''s federal referral packets.');

--------------------------------------------------------------
-- UPDATE: James White — now DWIHN CEO
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('white-james', 'James White', 'person',
    'Former Detroit Police Chief (2020-2024). Left DPD to become CEO of DWIHN (Detroit Wayne Integrated Health Network). Now works alongside former USAO Dawn Ison (VP Compliance) at same org. Bettison (his 1st Assistant Chief) replaced him as police chief. The former police chief and former top federal prosecutor are now at the same health network.');

--------------------------------------------------------------
-- RELATIONSHIPS: Purpose Group ownership
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('purpose-group', 'macdowell', 'management', 'Banks sole agent — manages MacDowell', 'Clutch Justice Sep 2026 + LARA records',
    'LLC operates the bottom-3%-statewide school.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('purpose-group', 'purpose-charter', 'management', 'Banks sole agent — manages Purpose Charter Academy', 'DPSCD board minutes Jul 2025 + Chalkbeat Sep 2025',
    'SECOND school authorized while first school failing. Same management entity.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('purpose-charter', 'dpscd', 'authorized-by', 'DPSCD authorized Jul 2025, 3% fee', 'Chalkbeat Sep 8, 2025',
    'DPSCD receives $81K/yr to authorize a convicted felon''s second school.');

--------------------------------------------------------------
-- RELATIONSHIPS: Ison-White at DWIHN
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('ison-dawn', 'white-james', 'colleague', 'Both at DWIHN: Ison VP Compliance, White CEO', 'DWIHN press release May 2026',
    'Former top federal prosecutor + former police chief at same org. The public corruption prosecutor and the police chief whose department is under FBI probe (Operation Northern Hook) now work together.');

--------------------------------------------------------------
-- RELATIONSHIPS: FBI bid-rigging statement
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fiore-gasper', 'banks-brian', 'bid-rigging', 'FBI SA Beeckman: "involved in bid-rigging with legislator Brian Banks"', 'Free Press Dec 29 2017 (briefly unsealed affidavit)',
    'This is not a suspicion — the FBI affirmatively stated bid-rigging in a sworn affidavit. Banks was never charged. Arena (former FBI SAC): could be because he left office, cooperated, or was "slime not crime." The Area Towing civil case now has these files.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('purpose-group', 'macdowell', 'management', 'record', 'Banks sole agent', 'LARA + Clutch Justice');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('purpose-group', 'purpose-charter', 'management', 'record', 'Second school, same management', 'DPSCD + Chalkbeat');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('ison-dawn', 'white-james', 'colleague', 'record', 'Both at DWIHN 2026', 'DWIHN release');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fiore-gasper', 'banks-brian', 'bid-rigging', 'record', 'FBI affidavit language — not charged', 'Free Press Dec 2017');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('purpose-charter', 'entity', 'Purpose Charter Academy (2nd Banks school)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('purpose-group', 'entity', 'The Purpose Group Michigan LLC', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('ison-dawn', 'person', 'Dawn Ison (former USAO → DWIHN)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('white-james', 'person', 'James White (former DPD Chief → DWIHN CEO)', 3);
