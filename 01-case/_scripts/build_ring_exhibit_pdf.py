"""
Build a print-ready PDF of the Ring doorbell video evidence:
  Page 1-2: Contact sheet of 15 critical frames (4 per page)
  Page 3+:  Frame-by-frame narrative with timestamps
  
Output: RING_EXHIBIT_KEYFRAMES_SEP2.pdf
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import black, white, HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

RING_DIR = os.path.join(os.path.dirname(__file__), 
    '..', '..', '02-evidence', 'ring_sep2')
DENSE_DIR = os.path.join(RING_DIR, 'dense_frames')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__),
    '..', '..', '..', 'Desktop', 'DETROIT_PRINT_SEP17')
OUTPUT_PATH = os.path.join(OUTPUT_DIR, 'RING_EXHIBIT_KEYFRAMES_SEP2.pdf')

# Also save a copy in the evidence folder
EVIDENCE_COPY = os.path.join(os.path.dirname(__file__),
    '..', 'evidence', 'RING_EXHIBIT_KEYFRAMES_SEP2.pdf')

KEY_FRAMES = [
    ("ring_000s.png", "0s — 23:06:58", "Father ALONE on porch — he was there first"),
    ("ring_008s.png", "8s — 23:07:06", "Two people — Shayla has arrived"),
    ("ring_010s.png", "10s — 23:07:08", "Father shouting 'CALL THE POLICE'"),
    ("ring_018s.png", "18s — 23:07:15", "Deanna restraining father (fear of Smiths)"),
    ("ring_025s.png", "25s — 23:07:22", "Leon (blue) approaching — three people"),
    ("ring_027s.png", "27s — 23:07:24", "★ Deanna grabbing father's arm before impact"),
    ("ring_028s.png", "28s — 23:07:25", "★★ IMPACT — body driven toward door"),
    ("ring_030s.png", "30s — 23:07:27", "★★ Father's body PRESSED against Ring camera"),
    ("ring_032s.png", "32s — 23:07:29", "Aftermath — 'Love and Protect' shirt visible"),
    ("ring_034s.png", "34s — 23:07:31", "Leon (blue) visible behind father"),
    ("ring_038s.png", "38s — 23:07:35", "★★ Shayla ON PHONE during assault"),
    ("ring_040s.png", "40s — 23:07:37", "★★ CHILD WITH BRAIDS visible on porch"),
    ("ring_044s.png", "44s — 23:07:42", "Mass scene — children being taken to car"),
    ("ring_049s.png", "49s — 23:07:47", "★ Shayla on phone — children GONE"),
    ("ring_059s.png", "59s — 23:07:57", "Aftermath — Shayla still on phone"),
]

def find_frame(filename):
    """Find a frame file in dense_frames or overview frames."""
    # Map from analysis naming to actual file naming
    # Analysis uses ring_000s.png, files are ring_00m00s.png (overview) 
    # or frame_00000.png style (dense)
    
    # Try dense_frames first - these are 1-sec interval
    sec = filename.replace("ring_", "").replace("s.png", "")
    sec_num = int(sec)
    
    # Dense frames naming pattern
    for pattern in [
        os.path.join(DENSE_DIR, f"frame_{sec_num:05d}.png"),
        os.path.join(DENSE_DIR, f"ring_{sec_num:03d}s.png"),
        os.path.join(DENSE_DIR, f"frame_{sec_num}.png"),
    ]:
        if os.path.exists(pattern):
            return pattern
    
    # Overview frames: ring_00m00s.png style
    mins = sec_num // 60
    secs = sec_num % 60
    overview = os.path.join(RING_DIR, f"ring_{mins:02d}m{secs:02d}s.png")
    if os.path.exists(overview):
        return overview
    
    # Try exact filename
    exact = os.path.join(RING_DIR, filename)
    if os.path.exists(exact):
        return exact
    exact2 = os.path.join(DENSE_DIR, filename)
    if os.path.exists(exact2):
        return exact2
        
    return None

def draw_header(c, page_w, page_h, title, subtitle=None):
    """Draw exhibit header on page."""
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(page_w/2, page_h - 0.6*inch, title)
    if subtitle:
        c.setFont("Helvetica", 9)
        c.drawCentredString(page_w/2, page_h - 0.85*inch, subtitle)

def draw_footer(c, page_w, page_num):
    """Draw page footer."""
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor("#666666"))
    c.drawCentredString(page_w/2, 0.4*inch, 
        f"Ring Doorbell Evidence — Sep 2, 2026, 23:06:58-23:07:57 EDT — "
        f"XXXX Cornerstone Blvd, Detroit MI — Page {page_num}")

def build_contact_sheets(c, page_w, page_h):
    """Build contact sheet pages with 4 frames per page."""
    frames_per_page = 4
    img_w = 3.2 * inch
    img_h = 1.8 * inch  # 16:9 ratio
    margin_x = (page_w - 2*img_w) / 3
    
    page_num = 0
    for page_start in range(0, len(KEY_FRAMES), frames_per_page):
        page_num += 1
        page_frames = KEY_FRAMES[page_start:page_start+frames_per_page]
        
        draw_header(c, page_w, page_h, 
            "EXHIBIT A-2: RING DOORBELL KEY FRAMES",
            f"September 2, 2026 — XXXX Cornerstone Blvd, Detroit MI 48201 — "
            f"Page {page_num} of {(len(KEY_FRAMES)+frames_per_page-1)//frames_per_page}")
        
        # 2x2 grid
        positions = []
        row_height = (page_h - 1.5*inch) / 2
        for row in range(2):
            for col in range(2):
                x = margin_x + col * (img_w + margin_x)
                y = page_h - 1.3*inch - row * (img_h + 1.0*inch)
                positions.append((x, y))
        
        for idx, (filename, timestamp, caption) in enumerate(page_frames):
            if idx >= len(positions):
                break
            x, y = positions[idx]
            
            frame_path = find_frame(filename)
            if frame_path and os.path.exists(frame_path):
                try:
                    c.drawImage(frame_path, x, y - img_h, 
                               width=img_w, height=img_h,
                               preserveAspectRatio=True)
                    # Border
                    c.setStrokeColor(black)
                    c.setLineWidth(0.5)
                    c.rect(x, y - img_h, img_w, img_h, stroke=1, fill=0)
                except Exception as e:
                    c.setFont("Helvetica", 8)
                    c.drawString(x + 5, y - img_h/2, f"[Frame: {filename}]")
            else:
                c.setFont("Helvetica-Oblique", 8)
                c.setFillColor(HexColor("#999999"))
                c.drawString(x + 5, y - img_h/2, f"[Frame not found: {filename}]")
                c.setFillColor(black)
            
            # Frame number + timestamp
            frame_num = page_start + idx + 1
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(black)
            c.drawString(x, y - img_h - 12, 
                f"Frame {frame_num}/15 — {timestamp}")
            
            # Caption
            c.setFont("Helvetica", 8)
            star = "★ " if "★" in caption else ""
            clean_caption = caption.replace("★★ ", "").replace("★ ", "")
            if star:
                c.setFillColor(HexColor("#CC0000"))
                c.drawString(x, y - img_h - 24, f"★ {clean_caption}")
                c.setFillColor(black)
            else:
                c.drawString(x, y - img_h - 24, clean_caption)
        
        draw_footer(c, page_w, page_num)
        c.showPage()
    
    return page_num

def build_narrative_pages(c, page_w, page_h, start_page):
    """Build the narrative analysis pages."""
    page_num = start_page
    
    sections = [
        ("WHAT THE VIDEO PROVES", [
            "1. Father was there FIRST and was NOT the aggressor (alone at 23:06:58)",
            "2. Father's FIRST response: 'Call the police, mom, call the police' (audio 9-15s)",
            "3. Leon A. Smith physically ASSAULTED the father (frames 27-32s, body into door)",
            "4. Shayla Smith COORDINATED the operation by phone (on phone at 38s, 49s, 59s)",
            "5. Shayla DEMANDED children from Deanna, ignoring the father entirely",
            "6. Leon had NO legal right — 'give me my grandkids' is not a custody order",
            "7. Deanna restrained her own son out of FEAR (frames 18s, 27s)",
            "8. CHILDREN PRESENT during violence — child with braids visible at 40s",
            "9. Children taken in under 60 seconds (visible 40s, gone 49s)",
            "10. Father's shirt: 'Love and Protect the Mind Body and Spirit'",
        ]),
        ("AUDIO TRANSCRIPT (OpenAI Whisper, verified by eyewitness)", [
            "[1.32s]  Father: 'No' — telling Shayla she cannot take the children",
            "[9-15s]  Father: 'Call the police, call the police, MOM, call the police'",
            "[15-18s] Father/Deanna: 'Yes, we're gonna call them man'",
            "[~0-8s]  Leon Smith: 'Give me my grandkids' (eyewitness, below mic threshold)",
            "[56s]    Unknown: 'Let's go' — Smith party departing with children",
        ]),
        ("THE COORDINATED ASSAULT PATTERN", [
            "Leon Smith = the MUSCLE (physical force, assault on father)",
            "Shayla Smith = the COORDINATOR (phone, directing operations, calm throughout)",
            "Roles were PRE-ASSIGNED: Leon engaged father while Shayla called children out",
            "Shayla's constant phone use suggests off-site communication/direction",
            "This was NOT a custody dispute — it was a planned forcible taking",
        ]),
        ("RETALIATION TIMELINE", [
            "Aug 18 — Kevin sends 6 certified letters to Smith family",
            "Aug 21 — 4 letters intercepted at Harper Woods PO (Leon's station)",
            "Aug 25 — 'You guys are not that smart' text via Leon's phone",
            "Aug 26 — USPS OIG complaint filed (#174517 / #202990)",
            "Aug 27 — Civil suit filed: Mok v. Smith (Ingham 4301)",
            "Sep 1  — Banks served, calls DaSean to threaten",
            "SEP 2  — ★★ LEON ASSAULTS DaSEAN; SHAYLA TAKES CHILDREN ★★",
            "Sep 3  — Shayla files emergency motion — OMITS the assault entirely",
            "Sep 9  — Second incident at PCA (DPD #26-0909-0176)",
            "Sep 13 — Counter-report filed at 3rd Precinct (Lt. White + Sgt. White)",
            "Sep 15 — Leon texts 'Good luck' then 'see you in court'",
        ]),
        ("AI METHODOLOGY DISCLOSURE", [
            "61 frames extracted at 1-sec intervals via OpenCV (mechanical, no AI judgment)",
            "Audio extracted via ffmpeg 9.0.1, transcribed by OpenAI Whisper (medium, 769M params)",
            "Initial visual analysis by Claude (Anthropic) — described events, misidentified persons",
            "Human verification Sep 3, 2026: petitioner corrected all person identifications",
            "AI correctly observed all PHYSICAL EVENTS; human corrected WHO was who",
            "Raw Whisper JSON and all frame files preserved for independent verification",
            "Original video file (I-qmwA9uNzjOvM7B.MOV, 63.3MB, 1280x720) available to Court",
        ]),
    ]
    
    page_num += 1
    y = page_h - 0.5*inch
    
    draw_header(c, page_w, page_h, 
        "RING DOORBELL VIDEO ANALYSIS — NARRATIVE SUMMARY",
        "September 2, 2026 — 23:06:58–23:07:57 EDT — XXXX Cornerstone Blvd, Detroit MI")
    y -= 0.6*inch
    
    for section_title, items in sections:
        if y < 2*inch:
            draw_footer(c, page_w, page_num)
            c.showPage()
            page_num += 1
            y = page_h - 0.5*inch
            draw_header(c, page_w, page_h,
                "RING DOORBELL VIDEO ANALYSIS — NARRATIVE SUMMARY (cont.)")
            y -= 0.5*inch
        
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(black)
        c.drawString(0.75*inch, y, section_title)
        y -= 6
        c.setStrokeColor(black)
        c.setLineWidth(0.5)
        c.line(0.75*inch, y, page_w - 0.75*inch, y)
        y -= 16
        
        c.setFont("Helvetica", 9)
        for item in items:
            if y < 1*inch:
                draw_footer(c, page_w, page_num)
                c.showPage()
                page_num += 1
                y = page_h - 0.5*inch
                draw_header(c, page_w, page_h,
                    "RING DOORBELL VIDEO ANALYSIS — NARRATIVE SUMMARY (cont.)")
                y -= 0.5*inch
            
            if "★★" in item:
                c.setFont("Helvetica-Bold", 9)
                c.setFillColor(HexColor("#CC0000"))
            elif item.startswith("SEP 2"):
                c.setFont("Helvetica-Bold", 9)
                c.setFillColor(HexColor("#CC0000"))
            else:
                c.setFont("Helvetica", 9)
                c.setFillColor(black)
            
            c.drawString(1*inch, y, item)
            y -= 14
            c.setFillColor(black)
        
        y -= 10
    
    # Final statement
    if y < 3*inch:
        draw_footer(c, page_w, page_num)
        c.showPage()
        page_num += 1
        y = page_h - 1*inch
    
    y -= 10
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.75*inch, y, "CASE REFERENCES:")
    y -= 16
    c.setFont("Helvetica", 9)
    refs = [
        "PPO Cases: 26-000000-4432-PP, 4433-PH, 4434-PH, 4436-PH (Ingham, Hon. Koenig)",
        "Civil: 2026-4301-CZ Mok v. Smith et al. (Ingham, Hon. Stokes)",
        "Civil: 2026-4349-CZ Mok v. Banks et al. (Ingham, Hon. Stokes)",
        "Custody: 26-108221-DC Smith v. Mitchell (Wayne, Hon. Triplett)",
        "DPD Report: #26-0909-0176 (Sep 9, 2026)",
        "USPS OIG: #174517 / #202990",
    ]
    for ref in refs:
        c.drawString(1*inch, y, ref)
        y -= 13
    
    y -= 16
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(0.75*inch, y, 
        "Prepared by Kevin Mok, pro se, on behalf of Petitioner DaSean Mitchell")
    y -= 12
    c.drawString(0.75*inch, y, 
        "AI tools: OpenCV, ffmpeg, OpenAI Whisper, Claude (Anthropic)")
    y -= 12
    c.drawString(0.75*inch, y, 
        "Human verification: Petitioner's eyewitness review, September 3, 2026")
    
    draw_footer(c, page_w, page_num)
    return page_num

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    page_w, page_h = letter
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)
    c.setTitle("Ring Doorbell Evidence — September 2, 2026")
    c.setAuthor("Kevin Mok")
    c.setSubject("Assault at XXXX Cornerstone Blvd, Detroit MI")
    
    # Build contact sheets (15 frames, ~4 pages)
    last_page = build_contact_sheets(c, page_w, page_h)
    
    # Build narrative pages
    last_page = build_narrative_pages(c, page_w, page_h, last_page)
    
    c.save()
    print(f"DONE Built: {OUTPUT_PATH}")
    print(f"   Pages: {last_page}")
    
    # Copy to evidence folder too
    os.makedirs(os.path.dirname(EVIDENCE_COPY), exist_ok=True)
    import shutil
    shutil.copy2(OUTPUT_PATH, EVIDENCE_COPY)
    print(f"DONE Copy:  {EVIDENCE_COPY}")

if __name__ == "__main__":
    main()
