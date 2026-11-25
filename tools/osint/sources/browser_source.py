"""Base class for Playwright browser-based OSINT sources.

Manages a shared browser instance to avoid launching Chromium per query.
All browser-based scrapers inherit from this.
"""

from __future__ import annotations
from abc import abstractmethod
from contextlib import asynccontextmanager
from playwright.async_api import async_playwright, Browser, Page, BrowserContext
from sources.base import Source
from models import SearchResult

_browser_instance: Browser | None = None
_context_instance: BrowserContext | None = None


async def get_browser() -> Browser:
    global _browser_instance
    if _browser_instance is None or not _browser_instance.is_connected():
        pw = await async_playwright().start()
        _browser_instance = await pw.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
    return _browser_instance


async def get_context() -> BrowserContext:
    global _context_instance
    browser = await get_browser()
    if _context_instance is None:
        _context_instance = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/128.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            java_script_enabled=True,
        )
    return _context_instance


async def close_browser():
    global _browser_instance, _context_instance
    try:
        if _context_instance:
            await _context_instance.close()
    except Exception:
        pass
    _context_instance = None
    try:
        if _browser_instance:
            await _browser_instance.close()
    except Exception:
        pass
    _browser_instance = None


@asynccontextmanager
async def new_page():
    ctx = await get_context()
    page = await ctx.new_page()
    try:
        yield page
    finally:
        await page.close()


class BrowserSource(Source):
    """Base for all browser-automated sources."""
    requires_browser = True

    def available(self) -> bool:
        try:
            from playwright.async_api import async_playwright
            return True
        except ImportError:
            return False

    async def _goto_and_wait(self, page: Page, url: str, wait_selector: str | None = None, timeout: int = 15000):
        await page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        if wait_selector:
            try:
                await page.wait_for_selector(wait_selector, timeout=timeout)
            except Exception:
                pass
        await page.wait_for_timeout(1000)

    async def _get_page_text(self, page: Page) -> str:
        return await page.evaluate("() => document.body.innerText")

    async def _get_page_html(self, page: Page) -> str:
        return await page.content()

