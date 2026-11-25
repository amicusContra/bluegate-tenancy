-- caseDB update: Oct 4, 2026 (Node Classification — Family vs. Betweenness)
-- Analytical framework: distinguish between people who CHOSE their position
-- in the network (high betweenness) vs. people who INHERITED it (family).
-- Some of these people are about to find out family betrayed them.
--
-- IMPORTANT: Crump-Gibson drew the Oct 1 line. She may be ok people.
-- The AGC notification for her is guidance-seeking, NOT discipline.
-- She is on the Attorney Discipline Board (ADB), NOT the AGC itself.
--
-- Run: sqlite3 caseDB.sqlite < update_oct4_node_classification.sql

--------------------------------------------------------------
-- NODE CLASSIFICATION: Add node_class column concept
--------------------------------------------------------------

-- Classification values:
-- 'operator'   = chose this, actively operates network infrastructure
-- 'between'    = high betweenness, bridges multiple clusters by choice
-- 'family'     = in network through family relationship, may be unwitting
-- 'captured'   = professional captured by network (lent credentials)
-- 'peripheral' = minor role, may not understand their position
-- 'signal'     = gave a signal they may be distancing (Crump-Gibson Oct 1)

-- OPERATORS (chose this, run it)
UPDATE graph_nodes SET tier = 1 WHERE id = 'banks-brian';
-- Carol Banks = co-operator with Brian, not inherited
-- Holland = knowing participant (lives at Banks home, manages PAC)

-- HIGH BETWEENNESS (bridge multiple clusters by choice)
-- Spencer Leach: endorsement machine ↔ Carol Banks ↔ Dem party orgs
-- Kenneth Daniels: dark money ↔ real estate ↔ Dykema
-- Gwendolyn Lewis: catering loop ↔ Dem politics ↔ real estate
-- Jason Gordon: UAW ↔ Banks campaigns ↔ Johnson campaign (+ attorney!)
-- Holland: Banks home ↔ charity ↔ PAC ↔ school foundation
-- Moreland: legal representation ↔ school governance (BETRAYAL BRIDGE)

-- FAMILY (inherited, may be unwitting)
-- Crump family: Crump-Gibson (signal), Hall (operator)
-- Gordon family: Eric + Sara (may have been getting out), Jason (between)
-- Ross family: Louis + Louis III (catering), Carlton (between/operator)
-- Daniels family: Kenneth + Kenneth III (both have entities — likely knowing)

-- CAPTURED (professional credentials lent to network)
-- Alcendor + Harmon: GLLG partners, exposure through Crump-Gibson
-- Meiste + Reams: Anchor Rock partners, may not know about Detroit side
-- Miller (Cylenthia): PCA president, background unknown
-- Hutchings: PCA treasurer, Ypsilanti — distance suggests recruited

-- SIGNAL (distancing behavior observed)
-- Crump-Gibson: Oct 1 letter = explicit scope limitation
-- Eric/Sara Gordon: Custom Promo Inc dissolution = possible exit attempt

--------------------------------------------------------------
-- METADATA: Tag nodes with classification
--------------------------------------------------------------

-- We store classification in graph_nodes notes field since schema
-- doesn't have a dedicated column. Future: add node_class column.

-- Operators
UPDATE graph_nodes SET label = label || ' [OPERATOR]' 
WHERE id IN ('banks-brian') AND label NOT LIKE '%OPERATOR%';

-- High betweenness
UPDATE graph_nodes SET label = label || ' [HIGH-BETWEEN]'
WHERE id IN ('leach-spencer', 'daniels-kenneth', 'lewis-gwendolyn', 
             'gordon-jason', 'holland-joseph', 'moreland-lamar')
AND label NOT LIKE '%BETWEEN%';

-- Family (potentially unwitting)  
UPDATE graph_nodes SET label = label || ' [FAMILY]'
WHERE id IN ('ross-louis', 'alcendor-ayanna', 'harmon-henri',
             'meiste-brian', 'nakenge-beverly', 'elcock-kiambu')
AND label NOT LIKE '%FAMILY%';

-- Signal (distancing observed)
UPDATE graph_nodes SET label = label || ' [SIGNAL]'
WHERE id IN ('crump-gibson-jehan')
AND label NOT LIKE '%SIGNAL%';

--------------------------------------------------------------
-- CRUMP-GIBSON CLARIFICATION
--------------------------------------------------------------

-- Crump-Gibson is on the ATTORNEY DISCIPLINE BOARD (ADB), 
-- NOT the Attorney Grievance Commission (AGC).
-- AGC = investigates + prosecutes attorney misconduct
-- ADB = adjudicates (holds hearings, decides discipline)
-- She is a HEARING PANELIST on ADB.
-- She would recuse from GLLG-related matters.
-- Her COLLEAGUES on ADB would hear any case that proceeds.
-- The AGC notification drafted for her is GUIDANCE-SEEKING,
-- NOT a complaint seeking discipline.
-- Her Oct 1 letter = strongest signal of possible good faith.

--------------------------------------------------------------
-- "ABOUT TO FIND OUT" LIST
--------------------------------------------------------------

-- People who may learn their family/associates put them at risk:
--
-- 1. Jehan Crump-Gibson
--    Risk: If Hall is her sister, Hall's PPO put Crump-Gibson's
--    ADB position at risk. Crump-Gibson already drew the line.
--    She may not know about Crump Hall of Justice entities.
--
-- 2. Louis Ross / Louis Ross III
--    Risk: Their catering company was the receiving end of a
--    money loop they may not have designed. Carlton Ross 
--    (Right Turn Treasurer) was the architect.
--
-- 3. Eric & Sara Gordon
--    Risk: Their son Jason inherited the family business, got
--    FBI-investigated, and runs it from a law office. The
--    dissolution (Feb 2022) may have been their exit attempt.
--
-- 4. Ayanna Alcendor & Henri Harmon (GLLG partners)
--    Risk: Equity partners whose firm is now linked to a PPO
--    filing Crump-Gibson explicitly disclaimed. Professional
--    liability + reputation tied to decisions they didn't make.
--
-- 5. Doug Reams & Brian Meiste (Anchor Rock partners)
--    Risk: West Michigan builders in commercial partnership
--    with Banks. They may have no idea about the Detroit 
--    political empire, the felony history, or the schools.
--
-- NOTE: This classification informs the TONE of any
-- communication. Operators get confronted. Betweens get
-- mapped. Family gets treated with care. Signals get
-- acknowledged. Captured professionals get the courtesy
-- of learning what they're part of before it goes public.
