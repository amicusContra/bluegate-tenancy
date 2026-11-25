-- caseDB update: Oct 4, 2026 (DARK MONEY LOOP — journalist suppression mechanism)
-- Save Detroit Jobs → renamed Detroit Leaders → funded Latisha Johnson vs Elrick
-- Johnson won → now on Purpose Charter Academy board (Brian Banks school)
-- Carol Banks ran Eastside Slate endorsement-for-hire operation
-- Duggan dark money groups pushed Johnson + Santiago
-- Officers: Knox (Duggan ethics appointee), Mitchell (police commissioner candidate),
--   Kenneth Daniels (charged buying Mercedes for drug dealer)
-- Run: sqlite3 caseDB.sqlite < update_oct4_dark_money_loop.sql

--------------------------------------------------------------
-- SAVE DETROIT JOBS / DETROIT LEADERS — the suppression mechanism
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('save-detroit-jobs', 'Save Detroit Jobs / Detroit Leaders', 'org',
    'Dark money 501c4 nonprofit. Originally "Save Detroit Jobs" (2016). Renamed "Detroit Leaders" Aug 10, 2021 — ONE WEEK after primary. Officers: Knox (Duggan''s former ethics board appointee, president), Damian Mitchell (District 3 candidate for Detroit Board of Police Commissioners), former state Rep Kenneth Daniels (charged 2014 helping buy Mercedes for convicted drug dealer). Raised $100K+ in 2016. Donors: Blue Cross Blue Shield, Turn Around Wayne County PAC (Moroun Central Transport), Schostak Family PAC (primarily Republican donors). Paid Carol Banks $18K+ as it fought Prop A 2016. THEN PIVOTED to fight ML Elrick in District 4 council race — funded mailers + yard signs for Latisha Johnson. Johnson won. Johnson is now Purpose Charter Academy board secretary. The entity that paid Carol Banks $18K then helped elect the woman who now sits on Brian Banks''s school board. Another dark money group "Opportunity For All Michigan" also sent mailers for Johnson.');

--------------------------------------------------------------
-- EASTSIDE SLATE — endorsement-for-hire
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('eastside-slate', 'Eastside Community Slate', 'org',
    'Endorsement operation run by Carol Banks and William Spencer "Nabil" Leach. Candidates paid $250+ for endorsements. Raised $35K from Detroit candidates in one cycle. Duggan campaign gave $25K to related operation. Latisha Johnson contributed $8,300 into these slate operations. FBI search warrants specifically sought "documents regarding social welfare nonprofit organizations" — these are the entities.');

--------------------------------------------------------------
-- THE FULL SUPPRESSION LOOP
--------------------------------------------------------------

-- STEP 1: Elrick (Fox 2) exposes Carol Banks dual salary (2015)
-- STEP 2: DPS fires Carol Banks
-- STEP 3: Benson triples her city contract ($20K → $60K)
-- STEP 4: Save Detroit Jobs pays Carol Banks $18K+ (2016)
-- STEP 5: Save Detroit Jobs renames to Detroit Leaders (Aug 2021)
-- STEP 6: Detroit Leaders funds mailers/signs for Latisha Johnson vs Elrick
-- STEP 7: Another Duggan dark money group also pushes Johnson
-- STEP 8: Latisha Johnson wins District 4
-- STEP 9: Johnson becomes Purpose Charter Academy board SECRETARY
-- STEP 10: Purpose Charter Academy is Brian Banks's school
-- STEP 11: Brian Banks was named alongside Carol Banks in 2018 federal probe
-- STEP 12: Investigation closed by USAO Dawn Ison (now DWIHN VP)
--
-- The journalist who exposed the corruption was kneecapped by the
-- dark money apparatus that protects the same network.
-- The person who replaced him is now on the corrupt school board.
--
-- THIS is the institutional capture mechanism in action.

--------------------------------------------------------------
-- UPDATE: Ayers
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ayers-janee', 'Janeé Ayers', 'person',
    'Former Detroit City Council member (at-large). Home raided by FBI Aug 25, 2021 (Operation Northern Hook). Chief of staff Ricardo Silva also raided. Lost re-election 2021 (investigation contributed). Investigation closed Jan 2025 without charges (USAO Dawn Ison). Defense attorney Abed Hammoud. Caught up in towing corruption probe alongside Benson.');

--------------------------------------------------------------
-- UPDATE: Silva
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('silva-ricardo', 'Ricardo Silva', 'person',
    'Chief of staff for Councilwoman Janeé Ayers. Home raided by FBI Aug 25, 2021 (Operation Northern Hook). Investigation closed Jan 2025 without charges. Attorney Allison Kriger: "We anticipated this outcome." Part of the broader City Council towing corruption investigation.');

--------------------------------------------------------------
-- Operation Northern Hook CONVICTION REGISTRY
--------------------------------------------------------------

-- Convicted in Operation Northern Hook:
-- 1. André Spivey — 24 months, $35,800 in bribes
-- 2. Five former Detroit police officers (bribed by towing industry UCO)
--    Including: Mike Pacteles (former DPD detective → Hamtramck PD,
--    convicted taking bribes from towing company owner, 1yr halfway house)
-- 3. Total: 6 convictions, multiple prison terms
--
-- NOT charged despite FBI raids:
-- Scott Benson (remains on council)
-- Janeé Ayers (lost re-election)
-- Carol Banks (still Benson COS)
-- Ricardo Silva
--
-- All closed Jan 2025 by USAO Dawn Ison's office.
-- Ison now VP at DWIHN.

--------------------------------------------------------------
-- RELATIONSHIPS
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('save-detroit-jobs', 'johnson-latisha', 'dark-money', 'Funded mailers + yard signs for Johnson vs Elrick (District 4)', 'Deadline Detroit + Detroit News',
    'The entity that paid Carol Banks $18K then helped elect the woman who now sits on Brian Banks''s school board.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('save-detroit-jobs', 'banks-carol', 'payee', '$18K+ in "unspecified reimbursements"', 'Deadline Detroit',
    'Carol Banks also ran Eastside Slate endorsement operation. FBI search warrants sought social welfare nonprofit docs.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('save-detroit-jobs', 'elrick-ml', 'opposition', 'Funded anti-Elrick campaign in District 4', 'Deadline Detroit + Detroit News',
    'Elrick exposed Carol Banks. The entity that paid Carol Banks then fought the journalist who exposed her.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('save-detroit-jobs', 'johnson-latisha', 'dark-money', 'record', 'Funded mailers/signs vs Elrick in D4', 'Deadline Detroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('save-detroit-jobs', 'banks-carol', 'payee', 'record', '$18K+ unspecified reimbursements', 'Deadline Detroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('save-detroit-jobs', 'elrick-ml', 'opposition', 'record', 'Anti-Elrick campaign funding', 'Deadline Detroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('eastside-slate', 'banks-carol', 'operator', 'record', 'Carol Banks ran endorsement-for-hire', 'Deadline Detroit');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('save-detroit-jobs', 'entity', 'Save Detroit Jobs / Detroit Leaders (dark money)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('eastside-slate', 'entity', 'Eastside Slate (endorsement-for-hire)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('ayers-janee', 'person', 'Janeé Ayers (former Council, FBI raid)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('silva-ricardo', 'person', 'Ricardo Silva (Ayers COS, FBI raid)', 4);
