"""Data models for OSINT search results."""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class SearchResult:
    source: str
    target_id: str
    target_name: str
    query: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    hits: list[dict[str, Any]] = field(default_factory=list)
    raw_data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    @property
    def hit_count(self) -> int:
        return len(self.hits)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "target_id": self.target_id,
            "target_name": self.target_name,
            "query": self.query,
            "timestamp": self.timestamp,
            "hit_count": self.hit_count,
            "hits": self.hits,
            "error": self.error,
        }

    def to_markdown(self) -> str:
        lines = [
            f"### {self.source} — {self.target_name}",
            f"**Query:** `{self.query}`  ",
            f"**Time:** {self.timestamp}  ",
            f"**Hits:** {self.hit_count}",
            "",
        ]
        if self.error:
            lines.append(f"**ERROR:** {self.error}\n")
        for i, hit in enumerate(self.hits, 1):
            lines.append(f"#### Hit {i}")
            for k, v in hit.items():
                if v is not None and v != "":
                    lines.append(f"- **{k}:** {v}")
            lines.append("")
        return "\n".join(lines)

