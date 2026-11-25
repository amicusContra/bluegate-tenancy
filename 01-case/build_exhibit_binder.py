"""
Build PPO Hearing Exhibit Binder — PDF Assembly
DaSean Mitchell PPO Hearing, Sep 29 2026, Hon. Koenig, Courtroom #4

Produces:
  PPO_EXHIBIT_BINDER_SEP29.pdf  — full binder with tab dividers
  (copy to USB along with RING_VIDEO_SEP2_2026_ASSAULT.mp4)

Usage: python build_exhibit_binder.py
"""

import os
import sys
from pathlib import Path

try:
    import fitz  # pymupdf
except ImportError:
    print("ERROR: pymupdf not installed. Run: pip install pymupdf")
    sys.exit(1)

from PIL import Image
import io

BASE = Path(r"C:\Users\mokke\jobHunt\bluegate-tenancy")
EVIDENCE = BASE / "02-evidence"
CASE_EVIDENCE = BASE / "01-case" / "evidence"
OUTPUT = BASE / "01-case" / "PPO_EXHIBIT_BINDER_SEP29.pdf"

# Page dimensions (letter: 612 x 792 points)
W, H = 612, 792


def create_tab_page(doc, tab_id, title, description=""):
    """Create a colored tab divider page."""
    page = doc.new_page(width=W, height=H)
    
    # Background color — light gray
    rect = fitz.Rect(0, 0, W, H)
    page.draw_rect(rect, color=None, fill=(0.92, 0.92, 0.92))
    
    # Dark header bar
    header = fitz.Rect(0, 280, W, 380)
    page.draw_rect(header, color=None, fill=(0.15, 0.15, 0.25))
    
    # Tab ID — large centered white text
    page.insert_text(
        fitz.Point(W/2 - len(tab_id)*18, 350),
        tab_id,
        fontsize=48,
        fontname="helv",
        color=(1, 1, 1),
    )
    
    # Title — below header
    title_lines = []
    words = title.split()
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        if len(test) > 55:
            title_lines.append(line)
            line = word
        else:
            line = test
    if line:
        title_lines.append(line)
    
    y = 420
    for tl in title_lines:
        page.insert_text(
            fitz.Point(72, y),
            tl,
            fontsize=18,
            fontname="helv",
            color=(0.15, 0.15, 0.25),
        )
        y += 28
    
    # Description — smaller text
    if description:
        y += 20
        desc_lines = []
        words = description.split()
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if len(test) > 75:
                desc_lines.append(line)
                line = word
            else:
                line = test
        if line:
            desc_lines.append(line)
        
        for dl in desc_lines:
            page.insert_text(
                fitz.Point(72, y),
                dl,
                fontsize=12,
                fontname="helv",
                color=(0.4, 0.4, 0.4),
            )
            y += 18
    
    # Case info at bottom
    page.insert_text(
        fitz.Point(72, 700),
        "Mitchell v. Smith et al. — PPO Hearing Sep 29, 2026",
        fontsize=10,
        fontname="helv",
        color=(0.5, 0.5, 0.5),
    )
    page.insert_text(
        fitz.Point(72, 715),
        "Hon. Carol N. Koenig — Courtroom #4 — 313 W. Kalamazoo St, Lansing",
        fontsize=10,
        fontname="helv",
        color=(0.5, 0.5, 0.5),
    )
    
    return page


def add_pdf(doc, pdf_path, label=""):
    """Insert all pages from an existing PDF."""
    if not pdf_path.exists():
        print(f"  ⚠ MISSING: {pdf_path}")
        # Add a placeholder page
        page = doc.new_page(width=W, height=H)
        page.insert_text(
            fitz.Point(72, 396),
            f"[MISSING FILE: {pdf_path.name}]",
            fontsize=14, fontname="helv", color=(0.8, 0, 0),
        )
        if label:
            page.insert_text(
                fitz.Point(72, 420),
                f"Label: {label}",
                fontsize=11, fontname="helv", color=(0.4, 0.4, 0.4),
            )
        return 0
    
    try:
        src = fitz.open(str(pdf_path))
        count = len(src)
        doc.insert_pdf(src)
        src.close()
        print(f"  + {pdf_path.name} ({count} pages)")
        return count
    except Exception as e:
        print(f"  ⚠ ERROR reading {pdf_path.name}: {e}")
        page = doc.new_page(width=W, height=H)
        page.insert_text(
            fitz.Point(72, 396),
            f"[ERROR: {pdf_path.name}]",
            fontsize=14, fontname="helv", color=(0.8, 0, 0),
        )
        return 0


def add_image(doc, img_path, label=""):
    """Insert an image as a full page, scaled to fit."""
    if not img_path.exists():
        print(f"  ⚠ MISSING: {img_path}")
        page = doc.new_page(width=W, height=H)
        page.insert_text(
            fitz.Point(72, 396),
            f"[MISSING FILE: {img_path.name}]",
            fontsize=14, fontname="helv", color=(0.8, 0, 0),
        )
        return
    
    try:
        page = doc.new_page(width=W, height=H)
        
        # Add label at top if provided
        y_offset = 36
        if label:
            page.insert_text(
                fitz.Point(36, 24),
                label,
                fontsize=9, fontname="helv", color=(0.4, 0.4, 0.4),
            )
            y_offset = 40
        
        # Calculate image placement — fit within margins
        margin = 36
        max_w = W - 2 * margin
        max_h = H - y_offset - margin
        
        img_rect = fitz.Rect(margin, y_offset, margin + max_w, y_offset + max_h)
        page.insert_image(img_rect, filename=str(img_path), keep_proportion=True)
        print(f"  + {img_path.name}")
    except Exception as e:
        print(f"  ⚠ ERROR with {img_path.name}: {e}")


def add_images_grid(doc, img_paths, label="", cols=2):
    """Add multiple small images in a grid on one page."""
    existing = [p for p in img_paths if p.exists()]
    if not existing:
        return
    
    rows_per_page = 3
    per_page = cols * rows_per_page
    margin = 36
    gap = 12
    cell_w = (W - 2*margin - (cols-1)*gap) / cols
    cell_h = (H - 72 - margin - (rows_per_page-1)*gap) / rows_per_page
    
    for batch_start in range(0, len(existing), per_page):
        batch = existing[batch_start:batch_start + per_page]
        page = doc.new_page(width=W, height=H)
        
        if label:
            page.insert_text(
                fitz.Point(margin, 24),
                label,
                fontsize=9, fontname="helv", color=(0.4, 0.4, 0.4),
            )
        
        for idx, img_path in enumerate(batch):
            row = idx // cols
            col = idx % cols
            x = margin + col * (cell_w + gap)
            y = 40 + row * (cell_h + gap)
            rect = fitz.Rect(x, y, x + cell_w, y + cell_h)
            try:
                page.insert_image(rect, filename=str(img_path), keep_proportion=True)
            except Exception as e:
                page.insert_text(fitz.Point(x+4, y+20), f"[err: {img_path.name}]",
                               fontsize=8, fontname="helv", color=(0.8,0,0))
        
        print(f"  + grid page: {len(batch)} images")


def create_cover_page(doc):
    """Create the binder cover page."""
    page = doc.new_page(width=W, height=H)
    
    # Title block
    page.insert_text(fitz.Point(72, 200), "EXHIBIT BINDER",
                     fontsize=36, fontname="helv", color=(0.1, 0.1, 0.2))
    
    page.insert_text(fitz.Point(72, 260), "PERSONAL PROTECTION ORDER HEARING",
                     fontsize=16, fontname="helv", color=(0.2, 0.2, 0.3))
    
    page.insert_text(fitz.Point(72, 300), "September 29, 2026 — 1:30 PM",
                     fontsize=14, fontname="helv", color=(0.3, 0.3, 0.4))
    page.insert_text(fitz.Point(72, 320), "Hon. Carol N. Koenig — Courtroom #4",
                     fontsize=14, fontname="helv", color=(0.3, 0.3, 0.4))
    page.insert_text(fitz.Point(72, 340), "313 W. Kalamazoo St, Lansing, MI 48933",
                     fontsize=14, fontname="helv", color=(0.3, 0.3, 0.4))
    
    # Cases
    y = 400
    page.insert_text(fitz.Point(72, y), "CONSOLIDATED CASES:",
                     fontsize=12, fontname="helv", color=(0.2, 0.2, 0.3))
    cases = [
        "26-4432-PP   Mitchell v. S. Smith (Domestic)",
        "26-4433-PH   Mitchell v. M. Smith (Harassment)",
        "26-4434-PH   Mitchell v. S.R. Smith (Harassment)",
        "26-4435-PH   Mitchell v. Banks (Harassment)",
        "26-4436-PH   Mitchell v. L. Smith (Harassment)",
    ]
    for c in cases:
        y += 22
        page.insert_text(fitz.Point(90, y), c,
                        fontsize=11, fontname="helv", color=(0.3, 0.3, 0.4))
    
    # Petitioner
    y += 50
    page.insert_text(fitz.Point(72, y), "Petitioner:  DaSean Mitchell (Pro Se)",
                     fontsize=12, fontname="helv", color=(0.2, 0.2, 0.3))
    y += 22
    page.insert_text(fitz.Point(72, y), "Witness:     Kevin Mok",
                     fontsize=12, fontname="helv", color=(0.2, 0.2, 0.3))
    
    # Table of contents
    y += 60
    page.insert_text(fitz.Point(72, y), "EXHIBIT INDEX:",
                     fontsize=12, fontname="helv", color=(0.2, 0.2, 0.3))
    tabs = [
        ("Tab 1A", "Ring camera video stills — Sep 2, 2026 assault"),
        ("Tab 1B", "Shayla's texts coordinating child pickup"),
        ("Tab 2A", "ICHAT — Banks SID 2029469K (9 felony convictions)"),
        ("Tab 2B", "State Bar of Michigan — no record of admission"),
        ("Tab 2C", "DPD Report #26-0909-0176 — 'I am an attorney'"),
        ("Tab 3A", "Forged certified mail return receipts (x4)"),
        ("Tab 3B", "Leon texts — 'Good luck' / 'Will see you in court'"),
        ("Tab 4A", "Shayla's emergency custody filing (Wayne County)"),
        ("Tab 5A", "PS Form 3665 — proof of mailing (19 pieces)"),
        ("Tab 5B", "MDE FOIA response — credentialing fraud"),
    ]
    for tab_id, desc in tabs:
        y += 18
        page.insert_text(fitz.Point(90, y), f"{tab_id}    {desc}",
                        fontsize=10, fontname="helv", color=(0.3, 0.3, 0.4))


def main():
    print("=" * 60)
    print("Building PPO Exhibit Binder")
    print("=" * 60)
    
    doc = fitz.open()
    
    # ============================================================
    # COVER PAGE
    # ============================================================
    print("\n[COVER]")
    create_cover_page(doc)
    print("  + Cover page with exhibit index")
    
    # ============================================================
    # TAB 1A — Ring Camera Video Stills (Sep 2 Assault)
    # ============================================================
    print("\n[TAB 1A] Ring Camera — Sep 2 Assault")
    create_tab_page(doc, "TAB 1A",
        "Ring Camera Video — September 2, 2026 Assault",
        "Leon Smith assaults DaSean Mitchell at XXXX Cornerstone Blvd "
        "(Deanna Mitchell's residence — paternal grandmother). "
        "Ring doorbell camera. Timestamped, geo-located. "
        "Full video on USB drive.")
    
    # First try the existing PDF of key frames
    keyframes_pdf = CASE_EVIDENCE / "RING_EXHIBIT_KEYFRAMES_SEP2.pdf"
    if keyframes_pdf.exists():
        add_pdf(doc, keyframes_pdf, "Tab 1A — Ring camera key frames")
    else:
        # Fall back to individual frames from ppo-materials/exhibits
        exhibit_frames = sorted((EVIDENCE / "ppo-materials" / "exhibits").glob("*_ring_*.png"))
        if exhibit_frames:
            for frame in exhibit_frames:
                add_image(doc, frame, f"Tab 1A — {frame.stem}")
        else:
            # Fall back to dpd-counter-report ring frames
            ring_frames = sorted((EVIDENCE / "dpd-counter-report").glob("ring_*.png"))
            for frame in ring_frames[:10]:
                add_image(doc, frame, f"Tab 1A — {frame.stem}")
    
    # ============================================================
    # TAB 1B — Shayla's Texts Coordinating Pickup
    # ============================================================
    print("\n[TAB 1B] Shayla's Texts — Pre-Planned Pickup")
    create_tab_page(doc, "TAB 1B",
        "Shayla's Texts Coordinating Child Pickup",
        "Text messages show Shayla coordinated the removal of "
        "Sahana and Allanna from Deanna Mitchell's house ahead of time, "
        "completely excluding DaSean. Pre-planned, not spontaneous. "
        "Source: Shayla's own 192-page emergency custody filing exhibits.")
    
    # Shayla's texts — from custody filing exhibits or text screenshots
    shayla_exhibits = EVIDENCE / "court-filings" / "shayla" / "shaylaExhbits.pdf"
    if shayla_exhibits.exists():
        add_pdf(doc, shayla_exhibits, "Tab 1B — Shayla's exhibits (contains coordination texts)")
    
    # Also add relevant text screenshots if available
    text_imgs = sorted((EVIDENCE / "smith-texts" / "leon-shayla-combined").glob("IMG_60*.PNG"))
    if text_imgs:
        # Add a few key ones — the coordination texts
        for img in text_imgs[:4]:
            add_image(doc, img, f"Tab 1B — Text messages")
    
    # ============================================================
    # TAB 2A — ICHAT (Banks — 9 Felony Convictions)
    # ============================================================
    print("\n[TAB 2A] ICHAT — Banks 9 Felony Convictions")
    create_tab_page(doc, "TAB 2A",
        "ICHAT Criminal History — Brian Roderick Banks",
        "Michigan ICHAT, SID 2029469K. "
        "Nine (9) felony convictions with dates, charges, and dispositions. "
        "This individual is the superintendent of the school "
        "DaSean's daughters attend.")
    
    banks_ichat = EVIDENCE / "screenshots" / "brianBanksICHAT.pdf"
    if banks_ichat.exists():
        add_pdf(doc, banks_ichat, "Tab 2A — Banks ICHAT")
    
    # ============================================================
    # TAB 2B — State Bar Search (No Record)
    # ============================================================
    print("\n[TAB 2B] State Bar — No Record")
    create_tab_page(doc, "TAB 2B",
        "State Bar of Michigan — Attorney Search",
        "No record of Brian Banks ever being admitted to the "
        "Michigan State Bar. He is NOT an attorney despite claiming "
        "to be one in DPD Report #26-0909-0176.")
    
    state_bar = EVIDENCE / "cbcf-package" / "1_STATE_BAR_ZERO_RESULTS.png"
    if state_bar.exists():
        add_image(doc, state_bar, "Tab 2B — State Bar search: zero results for Brian Banks")
    
    # ============================================================
    # TAB 2C — DPD Report (Banks Claims Attorney)
    # ============================================================
    print("\n[TAB 2C] DPD Report — 'I Am An Attorney'")
    create_tab_page(doc, "TAB 2C",
        "DPD Report #26-0909-0176",
        "September 9, 2026. Brian Banks told Detroit Police officers "
        "'I am an attorney.' Banks also filed a retaliatory police report "
        "against Kevin Mok. See Tab 2B — Banks has no bar admission.")
    
    # Banks response screenshots (from the DPD interaction)
    banks_response_full = CASE_EVIDENCE / "BANKS_RESPONSE_SEP10_FULL.png"
    banks_response_close = CASE_EVIDENCE / "BANKS_RESPONSE_SEP10_CLOSEUP.png"
    banks_service_confirm = CASE_EVIDENCE / "BANKS_SERVICE_CONFIRMATION_SEP9.png"
    
    for img_path in [banks_service_confirm, banks_response_full, banks_response_close]:
        if img_path.exists():
            add_image(doc, img_path, f"Tab 2C — {img_path.stem}")
    
    # Also the CBCF package versions
    cbcf_reply_full = EVIDENCE / "cbcf-package" / "4_BANKS_REPLY_FULL.png"
    cbcf_reply_close = EVIDENCE / "cbcf-package" / "4B_BANKS_REPLY_CLOSEUP.png"
    for img_path in [cbcf_reply_full, cbcf_reply_close]:
        if img_path.exists() and not banks_response_full.exists():
            add_image(doc, img_path, f"Tab 2C — {img_path.stem}")
    
    # ============================================================
    # TAB 3A — Forged Certified Mail Receipts
    # ============================================================
    print("\n[TAB 3A] Forged Certified Mail Receipts")
    create_tab_page(doc, "TAB 3A",
        "Forged Certified Mail Return Receipts (x4)",
        "Four return receipts for legal mail came back signed with forged "
        "signatures — all in the same handwriting. Leon Smith is a USPS "
        "mail carrier at the Harper Woods post office. "
        "USPS OIG Cases #174517, #202990, #208322.")
    
    # Return receipt PDFs
    rr_pdf = CASE_EVIDENCE / "RestrictedReturnReceipt.pdf"
    rr_sigs_pdf = CASE_EVIDENCE / "RestrictedReturnReceiptSigs.pdf"
    if rr_pdf.exists():
        add_pdf(doc, rr_pdf, "Tab 3A — Return receipts")
    if rr_sigs_pdf.exists():
        add_pdf(doc, rr_sigs_pdf, "Tab 3A — Forged signature detail")
    
    # Signature comparison exhibits
    sig_dir = EVIDENCE / "signature-comparison"
    sig_files = [
        sig_dir / "EXHIBIT_B1_GREEN_CARD_SIGNATURES_ALL.png",
        sig_dir / "EXHIBIT_B2_LEON_MARQUITA_AUTHENTIC_VS_GREEN_CARDS.png",
        sig_dir / "EXHIBIT_B3_SIMONE_AUTHENTIC_VS_GREEN_CARD.png",
    ]
    for sf in sig_files:
        if sf.exists():
            add_image(doc, sf, f"Tab 3A — {sf.stem}")
    
    # Service receipts showing forged signatures
    service_receipts = [
        EVIDENCE / "service-proof" / "SERVICE_CERT_MAIL_LEON_SMITH_RECEIPT.png",
        EVIDENCE / "service-proof" / "SERVICE_CERT_MAIL_SHAYLA_SMITH_RECEIPT.png",
        EVIDENCE / "service-proof" / "SERVICE_CERT_MAIL_MARQUITA_SMITH_RECEIPT.png",
        EVIDENCE / "service-proof" / "SERVICE_CERT_MAIL_SIMONE_SMITH_RECEIPT.png",
    ]
    for sr in service_receipts:
        if sr.exists():
            add_image(doc, sr, f"Tab 3A — {sr.stem}")
    
    # ============================================================
    # TAB 3B — Leon Texts ('Good Luck' / 'Will See You In Court')
    # ============================================================
    print("\n[TAB 3B] Leon Texts — 'Good Luck'")
    create_tab_page(doc, "TAB 3B",
        "Text Messages — Leon Smith to Kevin Mok",
        "September 16-17, 2026. Leon Smith texts Kevin Mok: "
        "'Good luck' and 'Do not text me again. Will see you in court.' "
        "Confirms actual notice of all proceedings. Intimidation.")
    
    leon_texts = [
        EVIDENCE / "screenshots-correspondence" / "LEON_TEXT_SIGNATURE_COMPARISON_GOOD_LUCK_SEP17.png",
        EVIDENCE / "screenshots-correspondence" / "LEON_TEXT_SIGNATURE_COMPARISON_FULL_SEP17.png",
    ]
    for lt in leon_texts:
        if lt.exists():
            add_image(doc, lt, f"Tab 3B — {lt.stem}")
    
    # Also the raw text screenshots
    leon_raw = sorted((EVIDENCE / "smith-texts" / "leon-downloads").glob("IMG_60*.PNG"))
    for lr in leon_raw:
        add_image(doc, lr, f"Tab 3B — Leon text messages")
    
    # ============================================================
    # TAB 4A — Shayla's 192-Page Emergency Custody Filing
    # ============================================================
    print("\n[TAB 4A] Shayla's Emergency Custody Filing")
    create_tab_page(doc, "TAB 4A",
        "Shayla's Emergency Custody Filing — Wayne County",
        "Case 26-108221-DC. Filed September 5, 2026 — three days after "
        "the assault. 192 pages of exhibits. Explicitly requests Kevin Mok "
        "be barred from contact with DaSean and the children. "
        "Her own exhibits are party admissions proving coordination.")
    
    # Include key pages — the counterresponse and temp order
    shayla_counter = EVIDENCE / "court-filings" / "shayla" / "shaylaCounterreponse.pdf"
    shayla_temp = EVIDENCE / "court-filings" / "shayla" / "shaylaTempOrder.pdf"
    if shayla_counter.exists():
        add_pdf(doc, shayla_counter, "Tab 4A — Shayla's counterresponse")
    if shayla_temp.exists():
        add_pdf(doc, shayla_temp, "Tab 4A — Temporary custody order")
    
    # ============================================================
    # TAB 5A — PS Form 3665 (Proof of Mailing)
    # ============================================================
    print("\n[TAB 5A] PS Form 3665 — Proof of Mailing")
    create_tab_page(doc, "TAB 5A",
        "PS Form 3665 — Proof of Mailing",
        "19 pieces mailed September 28, 2026. USPS-stamped proof of mailing. "
        "Court-admissible under MCR 2.107(C)(3). Includes all respondents "
        "and related entities. Cannot be refused, forged, or intercepted.")
    
    # PS3665 — check if filled form exists as PDF
    ps3665_candidates = [
        BASE / "01-case" / "filing-ready" / "PS3665_WAVE1_SEP29.pdf",
        BASE / "01-case" / "evidence" / "PS3665_WAVE1.pdf",
        CASE_EVIDENCE / "ps3665.pdf",
    ]
    found_ps3665 = False
    for p in ps3665_candidates:
        if p.exists():
            add_pdf(doc, p, "Tab 5A — PS Form 3665")
            found_ps3665 = True
            break
    if not found_ps3665:
        # Placeholder — this will be filled in at the post office
        page = doc.new_page(width=W, height=H)
        page.insert_text(fitz.Point(72, 300),
            "PS Form 3665 — TO BE STAMPED AT POST OFFICE",
            fontsize=16, fontname="helv", color=(0.6, 0, 0))
        page.insert_text(fitz.Point(72, 340),
            "This form will be completed at the USPS counter when",
            fontsize=12, fontname="helv", color=(0.4, 0.4, 0.4))
        page.insert_text(fitz.Point(72, 358),
            "spoliation + demand letters are mailed.",
            fontsize=12, fontname="helv", color=(0.4, 0.4, 0.4))
        print("  + PS3665 placeholder (fill at post office)")
    
    # ============================================================
    # TAB 5B — MDE FOIA Response
    # ============================================================
    print("\n[TAB 5B] MDE FOIA Response — Credentialing Fraud")
    create_tab_page(doc, "TAB 5B",
        "MDE FOIA Response — Credentialing Investigation",
        "Received September 25, 2026. 20 files. Confirms February 2022 "
        "investigation of Banks for lacking credentials. MOECS application "
        "#590606 on HOLD. 2hr 24min cover-up. MDE gave loophole instead "
        "of requiring removal. Admin cert issued Sep 2, 2022 — 7 months "
        "after investigation, 3 days after school year started.")
    
    mde_response = EVIDENCE / "mde-foia-sep25" / "MDE_FOIA_RESPONSE_SEP25.pdf"
    mde_investigation = EVIDENCE / "mde-foia-sep25" / "investigation" / "Investigation Letter for Banks.pdf"
    mde_educator = EVIDENCE / "mde-foia-sep25" / "investigation" / "Educator Report Form for Banks.pdf"
    mde_hold = EVIDENCE / "mde-foia-sep25" / "investigation" / "MOECS Admin Permit Hold for Banks.png"
    mde_eem = EVIDENCE / "mde-foia-sep25" / "investigation" / "EEM for Banks.png"
    
    # Just include the key smoking guns, not all 9 audit years
    if mde_response.exists():
        add_pdf(doc, mde_response, "Tab 5B — MDE FOIA cover letter")
    if mde_investigation.exists():
        add_pdf(doc, mde_investigation, "Tab 5B — Investigation letter")
    if mde_educator.exists():
        add_pdf(doc, mde_educator, "Tab 5B — Educator report form")
    if mde_hold.exists():
        add_image(doc, mde_hold, "Tab 5B — MOECS Admin Permit HOLD")
    if mde_eem.exists():
        add_image(doc, mde_eem, "Tab 5B — EEM for Banks")
    
    # ============================================================
    # SAVE
    # ============================================================
    print(f"\n{'=' * 60}")
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")
    
    doc.save(str(OUTPUT), deflate=True, garbage=4)
    doc.close()
    
    size_mb = OUTPUT.stat().st_size / (1024 * 1024)
    print(f"Saved: {OUTPUT}")
    print(f"Size:  {size_mb:.1f} MB")
    print(f"\nCopy to USB along with:")
    print(f"  {EVIDENCE / 'dpd-counter-report' / 'RING_VIDEO_SEP2_2026_ASSAULT.mp4'}")
    print(f"\nDone.")


if __name__ == "__main__":
    main()
