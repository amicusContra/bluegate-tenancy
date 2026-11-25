$fr = "C:\Users\mokke\jobHunt\bluegate-tenancy\01-case\filing-ready"
$pt = "$fr\PRINT_TOMORROW"
$sub = "$fr\SUBMITTED_AUG31"
$pkt = "$fr\exhibits\PACKET_E_BANKS_LAWSUIT"

# === BANKS LAWSUIT — copy complaint + print files ===
Copy-Item "$fr\39_KEVIN_V_BANKS_COMPLAINT.txt" "$pt\BANKS_LAWSUIT\01_COMPLAINT.txt"
Copy-Item "$pkt\PRINT_ALL_TEXT_EXHIBITS.md" "$pt\BANKS_LAWSUIT\02_TEXT_EXHIBITS.md"
Copy-Item "$pkt\PRINT_ALL_IMAGE_EXHIBITS.pdf" "$pt\BANKS_LAWSUIT\03_IMAGE_EXHIBITS.pdf"
Copy-Item "$pkt\A_PARENTAL_AUTHORIZATION.pdf" "$pt\BANKS_LAWSUIT\04_EXHIBIT_A.pdf"
Copy-Item "$pkt\I_UPL_RECEIPT_AUG31.pdf" "$pt\BANKS_LAWSUIT\05_EXHIBIT_I.pdf"
Copy-Item "$pkt\JK_JTC_CERTIFIED_MAIL.pdf" "$pt\BANKS_LAWSUIT\06_EXHIBIT_JK_CERT.pdf"
Copy-Item "$pkt\JK_JTC_NOTARY.pdf" "$pt\BANKS_LAWSUIT\07_EXHIBIT_JK_NOTARY.pdf"

# === MDE PACKET ===
Copy-Item "$fr\36D_MDE_CERT_VIOLATION.md" "$pt\MDE_PACKET\01_MDE_COMPLAINT.md"
Copy-Item "$pkt\H_BANKS_OSINT_BRIEF.md" "$pt\MDE_PACKET\02_OSINT_BRIEF.md"
Copy-Item "$pkt\PRINT_ALL_IMAGE_EXHIBITS.pdf" "$pt\MDE_PACKET\03_LINKEDIN_AND_EXHIBITS.pdf"

# === AG PACKET ===
Copy-Item "$fr\36E_AG_UPL_PROSECUTION.md" "$pt\AG_PACKET\01_AG_COMPLAINT.md"
Copy-Item "$pkt\H_BANKS_OSINT_BRIEF.md" "$pt\AG_PACKET\02_OSINT_BRIEF.md"
Copy-Item "$pkt\PRINT_ALL_IMAGE_EXHIBITS.pdf" "$pt\AG_PACKET\03_LINKEDIN_AND_EXHIBITS.pdf"

# === SUBMITTED AUG 31 — move today's filed docs ===
Copy-Item "$fr\36A_UPL_STATE_BAR.md" "$sub\"
Copy-Item "$fr\36B_JTC_YANCEY.md" "$sub\"
Copy-Item "$fr\36C_JTC_MILLER.md" "$sub\"
Copy-Item "$fr\36F_DPSCD_EMAIL.md" "$sub\"
Copy-Item "$fr\37_FIRST_AMENDED_COMPLAINT_CONSPIRACY.txt" "$sub\"
Copy-Item "$fr\ABC_SERVICE_ORDER_BANKS.md" "$sub\"

Write-Host ""
Write-Host "=== PRINT_TOMORROW ==="
Get-ChildItem "$pt" -Recurse -File | Select-Object FullName | Format-Table -AutoSize
Write-Host ""
Write-Host "=== SUBMITTED_AUG31 ==="
Get-ChildItem "$sub" -File | Select-Object Name | Format-Table -AutoSize

