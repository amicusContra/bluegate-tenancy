#!/bin/bash
# Forgejo Public Record Push Script
# Generated: 2026-09-19 07:45
# Repo: https://git.primals.eco/publicRecord/detroit
# Local: /home/sporegate/Development/detroit

set -e

cd ~/Development/detroit

# Verify we're in the right repo
echo "Current remote:"
git remote -v
echo ""

# filings/2026-09-22_federal_master_packet.pdf
cp /path/to/staged/filings/2026-09-22_federal_master_packet.pdf filings/2026-09-22_federal_master_packet.pdf
git add filings/2026-09-22_federal_master_packet.pdf
git commit -m "filing: Federal Multi-Agency Intelligence Packet — Banks Network RICO pattern"
echo "Committed: filings/2026-09-22_federal_master_packet.pdf"

# filings/2026-09-22_journalist_briefing_packet.pdf
cp /path/to/staged/filings/2026-09-22_journalist_briefing_packet.pdf filings/2026-09-22_journalist_briefing_packet.pdf
git add filings/2026-09-22_journalist_briefing_packet.pdf
git commit -m "filing: Journalist briefing packet — 7 investigative story angles"
echo "Committed: filings/2026-09-22_journalist_briefing_packet.pdf"

# filings/2026-09-17_oig_supplement_forgery.md
cp /path/to/staged/filings/2026-09-17_oig_supplement_forgery.md filings/2026-09-17_oig_supplement_forgery.md
git add filings/2026-09-17_oig_supplement_forgery.md
git commit -m "filing: DOE OIG supplement — credential forgery evidence"
echo "Committed: filings/2026-09-17_oig_supplement_forgery.md"

# filings/2026-09-16_complaint_chain_master.md
cp /path/to/staged/filings/2026-09-16_complaint_chain_master.md filings/2026-09-16_complaint_chain_master.md
git add filings/2026-09-16_complaint_chain_master.md
git commit -m "filing: Master complaint chain — all filed complaints and their relationships"
echo "Committed: filings/2026-09-16_complaint_chain_master.md"

# filings/2026-09-17_motion_alternative_service.md
cp /path/to/staged/filings/2026-09-17_motion_alternative_service.md filings/2026-09-17_motion_alternative_service.md
git add filings/2026-09-17_motion_alternative_service.md
git commit -m "filing: Motion for alternative service — Banks PPO"
echo "Committed: filings/2026-09-17_motion_alternative_service.md"

# evidence/2026-09-17_oig_supplement_proof_package.pdf
cp /path/to/staged/evidence/2026-09-17_oig_supplement_proof_package.pdf evidence/2026-09-17_oig_supplement_proof_package.pdf
git add evidence/2026-09-17_oig_supplement_proof_package.pdf
git commit -m "evidence: OIG proof package — credential forgery documentary evidence"
echo "Committed: evidence/2026-09-17_oig_supplement_proof_package.pdf"

# evidence/2026-09-02_ring_exhibit_keyframes.pdf
cp /path/to/staged/evidence/2026-09-02_ring_exhibit_keyframes.pdf evidence/2026-09-02_ring_exhibit_keyframes.pdf
git add evidence/2026-09-02_ring_exhibit_keyframes.pdf
git commit -m "evidence: Ring camera keyframes — physical evidence of assault"
echo "Committed: evidence/2026-09-02_ring_exhibit_keyframes.pdf"

# correspondence/2026-09-18_banks_ppo_service_email.txt
cp /path/to/staged/correspondence/2026-09-18_banks_ppo_service_email.txt correspondence/2026-09-18_banks_ppo_service_email.txt
git add correspondence/2026-09-18_banks_ppo_service_email.txt
git commit -m "correspondence: PPO service notification sent to Banks via email"
echo "Committed: correspondence/2026-09-18_banks_ppo_service_email.txt"

# Push all at once
git push
echo "\nAll 8 files pushed to git.primals.eco"
echo "Verify at: https://git.primals.eco/publicRecord/detroit"
