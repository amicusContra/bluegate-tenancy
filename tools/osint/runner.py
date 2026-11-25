"""OSINT Search Toolkit — CLI Runner.

Usage:
    python runner.py                          # Search ALL targets, ALL non-browser sources
    python runner.py --browser                # Include browser-automated sources
    python runner.py --all-sources            # Enable everything (browser + all APIs)
    python runner.py --target brian_banks     # Search one person across all sources
    python runner.py --target purpose_foundation --type entity
    python runner.py --source propublica      # All targets, one source only
    python runner.py --resume                 # Skip targets with existing results
    python runner.py --consolidate            # Merge all result runs into master report
    python runner.py --build-campaign-db      # Download MI SOS bulk data + build SQLite
    python runner.py --list                   # List all targets and sources
"""

from __future__ import annotations
import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table

from config import (
    RESULTS_DIR, load_targets, get_person, get_entity, get_address,
    all_people, all_entities, all_addresses,
)
from models import SearchResult

# HTTP-based sources (always available)
from sources.propublica import ProPublicaSource
from sources.opencorporates import OpenCorporatesSource
from sources.irs_teos import IRSTEOSSource
from sources.lara import LARASource
from sources.state_bar import StateBarSource
from sources.campaign_finance import CampaignFinanceSource
from sources.web_search import WebSearchSource
from sources.pubrecords_source import PubRecordsSource
from sources.courtlistener import CourtListenerSource
from sources.mi_campaign_local import MICampaignLocalSource

# Browser-based sources (require Playwright)
from sources.lara_browser import LARABrowserSource
from sources.state_bar_browser import StateBarBrowserSource
from sources.property_browser import PropertyBrowserSource
from sources.mde_browser import MDEBrowserSource
from sources.nmls_browser import NMLSBrowserSource

console = Console()

HTTP_SOURCES = {
    "pubrecords": PubRecordsSource(),
    "courtlistener": CourtListenerSource(),
    "propublica": ProPublicaSource(),
    "opencorporates": OpenCorporatesSource(),
    "irs_teos": IRSTEOSSource(),
    "lara": LARASource(),
    "state_bar_mi": StateBarSource(),
    "campaign_finance": CampaignFinanceSource(),
    "web_search": WebSearchSource(),
    "mi_campaign_local": MICampaignLocalSource(),
}

BROWSER_SOURCES = {
    "lara_browser": LARABrowserSource(),
    "state_bar_browser": StateBarBrowserSource(),
    "property_browser": PropertyBrowserSource(),
    "mde_browser": MDEBrowserSource(),
    "nmls_browser": NMLSBrowserSource(),
}


def get_all_sources(include_browser: bool = False) -> dict:
    sources = dict(HTTP_SOURCES)
    if include_browser:
        sources.update(BROWSER_SOURCES)
    return sources


def list_targets(include_browser: bool = False):
    data = load_targets()
    t = Table(title="PEOPLE", show_lines=True)
    t.add_column("ID", style="cyan")
    t.add_column("Name", style="bold")
    t.add_column("Searches")
    for p in data["people"]:
        sources = list(p.get("searches", {}).keys())
        t.add_row(p["id"], p["name"], ", ".join(sources))
    console.print(t)

    t = Table(title="ENTITIES", show_lines=True)
    t.add_column("ID", style="cyan")
    t.add_column("Name", style="bold")
    t.add_column("LARA ID")
    for e in data["entities"]:
        t.add_row(e["id"], e["name"], e.get("lara_id", "?"))
    console.print(t)

    t = Table(title="ADDRESSES", show_lines=True)
    t.add_column("ID", style="cyan")
    t.add_column("Address", style="bold")
    t.add_column("Associated With")
    for a in data["addresses"]:
        assoc = ", ".join(a.get("associated_with", []))
        t.add_row(a["id"], f"{a['address']}, {a['city']}", assoc)
    console.print(t)

    sources = get_all_sources(include_browser)
    t = Table(title=f"SOURCES ({len(sources)})", show_lines=True)
    t.add_column("Name", style="cyan")
    t.add_column("Type")
    t.add_column("Status")
    for name, src in sources.items():
        stype = "browser" if getattr(src, "requires_browser", False) else "http"
        status = "[green]ready" if src.available() else "[yellow]needs key" if src.requires_key else "[red]unavailable"
        t.add_row(name, stype, status)
    console.print(t)


def get_existing_results() -> set[str]:
    """Return set of target_ids that already have results."""
    existing = set()
    for run_dir in RESULTS_DIR.iterdir():
        if not run_dir.is_dir():
            continue
        json_file = run_dir / "results.json"
        if json_file.exists():
            try:
                with open(json_file, encoding="utf-8") as f:
                    data = json.load(f)
                for r in data:
                    if r.get("hit_count", 0) > 0:
                        existing.add(r["target_id"])
            except Exception:
                pass
    return existing


async def run_search(
    target_ids: list[str] | None,
    target_type: str,
    source_names: list[str] | None,
    include_browser: bool = False,
    resume: bool = False,
) -> list[SearchResult]:
    all_sources = get_all_sources(include_browser)
    if source_names:
        sources = {k: v for k, v in all_sources.items() if k in source_names}
    else:
        sources = {k: v for k, v in all_sources.items() if v.available()}

    skip_ids = get_existing_results() if resume else set()
    all_results: list[SearchResult] = []

    if target_type == "person":
        people = [get_person(tid) for tid in target_ids] if target_ids else all_people()
        people = [p for p in people if p is not None]
        if resume:
            before = len(people)
            people = [p for p in people if p["id"] not in skip_ids]
            if before != len(people):
                console.print(f"[dim]Resuming: skipping {before - len(people)} targets with existing results[/dim]")

        total_tasks = len(people) * len(sources)
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Searching people...", total=total_tasks)
            for person in people:
                progress.update(task, description=f"[bold]{person['name']}[/bold]")
                for sname, source in sources.items():
                    progress.update(task, description=f"[bold]{person['name']}[/bold] [{sname}]")
                    try:
                        results = await source.search_person(person)
                        total = sum(r.hit_count for r in results)
                        errors = sum(1 for r in results if r.error)
                        if total > 0 or errors > 0:
                            console.print(f"  [cyan]{sname}[/cyan] -> {total} hits, {errors} errors")
                        all_results.extend(results)
                    except Exception as e:
                        console.print(f"  [red]{sname} FAILED: {e}[/red]")
                        all_results.append(SearchResult(
                            source=sname,
                            target_id=person["id"],
                            target_name=person["name"],
                            query="(search_person)",
                            error=str(e),
                        ))
                    progress.advance(task)

    elif target_type == "entity":
        entities = [get_entity(tid) for tid in target_ids] if target_ids else all_entities()
        entities = [e for e in entities if e is not None]
        if resume:
            before = len(entities)
            entities = [e for e in entities if e["id"] not in skip_ids]
            if before != len(entities):
                console.print(f"[dim]Resuming: skipping {before - len(entities)} targets[/dim]")

        total_tasks = len(entities) * len(sources)
        with Progress(
            SpinnerColumn(), TextColumn("[bold blue]{task.description}"),
            BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(), console=console,
        ) as progress:
            task = progress.add_task("Searching entities...", total=total_tasks)
            for entity in entities:
                progress.update(task, description=f"[bold]{entity['name']}[/bold]")
                for sname, source in sources.items():
                    progress.update(task, description=f"[bold]{entity['name']}[/bold] [{sname}]")
                    try:
                        results = await source.search_entity(entity)
                        total = sum(r.hit_count for r in results)
                        errors = sum(1 for r in results if r.error)
                        if total > 0 or errors > 0:
                            console.print(f"  [cyan]{sname}[/cyan] -> {total} hits, {errors} errors")
                        all_results.extend(results)
                    except Exception as e:
                        console.print(f"  [red]{sname} FAILED: {e}[/red]")
                    progress.advance(task)

    elif target_type == "address":
        addrs = [get_address(tid) for tid in target_ids] if target_ids else all_addresses()
        addrs = [a for a in addrs if a is not None]

        total_tasks = len(addrs) * len(sources)
        with Progress(
            SpinnerColumn(), TextColumn("[bold blue]{task.description}"),
            BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(), console=console,
        ) as progress:
            task = progress.add_task("Searching addresses...", total=total_tasks)
            for addr in addrs:
                progress.update(task, description=f"[bold]{addr['address']}[/bold]")
                for sname, source in sources.items():
                    progress.update(task, description=f"[bold]{addr['address']}[/bold] [{sname}]")
                    try:
                        results = await source.search_address(addr)
                        total = sum(r.hit_count for r in results)
                        if total > 0:
                            console.print(f"  [cyan]{sname}[/cyan] -> {total} hits")
                        all_results.extend(results)
                    except Exception as e:
                        console.print(f"  [red]{sname} FAILED: {e}[/red]")
                    progress.advance(task)

    return all_results


def save_results(results: list[SearchResult], run_name: str) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = RESULTS_DIR / f"{run_name}_{ts}"
    run_dir.mkdir(parents=True, exist_ok=True)

    json_path = run_dir / "results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump([r.to_dict() for r in results], f, indent=2, default=str)

    md_path = run_dir / "results.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# OSINT Search Results — {run_name}\n")
        f.write(f"**Run:** {ts}\n\n")
        f.write(f"**Total queries:** {len(results)}  \n")
        f.write(f"**Total hits:** {sum(r.hit_count for r in results)}  \n")
        f.write(f"**Errors:** {sum(1 for r in results if r.error)}\n\n---\n\n")

        by_target: dict[str, list[SearchResult]] = {}
        for r in results:
            by_target.setdefault(r.target_id, []).append(r)

        for tid, target_results in by_target.items():
            name = target_results[0].target_name
            f.write(f"## {name} (`{tid}`)\n\n")
            for r in target_results:
                f.write(r.to_markdown())
                f.write("\n---\n\n")

    console.print(f"\n[green]Results saved:[/green]")
    console.print(f"  JSON: {json_path}")
    console.print(f"  MD:   {md_path}")
    return run_dir


def consolidate_results():
    """Merge all result runs into a single master report."""
    all_data = []
    run_dirs = sorted(RESULTS_DIR.iterdir())

    for run_dir in run_dirs:
        if not run_dir.is_dir():
            continue
        json_file = run_dir / "results.json"
        if not json_file.exists():
            continue
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
            all_data.extend(data)
            console.print(f"  Loaded {len(data)} results from {run_dir.name}")
        except Exception as e:
            console.print(f"  [red]Error loading {run_dir.name}: {e}[/red]")

    if not all_data:
        console.print("[yellow]No results to consolidate.[/yellow]")
        return

    # Deduplicate by (source, target_id, query)
    seen = set()
    unique = []
    for r in all_data:
        key = (r.get("source"), r.get("target_id"), r.get("query"))
        if key not in seen:
            seen.add(key)
            unique.append(r)

    console.print(f"\n[bold]Consolidated: {len(all_data)} total -> {len(unique)} unique results[/bold]")

    master_dir = RESULTS_DIR / "MASTER"
    master_dir.mkdir(parents=True, exist_ok=True)

    json_path = master_dir / "all_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(unique, f, indent=2, default=str)

    md_path = master_dir / "all_results.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# OSINT Master Report — All Results Consolidated\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n")
        f.write(f"**Total unique results:** {len(unique)}\n")
        f.write(f"**Total hits:** {sum(r.get('hit_count', 0) for r in unique)}\n\n---\n\n")

        by_target: dict[str, list] = {}
        for r in unique:
            by_target.setdefault(r.get("target_id", "unknown"), []).append(r)

        for tid, results in sorted(by_target.items()):
            name = results[0].get("target_name", tid)
            total_hits = sum(r.get("hit_count", 0) for r in results)
            f.write(f"## {name} (`{tid}`) — {total_hits} hits\n\n")
            for r in results:
                f.write(f"### {r.get('source', '?')} — {name}\n")
                f.write(f"**Query:** `{r.get('query', '?')}`  \n")
                f.write(f"**Hits:** {r.get('hit_count', 0)}\n\n")
                if r.get("error"):
                    f.write(f"**ERROR:** {r['error']}\n\n")
                for i, hit in enumerate(r.get("hits", []), 1):
                    f.write(f"#### Hit {i}\n")
                    for k, v in hit.items():
                        if v is not None and v != "":
                            f.write(f"- **{k}:** {v}\n")
                    f.write("\n")
                f.write("---\n\n")

    # Summary table
    by_source: dict[str, int] = {}
    for r in unique:
        s = r.get("source", "?")
        by_source[s] = by_source.get(s, 0) + r.get("hit_count", 0)

    t = Table(title="Hits by Source")
    t.add_column("Source", style="cyan")
    t.add_column("Hits", style="bold green", justify="right")
    for s, h in sorted(by_source.items(), key=lambda x: -x[1]):
        t.add_row(s, str(h))
    console.print(t)

    console.print(f"\n[green]Master report saved:[/green]")
    console.print(f"  JSON: {json_path}")
    console.print(f"  MD:   {md_path}")


def main():
    parser = argparse.ArgumentParser(
        description="OSINT Search Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python runner.py                              # All targets, HTTP sources only
  python runner.py --browser                    # Include browser-automated sources
  python runner.py --all-sources                # Everything enabled
  python runner.py -t brian_banks -s propublica  # One target, one source
  python runner.py --resume                     # Skip targets with existing results
  python runner.py --consolidate                # Merge all runs into master report
  python runner.py --build-campaign-db          # Download MI SOS bulk data
        """,
    )
    parser.add_argument("--target", "-t", nargs="*", help="Target ID(s) to search")
    parser.add_argument(
        "--type", choices=["person", "entity", "address"], default="person",
        help="Target type (default: person)"
    )
    parser.add_argument("--source", "-s", nargs="*", help="Source(s) to use")
    parser.add_argument("--browser", action="store_true", help="Include browser-automated sources")
    parser.add_argument("--no-browser", action="store_true", help="Exclude browser sources (default)")
    parser.add_argument("--all-sources", action="store_true", help="Enable all sources including browser")
    parser.add_argument("--resume", action="store_true", help="Skip targets with existing results")
    parser.add_argument("--consolidate", action="store_true", help="Merge all result runs into master report")
    parser.add_argument("--build-campaign-db", action="store_true", help="Download MI SOS bulk data + build SQLite")
    parser.add_argument("--list", "-l", action="store_true", help="List all targets and sources")
    parser.add_argument("--name", "-n", default="search", help="Run name for output folder")
    args = parser.parse_args()

    if args.consolidate:
        console.print("[bold]Consolidating all results...[/bold]")
        consolidate_results()
        return

    if args.build_campaign_db:
        console.print("[bold]Building MI campaign finance database...[/bold]")
        from sources.mi_campaign_local import download_and_index
        asyncio.run(download_and_index())
        return

    include_browser = args.browser or args.all_sources
    if args.no_browser:
        include_browser = False

    if args.list:
        list_targets(include_browser)
        return

    all_sources = get_all_sources(include_browser)
    if args.source:
        bad = [s for s in args.source if s not in all_sources]
        if bad:
            console.print(f"[red]Unknown source(s): {bad}[/red]")
            console.print(f"Available: {list(all_sources.keys())}")
            return

    console.rule("[bold blue]OSINT Search Toolkit[/bold blue]")
    console.print(f"Targets: {args.target or 'ALL'}")
    console.print(f"Type: {args.type}")
    console.print(f"Sources: {args.source or 'ALL'}")
    console.print(f"Browser: {'enabled' if include_browser else 'disabled'}")
    console.print(f"Resume: {'yes' if args.resume else 'no'}")
    console.print(f"Started: {datetime.now().isoformat()}")
    console.print()

    results = asyncio.run(run_search(
        args.target, args.type, args.source,
        include_browser=include_browser,
        resume=args.resume,
    ))

    if results:
        save_results(results, args.name)

    # Close browser if it was used
    if include_browser:
        try:
            from sources.browser_source import close_browser
            asyncio.run(close_browser())
        except Exception:
            pass

    errors = [r for r in results if r.error]
    hits = sum(r.hit_count for r in results)
    console.rule("[bold green]Complete[/bold green]")
    console.print(f"[bold]{len(results)}[/bold] queries, [bold green]{hits}[/bold green] total hits, [bold red]{len(errors)}[/bold red] errors")


if __name__ == "__main__":
    main()

