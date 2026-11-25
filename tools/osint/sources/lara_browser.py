"""LARA MiBusiness Registry — browser-based scraper.

New portal: michigan.gov/corpentitysearch
Searches by entity name, agent name, entity ID, and address.
"""

from __future__ import annotations
import re
from sources.browser_source import BrowserSource, new_page
from models import SearchResult

PORTAL_URL = "https://www.michigan.gov/corpentitysearch"


class LARABrowserSource(BrowserSource):
    name = "lara_browser"

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        lara_cfg = person.get("searches", {}).get("lara", {})
        if not lara_cfg:
            return results

        if lara_cfg.get("agent_name"):
            r = await self._search_portal(
                person["name"], "agent", person["id"], person["name"]
            )
            results.append(r)

        for eid in lara_cfg.get("entity_ids", []):
            r = await self._search_portal(
                eid, "id", person["id"], person["name"]
            )
            results.append(r)

        if lara_cfg.get("entity_name"):
            r = await self._search_portal(
                lara_cfg["entity_name"], "entity", person["id"], person["name"]
            )
            results.append(r)

        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        if entity.get("lara_id"):
            r = await self._search_portal(
                entity["lara_id"], "id", entity["id"], entity["name"]
            )
            results.append(r)
        r = await self._search_portal(
            entity["name"], "entity", entity["id"], entity["name"]
        )
        results.append(r)
        return results

    async def _search_portal(
        self, query: str, search_type: str, target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"lara_{search_type}: {query}",
        )
        try:
            async with new_page() as page:
                await self._goto_and_wait(page, PORTAL_URL, timeout=20000)
                await page.wait_for_timeout(2000)

                search_input = page.locator(
                    "input[type='text'], input[type='search'], "
                    "input[name*='search'], input[name*='entity'], "
                    "input[placeholder*='search' i], input[placeholder*='name' i]"
                ).first

                try:
                    await search_input.wait_for(timeout=10000)
                    await search_input.fill(query)
                    await page.wait_for_timeout(500)

                    search_btn = page.locator(
                        "button[type='submit'], input[type='submit'], "
                        "button:has-text('Search'), a:has-text('Search')"
                    ).first
                    await search_btn.click()
                    await page.wait_for_timeout(3000)

                    text = await self._get_page_text(page)
                    html = await self._get_page_html(page)
                    result.raw_data = {"url": page.url, "text_length": len(text)}
                    result.hits = self._parse_results(text, html, page.url)

                except Exception:
                    text = await self._get_page_text(page)
                    result.raw_data = {"url": page.url, "note": "Could not find search input"}
                    result.hits.append({
                        "note": "Portal loaded but search input not found — may need manual interaction",
                        "url": page.url,
                        "page_text_preview": text[:500],
                    })

        except Exception as e:
            result.error = str(e)
        return result

    def _parse_results(self, text: str, html: str, url: str) -> list[dict]:
        hits = []
        lines = text.split("\n")
        current = {}

        for line in lines:
            line = line.strip()
            if not line:
                if current:
                    hits.append(current)
                    current = {}
                continue

            if re.match(r"^\d{9}$", line):
                current["entity_id"] = line
            elif "active" in line.lower() and len(line) < 30:
                current["status"] = line
            elif "inactive" in line.lower() and len(line) < 30:
                current["status"] = line
            elif re.match(r"^(DOMESTIC|FOREIGN)", line, re.IGNORECASE):
                current["entity_type"] = line
            elif re.match(r"^\d{1,2}/\d{1,2}/\d{4}", line):
                current["date"] = line
            elif line.isupper() and len(line) > 5 and "LLC" in line or "INC" in line or "CORP" in line:
                current["entity_name"] = line
            elif line.isupper() and "," in line and any(
                st in line for st in ["MI ", "MI,", "MICHIGAN"]
            ):
                current["address"] = line

        if current:
            hits.append(current)

        if not hits:
            if "no results" in text.lower() or "0 results" in text.lower():
                hits.append({"note": "No results found", "url": url})
            elif len(text) > 100:
                hits.append({
                    "note": "Results page loaded — parsing may need refinement",
                    "url": url,
                    "text_preview": text[:1000],
                })
        return hits

