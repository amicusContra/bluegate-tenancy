-- ============================================================
-- OCT 7, 2026 — HEMLOCK SUBGRAPH: Ellison Panopticon
-- Anderson localization in a town of 2,000
-- Six-layer architecture: ISP → FOIA → schools → courts → legal → mask
-- Run: sqlite3 caseDB.sqlite < update_oct7_hemlock_subgraph.sql
-- ============================================================

-- ============================================================
-- PERSONS
-- ============================================================

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ellison-philip', 'Philip L. Ellison', 'person',
    'P70894. Hemlock, MI. Born and raised Hemlock. BS Business Admin + Personal Computer Specialist (LSSU 2004). MBA (CMU 2006). JD (MSU Law 2010). Adjunct professor SVSU (Aug 2017-present) and Mid Michigan CC (2006). Owner Quagmire Solutions LLC (Nov 2000-Aug 2007). Attorney OLC PLC (Nov 2010-present). Super Lawyers 2016-2025. Federally appointed class counsel x2. SCOTUS bar member. AGC 25-2363 OPEN (told court it was closed — AGC confirmed open). $73,752.45 federal sanctions (Garcia v. Title Check, W.D. Mich 1:15-cv-00975, SCOTUS cert denied). Fabricated witness "Samantha Aljouny" — IC3 filed Oct 6 2026. 153-domain portfolio via Quagmire/info@quagmiresolutions.com. Harassment domains targeting Rita Williams incl. minor child. SLAPP suit 25-2441-CZ void ab initio (bankruptcy auto stay, Kalb v. Feuerstein). Macomb County home foreclosed ~2013. Hemlock PS "Human of Hemlock." SCBA member. LSSU Student Webmaster 2001-2004. Co-op Hemlock Semiconductor 2000-2001. NODE_CLASS: OPERATOR.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ellison-katherine', 'Katherine (Katie) Ellison', 'person',
    'Philip Ellison''s wife. VP, Saginaw Intermediate School District Board of Education. VP, Hemlock Public School District Board of Education. Dual board positions = budget oversight authority across two districts. Vendor contracts, legal services, IT infrastructure, FOIA compliance. NODE_CLASS: OPERATOR.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ellison-calvin', 'Calvin Lee Ellison', 'person',
    'Resides at Quagmire Solutions LLC registered address (family property, South Brennan Rd area, Hemlock). Philip''s relative (father or brother). Voter record confirms Hemlock. NODE_CLASS: FAMILY.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('edgecomb-lisa', 'Lisa Edgecomb', 'person',
    'Legal Assistant to Philip L. Ellison at OLC PLC. Tel: (989) 642-0055. Notary public. Notarized Ellison''s sworn denial of connection to Samantha Aljouny. The person keeping the record (notarized affidavit) is the employee of the person swearing the affidavit. NODE_CLASS: CAPTURED.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('gafkay-julie', 'Judge Julie A. Gafkay', 'person',
    'Chief Judge, 10th Circuit Court (Saginaw County). Adjunct professor SVSU — 6+ year colleague overlap with Ellison at same small regional university. Past President, Saginaw County Bar Association. Three simultaneous Ellison/OLC cases on her docket: (1) OLC v. Williams 25-2441-CZ (SLAPP), (2) Ellison v. Consumers Energy, (3) Sova class action. MCR 2.003(C)(1) recusal question: personal bias or prejudice re party''s attorney. NODE_CLASS: CAPTURED.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('borrello-andre', 'Judge Andre R. Borrello', 'person',
    'Saginaw County Circuit Court Judge. Originally signed contempt order against Rita Williams in OLC v. Williams. Recused May 2026. Recusal order did not state reasons. NODE_CLASS: PERIPHERAL.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ellsworth-kelly', 'Kelly D. Ellsworth', 'person',
    'P39820, admitted 1990, Saginaw County. Briefly represented Rita Williams, dissuaded her from pursuing claims. Family in Saginaw bar since 1986 (Kirk Ellsworth Sr. founded firm). OWI reprimand on disciplinary record. Not conspiracy — structural cowardice: small-town bar member cannot go scorched earth on colleague without losing chief judge goodwill for all other clients. NODE_CLASS: PERIPHERAL.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('fabien-chris', 'Christopher A. Fabien', 'person',
    'Co-Owner, CTO, Network Engineer at LakeNet LLC since April 2010. BS Computer Engineering (Kettering University). Stanley Assembly Technologies (Aug 2000-Nov 2007). Nexteer Automotive (Dec 2007-Jan 2013). Lives at XXX St Marys Dr, Hemlock MI 48626. FCC Form 499 CEO. MPSC CLEC testimony (Case U-20961). ARIN contact: FABIE1-ARIN. chris@lakenetmi.com. NODE_CLASS: INDEPENDENT (no proven connection to Ellison network).');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('fabien-keri', 'Keri Fabien', 'person',
    'Co-Owner, Director of Operations at LakeNet LLC. FCC Form 499 senior officer. NODE_CLASS: INDEPENDENT.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('williams-rita', 'Rita Williams', 'person',
    'Investigative journalist. Clutch Justice (clutchjustice.com). hello@clutchjustice.com. Richland, Michigan. SLAPP suit target (25-2441-CZ). PPO target (manufactured violation — fabricated Facebook account). Harassment domain target (ritafelinewilliams.com + minor child domain). Employer contact retaliation. Primary Analytical Reference for detroit.primals.eco. Essie Justice Group National Policy Agenda Advisory Subcommittee. Tuebor cross-protection ACTIVE Oct 6, 2026. WRONGED PARTY. NODE_CLASS: TARGET/WRONGED.');

-- ============================================================
-- ENTITIES (organizations / businesses)
-- ============================================================

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('olc-plc', 'Outside Legal Counsel PLC', 'entity',
    'Michigan professional limited liability company. Est. Nov 2010. HQ: 530 W Saginaw St (PO Box 107), Hemlock MI 48626. Up North Office: 4522 W Higgins Lake Dr, Roscommon MI 48653 (purchased Nov 7 2024 for $150K — former bank). (989) 642-0055. olcplc.com + michigansupremecourtattorney.com. Civil litigation: property/water rights, civil rights, government transparency, class actions, appeals. Philip L. Ellison sole attorney. Lisa Edgecomb legal assistant.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('quagmire-solutions', 'Quagmire Solutions LLC', 'entity',
    'Michigan domestic LLC. Philip L. Ellison owner (Nov 2000-Aug 2007 per LinkedIn, but entity still ACTIVE per LARA). Web design and communications firm. Served: "Internet service companies" (plural), "a major regional newspaper owned by an international outfit" (Saginaw News / Advance Local / Newhouse / Condé Nast). WHOIS registrant for 153+ domains (info@quagmiresolutions.com). Operates FOIAworks. I-500 snowmobile race website credits (Wayback Machine 2006). Hemlock address.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('south-brennan-property', 'South Brennan Property LLC', 'entity',
    'Michigan domestic LLC. Entity ID E62024. Formed April 2, 2015. Active. Registered agent: Philip L. Ellison. Address: 529 W Saginaw St, Hemlock MI 48626. Named after South Brennan Road in Hemlock. Managed by members. Likely real estate holding company for Hemlock property.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('foiaworks', 'FOIAworks', 'entity',
    'Michigan FOIA software platform. foiaworks.com. "Owned and operated by Quagmire Solutions, LLC." "Conceived by a Michigan FOIA attorney and former website designer." NO PRIVACY POLICY — /privacy/ returns 404. ToS (effective Aug 22 2026) grants Quagmire "limited license to host, copy, process, transmit, back up, and display User Content." Collects: who is filing, what records they want, which agencies, all correspondence, full timeline. Target users: journalists, investigators, frequent requesters, community groups. Pricing: free first request, $4.95/submission, Pro $19.95/mo, Statewide $69.95/mo (120 submissions — enough for all 83 MI counties), Enterprise custom. SURVEILLANCE PLATFORM DISGUISED AS TRANSPARENCY TOOL.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('lakenet-llc', 'LakeNet LLC', 'entity',
    'Michigan domestic LLC. Formed April 8, 2010. HQ: 16690 Gratiot Rd, Hemlock MI 48626. (989) 643-5819. lakenet@lakenetmi.com. lakenetfiber.com. MPSC registered: Fiber/Wireless Broadband, CAP, CLEC (Case U-20961), VoIP, Fixed Wireless. FCC Filer #829254. AS11910. IP range: 162.247.144.0/21 + 158.51.68.0/22. Officers: Chris Fabien (CTO), Keri Fabien (Operations), Rob Bresnahan (CFO). ONLY broadband ISP headquartered in Hemlock. 100+ miles fiber in Hemlock/Merrill/Marion Springs/St. Charles. Upstream: Hurricane Electric, Cogent, Daystarr. ARIN route modified by admin@pfnllc.net Sep 18 2024. ROBIN grant expansion. "Internet service in Mid-Michigan since 2010." Calix GigaSpire managed WiFi.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('saginaw-isd', 'Saginaw Intermediate School District', 'org',
    'Board of Education. Katie Ellison = Vice President. Budget oversight for all constituent districts in Saginaw County.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('hemlock-ps', 'Hemlock Public School District', 'org',
    'Board of Education. Katie Ellison = Vice President. Published "Humans of Hemlock: Philip Ellison" on hemlockps.com/article/1721872. Budget/vendor/FOIA oversight. Hemlock Huskies. Est. 1863.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('svsu', 'Saginaw Valley State University', 'org',
    'University Center, Michigan. Ellison adjunct professor of law since Aug 2017. Gafkay adjunct professor. 6+ year colleague overlap at same small regional university. Faculty directory confirms both.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('scba', 'Saginaw County Bar Association', 'org',
    'Professional bar association. Gafkay = past president. Ellison = member. Small bar — everyone knows everyone. Structural capture: local attorneys depend on chief judge goodwill for all other clients.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('saginaw-circuit', 'Saginaw County Circuit Court', 'org',
    '10th Judicial Circuit. Chief Judge: Julie A. Gafkay. Cases: OLC v. Williams 25-2441-CZ, Ellison v. Consumers Energy, Sova class action. Borrello recused from SLAPP suit May 2026.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('air-advantage', 'Air Advantage', 'entity',
    'Frankenmuth MI wireless ISP. USDA Rural Utilities Service (RUS) funded. Motorola point-to-multipoint. Served Saginaw, Bay, Lapeer, St. Clair counties. 4,500 subscribers. President: Scott Zimmer. Likely one of Quagmire Solutions'' "Internet service companies" clients (2000-2007 timeframe, same geography).');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('saginaw-news', 'Saginaw News / MLive Media Group', 'entity',
    'Saginaw regional newspaper. Owned by Advance Local (subsidiary of Advance Publications / Newhouse family / Condé Nast = "international outfit"). Likely the "major regional newspaper owned by an international outfit" that Quagmire Solutions served. Saginaw/Midland geography matches.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('clutch-justice', 'Clutch Justice', 'entity',
    'Rita Williams'' investigative journalism platform. clutchjustice.com. hello@clutchjustice.com. Independent. Investigative journalism + institutional forensics consulting. Arm 1: paid forensics. Arm 2: free journalism (no paywall). Saginaw County SLAPP coverage. Barry County coverage. Amicus brief library. 2+ years publishing. Primary source reporting cited in court filings.');

-- ============================================================
-- CASES
-- ============================================================

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-slapp-williams', 'OLC PLC et al. v. Williams (25-2441-CZ)', 'case',
    'Saginaw County Circuit Court. Filed Nov 2025 by Ellison. Defamation/SLAPP suit against Rita Williams. VOID AB INITIO — filed during federal bankruptcy automatic stay (11 U.S.C. § 362(a)). Kalb v. Feuerstein, 308 U.S. 433 (1940). Ellison never sought relief from stay. UPEPA special motion filed by Rita May 6 2026. Borrello originally assigned, recused May 2026. Gafkay = remaining chief judge. MCL 691.1851 et seq. COA Case No. 380599.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-garcia-sanctions', 'Garcia v. Title Check LLC (1:15-cv-00975)', 'case',
    'W.D. Michigan. $73,752.45 sanctions against Ellison. SCOTUS cert denied. Pattern: file frivolous → sanctioned → appeal → denied → SCOTUS → denied. Financial exposure motivates §1988 fee-shifting strategy in SLAPP litigation.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-agc-25-2363', 'AGC Investigation 25-2363', 'case',
    'Attorney Grievance Commission investigation of Philip L. Ellison. OPEN as of Oct 2026. Ellison told Saginaw County Circuit Court this investigation was closed. AGC confirmed it remains open. False statement to court about own disciplinary status.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-ic3-aljouny', 'IC3 Complaint — Fabricated Witness', 'case',
    'Filed Oct 6, 2026. "Samantha Aljouny" fabricated witness submitted via ProtonMail. 13 convergence points prove fabrication. Wire fraud (18 U.S.C. § 1343). Used to support SLAPP suit and federal contempt proceedings.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-ellison-consumers', 'Ellison v. Consumers Energy', 'case',
    'Saginaw County Circuit Court. Before Judge Gafkay. One of three simultaneous Ellison cases before same judge. UPEPA invoked — Ellison''s own precedent creates judicial estoppel.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-sova', 'Sova Class Action', 'case',
    'Saginaw County Circuit Court. Before Judge Gafkay. Third simultaneous Ellison case. Three cases before one judge = structural conflict (MCR 2.003).');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-taylor-saginaw', 'Taylor v. City of Saginaw', 'case',
    'Federal class action. Tire chalking = Fourth Amendment violation. Ellison''s signature "fights for the little guy" case. Sixth Circuit ruling in favor. MLive profile 2019. Class counsel appointment. The mask''s foundation.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('case-howard-macomb', 'Howard v. Macomb County', 'case',
    'Tax foreclosure surplus proceeds. Sixth Circuit (25a0070p-06). SCOTUS petition with Pacific Legal Foundation. Ellison = trial and appellate counsel. Irony: his own Macomb home was foreclosed ~2013. Built class-action practice on the pain he experienced.');

-- ============================================================
-- PROPERTIES
-- ============================================================

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('prop-530-saginaw', '530 W Saginaw St, Hemlock MI 48626', 'property',
    'OLC PLC headquarters. PO Box 107. (989) 642-0055.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('prop-529-saginaw', '529 W Saginaw St, Hemlock MI 48626', 'property',
    'South Brennan Property LLC registered address. Across street from OLC HQ. 2 entities registered at this address per CompaniesMI.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('prop-4522-higgins', '4522 W Higgins Lake Dr, Roscommon MI 48653', 'property',
    'OLC PLC "Up North Office." Sold Nov 7, 2024 for $150,000. MLS# 201830608. Former bank (drive-through window), renovated to real estate office, now attorney office. 1,500 sq ft commercial, 0.40 acres. Parcel #004-468-001-0000. Gerrish Township. FOIAworks mailing address. BUYER UNKNOWN — Roscommon County Register of Deeds needed. Listed by Midge Rutter, Midge & Co-Luxury Lakefront Homes.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('prop-16690-gratiot', '16690 Gratiot Rd, Hemlock MI 48626', 'property',
    'LakeNet LLC headquarters. MPSC, FCC, ARIN registered address.');

-- ============================================================
-- DOMAINS (harassment + infrastructure)
-- ============================================================

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('domain-ritasite', 'ritafelinewilliams.com', 'domain',
    'Harassment domain. Registered via GoDaddy. Targets Rita Williams by name. Impersonation site LIVE. Renewed Sep 2026. Part of 30-minute batch registration (3 domains targeting SLAPP victims).');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('domain-olcplc', 'olcplc.com', 'domain',
    'OLC PLC law firm website. WHOIS history: originally registered to Philip Ellison / info@quagmiresolutions.com → changed to Outside Legal Counsel → Domains By Proxy privacy shield. Same GoDaddy + domaincontrol.com nameserver infrastructure as harassment domains.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('domain-foiaworks', 'foiaworks.com', 'domain',
    'FOIAworks platform. Operated by Quagmire Solutions LLC. No privacy policy (404 at /privacy/). Intelligence collection platform.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('domain-scotus', 'michigansupremecourtattorney.com', 'domain',
    'OLC PLC vanity domain. Positions Ellison as SCOTUS-level attorney. Part of the public persona mask.');

-- ============================================================
-- GRAPH EDGES — The Network
-- ============================================================

-- Layer 1: Entity ownership
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('ellison-philip', 'olc-plc', 'owns/operates', 'Sole attorney. Founded Nov 2010.'),
('ellison-philip', 'quagmire-solutions', 'owns/operates', 'Founded Nov 2000. LinkedIn says ended Aug 2007 but LARA entity still active. Operates FOIAworks.'),
('ellison-philip', 'south-brennan-property', 'registered agent', 'Formed April 2, 2015. Real estate holding.'),
('quagmire-solutions', 'foiaworks', 'owns/operates', 'Per foiaworks.com/about: "owned and operated by Quagmire Solutions, LLC"'),
('quagmire-solutions', 'domain-ritasite', 'registered', 'WHOIS history: info@quagmiresolutions.com. GoDaddy. 30-min batch.'),
('quagmire-solutions', 'domain-olcplc', 'registered', 'WHOIS history shows original registrant.'),
('quagmire-solutions', 'domain-foiaworks', 'registered', 'FOIAworks domain.'),
('olc-plc', 'domain-scotus', 'operates', 'Vanity domain for SCOTUS practice marketing.');

-- Layer 2: Family
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('ellison-philip', 'ellison-katherine', 'spouse', 'Married. MLive 2019: "Ellison, who is married and the father of an 18-month-old son." Son: Patton.'),
('ellison-philip', 'ellison-calvin', 'family', 'Calvin Lee Ellison at Quagmire Solutions registered address. Father or brother.'),
('ellison-philip', 'edgecomb-lisa', 'employs', 'Legal assistant at OLC PLC. Notarized Ellison sworn denial of Aljouny connection.');

-- Layer 3: School boards
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('ellison-katherine', 'saginaw-isd', 'VP Board of Education', 'Dual board seat. Budget/vendor/FOIA oversight.'),
('ellison-katherine', 'hemlock-ps', 'VP Board of Education', 'Dual board seat. Published "Humans of Hemlock: Philip Ellison" on hemlockps.com.'),
('hemlock-ps', 'ellison-philip', 'promoted', '"Humans of Hemlock" profile: "Hemlock is a brighter, more connected place because of Philip Ellison."');

-- Layer 4: Judicial access
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('ellison-philip', 'svsu', 'adjunct professor', 'Aug 2017-present. Teaches law.'),
('gafkay-julie', 'svsu', 'adjunct professor', '6+ year overlap with Ellison at same institution.'),
('ellison-philip', 'gafkay-julie', 'SVSU colleague + SCBA member', 'Colleague at same small university. She = past SCBA president, he = member. 3 simultaneous cases before her.'),
('ellison-philip', 'scba', 'member', 'Saginaw County Bar Association.'),
('gafkay-julie', 'scba', 'past president', 'Past President SCBA. Institutional authority.'),
('gafkay-julie', 'saginaw-circuit', 'Chief Judge', '10th Judicial Circuit.'),
('borrello-andre', 'saginaw-circuit', 'Judge', 'Originally assigned to SLAPP suit. Recused May 2026.');

-- Layer 5: Cases
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('ellison-philip', 'case-slapp-williams', 'plaintiff attorney', 'Filed SLAPP suit against Rita. Void ab initio.'),
('williams-rita', 'case-slapp-williams', 'defendant', 'SLAPP target. Filed UPEPA special motion.'),
('gafkay-julie', 'case-slapp-williams', 'presiding judge', 'After Borrello recusal. Chief Judge.'),
('borrello-andre', 'case-slapp-williams', 'recused judge', 'Signed contempt, then recused May 2026.'),
('gafkay-julie', 'case-ellison-consumers', 'presiding judge', 'Second simultaneous Ellison case.'),
('gafkay-julie', 'case-sova', 'presiding judge', 'Third simultaneous Ellison case.'),
('ellison-philip', 'case-garcia-sanctions', 'sanctioned attorney', '$73,752.45. SCOTUS cert denied.'),
('ellison-philip', 'case-agc-25-2363', 'subject', 'Open investigation. Told court it was closed.'),
('ellison-philip', 'case-ic3-aljouny', 'subject', 'IC3 filed Oct 6 2026. Fabricated witness.'),
('ellison-philip', 'case-taylor-saginaw', 'class counsel', 'Tire chalking. "Fights for the little guy." The mask.'),
('ellison-philip', 'case-howard-macomb', 'trial/appellate counsel', 'Tax foreclosure. SCOTUS petition w/ Pacific Legal Foundation.');

-- Layer 6: ISP infrastructure
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('fabien-chris', 'lakenet-llc', 'co-owner/CTO', 'Founded April 2010. BS Computer Engineering, Kettering.'),
('fabien-keri', 'lakenet-llc', 'co-owner/operations', 'Director of Operations.'),
('ellison-philip', 'lakenet-llc', 'customer', 'Office IP 162.247.150.54 = LakeNet AS11910.'),
('quagmire-solutions', 'air-advantage', 'suspected client', 'Ellison served "Internet service companies" (plural) 2000-2007. Air Advantage = Saginaw-area wireless ISP. Unconfirmed.'),
('quagmire-solutions', 'saginaw-news', 'client', '"Major regional newspaper owned by an international outfit." Saginaw News = Advance Local = Newhouse = Condé Nast.');

-- Layer 7: Properties
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('olc-plc', 'prop-530-saginaw', 'headquarters', 'PO Box 107.'),
('south-brennan-property', 'prop-529-saginaw', 'registered address', 'Across street from OLC HQ.'),
('olc-plc', 'prop-4522-higgins', 'Up North Office', 'Purchased Nov 7 2024 for $150K. Former bank. FOIAworks mailing address.'),
('lakenet-llc', 'prop-16690-gratiot', 'headquarters', 'MPSC/FCC/ARIN registered.'),
('ellison-calvin', 'quagmire-solutions', 'resides at registered address', 'Calvin at Quagmire Solutions family property.');

-- Layer 8: Attack vectors (targeting Rita)
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('ellison-philip', 'williams-rita', 'SLAPP suit', '25-2441-CZ. Void ab initio.'),
('ellison-philip', 'williams-rita', 'fabricated witness', '"Samantha Aljouny" via ProtonMail. 13 convergence points.'),
('ellison-philip', 'williams-rita', 'harassment domains', 'ritafelinewilliams.com + minor child domain. 30-min batch.'),
('ellison-philip', 'williams-rita', 'employer contact', 'Contacted Rita''s employers. Retaliation for journalism.'),
('ellison-philip', 'williams-rita', 'PPO weaponization', 'Manufactured PPO violation via fabricated Facebook account.'),
('ellison-philip', 'williams-rita', 'cross-forum multiplication', 'Same allegations filed across Macomb, Oakland, Saginaw counties.');

-- Layer 9: Cross-reference to Detroit subgraph
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, notes) VALUES
('williams-rita', 'clutch-justice', 'founder/journalist', 'Primary Analytical Reference for detroit.primals.eco.'),
('clutch-justice', 'ellison-philip', 'investigative target', 'Published: ghost witness, void lawsuit, UPEPA, AGC investigation.');

-- ============================================================
-- GRAPH NODES — For visualization / NetworkX / D3
-- ============================================================

INSERT OR IGNORE INTO graph_nodes (id, label, tier, x, y) VALUES
-- Tier 1: Center (Ellison family)
('ellison-philip', 'Philip L. Ellison [OPERATOR]', 1, 0, 0),
('ellison-katherine', 'Katie Ellison [OPERATOR]', 1, 100, 50),
('ellison-calvin', 'Calvin Ellison [FAMILY]', 1, -100, 50),

-- Tier 2: Entities
('olc-plc', 'Outside Legal Counsel PLC', 2, 200, -100),
('quagmire-solutions', 'Quagmire Solutions LLC', 2, -200, -100),
('south-brennan-property', 'South Brennan Property LLC', 2, 0, -200),
('foiaworks', 'FOIAworks [NO PRIVACY POLICY]', 2, -300, -200),

-- Tier 3: Institutional capture
('gafkay-julie', 'Judge Gafkay [CAPTURED]', 3, 300, 100),
('saginaw-isd', 'Saginaw ISD Board', 3, 200, 200),
('hemlock-ps', 'Hemlock PS Board', 3, 0, 200),
('svsu', 'SVSU', 3, 400, 0),
('scba', 'Saginaw County Bar', 3, 400, 200),
('saginaw-circuit', 'Saginaw Circuit Court', 3, 300, -100),
('borrello-andre', 'Judge Borrello [RECUSED]', 3, 400, -200),

-- Tier 4: ISP layer
('lakenet-llc', 'LakeNet LLC [ISP]', 4, -400, 100),
('fabien-chris', 'Chris Fabien', 4, -500, 50),
('fabien-keri', 'Keri Fabien', 4, -500, 150),

-- Tier 5: Wronged / targets
('williams-rita', 'Rita Williams [WRONGED]', 5, 0, 400),
('clutch-justice', 'Clutch Justice', 5, -150, 400),

-- Tier 6: Properties
('prop-530-saginaw', '530 W Saginaw', 6, 200, -300),
('prop-529-saginaw', '529 W Saginaw', 6, 100, -300),
('prop-4522-higgins', 'XXXX Higgins Lake Dr', 6, 0, -350),
('prop-16690-gratiot', '16690 Gratiot Rd', 6, -400, -300),

-- Tier 7: External entities
('air-advantage', 'Air Advantage [ISP]', 7, -500, -200),
('saginaw-news', 'Saginaw News / Advance', 7, -300, -350),
('edgecomb-lisa', 'Lisa Edgecomb [CAPTURED]', 7, 100, -100),
('ellsworth-kelly', 'Kelly Ellsworth [PERIPHERAL]', 7, 200, 350),

-- Tier 8: Harassment domains
('domain-ritasite', 'ritafelinewilliams.com', 8, -200, 350),
('domain-olcplc', 'olcplc.com', 8, 300, -250),
('domain-foiaworks', 'foiaworks.com', 8, -400, -250),
('domain-scotus', 'michigansupremecourtattorney.com', 8, 400, -300),

-- Tier 9: Cases
('case-slapp-williams', 'SLAPP 25-2441-CZ [VOID]', 9, 100, 300),
('case-garcia-sanctions', 'Garcia - $73K Sanctions', 9, -100, 300),
('case-agc-25-2363', 'AGC 25-2363 [OPEN]', 9, 200, 300),
('case-ic3-aljouny', 'IC3 - Fabricated Witness', 9, -200, 300);

-- ============================================================
-- METADATA
-- ============================================================

-- Hemlock subgraph statistics
-- Persons: 10
-- Organizations: 7
-- Entities (business): 8
-- Cases: 8
-- Properties: 4
-- Domains: 4
-- Graph nodes: 30+
-- Graph edges: 40+
-- Layers: 9 (entity ownership, family, school boards, judicial,
--          cases, ISP, properties, attack vectors, cross-reference)
