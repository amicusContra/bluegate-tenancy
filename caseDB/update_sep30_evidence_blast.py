"""
Sep 30 Evidence Blast — loads proof-packet-sep30 files, MDE FOIA,
Wayne ROD instruments, Banks credential evidence, and all Sep 29-30
drafted documents into caseDB.

Run: python update_sep30_evidence_blast.py
"""
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caseDB.sqlite")

def j(lst):
    return json.dumps(lst) if lst else None

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")
    conn.row_factory = sqlite3.Row

    # ============================================================
    # EVIDENCE — Proof Packet Files (staged Sep 30)
    # Each maps to a real file in proof-packet-sep30/
    # ============================================================
    PP = r"C:\Users\mokke\Documents\cases\evidence\proof-packet-sep30"

    proof_packet_evidence = [
        # (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
        ("mdoc-holland-443789", "MDOC OTIS — Holland #443789", "public-record",
         "Michigan MDOC OTIS",
         os.path.join(PP, "01_MDOC_HOLLAND_443789.png"),
         "Holland MDOC #443789. Discharged WITHOUT IMPROVEMENT May 2024. Joseph Antione Williams alias.",
         "2024-05-01",
         j(["holland-joseph"]),
         j(["2026-4349-CZ"]),
         "MDOC OTIS public search"),

        ("lara-purpose-foundation-articles", "LARA — Purpose Foundation Articles of Incorporation", "public-record",
         "LARA Entity #803294855",
         os.path.join(PP, "02_LARA_PURPOSE_FOUNDATION_ARTICLES.pdf"),
         "Purpose Foundation articles filed Dec 9, 2024. Banks president, Holland sec/treas. Same home address.",
         "2024-12-09",
         j(["banks-brian", "holland-joseph", "purpose-foundation"]),
         j(["2026-4349-CZ"]),
         "LARA certified filing"),

        ("lara-purpose-foundation-entity", "LARA — Purpose Foundation Entity Detail Screenshot", "public-record",
         "LARA Entity Search",
         os.path.join(PP, "02b_LARA_PURPOSE_FOUNDATION_ENTITY.png"),
         "LARA entity detail page showing Purpose Foundation active status, registered agent, officers.",
         "2026-09-14",
         j(["purpose-foundation"]),
         j(["2026-4349-CZ"]),
         "LARA website screenshot"),

        ("lara-purpose-foundation-annual", "LARA — Purpose Foundation 2026 Annual Report", "public-record",
         "LARA Entity #803294855",
         os.path.join(PP, "02c_LARA_PURPOSE_FOUNDATION_ANNUAL_2026.pdf"),
         "2026 annual report confirming current officers: Banks president, Holland secretary/treasurer.",
         "2026-01-01",
         j(["banks-brian", "holland-joseph", "purpose-foundation"]),
         j(["2026-4349-CZ"]),
         "LARA annual filing"),

        ("lara-purpose-group-articles", "LARA — Purpose Group LLC Articles of Organization", "public-record",
         "LARA Entity #803295082",
         os.path.join(PP, "03_LARA_PURPOSE_GROUP_ARTICLES.pdf"),
         "Purpose Group LLC articles filed Nov 14, 2024. Banks sole member. CMO taking 72.67% of school revenue.",
         "2024-11-14",
         j(["banks-brian", "purpose-group"]),
         j(["2026-4349-CZ"]),
         "LARA certified filing"),

        ("rod-severn-property", "Wayne ROD — 1968 Severn Property Record", "public-record",
         "Wayne County Register of Deeds",
         os.path.join(PP, "04_WAYNE_ROD_1968_SEVERN_PROPERTY.pdf"),
         "Full property record for 1968 Severn Rd, Grosse Pointe Woods. Shows chain of title.",
         None,
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "Wayne County ROD certified"),

        ("rod-newcastle-qcd", "Wayne ROD — Newcastle QCD #2007402847", "public-record",
         "Wayne County Register of Deeds",
         os.path.join(PP, "05a_WAYNE_ROD_NEWCASTLE_QCD_2007402847.pdf"),
         "Jun 2007 QCD: Banks → Banks + Holland JTWRS, 21553 Newcastle Rd. $1 consideration. Proves 20-year domestic unit.",
         "2007-06-01",
         j(["banks-brian", "holland-joseph"]),
         j(["2026-4349-CZ"]),
         "Wayne County ROD Instrument #2007402847"),

        ("rod-severn-trust-qcd", "Wayne ROD — Severn Trust Transfer QCD 2024", "public-record",
         "Wayne County Register of Deeds",
         os.path.join(PP, "05b_WAYNE_ROD_SEVERN_TRUST_QCD_2024.pdf"),
         "Aug 2024 QCD: Banks → Brian Banks Living Trust. 1968 Severn. Asset protection move.",
         "2024-08-01",
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "Wayne County ROD Instrument #2024223261"),

        ("rod-trust-certificate", "Wayne ROD — Trust Certificate (Holland Successor)", "public-record",
         "Wayne County Register of Deeds",
         os.path.join(PP, "05c_WAYNE_ROD_TRUST_CERTIFICATE_HOLLAND.pdf"),
         "Nov 7, 2025 Trust Certificate. Holland is 1st Successor Trustee of Brian Banks Living Trust.",
         "2025-11-07",
         j(["banks-brian", "holland-joseph"]),
         j(["2026-4349-CZ"]),
         "Wayne County ROD Instrument #2025307266"),

        ("rod-tax-lien-newcastle", "Wayne ROD — Tax Lien at Newcastle (Banks at Holland address)", "public-record",
         "Wayne County Register of Deeds",
         os.path.join(PP, "05d_WAYNE_ROD_TAX_LIEN_NEWCASTLE_BANKS.pdf"),
         "Banks has tax lien at 21553 Newcastle — Holland's address. Proves cohabitation.",
         None,
         j(["banks-brian", "holland-joseph"]),
         j(["2026-4349-CZ"]),
         "Wayne County ROD Instrument"),

        ("sos-pac-committee", "MI SOS — PAC Committee Info (#517977)", "public-record",
         "Michigan Secretary of State Campaign Finance",
         os.path.join(PP, "06a_SOS_PAC_COMMITTEE.png"),
         "Banks Strategy PAC #517977 committee registration page.",
         None,
         j(["banks-brian", "banks-strategy"]),
         j(["2026-4349-CZ"]),
         "SOS website screenshot"),

        ("sos-pac-late-fees", "MI SOS — PAC Late Filing Fees", "public-record",
         "Michigan Secretary of State Campaign Finance",
         os.path.join(PP, "06b_SOS_PAC_LATE_FEES.png"),
         "PAC #517977 late filing fee history. Chronic non-compliance.",
         None,
         j(["banks-brian", "banks-strategy"]),
         j(["2026-4349-CZ"]),
         "SOS website screenshot"),

        ("sos-pac-members", "MI SOS — PAC Members & Addresses", "public-record",
         "Michigan Secretary of State Campaign Finance",
         os.path.join(PP, "06c_SOS_PAC_MEMBERS.png"),
         "PAC #517977 member list with addresses. Banks at 1968 Severn.",
         None,
         j(["banks-brian", "banks-strategy"]),
         j(["2026-4349-CZ"]),
         "SOS website screenshot"),

        ("sos-pac-filings", "MI SOS — PAC Filing History", "public-record",
         "Michigan Secretary of State Campaign Finance",
         os.path.join(PP, "06d_SOS_PAC_FILINGS.png"),
         "PAC #517977 filing history — when reports were (or weren't) filed.",
         None,
         j(["banks-brian", "banks-strategy"]),
         j(["2026-4349-CZ"]),
         "SOS website screenshot"),

        ("ichat-holland", "ICHAT — Holland Full Criminal Record", "public-record",
         "Michigan ICHAT",
         os.path.join(PP, "10_ICHAT_HOLLAND_FULL.pdf"),
         "Holland criminal history. Multiple convictions. MDOC #443789.",
         "2026-09-14",
         j(["holland-joseph"]),
         j(["2026-4349-CZ"]),
         "State criminal records system"),

        ("regan-v-banks", "Regan v. Banks — SOS CFR Complaint (31 pages)", "public-record",
         "Michigan Secretary of State",
         os.path.join(PP, "11_REGAN_V_BANKS_SOS_COMPLAINT.pdf"),
         "SOS campaign finance complaint against Banks. 31 pages. Violations documented.",
         None,
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "SOS public record"),

        ("banks-demand-pca", "Banks Demand Letter to PCA", "document",
         "Filed with court",
         os.path.join(PP, "banksDeamndPCA.pdf"),
         "Banks demand letter regarding PCA access. Court exhibit.",
         "2026-09-01",
         j(["banks-brian", "mok-kevin"]),
         j(["2026-4349-CZ", "26-4435-PH"]),
         "Court filing"),

        ("mok-banks-ppo", "Kevin PPO Petition vs Banks", "document",
         "Ingham County 30th Circuit",
         os.path.join(PP, "mokBanksPPO.pdf"),
         "Kevin's PPO petition against Banks. Filed before DaSean's return.",
         "2026-09-15",
         j(["mok-kevin", "banks-brian"]),
         j(["26-ppo-mok-banks"]),
         "Court filing"),

        ("parentage-confessions", "Parentage Confessions — Shayla Complaint Extract", "document",
         "Wayne County 26-108221-DC",
         os.path.join(PP, "parentageConfessions03.pdf"),
         "Pages from Shayla complaint confirming AOP. Para 6: Paternity established through Affidavit of Parentage.",
         "2026-09-05",
         j(["smith-shayla", "mitchell-dasean"]),
         j(["26-108221-DC", "26-4432-PP"]),
         "Court-filed document — party admission"),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO evidence
           (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        proof_packet_evidence
    )
    print(f"  Proof packet: {len(proof_packet_evidence)} evidence items loaded")

    # ============================================================
    # EVIDENCE — MDE FOIA Sub-items
    # ============================================================
    MDE = r"C:\Users\mokke\Downloads\MDE_FOIA"

    mde_evidence = [
        ("mde-investigation-letter", "MDE Investigation Letter for Banks", "document",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "1 - Investigation", "Investigation Letter for Banks.pdf"),
         "Formal MDE investigation letter regarding Banks credential compliance at MacDowell.",
         "2022-02-01",
         j(["mde", "banks-brian", "macdowell"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),

        ("mde-moecs-hold", "MDE MOECS Admin Permit HOLD for Banks", "public-record",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "1 - Investigation", "MOECS Admin Permit Hold for Banks.png"),
         "MOECS system showing HOLD status on Banks admin permit. Credential not valid.",
         "2022-02-01",
         j(["mde", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),

        ("mde-rep-blank", "MDE REP — Banks Blank Credential", "public-record",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "1 - Investigation", "REP for Banks.png"),
         "MDE Registry of Educational Personnel showing Banks has blank/no valid credential.",
         None,
         j(["mde", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),

        ("mde-eem-banks", "MDE EEM — Banks Employment Record", "public-record",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "1 - Investigation", "EEM for Banks.png"),
         "MDE Educator Evaluation Module record for Banks.",
         None,
         j(["mde", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),

        ("mde-educator-report", "MDE Educator Report Form for Banks", "document",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "1 - Investigation", "Educator Report Form for Banks.pdf"),
         "Official MDE educator report form. Used to document credential investigation findings.",
         None,
         j(["mde", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),

        ("mde-schmiedeknecht-email", "MDE Katie Schmiedeknecht — No Investigation Email", "email",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "2 - Cleared", "Katie_s email to district of no investigation.msg"),
         "Katie Schmiedeknecht email telling district no investigation needed — the loophole. 2hr 24min cover-up.",
         "2022-02-01",
         j(["schmiedeknecht-katie", "mde", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),

        ("mde-non-placement", "MDE Non-Placement Email", "email",
         "MDE FOIA Response",
         os.path.join(MDE, "MacDowell Preparatory Academy", "2 - Cleared", "Email of non-placement.msg"),
         "MDE email regarding non-placement determination for Banks.",
         None,
         j(["mde", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "Government FOIA response"),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO evidence
           (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        mde_evidence
    )
    print(f"  MDE FOIA: {len(mde_evidence)} evidence items loaded")

    # ============================================================
    # EVIDENCE — MDE Financial Audits (MacDowell 82747)
    # ============================================================
    AUDIT = os.path.join(MDE, "Audits", "Audits")

    audit_years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    audit_evidence = []
    for yr in audit_years:
        if yr == 2021:
            fname = f"82747 FS  - {yr}.pdf"
        elif yr in (2024, 2025):
            fname = f"82747fs - {yr}.pdf"
        elif yr == 2022:
            fname = f"82747 FS - {yr}.pdf"
        else:
            fname = f"82747 FS - {yr}.pdf"

        fpath = os.path.join(AUDIT, fname)
        if os.path.exists(fpath):
            audit_evidence.append((
                f"mde-audit-macdowell-{yr}",
                f"MacDowell Financial Audit FY{yr} (Entity #82747)",
                "financial",
                "MDE FOIA Response",
                fpath,
                f"MacDowell Preparatory Academy (Entity #82747) financial statement audit for fiscal year {yr}. Shows Purpose Group management fee extraction.",
                f"{yr}-06-30",
                j(["macdowell", "purpose-group", "banks-brian"]),
                j(["2026-4349-CZ"]),
                "MDE FOIA — CPA audited financial statements"
            ))

    if audit_evidence:
        conn.executemany(
            """INSERT OR REPLACE INTO evidence
               (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            audit_evidence
        )
    print(f"  MDE Audits: {len(audit_evidence)} financial audit files loaded")

    # ============================================================
    # DOCUMENTS — Filed/Drafted filings
    # ============================================================
    FILING = r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready"

    documents = [
        ("reply-banks-linexline-sep29",
         "Reply to Banks — Line-by-Line Sep 29",
         "demand-letter",
         os.path.join(FILING, "REPLY_BANKS_LINEXLINE_SEP29.md"),
         j(["2026-4349-CZ", "26-ppo-mok-banks"]),
         "2026-09-29", "banks-brian", "served",
         "Point-by-point response to Banks cease-and-desist. Credential exposure."),

        ("reply-all-three-sep29",
         "Reply to Banks + Leon + Shayla — Sep 29 Late",
         "demand-letter",
         os.path.join(FILING, "REPLY_ALL_THREE_SEP29_LATE.md"),
         j(["2026-4301-CZ", "2026-4349-CZ"]),
         "2026-09-29", "banks-brian", "served",
         "Replies to all 3 defendants. 7 admissions extracted."),

        ("email-6am-sep30",
         "6 AM Email — PPO Hearing + Appeals Announcement",
         "demand-letter",
         os.path.join(FILING, "EMAIL_6AM_SEP30.md"),
         j(["26-ppo-mok-banks", "26-4432-PP", "26-4435-PH", "26-4436-PH"]),
         "2026-09-30", "banks-brian", "served",
         "PPO hearing notice + appeal announcements + Shayla AOP demand."),

        ("email-defamation-dare-sep30",
         "Defamation Dare — Banks v. Dr. Mok Trap",
         "demand-letter",
         os.path.join(FILING, "EMAIL_DEFAMATION_DARE_SEP30.md"),
         j(["2026-4349-CZ", "26-ppo-mok-banks"]),
         "2026-09-30", "banks-brian", "served",
         "Invites Banks to sue for defamation. Discovery trap — must prove bar admission."),

        ("email-part2-tonight-sep29",
         "You Thought Today Was the End — Sep 29 Night",
         "demand-letter",
         os.path.join(FILING, "EMAIL_PART2_TONIGHT_SEP29.md"),
         j(["2026-4301-CZ", "2026-4349-CZ", "26-ppo-mok-banks"]),
         "2026-09-29", "banks-brian", "served",
         "New chain. PPO + appeals + expansion warning."),

        ("cross-case-strategy-sep30",
         "Cross-Case Strategy — 4301 ↔ 4349 Pipeline",
         "motion",
         os.path.join(FILING, "CROSS_CASE_STRATEGY_SEP30.md"),
         j(["2026-4301-CZ", "2026-4349-CZ"]),
         "2026-09-30", None, "drafted",
         "4301 builds evidence for 4349. Spoliation + witness notices."),

        ("case-4349-expansion-sep30",
         "4349 Expansion — Holland + Entities + Discovery 36-61",
         "motion",
         os.path.join(FILING, "CASE_4349_EXPANSION_SEP30.md"),
         j(["2026-4349-CZ"]),
         "2026-09-30", None, "drafted",
         "Adding Holland, Ellis, entities. 26 new discovery items."),

        ("email-banks-gloves-off-sep30",
         "Gloves Off — Banks Loses Kevin Protection",
         "demand-letter",
         os.path.join(FILING, "EMAIL_BANKS_GLOVES_OFF_SEP30.md"),
         j(["2026-4349-CZ"]),
         "2026-09-30", "banks-brian", "served",
         "Reveals full knowledge of Holland, trust, foundation, MDOC, PAC."),

        ("email-proof-packet-sep30",
         "Proof Packet — 27 Evidence Files to Banks",
         "demand-letter",
         os.path.join(FILING, "EMAIL_PROOF_PACKET_SEP30.md"),
         j(["2026-4349-CZ", "26-ppo-mok-banks"]),
         "2026-09-30", "banks-brian", "drafted",
         "9-section proof packet. MDOC, LARA, ROD, MDE, ICHAT, SOS, Regan."),

        ("banks-life-story-sep30",
         "Banks Life Story — 7-Chapter Comprehensive Profile",
         "exhibit",
         os.path.join(FILING, "BANKS_LIFE_STORY_SEP30.md"),
         j(["2026-4349-CZ"]),
         "2026-09-30", None, "drafted",
         "BMF family, criminal career, Holland partnership, credentials, state rep, school empire, unraveling."),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO documents
           (id, title, doc_type, file_path, case_ids, filed_date, filed_with, status, notes)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        documents
    )
    print(f"  Documents: {len(documents)} filings/emails loaded")

    # ============================================================
    # EVIDENCE — Banks Credential Chain
    # ============================================================
    credential_evidence = [
        ("banks-msu-jd", "Banks MSU J.D. — Never Bar Admitted", "public-record",
         "State Bar of Michigan + MSU Law",
         None,
         "Banks earned J.D. from Michigan State University College of Law. Felony convictions prevented bar admission. Has never been admitted to any state bar.",
         None,
         j(["banks-brian"]),
         j(["2026-4349-CZ", "26-ppo-mok-banks"]),
         "State Bar search negative + court records"),

        ("banks-bar-prep-fraud", "Banks Bar Prep Course — Fraudulent Loans", "financial",
         "Federal student loan records",
         None,
         "Banks took fraudulent loans for bar prep course he was ineligible to use due to felony bar exclusion.",
         None,
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "Federal loan records"),

        ("banks-walden-doctorate", "Banks Walden University Doctorate — No IRB Disclosures", "document",
         "Walden University dissertation",
         None,
         "Doctorate from Walden University. Dissertation lacks basic IRB disclosures. Holland may be interview subject.",
         None,
         j(["banks-brian", "holland-joseph"]),
         j(["2026-4349-CZ"]),
         "Published dissertation"),

        ("banks-dpd-attorney-claim", "Banks Tells DPD He Is An Attorney", "public-record",
         "DPD Report #26-0909-0176",
         None,
         "Banks told Detroit Police officers he is an attorney on Sep 9, 2026. He has a J.D. but is not bar-admitted. Knows the difference. MCL 450.681 UPL violation.",
         "2026-09-09",
         j(["banks-brian"]),
         j(["2026-4349-CZ", "26-4435-PH", "26-ppo-mok-banks"]),
         "Police report + State Bar negative search"),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO evidence
           (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        credential_evidence
    )
    print(f"  Credential chain: {len(credential_evidence)} evidence items loaded")

    # ============================================================
    # EVIDENCE — Holland PACER Bankruptcies
    # ============================================================
    pacer_evidence = [
        ("holland-bk1-09-46072", "Holland BK1 — Case 09-46072 (Ch.7)", "public-record",
         "PACER ED Mich Bankruptcy",
         None,
         "Holland BK1. Schedule A should show Newcastle at $65K. Schedule H should show Banks as codebtor. Need to pull schedules.",
         "2009-01-01",
         j(["holland-joseph", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "PACER federal court record"),

        ("holland-bk3-14-51632", "Holland BK3 — Case 14-51632 (Ch.7 Concealment)", "public-record",
         "PACER ED Mich Bankruptcy",
         None,
         "Holland BK3. Schedule A should show NONE (Newcastle concealed). Schedule H shows no codebtors (Banks erased). 18 USC 152 concealment.",
         "2014-01-01",
         j(["holland-joseph", "banks-brian"]),
         j(["2026-4349-CZ"]),
         "PACER federal court record"),

        ("banks-bk-06-55281", "Banks BK — Case 06-55281 Full Petition (55pp)", "public-record",
         "PACER ED Mich Bankruptcy",
         r"C:\Users\mokke\Documents\cases\evidence\pacer-indexed\banks_06-55281\06-55281_banks_petition_full_55pp.pdf",
         "Banks full bankruptcy petition. 55 pages. Includes schedules, assets, liabilities.",
         "2006-01-01",
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "PACER federal court record"),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO evidence
           (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        pacer_evidence
    )
    print(f"  PACER bankruptcies: {len(pacer_evidence)} evidence items loaded")

    # ============================================================
    # EVIDENCE — Additional vault items
    # ============================================================
    vault = r"C:\Users\mokke\Documents\cases\evidence"

    vault_evidence = [
        ("lara-banks-strategy-entity", "LARA — Banks Strategy & Consultants LLC", "public-record",
         "LARA Entity #802070120",
         os.path.join(vault, "banks-lara"),
         "Banks Strategy entity filings + 8 annual reports. Banks sole member. Receives judge campaign payments.",
         None,
         j(["banks-brian", "banks-strategy"]),
         j(["2026-4349-CZ"]),
         "LARA certified filing"),

        ("rod-analysis-banks-holland", "Wayne ROD Analysis — Banks-Holland Property Chain", "document",
         "ELRICK_SEP15 journalist packet",
         r"C:\Users\mokke\Documents\ELRICK_SEP15\12_HOLLAND_ICHAT\BANKS_HOLLAND_ROD_ANALYSIS.md",
         "420-line comprehensive analysis mapping every Wayne ROD instrument to Banks-Holland property transactions. Newcastle QCD, Severn transfers, trust certificates, tax liens.",
         "2026-09-15",
         j(["banks-brian", "holland-joseph"]),
         j(["2026-4349-CZ"]),
         "Wayne ROD instruments cross-referenced"),

        ("smith-bk-schedules-17-52263", "Smith Bankruptcy Schedules — 17-52263 (41pp)", "public-record",
         "PACER ED Mich Bankruptcy",
         os.path.join(vault, r"court-filings\smith-bankruptcy-schedules\17-52263_smith_schedules_41pp.pdf"),
         "Leon + Marquita Smith joint bankruptcy schedules. 41 pages. Assets, liabilities, income.",
         "2017-01-01",
         j(["smith-leon", "smith-marquita"]),
         j(["2026-4301-CZ"]),
         "PACER federal court record"),

        ("custody-shayla-originals", "Wayne County Custody — Shayla Original Filings", "document",
         "Wayne County 26-108221-DC",
         os.path.join(vault, r"court-filings\custody-26-108221"),
         "8 JPEG pages of Shayla original filings in custody case. Contains AOP confession at paragraph 6.",
         "2026-09-05",
         j(["smith-shayla"]),
         j(["26-108221-DC"]),
         "Court-filed document"),

        ("banks-severn-permits", "Building Permits — 1968 Severn", "public-record",
         "City of Grosse Pointe Woods",
         os.path.join(vault, r"banks-property\1968_severn_permits.pdf"),
         "Building permits for 1968 Severn Rd. Construction/renovation history.",
         None,
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "Municipal records"),

        ("banks-severn-tax", "Tax Records — 1968 Severn", "financial",
         "Wayne County Treasurer",
         os.path.join(vault, r"banks-property\1968_severn_tax.pdf"),
         "Tax records for 1968 Severn Rd. Assessment, payments, liens.",
         None,
         j(["banks-brian"]),
         j(["2026-4349-CZ"]),
         "County tax records"),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO evidence
           (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        vault_evidence
    )
    print(f"  Vault items: {len(vault_evidence)} evidence items loaded")

    # ============================================================
    # NEW ENTITY — DPD
    # ============================================================
    conn.execute(
        "INSERT OR IGNORE INTO entities (id, name, type, notes) VALUES (?,?,?,?)",
        ("dpd", "Detroit Police Department", "agency", "DPD Report #26-0909-0176. Banks claimed to be attorney.")
    )

    # ============================================================
    # FOIA — New requests
    # ============================================================
    foias = [
        ("foia-dpd-sep30", "dpd", "2026-09-30", "2026-10-07",
         "DPD FOIA — 4 police reports + all interactions re: Banks, PCA, Kevin Mok",
         "pending", None, None, None),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO foia_requests
           (id, agency_id, date_sent, due_date, subject, status, response_date, response_notes, file_path)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        foias
    )
    print(f"  FOIA requests: {len(foias)} added")

    # ============================================================
    # SERVICE LOG — Sep 29-30 email service
    # ============================================================
    email_service = [
        ("2026-4301-CZ", "banks-brian", "2026-09-29", "email", "bbanks@macdowellprep.com", None,
         "acknowledged", "Banks responded within minutes to demand email."),
        ("2026-4301-CZ", "smith-leon", "2026-09-29", "email", "oneomega1970@gmail.com", None,
         "acknowledged", "Leon replied with threats."),
        ("2026-4301-CZ", "smith-shayla", "2026-09-29", "email", "smith.shayla2013@yahoo.com", None,
         "acknowledged", "Shayla replied disputing service — confirming receipt."),
        ("2026-4349-CZ", "banks-brian", "2026-09-30", "email", "bbanks@macdowellprep.com", None,
         "acknowledged", "Banks replied to gloves-off email."),
    ]

    conn.executemany(
        """INSERT INTO service_log
           (case_id, entity_id, date, method, address, tracking, result, notes)
           VALUES (?,?,?,?,?,?,?,?)""",
        email_service
    )
    print(f"  Service log: {len(email_service)} email service entries added")

    conn.commit()

    # ============================================================
    # SUMMARY
    # ============================================================
    print(f"\n{'='*60}")
    print(f"EVIDENCE BLAST COMPLETE")
    print(f"{'='*60}")
    for table in ["entities", "cases", "case_parties", "events", "evidence",
                  "documents", "hearings", "relationships", "properties",
                  "service_log", "agency_referrals", "foia_requests"]:
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table:25} {count:>5} rows")

    conn.close()

if __name__ == "__main__":
    main()
