-- caseDB update: Oct 4, 2026 (LARA Nuclear — Carol Banks + Verkeydia Hall)
-- Source: LARA API SearchByOption=3 (agent search)
--
-- NUCLEAR FINDINGS:
-- 1. Verkeydia Hall MSU email = crumpver@msu.edu. CRUMP IS HER MAIDEN NAME.
--    If Crump-Gibson and Crump-Hall share surname, Banks legal team = family.
-- 2. Carol Banks owns ORIGINAL EASTSIDE SLATE (4th incarnation, filed 2020, ACTIVE)
-- 3. Carol Banks + Spencer Leach parallel Pan-African entity naming
--    Carol: Niger Group, Nile Group II. Spencer: Songhai, Azania, Sudanese Groups.
-- 4. Carol Banks officers overlap: Beverly Nakenge + Kiambu/Kikora Elcock
--    appear on BOTH Original Eastside Slate AND Niger Group. Same core team.
-- 5. Hall entity email: vhall@chojlf.com — domain TBD (Crump Hall Of Justice?)
-- 6. Hall home: 38190 Tralee Trl, Northville 48167
-- 7. Carol Banks home: 1533 Fairview, Detroit 48214
-- 8. Carol Banks email: carolbanks313@gmail.com
--
-- Run: sqlite3 caseDB.sqlite < update_oct4_lara_nuclear.sql

--------------------------------------------------------------
-- CAROL BANKS — FULL ENTITY PORTFOLIO
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Brian Banks''s sister. Former Detroit City Councilwoman Benson Chief of Staff. FBI raid target (dual DPS salary). LARA entities: (1) ORIGINAL EASTSIDE SLATE (802434498, filed 04/09/2020, Active, Good) — 4th incarnation of the endorsement machine. (2) THE NILE GROUP II LLC (801454732, filed 04/11/2008, Active, Good). (3) THE NIGER GROUP (800934647, filed 07/06/2012, Dissolved 12/01/2025). Home/office: 1533 Fairview, Detroit MI 48214. Email: carolbanks313@gmail.com. Parallel Pan-African entity naming with Spencer Leach (Carol: Niger/Nile. Leach: Songhai/Azania/Sudanese). ORIGINAL EASTSIDE SLATE board: Carol Banks (President), Beverly Nakenge (Treasurer, 5510 Yorkshire), Kikora Elcock (Secretary, 1533 Fairview = Carol''s address), Kiambu Elcock (Director, 5567 Bishop), Emberly Vick, Teri Bright (321 W Lafayette), Anthoney Bradford, Carl Collins (XXXXX Myers Rd), Althea Jackson. NIGER GROUP had SAME officers: Carol Banks, Beverly Nakenge, Kiambu Elock. Core team: Banks+Nakenge+Elcock(s).'
WHERE id = 'carol-banks';

-- Create if not exists
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('carol-banks', 'Carol Banks', 'person',
    'Brian Banks''s sister. Former Detroit City Councilwoman Benson Chief of Staff. FBI raid target. 1533 Fairview, Detroit MI 48214. Email: carolbanks313@gmail.com. Controls Original Eastside Slate, Nile Group II, Niger Group.');

--------------------------------------------------------------
-- CAROL BANKS ENTITIES
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('original-eastside-slate', 'Original Eastside Slate', 'org',
    'LARA Entity ID 802434498. Domestic Nonprofit Corporation. Filed 04/09/2020. Active, Good. Agent: Carol Banks, 1533 Fairview, Detroit MI 48214. Email: carolbanks313@gmail.com. FOURTH incarnation of Eastside Slate (after Lemmons 1994, Leach 2008, Lemmons 2019). Carol Banks created her own "Original" version. Officers: Carol Banks (Pres), Beverly Nakenge (Treas, 5510 Yorkshire), Kikora Elcock (Sec, lives at Carol''s address!), Kiambu Elcock (Dir), Emberly Vick, Teri Bright, Anthoney Bradford, Carl Collins, Althea Jackson.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('nile-group-ii', 'The Nile Group II LLC', 'org',
    'LARA Entity ID 801454732. Filed 04/11/2008. Active, Good. Agent: Carol Banks, 1533 Fairview, Detroit 48214. Email: carolbanks313@gmail.com. Pan-African naming parallel to Leach''s Songhai/Azania/Sudanese Groups. "II" implies a Nile Group I exists.');

--------------------------------------------------------------
-- CAROL BANKS ASSOCIATES
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('nakenge-beverly', 'Beverly Nakenge', 'person',
    'Original Eastside Slate Treasurer + Niger Group Treasurer/Director. 5510 Yorkshire, Detroit MI 48224. Core Carol Banks operative — appears on BOTH slate and nonprofit. Carol Banks''s #1 financial officer across multiple entities.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('elcock-kiambu', 'Kiambu Elcock', 'person',
    'Original Eastside Slate Director + Niger Group Secretary/Director. 5567 Bishop, Detroit MI 48224 (also appears at Carol Banks''s 1533 Fairview address via spouse Kikora). Spelled "ELOCK" in Niger Group filing. Core Carol Banks operative.');

--------------------------------------------------------------
-- VERKEYDIA HALL — FULL ENTITY PORTFOLIO + CRUMP CONNECTION
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Attorney. AGC complaint filed (Hall MRPC 8.4c, 8.4d). Filed PPO against Kevin Mok. MAIDEN NAME = CRUMP (confirmed: MSU email crumpver@msu.edu). If related to Jehan CRUMP-Gibson, Banks legal team = family operation. LARA entities: (1) Verkeydia Hall Law PLLC (802338461, filed 06/28/2019, Active). Home: 38190 Tralee Trl, Northville MI 48167. Office: 18444 W. 10 Mile Rd Suite 204, Southfield MI 48075. Email: vhall@chojlf.com (domain = Crump Hall Of Justice Law Firm?). (2) Crump Hall Enterprises Inc (802638003, filed 04/06/2021, Dissolved). Sole officer. (3) Crump Hall Property & Investments Co (802640755, filed 04/12/2021, Dissolved). Sole officer. (4) Crump Properties & Investments LLC (802517883, filed 09/11/2020, Active). Agent addr: 15803 Whitcomb Detroit 48227. Mailing: 821 Barclay Dr Troy 48085. Email: crumpver@msu.edu. (5) Hall Signing Agency Inc (802554906, filed 11/16/2020, Dissolved). Notary signing. (6) Valor Veterans Services LLC (900089962, filed 09/09/2025, Active). 19327 W Chicago Detroit 48228.'
WHERE id = 'hall-verkeydia';

-- Create if not exists
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('hall-verkeydia', 'Verkeydia Crump Hall', 'person',
    'Attorney. Maiden name CRUMP (MSU email crumpver@msu.edu). Filed PPO against Kevin. Home: 38190 Tralee Trl, Northville MI 48167. Entities: Verkeydia Hall Law PLLC, Crump Hall Enterprises, Crump Hall Property & Investments, Crump Properties & Investments, Hall Signing Agency, Valor Veterans Services. Email: vhall@chojlf.com.');

--------------------------------------------------------------
-- CRUMP FAMILY CONNECTION
--------------------------------------------------------------

-- Verkeydia CRUMP Hall: crumpver@msu.edu, entities named "Crump Hall..."
-- Jehan CRUMP-Gibson: managing partner GLLG
-- BOTH have surname CRUMP
-- BOTH represent Banks
-- BOTH are attorneys
-- If sisters/cousins: Banks legal representation has been a family affair
-- chojlf.com domain needs investigation (Crump Hall Of Justice Law Firm?)

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('hall-verkeydia', 'crump-gibson-jehan', 'possible-family', 'inference', 'Both share surname CRUMP. Hall maiden name confirmed via crumpver@msu.edu. Both represent Banks. If related, legal team = family.', 'LARA + MSU email');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('carol-banks', 'original-eastside-slate', 'controls', 'confirmed', 'President + Agent. 4th Eastside Slate incarnation, filed 2020.', 'LARA 802434498');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('carol-banks', 'nile-group-ii', 'controls', 'confirmed', 'Agent. Pan-African entity parallel to Leach groups.', 'LARA 801454732');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('nakenge-beverly', 'original-eastside-slate', 'officer', 'confirmed', 'Treasurer. Also on Niger Group. Core Carol Banks team.', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('elcock-kiambu', 'original-eastside-slate', 'officer', 'confirmed', 'Director. Also on Niger Group. Core Carol Banks team.', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('carol-banks', 'leach-spencer', 'parallel-ops', 'inference', 'Parallel Pan-African entity naming (Niger/Nile vs Songhai/Azania/Sudanese). Both run slate orgs. Infrastructure partnership.', 'LARA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('original-eastside-slate', 'entity', 'Original Eastside Slate (Carol Banks, 2020, Active)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('nakenge-beverly', 'person', 'Beverly Nakenge (Carol Banks operative, slate+nonprofit)', 5);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('elcock-kiambu', 'person', 'Kiambu Elcock (Carol Banks operative)', 5);
