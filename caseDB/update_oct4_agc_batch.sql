-- caseDB update: Oct 4, 2026 (morning batch)
-- AGC complaints: Meihn (NEW), Moreland (SUPPLEMENT), Hall (NEW)
-- AGC notification: Crump-Gibson (guidance, not discipline)
-- Emails: Crump-Gibson dove, GLLG going-dark
-- Run: sqlite3 caseDB.sqlite < update_oct4_agc_batch.sql

--------------------------------------------------------------
-- NEW ENTITY: Gregory Meihn
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, email, phone, notes)
VALUES ('meihn-gregory', 'Gregory M. Meihn', 'person', NULL, NULL,
    'P65372. Admitted 2003. Active Member in Good Standing. CURRENT: Gordon Rees Scully Mansukhani LLP (Detroit office, Employment & Education Law). FORMER: Foley & Mansfield PLLP (Ferndale). gmeihn@foleymansfield.com BOUNCED Oct 4 — left firm. MacDowell board counsel. Testified TCR 22-12 Feb 9 2023: Banks has "integrity, hard work, honesty, transparency, and compliance." Weekly meetings with Banks. Reviewed §5.2 false representation. AGC complaint filed Oct 4 2026: MRPC 3.3, 8.4(c), 1.13.');

--------------------------------------------------------------
-- UPDATE: Moreland P-number confirmed
--------------------------------------------------------------

UPDATE entities SET
    notes = 'P55993. Admitted June 7, 1999. Active Member in Good Standing. AAG, Michigan Attorney General. 3030 W Grand Blvd Ste 10-350, Detroit MI 48202-6030. PCA Vice Chair. AG office ARGUED AGAINST Banks certificate at TCR 22-12 — then Moreland sits on Banks board. AGC complaint filed Sep 10 2026. SUPPLEMENT filed Oct 4: adds MRPC 1.11, 1.7 institutional conflict.'
WHERE id = 'moreland-lamar';

--------------------------------------------------------------
-- NEW ENTITY: Verkeydia Hall
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, email, phone, notes)
VALUES ('hall-verkeydia', 'Verkeydia Hall', 'person', NULL, '248-270-6262',
    'Licensed 2018. Active Member in Good Standing. P-number TBD (confirm via SBM 800-968-1442). Crump Hall of Justice Law Firm PLLC, 615 Griswold St Ste 1300, Detroit MI 48226. Practice: Criminal Defense, Family Law, ADR, Business Law. MacDowell board member. Licensed attorney who accepted §5.2 false representation without objection. AGC complaint filed Oct 4 2026: MRPC 8.4(c), 8.4(d).');

--------------------------------------------------------------
-- UPDATE: Meihn firm change
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('grsm', 'Gordon Rees Scully Mansukhani LLP', 'org',
    'National law firm. Detroit office. Meihn current employer. Employment & Education Law practice group.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('foley-mansfield', 'Foley & Mansfield PLLP', 'org',
    'Former firm for Meihn. 130 E Nine Mile Rd, Ferndale MI 48220. gmeihn@foleymansfield.com bounced Oct 4 2026: 550 5.4.1 Recipient address rejected.');

--------------------------------------------------------------
-- RELATIONSHIPS: Meihn
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('meihn-gregory', 'macdowell', 'board-counsel', 'Board counsel, weekly meetings with Banks', 'TCR 22-12 testimony',
    'Testified Feb 9 2023 that Banks has integrity. Reviewed Management Agreement §5.2 weekly. False No Related Parties representation.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('meihn-gregory', 'grsm', 'employer', 'Partner, Detroit office, Employment & Education Law', 'GRSM website');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('meihn-gregory', 'foley-mansfield', 'former-employer', 'Former partner', 'SBM directory + bounce-back',
    'Email bounced Oct 4 2026. Moved to GRSM.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('meihn-gregory', 'banks-brian', 'professional-support', 'TCR 22-12 character witness + weekly board counsel meetings', 'TCR 22-12 Final Decision',
    'Credential-washed Banks at tribunal. Most senior professional endorsement in the network. MRPC 3.3 violation: candor toward tribunal.');

--------------------------------------------------------------
-- RELATIONSHIPS: Hall
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('hall-verkeydia', 'macdowell', 'board-member', 'MacDowell Preparatory Academy board member', 'MacDowell board listing',
    'Licensed attorney on board. Accepted §5.2 false representation. Heightened professional duty to identify contract fraud.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('hall-verkeydia', 'crump-hall-law', 'employer', 'Crump Hall of Justice Law Firm PLLC', 'Lawyer Legion profile');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('crump-hall-law', 'Crump Hall of Justice Law Firm PLLC', 'org',
    '615 Griswold St Ste 1300, Detroit MI 48226. Verkeydia Hall. Criminal Defense, Family Law.');

--------------------------------------------------------------
-- EVIDENCE: Oct 4 AGC batch
--------------------------------------------------------------

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('agc-meihn-oct4',
    'AGC Complaint — Gregory Meihn P65372 (NEW)',
    'agc-complaint',
    'Filed by Kevin Mok Oct 4 2026',
    'MRPC 3.3 (candor toward tribunal — TCR 22-12 testimony), MRPC 8.4(c) (§5.2 false representation weekly review), MRPC 1.13 (organization as client — testified for Banks personal interest not school interest). Brand new complaint, not supplement.',
    '2026-10-04',
    '["meihn-gregory", "banks-brian", "macdowell", "holland-reginald"]',
    '["2026-4349-CZ"]',
    'Strongest new complaint. Board counsel who testified convicted felon has integrity while reviewing false contract weekly.'
);

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('agc-moreland-supp-oct4',
    'AGC Supplement — Lamar Moreland P55993',
    'agc-supplement',
    'Filed by Kevin Mok Oct 4 2026',
    'Supplements Sep 10 filing. Adds MRPC 1.11 (government officer conflict — AAG on board of entity AG opposed), MRPC 1.7 (concurrent conflict — state employer vs board fiduciary). P55993 confirmed via SBM directory.',
    '2026-10-04',
    '["moreland-lamar", "banks-brian", "pca"]',
    '["2026-4349-CZ"]',
    'AG institutional conflict analysis. AG cannot investigate own employees affiliated org.'
);

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('agc-hall-oct4',
    'AGC Complaint — Verkeydia Hall (NEW)',
    'agc-complaint',
    'Filed by Kevin Mok Oct 4 2026',
    'MRPC 8.4(c) (participation in misrepresentation — §5.2 false No Related Parties), MRPC 8.4(d) (prejudicial to administration of justice). Licensed attorney on board with heightened duty to identify contract fraud.',
    '2026-10-04',
    '["hall-verkeydia", "banks-brian", "macdowell", "holland-reginald"]',
    '["2026-4349-CZ"]',
    'Licensed attorney on board cannot claim ignorance of false contract terms.'
);

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('agc-crump-notification-oct4',
    'AGC Notification — Crump-Gibson P73178 (NOT a complaint)',
    'agc-notification',
    'Filed by Kevin Mok Oct 4 2026',
    'Notification to AGC that Crump-Gibson was placed in structurally conflicted position by prior conduct of Meihn, Moreland, Perlmuter, Perkins. Seeks guidance not discipline. ONLY bar member in network receiving this treatment. Plaintiff offers to testify FOR her. Attorney-in-fact conflict identified Sep 19 — 11 days before she entered.',
    '2026-10-04',
    '["crump-gibson-jehan", "meihn-gregory", "moreland-lamar", "perlmuter-gary", "perkins-todd", "banks-brian"]',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    'Structurally novel filing. Adverse plaintiff filing FOR opposing counsel. No known precedent. Contrast with 15+ adversarial complaints validates all filings.'
);

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('email-dove-crump-oct4',
    'Dove email to Crump-Gibson — draft AGC notification shared before filing',
    'email',
    'eco.primal@pm.me to jehan@gllegalgroup.com',
    'Subject: Dove with an Olive Branch. Sent draft AGC notification for review before filing. Personal note: genuinely sorry she is in this position, believes she does good work, GLLG mission matters. All signal channels open (email, phone, WhatsApp, Discord, site). Cannot apologize for war itself.',
    '2026-10-04',
    '["crump-gibson-jehan", "gllg"]',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    'Maximum professional courtesy. TO: jehan@gllegalgroup.com, CC: admin@gllegalgroup.com. Sent ~8:25 AM Sunday.'
);

INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES ('email-going-dark-oct4',
    'Going dark email to GLLG — proactive disclosure Phase 1',
    'email',
    'eco.primal@pm.me to admin@gllegalgroup.com',
    'Proactive disclosure: what happened today (DPSCD, Chief Judge, AGC batch), what is coming this week (Wayne State, Baker, NCC, Pahara, Tate, Howard, SCAO), why he can do this (combat training — attack/defend/recon/triage simultaneously under fire — doctrine not mania), testimony offer for Crump-Gibson, allies by function not agreement, deadline: Phase 3 Friday then court filings only.',
    '2026-10-04',
    '["gllg", "crump-gibson-jehan", "banks-brian"]',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    'Evening send. Three signals three emails: dove (now), AGC (mail Monday), going-dark (evening). Combat doctrine frame: "What you are seeing is not mania. It is doctrine."'
);

--------------------------------------------------------------
-- EVENTS: Oct 4 morning
--------------------------------------------------------------

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-04', 'AGC batch prepared: Meihn (NEW), Hall (NEW), Moreland (SUPP), Crump-Gibson (NOTIFICATION)',
    'Four AGC filings prepared before 9 AM Sunday. Meihn and Hall are brand new complaints (never filed before). Moreland is supplement to Sep 10 filing with confirmed P55993. Crump-Gibson is structurally novel notification seeking guidance not discipline — adverse plaintiff filing FOR opposing counsel. Total AGC/bar filings now: 18+ across 17 respondents.',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    '["meihn-gregory", "hall-verkeydia", "moreland-lamar", "crump-gibson-jehan", "banks-brian"]',
    'AGC filings + email confirmations',
    'Three-tier signal architecture: dove to Crump-Gibson (respect), AGC filings (record), going-dark to GLLG (doctrine). Plaintiff demonstrates taxonomy of misconduct — different treatment for different culpability levels.'
);

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance)
VALUES ('2026-10-04', 'Dove with an Olive Branch — draft AGC notification sent to Crump-Gibson',
    'Kevin emails Crump-Gibson the draft AGC notification before filing. Subject line: Dove with an Olive Branch. Personal note, all channels open. She is the ONLY bar member receiving this treatment. 15+ others got adversarial complaints.',
    '["2026-4301-CZ", "2026-4349-CZ"]',
    '["crump-gibson-jehan", "gllg"]',
    'Email sent ~8:25 AM Oct 4',
    'No known precedent for adverse plaintiff sharing protective AGC filing with opposing counsel before submission. Structural novelty validates complainant credibility across all other filings.'
);

--------------------------------------------------------------
-- GRAPH EDGES: Oct 4
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('meihn-gregory', 'macdowell', 'board-counsel', 'record', 'Board counsel, weekly meetings, TCR 22-12 testimony', 'TCR 22-12 + AGC complaint');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('meihn-gregory', 'banks-brian', 'credential-wash', 'record', 'Testified Banks has integrity at state tribunal', 'TCR 22-12');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('meihn-gregory', 'grsm', 'employer', 'record', 'Current: Partner, Detroit office', 'GRSM website');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('meihn-gregory', 'foley-mansfield', 'former-employer', 'record', 'Former partner, email bounced Oct 4', 'SBM + bounce-back');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('hall-verkeydia', 'macdowell', 'board-member', 'record', 'Licensed attorney on board', 'MacDowell board listing');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('hall-verkeydia', 'crump-hall-law', 'employer', 'record', 'Crump Hall of Justice Law Firm PLLC', 'Lawyer Legion');

--------------------------------------------------------------
-- GRAPH NODES: Oct 4
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('meihn-gregory', 'person', 'Gregory Meihn P65372', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('hall-verkeydia', 'person', 'Verkeydia Hall', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('grsm', 'entity', 'Gordon Rees Scully Mansukhani LLP', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('foley-mansfield', 'entity', 'Foley & Mansfield PLLP', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('crump-hall-law', 'entity', 'Crump Hall of Justice Law Firm PLLC', 4);
