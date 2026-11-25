#!/usr/bin/env python3
"""Patch JTC print packets with missing ATTACHED exhibits."""
from pathlib import Path

DESKTOP = Path(r"C:\Users\mokke\Desktop\JTC_PRINT_PACKETS")
EXHIBITS_MARKER = "<!-- ============ EXHIBITS START ============ -->"


def osint_brief(letter: str) -> str:
    return f"""<div class="page-break"></div>
<div class="exhibit-label">EXHIBIT {letter} — BRIAN BANKS OSINT BRIEF (CONDENSED)</div>
<div class="exhibit-note">Open-Source Intelligence Brief v2 (September 1, 2026) — Condensed excerpt for print packet. Full 450-line version on file.</div>

<p><strong>Subject:</strong> Brian Roderick Banks<br>
<strong>Compiled by:</strong> Kevin Mok | August 30 – September 1, 2026<br>
<strong>Method:</strong> OSINT only — public records, LARA corporate filings, campaign finance (TransparencyUSA), court records, FBI wiretap affidavits, news archives, school financial documents.</p>

<h3>I. Identity</h3>
<p>Brian Roderick Banks is an eight-time convicted felon who presents himself publicly as &ldquo;Brian Banks, J.D., Ph.D.&rdquo; He is <strong>not licensed</strong> with the State Bar of Michigan and has never been admitted to practice law. He founded and operates Purpose Charter Academy (PCA) and MacDowell Preparatory Academy. Registered address for multiple entities: <strong>1968 Severn Road, Grosse Pointe Woods, MI 48236</strong> (Banks&rsquo; personal residence).</p>
<p>Banks resigned from the Michigan House of Representatives (District 1) in February 2017 after pleading guilty to loan fraud. He formed Banks Strategy &amp; Consultants, LLC eight days later. He is named as a defendant in <em>Kevin Mok v. Brian Banks</em>, Wayne County 3rd Circuit Court.</p>

<h3>II. Criminal &amp; Civil History</h3>
<table>
  <tr><th>Category</th><th>Detail</th></tr>
  <tr><td>Felony convictions (1998–2004)</td><td>Series of bad check and credit card fraud convictions; convicted as habitual offender</td></tr>
  <tr><td>2016–2017 loan fraud</td><td>Used fake pay stubs from IHI Attorneys to obtain $7,500 loan; pled guilty to misdemeanor Feb 2017; 3 felonies dropped; resigned from House</td></tr>
  <tr><td>2013 sexual harassment lawsuit</td><td>Tramaine Cotton (former aide) sued; settled $11,950; state paid $85,622 for Banks&rsquo; defense</td></tr>
  <tr><td>2016 FBI wiretap</td><td>Named 1 of 18 &ldquo;target subjects&rdquo; in towing corruption investigation; captured discussing MDOT bid-rigging with Gasper Fiore (convicted 2017); Banks never charged</td></tr>
  <tr><td>Civil judgments</td><td>$47,809.84 total since first election; 7 evictions; both cars repossessed; Outfront Media $17,000+ judgment</td></tr>
</table>

<h3>III. Entity Map (LARA)</h3>
<p>All Banks-connected entities registered at 1968 Severn Road, Grosse Pointe Woods:</p>
<table>
  <tr><th>Entity</th><th>LARA ID</th><th>Formed</th><th>Function</th></tr>
  <tr><td>Banks Strategy &amp; Consultants, LLC</td><td>802070120</td><td>Feb 2017</td><td>Consulting; $49K–59K tracked revenue</td></tr>
  <tr><td>Purpose Foundation</td><td>803294855</td><td>Dec 2024</td><td>501(c)(3) nonprofit; Banks sole director</td></tr>
  <tr><td>The Purpose Group, LLC</td><td>803295082</td><td>Nov 2024</td><td>Charter management org (CMO); 10–15% of per-pupil funding</td></tr>
  <tr><td>The Right Turn Project</td><td>—</td><td>2013</td><td>Dissolved by IRS 2019; ~$30K from no-fault opponents; never registered with MI AG</td></tr>
</table>
<p>Joseph Holland Jr. (Secretary/Treasurer, Purpose Foundation; Treasurer, Bank on Banks PAC) shares Banks&rsquo; home address. Bank on Banks PAC owes $14,500 in campaign finance fines (referred to AG May 2022).</p>

<h3>IV. School Connections</h3>
<p><strong>Purpose Charter Academy:</strong> Founded by Banks; Judge Cylenthia Miller serves as Board Chair. The Purpose Group LLC extracts management fees as CMO.</p>
<p><strong>MacDowell Preparatory Academy:</strong> Judge Tenisha Yancey serves as Board Chair. MacDowell check register (FY 2023–24) shows Banks paid himself <strong>$13,970</strong>, mostly labeled &ldquo;gift cards&rdquo;:</p>
<table>
  <tr><th>Date</th><th>Amount</th><th>Description</th></tr>
  <tr><td>08/08/2023</td><td>$1,890</td><td>Staff Gift Cards</td></tr>
  <tr><td>11/20/2023</td><td>$400</td><td>Gift cards for travel</td></tr>
  <tr><td>12/20/2023</td><td>$9,945</td><td>Staff gifts cards</td></tr>
  <tr><td>01/11/2024</td><td>$265</td><td>Reimbursement</td></tr>
  <tr><td>06/24/2024</td><td>$1,470</td><td>Staff Gift Cards for NCSC24</td></tr>
</table>
<p>Other suspicious MacDowell payments: $1,000 to &ldquo;Rafeal Camper&rdquo; (&ldquo;Prayers to you and your fam&rdquo;); $746 to Detroit Athletic Club; $900 to KJ Investment Group; $5,000 attorney retainer to Gregory M. Meihn.</p>

<h3>V. Campaign Finance</h3>
<table>
  <tr><th>Transaction</th><th>Amount</th><th>Significance</th></tr>
  <tr><td>Yancey campaign → Banks Strategy &amp; Consultants (2022)</td><td>$15,366.18</td><td>44.9% of Yancey&rsquo;s total expenditures; Banks&rsquo; only client that year</td></tr>
  <tr><td>Bank on Banks PAC → Yancey</td><td>$250</td><td>Net flow: Yancey sent $15,116 more to Banks than received</td></tr>
  <tr><td>Banks for Senate → Inner Link Graphics</td><td>$39,315</td><td>Part of $118,116+ network-wide Inner Link payments</td></tr>
  <tr><td>Bank on Banks PAC fines</td><td>$14,500</td><td>Delinquent; SOS referred to AG May 2022</td></tr>
</table>
<p><strong>Banks Senate Campaign totals:</strong> $167,175 raised / $166,944 spent. Notable payees: Mass Mailing LLC ($24,240), Gloria McCastle ($9,450), Outfront Media ($6,875 — never paid, bad check).</p>

<p><em>Compiled by Kevin Mok — OSINT only. Zero confidential sources. Every claim cited in full brief.</em></p>"""


def lara_entity_map(letter: str) -> str:
    return f"""<div class="page-break"></div>
<div class="exhibit-label">EXHIBIT {letter} — BANKS ENTITY MAP — LARA CORPORATE FILINGS</div>
<div class="exhibit-note">Source: mibusinessregistry.lara.state.mi.us | Searched August 31, 2026 (data as of 08/30/2026)</div>

<h3>G1 — The Purpose Group, LLC</h3>
<table>
  <tr><th>Field</th><th>Value</th></tr>
  <tr><td>Entity Name</td><td>THE PURPOSE GROUP, LLC</td></tr>
  <tr><td>Identification #</td><td>803295082</td></tr>
  <tr><td>Entity Type</td><td>Domestic Limited Liability Company</td></tr>
  <tr><td>Entity Status</td><td>Active</td></tr>
  <tr><td>AR Due Date</td><td>02/15/2026 (OVERDUE — 6+ months past due)</td></tr>
  <tr><td>Initial Filing</td><td>11/14/2024</td></tr>
  <tr><td>Resident Agent</td><td>BRIAN BANKS</td></tr>
  <tr><td>Registered Office</td><td>1968 SEVERN RD., GROSSE POINTE WOODS, MI 48236</td></tr>
</table>
<p><em>NOTE:</em> Charter management company operating Purpose Charter Academy. Filed 8 days after Banks&rsquo; November 6, 2024 loss in the Wayne County Commission race. Annual statement overdue since February 15, 2026.</p>

<h3>G2 — Banks Strategy &amp; Consultants, LLC</h3>
<table>
  <tr><th>Field</th><th>Value</th></tr>
  <tr><td>Entity Name</td><td>BANKS STRATEGY &amp; CONSULTANTS, LLC</td></tr>
  <tr><td>Identification #</td><td>802070120</td></tr>
  <tr><td>Entity Type</td><td>Domestic Limited Liability Company</td></tr>
  <tr><td>Entity Status</td><td>Active</td></tr>
  <tr><td>AR Due Date</td><td>02/15/2026 (OVERDUE — 6+ months past due)</td></tr>
  <tr><td>Initial Filing</td><td>02/25/2017</td></tr>
  <tr><td>Resident Agent</td><td>BRIAN R BANKS</td></tr>
  <tr><td>Registered Office</td><td>1968 SEVERN, GROSSE POINTE WOODS, MI 48236</td></tr>
</table>
<p><em>NOTE:</em> Filed February 25, 2017 — EIGHT DAYS after Banks resigned from the Michigan House under felony indictment. Advertises legal consulting services on LinkedIn. Annual statement overdue.</p>

<h3>G3 — Purpose Foundation</h3>
<table>
  <tr><th>Field</th><th>Value</th></tr>
  <tr><td>Entity Name</td><td>PURPOSE FOUNDATION</td></tr>
  <tr><td>Identification #</td><td>803294855</td></tr>
  <tr><td>Entity Type</td><td>Domestic Nonprofit Corporation</td></tr>
  <tr><td>Entity Status</td><td>Active</td></tr>
  <tr><td>AR Due Date</td><td>10/01/2026</td></tr>
  <tr><td>Initial Filing</td><td>12/09/2024</td></tr>
  <tr><td>Resident Agent</td><td>BRIAN BANKS</td></tr>
  <tr><td>Registered Office</td><td>1968 SEVERN ROAD, GROSSE POINTE WOODS, MI 48236</td></tr>
</table>
<p><strong>Officers and Directors:</strong> President — BRIAN BANKS; Secretary/Treasurer — JOSEPH HOLLAND JR (same address). Joseph Holland Jr is treasurer of &ldquo;Bank on Banks for Michigan&rdquo; PAC ($14,500 in fines). Filed 12/09/2024 — one month after Purpose Group.</p>

<h3>G4 — All Entities Associated with &ldquo;Brian Banks&rdquo;</h3>
<p>Individual name search — Results: 9 entities. Banks-connected (Agent = Brian Banks):</p>
<table>
  <tr><th>Entity</th><th>ID</th><th>Filed</th><th>Status</th></tr>
  <tr><td>Anchor Rock Services, Inc.</td><td>800770907</td><td>02/09/2015</td><td>Active</td></tr>
  <tr><td>Purpose Foundation</td><td>803294855</td><td>12/09/2024</td><td>Active</td></tr>
  <tr><td>Serenity Guardianship Services, Inc.</td><td>802290962</td><td>03/07/2019</td><td>DISSOLVED</td></tr>
  <tr><td>The Purpose Group, LLC</td><td>803295082</td><td>11/14/2024</td><td>Active — AR OVERDUE</td></tr>
  <tr><td>Banks Strategy &amp; Consultants, LLC</td><td>802070120</td><td>02/25/2017</td><td>Active — AR OVERDUE</td></tr>
</table>

<h3>Pattern</h3>
<p>All Banks entities share registered address: <strong>1968 Severn Road, Grosse Pointe Woods, MI 48236</strong> — Banks&rsquo; personal residence. Two of five active entities have overdue annual statements. The nonprofit&rsquo;s only officers are Banks and Joseph Holland Jr (PAC treasurer who owes $14,500 in campaign fines).</p>"""


EXHIBIT_P_MILLER = """<div class="page-break"></div>
<div class="exhibit-label">EXHIBIT P — PACER DOCKET — BRYANT v. MILLER</div>
<p style="text-align:center; margin-top:2in; font-size:14pt;"><strong>EXHIBIT P — PACER DOCKET — BRYANT v. MILLER</strong></p>
<p style="text-align:center; margin-top:1em;">Case No. 2:26-cv-10917-LVP-EAS<br>
U.S. District Court, E.D. Michigan</p>
<p style="text-align:center; margin-top:1em;"><strong>Filed:</strong> March 19, 2026</p>
<p style="text-align:center; margin-top:2em; font-style:italic;">Docket printout to be attached separately from PACER.</p>"""

EXHIBIT_Q_MILLER = """<div class="page-break"></div>
<div class="exhibit-label">EXHIBIT Q — BRYANT AMENDED COMPLAINT EXCERPTS — FIVE-LINK THEORY</div>
<p style="text-align:center; margin-top:2in; font-size:14pt;"><strong>EXHIBIT Q — BRYANT AMENDED COMPLAINT EXCERPTS</strong></p>
<p style="text-align:center; margin-top:1em;">Five-Link Structural Financial Conflict Theory<br>
<em>Doc 30, Amended Complaint — August 17, 2026</em><br>
<em>Bryant v. Miller et al., Case No. 2:26-cv-10917-LVP-EAS</em></p>
<p style="margin-top:2em;">Key paragraphs alleging the Five-Link Structural Financial Conflict within the Third Judicial Circuit Court:</p>
<ol>
  <li><strong>Revenue:</strong> The court collected $1.7M in criminal court costs in FY 2024.</li>
  <li><strong>GASB 34 Receivables:</strong> Criminal assessments booked as county assets — $69.6M in deferred inflows.</li>
  <li><strong>General Fund:</strong> Receivables flow into the General Fund ($147.1M in &ldquo;Charges for Services&rdquo;).</li>
  <li><strong>Bond Debt:</strong> The General Fund services $121.8M annual debt on the $200M Wayne County Building Authority bonds (Series 2010). Mandatory sinking fund redemptions begin December 2026.</li>
  <li><strong>Courthouse:</strong> Those bonds funded the Criminal Justice Center (opened September 2024) — where Judge Miller presides.</li>
</ol>
<p style="text-align:center; margin-top:2em; font-style:italic;">Full Amended Complaint (Doc 30) to be attached separately from PACER.</p>"""


BAR_COMPLAINT = """<div class="page-break"></div>
<div class="exhibit-label">EXHIBIT F — REQUEST FOR INVESTIGATION — TODD J. PERKINS (P55623)</div>

<h1 style="font-size:14pt;">Request for Investigation</h1>
<p style="text-align:center;">Attorney Grievance Commission / Michigan Attorney Discipline Board</p>

<p><strong>From:</strong> Kevin Mok<br>
[REDACTED_ADDR_1], Lansing, MI 48910<br>
[REDACTED_PHONE] | eco.primal@pm.me</p>

<p><strong>To:</strong> Attorney Grievance Commission<br>
755 W. Big Beaver Rd., Suite 2100, Troy, MI 48084</p>

<p><strong>Date:</strong> September 8, 2026</p>
<p><strong>Re:</strong> Request for Investigation<br>
Subject: Todd J. Perkins (P55623), Perkins Law Group PLLC</p>

<hr>

<h2>I. Attorney Identification</h2>
<table>
  <tr><th>Field</th><th>Value</th></tr>
  <tr><td>Name</td><td>Todd J. Perkins</td></tr>
  <tr><td>Bar Number</td><td>P55623</td></tr>
  <tr><td>Firm</td><td>Perkins Law Group PLLC</td></tr>
  <tr><td>Status</td><td>Active (Michigan State Bar)</td></tr>
  <tr><td>Known Clients</td><td>Brian Roderick Banks; Hon. Cylenthia LaToye Miller (3rd Circuit)</td></tr>
  <tr><td>Brother</td><td>Hon. Sean B. Perkins (36th District Court, Courtroom 535)</td></tr>
</table>

<h2>II. Nature of Complaint</h2>
<p>This complaint concerns a pattern of undisclosed conflicts of interest, facilitation of unauthorized practice of law, and the structural conflict created by Todd Perkins&rsquo; simultaneous roles as: (1) personal attorney to a sitting Criminal Division judge, (2) counsel to a convicted felon operating a charter school under that judge&rsquo;s board governance, and (3) brother of a judge sitting on a related bench.</p>

<h2>III. Facts</h2>

<h3>A. The Miller Representation (2024)</h3>
<p>On June 8, 2024, Judge Cylenthia LaToye Miller was arrested at Detroit Metropolitan Airport with a loaded, unregistered .380 caliber Smith &amp; Wesson handgun. She initially told police the gun belonged to &ldquo;her brother&rdquo; in Ohio. Todd Perkins, described as a &ldquo;personal friend,&rdquo; represented Judge Miller in the resulting criminal proceeding.</p>
<p>Judge Miller pleaded no contest on September 16, 2024, in the 34th District Court (case referred from Wayne County due to Prosecutor Kym Worthy&rsquo;s recusal). She received 90 days probation and $1,400 in fines.</p>
<p>Todd Perkins admitted during the proceeding that Judge Miller&rsquo;s initial statement to police — that the gun belonged to a relative — was false.</p>
<p><strong>Source:</strong> WXYZ-TV Detroit; FOX 2 Detroit; MLive; Belleville Independent.</p>

<h3>B. The Evans Murder Case — Undisclosed Conflict (Dec 2025)</h3>
<p>On December 8, 2025, Judge Miller dismissed <em>People v. Charles Evans</em> (Felony Murder and Child Abuse First Degree — the killing of nine-month-old Kinsley Evans) <strong>with prejudice</strong>.</p>
<p>The defense attorney in the Evans case was affiliated with <strong>Perkins Law Group PLLC</strong> — Todd Perkins&rsquo; firm.</p>
<p>This means Perkins Law Group simultaneously:</p>
<ol>
  <li>Represented Judge Miller personally (2024 gun case)</li>
  <li>Appeared before Judge Miller as defense counsel (Evans 2025)</li>
</ol>
<p><strong>Neither Judge Miller nor defense counsel disclosed this prior attorney-client relationship</strong> to the prosecution, the victim&rsquo;s family, or the public record.</p>
<p>Wayne County Prosecutor Kym Worthy stated: &ldquo;There is no such thing as dismissal with prejudice in criminal law.&rdquo; She further stated: &ldquo;In all of my years of practice I have never seen a judge behave like this.&rdquo;</p>
<p>The Wayne County Prosecutor&rsquo;s Office filed an appeal, which remains pending.</p>
<p><strong>Todd Perkins&rsquo; obligation:</strong> As the supervising attorney of Perkins Law Group PLLC, Todd Perkins had a professional obligation to ensure that his firm&rsquo;s appearance before a judge who was a current or recent client of the firm was disclosed. The failure to disclose this conflict resulted in the most extreme defense outcome — dismissal with prejudice of a murder charge involving an infant victim.</p>
<p><strong>Source:</strong> WXYZ-TV Detroit; Wayne County Prosecutor&rsquo;s Office press release.</p>

<h3>C. Brian Banks Representation</h3>
<p>Todd Perkins represents and/or has represented Brian Roderick Banks in various matters, including business entity formation and legal consultations. Banks is not licensed to practice law in Michigan (confirmed by State Bar P-number search). Banks presents himself as &ldquo;Brian Banks, J.D., Ph.D.&rdquo; and operates under the title &ldquo;attorney&rdquo; in public representations.</p>
<p>Judge Miller, Todd Perkins&rsquo; personal client, serves as <strong>Chairperson of the Board of Directors</strong> of Purpose Charter Academy — a school Banks founded and leads as superintendent.</p>
<p>Todd Perkins&rsquo; dual role — as Banks&rsquo; attorney and Miller&rsquo;s personal attorney — creates a structural conflict: Perkins has privileged knowledge of both the school&rsquo;s founder/operator and the judge who governs it.</p>

<h3>D. Brother on the Bench</h3>
<p>Todd Perkins&rsquo; brother, <strong>Sean B. Perkins</strong>, was appointed to the 36th District Court on May 5, 2021, by Governor Whitmer. Before his appointment, Sean Perkins was an attorney at <strong>Perkins Law Group PLLC</strong> — Todd&rsquo;s firm. They were law partners.</p>
<p>Sean Perkins now sits on the same 36th District bench as Judge Tenisha Yancey (MacDowell Board Chair; paid Banks $15,750 from campaign) and Judge Adam Sabree (son of Wayne County Treasurer Eric Sabree, who endorsed Banks and Miller). All three were elected on the same November 8, 2022 ballot.</p>
<p>Todd Perkins continues to practice law. Any appearance by Todd Perkins or any Perkins Law Group attorney before the 36th District Court — where his brother and former law partner sits — presents a structural conflict.</p>

<h3>E. Todd Perkins&rsquo; Mayoral Campaign (2025)</h3>
<p>Todd Perkins ran for Mayor of Detroit in 2025, receiving 5.35% of the vote. This political activity overlapped with his continued representation of Banks and his brother&rsquo;s judicial service.</p>

<h3>F. Todd Perkins&rsquo; Bankruptcy History</h3>
<p>PACER Case Locator records show the following federal bankruptcy filings in the Eastern District of Michigan:</p>
<table>
  <tr><th>Case No.</th><th>Filed</th><th>Name on Petition</th></tr>
  <tr><td>03-45986</td><td>Mar 4, 2003</td><td>Todd Perkins (solo)</td></tr>
  <tr><td>06-46764</td><td>May 30, 2006</td><td>Todd J. Perkins and Diane C. Perkins</td></tr>
  <tr><td>22-45209</td><td>Jun 30, 2022</td><td>Todd J. Perkins and Diane C. Perkins</td></tr>
</table>
<p>The 2022 filing (22-45209) was made WHILE Perkins was actively practicing law and representing clients including Banks and, subsequently, Judge Miller. Detroit News reporting has confirmed over $100,000 in IRS tax liens against Perkins between 2009 and 2016.</p>
<p>While bankruptcy alone does not constitute professional misconduct, the combination of chronic personal financial distress across two decades with the lucrative Banks representation and the extraordinary outcomes obtained from Judge Miller&rsquo;s courtroom (murder dismissal with prejudice) warrants scrutiny of the financial dimension of these relationships.</p>

<h2>IV. Rules of Professional Conduct Implicated</h2>
<p><strong>MRPC 1.7 — Conflict of Interest: Current Clients.</strong> Todd Perkins simultaneously represented Judge Miller (personal criminal defense) and appeared before her courtroom through his firm (Evans defense).</p>
<p><strong>MRPC 1.10 — Imputation of Conflicts.</strong> Perkins Law Group&rsquo;s conflict from the Miller representation extends to all attorneys at the firm.</p>
<p><strong>MRPC 3.3 — Candor Toward the Tribunal.</strong> The failure to disclose the prior attorney-client relationship between Perkins Law Group and Judge Miller during the Evans murder trial constitutes a failure of candor.</p>
<p><strong>MRPC 5.5 — Unauthorized Practice of Law.</strong> To the extent Todd Perkins has facilitated Brian Banks&rsquo; public representation of himself as an attorney, Perkins may be assisting in the unauthorized practice of law.</p>
<p><strong>MRPC 8.4 — Misconduct.</strong> The pattern of undisclosed conflicts, combined with the extraordinary outcome in the Evans case, constitutes conduct prejudicial to the administration of justice.</p>

<h2>V. Pattern Summary</h2>
<p>Todd Perkins sits at the intersection of three conflict streams:</p>
<ol>
  <li><strong>Judge-to-attorney:</strong> He personally represents Judge Miller, then his firm appears before her and wins dismissal with prejudice in a murder case — without disclosure.</li>
  <li><strong>Attorney-to-enterprise:</strong> He represents Banks while his personal client Judge Miller chairs the board of Banks&rsquo; school.</li>
  <li><strong>Family-to-bench:</strong> His brother, his former law partner, sits on the 36th District bench alongside two other judges with Banks network connections.</li>
</ol>

<h2>VI. Request</h2>
<p>I respectfully request that the Attorney Grievance Commission investigate:</p>
<ol type="a">
  <li>The failure to disclose the Perkins Law Group / Judge Miller attorney-client relationship during the <em>People v. Charles Evans</em> proceeding;</li>
  <li>Whether Todd Perkins or Perkins Law Group has appeared before Judge Sean Perkins (36th District) without disclosure of the family and prior partnership relationship;</li>
  <li>Whether Todd Perkins has facilitated or enabled Brian Banks&rsquo; unauthorized practice of law in Michigan;</li>
  <li>The broader pattern of conflicts arising from Todd Perkins&rsquo; simultaneous roles as counsel to a judge, counsel to a convicted felon, and brother of a judge.</li>
</ol>
<p>I am available to provide additional documentation upon request.</p>

<div class="sig-block">
  <p>Respectfully submitted,</p>
  <p>_________________________________<br>
  Kevin Mok<br>
  Pro Se Plaintiff<br>
  Mok v. Banks, Case No. 2026-4349-CZ (Ingham County Circuit Court)</p>
</div>"""


def insert_before_marker(html: str, marker: str, content: str) -> str:
    if marker not in html:
        raise ValueError(f"Marker not found: {marker!r}")
    return html.replace(marker, content + "\n\n" + marker, 1)


def patch_miller() -> None:
    path = DESKTOP / "01_MILLER_PACKET.html"
    html = path.read_text(encoding="utf-8")
    additions = (
        EXHIBIT_P_MILLER
        + "\n"
        + EXHIBIT_Q_MILLER
        + "\n"
        + lara_entity_map("S")
        + "\n"
    )
    html = insert_before_marker(html, EXHIBITS_MARKER, additions)
    footer = "<p><em>Compiled by Kevin Mok — September 8, 2026. Derived from public records.</em></p>"
    html = html.replace(footer, footer + "\n" + osint_brief("V"), 1)
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.name}")


def patch_yancey() -> None:
    path = DESKTOP / "02_YANCEY_PACKET.html"
    html = path.read_text(encoding="utf-8")
    additions = osint_brief("J") + "\n" + lara_entity_map("K") + "\n"
    html = insert_before_marker(html, EXHIBITS_MARKER, additions)
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.name}")


def patch_aliyah() -> None:
    path = DESKTOP / "03_ALIYAH_SABREE_PACKET.html"
    html = path.read_text(encoding="utf-8")
    additions = osint_brief("A") + "\n" + lara_entity_map("G") + "\n"
    html = insert_before_marker(html, EXHIBITS_MARKER, additions)
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.name}")


def patch_adam() -> None:
    path = DESKTOP / "04_ADAM_SABREE_PACKET.html"
    html = path.read_text(encoding="utf-8")
    additions = osint_brief("A") + "\n" + lara_entity_map("F") + "\n"
    html = insert_before_marker(html, EXHIBITS_MARKER, additions)
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.name}")


def patch_perkins() -> None:
    path = DESKTOP / "05_PERKINS_PACKET.html"
    html = path.read_text(encoding="utf-8")
    old_f = (
        '<div class="page-break"></div>\n'
        '<div class="exhibit-label">EXHIBIT F — BAR COMPLAINT AGAINST TODD J. PERKINS (P55623)</div>\n'
        '<p class="exhibit-note">Copy of Request for Investigation filed with the Attorney Grievance Commission, '
        "September 8, 2026, is attached hereto as a separate document.</p>"
    )
    if old_f not in html:
        raise ValueError("Perkins placeholder Exhibit F not found")
    html = html.replace(old_f, BAR_COMPLAINT, 1)
    exhibits_start = html.find(EXHIBITS_MARKER)
    before_f = html.find('<div class="exhibit-label">EXHIBIT F — REQUEST FOR INVESTIGATION', exhibits_start)
    html = html[:before_f] + osint_brief("A") + "\n\n" + html[before_f:]
    body_end = html.rfind("</body>")
    html = html[:body_end] + "\n" + lara_entity_map("H") + "\n\n" + html[body_end:]
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.name}")


def main() -> None:
    patch_miller()
    patch_yancey()
    patch_aliyah()
    patch_adam()
    patch_perkins()
    print("All packets patched successfully.")


if __name__ == "__main__":
    main()
