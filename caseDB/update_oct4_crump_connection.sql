-- caseDB update: Oct 4, 2026 (Crump Connection — Web OSINT confirmation)
-- Source: Web search, LinkedIn, LawyerLegion, GLLG website
--
-- CRITICAL FINDINGS:
-- 1. chojlf.com = CRUMP HALL OF JUSTICE LAW FIRM, PLLC
--    200 E Big Beaver Rd, Troy MI 48083. Phone: (248) 270-6262.
--    Website: mychoj.com. Hall's separate law practice from GLLG.
-- 2. Crump-Gibson attended MSU (undergrad). Hall has crumpver@msu.edu.
--    BOTH Crumps at Michigan State University.
-- 3. Crump-Gibson is a HEARING PANELIST for MI Attorney Discipline Board.
--    She sits on the body that receives AGC complaints (that Kevin filed!).
-- 4. Hall interned at BCBS of Michigan (2016-2017).
--    BCBS is a Save Detroit Jobs / Detroit Leaders PAC donor.
-- 5. Hall also works at Scarfone & Geen P.C. (civil defense firm,
--    Madison Heights) since Dec 2018 — concurrent with Banks representation.
-- 6. Hall licensed 2018 (MI bar). Crump-Gibson is senior.
--
-- Run: sqlite3 caseDB.sqlite < update_oct4_crump_connection.sql

--------------------------------------------------------------
-- CRUMP HALL OF JUSTICE LAW FIRM
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('chojlf', 'Crump Hall of Justice Law Firm PLLC', 'org',
    'Verkeydia Hall''s personal law firm (separate from GLLG). 200 E Big Beaver Rd, Troy MI 48083. Also listed at 615 Griswold St Ste 1300, Detroit MI 48226. Phone: (248) 270-6262. Website: mychoj.com. Email: vhall@chojlf.com. CHOJLF = Crump Hall Of Justice Law Firm. Practice areas: Criminal Defense, Family Law, Business Law, ADR, Estate Planning, Real Estate. The firm NAME contains "CRUMP" — Hall''s maiden name.');

--------------------------------------------------------------
-- CRUMP-GIBSON — AGC DISCIPLINE BOARD PANELIST
--------------------------------------------------------------

-- FROM GLLG WEBSITE: Crump-Gibson serves as
-- "Hearing Panelist for the Michigan Attorney Discipline Board"
-- This means she sits on the SAME body that processes AGC complaints.
-- Kevin filed AGC complaints against Meihn, Hall, and notifications
-- about Moreland and Crump-Gibson herself.
-- If Crump-Gibson is on a discipline hearing panel, she would have
-- colleagues who receive/process those very complaints.
-- This is a potential conflict of interest in the AGC process.

-- Also: Crump-Gibson = Wolverine Bar Association past President (2016-17)
-- Also: Crump-Gibson attended MSU (undergrad) + Wayne State Law
-- Also: CitizenDetroit Action Group Board Vice President
-- Also: Delta Sigma Theta Sorority, Detroit Alumnae Chapter

UPDATE entities SET
    notes = 'Managing partner, GLLG. LARA entity 802112914 (Member/Manager). AGC DISCIPLINE BOARD: Crump-Gibson serves as HEARING PANELIST for Michigan Attorney Discipline Board — the body that processes AGC complaints. Kevin filed AGC complaints re: Meihn, Hall, Moreland, and Crump-Gibson notification. Her colleagues on that board would process those complaints. MSU undergrad (PoliSci + English). Wayne State Law. Wolverine Bar Association past President (2016-17). Delta Sigma Theta. CitizenDetroit Action Group Board VP. Recognized by Sen. Gary Peters for MI Judicial Advisory Committee. Crump-Gibson confirmed in writing (Oct 1, 2:28 PM): NOT retained for law enforcement, police reports, or PPO proceedings.'
WHERE id = 'crump-gibson-jehan';

-- Create if not exists
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('crump-gibson-jehan', 'Jehan Crump-Gibson', 'person',
    'Managing partner GLLG. MI Attorney Discipline Board Hearing Panelist. MSU undergrad. Wayne State Law.');

--------------------------------------------------------------
-- HALL — DUAL EMPLOYMENT + BCBS
--------------------------------------------------------------

-- Hall works CONCURRENTLY at:
-- 1. Scarfone & Geen, P.C. (since Dec 2018) — civil defense firm
--    Represents insurance carriers + Fortune 500 companies
--    Madison Heights, MI
-- 2. Crump Hall of Justice Law Firm (her own practice)
-- 3. Banks representation (via what entity? GLLG? or CHOJLF?)
--
-- BCBS CONNECTION:
-- Hall interned at Blue Cross Blue Shield of Michigan (May 2016 - Apr 2017)
-- BCBS is listed as a Save Detroit Jobs / Detroit Leaders PAC contributor
-- This creates a potential network connection:
--   Hall → BCBS (intern) → Save Detroit Jobs (donor) → Banks orbit

--------------------------------------------------------------
-- MSU CRUMP CONNECTION EVIDENCE
--------------------------------------------------------------

-- Crump-Gibson: MSU undergrad (Political Science + English)
-- Hall: crumpver@msu.edu (MSU email, "crump" + "ver" for Verkeydia)
-- Both Crumps at Michigan State University
-- Strong inference: family (sisters, cousins)
-- Not yet confirmed publicly
-- If related: Banks legal team = Crump family operation
--   Crump-Gibson (GLLG founder) → Hall (CHOJLF owner) → Moreland (PCA Director)
--   All three represent Banks. Moreland also sits on Banks's school board.

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('hall-verkeydia', 'chojlf', 'controls', 'confirmed', 'Owner of Crump Hall of Justice Law Firm. Firm name contains maiden name CRUMP.', 'LARA + web');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('crump-gibson-jehan', 'agc-discipline-board', 'member', 'confirmed', 'Hearing Panelist for MI Attorney Discipline Board. Listed on GLLG website bio.', 'gllegalgroup.com');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('chojlf', 'entity', 'Crump Hall of Justice Law Firm (Hall, Troy MI)', 2);
