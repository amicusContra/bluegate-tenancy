"""Michigan Department of Education — educator credential lookup.

Portal: mdoe.state.mi.us/MOECS/PublicCredentialSearch.aspx
Searches for administrator certifications, teaching certificates, etc.
"""

from __future__ import annotations
from sources.browser_source import BrowserSource, new_page
from models import SearchResult

MDE_URL = "https://mdoe.state.mi.us/MOECS/PublicCredentialSearch.aspx"


class MDEBrowserSource(BrowserSource):
    name = "mde_browser"

    async def search_person(self, person: dict) -> list[SearchResult]:
        if not person.get("searches", {}).get("mde"):
            return []
        parts = person["name"].split()
        last = parts[-1] if parts else person["name"]
        first = parts[0] if len(parts) > 1 else ""
        r = await self._search_educator(first, last, person["id"], person["name"])
        return [r]

    async def _search_educator(
        self, first: str, last: str, target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"educator: {first} {last}",
        )
        try:
            async with new_page() as page:
                await self._goto_and_wait(page, MDE_URL, timeout=20000)
                await page.wait_for_timeout(2000)

                last_input = page.locator(
                    "input[name*='LastName' i], input[id*='LastName' i], "
                    "input[name*='last' i]"
                ).first
                first_input = page.locator(
                    "input[name*='FirstName' i], input[id*='FirstName' i], "
                    "input[name*='first' i]"
                ).first

                try:
                    await last_input.wait_for(timeout=10000)
                    await last_input.fill(last)
                    if first:
                        await first_input.fill(first)
                    await page.wait_for_timeout(500)

                    search_btn = page.locator(
                        "input[type='submit'][value*='Search' i], "
                        "button:has-text('Search'), "
                        "input[name*='Search' i]"
                    ).first
                    await search_btn.click()
                    await page.wait_for_timeout(5000)

                    text = await self._get_page_text(page)
                    result.raw_data = {"url": page.url, "text_length": len(text)}
                    result.hits = self._parse_results(text, first, last, page.url)

                except Exception:
                    text = await self._get_page_text(page)
                    result.hits.append({
                        "note": "Could not interact with MDE search form",
                        "url": page.url,
                        "page_preview": text[:500],
                    })

        except Exception as e:
            result.error = str(e)
        return result

    def _parse_results(self, text: str, first: str, last: str, url: str) -> list[dict]:
        hits = []
        lines = text.split("\n")
        current = {}

        for line in lines:
            line = line.strip()
            if not line:
                continue
            ll = line.lower()

            if last.lower() in ll and (not first or first.lower() in ll):
                if current and current.get("name"):
                    hits.append(current)
                current = {"name": line}
            elif "certificate" in ll or "credential" in ll:
                current["credential"] = line
            elif "valid" in ll or "expire" in ll or "issue" in ll:
                current["validity"] = line
            elif "condition" in ll or "restriction" in ll:
                current["conditions"] = line
            elif "school admin" in ll or "administrator" in ll:
                current["cert_type"] = line
            elif "endorsement" in ll:
                current["endorsement"] = line

        if current:
            hits.append(current)

        if not hits:
            if "no records" in text.lower() or "no results" in text.lower():
                return [{"note": f"No educator records: {first} {last}", "url": url}]
            elif len(text) > 200:
                return [{
                    "note": "Results page loaded — may need parser refinement",
                    "url": url,
                    "text_preview": text[:1000],
                }]
        return hits

