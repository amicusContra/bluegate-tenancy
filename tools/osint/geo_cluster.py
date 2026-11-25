"""
Geographic Cluster Analysis — Property Distance Matrix
Calculates beeline (haversine) distances between all key addresses.
"""
import math
import json
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent.parent / "02-evidence" / "web-captures"

# Key properties with approximate coordinates
# Format: (label, lat, lon, owner/connection, municipality)
PROPERTIES = [
    ("XXXXX Dresden St", 42.4245, -82.9989, "Leon & Marquita Smith", "Detroit"),
    ("XXXXX Normandy Ave", 42.4542, -82.9329, "Simone Smith (sold/foreclosed)", "Eastpointe"),
    ("XXXXX Stricker Ave", 42.4520, -82.9380, "Marquita 'King' (Directory411)", "Eastpointe"),
    ("17363 Toepfer Dr", 42.4588, -82.9423, "Lovelife Church / Kevin Lancaster", "Eastpointe"),
    ("1968 Severn Rd", 42.4430, -82.9038, "Brian Banks (home/Purpose Fdn)", "GPW"),
    ("21456 Newcastle Rd", 42.4320, -82.9200, "Right Turn Project (dissolved)", "Harper Woods"),
    ("10101 E Canfield St", 42.3710, -83.0090, "Purpose Charter Academy", "Detroit"),
    ("615 Griswold St", 42.3300, -83.0490, "Perkins Law Group", "Detroit (downtown)"),
    ("500 Woodward Ste 4000", 42.3330, -83.0460, "Lovelife 2nd address", "Detroit (downtown)"),
    ("XXXXX Bowman St", 42.4505, -82.9440, "Rental property ($2,200/mo)", "Eastpointe"),
    ("Merrimac Circle", 42.5750, -82.9200, "Marquita & Walter Smith deed", "Harrison Twp"),
    ("17370 W Point St", 42.4150, -83.0300, "Marquita (flipped during BK)", "Detroit"),
    ("XXXXX Hickory Ct", 42.2380, -83.2920, "Judge Miller (current)", "Flat Rock"),
    ("14551 Broadstone Blvd", 42.3780, -82.9840, "Judge Yancey (sold $200K)", "Detroit"),
    ("XXXXX George Washington Dr", 42.4730, -83.2640, "Yecart Accounting / Tracey Ellis", "Southfield"),
]


def haversine_miles(lat1, lon1, lat2, lon2):
    """Calculate great-circle distance in miles."""
    R = 3958.8  # Earth radius in miles
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c


def driving_estimate(beeline_miles):
    """Estimate driving distance as ~1.3x beeline for urban grid."""
    return beeline_miles * 1.35


def main():
    n = len(PROPERTIES)

    output = RESULTS_DIR / "GEO_CLUSTER_DISTANCE_MATRIX.md"
    with open(output, "w", encoding="utf-8") as f:
        f.write("# GEOGRAPHIC CLUSTER ANALYSIS\n")
        f.write("## Property Distance Matrix — All Key Addresses\n")
        f.write("## Generated: September 7, 2026\n\n")
        f.write("Beeline = haversine (straight-line) distance\n")
        f.write("Driving ≈ 1.35× beeline (urban grid estimate)\n\n")
        f.write("---\n\n")

        # Full matrix
        f.write("## FULL DISTANCE MATRIX (miles)\n\n")
        f.write("| From → To | Beeline | Driving Est. | Cluster |\n")
        f.write("|-----------|---------|-------------|--------|\n")

        clusters = {}
        for i in range(n):
            for j in range(i+1, n):
                label_i = PROPERTIES[i][0]
                label_j = PROPERTIES[j][0]
                d = haversine_miles(
                    PROPERTIES[i][1], PROPERTIES[i][2],
                    PROPERTIES[j][1], PROPERTIES[j][2],
                )
                dr = driving_estimate(d)
                cluster = ""
                if d < 1.0:
                    cluster = "🔴 SAME NEIGHBORHOOD"
                elif d < 2.5:
                    cluster = "🟠 ADJACENT"
                elif d < 5.0:
                    cluster = "🟡 NEARBY"
                elif d < 10.0:
                    cluster = "🟢 SAME METRO"
                else:
                    cluster = "⚪ DISTANT"

                key = f"{label_i} → {label_j}"
                clusters[key] = (d, dr, cluster, PROPERTIES[i][3], PROPERTIES[j][3])

        # Sort by distance
        sorted_pairs = sorted(clusters.items(), key=lambda x: x[1][0])

        for key, (d, dr, cluster, owner_i, owner_j) in sorted_pairs:
            f.write(f"| {key} | {d:.1f} mi | {dr:.1f} mi | {cluster} |\n")

        # Eastpointe cluster analysis
        f.write("\n---\n\n")
        f.write("## 🔴 EASTPOINTE CLUSTER (< 1 mile radius)\n\n")
        f.write("These properties are all within walking distance:\n\n")

        eastpointe = [p for p in PROPERTIES if p[4] in ("Eastpointe",)]
        f.write("| Property | Owner/Connection | Municipality |\n")
        f.write("|----------|-----------------|-------------|\n")
        for p in eastpointe:
            f.write(f"| {p[0]} | {p[3]} | {p[4]} |\n")

        f.write("\n**Distances within Eastpointe cluster:**\n\n")
        for i in range(len(eastpointe)):
            for j in range(i+1, len(eastpointe)):
                d = haversine_miles(
                    eastpointe[i][1], eastpointe[i][2],
                    eastpointe[j][1], eastpointe[j][2],
                )
                f.write(f"- {eastpointe[i][0]} ↔ {eastpointe[j][0]}: **{d:.2f} mi** beeline\n")

        # Banks/GPW cluster
        f.write("\n---\n\n")
        f.write("## 🟠 GROSSE POINTE CLUSTER\n\n")
        gpw = [p for p in PROPERTIES if p[4] in ("GPW", "Harper Woods")]
        f.write("| Property | Owner/Connection | Municipality |\n")
        f.write("|----------|-----------------|-------------|\n")
        for p in gpw:
            f.write(f"| {p[0]} | {p[3]} | {p[4]} |\n")

        if len(gpw) >= 2:
            for i in range(len(gpw)):
                for j in range(i+1, len(gpw)):
                    d = haversine_miles(gpw[i][1], gpw[i][2], gpw[j][1], gpw[j][2])
                    f.write(f"\n- {gpw[i][0]} ↔ {gpw[j][0]}: **{d:.2f} mi** beeline")

        # Key cross-cluster distances
        f.write("\n\n---\n\n")
        f.write("## KEY CROSS-CLUSTER DISTANCES\n\n")
        f.write("| Connection | Beeline | Driving | Significance |\n")
        f.write("|-----------|---------|---------|-------------|\n")

        key_pairs = [
            (0, 1, "Leon's house to Simone's property"),
            (0, 2, "Leon's house to Marquita's Eastpointe alias address"),
            (0, 3, "Leon's house to Lovelife Church ($200/mo recipient)"),
            (1, 3, "Simone's property to Lovelife Church"),
            (2, 3, "Marquita alias address to Lovelife Church"),
            (1, 2, "Simone's property to Marquita alias address"),
            (0, 4, "Leon's house to Banks' home"),
            (4, 5, "Banks' home to Right Turn Project"),
            (3, 10, "Lovelife Church to Harrison Twp (Shayla QCDs)"),
            (4, 7, "Banks' home to Perkins Law Group"),
            (0, 6, "Leon's house to Purpose Charter Academy"),
        ]

        for i, j, sig in key_pairs:
            d = haversine_miles(
                PROPERTIES[i][1], PROPERTIES[i][2],
                PROPERTIES[j][1], PROPERTIES[j][2],
            )
            dr = driving_estimate(d)
            f.write(f"| {sig} | {d:.1f} mi | {dr:.1f} mi | {PROPERTIES[i][0]} ↔ {PROPERTIES[j][0]} |\n")

        f.write("\n---\n\n")
        f.write("## COORDINATE SOURCES & ACCURACY\n\n")
        f.write("| Property | Lat | Lon | Source | Accuracy |\n")
        f.write("|----------|-----|-----|--------|----------|\n")
        for p in PROPERTIES:
            f.write(f"| {p[0]} | {p[1]:.4f} | {p[2]:.4f} | Web geocoding | ±0.002° (~200m) |\n")

        f.write("\n*Coordinates are approximate. Stricker and Bowman estimated from Eastpointe grid.*\n")
        f.write("*Merrimac estimated from Harrison Township centroid.*\n")
        f.write("*For precise driving distances, use Google Maps API with a key.*\n")

    print(f"Distance matrix saved to: {output}")


if __name__ == "__main__":
    main()
