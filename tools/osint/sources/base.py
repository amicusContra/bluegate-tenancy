"""Base class for all OSINT search sources."""

from __future__ import annotations
from abc import ABC, abstractmethod
from models import SearchResult


class Source(ABC):
    name: str = "base"
    requires_key: bool = False

    @abstractmethod
    async def search_person(self, person: dict) -> list[SearchResult]:
        """Run all relevant searches for a person target."""
        ...

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        """Run all relevant searches for an entity target."""
        return []

    async def search_address(self, address: dict) -> list[SearchResult]:
        """Run all relevant searches for an address target."""
        return []

    def available(self) -> bool:
        """Return True if this source is configured and ready."""
        return True

