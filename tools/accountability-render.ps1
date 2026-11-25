# Accountability Clock Renderer

$clockFile = "C:\Users\mokke\jobHunt\bluegate-tenancy\tools\accountability-clock.jsonl"
$today = Get-Date

$entries = Get-Content $clockFile | ForEach-Object { $_ | ConvertFrom-Json }

Write-Host ""
Write-Host "============================================================"
Write-Host "  JUSTICE DELAYED IS JUSTICE DENIED"
Write-Host "  Accountability Clock"
Write-Host "  $($today.ToString('MMMM d, yyyy'))"
Write-Host "============================================================"
Write-Host ""

$notifications = $entries | Where-Object { $_.type -eq "notification" }
$seoSignals = $entries | Where-Object { $_.type -eq "seo_signal" }
$harm = $entries | Where-Object { $_.type -eq "harm" }

Write-Host "  AGENCIES NOTIFIED: $($notifications.Count)"
Write-Host "  ----------------------------------------"
Write-Host ""
foreach ($n in $notifications | Sort-Object date) {
    $notifyDate = [datetime]::Parse($n.date)
    $elapsed = ($today - $notifyDate).Days
    $status = switch ($n.response) {
        "none" { "NO RESPONSE" }
        "acknowledged" { "ACKNOWLEDGED" }
        "partial_response_sep25" { "PARTIAL RESPONSE" }
        "investigation_opened_then_closed" { "CLOSED WITHOUT ENFORCEMENT" }
        "investigation_closed_without_enforcement" { "CLEARED FELON" }
        "inquiry_filed" { "INQUIRY FILED" }
        "published" { "PUBLISHED" }
        "monitoring" { "MONITORING" }
        "hearing_sep29" { "HEARING SCHEDULED" }
        default { $n.response }
    }
    $pad = $n.entity.PadRight(40)
    $dayStr = "$elapsed days".PadLeft(10)
    Write-Host "  $pad $dayStr  [$status]"
}

Write-Host ""
Write-Host "  EVIDENCE PUBLICLY DISCOVERABLE"
Write-Host "  ----------------------------------------"
Write-Host ""
foreach ($s in $seoSignals | Sort-Object date) {
    $d = [datetime]::Parse($s.date)
    $elapsed = ($today - $d).Days
    Write-Host "  $($s.date) | $elapsed days ago | $($s.description)"
}

Write-Host ""
Write-Host "  ONGOING HARM"
Write-Host "  ----------------------------------------"
Write-Host ""
foreach ($h in $harm | Sort-Object date) {
    $d = [datetime]::Parse($h.date)
    $elapsed = ($today - $d).Days
    $years = [math]::Floor($elapsed / 365)
    Write-Host "  Since $($h.date) -- $elapsed days -- $years years"
    Write-Host "  $($h.description)"
    if ($h.annual_students -is [int]) {
        $affected = $h.annual_students * $years
        Write-Host "  Estimated student-years affected: $affected"
    }
    Write-Host ""
}

$firstNotify = ($notifications | Sort-Object date | Select-Object -First 1).date
$firstDate = [datetime]::Parse($firstNotify)
$totalDays = ($today - $firstDate).Days
$noResponse = ($notifications | Where-Object { $_.response -eq "none" }).Count

Write-Host "============================================================"
Write-Host "  First notification: $firstNotify -- $totalDays days ago"
Write-Host "  Agencies with NO RESPONSE: $noResponse of $($notifications.Count)"
Write-Host "  Site indexed on Bing: Sep 26, 2026"
Write-Host "  Every day after indexing is a documented choice."
Write-Host "============================================================"
