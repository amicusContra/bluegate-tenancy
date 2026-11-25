"""
Split the full OCR into clean chapter files.
Removes Kindle UI artifacts and splits on chapter headings.
v2: Line-based approach, skips TOC block.
"""
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(SCRIPT_DIR, "FULL_BOOK_OCR.md")
OUT_DIR = SCRIPT_DIR

def clean_line(line):
    """Remove Kindle UI artifacts from a single line."""
    # Remove nav arrows
    line = line.replace('(<)', '').replace('(>)', '')
    # Remove stray single-char UI artifacts at line boundaries
    line = re.sub(r'^\s*Q\s*$', '', line)
    line = re.sub(r'^\s*eo\s*$', '', line)
    line = re.sub(r'^\s*@\s*aS\s*$', '', line)
    line = re.sub(r'^\s*WO Q\)\s*$', '', line)
    # Remove page/progress markers
    line = re.sub(r'Page \d+ of \d+\s*[+\-.]*\s*\d*%?', '', line)
    line = re.sub(r'\d+ mins? left in (?:chapter|book)', '', line)
    line = re.sub(r'Learning reading speed\.\.\.', '', line)
    # Remove Kindle header
    line = re.sub(r'D Kindle Library\s*', '', line)
    line = re.sub(r'IT HAD 2 HAPPEN: THE AGONY OF SUCCESS\s*Q?', '', line)
    return line

# Chapter headings and their approximate first-occurrence line in body text
# (after the TOC block which ends around line 145)
CHAPTER_MARKERS = [
    ("Introduction", 160),
    ("A Blended Family", 230),
    ("Whats This Ladys Problem", 380),
    ("Whos My Daddy", 598),
    ("The Wrong Side of the Bench", 770),
    ("Revelation Day", 970),
    ("School and the Extra Push", 1230),
    ("Ds Get Degrees", 1750),
    ("Keeping It Together", 1940),
    ("Bank on Banks", 2090),
    ("From Law Breaker to Law Maker", 2240),
    ("When the Bottom Falls Out", 2380),
    ("Friends How Many of Us Have Them", 2550),
    ("If I Had Known in the Beginning", 2700),
    ("Biography", 2840),
]

def main():
    with open(INPUT, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    print(f"Total lines in OCR file: {total_lines}")
    
    # Clean all lines
    cleaned_lines = [clean_line(l.rstrip()) for l in lines]
    
    # Find actual chapter start lines (skip TOC block, lines < 150)
    chapter_starts = []
    
    # Chapter heading patterns (flexible for OCR errors)
    patterns = [
        (r"Introduction", "Introduction"),
        (r"A Blended Family", "A Blended Family"),
        (r"What.s This Lady.s Problem", "Whats This Ladys Problem"),
        (r"Who.*My Daddy", "Whos My Daddy"),
        (r"The Wrong Side of the Bench", "The Wrong Side of the Bench"),
        (r"Revelation Day", "Revelation Day"),
        (r"School and the Extra Push", "School and the Extra Push"),
        (r"D.s Get Degrees", "Ds Get Degrees"),
        (r"Keeping It Together", "Keeping It Together"),
        (r"Bank on Banks", "Bank on Banks"),
        (r"From Law Breaker to Law Maker", "From Law Breaker to Law Maker"),
        (r"When the Bottom Falls Out", "When the Bottom Falls Out"),
        (r"[Ff]?[ri]*ends.*How Many.*(?:Us|Them)", "Friends How Many of Us Have Them"),
        (r"If I Had Known", "If I Had Known in the Beginning"),
        (r"^Biography\b", "Biography"),
    ]
    
    for pattern, ch_name in patterns:
        for i, line in enumerate(cleaned_lines):
            if i < 150:  # Skip TOC
                continue
            stripped = line.strip()
            if re.search(pattern, stripped, re.IGNORECASE):
                # Check if this is a heading (starts a line or is prominent)
                # Use the approximate line numbers to pick the right one
                for marker_name, approx_line in CHAPTER_MARKERS:
                    if marker_name == ch_name and abs(i - approx_line) < 100:
                        chapter_starts.append((ch_name, i))
                        break
                else:
                    # If no approximate match, still use the first body occurrence
                    if not any(cs[0] == ch_name for cs in chapter_starts):
                        chapter_starts.append((ch_name, i))
                break  # Only take first match after TOC
    
    # Sort by line number
    chapter_starts.sort(key=lambda x: x[1])
    
    print(f"\nFound {len(chapter_starts)} chapters:")
    for ch, line_num in chapter_starts:
        print(f"  Line {line_num}: {ch}")
    
    # Write front matter (everything before Introduction, after header)
    header_end = 8  # Skip the OCR file header
    if chapter_starts:
        intro_line = chapter_starts[0][1]
    else:
        intro_line = total_lines
    
    fm_text = '\n'.join(cleaned_lines[header_end:intro_line])
    fm_text = re.sub(r'\n{3,}', '\n\n', fm_text).strip()
    
    fm_path = os.path.join(OUT_DIR, "00_FRONT_MATTER.md")
    with open(fm_path, 'w', encoding='utf-8') as f:
        f.write("# IT HAD 2 HAPPEN: THE AGONY OF SUCCESS\n")
        f.write("## Front Matter\n")
        f.write("## OCR Transcript from Kindle Cloud Reader screenshots\n\n")
        f.write("---\n\n")
        f.write(fm_text)
        f.write("\n")
    print(f"\nWrote: 00_FRONT_MATTER.md ({len(fm_text.split())} words)")
    
    # Write each chapter
    for idx, (ch_name, start_line) in enumerate(chapter_starts):
        if idx + 1 < len(chapter_starts):
            end_line = chapter_starts[idx + 1][1]
        else:
            end_line = total_lines
        
        ch_text = '\n'.join(cleaned_lines[start_line:end_line])
        ch_text = re.sub(r'\n{3,}', '\n\n', ch_text).strip()
        
        safe_name = re.sub(r'[^\w\s-]', '', ch_name).strip().replace(' ', '_')
        filename = f"{idx + 1:02d}_{safe_name}.md"
        filepath = os.path.join(OUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {ch_name}\n\n")
            f.write("---\n\n")
            f.write(ch_text)
            f.write("\n")
        
        word_count = len(ch_text.split())
        print(f"Wrote: {filename} ({word_count} words)")
    
    print(f"\nDone! {len(chapter_starts)} chapters + front matter")

if __name__ == "__main__":
    main()
