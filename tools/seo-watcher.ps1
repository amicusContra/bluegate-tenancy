# SEO Indexing Watcher — northGate Tower Atomic concept
# Monitors search engine indexing of detroit.primals.eco
# Conceptually: skunkBat signal detection for the extracellular membrane

$logFile = "C:\Users\mokke\jobHunt\bluegate-tenancy\tools\seo-signal-log.jsonl"
$timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
$ua = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 Chrome/120.0"

Write-Host "=== SEO SIGNAL CHECK === $timestamp"
Write-Host ""

$domains = @("detroit.primals.eco", "sporeprint.primals.eco")

foreach ($domain in $domains) {
    Write-Host "--- $domain ---"

    # Sitemap health
    try {
        $sr = Invoke-WebRequest -Uri "https://$domain/sitemap.xml" -UseBasicParsing -TimeoutSec 10 -ErrorAction Stop
        $sitemapCount = ([regex]::Matches($sr.Content, '<loc>')).Count
        Write-Host "  SITEMAP: $sitemapCount URLs (HTTP $($sr.StatusCode))"
    } catch {
        $sitemapCount = 0
        Write-Host "  SITEMAP: FAIL"
    }

    # Bing site: check
    try {
        $bingQuery = "site%3A$domain"
        $br = Invoke-WebRequest -Uri "https://www.bing.com/search?q=$bingQuery" -UseBasicParsing -TimeoutSec 15 -Headers @{"User-Agent"=$ua} -ErrorAction Stop
        $bingRefs = ([regex]::Matches($br.Content, [regex]::Escape($domain))).Count
        $bingCount = if ($br.Content -match '([\d,]+) results') { $Matches[1] } else { "unknown" }
        Write-Host "  BING:    $bingCount results, $bingRefs domain refs in page"
    } catch {
        $bingRefs = -1
        $bingCount = "error"
        Write-Host "  BING:    ERROR"
    }

    # Google site: check
    try {
        $googleQuery = "site%3A$domain"
        $gr = Invoke-WebRequest -Uri "https://www.google.com/search?q=$googleQuery" -UseBasicParsing -TimeoutSec 15 -Headers @{"User-Agent"=$ua} -ErrorAction Stop
        $googleRefs = ([regex]::Matches($gr.Content, [regex]::Escape($domain))).Count
        $googleCount = if ($gr.Content -match 'About ([\d,]+) results') { $Matches[1] } else { "unknown" }
        Write-Host "  GOOGLE:  $googleCount results, $googleRefs domain refs in page"
    } catch {
        $googleRefs = -1
        $googleCount = "error"
        Write-Host "  GOOGLE:  ERROR"
    }

    $entry = @{
        t = $timestamp
        d = $domain
        sitemap = $sitemapCount
        bing = $bingCount
        bing_refs = $bingRefs
        google = $googleCount
        google_refs = $googleRefs
    } | ConvertTo-Json -Compress
    Add-Content -Path $logFile -Value $entry
    Write-Host ""
}

# Key term detection — is detroit.primals.eco appearing for investigation queries?
Write-Host "=== KEY TERM DETECTION ==="
$terms = @(
    "Brian Banks MacDowell detroit charter",
    "Purpose Charter Academy credential audit",
    "detroit.primals.eco",
    "MacDowell Preparatory Academy 3 percent math"
)

foreach ($term in $terms) {
    try {
        $encoded = [System.Uri]::EscapeDataString($term)
        $r = Invoke-WebRequest -Uri "https://www.bing.com/search?q=$encoded" -UseBasicParsing -TimeoutSec 15 -Headers @{"User-Agent"=$ua} -ErrorAction Stop
        $found = ([regex]::Matches($r.Content, "detroit\.primals\.eco")).Count
        $clutch = ([regex]::Matches($r.Content, "clutchjustice")).Count
        $signal = if ($found -gt 0) { "SITE INDEXED" } elseif ($clutch -gt 0) { "clutch visible" } else { "not yet" }
        Write-Host "  [$signal] $term"
    } catch {
        Write-Host "  [error]  $term"
    }
}

Write-Host ""
Write-Host "Log: $logFile"
