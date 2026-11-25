"""NMLS Consumer Access — financial licensing lookup.

Portal: nmlsconsumeraccess.org
Searches for mortgage/financial licensing (relevant to Shayla/Lake Trust).
"""

from __future__ import annotations
from sources.browser_source import BrowserSource, new_page
from models import SearchResult

NMLS_URL = "https://www.nmlsconsumeraccess.org/"


class NMLSBrowserSource(BrowserSource):
    name = "nmls_browser"

    async def search_person(self, person: dict) -> list[SearchResult]:
        if not person.get("searches", {}).get("nmls"):
            return []
        r = await self._search_individual(person["name"], person["id"], person["name"])
        return [r]

    async def _search_individual(
        self, name: str, target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"nmls: {name}",
        )
        try:
            async with new_page() as page:
                await self._goto_and_wait(page, NMLS_URL, timeout=20000)
                await page.wait_for_timeout(2000)

                parts = name.split()
                last = parts[-1] if parts else name
                first = parts[0] if len(parts) > 1 else ""

                last_input = page.locator(
                    "input[name*='LastName' i], input[id*='LastName' i], "
                    "input[placeholder*='last' i]"
                ).first
                first_input = page.locator(
                    "input[name*='FirstName' i], input[id*='FirstName' i], "
                    "input[placeholder*='first' i]"
                ).first

                try:
                    await last_input.wait_for(timeout=10000)
                    await last_input.fill(last)
                    if first:
                        await first_input.fill(first)

                    state_select = page.locator("select[name*='state' i], select[id*='state' i]").first
                    try:
                        await state_select.select_option(label="Michigan")
                    except Exception:
                        try:
                            await state_select.select_option(value="MI")
                        except Exception:
                            pass

                    await page.wait_for_timeout(500)
                    search_btn = page.locator(
                        "button[type='submit'], input[type='submit'], "
                        "button:has-text('Search'), a:has-text('Search')"
                    ).first
                    await search_btn.click()
                    await page.wait_for_timeout(3000)

                    text = await self._get_page_text(page)
                    result.raw_data = {"url": page.url, "text_length": len(text)}

                    if "no results" in text.lower() or "0 results" in text.lower():
                        result.hits.append({
                            "note": f"No NMLS records for {name}",
                            "conclusion": "NOT REGISTERED",
                        })
                    elif last.lower() in text.lower():
                        result.hits.append({
                            "note": "Results found — parse for license details",
                            "url": page.url,
                            "text_preview": text[:1000],
                        })
                    else:
                        result.hits.append({
                            "note": "Search completed, no matching names in results",
                            "url": page.url,
                        })

                except Exception:
                    text = await self._get_page_text(page)
                    search_input = page.locator("input[type='text'], input[type='search']").first
                    try:
                        await search_input.fill(name)
                        await page.keyboard.press("Enter")
                        await page.wait_for_timeout(3000)
                        text = await self._get_page_text(page)
                        result.hits.append({
                            "note": "Fallback search executed",
                            "url": page.url,
                            "text_preview": text[:500],
                        })
                    except Exception:
                        result.hits.append({
                            "note": "Could not interact with NMLS search",
                            "url": page.url,
                        })

        except Exception as e:
            result.error = str(e)
        return result

