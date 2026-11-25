-- caseDB update: Oct 4, 2026 (federal connections + Operation Northern Hook)
-- Bert Johnson ghost employee (EAA education corruption cooperator)
-- Spivey Operation Northern Hook (ONGOING FBI + DPD corruption probe)
-- Gay-Dagnogo multi-campaign donor ($1K Sheffield, $750 Todd Perkins, $300+ others)
-- Bullock on State Board of Education (co-endorsed with Banks for Duggan)
-- Todd Perkins mayoral candidate + Gasper Fiore (convicted) donor
-- Run: sqlite3 caseDB.sqlite < update_oct4_federal_connections.sql

--------------------------------------------------------------
-- UPDATE: Bert Johnson — EAA education corruption thread
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Former MI State Senator (D-Highland Park). Endorsed Banks 2016. CONVICTED: conspiracy to steal from federally funded program. Ghost employee scheme — put Glynis Thornton on payroll ($23,133) to repay personal loans. Thornton was ALREADY a federal cooperator from Education Achievement Authority corruption case (bribery of Detroit school principal). Sentenced 90 days + 480hr community service + $23K restitution. U.S. District Judge Matthew Leitman. USAO prosecutors: the same E.D. Mich. office that has Kevin''s referral packets. Education corruption → legislative corruption pipeline.'
WHERE id = 'johnson-bert';

--------------------------------------------------------------
-- UPDATE: Spivey — Operation Northern Hook (ONGOING)
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Former Detroit City Councilman. Endorsed Banks 2016. CONVICTED: federal bribery conspiracy — $35,900 in bribes from towing industry (Operation Northern Hook, 2:21-cr-20490). Sentenced 24 months. FAILED FBI polygraph. LIED to FBI during debriefings. WARNED other targets. LEAKED FBI confidential source identity. Introduced FBI informant to OTHER council members. Operation Northern Hook described as ONGOING FBI investigation into Detroit government + DPD corruption. AUSAs: David Gardey + Frances Carlson, USAO E.D. Mich.'
WHERE id = 'spivey-andre';

--------------------------------------------------------------
-- NEW: Glynis Thornton — EAA cooperator bridge
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('thornton-glynis', 'Glynis Thornton', 'person',
    'Federal cooperator. Convicted: conspiracy to commit federal program bribery in Education Achievement Authority scheme (bribing Detroit school principal via tutoring company M.A.D.E.). Cooperated with FBI — secretly recorded Bert Johnson at his home (Nov 2015). Her cooperation CREATED the Johnson case. Bridge between education corruption and legislative corruption. Sentenced per cooperation agreement.');

--------------------------------------------------------------
-- NEW: Operation Northern Hook
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('operation-northern-hook', 'Operation Northern Hook', 'org',
    'ONGOING FBI investigation into corruption within Detroit city government and Detroit Police Department. First public case: Spivey (2:21-cr-20490, Sep 2021). Relates to towing industry AND "other incidents." FBI Detroit SAC Timothy Waters: "should serve as a warning to others." Spivey introduced FBI informant to OTHER unnamed council members. Investigation explicitly described as continuing.');

--------------------------------------------------------------
-- UPDATE: Gay-Dagnogo — multi-campaign donor mapping
--------------------------------------------------------------

UPDATE entities SET
    notes = entities.notes || ' | CAMPAIGN FINANCE: $1,000 to Sheffield mayoral, $750 to Todd Perkins mayoral, $300 to Whitfield-Calloway council, $1,000 to Young council. Total known political donations: $3,050+. Listed occupation variously as: manager at Team Wellness, UAW government affairs representative. Network campaign finance node — distributes money across Detroit political ecosystem while serving as City Ombudsman.'
WHERE id = 'gay-dagnogo-sherry';

--------------------------------------------------------------
-- NEW: Marshall Bullock — State Board of Education
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('bullock-marshall', 'Marshall Bullock II', 'person',
    'MI State Board of Education member (appointed Dec 2022 by Whitmer, term until Jan 2029). Former MI State Senator (D-Detroit, 2019-2023). Leads Duggan government affairs. Co-endorsed Duggan for Governor Aug 2025 alongside Banks. University of Phoenix B.A. Human Services. A sitting State Board of Education member endorsed alongside a 9-time convicted felon who runs charter schools under MDE oversight. State Board oversees MDE which issued Banks certificate.');

--------------------------------------------------------------
-- NEW: Gasper Fiore — convicted towing bribery
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('fiore-gasper', 'Gasper Fiore', 'person',
    'Towing consultant. CONVICTED: bribery, sentenced 21 months (2018). Donated $500 to Todd Perkins mayoral campaign. Another convicted felon in the campaign finance orbit. Towing industry = Operation Northern Hook nexus.');

--------------------------------------------------------------
-- NOTE: Todd Perkins mayoral candidate — VERIFY if same as P55623
--------------------------------------------------------------

-- Todd Perkins ran for Detroit mayor in 2025 ($219K raised)
-- Gay-Dagnogo donated $750 to his campaign
-- Gasper Fiore (convicted bribery) donated $500
-- NEED TO VERIFY: Is this the SAME Todd R. Perkins (P55623, Perkins Law Group)
-- who represented Banks? If YES: Gay-Dagnogo funded Banks's attorney's mayoral run
-- while she was City Ombudsman. If NO: separate individual, still note Fiore.

--------------------------------------------------------------
-- RELATIONSHIPS: Federal corruption threads
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('thornton-glynis', 'johnson-bert', 'cooperator', 'FBI cooperator — secretly recorded Johnson at his home Nov 2015', 'AP News + Detroit News + Deadline Detroit',
    'Education corruption (EAA school bribery) → legislative corruption (ghost employee). Same cooperator links both. FBI thread runs through schools to legislature.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('spivey-andre', 'operation-northern-hook', 'defendant', 'First public case in ongoing FBI probe', 'BridgeDetroit Sep 2021',
    'Spivey introduced FBI informant to OTHER unnamed council members. Investigation ongoing. Who else was introduced?');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bullock-marshall', 'banks-brian', 'co-endorser', 'Both endorsed Duggan for Governor Aug 2025', 'mikeduggan.com/endorsements + Metro Detroit News',
    'Sitting State Board of Education member endorsed alongside 9-time convicted felon charter school operator. State Board oversees MDE which issued Banks certificate.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('gay-dagnogo-sherry', 'perkins-todd', 'campaign-finance', '$750 donation to Todd Perkins mayoral campaign', 'Crain''s Detroit Business Jul 2025',
    'VERIFY if same Todd Perkins as P55623 (Banks prior counsel). If yes: Ombudsman funded Banks attorney''s mayoral run.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('thornton-glynis', 'johnson-bert', 'cooperator', 'record', 'FBI cooperator — recorded at his home', 'DOJ filings');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('spivey-andre', 'operation-northern-hook', 'defendant', 'record', 'First case in ongoing FBI Detroit probe', 'BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bullock-marshall', 'banks-brian', 'co-endorser', 'record', 'Both endorsed Duggan Aug 2025', 'mikeduggan.com');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fiore-gasper', 'perkins-todd', 'campaign-finance', 'record', '$500 donation — convicted bribery donor', 'Crain''s Detroit');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('thornton-glynis', 'person', 'Glynis Thornton (EAA cooperator)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('operation-northern-hook', 'entity', 'Operation Northern Hook (FBI — ONGOING)', 1);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('bullock-marshall', 'person', 'Marshall Bullock (State Board of Ed)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('fiore-gasper', 'person', 'Gasper Fiore (convicted bribery)', 4);
