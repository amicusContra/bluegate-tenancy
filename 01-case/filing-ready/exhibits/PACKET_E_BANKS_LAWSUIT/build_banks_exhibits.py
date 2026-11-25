"""Build print-ready exhibits for Kevin Mok v. Banks lawsuit (cleaned)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PKT = Path(r"C:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready\exhibits\PACKET_E_BANKS_LAWSUIT")

LETTER_W, LETTER_H = 2550, 3300
MARGIN = 150

EXHIBIT_IMAGES = [
    ("EXHIBIT B — LinkedIn Profile Screenshots (24 pages)\nBrian Banks LinkedIn — captured August 29, 2026", [
        PKT / "B_linkedin" / f"IMG_{n}.PNG" for n in range(5794, 5818)
    ]),
    ("EXHIBIT C — State Bar of Michigan Member Directory Search\n'brian banks' and 'banks' — searched August 31, 2026\nNo record of Brian Banks, Brian R. Banks, or Brian Roderick Banks", [
        PKT / "C1_SBAR_BRIAN_BANKS_ZERO_RESULTS.png",
        PKT / "C2_SBAR_BANKS_RESULTS_PAGE1.png",
        PKT / "C3_SBAR_BANKS_RESULTS_PAGE2.png",
    ]),
    ("EXHIBIT G — LARA Corporate Filings\nMiBusiness Registry Portal — searched August 31, 2026\nAll entities registered to Brian Banks at 1968 Severn Rd, GPW", [
        PKT / "G1_LARA_PURPOSE_GROUP_LLC.png",
        PKT / "G2_LARA_BANKS_STRATEGY_LLC.png",
        PKT / "G3_LARA_PURPOSE_FOUNDATION.png",
        PKT / "G4_LARA_ALL_BANKS_ENTITIES.png",
    ]),
    ("EXHIBIT N — DPSCD Authorizer Complaint (Email Sent)\nTo: dpscd.compliance@detroitk12.org — August 31, 2026", [
        PKT / "N_DPSCD_EMAIL_SENT.png",
    ]),
    ("EXHIBIT O — PCA Orientation Materials\nObtained at Purpose Charter Academy Back to School Bash\nAugust 29, 2026", [
        PKT / "O1_PCA_ORIENTATION_ARRIVAL.jpeg",
        PKT / "O2_PCA_ORIENTATION_UNIFORM.jpeg",
    ]),
]


def make_header_page(text):
    page = Image.new("RGB", (LETTER_W, LETTER_H), "white")
    draw = ImageDraw.Draw(page)
    try:
        font_title = ImageFont.truetype("arial.ttf", 72)
        font_body = ImageFont.truetype("arial.ttf", 48)
    except OSError:
        font_title = ImageFont.load_default()
        font_body = font_title

    lines = text.split("\n")
    y = LETTER_H // 4
    for i, line in enumerate(lines):
        font = font_title if i == 0 else font_body
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (LETTER_W - tw) // 2
        draw.text((x, y), line, fill="black", font=font)
        y += (bbox[3] - bbox[1]) + 40

    draw.line([(MARGIN, y + 20), (LETTER_W - MARGIN, y + 20)], fill="black", width=4)
    return page


def image_to_page(img_path):
    img = Image.open(img_path).convert("RGB")
    max_w = LETTER_W - (MARGIN * 2)
    max_h = LETTER_H - (MARGIN * 2)
    ratio = min(max_w / img.width, max_h / img.height)
    new_w = int(img.width * ratio)
    new_h = int(img.height * ratio)
    img_resized = img.resize((new_w, new_h), Image.LANCZOS)
    page = Image.new("RGB", (LETTER_W, LETTER_H), "white")
    x = (LETTER_W - new_w) // 2
    y = (LETTER_H - new_h) // 2
    page.paste(img_resized, (x, y))
    return page


print("Building PRINT_ALL_IMAGE_EXHIBITS.pdf ...")
all_pages = []

for header_text, image_files in EXHIBIT_IMAGES:
    imgs = [f for f in image_files if f.exists()]
    if not imgs:
        print(f"  SKIP (no files): {header_text[:50]}")
        continue
    all_pages.append(make_header_page(header_text))
    for img_path in imgs:
        all_pages.append(image_to_page(img_path))
    print(f"  {header_text.split(chr(10))[0]}: {len(imgs)} pages")

if all_pages:
    out = PKT / "PRINT_ALL_IMAGE_EXHIBITS.pdf"
    all_pages[0].save(out, save_all=True, append_images=all_pages[1:], resolution=300)
    print(f"\nSaved: {out.name} ({len(all_pages)} pages)")


print("\nBuilding PRINT_ALL_TEXT_EXHIBITS.md ...")
TEXT_EXHIBITS = [
    ("EXHIBIT A", "Parental Authorization — see A_PARENTAL_AUTHORIZATION.pdf (print separately)"),
    ("EXHIBIT C", PKT / "C_STATE_BAR_SEARCH_SUMMARY.md"),
    ("EXHIBIT D", PKT / "D_ELRICK_FREEP_JULY2022.md"),
    ("EXHIBIT E", PKT / "E_PCA_FOUNDER_PAGE.md"),
    ("EXHIBIT F", PKT / "F_ELRICK_FREEP_AUG2023.md"),
    ("EXHIBIT G", PKT / "G_LARA_FILINGS_SUMMARY.md"),
    ("EXHIBIT H", PKT / "H_BANKS_OSINT_BRIEF.md"),
    ("EXHIBIT L", PKT / "L_MDE_COMPLAINT.md"),
    ("EXHIBIT M", PKT / "M_AG_REFERRAL.md"),
    ("EXHIBIT P", PKT / "P_MACDOWELL_BOARD.md"),
    ("EXHIBIT Q", PKT / "Q_CHALKBEAT_SEPT2025.md"),
    ("EXHIBIT R", PKT / "R_KEEPJUDGEMILLER.md"),
    ("EXHIBIT S", PKT / "S1_BALLOTPEDIA_YANCEY.md"),
    ("EXHIBIT S (cont.)", PKT / "S2_BALLOTPEDIA_MILLER.md"),
]

EXHIBIT_INDEX = """======================================================================
  EXHIBIT INDEX — Kevin Mok v. Brian Banks et al.
  Ingham County Circuit Court
======================================================================

  A — Parental Authorization (DaSean Mitchell, Aug 29, 2026)
        [print separately: A_PARENTAL_AUTHORIZATION.pdf]

  B — Brian Banks LinkedIn Profile Screenshots (24 pages)
        [print separately: PRINT_ALL_IMAGE_EXHIBITS.pdf]

  C — State Bar of Michigan Member Directory Search
        [text below + screenshots in PRINT_ALL_IMAGE_EXHIBITS.pdf]

  D — M.L. Elrick, Detroit Free Press (July 3, 2022)
        "Here's the record Brian Banks doesn't want you to know"

  E — PCA "Our Founder" Page (purposecharteracademy.com)
        "Dr. Brian Banks, J.D., Ph.D."

  F — M.L. Elrick, Detroit Free Press (Aug 27, 2023)
        Administrator certificate conditions confirmed by MDE

  G — LARA Corporate Filings (4 Banks entities)
        [text below + screenshots in PRINT_ALL_IMAGE_EXHIBITS.pdf]

  H — OSINT Analysis Brief (comprehensive public records compilation)

  I — UPL Complaint, State Bar of Michigan (Aug 31, 2026)
        [print separately: I_UPL_RECEIPT_AUG31.pdf]

  J — JTC Request — Judge Tenisha R. Yancey (Aug 31, 2026)
        [print separately: JK_JTC_CERTIFIED_MAIL.pdf + JK_JTC_NOTARY.pdf]

  K — JTC Request — Judge Cylenthia LaToye Miller (Aug 31, 2026)
        [print separately: JK_JTC_CERTIFIED_MAIL.pdf + JK_JTC_NOTARY.pdf]

  L — MDE Certificate Violation Complaint (Sept 1, 2026)

  M — AG UPL Prosecution Referral (Sept 1, 2026)

  N — DPSCD Authorizer Complaint (Aug 31, 2026)
        [screenshot in PRINT_ALL_IMAGE_EXHIBITS.pdf]

  O — PCA Orientation Materials (Aug 29, 2026)
        [photos in PRINT_ALL_IMAGE_EXHIBITS.pdf]

  P — MacDowell Prep Board of Directors (macdowellprep.com)

  Q — Chalkbeat Detroit (Sept 8, 2025)
        Judge Miller on PCA development team

  R — keepjudgemiller.com — shared endorsers with Banks

  S — Ballotpedia — Judge Yancey and Judge Miller

  T — PCA Enrollment Records (to be obtained in discovery)

======================================================================"""

combined = [EXHIBIT_INDEX, "\n\n---\n*PAGE BREAK*\n---\n\n"]
for label, source in TEXT_EXHIBITS:
    combined.append(f"{'=' * 70}")
    combined.append(f"  {label}")
    combined.append(f"{'=' * 70}\n")
    if isinstance(source, str):
        combined.append(source)
    elif isinstance(source, Path) and source.exists():
        combined.append(source.read_text(encoding="utf-8"))
    else:
        combined.append(f"[FILE NOT FOUND: {source}]")
    combined.append("\n\n---\n*PAGE BREAK*\n---\n\n")

out_md = PKT / "PRINT_ALL_TEXT_EXHIBITS.md"
out_md.write_text("\n".join(combined), encoding="utf-8")
print(f"Saved: {out_md.name}")

print("\nPRINT ORDER:")
print("  1. 39_KEVIN_V_BANKS_COMPLAINT.txt (sign and date)")
print("  2. PRINT_ALL_TEXT_EXHIBITS.md (Exhibits A,C,D,E,F,G,H,L,M,P,Q,R,S)")
print("  3. PRINT_ALL_IMAGE_EXHIBITS.pdf (Exhibits B,C,G,N,O)")
print("  4. A_PARENTAL_AUTHORIZATION.pdf (print separately)")
print("  5. I_UPL_RECEIPT_AUG31.pdf (print separately)")
print("  6. JK_JTC_CERTIFIED_MAIL.pdf + JK_JTC_NOTARY.pdf (print separately)")

