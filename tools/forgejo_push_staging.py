"""
Forgejo Public Record Staging Script
======================================
Stages files from bluegate-tenancy into the publicRecord/detroit
Forgejo repo structure for public release.

PUBLIC RECORD REPO: https://git.primals.eco/publicRecord/detroit
LOCAL CLONE: /home/sporegate/Development/detroit

WHAT GOES PUBLIC:
- Filed complaints (already submitted to courts/agencies)
- Federal master packet (once sent to agencies)
- Journalist packet (designed for public consumption)
- OIG complaints and supplements
- Evidence PDFs that support filed complaints
- Timeline/chronology documents

WHAT STAYS PRIVATE (OPERATIONAL):
- Strategy documents (battle plans, assessment, deployment day)
- OSINT scrape raw results (operational intelligence)
- DaSean briefing (private strategy)
- Book transcripts (copyright)
- PACER scraper tools + credentials
- PPO tracker, checklists (operational)

STRUCTURE:
  filings/           → Court filings, complaints, motions
  correspondence/    → Letters, emails, agent communications
  evidence/          → Documentary evidence, financial records, org charts
  foia/              → FOIA requests and responses
  timeline/          → Chronological event summaries
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

PROJECT = Path(r"C:\Users\mokke\jobHunt\bluegate-tenancy")
STAGING = PROJECT / "tools" / "_forgejo_staging"

STAGING_MAP = {
    "filings": [
        {
            "src": "01-case/filing-ready/FEDERAL_MASTER_PACKET_SEP18.pdf",
            "dst": "2026-09-22_federal_master_packet.pdf",
            "commit_msg": "filing: Federal Multi-Agency Intelligence Packet — Banks Network RICO pattern",
            "public_on": "deployment day (Sep 22)",
        },
        {
            "src": "01-case/filing-ready/JOURNALIST_PACKET_SEP22.pdf",
            "dst": "2026-09-22_journalist_briefing_packet.pdf",
            "commit_msg": "filing: Journalist briefing packet — 7 investigative story angles",
            "public_on": "deployment day (Sep 22)",
        },
        {
            "src": "01-case/filing-ready/OIG_SUPPLEMENT_FORGERY_SEP17.md",
            "dst": "2026-09-17_oig_supplement_forgery.md",
            "commit_msg": "filing: DOE OIG supplement — credential forgery evidence",
            "public_on": "already filed",
        },
        {
            "src": "01-case/filing-ready/COMPLAINT_CHAIN_MASTER_SEP16.md",
            "dst": "2026-09-16_complaint_chain_master.md",
            "commit_msg": "filing: Master complaint chain — all filed complaints and their relationships",
            "public_on": "already filed",
        },
        {
            "src": "01-case/filing-ready/MOTION_ALTERNATIVE_SERVICE_SEP17.md",
            "dst": "2026-09-17_motion_alternative_service.md",
            "commit_msg": "filing: Motion for alternative service — Banks PPO",
            "public_on": "already filed",
        },
    ],
    "evidence": [
        {
            "src": "01-case/evidence/OIG_SUPPLEMENT_PROOF_PACKAGE_SEP17.pdf",
            "dst": "2026-09-17_oig_supplement_proof_package.pdf",
            "commit_msg": "evidence: OIG proof package — credential forgery documentary evidence",
            "public_on": "already filed with DOE OIG",
        },
        {
            "src": "01-case/evidence/RING_EXHIBIT_KEYFRAMES_SEP2.pdf",
            "dst": "2026-09-02_ring_exhibit_keyframes.pdf",
            "commit_msg": "evidence: Ring camera keyframes — physical evidence of assault",
            "public_on": "already filed with court",
        },
    ],
    "correspondence": [
        {
            "src": "01-case/filing-ready/BANKS_PPO_EMAIL_READY.txt",
            "dst": "2026-09-18_banks_ppo_service_email.txt",
            "commit_msg": "correspondence: PPO service notification sent to Banks via email",
            "public_on": "already sent",
        },
    ],
    "timeline": [],
}


def stage():
    """Stage files into Forgejo repo structure."""
    if STAGING.exists():
        shutil.rmtree(STAGING)

    print(f"Staging to: {STAGING}\n")

    push_commands = []
    total_size = 0

    for category, files in STAGING_MAP.items():
        cat_dir = STAGING / category
        cat_dir.mkdir(parents=True, exist_ok=True)

        for item in files:
            src = PROJECT / item["src"]
            dst = cat_dir / item["dst"]

            if src.exists():
                shutil.copy2(src, dst)
                size = dst.stat().st_size
                total_size += size
                print(f"  OK {category}/{item['dst']} ({size:,} bytes)")
                print(f"    Public on: {item['public_on']}")

                push_commands.append({
                    "file": f"{category}/{item['dst']}",
                    "msg": item["commit_msg"],
                })
            else:
                print(f"  MISSING: {item['src']}")

    push_script = STAGING / "PUSH_COMMANDS.sh"
    with open(push_script, "w", encoding="utf-8") as f:
        f.write("#!/bin/bash\n")
        f.write("# Forgejo Public Record Push Script\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"# Repo: https://git.primals.eco/publicRecord/detroit\n")
        f.write(f"# Local: /home/sporegate/Development/detroit\n\n")
        f.write("set -e\n\n")
        f.write("cd ~/Development/detroit\n\n")
        f.write("# Verify we're in the right repo\n")
        f.write('echo "Current remote:"\n')
        f.write("git remote -v\n")
        f.write('echo ""\n\n')

        for cmd in push_commands:
            f.write(f'# {cmd["file"]}\n')
            f.write(f'cp /path/to/staged/{cmd["file"]} {cmd["file"]}\n')
            f.write(f'git add {cmd["file"]}\n')
            f.write(f'git commit -m "{cmd["msg"]}"\n')
            f.write(f'echo "Committed: {cmd["file"]}"\n\n')

        f.write("# Push all at once\n")
        f.write("git push\n")
        f.write(f'echo "\\nAll {len(push_commands)} files pushed to git.primals.eco"\n')
        f.write('echo "Verify at: https://git.primals.eco/publicRecord/detroit"\n')

    manifest = STAGING / "MANIFEST.md"
    with open(manifest, "w", encoding="utf-8") as f:
        f.write("# FORGEJO PUBLIC RECORD — STAGING MANIFEST\n")
        f.write(f"## Generated: {datetime.now().strftime('%B %d, %Y %H:%M')}\n")
        f.write(f"## Repo: https://git.primals.eco/publicRecord/detroit\n\n")
        f.write("---\n\n")

        f.write("## FILES TO PUSH\n\n")
        f.write("| # | Category | Filename | Size | Status |\n")
        f.write("|---|----------|----------|------|--------|\n")

        for i, cmd in enumerate(push_commands, 1):
            cat, fn = cmd["file"].split("/", 1)
            src_file = STAGING / cmd["file"]
            size = f"{src_file.stat().st_size:,} B" if src_file.exists() else "?"
            f.write(f"| {i} | {cat} | `{fn}` | {size} | Ready |\n")

        f.write(f"\n**Total files:** {len(push_commands)}\n")
        f.write(f"**Total size:** {total_size:,} bytes ({total_size/1024:.0f} KB)\n\n")

        f.write("---\n\n")
        f.write("## WHAT STAYS PRIVATE (DO NOT PUSH)\n\n")
        f.write("| Item | Why |\n")
        f.write("|------|-----|\n")
        f.write("| Strategy docs (battle plan, assessment) | Operational intelligence |\n")
        f.write("| DaSean briefing | Private strategy communication |\n")
        f.write("| OSINT scrape results | Raw operational data |\n")
        f.write("| Book transcripts (Banks, BMF) | Copyright + analysis methodology |\n")
        f.write("| PACER scrapers + credentials | Tool security |\n")
        f.write("| PPO tracker, checklists | Operational status |\n")
        f.write("| Deployment day plan | Timing/tactical intelligence |\n")
        f.write("| SCRAPING_MATRIX | Operational methodology |\n\n")

        f.write("---\n\n")
        f.write("## PUSH SEQUENCE\n\n")
        f.write("### Option A: From Windows (if Forgejo SSH is configured)\n")
        f.write("```powershell\n")
        f.write("# Add Forgejo remote to bluegate-tenancy\n")
        f.write("cd C:\\Users\\mokke\\jobHunt\\bluegate-tenancy\n")
        f.write("# This won't work directly — different repo structure\n")
        f.write("# Use Option B instead\n")
        f.write("```\n\n")

        f.write("### Option B: From Server (recommended)\n")
        f.write("```bash\n")
        f.write("# 1. SSH into primals.eco server\n")
        f.write("ssh sporegate@primals.eco\n\n")
        f.write("# 2. Navigate to local clone\n")
        f.write("cd ~/Development/detroit\n\n")
        f.write("# 3. Transfer staged files (from Windows via scp/rsync)\n")
        f.write("# From Windows:\n")
        f.write('#   scp -r C:\\Users\\mokke\\jobHunt\\bluegate-tenancy\\tools\\_forgejo_staging\\* sporegate@primals.eco:~/Development/detroit/\n\n')
        f.write("# 4. Or run the push script\n")
        f.write("bash PUSH_COMMANDS.sh\n")
        f.write("```\n\n")

        f.write("### Option C: Direct git push from server with manual file drops\n")
        f.write("```bash\n")
        f.write("cd ~/Development/detroit\n")
        f.write("# Copy each file into the right directory, commit, push\n")
        f.write("# See PUSH_COMMANDS.sh for individual commit messages\n")
        f.write("```\n\n")

        f.write("---\n\n")
        f.write("## DEPLOYMENT DAY INTEGRATION\n\n")
        f.write("Add as **Phase 0** of Deployment Day (before portal submissions):\n\n")
        f.write("1. Push all files to Forgejo\n")
        f.write("2. Verify public access at https://git.primals.eco/publicRecord/detroit\n")
        f.write("3. Include the repo URL in journalist emails:\n")
        f.write('   > "Full evidence with git provenance: https://git.primals.eco/publicRecord/detroit"\n')
        f.write("4. Each agency email can also reference the public repo\n")
        f.write("5. The git commit hashes serve as tamper-evident timestamps\n")

    print(f"\n{'='*60}")
    print(f"Staged {len(push_commands)} files ({total_size:,} bytes)")
    print(f"Manifest: {manifest}")
    print(f"Push script: {push_script}")
    print(f"{'='*60}")


if __name__ == "__main__":
    stage()
