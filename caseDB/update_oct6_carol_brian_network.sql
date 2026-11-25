-- ============================================================
-- OCT 6, 2026 — CAROL BANKS ↔ BRIAN BANKS NETWORK MAP
-- No confirmed family relation. Extraordinary overlap.
-- ============================================================

-- 2012: Brian Banks beats Scott Benson by 96 votes (District 1 primary)
-- 2013: Banks takes office; Benson becomes city councilman
-- 2014: Carol Banks becomes Benson's chief of staff
-- 2016: Carol Banks receives $18K+ from Save Detroit Jobs (Dykema entity)
-- 2017: Brian Banks resigns House after plea deal, files for Senate
-- 2018: Carol Banks AND Latisha Johnson run in SAME primary (Dist 2 State Rep)
--        Carol: 15.1% (1,575), Johnson: 16.8% (1,748), Joe Tate wins 28.4%
--        Brian Banks loses Senate primary to Adam Hollier
-- 2021: Carol Banks (via Save Detroit Jobs/Detroit Leaders) backs Johnson for council
--        Johnson defeats Steve Elrick → goes on PCA Board (Brian Banks's charter school)
-- 2025: Eastside Slate (Carol Banks Vice Chair) endorses Mary Sheffield for Mayor

INSERT INTO edges (source, target, relationship, weight, notes) VALUES

-- Brian Banks beat Benson → Carol became Benson's staff
('Brian Banks', 'Scott Benson', 'defeated by 96 votes (2012 District 1 primary)', 8,
 'Brian Banks won the Democratic primary for the 1st District Michigan House by 96 votes over Scott Benson. Benson then pivoted to Detroit City Council, won 2013. Carol Banks became his chief of staff 2014. Source: Wikipedia, Daily Kos'),

-- Carol Banks + Johnson in same primary
('Carol Banks', 'Latisha Johnson', 'ran in same 2018 primary (District 2 State Rep)', 8,
 'Aug 7 2018. Carol Banks: 15.1% (1,575 votes). Johnson: 16.8% (1,748 votes). Joe Tate won with 28.4%. Both lost. Three years later, Carol Banks backed Johnson for council via Save Detroit Jobs/Detroit Leaders.'),

-- Brian Banks as Baker College adjunct
('Brian Banks', 'Baker College', 'adjunct professor (2012)', 7,
 'Daily Kos 2012 profile: "Brian Banks is a lawyer and an adjunct professor at Baker College." Same Baker College that severed relationship with his PCA charter school within 48 hours of learning about his criminal history (Oct 2026).'),

-- Benson → Tate connection
('Scott Benson', 'Joe Tate', 'both in Detroit political ecosystem', 6,
 'Joe Tate won the 2018 District 2 State Rep primary that Carol Banks and Johnson both lost. Tate went on to become Michigan House Speaker (2023-2024).'),

-- Assad Turfe enrichment
('Assad Turfe', 'FBI Wiretap Target List', 'target subject — now Deputy County Exec', 10,
 'ENRICHED: Assad Ibrahim Turfe was Chief Assistant to Wayne County Executive Warren Evans when named on 2016 wiretap target list. FBI had probable cause of bribery. He was PROMOTED to Chief of Staff (2018), then Deputy County Executive (Sep 2022). He is now the #2 person in Wayne County government. Crain "50 Names to Know in Government" (2023). Honored at La Pita celebration (2023). Oversees 43 communities. Chairs Wayne County Transit Authority. The man the FBI suspected of bribery now runs the county.'),

-- Sollars full conviction detail
('Rick Sollars', 'FBI', 'convicted 71 months (Oct 2024)', 9,
 'ENRICHED: Former Taylor Mayor. Pled guilty to conspiracy to commit bribery + wire fraud. Stole $70K+ from campaign, received $85K in bribes from contractor Shady Awad (home improvements, kitchen appliances, garage door). FBI raids Feb 2019 at homes, office, City Hall. Sentenced Oct 22, 2024. Wiretap from Fiore phone led FBI to investigate Sollars. Same civil case (Area Towing v. Sollars, 2:19-cv-10989) that produced Banks recordings.'),

-- Janee Ayers detail
('Janee Ayers', 'Gasper Fiore', 'campaign billboards funneled through Primus', 8,
 'Wiretap May 10, 2016: Primus told Fiore he was providing billboards for Ayers (gearing up for special election). They "discussed ways to get money to her but disguise it." Fiore had attended a party for Ayers. FBI raided Ayers home Aug 2021. Investigation closed Jan 2025 without charges.'),

-- Andre Spivey conviction
('Andre Spivey', 'FBI', 'convicted 2 years — towing bribery', 9,
 'Detroit City Councilman. Pled guilty to conspiracy to commit bribery. $36,000 in bribes. His conviction triggered the Aug 2021 FBI raid wave that hit Benson, Ayers, Carol Banks, Silva.'),

-- FBI 2021 raid cascade
('FBI', 'Detroit City Council Towing Probe', 'Aug 25, 2021 raids', 10,
 'Simultaneous raids: Benson home + office, Ayers home, Carol Banks home (East English Village), Ricardo Silva home, City Hall. Focus: towing operations + bribery. 20+ agents at City Hall, black containers wheeled out of Benson home. Investigation closed Jan 2025 by USAO Dawn Ison without charges against Benson, Ayers, Banks, Silva. But Spivey convicted.');

-- ============================================================
-- THE BAKER COLLEGE IRONY
-- ============================================================
-- Brian Banks was an adjunct professor at Baker College.
-- Baker College severed its relationship with Banks's PCA within 48 hours
-- of learning about his criminal history (Oct 2026).
-- The institution that once employed him as a professor
-- later cut ties with his charter school.
-- This is publicly documented and cited.
-- ============================================================

-- ============================================================
-- TURFE TIMELINE — From Wiretap Target to Running the County
-- ============================================================
-- 2002: Joins Wayne County Sheriff's Office as entry-level deputy
-- 2010s: Rises to lieutenant (youngest in department history)
-- 2015: Joins County Executive Warren Evans administration
-- 2016: Named as FBI wiretap target (#14 on Beeckman list)
--        FBI had probable cause he was "engaged in bribery"
-- 2017: Wiretap documents accidentally unsealed, his name published
-- 2018: Promoted to Chief of Staff to Evans
-- 2022: Promoted to Deputy County Executive (Sep)
-- 2023: Honored at La Pita celebration in Dearborn
-- 2023: Crain's "50 Names to Know in Government"
-- 2024: Public surrogate for Kamala Harris presidential campaign
-- 2025: Michigan Chronicle award recipient
-- 2026: STILL running Wayne County as Deputy Executive
--
-- The man the FBI suspected of bribery in 2016
-- is now the #2 person in Wayne County government.
-- ============================================================
