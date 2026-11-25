-- UPDATE OCT 6 BATCH 3: TransparencyUSA + Dark Money Pipeline
-- Sources: TransparencyUSA, BridgeDetroit, Metro Times, Outlier Media, Free Press

-- ========================================
-- MCCASTLE FULL COMMITTEE SPREAD — $20,410 total
-- ========================================
-- Gloria McCastle is a SHARED OPERATIVE paid by 5 committees:
-- 1. Brian Banks for Senate:           $9,450
-- 2. David Knezek for State Senate:    $5,000
-- 3. Bank on Banks for Michigan (PAC): $3,650
-- 4. Committee to Elect Tenisha Yancey: $1,310
-- 5. Gay-Dagnogo Strong Women Lead PAC: $1,000
--
-- McCastle connects Banks → Knezek → Yancey (judge) → Gay-Dagnogo
-- She is the human wire connecting the campaign finance network

-- ========================================
-- BRIAN BANKS FOR SENATE — FULL PAYEE LIST
-- ========================================
-- Now EVERY major payee is identified:
-- $39,315 — Inner Link Graphics (Larry Thomas Jr, Southfield)
-- $24,240 — Mass Mailing LLC
-- $10,500 — Custom Promotions (Jason Gordon, FBI/IRS investigated)
--  $9,450 — Gloria McCastle (shared operative)
--  $8,500 — Carles Whitlow (Harper Woods, SONG Project)
--  $8,431 — Ross Catering (Carlton Ross = Right Turn Project treas)
--  $8,000 — Brian Banks (self-pay)
--  $7,350 — VENUS COLEMAN (convicted drug money launderer, 2:91-cr-80936)
--  $6,875 — Outfront Media
--  $6,675 — Latania Lewis (Central City Health)
--
-- A convicted drug money launderer received $7,350 from a candidate's
-- Senate campaign. Venus Coleman laundered drug money for the Karl
-- Wingo drug ring (cocaine + heroin distribution), was convicted by
-- jury, and affirmed by the 6th Circuit. She now appears as a payee
-- on a Michigan political campaign.

-- ========================================
-- DARK MONEY PIPELINE: 5PLUS1 → DETROIT NEXT → SHEFFIELD
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('5plus1', '5Plus1', 'entity', 3,
 '501(c)(4) social welfare nonprofit — DARK MONEY vehicle. Formed by Scott Holiday. Operates from same address as DABO (Detroit Association of Black Organizations) at 12048 Grand River Ave, Detroit. Advised by Rev. Horace Sheffield III (Sheffield''s father). Provided $151,000 (44% of total) to Detroit Next PAC before Sheffield''s 2025 mayoral primary. Does NOT disclose donors. Source: BridgeDetroit.');

INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('detroit-next-pac', 'Detroit Next PAC', 'entity', 3,
 'Political action committee formed Dec 2024, two weeks before Sheffield announced candidacy. Treasurer: Amy Gray. Raised $909K, spent ~$900K in 2025-2026. Major donors: 5Plus1 ($151K), Save Detroit Jobs ($84,500), Michigan Energy First/$50K (DTE-linked), Michigan Vindicated ($45K), Matthew Moroun ($44K), Health Alliance Plan PAC ($20K), Arn Tellem/Pistons ($10K). Spent $212,600+ on Sheffield primary ads — billboards, mailers, digital. In 2026, pivoted to support 6 state legislative candidates including Korey Hall ($54K) and Justin Onwenu ($20K). Source: BridgeDetroit, Metro Times, Outlier Media.');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('5plus1', 'detroit-next-pac', 'funding', 151000,
 '$151,000 — 44% of Detroit Next funding before Sheffield primary. BridgeDetroit.', 'RECORD');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('sdj', 'detroit-next-pac', 'funding', 84500,
 '$84,500 from Save Detroit Jobs to Detroit Next PAC. Same Dykema-formed entity that funded Johnson vs Elrick. Now also funded Sheffield.', 'RECORD');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('detroit-next-pac', 'sheffield', 'funding', 212600,
 '$212,600+ on pro-Sheffield ads (billboards, mailers, digital) before Aug 2025 primary.', 'RECORD');

-- THE CHAIN:
-- Dykema formed Save Detroit Jobs (Entity 802002459)
-- → Save Detroit Jobs funded Johnson's campaign vs Elrick (2021)
-- → Johnson now sits on PCA Board with Judge Miller
-- → Save Detroit Jobs gave $84,500 to Detroit Next PAC
-- → Detroit Next PAC funded Sheffield's mayoral campaign
-- → Sheffield is now MAYOR
-- → Sheffield's father Horace Sheffield III advises 5Plus1
-- → 5Plus1 gave $151,000 to Detroit Next PAC
-- → Same pipeline, same dark money, same network

-- ========================================
-- HORACE SHEFFIELD III — UPDATED
-- ========================================
UPDATE nodes SET description =
'Rev. Horace L. Sheffield III. CEO of DABO (Detroit Association of Black Organizations), 12048 Grand River Ave, Detroit. Senior Pastor, New Destiny Christian Fellowship. President, Michigan Chapter National Action Network. Chair, Detroit Ecumenical Ministers Alliance. Host, "The Wake-Up Call" on FaithTalk 101.5 FM. Father of Mayor Mary Sheffield. Adviser to 5Plus1 (dark money 501c4, $151K to Detroit Next PAC). Sheffield father listed as incorporator of 5Plus1 on TV ad order — name removed after BridgeDetroit contacted him. 5Plus1 and Detroit Next PAC both operated from DABO headquarters. Detroit Next PAC paid $15K to Ecumenical Ministers Alliance (Sheffield = chair). In 2024, El-Sayed campaign paid Ecumenical Ministers Alliance $75K (10 x $7,500) as "political consulting" while Sheffield endorsed El-Sayed on radio without disclosing payments. Sources: BridgeDetroit, Free Press/Elrick, Todd K. Marsha.'
WHERE id = 'sheffield';

-- Note: the Sheffield node may need to be split — Horace III vs Mary
-- For now, updated the existing Sheffield entry

-- ========================================
-- SAVE DETROIT JOBS → DUAL USE CONFIRMED
-- ========================================
-- Previously documented:
--   Save Detroit Jobs funded Latisha Johnson vs Steve Elrick (2021)
--   Johnson → PCA Board Secretary
-- NOW documented:
--   Save Detroit Jobs gave $84,500 to Detroit Next PAC (2025)
--   Detroit Next PAC → Sheffield mayoral campaign
--   Sheffield won → now Mayor
--
-- SAME DYKEMA-FORMED ENTITY funds BOTH:
--   1. The council member who sits on Banks's school board
--   2. The Mayor of Detroit
-- And the entity's officers ALL shared the same registered address
-- (13560 E. McNichols — shell nonprofit confirmed)

-- ========================================
-- CELIA WASHINGTON — ENRICHED
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('washington-celia', 'Celia Washington', 'actor', 4,
 'Former DPD Deputy Chief of Police and legal adviser to Chief of Police. Oversaw towing permits, licensing, and rotations. Pled guilty Jan 2018 to bribery conspiracy with Gasper Fiore. Sentenced Apr 2018: 12 months + $2,500 fine + 2 years supervision. Accepted $4,000 cash from Fiore + $800 birthday bar tab at Granite City + car arrangement + free oil changes from another tower. Met Fiore privately at Coldstone and bars. Gave Fiore personal email to avoid detection. Beeckman wrote she was "attempting to steer work to Fiore" and "find ways to work around a system." Her attorney Arnold Reed filed the suppression motion that accidentally unsealed the full 18-target wiretap list. Middle name "Banks" — no confirmed blood relation to Brian Banks. Detroit OIG Case #18-0008-INV (Nov 2, 2018) documents Boulevard & Trumbull investigation.');

-- ========================================
-- PAUL OTT — ENRICHED
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('ott-paul', 'Paul Ott', 'actor', 5,
 'Owner of Gene''s Towing Inc and City Wide Towing Inc. Companies alleged by Detroit OIG to be fronts for Fiore. Debarred 7 years (May 2018 - May 2025). Sued Detroit with Joan Fiore: Fiore v. City of Detroit (2:19-cv-10853, E.D. Mich.) — claimed city improperly used wiretap affidavit for debarment. Dismissed by court. 6th Circuit affirmed: "rooting out corruption, or the appearance of corruption" justified city action. Not federally charged.');

-- ========================================
-- SHANE ANDERS — KEY NODE (COOPERATOR + AREA TOWING)
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('anders-shane', 'Shane Anders', 'actor', 4,
 'Owner of Star Towing (Monroe) and Area Towing & Recovery (Taylor). FBI COOPERATOR — NOT corrupt. Told FBI that Mayor Sollars forced him to use Fiore for heavy tows in Taylor. FBI cleared him as not a target (Mar 8, 2018, letter from USAO). His cooperation led to FBI raid on Sollars (Feb 19, 2019). Filed whistleblower lawsuit: Area Towing v. City of Taylor et al. (2:19-cv-10989, E.D. Mich., Judge Linda V. Parker). THIS IS THE SAME CIVIL CASE that produced FBI wiretap files containing Banks recorded conversations (produced in discovery Sep 2025). Anders is the reason we have the Banks wiretap evidence in a civil case file. Source: Detroit News, ClickOnDetroit, 6th Circuit No. 20-2234, Free Press.');

-- ========================================
-- JESSICA LUCAS — FIORE DAUGHTER
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('lucas-jessica', 'Jessica Lucas', 'actor', 5,
 'Daughter of Gasper and Joan Fiore. Owned 20% of Boulevard & Trumbull Towing. Ran B&T day-to-day operations including DPD tow rotations. "In the office every day." Debarred 10 years (May 2018 - May 2028). Detroit OIG found she either knew about Fiore corruption or "provided no meaningful oversight." Michael Irvin Lucas (wiretap target #16) likely her husband/partner. Source: Detroit OIG Case #18-0008-INV.');

-- ========================================
-- LOUAY HUSSEIN — TOWING DONOR
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('hussein-louay', 'Louay Malakey Hussein', 'actor', 5,
 'Manager of Nationwide Towing Inc (owned by brother Hussein "Sam" Hussein). Employer: Mayflower Enterprises, President of Operations. Northville MI 48167. $272,750 in political contributions (TransparencyUSA): $68K Northville Leadership Fund, $42K Leadership Matters PAC, $40K MI Leaders of Tomorrow, $30K Alex Garza for Governor, $16.6K Aric Nesbitt for Governor, $8.3K each to Edevbie/Gilchrist/Benson/Cox for Governor, $6.6K Schuette, $1.2K Rylee Linting. Brother''s MetroTech Collision also connected. Nationwide subject of Detroit OIG investigation (opened Mar 2018) for "hunting" stolen vehicles, above-market rates, cash-only redemption, driver cash incentives. Not criminally convicted. Bipartisan mega-donor in towing industry.');

-- ========================================
-- MORRIS JOSEPH — EX-DPD
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('joseph-morris', 'Morris Joseph', 'actor', 5,
 'Former Detroit Police officer. Wiretap target #9. Involved in DPD towing operations. Named in Anjorin v. City of Detroit (2:16-cv-10893) for directing Boulevard & Trumbull Towing to tow vehicles from resident property. Metro Times: "ex-Detroit cop Morris Joseph." Not federally charged. His role in the DPD towing ecosystem connects him to the Fiore/Washington bribery network.');
