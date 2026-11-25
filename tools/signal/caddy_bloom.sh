#!/usr/bin/env bash
# caddy_bloom.sh — Salesman bloom pattern analysis
# Reads Caddy access logs and identifies cluster behaviors
# Run on sporeGate/relay where logs live
#
# Usage:
#   bash caddy_bloom.sh                    # last 24h
#   bash caddy_bloom.sh 48                 # last 48h
#   bash caddy_bloom.sh watch              # live tail mode
#   bash caddy_bloom.sh report             # full report

set -uo pipefail

HOURS="${1:-24}"
LOG="/var/log/caddy/detroit.primals.eco.access.log"
ALT_LOG="/var/log/caddy/access.log"

# Find the log
if [[ -f "$LOG" ]]; then
    LOGFILE="$LOG"
elif [[ -f "$ALT_LOG" ]]; then
    LOGFILE="$ALT_LOG"
else
    # Try journalctl for caddy
    echo "No log file found. Trying journalctl..."
    LOGFILE=""
fi

# Key pages — the ones in the email
TARGETS=(
    "/analysis/corporate-network-lara"
    "/analysis/dykema-infrastructure"
    "/network"
    "/analysis/funding-flow"
    "/analysis/credential-audit"
)

# Known IP ranges for cluster identification
# These are APPROXIMATE — real ranges need updating from live data
declare -A CLUSTERS
CLUSTERS["CMU/Mt Pleasant"]="141.209"
CLUSTERS["Dykema/Bloomfield"]="199.43"
CLUSTERS["Lansing/State"]="198.108"
CLUSTERS["Detroit/City"]="167.71"
CLUSTERS["Grosse Pointe"]="24.181"
CLUSTERS["Southfield"]="24.130"
CLUSTERS["Warren"]="24.129"
CLUSTERS["Hemlock/Saginaw"]="141.215"

bloom_report() {
    local hours=$1
    local since=$(date -d "${hours} hours ago" +%Y-%m-%dT%H:%M:%S 2>/dev/null || date -v-${hours}H +%Y-%m-%dT%H:%M:%S)

    echo "============================================"
    echo "  BLOOM PATTERN REPORT — Last ${hours}h"
    echo "  $(date)"
    echo "============================================"
    echo ""

    if [[ -z "$LOGFILE" ]]; then
        echo "Using journalctl for caddy logs..."
        local LOG_DATA=$(journalctl -u caddy --since "${hours} hours ago" --no-pager 2>/dev/null)
    else
        local LOG_DATA=$(cat "$LOGFILE")
    fi

    # Total hits
    local total=$(echo "$LOG_DATA" | grep -c "detroit.primals.eco" 2>/dev/null || echo "0")
    echo "TOTAL HITS: $total"
    echo ""

    # Hits to target pages
    echo "--- TARGET PAGE HITS ---"
    for target in "${TARGETS[@]}"; do
        local count=$(echo "$LOG_DATA" | grep -c "$target" 2>/dev/null || echo "0")
        if [[ "$count" -gt 0 ]]; then
            echo "  $target: $count"
        fi
    done
    echo ""

    # Unique IPs
    echo "--- UNIQUE VISITORS ---"
    echo "$LOG_DATA" | grep "detroit.primals.eco" | \
        grep -oP '\d+\.\d+\.\d+\.\d+' | sort -u | wc -l
    echo ""

    # IP cluster analysis
    echo "--- CLUSTER ANALYSIS ---"
    for name in "${!CLUSTERS[@]}"; do
        local prefix="${CLUSTERS[$name]}"
        local count=$(echo "$LOG_DATA" | grep -c "$prefix" 2>/dev/null || echo "0")
        if [[ "$count" -gt 0 ]]; then
            echo "  [$name] ($prefix.*): $count hits"
        fi
    done
    echo ""

    # Top IPs
    echo "--- TOP 20 IPs ---"
    echo "$LOG_DATA" | grep "detroit.primals.eco" | \
        grep -oP '\d+\.\d+\.\d+\.\d+' | sort | uniq -c | sort -rn | head -20
    echo ""

    # Temporal clustering — hits per hour
    echo "--- HOURLY PATTERN ---"
    echo "$LOG_DATA" | grep "detroit.primals.eco" | \
        grep -oP '\d{2}:\d{2}' | cut -c1-2 | sort | uniq -c | sort -k2
    echo ""

    # User agents (grouped)
    echo "--- USER AGENT CLUSTERS ---"
    echo "$LOG_DATA" | grep "detroit.primals.eco" | \
        grep -oP '"[^"]*"' | tail -1 | sort | uniq -c | sort -rn | head -10
    echo ""

    # Referrer analysis
    echo "--- REFERRERS ---"
    echo "$LOG_DATA" | grep "detroit.primals.eco" | \
        grep -oP 'referer":"[^"]*"' | sort | uniq -c | sort -rn | head -10
    echo ""

    # Time-clustered bursts (>3 hits from same /16 in 5 min window)
    echo "--- BURST DETECTION (same /16 subnet, >3 hits in window) ---"
    echo "$LOG_DATA" | grep "detroit.primals.eco" | \
        grep -oP '\d+\.\d+' | sort | uniq -c | sort -rn | \
        awk '$1 > 3 {print "  "$1" hits from "$2".*.*"}'
    echo ""

    echo "============================================"
    echo "  Sensor only. No tracking. Cluster behaviors."
    echo "============================================"
}

bloom_watch() {
    echo "=== LIVE BLOOM WATCH ==="
    echo "Tailing Caddy logs for detroit.primals.eco..."
    echo "Ctrl+C to stop"
    echo ""

    if [[ -n "$LOGFILE" ]]; then
        tail -f "$LOGFILE" | while read line; do
            if echo "$line" | grep -q "detroit.primals.eco"; then
                local ip=$(echo "$line" | grep -oP '\d+\.\d+\.\d+\.\d+' | head -1)
                local path=$(echo "$line" | grep -oP '"GET [^"]*"' | head -1)
                local ts=$(date +%H:%M:%S)

                # Check if it's a target page
                local is_target=""
                for target in "${TARGETS[@]}"; do
                    if echo "$line" | grep -q "$target"; then
                        is_target=" *** TARGET ***"
                        break
                    fi
                done

                # Check cluster membership
                local cluster=""
                for name in "${!CLUSTERS[@]}"; do
                    local prefix="${CLUSTERS[$name]}"
                    if echo "$ip" | grep -q "^$prefix"; then
                        cluster=" [$name]"
                        break
                    fi
                done

                echo "[$ts] $ip$cluster $path$is_target"
            fi
        done
    else
        journalctl -u caddy -f | while read line; do
            if echo "$line" | grep -q "detroit.primals.eco"; then
                echo "[$(date +%H:%M:%S)] $line"
            fi
        done
    fi
}

# Main
case "${1:-}" in
    watch)
        bloom_watch
        ;;
    report)
        bloom_report 48
        ;;
    [0-9]*)
        bloom_report "$1"
        ;;
    *)
        bloom_report 24
        ;;
esac
