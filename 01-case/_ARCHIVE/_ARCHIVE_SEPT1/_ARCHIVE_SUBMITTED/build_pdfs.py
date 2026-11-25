"""Build print-ready PDFs for JTC + UPL exhibit packets."""
import os
from pathlib import Path
from PIL import Image

EXHIBITS = Path(r"c:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready\exhibits")

def images_to_pdf(image_dir: Path, output_path: Path):
    """Convert a folder of PNGs/JPEGs to a single PDF, one image per page, fit to letter."""
    LETTER_W, LETTER_H = 2550, 3300  # 8.5x11 at 300 DPI

    imgs = sorted(
        [f for f in image_dir.iterdir() if f.suffix.lower() in ('.png', '.jpg', '.jpeg')],
        key=lambda x: x.name
    )
    if not imgs:
        print(f"  No images found in {image_dir}")
        return

    pages = []
    for img_path in imgs:
        img = Image.open(img_path).convert("RGB")
        
        # Scale to fit letter page with margins (0.5in = 150px at 300dpi)
        max_w = LETTER_W - 300
        max_h = LETTER_H - 300
        ratio = min(max_w / img.width, max_h / img.height)
        new_w = int(img.width * ratio)
        new_h = int(img.height * ratio)
        img_resized = img.resize((new_w, new_h), Image.LANCZOS)
        
        # Center on white letter page
        page = Image.new("RGB", (LETTER_W, LETTER_H), "white")
        x = (LETTER_W - new_w) // 2
        y = (LETTER_H - new_h) // 2
        page.paste(img_resized, (x, y))
        pages.append(page)

    pages[0].save(output_path, save_all=True, append_images=pages[1:], resolution=300)
    print(f"  {output_path.name}: {len(pages)} pages")


def combine_markdown(md_files: list[Path], output_path: Path):
    """Concatenate markdown files with page-break markers between them."""
    combined = []
    for f in md_files:
        combined.append(f.read_text(encoding="utf-8"))
        combined.append("\n\n---\n*PAGE BREAK — Print next section on new page*\n---\n\n")
    output_path.write_text("".join(combined), encoding="utf-8")
    print(f"  {output_path.name}: {len(md_files)} documents combined")


# PACKET A — UPL
print("PACKET A — UPL")
packet_a = EXHIBITS / "PACKET_A_UPL"
a_docs = sorted([
    f for f in packet_a.iterdir()
    if f.suffix == '.md' and f.is_file()
], key=lambda x: x.name)
combine_markdown(a_docs, packet_a / "PRINT_ALL_DOCS.md")
images_to_pdf(packet_a / "linkedin", packet_a / "PRINT_LINKEDIN_EXHIBITS.pdf")

# PACKET BC — JTC COMBINED
print("PACKET BC — JTC COMBINED")
packet_bc = EXHIBITS / "PACKET_BC_JTC_COMBINED"
bc_docs = sorted([
    f for f in packet_bc.iterdir()
    if f.suffix == '.md' and f.is_file()
], key=lambda x: x.name)
combine_markdown(bc_docs, packet_bc / "PRINT_ALL_DOCS.md")
images_to_pdf(packet_bc / "linkedin", packet_bc / "PRINT_LINKEDIN_EXHIBITS.pdf")

print("\nDone. Two files per packet:")
print("  PRINT_ALL_DOCS.md    — open and print (text)")
print("  PRINT_LINKEDIN_EXHIBITS.pdf — open and print (images)")

