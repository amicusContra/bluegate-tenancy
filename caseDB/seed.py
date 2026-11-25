"""
Seed the case intelligence database with all known data.
Run: python seed.py
Creates/overwrites caseDB.sqlite in this directory.
"""
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "caseDB.sqlite")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def j(lst):
    """JSON-encode a list for storage."""
    return json.dumps(lst) if lst else None

def main():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(open(SCHEMA_PATH).read())

    # ============================================================
    # ENTITIES
    # ============================================================
    entities = [
        # -- People: defendants / respondents --
        ("banks-brian", "Brian Roderick Banks", "person",
         j(["Brian Banks, J.D., Ph.D."]),
         j([{"street": "1968 Severn Road", "city": "Grosse Pointe Woods", "state": "MI", "zip": "48236", "source": "Wayne ROD", "current": True}]),
         None, "info@macdowellprep.com", "9 felony convictions. SID 2029469K. Claims J.D. — no bar record."),

        ("holland-joseph", "Joseph Holland Jr.", "person",
         j(["Joseph Antione Williams"]),
         j([{"street": "1968 Severn Road", "city": "Grosse Pointe Woods", "state": "MI", "zip": "48236", "source": "LARA/ROD", "current": True}]),
         None, None, "MDOC #443789. Discharged WITHOUT IMPROVEMENT May 2024. 5 bankruptcies."),

        ("smith-shayla", "Shayla R. Smith", "person", None,
         j([{"street": "XXXXX Dresden Street", "city": "Detroit", "state": "MI", "zip": "48205", "source": "court filings", "current": False},
            {"street": "32332 N River Road", "city": "Harrison Township", "state": "MI", "zip": "48045", "source": "Macomb ROD", "current": True}]),
         None, None, "DaSean's ex. 9 years unilateral custody. No court order."),

        ("smith-leon", "Leon A. Smith", "person", None,
         j([{"street": "XXXXX Dresden Street", "city": "Detroit", "state": "MI", "zip": "48205", "source": "court filings", "current": True}]),
         "(313) 412-4703", None, "USPS mail carrier, Harper Woods PO. Assaulted DaSean Sep 2."),

        ("smith-marquita", "Marquita R. Smith", "person", None,
         j([{"street": "XXXXX Merrimac Circle", "city": "Clinton Township", "state": "MI", "zip": "48038", "source": "Macomb ROD", "current": True}]),
         None, None, "Leon's wife. BK 26-47542."),

        ("smith-simone", "Simone R. Smith", "person", None,
         j([{"street": "21734 Normandy Avenue", "city": "Eastpointe", "state": "MI", "zip": "48021", "source": "Macomb ROD", "current": True}]),
         None, None, "Shayla's sister. BK 26-49404-lsg."),

        # -- People: plaintiffs / petitioners --
        ("mok-kevin", "Kevin Mok", "person", None,
         j([{"street": "[REDACTED_ADDR_1]", "city": "Lansing", "state": "MI", "zip": "48910", "current": True}]),
         "[REDACTED_PHONE]", "eco.primal@pm.me", "Navy veteran. Military intelligence. Pro se plaintiff + witness/expert."),

        ("mitchell-dasean", "DaSean Mitchell", "person", None,
         j([{"street": "[REDACTED_ADDR_2] St", "city": "Lansing", "state": "MI", "zip": "48910", "current": True}]),
         None, None, "Army veteran. Father of Sahana (9) and Allanna (7). Kevin's best friend."),

        # -- People: judges --
        ("judge-koenig", "Hon. Carol N. Koenig", "person", None, None, None, None, "Ingham County. PPO cases."),
        ("judge-stokes", "Hon. Stokes", "person", None, None, None, None, "Ingham County 30th Circuit. Civil cases 4301 + 4349."),
        ("judge-triplett", "Hon. Triplett", "person", None, None, None, None, "Wayne County. Custody 26-108221-DC."),
        ("judge-miller", "Hon. Cylenthia Miller", "person", None,
         j([{"street": "5301 Russell Street", "unit": "Room 504", "city": "Detroit", "state": "MI", "zip": "48211", "source": "CJC", "current": True}]),
         None, None, "3rd Circuit. PCA Board Chair. JTC complaint filed. Nov 3 ballot."),
        ("judge-yancey", "Hon. Tenisha Yancey", "person", None,
         j([{"street": "421 Madison Street", "city": "Detroit", "state": "MI", "zip": "48226", "current": True}]),
         None, None, "36th District. MacDowell Board Chair. Campaign paid Banks Strategy $383.82."),
        ("judge-perkins-sean", "Hon. Sean Perkins", "person", None, None, None, None, "36th District. Brother of Todd Perkins."),
        ("judge-ramsey", "Hon. Kelly Ramsey", "person", None,
         j([{"street": "5301 Russell Street", "unit": "Room 703", "city": "Detroit", "state": "MI", "zip": "48211", "current": True}]),
         None, None, "3rd Circuit. CJC."),
        ("judge-sabree-aliyah", "Hon. Aliyah Sabree", "person", None,
         j([{"street": "1025 E. Forest Ave", "unit": "Room 3-D", "city": "Detroit", "state": "MI", "zip": "48207", "current": True}]),
         None, None, "36th District. Lincoln Hall. Nov 3 ballot. Eric Sabree's daughter."),
        ("referee-biggar", "Referee Biggar", "person", None, None, None, None, "Wayne County FOC."),

        # -- People: attorneys / enablers --
        ("perkins-todd", "Todd Perkins", "person", j(["P55623"]), None, None, None, "Banks' attorney. Brother of Judge Sean Perkins. 4 bankruptcies."),
        ("moreland-lamar", "Lamar Moreland", "person", j(["AAG"]),
         j([{"street": "PO Box 30212", "city": "Lansing", "state": "MI", "zip": "48909", "current": True}]),
         None, None, "Assistant Attorney General."),
        ("schmiedeknecht-katie", "Katie Schmiedeknecht", "person", None, None, None, None, "MDE Analyst, OEE. Gave Banks the loophole Feb 2022."),
        ("welch-tonesa", "Tonesa Welch", "person", j(["Black Mafia Queen"]), None, None, None, "Banks' half-aunt. BMF defendant #22. USA v. Flenory (2:05-cr-80955)."),
        ("sabree-eric", "Eric Sabree", "person", None,
         j([{"street": "400 Monroe Street", "unit": "5th Floor", "city": "Detroit", "state": "MI", "zip": "48226", "current": True}]),
         None, None, "Wayne County Treasurer."),

        # -- Organizations --
        ("pca", "Purpose Charter Academy", "school", None,
         j([{"street": "10101 E. Canfield Street", "city": "Detroit", "state": "MI", "zip": "48214", "current": True}]),
         None, None, "Authorized by DPSCD Jul 2025. 3-year contract."),
        ("macdowell", "MacDowell Preparatory Academy", "school", None,
         j([{"street": "18551 Ryan Road", "city": "Detroit", "state": "MI", "zip": "48234", "current": True}]),
         None, None, "Entity #82747. 3% math proficiency."),
        ("purpose-group", "The Purpose Group LLC", "entity", None,
         j([{"street": "1968 Severn Road", "city": "Grosse Pointe Woods", "state": "MI", "zip": "48236", "current": True}]),
         None, None, "LARA 803295082. CMO. 72.67% management fee extraction."),
        ("purpose-foundation", "Purpose Foundation", "entity", None,
         j([{"street": "1968 Severn Road", "city": "Grosse Pointe Woods", "state": "MI", "zip": "48236", "current": True}]),
         None, None, "LARA 803294855. Banks president, Holland sec/treas."),
        ("banks-strategy", "Banks Strategy & Consultants LLC", "entity", None,
         j([{"street": "1968 Severn Road", "city": "Grosse Pointe Woods", "state": "MI", "zip": "48236", "current": True}]),
         None, None, "LARA 802070120. Receives campaign payments from judges."),

        # -- Agencies --
        ("mde", "Michigan Department of Education", "agency", None, None, None, None, "FOIA responded Sep 25."),
        ("dpscd", "Detroit Public Schools Community District", "agency", None, None, None, None, "Charter authorizer for PCA."),
        ("usps-oig", "USPS Office of Inspector General", "agency", None, None, None, None, "Cases #174517, #202990, #208322."),
        ("fbi-detroit", "FBI Detroit Field Office", "agency", None, None, None, None, "Federal referral Sep 22."),
        ("doe-oig", "DOE Office of Inspector General", "agency", None, None, None, None, "Federal referral Sep 22."),
        ("jtc", "Judicial Tenure Commission", "agency", None, None, None, None, "5 complaints filed."),
        ("state-bar", "State Bar of Michigan", "agency", None, None, None, None, "UPL complaint filed Aug 31."),
        ("mi-ag", "Michigan Attorney General", "agency", None, None, None, None, "Referral Sep 9."),
        ("lara", "LARA", "agency", None, None, None, None, "Michigan Dept of Licensing and Regulatory Affairs."),
        ("wayne-foc", "Wayne County FOC", "agency", None, None, None, None, "Family court operations."),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES (?,?,?,?,?,?,?,?)",
        entities
    )

    # ============================================================
    # CASES
    # ============================================================
    cases = [
        ("2026-4301-CZ", "ingham-30th", "judge-stokes", "Mok v. Smith et al.", "civil", "2026-09-04", "default-pending", None),
        ("2026-4349-CZ", "ingham-30th", "judge-stokes", "Mok v. Banks", "civil", "2026-09-01", "default-pending", None),
        ("26-4432-PP", "ingham-30th", "judge-koenig", "Mitchell v. S. Smith", "ppo-domestic", "2026-09-15", "active", "Reasonable cause found ~Sep 20."),
        ("26-4433-PH", "ingham-30th", "judge-koenig", "Mitchell v. M. Smith", "ppo-harassment", "2026-09-15", "active", None),
        ("26-4434-PH", "ingham-30th", "judge-koenig", "Mitchell v. S.R. Smith", "ppo-harassment", "2026-09-15", "active", None),
        ("26-4435-PH", "ingham-30th", "judge-koenig", "Mitchell v. Banks", "ppo-harassment", "2026-09-15", "active", None),
        ("26-4436-PH", "ingham-30th", "judge-koenig", "Mitchell v. L. Smith", "ppo-harassment", "2026-09-15", "active", None),
        ("26-108221-DC", "wayne-3rd", "judge-triplett", "Mitchell v. Smith", "custody", None, "active", "FOC Oct 7, Triplett Oct 9."),
        ("26-47542", "ed-mich-bk", None, "In re Marquita Smith", "bankruptcy", None, "active", "Trustee Sandweiss."),
        ("26-49404-lsg", "ed-mich-bk", None, "In re Simone Smith", "bankruptcy", None, "active", "Trustee Moran. Ch.13→Ch.7 conversion."),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO cases (id, court, judge, caption, case_type, filed_date, status, notes) VALUES (?,?,?,?,?,?,?,?)",
        cases
    )

    # ============================================================
    # CASE PARTIES
    # ============================================================
    parties = [
        ("2026-4301-CZ", "mok-kevin", "plaintiff"),
        ("2026-4301-CZ", "smith-shayla", "defendant"),
        ("2026-4301-CZ", "smith-leon", "defendant"),
        ("2026-4301-CZ", "smith-marquita", "defendant"),
        ("2026-4301-CZ", "smith-simone", "defendant"),
        ("2026-4349-CZ", "mok-kevin", "plaintiff"),
        ("2026-4349-CZ", "banks-brian", "defendant"),
        ("26-4432-PP", "mitchell-dasean", "petitioner"),
        ("26-4432-PP", "smith-shayla", "respondent"),
        ("26-4432-PP", "mok-kevin", "witness"),
        ("26-4432-PP", "mok-kevin", "expert"),
        ("26-4433-PH", "mitchell-dasean", "petitioner"),
        ("26-4433-PH", "smith-marquita", "respondent"),
        ("26-4434-PH", "mitchell-dasean", "petitioner"),
        ("26-4434-PH", "smith-simone", "respondent"),
        ("26-4435-PH", "mitchell-dasean", "petitioner"),
        ("26-4435-PH", "banks-brian", "respondent"),
        ("26-4436-PH", "mitchell-dasean", "petitioner"),
        ("26-4436-PH", "smith-leon", "respondent"),
        ("26-108221-DC", "mitchell-dasean", "petitioner"),
        ("26-108221-DC", "smith-shayla", "respondent"),
        ("26-108221-DC", "mok-kevin", "representative"),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES (?,?,?)",
        [(c, e, r) for c, e, r in parties]
    )

    # ============================================================
    # KEY EVENTS (timeline)
    # ============================================================
    events = [
        ("2026-08-29", "Kevin visits PCA on DaSean's behalf",
         "Banks personally denies access, claims to be an attorney. DaSean visits separately with police escort — Banks speaks to officers privately, police escort DaSean off property.",
         j(["2026-4349-CZ", "26-4435-PH"]), j(["mok-kevin", "banks-brian", "mitchell-dasean"]),
         "Witness testimony, police records", "Triggering event for civil case."),

        ("2026-09-02", "Leon assaults DaSean; Shayla removes children",
         "Leon physically assaults DaSean at XXXX Cornerstone Blvd. Ring camera captures assault with timestamp and geolocation. While Leon assaults DaSean, Shayla removes the children from the location.",
         j(["26-4436-PH", "26-4432-PP", "2026-4301-CZ", "26-108221-DC"]),
         j(["smith-leon", "mitchell-dasean", "smith-shayla"]),
         "Ring camera video", "Central event. Assault + child removal."),

        ("2026-09-02", "Shayla coordinates pickup via texts to Deanna and Sahana",
         "Text messages show Shayla coordinating the pickup ahead of time, completely leaving DaSean out. Pre-planned removal, not spontaneous.",
         j(["26-4432-PP", "26-108221-DC"]), j(["smith-shayla"]),
         "Text messages (from Shayla's emergency custody filing)", "Proves premeditation of child removal."),

        ("2026-09-03", "Emergency filings — Wayne County",
         "Emergency custody motion filed. PPO petitions prepared.",
         j(["26-108221-DC"]), j(["mitchell-dasean", "mok-kevin"]),
         "Court records", None),

        ("2026-09-04", "Civil action filed — Mok v. Smith (4301-CZ)",
         None, j(["2026-4301-CZ"]), j(["mok-kevin"]), "Court records", None),

        ("2026-09-07", "Process server contacts Leon",
         "Leon acknowledges proceedings, states he will arrange for family to accept service.",
         j(["2026-4301-CZ"]), j(["smith-leon"]),
         "Process server declaration", "Establishes actual notice."),

        ("2026-09-09", "Banks tells police 'I am an attorney'",
         "DPD Report #26-0909-0176. Banks files retaliatory police report against Kevin.",
         j(["2026-4349-CZ", "26-4435-PH"]), j(["banks-brian"]),
         "DPD report", "UPL evidence."),

        ("2026-09-12", "Certified mail served to all 4 Smiths + RFAs sent",
         "First class + certified mail. 4 return receipts forged.",
         j(["2026-4301-CZ"]), j(["smith-shayla", "smith-leon", "smith-marquita", "smith-simone"]),
         "USPS tracking, certified mail records", "RFA 28-day clock starts."),

        ("2026-09-15", "PPO cluster filed — 5 cases",
         "DaSean files PPOs against Shayla, Marquita, Simone, Banks, Leon in Ingham County.",
         j(["26-4432-PP", "26-4433-PH", "26-4434-PH", "26-4435-PH", "26-4436-PH"]),
         j(["mitchell-dasean"]), "Court records", None),

        ("2026-09-05", "Shayla files retaliatory PPO against Kevin (Wayne County)",
         "Filed within days of Kevin's civil complaint and DaSean's PPO petitions. Proves awareness of proceedings while evading service.",
         j(["26-108221-DC"]), j(["smith-shayla", "mok-kevin"]),
         "Wayne County court records", "Retaliation + coordination evidence."),

        ("2026-09-05", "Shayla files emergency custody motion requesting Kevin be barred",
         "Emergency custody filing explicitly asks that Kevin Mok be kept away from DaSean and the children. 192-page exhibit packet filed. Coordinated with retaliatory PPO.",
         j(["26-108221-DC"]), j(["smith-shayla", "mok-kevin"]),
         "Wayne County court records", "Abuse of process evidence. Her own exhibits are party admissions."),

        ("2026-09-17", "Motion for Alternative Service filed",
         "Documents mail interception, address fraud, service evasion by Smith family.",
         j(["2026-4301-CZ", "2026-4349-CZ"]), j(["mok-kevin"]),
         "Court records", None),

        ("2026-09-17", "Leon texts Kevin: 'Good luck' + 'Will see you in court'",
         "Actual notice confirmed via text message.",
         j(["26-4436-PH", "2026-4301-CZ"]), j(["smith-leon", "mok-kevin"]),
         "iPhone screenshots", "Confirms notice of all proceedings."),

        ("2026-09-18", "Multi-channel service blast on Banks",
         "Certified restricted delivery, first class x2, fax (PCA), email.",
         j(["26-4435-PH", "2026-4349-CZ"]), j(["banks-brian"]),
         "Service affidavit", None),

        ("2026-09-20", "Koenig finds reasonable cause on domestic PPO (26-4432-PP)",
         "Ex parte PPO order issued.",
         j(["26-4432-PP"]), j(["judge-koenig", "smith-shayla"]),
         "Court order", "First judicial finding."),

        ("2026-09-22", "Federal Master Packet submitted to 8 agencies",
         "FBI, USAO, USPS OIG, DOE OIG, IRS CI, FEC, State Bar, JTC.",
         None, j(["mok-kevin"]),
         "Email/fax/mail receipts", "243 pages."),

        ("2026-09-25", "MDE FOIA response received",
         "20 files. Confirms Feb 2022 investigation, MOECS HOLD, 2hr 24min cover-up, loophole.",
         None, j(["mde"]),
         "MDE FOIA Response", "Layer 2 evidence. Smoking gun on credentialing."),

        ("2026-09-28", "Spoliation Wave 1 mailed — 19 pieces",
         "First class + PS Form 3665. Defendants, entities, Miller, Yancey, Moreland.",
         j(["2026-4301-CZ", "2026-4349-CZ"]), None,
         "PS Form 3665", "Preservation duty triggered."),

        ("2026-09-29", "PPO Hearing — all 5 cases — Koenig",
         "1:30 PM, Courtroom #4, 313 W Kalamazoo, Lansing.",
         j(["26-4432-PP", "26-4433-PH", "26-4434-PH", "26-4435-PH", "26-4436-PH"]),
         j(["mitchell-dasean", "mok-kevin", "judge-koenig"]),
         None, "FIRST TIME IN FRONT OF A JUDGE."),
    ]

    conn.executemany(
        "INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES (?,?,?,?,?,?,?)",
        events
    )

    # ============================================================
    # EVIDENCE ITEMS
    # ============================================================
    ev = [
        ("ring-camera-sep2", "Ring camera video — Sep 2 assault", "video",
         "Ring camera at XXXX Cornerstone Blvd", None,
         "Leon assaults DaSean. Shayla removes children. Timestamped, geo-located.",
         "2026-09-02", j(["smith-leon", "mitchell-dasean", "smith-shayla"]),
         j(["26-4436-PH", "26-4432-PP", "2026-4301-CZ"]),
         "Ring timestamp + geolocation", None),

        ("ichat-banks", "ICHAT printout — Banks SID 2029469K", "public-record",
         "Michigan ICHAT", None,
         "9 felony convictions with dates, charges, dispositions.",
         "2026-09-20", j(["banks-brian"]),
         j(["2026-4349-CZ", "26-4435-PH"]),
         "State criminal records system", None),

        ("state-bar-search", "State Bar of Michigan search — no record", "public-record",
         "State Bar of Michigan", None,
         "Brian Banks: no record of bar admission.",
         None, j(["banks-brian"]),
         j(["2026-4349-CZ", "26-4435-PH"]),
         "State Bar website screenshot", None),

        ("forged-green-cards", "Forged certified mail return receipts", "document",
         "USPS certified mail return receipts", None,
         "4 return receipts signed with forged signatures. All same hand. Consistent with Leon's writing.",
         "2026-08-21", j(["smith-leon"]),
         j(["2026-4301-CZ", "26-4436-PH"]),
         "Handwriting comparison vs Wayne ROD authenticated signatures", None),

        ("leon-texts-sep17", "Text messages Leon ↔ Kevin (Sep 16-17)", "text-message",
         "iPhone screenshots", None,
         "Leon: 'Good luck' + 'Do not text me again. Will see you in court.'",
         "2026-09-17", j(["smith-leon", "mok-kevin"]),
         j(["26-4436-PH", "2026-4301-CZ"]),
         "iPhone screenshot with metadata", None),

        ("dpd-report-sep9", "DPD Report #26-0909-0176", "public-record",
         "Detroit Police Department", None,
         "Banks told officers 'I am an attorney.' Banks filed retaliatory report against Kevin.",
         "2026-09-09", j(["banks-brian", "mok-kevin"]),
         j(["2026-4349-CZ", "26-4435-PH"]),
         "Police report", None),

        ("shayla-texts-deanna-sahana", "Shayla's texts to Deanna and Sahana coordinating Sep 2 pickup", "text-message",
         "Shayla's emergency custody filing exhibits (192 pages)", None,
         "Texts show Shayla coordinating child pickup ahead of time, completely leaving DaSean out. Pre-planned removal.",
         "2026-09-02", j(["smith-shayla"]),
         j(["26-4432-PP", "26-108221-DC"]),
         "Party admission — Shayla filed these herself as exhibits", "Shayla's own sworn evidence."),

        ("shayla-192-page-filing", "Shayla's 192-page emergency custody exhibit packet", "document",
         "Wayne County court file — 26-108221-DC", None,
         "Emergency custody filing with 192 pages of exhibits. Explicitly requests Kevin Mok be barred. Contains text messages that are party admissions.",
         "2026-09-05", j(["smith-shayla"]),
         j(["26-108221-DC"]),
         "Court-filed document", "Her own exhibits prove coordination and premeditation."),

        ("mde-foia-response", "MDE FOIA Response — 20 files", "document",
         "Michigan Department of Education", "bluegate-tenancy/02-evidence/mde-foia-sep25/",
         "Feb 2022 investigation, MOECS HOLD, 2hr 24min cover-up, loophole, 7-month gap to admin cert.",
         "2026-09-25", j(["mde", "banks-brian", "schmiedeknecht-katie"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response", None),

        ("ps3665-wave1", "PS Form 3665 — Wave 1 (19 pieces)", "document",
         "USPS post office", "PRINT_RUN_SEP28/PS3665_WAVE1_FILLED.pdf",
         "Proof of mailing for spoliation + demand letters. Court-admissible under MCR 2.107(C)(3).",
         "2026-09-28", None,
         j(["2026-4301-CZ", "2026-4349-CZ"]),
         "USPS postmark", None),

        ("rod-dresden-qcd", "Wayne County ROD — Dresden St QCD", "public-record",
         "Wayne County Register of Deeds", None,
         "Doc# 2025200597. Leon → Leon+Marquita QCD Jun 24, 2025. Same day $68K mortgage (Doc# 2025201292). 6 days before Marquita BK.",
         "2025-06-24", j(["smith-leon", "smith-marquita"]),
         j(["2026-4301-CZ"]),
         "Wayne County ROD certified", None),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity, notes) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        ev
    )

    # ============================================================
    # HEARINGS
    # ============================================================
    hearings = [
        ("ppo-hearing-sep29", j(["26-4432-PP", "26-4433-PH", "26-4434-PH", "26-4435-PH", "26-4436-PH"]),
         "2026-09-29", "13:30", "judge-koenig", "Courtroom #4",
         "313 W. Kalamazoo St, Lansing, MI 48933",
         "ppo", "scheduled", None, "All 5 cases consolidated. DaSean present + Kevin as witness/expert."),

        ("foc-oct7", j(["26-108221-DC"]),
         "2026-10-07", None, "referee-biggar", None, None,
         "foc", "scheduled", None, "FOC hearing. Bring PPO orders from Koenig."),

        ("triplett-oct9", j(["26-108221-DC"]),
         "2026-10-09", "12:00", "judge-triplett", "Zoom", None,
         "motion", "scheduled", None, "Custody + GAL + venue transfer. Zoom hearing."),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO hearings (id, case_ids, date, time, judge_id, courtroom, court_address, hearing_type, status, outcome, notes) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        hearings
    )

    # ============================================================
    # KEY RELATIONSHIPS
    # ============================================================
    rels = [
        ("banks-brian", "holland-joseph", "co-owner", "JTWRS, Newcastle Rd. QCD June 2007.", "Wayne ROD"),
        ("banks-brian", "welch-tonesa", "family", "Half-nephew. OD Banks = both grandfathers.", "Both autobiographies"),
        ("banks-brian", "pca", "employer", "Superintendent.", "LARA/DPSCD"),
        ("banks-brian", "macdowell", "employer", "Superintendent since 2022.", "MDE FOIA"),
        ("banks-brian", "purpose-group", "owner", "Sole member.", "LARA"),
        ("banks-brian", "purpose-foundation", "board-member", "President + Director.", "LARA"),
        ("banks-brian", "banks-strategy", "owner", "Sole member.", "LARA"),
        ("banks-brian", "judge-miller", "board-member", "Miller is PCA Board Chair.", "DPSCD/PCA records"),
        ("banks-brian", "judge-yancey", "board-member", "Yancey is MacDowell Board Chair.", "DPSCD"),
        ("banks-brian", "perkins-todd", "attorney", "Perkins represents Banks.", "Court records"),
        ("holland-joseph", "purpose-foundation", "board-member", "Secretary + Treasurer.", "LARA"),
        ("smith-shayla", "mitchell-dasean", "family", "Ex-partner. Mother of Sahana and Allanna.", None),
        ("smith-leon", "smith-marquita", "family", "Married.", None),
        ("smith-leon", "smith-shayla", "family", "Father and daughter.", None),
        ("smith-simone", "smith-shayla", "family", "Sisters (or sister-in-law).", None),
        ("mok-kevin", "mitchell-dasean", "family", "Best friends. Fellow veterans. NOT biological brothers.", None),
        ("perkins-todd", "judge-perkins-sean", "family", "Brothers.", "Public record"),
        ("judge-yancey", "banks-strategy", "campaign-payment", "$383.82 campaign payment to Banks Strategy.", "TransparencyUSA"),
        ("judge-sabree-aliyah", "sabree-eric", "family", "Father and daughter.", "Public record"),
    ]

    conn.executemany(
        "INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES (?,?,?,?,?)",
        rels
    )

    # ============================================================
    # AGENCY REFERRALS
    # ============================================================
    referrals = [
        ("oig-174517", "usps-oig", "2026-09-08", "174517", "Leon Smith mail interception", "active", None, None),
        ("oig-202990", "usps-oig", "2026-09-08", "202990", "Leon Smith mail interception", "active", None, None),
        ("oig-208322", "usps-oig", "2026-09-17", "208322", "Leon Smith forgery supplement", "active", None, None),
        ("fbi-sep22", "fbi-detroit", "2026-09-22", None, "Banks network — RICO pattern, public corruption", "sent", None, None),
        ("doe-oig-sep22", "doe-oig", "2026-09-22", None, "Banks — federal education fraud, credential forgery", "sent", None, None),
        ("jtc-miller", "jtc", "2026-08-31", None, "Judge Cylenthia Miller — PCA Board Chair", "active", None, None),
        ("jtc-yancey", "jtc", "2026-08-31", None, "Judge Tenisha Yancey — MacDowell Board Chair", "active", None, None),
        ("bar-upl", "state-bar", "2026-08-31", None, "Banks UPL — claims J.D., no bar record", "active", None, None),
        ("ag-sep9", "mi-ag", "2026-09-09", None, "Banks referral — AG Moreland", "sent", None, None),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO agency_referrals (id, agency_id, date_sent, case_number, subject, status, response_date, notes) VALUES (?,?,?,?,?,?,?,?)",
        referrals
    )

    # ============================================================
    # FOIA REQUESTS
    # ============================================================
    foias = [
        ("foia-mde-sep21", "mde", "2026-09-21", "2026-09-28", "Banks credentials, MacDowell investigation, admin cert", "responded", "2026-09-25", "20 files received. Smoking gun.", "bluegate-tenancy/02-evidence/mde-foia-sep25/"),
        ("foia-dpscd-sep22", "dpscd", "2026-09-22", "2026-10-13", "PCA charter authorization, board minutes, background checks", "sent", None, "#2627-060", None),
    ]

    conn.executemany(
        "INSERT OR REPLACE INTO foia_requests (id, agency_id, date_sent, due_date, subject, status, response_date, response_notes, file_path) VALUES (?,?,?,?,?,?,?,?,?)",
        foias
    )

    conn.commit()

    # Print summary
    for table in ["entities", "cases", "case_parties", "events", "evidence",
                  "hearings", "relationships", "agency_referrals", "foia_requests"]:
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count} rows")

    conn.close()
    print(f"\nDatabase created: {DB_PATH}")

if __name__ == "__main__":
    main()
