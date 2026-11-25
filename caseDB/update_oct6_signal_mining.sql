-- UPDATE OCT 6: Signal-driven mining sweep
-- Resolved 6 blocking gaps, 1 new thread (Thornton/EAA), 1 new node (Whitlow)
-- Source: Web OSINT, CourtListener, PACER, FEC, IRS, Free Press, Detroit News, DOJ

-- ========================================
-- 1. CARLES WHITLOW — IDENTIFIED
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('whitlow-carles', 'Carles Renard Whitlow', 'actor', 5,
 'Harper Woods, Wayne County. Born 1991. Founder of S.O.N.G. Project Headquarters (EIN 88-3445471, Clinton Township, 501c3 educational, $0 assets, IRS exempt Apr 2024). Youth performing arts nonprofit. Received $8,500 from Banks-connected campaign committees. Lives adjacent to Grosse Pointe (Banks neighborhood). S.O.N.G. Project Givebutter page lists campaign: "Purpose by Design - A Musical Stageplay Production" — word "Purpose" matches Banks entity naming pattern (Purpose Charter Academy, Purpose Foundation, Purpose Group LLC). Congressional campaign committee C00863621 is Stuart Whitlow (TX-31), NOT Carles.');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('whitlow-carles', 'banks', 'campaign_payee', 8500,
 'TransparencyUSA: $8,500 total received from Banks-connected committees', 'RECORD');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('whitlow-carles', 'pca', 'possible_connection', 1,
 'S.O.N.G. Project Givebutter lists "Purpose by Design" stageplay production — naming pattern matches Banks Purpose entities. Coincidence or connection TBD.', 'INFERENCE');

-- ========================================
-- 2. VENUS COLEMAN — RESOLVED
-- ========================================
UPDATE nodes SET description = 
'Convicted: conspiracy to distribute cocaine/heroin + money laundering. Case: US v. Coleman et al, 2:91-cr-80936 (E.D. Mich., filed Nov 12 1991, terminated Oct 31 2013). Part of Karl Wingo drug distribution ring. Laundered drug money by placing cars and house in her name to "cover" for Wingo. Jury conviction affirmed 6th Circuit: US v. Lang, 39 F.3d 1182 (1994). Judge Patrick J. Duggan presided. Later filed coram nobis motions (denied 2005, 2008). Campaign finance payee receiving funds from Banks-connected committees — a convicted drug money launderer in the political payment network.'
WHERE id = 'coleman-venus';

-- If node doesn't exist yet:
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('coleman-venus', 'Venus Coleman', 'actor', 4,
 'Convicted: conspiracy to distribute cocaine/heroin + money laundering. Case: US v. Coleman et al, 2:91-cr-80936 (E.D. Mich., filed Nov 12 1991). Part of Karl Wingo drug ring. Laundered drug money. Affirmed 6th Circuit: US v. Lang, 39 F.3d 1182 (1994). Campaign finance payee receiving funds from Banks-connected committees.');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('coleman-venus', 'banks', 'campaign_payee', 1,
 'TransparencyUSA payee from Banks-connected committees. Convicted drug money launderer.', 'RECORD');

-- ========================================
-- 3. BERT JOHNSON — FEDERAL DOCKET RESOLVED
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('johnson-bert', 'Bertram "Bert" Johnson Jr.', 'actor', 3,
 'Former Michigan State Senator (D-Highland Park). Federal case: US v. Bertram Johnson Jr., No. 17-20233 (E.D. Mich., Judge Matthew F. Leitman). Indicted Apr 11 2017. Pled guilty Mar 2 2018 to conspiracy to commit theft. Ghost employee scheme — put cooperating witness Glynis Thornton on Senate payroll ($23,133) to repay personal loans ($10K tuition at U of D Jesuit + $7K property taxes). Sentenced Sep 6 2018: 90 days prison + $23,133 restitution + 480 hours community service. Thornton (CW-1) secretly recorded Johnson Nov 19 2015 at FBI direction. Resigned from Senate 3 hours after guilty plea. District: NE Detroit, Highland Park, Hamtramck, Harper Woods, all 5 Grosse Pointe communities.');

UPDATE nodes SET description = 
'Former Michigan State Senator (D-Highland Park). Federal case: US v. Johnson, No. 17-20233 (E.D. Mich., Judge Leitman). Ghost employee scheme with Glynis Thornton (CW-1). 90 days prison. Thornton was FBI cooperator from EAA school corruption probe. Thornton secretly recorded Johnson. District includes Harper Woods + Grosse Pointe = Banks territory.'
WHERE id = 'johnson-bert';

-- ========================================
-- 4. ERIC SMITH — FEDERAL DOCKETS RESOLVED  
-- ========================================
-- Criminal: obstruction plea, 21 months, Judge Parker (2022)
-- Civil asset freeze: 2:24-cv-11626, Parker recused Jul 24 2024 → Behm → DeClercq
UPDATE nodes SET description = 
'Former Macomb County Prosecutor. Criminal: obstruction of justice, pled guilty Jan 2021, sentenced Feb 16 2022 to 21 months by Judge Linda V. Parker. Kickback scheme: wrote campaign fund checks to friends/subordinates who kicked money back. FBI investigation revealed cover-up. Also faces state embezzlement charges ($600K from drug/forfeiture funds, pled guilty Aug 2023 to forgery conspiracy, Judge Nanci Grant). Civil asset freeze: US v. Smith, 2:24-cv-11626 (E.D. Mich.) — Parker initially presided, RECUSED Jul 24 2024, reassigned to Behm then DeClercq. KEY: Parker saw Smith criminal case AND Area Towing 2:19-cv-10989 — one federal judge sees both sides of the corruption network.'
WHERE id = 'smith-eric';

INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('smith-eric', 'Eric Smith', 'actor', 3,
 'Former Macomb County Prosecutor. Criminal: 21 months (Judge Parker). Civil: 2:24-cv-11626. Parker recused. State: forgery conspiracy. Part of Macomb corruption probe (23+ convicted).');

-- ========================================
-- 5. ANTHONY MARROCCO — RESOLVED (was "Sam")
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('marrocco-anthony', 'Anthony Marrocco', 'actor', 3,
 'Former Macomb County Public Works Commissioner (1993-2016). Pled guilty Sep 20 2022 to attempted extortion before U.S. District Judge Robert Cleland, Port Huron. Sentenced Mar 16 2023: 3 months prison + 2 years supervised release (450 days house arrest) + $50,000 fine. Scheme: pressured developers to buy fundraiser tickets, threatened to delay/withhold county permits. Key aide Dino Bucci pled guilty 2020, died 2021. Part of Macomb County corruption probe (23+ convicted including Eric Smith).');

-- ========================================
-- 6. LEE WILD — IDENTIFIED
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('wild-lee', 'Billy Lee Wild / Bill Lee Wild', 'actor', 6,
 'Detroit-area towing/auto salvage operator. Companies: Hi-Way Auto Equipment (Taylor MI), Bill Wild Enterprises Inc (Wayne MI), City Auto Storage LLC (3400 E Lafayette, Detroit), Phil''s Towing (Grayling MI), Independent Auto Wreckers of Detroit, connections to Ferrous Processing & Trading and Soave Enterprises LLC. Named in Beeckman wiretap affidavit. Towing industry = same sector as Gasper Fiore (Area Towing) corruption investigation. Wiretap target makes sense as towing competitor/associate in bid-rigging investigation.');

-- ========================================
-- 7. GLYNIS THORNTON — NEW NODE (EAA BRIDGE)
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('thornton-glynis', 'Glynis Thornton', 'actor', 4,
 'Owner of M.A.D.E. (Making A Difference Everyday) Training & Consulting. FBI cooperator (CW-1). Pled guilty Feb 4 2016 to conspiracy to commit federal program bribery (Judge David Lawson). Paid $58,050 in kickbacks to EAA principal Kenyetta Wilbourn-Snapp for tutoring contracts at Denby and Mumford high schools. Used Paulette Horton as middleman to disguise payments. Prosecutors recommended 15 months (down from 24-30) for substantial cooperation. BRIDGE NODE: Thornton cooperated in EAA probe → led to DPS principal investigation (13 principals, Norman Shy, $908K kickbacks, $2.7M fraud) → then secretly recorded Sen. Bert Johnson Nov 19 2015 at FBI direction → leading to Johnson ghost employee indictment. Thornton is the thread connecting school vendor corruption → political corruption → Northern Hook ecosystem.');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('thornton-glynis', 'johnson-bert', 'cooperator', 10,
 'FBI CW-1. Loaned Johnson $17K. Placed on Senate payroll as ghost employee. Secretly recorded Johnson Nov 19 2015. Led to indictment.', 'RECORD');

-- ========================================
-- 8. EAA CORRUPTION PROBE — CONTEXT NODE
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('eaa-probe', 'EAA Federal Corruption Probe', 'event', 0,
 'Wide-ranging FBI/USAO investigation of Education Achievement Authority (state reform district for lowest-performing Detroit schools). Began ~May 2014. Led by USAO Barbara McQuade, FBI Detroit. Key figures: Principal Kenyetta Wilbourn-Snapp (12 months, bribery), vendor Glynis Thornton (cooperator, M.A.D.E.), contractor Paulette Horton (15 months). EAA probe → revealed DPS principal corruption (13 principals, vendor Norman Shy, $908K kickbacks over 13 years 2002-2015, $2.7M fraud). SAME FBI Detroit field office, SAME USAO that investigated Area Towing/Fiore wiretap. EAA investigation techniques (vendor subpoenas, bank records) parallel the charter school extraction patterns documented in Banks case.');

INSERT OR IGNORE INTO edges (source, target, type, weight, evidence, source_type) VALUES
('thornton-glynis', 'eaa-probe', 'defendant_cooperator', 10,
 'Pled guilty Feb 2016. Provided substantial assistance. Led to DPS principal prosecutions and Johnson indictment.', 'RECORD');

-- ========================================
-- 9. KENYETTA WILBOURN-SNAPP — NEW NODE
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('snapp-kenyetta', 'Kenyetta (KC) Wilbourn-Snapp', 'actor', 4,
 'Former principal of Mumford and Denby High Schools (EAA). Drove Maserati with GUCCI1 vanity plate. Pled guilty Feb 2016 to bribery + tax evasion. Accepted $58,050 in kickbacks from Thornton/M.A.D.E. Sentenced Jun 2016: 12 months + 1 day (Judge David Lawson). Cooperated: provided substantial assistance leading to further prosecutions. Said payoffs were "part of the education culture in Detroit." FBI raided her apartment Nov 2014. EAA probe central figure.');

-- ========================================
-- 10. NORMAN SHY — NEW NODE (DPS VENDOR)
-- ========================================
INSERT OR IGNORE INTO nodes (id, name, type, tier, description) VALUES
('shy-norman', 'Norman Shy', 'actor', 4,
 'Owner of Allstate Sales (school supplies vendor, Franklin MI). Charged Mar 29 2016 in DPS principal corruption case. Paid $908,518 in kickbacks to at least 12 DPS principals over 13 YEARS (2002-2015). $2.7M in fraudulent purchases. Schools rarely received supplies. Age 74 at time of charges. The longest-running vendor corruption scheme documented in Detroit schools. Same extraction pattern as Banks — public education money diverted to private enrichment through vendor relationships.');

-- ========================================
-- BRAIDING NOTES
-- ========================================
-- KEY STRUCTURAL FINDING: The Thornton Thread
-- 
-- Thornton (school vendor) → bribed Snapp (EAA principal) → cooperated with FBI
-- → led to DPS principal probe (13 principals, Norman Shy)
-- → secretly recorded Sen. Bert Johnson → led to Johnson indictment
-- → Johnson on Northern Hook wiretap ecosystem radar
--
-- The SAME FBI Detroit field office ran:
--   1. EAA corruption probe (school vendors/principals)
--   2. DPS principal corruption probe (Norman Shy/13 principals)
--   3. Area Towing/Fiore wiretap (towing corruption, captured Banks on phone)
--   4. Operation Northern Hook (political corruption, Spivey, Sollars)
--   5. Carol Banks FBI raid
--
-- All five investigations involve the same geographic/institutional territory:
--   Detroit schools, Detroit politics, Wayne County government
--
-- Banks operates charter schools in the EXACT ecosystem that EAA was
-- created to reform. The EAA was dissolved. Its schools returned to DPSCD.
-- DPSCD then authorized Banks's Purpose Charter Academy.
-- The school corruption that the EAA was supposed to fix is the SAME
-- corruption pattern that Banks's enterprise continues.
--
-- Snapp: "Payoffs were part of the education culture in Detroit."
-- Banks: Extracts 72.67% through a self-dealing LLC.
-- Same culture. Different mechanism. Same city. Same FBI field office.

-- REMAINING UNKNOWNS:
-- "Casab" — still completely unknown (phonetic: Kasab, Cassab, Kazab)
-- Reynolds (corruption, 17yr) — first name still unknown
