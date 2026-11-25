-- caseDB update: Oct 4, 2026 (Sheffield/Bettison Circle — Power Mapping)
-- Source: LARA API + web OSINT (Crain's Detroit, BridgeDetroit, Free Press, Outlier)
--
-- SHEFFIELD ADMINISTRATION:
--   Deputy Mayor: Brian White (longtime COS, 10+ years)
--   Chief of Staff: David Bowser (ex-Duggan admin, Housing/Revitalization)
--   CFO: Tanya Stoudemire (30-year city veteran, continued from Duggan)
--   Corporation Counsel: Conrad Mallett Jr (Duggan ally, former deputy mayor)
--   Planning Director: Alexa Bush (continued from Duggan)
--   Housing Director: Julie Schneider (continued from Duggan)
--   Transition Chair: Melvin "Butch" Hollowell (Miller Law, former Duggan city atty)
--
-- KEY FINDING: Most cabinet is CONTINUITY from Duggan admin.
--   Sheffield didn't replace the machine — she inherited it.
--
-- SHEFFIELD DARK MONEY:
--   5Plus1 nonprofit → Detroit Next PAC → Sheffield campaign
--   5Plus1 advised by Rev. Horace Sheffield III (her FATHER)
--   $342,850 raised before primary. Secret donors.
--   Anthony Soave (Kwame Kilpatrick associate) gave $20K via Citizens for MI
--
-- Run: sqlite3 caseDB.sqlite < update_oct4_sheffield_bettison.sql

--------------------------------------------------------------
-- SHEFFIELD POWER CIRCLE
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('sheffield-mary', 'Mary Sheffield', 'person',
    'Detroit Mayor (Jan 2026-). Former City Council President. Granddaughter of labor leader Horace Sheffield Jr. LARA entities: Divine Touch Development LLC (802317160, filed 04/30/2019, Active — 1995 Hyde Park Detroit 48207, email msheffield4@gmail.com — development company filed while on Council); Full Potential LLC (801653825, dissolved 2012, 3320 Spinnaker Ln Detroit). Campaign raised $2.8M+. Dark money: Detroit Next PAC ($342K+) funded by 5Plus1 nonprofit advised by her father Horace Sheffield III. Max donors: Moroun family, Roger Penske, DTE CEO, Torgow family ($25K combined), Pistons Arn Tellem ($43K combined). Todd Flood gave max donation. Under OIG investigation re: Bettison/Smith phone controversy.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('white-brian-dm', 'Brian White (Deputy Mayor)', 'person',
    'Detroit Deputy Mayor (Jan 2026-). Sheffield''s COS for 10+ years from City Council days. Oversees state/federal policy, labor, regional partnerships, city operations. LARA: multiple entities under common name — not confirmed which are his.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('bowser-david', 'David Bowser (Chief of Staff)', 'person',
    'Detroit COS (Jan 2026-). From Duggan admin (Housing Deputy Director, Community Health Corps, Human Services). Rise Higher Detroit transition ops director. LARA: 12 Cats LLC, Bowser''s Services, BowserBytes (all dissolved), Blue Mountain Services LLC (900250718, filed 07/22/2026, Active).');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('mallett-conrad', 'Conrad Mallett Jr (Corporation Counsel)', 'person',
    'Detroit Corporation Counsel (city attorney). Longtime Duggan ally. Former DMC Sinai-Grace Hospital president. Former Duggan Deputy Mayor. LARA: ABK Development LLC (801199132, filed 2002, Active, 607 Shelby St Ste 200 Detroit). Confirmed by Council to continue under Sheffield.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('hollowell-melvin', 'Melvin "Butch" Hollowell', 'person',
    'Sheffield transition chair. Managing partner at Miller Law firm. Former city attorney under Duggan. Bridges Duggan→Sheffield continuity.');

--------------------------------------------------------------
-- HORACE SHEFFIELD III — MAYOR'S FATHER
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('sheffield-horace', 'Rev. Horace Sheffield III', 'person',
    'Mary Sheffield''s FATHER. Prominent Detroit pastor/activist. Advised 5Plus1 nonprofit that funded Detroit Next PAC ($342K+ for Sheffield campaign — dark money). LARA entities (all at 12048 Grand River Ave Detroit 48204): New Destiny Christian Fellowship Inc (802003240, Ecclesiastical Corp, Active — officers: Sheffield (Pres+Sec), Jennifer Hall (Treas), Ive Edwards (Dir), Kevin Hampton (Dir), QUENTIS LEVERETT (Dir — also Sheffield campaign donor)); One Mike Media LLC (802878419, 2022, Active — email cplonka@zausmer.com = ZAUSMER law firm); One Mike Brands LLC (802850480, 2022, Active); Detroit Social Action Alliance DSAA (803362444, filed 03/24/2025, Active — nonprofit filed DURING Sheffield campaign); Lauryn''s Paper Company Inc (803384657, filed 05/05/2025, Active). Email: sheffield3@aol.com. Home: 7192 Pebble Park Dr, West Bloomfield MI 48322.');

--------------------------------------------------------------
-- DETROIT PUBLIC SAFETY ACADEMY — FULL BOARD (LARA)
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Charter school authorized by Eastern Michigan University. LARA Entity ID 800934916. Filed 09/05/2012. Active. Agent: MELINDA BENKOVSKY (melinda.benkovsky@leonagroupmw.com — LEONA GROUP, major charter school management company, 2125 University Park Dr Okemos MI 48864). BOARD: Kamal Cheeks (President, 19427 Warrington Dr Detroit), Rolanda Williams (Treasurer, 3208 Columbus Detroit), Hazel White (Director, 15472 Grandville Detroit), Ken Dettloff (Director, 452 Water Tower Circle Brighton), TODD BETTISON (Secretary + Director, 28051 Copper Creek Lane, Farmington Hills MI 48331), Charles Simms (Director, 1250 Rosa Parks Blvd Detroit). The POLICE CHIEF sits on a charter school board managed by Leona Group.'
WHERE id = 'dpsa';

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('dpsa', 'Detroit Public Safety Academy', 'org',
    'Charter school. LARA 800934916. Agent: Melinda Benkovsky (Leona Group). Bettison = Secretary + Director.');

--------------------------------------------------------------
-- BETTISON
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Detroit Police Chief (permanent Feb 2025, interim Nov 2024). Former Deputy Mayor (2022-2024). DPD career 1994-2021, fastest rising member. LARA: New Professionals 101 LLC (801261590, filed 01/21/2004, Active, 870 Steward Ste 407 Detroit 48202). DPSA board Secretary + Director (LARA confirmed). Home: 28051 Copper Creek Lane, Farmington Hills MI 48331 (per DPSA LARA filing). Under OIG investigation (Sep 2026) for calling activist Jahdante Smith re: Sheffield photos, then DPD seized Smith''s phone. FBI now handling. Bettison uses official email bettisont239@detroitmi.gov for DPSA board business. Bachelor''s Wayne State (Criminal Justice). Sheffield reappointed him Jan 2026.'
WHERE id = 'bettison-todd';

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('bettison-todd', 'Todd Bettison', 'person',
    'Detroit Police Chief. DPSA board Secretary. Under OIG investigation. LARA: New Professionals 101 LLC.');

--------------------------------------------------------------
-- STALLWORTH
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('stallworth-thomas', 'Thomas F. Stallworth III', 'person',
    'Former MI State Representative. Married to Nicole Wells Stallworth (MacDowell Board Chair). LARA: Stallworth Consulting Group LLC (801840092, filed 10/06/2015, Active, 19793 Sorrento Detroit 48235). Together with Nicole, donated $1,250 to Banks 2022 campaign. Defended Banks at 2016 felony rally: "miscarriage of justice."');

--------------------------------------------------------------
-- SHEFFIELD CAMPAIGN DONOR CONNECTIONS
--------------------------------------------------------------

-- Todd Flood: Max donor to Sheffield. Attorney (Flood Law PLLC, 801888628).
--   155 W Congress Suite 350 Detroit. Email: tflood@floodlaw.com.
--   Also SMBD Consulting LLC (803364597, filed 03/27/2025).
-- Anthony Soave: $20K via Citizens for Michigan PAC.
--   Kwame KILPATRICK ASSOCIATE. Soave Enterprises. Florida golf club founder.
-- Moroun family: Multiple max donations + $25K via Detroit Next PAC.
-- Torgow family: $25K combined (Huntington Bank chairman).
-- Pistons/Tellem: $43K combined. Sheffield voted for $34.5M Pistons subsidy.

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sheffield-horace', 'sheffield-mary', 'family', 'confirmed', 'Father. Advised 5Plus1 dark money PAC that funded her campaign.', 'BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bettison-todd', 'dpsa', 'board-member', 'confirmed', 'Secretary + Director on LARA filing. Home address on record.', 'LARA 800934916');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sheffield-mary', 'bettison-todd', 'appointed', 'confirmed', 'Reappointed as police chief Jan 2026. Originally appointed by Duggan.', 'Crain''s Detroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-thomas', 'stallworth-nicole', 'spouse', 'confirmed', 'Married. Together donated $1,250 to Banks. She = MacDowell board chair.', 'TransparencyUSA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('sheffield-mary', 'person', 'Mary Sheffield (Mayor, Divine Touch Dev LLC)', 1);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('sheffield-horace', 'person', 'Rev. Horace Sheffield III (father, 5Plus1 dark money)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('mallett-conrad', 'person', 'Conrad Mallett Jr (Corp Counsel, ABK Dev, Duggan ally)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('stallworth-thomas', 'person', 'Thomas Stallworth III (former state rep, Banks rally)', 3);

--------------------------------------------------------------
-- MASTER TARGET LIST: PACER + LARA FOLLOW-UP
--------------------------------------------------------------

-- PACER TARGETS (federal case search):
-- 1. Brian Banks (prior convictions, any civil)
-- 2. Joseph Holland Jr (prior convictions, bankruptcy)
-- 3. Jason Gordon / Custom Promotions (UAW case connection)
-- 4. Gasper Fiore (16-cr-20732 + Area Towing civil)
-- 5. Andre Spivey (21-cr-20490, Op Northern Hook)
-- 6. Bert Johnson (ghost employee conviction)
-- 7. Todd Perkins / Perkins Law Group (Op Northern Hook clients)
-- 8. Anthony Soave (Kilpatrick connection)
-- 9. Save Detroit Jobs / Dykema (any federal filings)
-- 10. Area Towing v. Sollars (19-cv-10989 — wiretap docs)
-- 11. Gabe Leland (federal case)
-- 12. Venus Coleman (2:91-cr-80936)
-- 13. Carol Banks (any federal case)
-- 14. Kenneth Daniels (any federal case)
-- 15. Spencer Leach (any federal case)

-- LARA FOLLOW-UP TARGETS:
-- 1. Leona Group MW (DPSA management company)
-- 2. MacDowell Preparatory Academy entity
-- 3. F.A.M.E. entities
-- 4. Zausmer law firm (Horace Sheffield's media entity attorney)
-- 5. Detroit Next PAC (state entity?)
-- 6. 5Plus1 nonprofit
-- 7. Detroit Action (Adam Holiday)
-- 8. Perkins Law Group PLLC
-- 9. Miller Law firm (Hollowell's firm)
-- 10. Scarfone & Geen P.C. (Hall's concurrent employer)

-- TRANSPARENCYUSA FOLLOW-UP:
-- 1. Sheffield campaign full donor list
-- 2. Detroit Next PAC full donor list
-- 3. Bettison campaign contributions (if any)
-- 4. Moreland campaign contributions (if any state rep races)
-- 5. Cross-reference Banks network donors with Sheffield donors
