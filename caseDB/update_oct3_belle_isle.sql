-- caseDB update: Oct 3, 2026
-- Belle Isle Park Advisory Committee discovery
-- GLLG team correction (Murphy + Harmon replace Thomas)
-- Crump-Gibson as Purpose Foundation attorney-in-fact
-- Green cards evidence
-- Run: sqlite3 caseDB.sqlite < update_oct3_belle_isle.sql

--------------------------------------------------------------
-- NEW ENTITY: Belle Isle Park Advisory Committee
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('belle-isle-pac', 'Belle Isle Park Advisory Committee', 'org', NULL,
    'Michigan DNR advisory body. Mayor-appointed members. Banks is member. Contact page revised 2/12/2026. Source: michigan.gov/dnr/about/boards/belle-isle/committee-members');

--------------------------------------------------------------
-- NEW ENTITIES: Belle Isle committee members
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('elliott-meagan', 'Dr. Meagan Elliott', 'person', 'elliottm@belleisleconservancy.org',
    'Chair, Belle Isle Park Advisory Committee. Belle Isle Conservancy.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('peek-lonnie', 'Rev. Lonnie Peek', 'person', 'lonniepeek@aol.com',
    'Vice Chair, Belle Isle Park Advisory Committee.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('curis-michael', 'Michael Curis', 'person', 'mcuris7@aol.com',
    'Member, Belle Isle Park Advisory Committee.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('woods-sommer', 'Sommer Woods', 'person', 'sommerwoods0718@gmail.com',
    'Member, Belle Isle Park Advisory Committee. Detroit City Council appointed. Principal consultant at Sommer Solutions, director of external relations for M1-RAIL. Former City of Detroit film/culture director under Mayor Bing.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('lugo-thomas-angela', 'Angela Lugo-Thomas', 'person', 'alugothomas72@gmail.com',
    'Member, Belle Isle Park Advisory Committee.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('howard-melia', 'Melia Howard', 'person', 'mhoward@thepeoplemover.com',
    'Deputy Mayor of Detroit. Member, Belle Isle Park Advisory Committee. Mayor appointed. Former Director of Community Engagement, Director of Special Projects, Dept of Neighborhoods manager District 5. CVI Shotstoppers initiative.');

-- DNR representatives
INSERT OR IGNORE INTO entities (id, name, type, email, phone, notes)
VALUES ('hunt-louise', 'Louise Hunt', 'person', 'huntl4@michigan.gov', '248-803-5528',
    'DNR Urban District Supervisor (WOC). Belle Isle Park Advisory Committee DNR representative. State employee.');

INSERT OR IGNORE INTO entities (id, name, type, email, phone, notes)
VALUES ('fitch-gail', 'Gail Fitch', 'person', 'fitchg@michigan.gov', '313-817-9217',
    'DNR Park Supervisor. Belle Isle Park Advisory Committee DNR representative. State employee.');

--------------------------------------------------------------
-- CORRECT GLLG TEAM: Murphy + Harmon (not Thomas)
--------------------------------------------------------------

-- Remove placeholder Thomas entry
DELETE FROM entities WHERE id = 'thomas-gllg';
DELETE FROM relationships WHERE entity_a = 'thomas-gllg' OR entity_b = 'thomas-gllg';
DELETE FROM graph_edges WHERE source = 'thomas-gllg' OR target = 'thomas-gllg';
DELETE FROM graph_nodes WHERE id = 'thomas-gllg';

-- Add actual GLLG attorneys
INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('murphy-anisha', 'Anisha Murphy', 'person', NULL,
    'GLLG attorney. Newest team member. Business & Corporate Law, Transactional Law, Estate Planning. Mission: serving Black and Brown communities build wealth. Philosophical conflict: firm defending Banks who extracts $4.28M from 99.2% Black student schools.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('harmon-henri', 'Henri Harmon', 'person', NULL,
    'GLLG attorney. Practice areas TBD from further profiling.');

--------------------------------------------------------------
-- UPDATE GLLG: correct address
--------------------------------------------------------------

UPDATE entities SET
    addresses = '["1 Towne Square, Ste. 1835, Southfield, MI 48076"]',
    phone = '1-888-478-5253',
    notes = 'Boutique firm, 4 attorneys: Crump-Gibson, Alcendor, Murphy, Harmon. Southfield. Retained by Banks ~Sep 29. admin@gllegalgroup.com. tagline: Real People Real Issues Real Solutions. Practice: Business, Criminal, Family, Litigation, Probate, Real Estate, Trademark.'
WHERE id = 'gllg';

--------------------------------------------------------------
-- UPDATE BANKS: add Belle Isle + brianbanksjd email
--------------------------------------------------------------

UPDATE entities SET
    email = 'brianbanksjd@gmail.com',
    notes = entities.notes || ' | Belle Isle Park Advisory Committee member (Mayor appointed). michigan.gov/dnr bio lists JD without bar admission disclosure. Email uses JD credential in address. Discovered Oct 3 2026.'
WHERE id = 'banks-brian';

--------------------------------------------------------------
-- UPDATE CRUMP-GIBSON: attorney-in-fact relationship
--------------------------------------------------------------

UPDATE entities SET
    notes = 'P73178. Lead attorney on Banks defense. Purpose Foundation attorney-in-fact (LARA filings — pre-existing relationship with Banks entities BEFORE entering as defense counsel). Sent disclaimer Oct 1: NOT retained for law enforcement. Entered both 4301 and 4349 Sep 30.'
WHERE id = 'crump-gibson-jehan';

--------------------------------------------------------------
-- RELATIONSHIPS: Belle Isle
--------------------------------------------------------------

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-brian', 'belle-isle-pac', 'board-member', 'Mayor-appointed committee member', 'michigan.gov/dnr Belle Isle committee page, revised 2/12/2026',
    'Another institutional position held under false pretenses. Bio lists JD, omits no bar admission. moses-parks parallel: man compared to Parks Commissioner is on a parks committee.');

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('howard-melia', 'belle-isle-pac', 'board-member', 'Deputy Mayor, Mayor-appointed committee member', 'michigan.gov/dnr');

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('elliott-meagan', 'belle-isle-pac', 'board-member', 'Chair', 'michigan.gov/dnr');

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('woods-sommer', 'belle-isle-pac', 'board-member', 'Detroit City Council appointed', 'michigan.gov/dnr');

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('hunt-louise', 'belle-isle-pac', 'board-member', 'DNR Urban District Supervisor representative', 'michigan.gov/dnr');

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('fitch-gail', 'belle-isle-pac', 'board-member', 'DNR Park Supervisor representative', 'michigan.gov/dnr');

--------------------------------------------------------------
-- RELATIONSHIPS: GLLG team corrections
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('murphy-anisha', 'gllg', 'employer', 'Attorney at Great Lakes Legal Group PLLC', 'GLLG website');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('harmon-henri', 'gllg', 'employer', 'Attorney at Great Lakes Legal Group PLLC', 'GLLG website');

-- Crump-Gibson Purpose Foundation attorney-in-fact
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('crump-gibson-jehan', 'purpose-foundation', 'attorney', 'Attorney-in-fact for Purpose Foundation on LARA filings', 'LARA deep mine Sep 19 2026',
    'PRE-EXISTING relationship with Banks entities. She helped form the Foundation before becoming defense counsel. Cannot be fully independent — her own signature is on entity formation docs.');

--------------------------------------------------------------
-- RELATIONSHIPS: Deputy Mayor to City of Detroit
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('detroit-mayor-office', 'Office of the Mayor of Detroit', 'org',
    'Current Mayor Mike Duggan. Appointed Banks to Belle Isle committee.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('howard-melia', 'detroit-mayor-office', 'employer', 'Deputy Mayor of Detroit', 'michigan.gov/dnr, City of Detroit');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-brian', 'detroit-mayor-office', 'appointment', 'Mayor-appointed to Belle Isle Park Advisory Committee', 'michigan.gov/dnr',
    'City of Detroit appointed a 9-time convicted felon (6 felonies) to a state parks committee.');

--------------------------------------------------------------
-- EVIDENCE: Belle Isle discovery
--------------------------------------------------------------

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('belle-isle-discovery-oct3',
    'Belle Isle Park Advisory Committee — Banks member discovery',
    'web-scrape',
    'michigan.gov/dnr/about/boards/belle-isle/committee-members',
    'Banks listed as Mayor-appointed member. Bio lists JD without bar admission. Email: brianbanksjd@gmail.com. Contact page revised 2/12/2026. Committee includes Deputy Mayor Melia Howard and 2 DNR state employees.',
    '2026-10-03',
    '["banks-brian", "belle-isle-pac", "howard-melia", "hunt-louise", "fitch-gail"]',
    '["2026-4349-CZ"]',
    'Robert Moses parallel became literal: man compared to Parks Commissioner is on a parks committee. Analysis published Oct 1, discovery Oct 3 — 48 hours.'
);

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('green-cards-oct3',
    'Green cards — 6 signed federal/state agency return receipts',
    'postal-receipt',
    'PS Form 3811 return receipts, PS Form 3665 Certificate of Mailing',
    'Signed return receipts from USAO EDMI, US Trustee Region 9, FBI Detroit, DEA Detroit, MDE Office of Educator Excellence, Michigan AG. Certificate of Mailing (Sep 10) to AG + Attorney Grievance Commission (UPL + Bar). Photos sent to GLLG as reply-all Oct 3 3:00 PM.',
    '2026-10-03',
    '["banks-brian", "gllg", "crump-gibson-jehan"]',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    'Physical proof all agencies received and signed for evidence packets. Zero commentary sent — just photos of green cards.'
);

--------------------------------------------------------------
-- EVENTS: Oct 3
--------------------------------------------------------------

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-03', 'Green cards sent to GLLG — no commentary',
    'Kevin reply-alls photos of 6 signed return receipts (USAO, FBI, DEA, US Trustee, MDE, AG) plus Certificate of Mailing to AG/Attorney Grievance Commission. No words. Just receipts.',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    '["banks-brian", "gllg", "crump-gibson-jehan"]',
    'Email with photo attachments',
    'Physical proof every named agency received and signed for packets. Demonstrates Kevin''s claims are operational, not hypothetical. $0 cost, ~$1,000 in GLLG review time.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-03', 'Belle Isle Park Advisory Committee — Banks member discovered',
    'Kevin discovers Banks sits on Michigan DNR Belle Isle Park Advisory Committee. Mayor-appointed. Bio on michigan.gov lists JD without bar admission. Robert Moses parallel became literal 48 hours after historical-pattern analysis published.',
    '["2026-4349-CZ"]',
    '["banks-brian", "belle-isle-pac", "howard-melia"]',
    'michigan.gov/dnr/about/boards/belle-isle/committee-members',
    'Another institutional position held under false pretenses. Moses-to-parks parallel. Deputy Mayor now has felony record. 2 DNR state employees on notice.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-03', 'Belle Isle notification email sent — 15 recipients',
    'Kevin emails full committee (Chair, Vice Chair, 4 members including Banks and Deputy Mayor), 2 DNR state employees, GLLG (both addresses), M.L. Elrick (Free Press), BCC Smith defendants. Full criminal history table, 11 site links, git mirror. Sent from eco.primal@pm.me.',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    '["banks-brian", "belle-isle-pac", "howard-melia", "hunt-louise", "fitch-gail", "gllg", "crump-gibson-jehan", "elliott-meagan"]',
    'Email sent Oct 3 ~3:45 PM',
    'Nuclear: Deputy Mayor, 2 state employees, press, defense counsel all on same email about client''s 9 felony convictions. Anti-SLAPP protected (MCL 691.1731). $0 cost. No silos.');

--------------------------------------------------------------
-- GRAPH EDGES: Belle Isle
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'belle-isle-pac', 'board-member', 'record', 'Mayor-appointed committee member', 'michigan.gov/dnr');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('howard-melia', 'belle-isle-pac', 'board-member', 'record', 'Deputy Mayor, Mayor-appointed', 'michigan.gov/dnr');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('howard-melia', 'detroit-mayor-office', 'employer', 'record', 'Deputy Mayor', 'michigan.gov/dnr');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'detroit-mayor-office', 'appointment', 'record', 'Appointed to Belle Isle committee', 'michigan.gov/dnr');

-- Crump-Gibson to Purpose Foundation (attorney-in-fact — PRE-EXISTING)
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('crump-gibson-jehan', 'purpose-foundation', 'attorney', 'record', 'Attorney-in-fact on LARA filings — pre-existing relationship', 'LARA deep mine Sep 19');

-- GLLG team corrections
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('murphy-anisha', 'gllg', 'employer', 'record', 'Attorney at GLLG', 'gllegalgroup.com');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('harmon-henri', 'gllg', 'employer', 'record', 'Attorney at GLLG', 'gllegalgroup.com');

--------------------------------------------------------------
-- GRAPH NODES: new entities
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('belle-isle-pac', 'entity', 'Belle Isle Park Advisory Committee', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('howard-melia', 'person', 'Melia Howard (Deputy Mayor)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('detroit-mayor-office', 'entity', 'Office of the Mayor of Detroit', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('murphy-anisha', 'person', 'Anisha Murphy', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('harmon-henri', 'person', 'Henri Harmon', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('elliott-meagan', 'person', 'Dr. Meagan Elliott', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('hunt-louise', 'person', 'Louise Hunt (DNR)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('fitch-gail', 'person', 'Gail Fitch (DNR)', 4);
