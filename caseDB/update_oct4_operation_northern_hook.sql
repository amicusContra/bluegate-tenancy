-- caseDB update: Oct 4, 2026 (OPERATION NORTHERN HOOK expanded)
-- Carol Banks: Benson COS, former DPS board, dual salary, FBI raid, Northern Hook
-- Elrick exposed Carol Banks → Benson tripled her pay → Save Detroit Jobs fought Elrick
-- Carmack: FBI informant, charges dismissed, Judge MILLER ruled on his case
-- Wells Stallworth: Children's Center CEO, Planned Parenthood exec, praised Banks
-- Investigation closed Jan 2025 by USAO Dawn Ison (now at DWIHN)
-- Run: sqlite3 caseDB.sqlite < update_oct4_operation_northern_hook.sql

--------------------------------------------------------------
-- CAROL BANKS — Operation Northern Hook target
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('banks-carol', 'Carol Banks', 'person',
    'Scott Benson chief of staff. Former Detroit Public Schools ELECTED board member. Former DPS ombudswoman ($60K). DUAL SALARY: DPS $60K + city council $20K simultaneously, billing both for same hours. Fired by DPS after ML Elrick (Fox 2) exposed dual employment in 2015. Benson then TRIPLED her city contract from $20K → $60K. FBI RAIDED her East English Village home Aug 25, 2021 (20+ agents, large black containers wheeled out). Part of OPERATION NORTHERN HOOK investigation (towing corruption). Investigation closed Jan 2025 without charges (USAO Dawn Ison office — same Ison now at DWIHN). Named by Area Towing lawyer Perkins alongside Brian Banks in 2018 probe affidavit. Had LATISHA JOHNSON yard sign in front yard when FBI raided. Save Detroit Jobs (Benson nonprofit) paid Carol Banks $18K+ as it fought Prop A 2016, then PIVOTED TO FIGHT ML ELRICK in District 4 council race. Linked to "Eastside Community Slate" political operation. NOTE: NOT confirmed blood relation to Brian Banks — different families.');

--------------------------------------------------------------
-- CRITICAL PATTERN: Carol Banks → Elrick suppression
--------------------------------------------------------------

-- TIMELINE:
-- 2015: Elrick (Fox 2) exposes Carol Banks dual salary
-- 2015: DPS fires Carol Banks
-- 2015: Benson TRIPLES her city contract ($20K → $60K)
-- 2016: Save Detroit Jobs pays Carol Banks $18K+
-- 2017: Save Detroit Jobs fights ELRICK's District 4 council campaign
-- 2017: Bank on Banks PAC gives Benson $500
-- 2017: Benson gives Latisha Johnson $100 contribution
-- 2021: FBI raids Carol Banks's home (Northern Hook)
-- 2021: Carol Banks has Latisha Johnson yard sign when raided
-- 2025: USAO Dawn Ison closes investigation without charges
-- 2026: Ison now VP at DWIHN
--
-- The journalist who exposed Carol Banks was THEN targeted
-- by the entity that paid Carol Banks. And she backed the same
-- candidates as Brian Banks (Latisha Johnson = PCA board secretary).

--------------------------------------------------------------
-- UPDATE: Benson
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('benson-scott', 'Scott Benson', 'person',
    'Detroit City Council member (took office 2014, remains on council). Received $500 from Bank on Banks PAC. Chief of staff was Carol Banks (FBI raid target). FBI raided his home Aug 25, 2021 (Operation Northern Hook). Investigation closed Jan 2025 without charges (USAO Dawn Ison). Save Detroit Jobs nonprofit connected to his office — fought Elrick in District 4. Gave $100 to Latisha Johnson (Purpose Charter board secretary). Former real estate developer and Midtown Detroit Inc small business director.');

--------------------------------------------------------------
-- UPDATE: Carmack
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('carmack-robert', 'Robert Carmack', 'person',
    'Detroit businessman, FBI informant. B&C Land Development Corp owner. Wore FBI wire on Councilman Leland ($15K bribe). Star witness in Leland prosecution. Hired PIs to surveil Mayor Duggan, displayed extramarital affair video on billboard truck outside City Hall. City charged him with 4 felonies within 30 days of billboard — charges DISMISSED July 10, 2024. Court of Appeals affirmed city quiet-title judgment Apr 2025. Donated $150K to Tamara Greene reward fund (Kilpatrick-connected stripper murder). CRITICAL: Judge Cynthia LaToye Miller ruled on his retaliation case — denied Duggan testimony, called claims "conspiracy theory." This is the SAME Miller who is now Purpose Charter Academy board CHAIR. She protected Duggan from scrutiny in the Carmack case.');

--------------------------------------------------------------
-- UPDATE: Wells Stallworth
--------------------------------------------------------------

UPDATE entities SET
    notes = 'MacDowell Preparatory Academy Board Chair (since 2012). President & CEO of The Children''s Center (major Detroit nonprofit). Former Executive Director of Planned Parenthood Advocates of Michigan. Former VP for Public Advocacy at Planned Parenthood of Michigan. Donated $1,250 (with husband Tommy) to Banks campaign — biggest individual supporters. Told media that Banks''s criminal past was "one of the reasons" board voted UNANIMOUSLY to hire him. Praised Banks as "Black Excellence Honoree" at State of Black Learning conference (Aug 2024 LinkedIn). Wrote Bridge Michigan op-ed defending charter school financial accountability (June 2023). Also listed as "Managing Director, Zero Gravity" on current MacDowell board page.'
WHERE id = 'wellsstallworth-nicole';

--------------------------------------------------------------
-- Judge Miller ruled on Carmack case
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('miller-cylenthia', 'carmack-robert', 'judge', 'Ruled Duggan retaliation claims were "conspiracy theory"', 'Metro Times',
    'Same judge who chairs Purpose Charter Academy board. She protected Duggan from scrutiny in the Carmack case — a case arising from the same corruption probe (Operation Northern Hook) that produced the Spivey conviction and Carol Banks FBI raid.');

--------------------------------------------------------------
-- RELATIONSHIPS
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-carol', 'benson-scott', 'chief-of-staff', 'COS since ~2014. FBI raided both homes Aug 2021.', 'Free Press + Fox 2',
    'Benson tripled her contract after Elrick exposed dual salary.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-carol', 'johnson-latisha', 'political-support', 'Had Johnson yard sign when FBI raided', 'Free Press',
    'Carol Banks supported Latisha Johnson. Benson gave Johnson $100. Johnson is PCA board secretary. Carol Banks was named alongside Brian Banks in 2018 probe.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-carol', 'elrick-ml', 'retaliation', 'Elrick exposed Carol Banks dual salary → Save Detroit Jobs fought Elrick', 'Fox 2 + Deadline Detroit',
    'The journalist who exposed Carol Banks was targeted by the entity that paid her $18K+.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-carol', 'benson-scott', 'chief-of-staff', 'record', 'FBI raided both homes Operation Northern Hook', 'Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-carol', 'johnson-latisha', 'political-support', 'record', 'Johnson yard sign when FBI raided Carol Banks home', 'Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('benson-scott', 'banks-brian', 'pac-recipient', 'record', '$500 from Bank on Banks PAC', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('miller-cylenthia', 'carmack-robert', 'judge', 'record', 'Denied Duggan testimony, called retaliation "conspiracy theory"', 'Metro Times');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('carmack-robert', 'leland-gabe', 'fbi-informant', 'record', 'Wore wire for FBI, $15K bribe recorded', 'Fox 2 + Free Press');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('banks-carol', 'person', 'Carol Banks (Benson COS, FBI raid, DPS double-dip)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('benson-scott', 'person', 'Scott Benson (Council, FBI raid, Northern Hook)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('carmack-robert', 'person', 'Robert Carmack (FBI informant, Leland wire)', 3);
