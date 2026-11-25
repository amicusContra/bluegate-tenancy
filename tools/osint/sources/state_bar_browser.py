"""State Bar of Michigan — browser-based attorney verification.

Uses zeekbeek.com/SBM which requires JavaScript rendering.
"""

from __future__ import annotations
from sources.browser_source import BrowserSource, new_page
from models import SearchResult

SEARCH_URL = "https://www.reliaguide.com/SBM"


class StateBarBrowserSource(BrowserSource):
    name = "state_bar_browser"

    async def search_person(self, person: dict) -> list[SearchResult]:
        if not person.get("searches", {}).get("state_bar"):
            return []
        parts = person["name"].split()
        last = parts[-1] if parts else person["name"]
        first = parts[0] if len(parts) > 1 else ""
        r = await self._search_attorney(first, last, person["id"], person["name"])
        return [r]

    async def _search_attorney(
        self, first: str, last: str, target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"attorney: {first} {last}",
        )
        try:
            async with new_page() as page:
                await self._goto_and_wait(page, SEARCH_URL, timeout=20000)
                await page.wait_for_timeout(2000)

                first_input = page.locator(
                    "input[name*='irst' i], input[placeholder*='first' i], "
                    "input[id*='first' i], input[name*='FirstName']"
                ).first
                last_input = page.locator(
                    "input[name*='ast' i], input[placeholder*='last' i], "
                    "input[id*='last' i], input[name*='LastName']"
                ).first

                try:
                    await first_input.wait_for(timeout=10000)
                    await first_input.fill(first)
                    await last_input.fill(last)
                    await page.wait_for_timeout(500)

                    search_btn = page.locator(
                        "button[type='submit'], input[type='submit'], "
                        "button:has-text('Search'), a:has-text('Search')"
                    ).first
                    await search_btn.click()
                    await page.wait_for_timeout(3000)

                    text = await self._get_page_text(page)
                    result.raw_data = {"url": page.url, "text_length": len(text)}
                    result.hits = self._parse_results(text, first, last)

                except Exception:
                    text = await self._get_page_text(page)
                    if "search" in text.lower():
                        try:
                            search_box = page.locator("input[type='text'], input[type='search']").first
                            await search_box.fill(f"{first} {last}")
                            await page.keyboard.press("Enter")
                            await page.wait_for_timeout(3000)
                            text = await self._get_page_text(page)
                            result.hits = self._parse_results(text, first, last)
                        except Exception:
                            result.hits.append({
                                "note": "Could not interact with search form",
                                "url": page.url,
                                "page_preview": text[:500],
                            })
                    else:
                        result.hits.append({
                            "note": "Page loaded but search form not found",
                            "url": page.url,
                        })

        except Exception as e:
            result.error = str(e)
        return result

    def _parse_results(self, text: str, first: str, last: str) -> list[dict]:
        hits = []
        text_lower = text.lower()

        if "no results" in text_lower or "no members found" in text_lower or "0 result" in text_lower:
            return [{"note": f"No attorney found: {first} {last}", "conclusion": "NOT LICENSED"}]

        lines = text.split("\n")
        current = {}
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if last.lower() in line.lower() and first.lower() in line.lower():
                if current:
                    hits.append(current)
                current = {"name": line}
            elif line.startswith("P") and len(line) <= 8 and line[1:].isdigit():
                current["bar_number"] = line
            elif "active" in line.lower() and len(line) < 30:
                current["status"] = line
            elif "inactive" in line.lower() and len(line) < 30:
                current["status"] = line
            elif "suspended" in line.lower() and len(line) < 30:
                current["status"] = line
            elif any(w in line.lower() for w in ["admitted", "admission"]):
                current["admission_info"] = line

        if current:
            hits.append(current)

        if not hits and last.lower() in text_lower:
            hits.append({
                "note": f"Name '{last}' found in page text — manual review needed",
                "text_preview": text[:1000],
            })
        elif not hits:
            hits.append({"note": f"No attorney found: {first} {last}", "conclusion": "NOT LICENSED"})

        return hits

