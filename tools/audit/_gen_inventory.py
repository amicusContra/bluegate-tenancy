import os
import sys
from collections import defaultdict
from datetime import datetime

root = r"c:\Users\mokke\jobHunt\bluegate-tenancy"
TEXT_EXTS = {
    ".md", ".txt", ".py", ".tex", ".json", ".yaml", ".yml",
    ".csv", ".html", ".xml", ".sh", ".ps1", ".bat", ".cfg", ".ini", ".log",
}


def human_size(n):
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n / (1024 * 1024):.1f} MB"


def count_lines(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except OSError:
        return None


def inventory(base_rel):
    base = os.path.join(root, base_rel.replace("/", os.sep))
    if not os.path.isdir(base):
        return {}
    by_dir = defaultdict(list)
    for dirpath, _, filenames in os.walk(base):
        for fn in sorted(filenames):
            fp = os.path.join(dirpath, fn)
            st = os.stat(fp)
            rel_dir = os.path.relpath(dirpath, root).replace("\\", "/")
            ext = os.path.splitext(fn)[1].lower()
            lines = count_lines(fp) if ext in TEXT_EXTS else None
            by_dir[rel_dir].append(
                {
                    "name": fn,
                    "size": st.st_size,
                    "size_h": human_size(st.st_size),
                    "lines": lines,
                    "modified": datetime.fromtimestamp(st.st_mtime).strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                }
            )
    return dict(sorted(by_dir.items()))


def print_section(title, inv, skip_subdirs=None):
    skip_subdirs = skip_subdirs or set()
    total = sum(len(v) for k, v in inv.items() if not _is_skipped(k, skip_subdirs))
    print(f"## {title} ({total} files)")
    print()
    for d in sorted(inv.keys()):
        if _is_skipped(d, skip_subdirs):
            continue
        files = inv[d]
        print(f"### {d}/ ({len(files)} files)")
        print()
        print("| File | Size | Lines | Modified |")
        print("|------|------|-------|----------|")
        for f in files:
            lines = str(f["lines"]) if f["lines"] is not None else "—"
            print(
                f"| {f['name']} | {f['size_h']} | {lines} | {f['modified']} |"
            )
        print()


def _is_skipped(d, skip_subdirs):
    for sd in skip_subdirs:
        if d == sd or d.startswith(sd + "/"):
            return True
    return False


def filenames_only(base_rel, sub):
    p = os.path.join(root, base_rel.replace("/", os.sep), sub.replace("/", os.sep))
    if not os.path.isdir(p):
        return []
    names = []
    for dirpath, _, filenames in os.walk(p):
        for fn in sorted(filenames):
            names.append(fn)
    return sorted(names)


def main():
    inv_01case = inventory("01-case")
    inv_osint = inventory("tools/osint/results")
    inv_evidence = inventory("02-evidence")
    inv_discord = inventory("01-case/discord")
    inv_nolan = inventory("01-case/nolan_clean_drop")
    inv_filing = inventory("01-case/filing-ready")

    top_dirs = []
    for name in sorted(os.listdir(root)):
        p = os.path.join(root, name)
        if os.path.isdir(p) and name not in ("01-case", "02-evidence", "tools"):
            hits = []
            for dp, _, fns in os.walk(p):
                for fn in fns:
                    if os.path.splitext(fn)[1].lower() in {".md", ".txt", ".py"}:
                        fp = os.path.join(dp, fn)
                        st = os.stat(fp)
                        rel = os.path.relpath(fp, root).replace("\\", "/")
                        hits.append(
                            {
                                "rel": rel,
                                "name": fn,
                                "size_h": human_size(st.st_size),
                                "lines": count_lines(fp),
                                "modified": datetime.fromtimestamp(
                                    st.st_mtime
                                ).strftime("%Y-%m-%d %H:%M"),
                            }
                        )
            if hits:
                top_dirs.append((name, hits))

    root_hits = []
    for fn in sorted(os.listdir(root)):
        fp = os.path.join(root, fn)
        if os.path.isfile(fp) and os.path.splitext(fn)[1].lower() in {
            ".md",
            ".txt",
            ".py",
        }:
            st = os.stat(fp)
            root_hits.append(
                {
                    "name": fn,
                    "size_h": human_size(st.st_size),
                    "lines": count_lines(fp),
                    "modified": datetime.fromtimestamp(st.st_mtime).strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                }
            )

    out = os.path.join(root, "_INVENTORY_AUDIT.txt")
    with open(out, "w", encoding="utf-8") as f:
        def w(line=""):
            f.write(line + "\n")

        w("# bluegate-tenancy File Inventory Audit")
        w(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        w(f"Root: {root}")
        w()
        w("## Summary")
        w()
        w(f"- 01-case total: {sum(len(v) for v in inv_01case.values())} files")
        w(
            f"- tools/osint/results total: {sum(len(v) for v in inv_osint.values())} files"
        )
        w(f"- 02-evidence total: {sum(len(v) for v in inv_evidence.values())} files")
        w(f"- 01-case/discord: {sum(len(v) for v in inv_discord.values())} files")
        w(
            f"- 01-case/nolan_clean_drop: {sum(len(v) for v in inv_nolan.values())} files"
        )
        w(
            f"- 01-case/filing-ready total: {sum(len(v) for v in inv_filing.values())} files"
        )
        w()

        sections = [
            ("1. 01-case/ (all subdirectories)", inv_01case, None),
            ("2. tools/osint/results/", inv_osint, None),
            ("3. 02-evidence/", inv_evidence, None),
            ("4. 01-case/discord/", inv_discord, None),
            ("5. 01-case/nolan_clean_drop/", inv_nolan, None),
        ]
        for title, inv, skip in sections:
            skip = skip or set()
            total = sum(
                len(v) for k, v in inv.items() if not _is_skipped(k, skip)
            )
            w(f"## {title} ({total} files)")
            w()
            for d in sorted(inv.keys()):
                if _is_skipped(d, skip):
                    continue
                files = inv[d]
                w(f"### {d}/ ({len(files)} files)")
                w()
                w("| File | Size | Lines | Modified |")
                w("|------|------|-------|----------|")
                for fi in files:
                    lines = str(fi["lines"]) if fi["lines"] is not None else "—"
                    w(
                        f"| {fi['name']} | {fi['size_h']} | {lines} | {fi['modified']} |"
                    )
                w()

        skip = {
            "01-case/filing-ready/exhibits",
            "01-case/filing-ready/subpoenas",
        }
        fr_total = sum(
            len(v)
            for k, v in inv_filing.items()
            if not _is_skipped(k, skip)
        )
        w(
            f"## 6. 01-case/filing-ready/ (excluding exhibits/ and subpoenas/) ({fr_total} files)"
        )
        w()
        for d in sorted(inv_filing.keys()):
            if _is_skipped(d, skip):
                continue
            files = inv_filing[d]
            w(f"### {d}/ ({len(files)} files)")
            w()
            w("| File | Size | Lines | Modified |")
            w("|------|------|-------|----------|")
            for fi in files:
                lines = str(fi["lines"]) if fi["lines"] is not None else "—"
                w(
                    f"| {fi['name']} | {fi['size_h']} | {lines} | {fi['modified']} |"
                )
            w()

        ex_names = filenames_only("01-case/filing-ready", "exhibits")
        sub_names = filenames_only("01-case/filing-ready", "subpoenas")
        w(f"## 6b. filing-ready/exhibits/ — filenames only ({len(ex_names)} files)")
        w()
        for n in ex_names:
            w(f"- {n}")
        w()
        w(f"## 6c. filing-ready/subpoenas/ — filenames only ({len(sub_names)} files)")
        w()
        for n in sub_names:
            w(f"- {n}")
        w()

        w("## 7. Other top-level directories with .md, .txt, or .py files")
        w()
        if root_hits:
            w("### (root)/")
            w()
            w("| File | Size | Lines | Modified |")
            w("|------|------|-------|----------|")
            for h in root_hits:
                lines = str(h["lines"]) if h["lines"] is not None else "—"
                w(f"| {h['name']} | {h['size_h']} | {lines} | {h['modified']} |")
            w()
        for dname, hits in top_dirs:
            w(f"### {dname}/ ({len(hits)} text files)")
            w()
            w("| Path | Size | Lines | Modified |")
            w("|------|------|-------|----------|")
            for h in hits:
                lines = str(h["lines"]) if h["lines"] is not None else "—"
                w(f"| {h['rel']} | {h['size_h']} | {lines} | {h['modified']} |")
            w()

    line_count = sum(1 for _ in open(out, encoding="utf-8"))
    print(f"Wrote {out}")
    print(f"Lines: {line_count}")


if __name__ == "__main__":
    main()

