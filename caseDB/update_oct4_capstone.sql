-- caseDB update: Oct 4, 2026 (CAPSTONE — Purpose Charter Academy board = the nexus map)
-- PURPOSE BOARD: Judge Miller (chair), AAG Moreland (vice chair),
-- Council Member Latisha Johnson (secretary), Gay-Dagnogo ANNOUNCED it
-- Every AGC complaint target corresponds to a Banks school board member
-- Jerome Gorgon Jr. = current USAO E.D. Mich (Trump, confirmed Dec 2025)
-- Warren Evans confirmed endorser + political consolidation partner
-- Banks website: "Dr. Brian Banks, J.D., Ph.D." — claims J.D. he never earned
-- Run: sqlite3 caseDB.sqlite < update_oct4_capstone.sql

--------------------------------------------------------------
-- CAPSTONE: Purpose Charter Academy Board of Directors
--------------------------------------------------------------

-- THE BOARD (from purposecharteracademy.com/boardofdirectors):
--
-- 1. Hon. Cylenthia LaToye Miller — Judge, 3rd Circuit Court — BOARD CHAIR
-- 2. Mr. Lamar Moreland — Asst. Attorney General, State of Michigan — BOARD VICE CHAIR
-- 3. Hon. Latisha Johnson — Detroit City Council Member — BOARD SECRETARY
-- 4. Mr. Devin Hutchings — Founder, DH Strategies — BOARD TREASURER
-- 5. Mr. Major Clora — President/CEO, Clora Funeral Home — BOARD ASSISTANT TREASURER
--
-- And from Chalkbeat Sep 8, 2025:
-- "The nine-member development team behind Purpose Charter Academy includes
-- Michigan Third Circuit Court Judge Cylenthia LaToye Miller, attorney Lamar
-- Moreland, as well as educators, mental health practitioners, and civic leaders,
-- said Board member Sherry Gay-Dagnogo."
--
-- GAY-DAGNOGO (DPSCD board/Ombudsman) ANNOUNCED the school.
-- The quid pro quo announcement announces the credential-washed school.

--------------------------------------------------------------
-- UPDATE: Moreland — Purpose Charter Board Vice Chair
--------------------------------------------------------------

UPDATE entities SET
    notes = 'P55993, admitted June 7, 1999, Active Member Good Standing. 3030 W Grand Blvd Ste 10-350, Detroit 48202-6030. Assistant Attorney General, State of Michigan. AGC supplement filed today. MRPC 1.11, 1.7 institutional conflict. AG office argued AGAINST Banks certificate — then Moreland sits on Banks''s charter school board. PURPOSE CHARTER ACADEMY BOARD VICE CHAIR. Same person on Banks''s new school board who works at the agency that prosecuted Banks. Named in Chalkbeat Sep 2025 as part of 9-member development team. Former Wayne County prosecutor (homicide, non-fatal shootings).'
WHERE id = 'moreland-lamar';

--------------------------------------------------------------
-- NEW: Judge Cylenthia LaToye Miller — Purpose Board Chair
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('miller-cylenthia', 'Judge Cylenthia LaToye Miller', 'person',
    'Michigan 3rd Circuit Court Judge. PURPOSE CHARTER ACADEMY BOARD CHAIR. Kevin says she is NOT on 3rd Circuit anymore. Named in Chalkbeat Sep 2025 as part of 9-member development team for Banks''s second school. Bar complaint already filed? JTC complaints sent? A sitting judge chairing a convicted felon''s charter school board — Canon 4(C) violation (org likely to appear before the court). PCA serves juvenile justice-involved youth = certain to create court contact.');

--------------------------------------------------------------
-- UPDATE: Latisha Johnson — Purpose Board Secretary
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('johnson-latisha', 'Latisha Johnson', 'person',
    'Detroit City Council Member, District 4. PURPOSE CHARTER ACADEMY BOARD SECRETARY. Inner Link Graphics paid her campaign $850. Founder MECCA Development Corporation. Former Treasurer, 5th Precinct Police/Community Relations Council. Council member serving on a convicted felon''s charter school board while her campaign was funded by Banks''s campaign vendor.');

--------------------------------------------------------------
-- NEW: Devin Hutchings — Purpose Board Treasurer
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('hutchings-devin', 'Devin Hutchings', 'person',
    'Founder, DH Strategies. PURPOSE CHARTER ACADEMY BOARD TREASURER. Managing finances for a convicted felon''s charter school.');

--------------------------------------------------------------
-- NEW: Major Clora — Purpose Board Asst Treasurer
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('clora-major', 'Major Clora', 'person',
    'President/CEO, Clora Funeral Home. PURPOSE CHARTER ACADEMY BOARD ASSISTANT TREASURER.');

--------------------------------------------------------------
-- UPDATE: Gay-Dagnogo — announced Purpose Charter Academy
--------------------------------------------------------------

-- From Chalkbeat: Gay-Dagnogo (as DPSCD board member) was the one who
-- publicly described the Purpose Charter Academy development team.
-- The quid pro quo appointee (DPSCD board → City Ombudsman) announces
-- the credential-washed school for the convicted felon she helped install.

--------------------------------------------------------------
-- NEW: Jerome Gorgon Jr. — current USAO
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('gorgon-jerome', 'Jerome F. Gorgon Jr.', 'person',
    'U.S. Attorney, Eastern District of Michigan (interim May 2025, confirmed Dec 2025). Trump nominee, appointed by AG Pam Bondi. Born Southwest Detroit. Southwestern High School grad. Taught elementary science in DPS. U of M + U of M Law. Clerked for Anna Diggs Taylor (USDC) and Damon Keith (6th Circuit). Former partner Honigman LLP. 15 years as federal prosecutor: terrorism, violent crime, sex trafficking, carjacking, immigration. His office has Kevin''s federal referral packets and inherits all ongoing public corruption investigations from Ison era.');

--------------------------------------------------------------
-- BANKS WEBSITE: Claims "J.D., Ph.D." — J.D. NEVER EARNED
--------------------------------------------------------------

-- macdowellprep.com/meet-our-superintendent/:
-- "Dr. Brian Banks, J.D., Ph.D."
-- Banks has NEVER been bar-admitted. His J.D. is from MSU but
-- felonies prevented bar admission. The website representation
-- of "J.D." to parents of 362 predominantly Black children
-- at a charter school is credential fraud.
-- The Ph.D. is from Walden University (online).
-- This is MRPC 8.4(c) territory — misrepresentation.
-- Also potential MCL 750.259a (false representation as attorney).

--------------------------------------------------------------
-- CREDENTIAL MAP: AGC complaints ↔ school board members
--------------------------------------------------------------

-- MEIHN → MacDowell board counsel ($23K+ payments, testified at TCR 22-12)
-- MORELAND → Purpose Charter Vice Chair (AAG whose office prosecuted Banks)
-- HALL → MacDowell board member (licensed attorney, Crump Hall PLLC)
-- MILLER → Purpose Charter Chair (3rd Circuit judge)
-- YANCEY → MacDowell Board Chair (36th District judge, Banks ran her campaign)
-- WELLS STALLWORTH → MacDowell Board Chair (wife of Thomas who defended at rally)
-- LATISHA JOHNSON → Purpose Charter Secretary (council, Inner Link $850)
-- GAY-DAGNOGO → DPSCD board who announced Purpose (quid pro quo appointment)
--
-- Every single credential-washing bar member sits on a Banks school board.
-- The school boards ARE the credential-washing mechanism.

--------------------------------------------------------------
-- RELATIONSHIPS: Purpose Charter board
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('miller-cylenthia', 'purpose-charter', 'board-chair', 'Board Chair, Purpose Charter Academy', 'purposecharteracademy.com/boardofdirectors',
    '3rd Circuit judge chairing convicted felon''s charter school. School serves juvenile justice youth = Canon 4(C) violation. Named in Chalkbeat Sep 2025 development team.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('moreland-lamar', 'purpose-charter', 'board-vice-chair', 'Board Vice Chair, Purpose Charter Academy', 'purposecharteracademy.com/boardofdirectors',
    'AAG on board of school run by man his office prosecuted. MRPC 1.11 conflict. Named in Chalkbeat.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('johnson-latisha', 'purpose-charter', 'board-secretary', 'Board Secretary, Purpose Charter Academy', 'purposecharteracademy.com/boardofdirectors',
    'Council member whose campaign vendor (Inner Link $850) is Banks''s biggest vendor ($51K+).');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('gay-dagnogo-sherry', 'purpose-charter', 'announcer', 'DPSCD board member who announced Purpose Charter development team', 'Chalkbeat Sep 8, 2025',
    'The quid pro quo appointee announces the credential-washed school. She named Miller and Moreland as development team members.');

--------------------------------------------------------------
-- RELATIONSHIPS: Evans endorsement
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('evans-warren', 'banks-brian', 'endorser', 'Endorsed Banks for Wayne County Commissioner 2022 + 13th CD consolidation', 'M.L. Elrick Free Press Jul 2022',
    'Wayne County Executive (former sheriff + former DPD chief). Led political consolidation effort WITH Banks. Third-term executive endorsing 9-time convicted felon.');

--------------------------------------------------------------
-- NEW: Warren Evans
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('evans-warren', 'Warren Evans', 'person',
    'Wayne County Executive (2015-present, third term). Former Wayne County Sheriff. Former Detroit Police Chief. Endorsed Banks for Wayne County Commissioner 2022. Led 13th Congressional District political consolidation effort with Banks participating. Blasted Sabree over property deals but STILL endorsed Banks. Most powerful elected official in Wayne County endorsing a 9-time convicted felon.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('miller-cylenthia', 'purpose-charter', 'board-chair', 'record', '3rd Circuit judge = Purpose board chair', 'purposecharteracademy.com');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('moreland-lamar', 'purpose-charter', 'board-vice-chair', 'record', 'AAG = Purpose board vice chair', 'purposecharteracademy.com');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('johnson-latisha', 'purpose-charter', 'board-secretary', 'record', 'Council member = Purpose board secretary', 'purposecharteracademy.com');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('gay-dagnogo-sherry', 'purpose-charter', 'announcer', 'record', 'DPSCD board announced Purpose', 'Chalkbeat Sep 2025');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('evans-warren', 'banks-brian', 'endorser', 'record', 'Wayne County Exec endorsed 2022', 'Free Press');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('miller-cylenthia', 'person', 'Judge Miller (Purpose Chair, 3rd Circuit)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('johnson-latisha', 'person', 'Latisha Johnson (Purpose Secretary, D4 Council)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('hutchings-devin', 'person', 'Devin Hutchings (Purpose Treasurer)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('clora-major', 'person', 'Major Clora (Purpose Asst Treasurer)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('gorgon-jerome', 'person', 'Jerome Gorgon Jr. (current USAO E.D. Mich)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('evans-warren', 'person', 'Warren Evans (Wayne Co Exec, endorser)', 2);
