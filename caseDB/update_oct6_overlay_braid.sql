-- ============================================================
-- OCT 6, 2026 — NETWORK OVERLAY BRAID
-- Bettison ↔ Sheffield ↔ Save Detroit Jobs ↔ Banks pipeline
-- Dark money connections, structural parallels, DPD towing overlay
-- ============================================================

-- ============================================================
-- DARK MONEY PIPELINE: Save Detroit Jobs → Two Endpoints
-- ============================================================

INSERT INTO nodes (name, type, role, status, notes) VALUES
('Save Detroit Jobs', 'entity', 'dark money vehicle', 'active',
 'LARA Entity 802002459. Formed by Dykema Gossett PLLC. Also operated as Impact Detroit (2018) and Detroit Leaders (2021). All 3 officers at 13560 E. McNichols. Funded Johnson 2021 campaign AND gave $84,500 to Detroit Next PAC for Sheffield. Dual-use entity connecting PCA Board to Mayor.'),

('Detroit Next PAC', 'entity', 'political action committee', 'active',
 'Received: $84,500 from Save Detroit Jobs, $151,000 from 5Plus1, $50,000 from Michigan Energy First (DTE-linked), $45,000 from Michigan Vindicated (dark money), $44,000 from Matthew Moroun, $20,000 from Health Alliance Plan PAC. Spent $212,600+ on pro-Sheffield ads. Total haul well over $400K.'),

('5Plus1', 'entity', '501(c)(4) dark money', 'active',
 'Formed by Scott Holiday. Operated from DABO address (12048 Grand River). Advised by Rev. Horace Sheffield III (mayor father). 44% of Detroit Next PAC total funding. $151,000 direct. $15,000 to Ecumenical Ministers Alliance (Sheffield III = chair). Father funding daughter through dark money.'),

('Michigan Energy First', 'entity', 'dark money PAC', 'active',
 'DTE-linked entity. Gave $50,000 to Detroit Next PAC. DTE = Detroit major utility.'),

('Michigan Vindicated', 'entity', 'dark money', 'active',
 'Gave $45,000 to Detroit Next PAC. Dark money - donors not disclosed.'),

('Matthew Moroun', 'person', 'Ambassador Bridge heir', 'active',
 'Gave $44,000 to Detroit Next PAC. Moroun family controls Ambassador Bridge, CenTra Inc. Major Detroit real estate.'),

('Health Alliance Plan PAC', 'entity', 'health insurer PAC', 'active',
 'Gave $20,000 to Detroit Next PAC. HAP = Henry Ford Health System affiliate.');

-- ============================================================
-- EDGES: Dark Money Pipeline
-- ============================================================

INSERT INTO edges (source, target, relationship, weight, notes) VALUES
('Dykema Gossett PLLC', 'Save Detroit Jobs', 'formed entity', 9,
 'Dykema formed Entity 802002459. Entity email: compliance@dykema.com. Corporate formation.'),

('Save Detroit Jobs', 'Latisha Johnson', 'funded campaign (2021)', 8,
 'Operated as "Detroit Leaders" in 2021. Funded Johnson vs Steve Elrick. Johnson won District 2 council seat.'),

('Save Detroit Jobs', 'Detroit Next PAC', 'donated $84,500', 9,
 '2025 contribution. Direct pipeline from Dykema dark money vehicle to pro-Sheffield PAC.'),

('5Plus1', 'Detroit Next PAC', 'donated $151,000', 9,
 '44% of Detroit Next PAC total. Father (Sheffield III) advised 5Plus1. Father funding daughter. Dark money.'),

('Michigan Energy First', 'Detroit Next PAC', 'donated $50,000', 7,
 'DTE-linked. Utility money in mayoral dark money pipeline.'),

('Michigan Vindicated', 'Detroit Next PAC', 'donated $45,000', 7,
 'Dark money. Donors undisclosed.'),

('Matthew Moroun', 'Detroit Next PAC', 'donated $44,000', 7,
 'Ambassador Bridge family. Major Detroit real estate.'),

('Health Alliance Plan PAC', 'Detroit Next PAC', 'donated $20,000', 6,
 'Henry Ford Health System affiliate.'),

('Detroit Next PAC', 'Mary Sheffield', 'spent $212,600+ on ads', 10,
 'Billboards, mailers, digital advertising. Sheffield won mayoral primary and general.'),

('Mary Sheffield', 'Todd Bettison', 'appointed as Chief', 10,
 'Jan 2026. Retained Bettison (27-yr DPD) as Police Chief. Bettison later used DPD to protect Sheffield personal reputation.'),

('Latisha Johnson', 'PCA Board', 'serves as Secretary', 9,
 'Same entity (Save Detroit Jobs/Detroit Leaders) that funded her campaign also funded the Mayor. Johnson on convicted felon Banks school board.'),

('Todd Bettison', 'DPSA Board', 'serves as Secretary', 8,
 'Using official city email (bettisont239@detroitmi.gov) for charter school board. Structural parallel to Miller/PCA.'),

('Horace Sheffield III', '5Plus1', 'advisor/incorporator', 9,
 'Father of Mayor Sheffield. Name was on TV ad order, removed after BridgeDetroit contacted him. Chair of Ecumenical Ministers Alliance ($15K from Detroit Next PAC).'),

('Horace Sheffield III', 'Mary Sheffield', 'father-daughter', 10,
 'Father used 5Plus1 to funnel $151K to Detroit Next PAC supporting daughter mayoral campaign.'),

('Detroit Next PAC', 'Ecumenical Ministers Alliance', 'paid $15,000', 7,
 'Sheffield III = chair of EMA. PAC paying father org while supporting daughter campaign.');

-- ============================================================
-- STRUCTURAL PARALLEL: Miller/PCA = Bettison/DPSA
-- ============================================================

INSERT INTO edges (source, target, relationship, weight, notes) VALUES
('Cylenthia Miller', 'Todd Bettison', 'structural parallel', 8,
 'Both public officials on charter school boards. Miller = 3rd Circuit judge + PCA Board President. Bettison = Police Chief + DPSA Board Secretary. Both use official resources for board. Both under investigation (Miller: AGC+JTC, Bettison: OIG+FBI).'),

('Todd Bettison', 'Jahdante Smith', 'called to suppress photos', 8,
 'Aug 5 2026. 24-min recorded call asking Smith to remove Sheffield ex-boyfriend photos. City community relations also called. DPD later detained Smith, seized phone under warrant. OIG opened investigation Sep 16.'),

('Todd Bettison', 'Detroit OIG', 'under investigation', 9,
 'Sep 16 2026. Investigating use of DPD resources to protect Mayor personal reputation. FBI took over "public corruption side." Bettison says call was "personal."');

-- ============================================================
-- DPD TOWING OVERLAY — Same department, same period
-- ============================================================

INSERT INTO edges (source, target, relationship, weight, notes) VALUES
('Todd Bettison', 'Celia Washington', 'same department', 7,
 'Bettison 27yr DPD career. Washington was Deputy Chief/legal adviser. She was bribed by Fiore for towing rotations 2016-2017, convicted 2018. Bettison was in DPD during this period.'),

('Todd Bettison', 'John Kennedy', 'same department', 7,
 'Kennedy was Integrity Unit supervisor — literally in charge of investigating police misconduct. Was accepting towing bribes 2018-2021. Bettison was DPD during this period.'),

('Todd Bettison', 'Operation Northern Hook', 'chief during aftermath', 7,
 'Northern Hook (2021-2022) prosecuted 5+ DPD officers for towing bribes. Bettison left DPD for Deputy Mayor 2021 but returned as Chief Jan 2026. Now leads same department where systemic towing corruption was proven.');

-- ============================================================
-- McCAST  LE SPREAD — 5 committees one operative
-- ============================================================

INSERT INTO edges (source, target, relationship, weight, notes) VALUES
('Gloria McCastle', 'Brian Banks', 'paid by Banks Senate campaign $9,450', 8,
 'Political operative. Banks for Senate primary payee.'),

('Gloria McCastle', 'Bank on Banks for Michigan', 'paid $3,650', 7,
 'Banks PAC also using same operative.'),

('Gloria McCastle', 'Tenisha Yancey', 'paid $1,310 by Yancey committee', 7,
 'Yancey = 36th District Court judge, MacDowell Board Chair. Same operative.'),

('Gloria McCastle', 'Sherry Gay-Dagnogo', 'paid $1,000 by Strong Women Lead PAC', 7,
 'Gay-Dagnogo = former DPSCD board → City Ombudsman. Same operative.'),

('Gloria McCastle', 'David Knezek', 'paid $5,000 by Knezek committee', 6,
 'State Senate ally. Same operative network.');

-- ============================================================
-- BANKS SENATE FULL PAYEES — All major recipients identified
-- ============================================================

INSERT INTO nodes (name, type, role, status, notes) VALUES
('Inner Link Graphics', 'entity', 'Banks Senate vendor', 'identified',
 'Larry Thomas Jr, Southfield. LARA 801470477. $39,315 from Banks for Senate. Highest payee.'),

('Mass Mailing LLC', 'entity', 'Banks Senate vendor', 'identified',
 '$24,240 from Banks for Senate. Bulk mail services.'),

('Custom Promotions', 'entity', 'Banks Senate vendor', 'identified',
 'Jason Gordon. $10,500 from Banks for Senate. Gordon = FBI/IRS/DoL investigated for UAW bribery scheme.'),

('Ross Catering', 'entity', 'Banks Senate vendor', 'identified',
 'Carlton Ross = Right Turn Project treasurer. $8,431 from Banks for Senate.'),

('Outfront Media', 'entity', 'billboard vendor', 'identified',
 '$6,875 from Banks for Senate. Billboard advertising.'),

('Latania Lewis', 'person', 'Banks associate', 'identified',
 'Central City Health. $6,675 from Banks for Senate.');

INSERT INTO edges (source, target, relationship, weight, notes) VALUES
('Brian Banks', 'Inner Link Graphics', 'paid $39,315 (highest payee)', 8,
 'Larry Thomas Jr. Southfield. Print/graphics for Senate campaign.'),
('Brian Banks', 'Mass Mailing LLC', 'paid $24,240', 7,
 'Bulk mailing services.'),
('Brian Banks', 'Custom Promotions', 'paid $10,500', 8,
 'Jason Gordon. FBI/IRS/DoL investigated - UAW bribery.'),
('Brian Banks', 'Gloria McCastle', 'paid $9,450', 8,
 'Political operative spanning 5 committees.'),
('Brian Banks', 'Carles Whitlow', 'paid $8,500', 7,
 'Harper Woods. SONG Project nonprofit.'),
('Brian Banks', 'Ross Catering', 'paid $8,431', 7,
 'Carlton Ross = Right Turn Project treasurer.'),
('Brian Banks', 'Venus Coleman', 'paid $7,350', 9,
 'CONVICTED drug money launderer. Cocaine/heroin ring (2:91-cr-80936). Senate campaign paying a federal drug convict.'),
('Brian Banks', 'Outfront Media', 'paid $6,875', 6,
 'Billboard advertising.'),
('Brian Banks', 'Latania Lewis', 'paid $6,675', 6,
 'Central City Health. Campaign payee.');

-- ============================================================
-- NETWORK OVERLAY SUMMARY
-- ============================================================
-- TWO NETWORKS, ONE PIPELINE:
--
-- NETWORK A: Education Extraction
--   Banks → PCA (charter school) → public $ via per-pupil
--   Board: Miller (judge), Moreland (AAG), Johnson (council)
--   Protected by: lack of authorizer oversight, judicial immunity
--
-- NETWORK B: Enforcement Weaponization
--   Sheffield → Bettison → DPD → suppress dissent + towing $
--   Board: Bettison on DPSA (charter) while serving as Chief
--   Protected by: DPD chain of command, mayoral appointment power
--
-- CONNECTION: Same dark money pipeline
--   Save Detroit Jobs (Dykema) → funded Johnson (Network A)
--   Save Detroit Jobs (Dykema) → funded Sheffield via Detroit Next (Network B)
--   5Plus1 (Sheffield father) → Detroit Next → Sheffield → Bettison
--   McCastle spans both (Banks + Gay-Dagnogo + Yancey)
--
-- SAME PATTERN:
--   Official on school board while exercising public authority
--   Miller/PCA = Bettison/DPSA
--   Both under investigation (Oct 2026)
--
-- The data is in git. Clone it. Verify it. Every source is cited.
-- ============================================================
