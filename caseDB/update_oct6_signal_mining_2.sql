-- UPDATE OCT 6 BATCH 2: Deep mining results
-- FULL WIRETAP TARGET LIST + Reynolds + Casab + Norman Shy + EAA timeline
-- Sources: MLive, WXYZ, Detroit News, Free Press, AP, CourtListener, 6th Circuit

-- ========================================
-- FULL BEECKMAN WIRETAP TARGET LIST (18 names)
-- Source: WXYZ + MLive (accidentally unsealed court records, Dec 2017)
-- Celia Washington's attorney included the wiretap application
-- in a motion to suppress evidence
-- ========================================

-- The complete list of "Target Subjects" from FBI Special Agent
-- Robert Beeckman's wiretap request:

-- 1.  Gasper Fiore              ✅ Convicted (16-cr-20732)
-- 2.  Romel Casab               ✅ NOW IDENTIFIED — former Packard Plant owner
-- 3.  Paul Ott                  NEW — unknown role
-- 4.  Shane Anders              NEW — unknown role
-- 5.  Gabriel Leland            ✅ Convicted (state plea, bribery)
-- 6.  Vonda Evans               ✅ Known (retired 3rd Circuit judge, JTC suspended)
-- 7.  William Wild              ✅ NOW IDENTIFIED — towing/auto salvage operator
--                               (was listed as "Lee Wild" in our notes — full name
--                                is Billy Lee Wild / William Wild)
-- 8.  Alberta Tinsley-Talabi    ✅ Known (retired state rep, aka Jewel Ware)
-- 9.  Morris Joseph             NEW — unknown role
-- 10. Benny Napoleon            ✅ Known (Wayne County Sheriff)
-- 11. Jennifer Marie Fiore      NEW — Gasper's daughter, dated CM Gabe Leland
-- 12. Brian Roderick Banks      ✅ Primary subject
-- 13. Michael Patrick Gorman    NEW — unknown role
-- 14. Assad Ibrihim Turfe       ✅ Known (Warren Evans connection)
-- 15. Louay Malakey Hussein     NEW — unknown role
-- 16. Michael Irvin Lucas       NEW — unknown role
-- 17. Celia Banks Washington    ✅ DPD official, charged with 2 counts
-- 18. Robert Ray Nicholson      NEW — unknown role

-- Beeckman's affidavit stated:
-- "Evidence has been gathered showing that crimes involving corruption
--  have been committed by some of the target subjects, including
--  Tinsley-Talabi, Napoleon and (Romel Casab, former owner of the
--  Packard Plant in Detroit). However, those investigations have been
--  pending for months or years and the evidence so far has not been
--  sufficient to bring federal charges."

-- ========================================
-- ROMEL CASAB — IDENTIFIED ("Casab" from prior notes)
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('casab-romel', 'Romel Casab', 'actor', 5,
 'Former owner of the Packard Plant in Detroit. Named as wiretap target subject #2 in Beeckman affidavit (FBI corruption investigation). Separately indicted Jan 2016 for marijuana distribution, maintaining a drug facility at 29100 Northline Rd Romulus, and firearms charges. Facility contained 40+ kg marijuana, 374 plants, growing equipment. Collected $20K rent from growers. Convicted felon. Also filed Kassab v. Detroit (2:22-cv-12307, E.D. Mich.) re: marijuana licensing. The "Casab" unknown from our prior notes — NOW IDENTIFIED.');

-- ========================================
-- DEAN REYNOLDS — IDENTIFIED (17yr sentence)
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('reynolds-dean', 'Dean Reynolds', 'actor', 3,
 'Former Clinton Township trustee (Macomb County). Convicted June 21 2018 by jury of ALL 14 counts: bribery + bribery conspiracy. Sentenced Feb 6 2019: 204 months (17 years) by U.S. District Judge Robert Cleland, Port Huron. $15,000 fine. 6th Circuit affirmed (No. 19-1146, May 7 2020). FOUR separate bribery schemes: (1) Chuck Rizzo — $16M garbage-hauling contract, (2) Paulin Modi / Giffels Webster Engineering — $500K/yr engineering contract, (3) GASPER FIORE — towing contract, (4) Brett Harris / New Haven garbage contract. Took $150K+ in bribes including $50K in free legal services for his divorce + all-expenses Disney trip. ONLY person to stand trial in the Macomb corruption probe. 17th conviction in the probe. Longest corruption sentence in Metro Detroit except Kwame Kilpatrick (28 years).');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('reynolds-dean', 'fiore', 'bribery', 10,
 'Reynolds took bribes from Fiore for Clinton Township towing contract. Convicted on towing-related bribery count. Fiore also on wiretap with Banks.', 'RECORD');

-- ========================================
-- NEW WIRETAP TARGET NODES
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('fiore-jennifer', 'Jennifer Marie Fiore', 'actor', 5,
 'Daughter of Gasper Fiore (convicted bribery). Wiretap target #11. WXYZ/Fox 2 reported she was DATING Detroit City Councilman Gabe Leland, who voted for Fiore towing contracts while in a relationship with Fiore daughter. Leland later convicted of bribery (state plea).');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('fiore-jennifer', 'fiore', 'family', 10, 'Daughter of Gasper Fiore.', 'RECORD');
INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('fiore-jennifer', 'leland', 'romantic', 5,
 'Fox 2 reported Leland was dating Jennifer Fiore while voting for Fiore towing contracts.', 'JOURNALISM');

INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('washington-celia', 'Celia Banks Washington', 'actor', 5,
 'Detroit Police Department official. Wiretap target #17. Charged with 2 counts in the Fiore corruption case. Her attorney filed the motion to suppress wiretap evidence that accidentally exposed the full target list. Surname "Banks Washington" — relation to Brian Banks or Carol Banks TBD.');

INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('ott-paul', 'Paul Ott', 'actor', 6, 'Wiretap target #3. Role unknown. Identity TBD.');
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('anders-shane', 'Shane Anders', 'actor', 6, 'Wiretap target #4. Role unknown. Identity TBD.');
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('joseph-morris', 'Morris Joseph', 'actor', 6, 'Wiretap target #9. Role unknown. Identity TBD.');
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('gorman-michael', 'Michael Patrick Gorman', 'actor', 6, 'Wiretap target #13. Role unknown. Identity TBD.');
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('hussein-louay', 'Louay Malakey Hussein', 'actor', 6, 'Wiretap target #15. Role unknown. Identity TBD.');
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('lucas-michael', 'Michael Irvin Lucas', 'actor', 6, 'Wiretap target #16. Role unknown. Identity TBD.');
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('nicholson-robert', 'Robert Ray Nicholson', 'actor', 6, 'Wiretap target #18. Role unknown. Identity TBD.');

-- ========================================
-- NORMAN SHY — SENTENCE RESOLVED
-- ========================================
UPDATE nodes SET description = 
'Owner of Allstate Sales / World Wide Sales / Ronan Enterprises / R.S. Associates (Franklin MI). DPS approved vendor. Pled guilty May 11 2016 to conspiracy to commit federal program bribery + tax evasion. Sentenced Sep 6 2016: 5 years prison + 2 years supervised release + $2.7M restitution to DPS + $51,667 back taxes. Judge Victoria Roberts. Paid $908,500 in kickbacks to 12 principals + asst superintendent Clara Flowers over 13 years (2002-2015). $2.7M in fraudulent invoices for undelivered school supplies. Kept a LEDGER tracking kickback payments. Lived in $2.4M Farmington Hills mansion. Judge noted: "as many as 22 still uncharged current or former principals were part of this fraud." AUSAs: J. Michael Buckley + Frances Lee Carlson (SAME prosecutors as Bert Johnson case).'
WHERE id = 'shy-norman';

-- ========================================
-- CLARA FLOWERS — NEW NODE (DPS asst supt)
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('flowers-clara', 'Clara Flowers', 'actor', 4,
 'Former DPS assistant superintendent of specialized student services. Former principal of Henderson Academy. Age 61 at sentencing. Received nearly $325,000 in kickbacks from Norman Shy in the form of gift cards, money, and a new roof and gutters. Sentenced to 3 years prison (Sep 2016, Judge Victoria Roberts). The highest individual kickback recipient in the DPS principal corruption case. Promoted to assistant superintendent WHILE receiving kickbacks.');

-- ========================================
-- WILLIAM WILD — UPDATE (was "Lee Wild")
-- ========================================
UPDATE nodes SET name = 'William "Bill" Wild / Billy Lee Wild',
description = 'Detroit-area towing/auto salvage operator. Wiretap target #7 (listed as "William Wild" in court records). Companies: Hi-Way Auto Equipment (Taylor MI), Bill Wild Enterprises Inc (37500 Hillcrest, Wayne MI), City Auto Storage LLC (3400 E Lafayette, Detroit), Phil''s Towing (Grayling MI), Independent Auto Wreckers of Detroit, connections to Ferrous Processing & Trading and Soave Enterprises LLC. Named in Beeckman wiretap affidavit as towing industry target — same sector as Gasper Fiore (Area Towing). Competitor or associate in towing contract bid-rigging investigation.'
WHERE id = 'wild-lee';

-- ========================================
-- EAA → DPSCD → BANKS TIMELINE
-- ========================================
-- EAA created 2011 — 15 lowest-performing Detroit schools
-- EAA corruption probe began May 2014 (FBI/USAO Barbara McQuade)
-- Wilbourn-Snapp FBI raid Nov 2014
-- Snapp + Thornton + Horton indicted Dec 2015
-- All three pled guilty Feb 2016
-- 12 DPS principals + Norman Shy charged Mar 29 2016
-- EAA dissolved June 30 2017 — schools return to DPSCD
-- Superintendent Nikolai Vitti recommends DPSCD stop authorizing charters
-- DPSCD rejects 3-year renewals for former EAA schools (May 2018)
-- Former EAA schools seek other authorizers
-- Gay-Dagnogo on DPSCD board during this period
-- DPSCD board authorizes Banks's Purpose Charter Academy (2025)
-- Gay-Dagnogo voted to authorize Banks's PCA
-- Gay-Dagnogo then moves to City Ombudsman (10yr appointment)
--
-- THE PATTERN:
-- State creates EAA to fix failing schools → EAA becomes corrupt
-- → FBI investigates → 30+ convictions → EAA dissolved
-- → Schools return to DPSCD → DPSCD debates stopping charter authorization
-- → DPSCD board member (Gay-Dagnogo) authorizes Banks's charter school
-- → Banks extracts 72.67% through self-dealing LLC
-- → Same extraction pattern, same city, same FBI field office
-- → The reform agency created to fix corruption became corrupt
-- → The agency that absorbed the corrupt reform agency then authorized
--    a new school run by a convicted felon
-- → The board member who authorized it got a 10-year city appointment
--
-- Snapp: "Payoffs were part of the education culture in Detroit."
-- 22 uncharged principals still in the system as of Sep 2016.
-- Banks's schools are now operating in this same ecosystem.

-- ========================================
-- CROSS-REFERENCE: SAME PROSECUTORS
-- ========================================
-- AUSAs J. Michael Buckley and Frances Lee Carlson prosecuted:
--   1. Glynis Thornton (EAA corruption)
--   2. Kenyetta Wilbourn-Snapp (EAA corruption)
--   3. Norman Shy (DPS vendor corruption)
--   4. Bert Johnson (ghost employee)
--
-- Same prosecutors, same geographic territory, same institutional
-- ecosystem. If the FBI ever opens a Banks investigation, these
-- are the AUSAs who know the landscape.

-- ========================================
-- REMAINING UNKNOWNS (reduced from 5 to 0 blocking + 7 new wiretap)
-- ========================================
-- ALL PRIOR BLOCKING GAPS: RESOLVED
-- Inner Link Graphics: Larry Thomas Jr ✅
-- Carles Whitlow: Carles Renard Whitlow, Harper Woods ✅
-- Casab: Romel Casab, Packard Plant owner ✅
-- Lee Wild: William/Billy Lee Wild, towing operator ✅
-- Venus Coleman: drug conspiracy conviction ✅
-- Reynolds: Dean Reynolds, 17yr, Clinton Twp ✅
-- Bert Johnson: 17-20233 ✅
-- Eric Smith: 2:24-cv-11626 + criminal ✅
-- Marrocco: Anthony Marrocco, 3 months ✅
--
-- NEW UNKNOWNS from full wiretap list (Tier 6 — enrichment):
-- Paul Ott, Shane Anders, Morris Joseph, Michael Gorman,
-- Louay Malakey Hussein, Michael Irvin Lucas, Robert Ray Nicholson
