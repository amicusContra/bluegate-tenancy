-- ============================================================
-- OCT 6, 2026 — CAROL BANKS: THE OPERATIONAL HUB
-- Connects Dykema → Save Detroit Jobs → Eastside Slate →
-- Johnson (PCA Board) + Sheffield (Mayor) + Miller (endorsed)
--
-- THIS IS THE MISSING LINK between the dark money formation
-- layer and the political outcomes.
-- ============================================================

-- ============================================================
-- CAROL BANKS — The Operator
-- ============================================================

INSERT INTO nodes (name, type, role, status, notes) VALUES
('Carol Banks', 'person', 'political operative / operational hub', 'active',
 'Vice Chair, Original Eastside Slate. Former Chief of Staff to Councilman Scott Benson (2014-present). Former Detroit Public Schools board member (elected 2009). Former admin assistant to LaMar Lemmons. FBI raided her East English Village home Aug 25, 2021 in towing corruption investigation. Received $18,000+ from Save Detroit Jobs. Also affiliated with "Detroit Leaders" (renamed Save Detroit Jobs). Fired from DPS in 2015 after discovered working both DPS (ombudswoman) and Benson office simultaneously. Investigation closed Jan 2025 without charges.'),

('Scott Benson', 'person', 'Detroit City Councilman', 'active',
 'District 3. Took office 2014. FBI raided home and office Aug 25, 2021. Connected to Carol Banks through Eastside Slate. His staff were paid by Save Detroit Jobs to distribute literature. Investigation closed Jan 2025 without charges.'),

('Janee Ayers', 'person', 'former Detroit City Councilwoman', 'active',
 'FBI raided home Aug 25, 2021. Chief of staff Ricardo Silva also raided. Fiore/Primus discussed funneling money to her for campaign billboards. Lost re-election bid 2021 partly due to FBI cloud. Investigation closed Jan 2025 without charges.'),

('Ricardo Silva', 'person', 'former chief of staff to Ayers', 'active',
 'FBI raided home Aug 25, 2021. Part of same towing corruption investigation.'),

('Andre Spivey', 'person', 'former Detroit City Councilman', 'convicted',
 'Pled guilty to conspiracy to commit bribery. Sentenced to 2 years federal prison for accepting ~$36,000 in bribes. The conviction that triggered the Benson/Ayers/Banks raid wave.'),

('Nicholas Primus', 'person', 'intermediary', 'active',
 'Spoke with Fiore on wiretapped calls. Discussed funneling money to Ayers for campaign billboards. Described lunch with Taylor Mayor Sollars about towing contracts. Connected Fiore to political figures.'),

('Rick Sollars', 'person', 'former Taylor Mayor', 'convicted',
 'Convicted Oct 2024. 71 months federal prison. Conspiracy to commit bribery + wire fraud. $85K+ in bribes from Shady Awad. Vetoed Area Towing contract after Shane Anders cooperated with FBI. Wiretap transcripts showed Primus telling Fiore that Sollars left towing selection up to Fiore. FBI raids Feb 2019.'),

('LaMar Lemmons', 'person', 'former State Rep / Eastside Slate founder', 'active',
 'Founded original Eastside Community Slate in 1980s. Says Carol Banks and Nabil Leach "commandeered" the name when he fell behind on state paperwork. Called their version "illegitimate."'),

('William Spencer "Nabil" Leach', 'person', 'Eastside Slate co-operator', 'active',
 'Co-runs Eastside Slate with Carol Banks per state filings. High-betweenness node in Banks political network.');

-- ============================================================
-- THE CAROL BANKS OPERATIONAL MAP
-- ============================================================

INSERT INTO edges (source, target, relationship, weight, notes) VALUES
-- Carol Banks → Save Detroit Jobs (operational)
('Carol Banks', 'Save Detroit Jobs', 'affiliated operative, received $18K+', 10,
 'Received $18,000+ from Save Detroit Jobs in 2016 (Prop A fight). Also affiliated with renamed entity "Detroit Leaders." Banks IS the operational layer connecting Dykema corporate formation to political outcomes. Source: Deadline Detroit'),

-- Carol Banks → Eastside Slate (operational)
('Carol Banks', 'Original Eastside Slate', 'Vice Chair', 10,
 'Runs endorsement operation. Eastside Slate endorsed: Mary Sheffield for Mayor (2025, she won with 3/4 of votes), Jocelyn Benson for SOS/Governor, Gretchen Whitmer, Dana Nessel, Garlin Gilchrist. Also endorsed Judge Cylenthia Miller. Source: eastsideslate.com, Metro Times'),

-- Carol Banks → Scott Benson (employment)
('Carol Banks', 'Scott Benson', 'chief of staff since 2014', 8,
 'Connected through Eastside Slate work. Both raided by FBI Aug 2021. Benson staff also paid by Save Detroit Jobs to distribute literature.'),

-- Carol Banks → DPS Board (political)
('Carol Banks', 'Detroit Public Schools Board', 'elected member 2009', 7,
 'Won DPS board seat. Fired from DPS ombudswoman job 2015 after Fox 2 exposed dual employment. Later DPS became DPSCD which authorized Banks PCA charter.'),

-- Carol Banks → Latisha Johnson (Save Detroit Jobs/Detroit Leaders → campaign)
('Carol Banks', 'Latisha Johnson', 'Save Detroit Jobs/Detroit Leaders funded Johnson campaign 2021', 10,
 'Save Detroit Jobs (renamed Detroit Leaders) "meddled in city council races in districts 4 and 6." Johnson beat Elrick in District 4 (now District 2). Carol Banks had Johnson sign in her yard when FBI raided. Johnson then went on PCA Board. Source: Deadline Detroit'),

-- Carol Banks → Steve Elrick (opposition)
('Carol Banks', 'Steve Elrick', 'opposed via Save Detroit Jobs/Detroit Leaders', 9,
 'Elrick as Fox 2 reporter repeatedly exposed Banks (dual salary) and Benson (campaign finance). Save Detroit Jobs/Detroit Leaders sent mailers supporting Johnson against Elrick. Elrick filed complaint against Detroit Leaders for failure to register. Source: Deadline Detroit'),

-- Save Detroit Jobs → Prop A fight
('Save Detroit Jobs', 'Prop A (2016)', 'fought ballot measure', 7,
 'Paid Carol Banks $18K+ and Benson staff to fight Prop A. Political action using Dykema-formed dark money entity.'),

-- Save Detroit Jobs → District 4/2 race
('Save Detroit Jobs', 'District 4 Council Race 2021', 'meddled via Detroit Leaders', 9,
 'Renamed to "Detroit Leaders." Sent mailers supporting Johnson against Elrick. Elrick = journalist who exposed Benson/Banks. Johnson won → PCA Board Secretary.'),

-- Eastside Slate → Mary Sheffield endorsement
('Original Eastside Slate', 'Mary Sheffield', 'endorsed for Mayor 2025', 9,
 'Sheffield won with 3/4 of votes. Carol Banks as Vice Chair issued endorsement. Same Banks affiliated with Save Detroit Jobs which also funded Sheffield via Detroit Next PAC. Source: Metro Times'),

-- Eastside Slate → Cylenthia Miller endorsement  
('Original Eastside Slate', 'Cylenthia Miller', 'endorsed for judge', 8,
 'Carol Banks on Eastside Slate board. Miller now PCA Board President. Same endorsement network that put Johnson on PCA Board also endorsed the judge on PCA Board.'),

-- Nicholas Primus → Fiore (intermediary)
('Nicholas Primus', 'Gasper Fiore', 'discussed funneling money to Ayers', 8,
 'Wiretapped May 2016. Discussed disguising payments to Ayers for campaign billboards. Also told Fiore about lunch with Sollars re: Taylor towing contract.'),

-- Nicholas Primus → Janee Ayers (campaign)
('Nicholas Primus', 'Janee Ayers', 'funneled money for billboards', 8,
 'FBI wiretap shows Primus and Fiore "discussed ways to get money to her but disguise it." Primus providing billboards, offered Fiore chance to pay.'),

-- Nicholas Primus → Rick Sollars (towing)
('Nicholas Primus', 'Rick Sollars', 'described Sollars leaving towing to Fiore', 8,
 'Wiretapped May 2016. "Apparently, the mayor is leaving it up to [a businessman] and Fiore to work out who is the municipal tower for Taylor."'),

-- Assad Turfe → Warren Evans (employment)
('Assad Turfe', 'Warren Evans', 'Deputy County Executive / former Chief of Staff', 9,
 'Started as Wayne County Sheriff deputy 2002. Rose to lieutenant. Chief Assistant, then Chief of Staff, then Deputy County Executive (Sep 2022). Named as wiretap target while serving as Chief Assistant to Evans. Now #2 in Wayne County government.'),

-- Assad Turfe → FBI wiretap
('Assad Turfe', 'FBI Wiretap Target List', 'target subject #14', 9,
 'Named in 2016 Beeckman affidavit. FBI had probable cause to believe Turfe was "engaged in the payment and receipt of bribes and corrupt payments." Was Chief Assistant to Wayne County Executive at time. No charges filed. Now Deputy Wayne County Executive — the #2 person in Wayne County government.'),

-- Taylor mayor → conviction
('Rick Sollars', 'Shane Anders', 'vetoed Area Towing contract in retaliation', 9,
 'Anders cooperated with FBI investigation of Fiore. Sollars vetoed council-approved Area Towing contract. Anders sued (2:19-cv-10989). Sollars convicted 2024, 71 months. Same civil case produced FBI wiretap materials including Banks recordings in discovery.'),

-- Michael Irvin Lucas → identified
('Michael Irvin Lucas', 'Jessica Lucas (Fiore)', 'married to Fiore daughter', 8,
 'Worked at B&G Towing in Detroit. Married to Jessica Lucas, daughter of Gasper Fiore. B&G = Boulevard & Trumbull Towing = Fiore empire. Source: Detroit News');

-- ============================================================
-- THE COMPLETE OPERATIONAL MAP
-- ============================================================
-- 
-- FORMATION LAYER (Corporate):
--   Dykema Gossett → formed Save Detroit Jobs (Entity 802002459)
--   Entity operated under 3 names: SDJ (2016), Impact Detroit (2018), Detroit Leaders (2021)
--
-- OPERATIONAL LAYER (Carol Banks):
--   Carol Banks received $18K+ from Save Detroit Jobs
--   Carol Banks = Vice Chair of Eastside Slate
--   Carol Banks = Chief of Staff to Benson
--   Carol Banks had Johnson campaign sign in her yard
--   Save Detroit Jobs / Detroit Leaders sent mailers for Johnson
--   Eastside Slate endorsed Sheffield for Mayor
--
-- OUTCOME LAYER (Political):
--   Johnson beat Elrick → PCA Board Secretary (Banks's school board)
--   Sheffield won mayor → appointed Bettison as Chief
--   Miller endorsed → PCA Board President (Banks's school board)
--   All three outcomes benefit Brian Banks's charter school network
--
-- FBI AWARENESS:
--   Carol Banks's home raided Aug 2021 (towing corruption)
--   Assad Turfe on wiretap target list (2016) → now Deputy County Executive
--   Investigation closed Jan 2025 without charges (Benson/Ayers/Banks/Silva)
--   BUT: Area Towing v. Sollars civil case still active with wiretap materials
--
-- QUESTION:
--   Is Carol Banks related to Brian Banks?
--   Different last name chain? Or family connection?
--   Both "Banks" in Detroit politics, both connected to same network.
--   Carol Banks ran DPS board. Brian Banks ran PCA charter school.
--   NEEDS CONFIRMATION.
--
-- The data is in git. Clone it. Verify it.
-- ============================================================
