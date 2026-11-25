$pkt = "C:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready\exhibits\PACKET_E_BANKS_LAWSUIT"
$ev  = "C:\Users\mokke\jobHunt\bluegate-tenancy\02-evidence"
$ex  = "C:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready\exhibits"

# A - Parental Authorization
Copy-Item "$ev\case-docs\DASEAN_PCA_AUTHORIZATION.pdf" "$pkt\A_PARENTAL_AUTHORIZATION.pdf"

# B - LinkedIn screenshots
Copy-Item "$ev\banks-linkedin\*" "$pkt\B_linkedin\" -Force

# D - Elrick July 2022
Copy-Item "$ex\EXHIBIT_ELRICK_FREEP_JULY2022.md" "$pkt\D_ELRICK_FREEP_JULY2022.md"

# E - PCA Founder page
Copy-Item "$ex\EXHIBIT_PCA_FOUNDER_PAGE.md" "$pkt\E_PCA_FOUNDER_PAGE.md"

# H - OSINT Brief
Copy-Item "$ex\EXHIBIT_BANKS_OSINT_BRIEF.md" "$pkt\H_BANKS_OSINT_BRIEF.md"

# I - UPL receipt
Copy-Item "$ev\mail-receipts\UPL_DROPOFF_RECEIPT_AUG31.pdf" "$pkt\I_UPL_RECEIPT_AUG31.pdf"

# J/K - JTC certified mail + notary
Copy-Item "$ev\mail-receipts\JTC_CERTIFIED_MAIL_AUG31.pdf" "$pkt\JK_JTC_CERTIFIED_MAIL.pdf"
Copy-Item "$ev\mail-receipts\JTC_NOTARY_AUG31.pdf" "$pkt\JK_JTC_NOTARY.pdf"

# P - Amended complaint filed
Copy-Item "$ev\case-docs\INGHAM_AMENDED_FILED_AUG31.pdf" "$pkt\P_AMENDED_COMPLAINT_FILED.pdf"

# R - PCA orientation materials
Copy-Item "$ev\pca-orientation\IMG_5792.jpeg" "$pkt\R1_PCA_ORIENTATION_ARRIVAL.jpeg"
Copy-Item "$ev\pca-orientation\IMG_5793.jpeg" "$pkt\R2_PCA_ORIENTATION_UNIFORM.jpeg"

# S - MacDowell Board
Copy-Item "$ex\EXHIBIT_MACDOWELL_BOARD.md" "$pkt\S_MACDOWELL_BOARD.md"

# T - Chalkbeat
Copy-Item "$ex\EXHIBIT_CHALKBEAT_SEPT2025.md" "$pkt\T_CHALKBEAT_SEPT2025.md"

# U - keepjudgemiller
Copy-Item "$ex\EXHIBIT_KEEPJUDGEMILLER.md" "$pkt\U_KEEPJUDGEMILLER.md"

# V - Ballotpedia
Copy-Item "$ex\EXHIBIT_BALLOTPEDIA_YANCEY.md" "$pkt\V1_BALLOTPEDIA_YANCEY.md"
Copy-Item "$ex\EXHIBIT_BALLOTPEDIA_MILLER.md" "$pkt\V2_BALLOTPEDIA_MILLER.md"

# W - Property report
Copy-Item "$ev\property-records\*Dresden*" "$pkt\W_PROPERTY_REPORT_DRESDEN.pdf"

Write-Host "Banks lawsuit packet staged. Missing exhibits to add tomorrow:"
Write-Host "  C - State Bar member directory screenshot"
Write-Host "  F - Banks admin certificate (use Elrick Aug 2023 or MDE MOECS)"
Write-Host "  G - LARA corporate filings screenshots"
Write-Host "  L - MDE receipt (get tomorrow)"
Write-Host "  M - AG receipt (get tomorrow)"
Write-Host "  N - DPSCD sent email screenshot"
Write-Host "  O - USPS OIG confirmation screenshot"
Write-Host "  Q - Leon Smith text screenshots (select from text-screenshots folder)"

