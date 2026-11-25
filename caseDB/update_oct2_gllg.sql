-- caseDB update: Oct 2, 2026
-- GLLG firm expansion: attorneys, contact info, board connections,
-- Crump-Gibson disclaimer evidence, subgraph entities
-- Run: sqlite3 caseDB.sqlite < update_oct2_gllg.sql

--------------------------------------------------------------
-- UPDATE EXISTING ENTITIES: add phone, address, notes
--------------------------------------------------------------

UPDATE entities SET
    phone = '(248) 395-3699',
    addresses = '["27350 Southfield Road, Suite A, Lathrup Village, MI 48076-3409"]',
    notes = 'Boutique firm, 4 attorneys. Southfield/Lathrup Village. Retained by Banks ~Sep 29. admin@gllegalgroup.com confirmed CC on Crump-Gibson emails.'
WHERE id = 'gllg';

UPDATE entities SET
    phone = '(248) 395-3699',
    notes = 'P73178. Lead attorney on Banks defense. Sent disclaimer Oct 1 2:31 PM: NOT retained for law enforcement, police reports, or PPO proceedings. Einstein quote on materials.'
WHERE id = 'crump-gibson-jehan';

--------------------------------------------------------------
-- NEW ENTITIES: other GLLG attorneys
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('alcendor-ayanna', 'Ayanna Alcendor', 'person', NULL,
    'GLLG attorney. Connection to The Childrens Center of Wayne County (board/professional). Practice areas TBD.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('thomas-gllg', 'Attorney Thomas (GLLG)', 'person', NULL,
    'GLLG attorney. Full name and practice areas TBD from further profiling.');

-- The Children's Center of Wayne County
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('childrens-center-wayne', 'The Childrens Center of Wayne County', 'org',
    '$20-30M nonprofit serving Wayne County children. Former CEO Nicole Wells Stallworth (wife of Thomas Stallworth III). Current board includes a Simone Smith (NOT defendant Simone Smith). Alcendor (GLLG) has professional connections here.');

-- Thomas Stallworth III
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('stallworth-thomas-iii', 'Thomas Stallworth III', 'person',
    'Former Michigan State Rep (D-Detroit). Wife Nicole Wells Stallworth was CEO of The Childrens Center through May 2024. Political network connection. Power chain to Banks appointment.');

-- Nicole Wells Stallworth
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('stallworth-nicole', 'Nicole Wells Stallworth', 'person',
    'Former CEO, The Childrens Center of Wayne County (through May 2024). Wife of Thomas Stallworth III. Oversaw $20-30M nonprofit.');

--------------------------------------------------------------
-- RELATIONSHIPS: GLLG attorney connections
--------------------------------------------------------------

-- Alcendor employed at GLLG
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('alcendor-ayanna', 'gllg', 'employer', 'Attorney at Great Lakes Legal Group PLLC', 'GLLG website');

-- Thomas employed at GLLG
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('thomas-gllg', 'gllg', 'employer', 'Attorney at Great Lakes Legal Group PLLC', 'GLLG website');

-- GLLG retained by Banks
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date)
VALUES ('gllg', 'banks-brian', 'attorney', 'Firm retained to defend Banks in civil cases', 'Crump-Gibson email Sep 30', '2026-09-30');

-- Alcendor connection to Children's Center
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('alcendor-ayanna', 'childrens-center-wayne', 'board-member', 'Professional connection to The Childrens Center', 'OSINT profiling Oct 1',
    'Nature of connection (board, counsel, volunteer) TBD. Creates potential conflict under MRPC 1.7(a)(2).');

-- Stallworth III connection to Children's Center
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('stallworth-thomas-iii', 'childrens-center-wayne', 'board-member', 'Wife was CEO through May 2024. Political influence over org.', 'Public records, news');

-- Nicole Stallworth CEO of Children's Center
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date, end_date)
VALUES ('stallworth-nicole', 'childrens-center-wayne', 'employer', 'CEO of The Childrens Center', 'Public records', NULL, '2024-05-01');

-- Stallworth marriage
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('stallworth-thomas-iii', 'stallworth-nicole', 'family', 'Married', 'Public records');

-- Ellis connection to Children's Center
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('ellis-tracey', 'childrens-center-wayne', 'board-member', 'Board connection to The Childrens Center', 'OSINT profiling Oct 1',
    'Ellis sits on board(s) overlapping with Banks network and Childrens Center. Part of racketeering pattern.');

--------------------------------------------------------------
-- EVIDENCE: Crump-Gibson disclaimer email
--------------------------------------------------------------

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('crump-gibson-disclaimer-oct1',
    'Crump-Gibson Disclaimer Email — Not Retained for Law Enforcement',
    'email',
    'Email from jehan@gllegalgroup.com Oct 1 2:31 PM',
    'Crump-Gibson explicitly states: I am NOT retained in connection with any law enforcement matters or [police reports/PPO proceedings]. Confirms scope limitation. CC admin@gllegalgroup.com.',
    '2026-10-01',
    '["crump-gibson-jehan", "gllg", "banks-brian"]',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    'Key evidence: defense counsel disclaiming responsibility for Banks law enforcement conduct. Screenshot preserved. Proves GLLG aware of separate proceedings.'
);

-- Kevin morning email Oct 2 (standing, boards, GAL)
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids)
VALUES ('kevin-gllg-morning-oct2',
    'Kevin Morning Email to GLLG — Standing, Boards, Children',
    'email',
    'Email from eco.primal@pm.me to admin@gllegalgroup.com Oct 2 ~9:45 AM',
    'Three questions: (1) Will Banks stay out of custody case, (2) Are GLLG looking at board names in RICO pattern, (3) Have they read GAL motion. Attached GAL_motion_20260820.pdf.',
    '2026-10-02',
    '["crump-gibson-jehan", "gllg", "banks-brian"]',
    '["2026-4301-CZ", "2026-4349-CZ", "26-108221-DC"]'
);

-- Kevin 9-line followup Oct 2
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids)
VALUES ('kevin-9line-followup-oct2',
    'Kevin 9-Line Reply — Federal Referrals Pre-Date Retaliation',
    'email',
    'Reply-all from eco.primal@pm.me Oct 2',
    'Attached 9LINE_FEDERAL_REFERRAL_SEP25.pdf. Four sentences establishing federal agencies had everything before Banks Sep 28 police report and Sep 29 PPO appearance.',
    '2026-10-02',
    '["crump-gibson-jehan", "gllg", "banks-brian"]',
    '["2026-4301-CZ", "2026-4349-CZ"]'
);

--------------------------------------------------------------
-- EVENTS
--------------------------------------------------------------

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-01', 'Crump-Gibson disclaims law enforcement scope',
    'Jehan Crump-Gibson emails Kevin at 2:31 PM: NOT retained for law enforcement matters, police reports, or PPO proceedings. CC admin@gllegalgroup.com. Confirms awareness of separate proceedings.',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    '["crump-gibson-jehan", "gllg", "banks-brian"]',
    'Email screenshot',
    'Defense counsel creating written record of scope limitation. Proves GLLG will not defend Banks retaliatory conduct. Sporulation signal — counsel forming protective spore around narrow scope.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-02', 'Kevin morning email — standing, boards, GAL motion',
    'Email to GLLG admin and Smiths. Three questions re Banks standing in custody, board overlap with RICO, GAL motion. Attached GAL_motion_20260820.pdf.',
    '["2026-4301-CZ", "2026-4349-CZ", "26-108221-DC"]',
    '["crump-gibson-jehan", "gllg", "banks-brian"]',
    'Email',
    'Documents GLLG awareness of (1) Banks lack of standing in custody, (2) board connections to racketeering pattern, (3) GAL motion predating Kevin involvement. Creates MRPC obligation chain.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-02', 'Kevin sends 9-line federal referral cover to GLLG',
    'Reply-all attaching 9LINE_FEDERAL_REFERRAL_SEP25.pdf. Establishes federal agencies had packets before Banks Sep 28 GPW report and Sep 29 PPO appearance.',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    '["crump-gibson-jehan", "gllg", "banks-brian"]',
    'Email',
    'Timeline evidence: federal referrals (Sep 21-25) predate both retaliatory events (Sep 28-29). Proves Banks escalated AFTER federal agencies were already apprised.');

--------------------------------------------------------------
-- GRAPH EDGES: GLLG subgraph
--------------------------------------------------------------

-- GLLG attorneys
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('alcendor-ayanna', 'gllg', 'employer', 'record', 'Attorney at GLLG', 'GLLG website');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('thomas-gllg', 'gllg', 'employer', 'record', 'Attorney at GLLG', 'GLLG website');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('gllg', 'banks-brian', 'attorney', 'record', 'Firm represents Banks in civil defense', 'Crump-Gibson email Sep 30');

-- Children's Center connections
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('alcendor-ayanna', 'childrens-center-wayne', 'board-member', 'inference', 'Professional connection — nature TBD', 'OSINT profiling Oct 1');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-thomas-iii', 'childrens-center-wayne', 'board-member', 'record', 'Wife was CEO through May 2024', 'Public records');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-nicole', 'childrens-center-wayne', 'employer', 'record', 'CEO through May 2024', 'Public records');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-thomas-iii', 'stallworth-nicole', 'family', 'record', 'Married', 'Public records');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('ellis-tracey', 'childrens-center-wayne', 'board-member', 'inference', 'Board connection — nature TBD', 'OSINT profiling Oct 1');

-- Graph nodes for new entities
INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('alcendor-ayanna', 'person', 'Ayanna Alcendor', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('thomas-gllg', 'person', 'Attorney Thomas (GLLG)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('childrens-center-wayne', 'entity', 'The Childrens Center of Wayne County', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('stallworth-thomas-iii', 'person', 'Thomas Stallworth III', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('stallworth-nicole', 'person', 'Nicole Wells Stallworth', 3);
