"""Configuration loader — reads targets.json and .env."""

from __future__ import annotations
import json
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

load_dotenv(ROOT / ".env")


def get_key(name: str) -> str | None:
    return os.getenv(name) or None


def load_targets() -> dict:
    with open(ROOT / "targets.json", encoding="utf-8") as f:
        return json.load(f)


def get_person(target_id: str) -> dict | None:
    data = load_targets()
    for p in data["people"]:
        if p["id"] == target_id:
            return p
    return None


def get_entity(entity_id: str) -> dict | None:
    data = load_targets()
    for e in data["entities"]:
        if e["id"] == entity_id:
            return e
    return None


def get_address(addr_id: str) -> dict | None:
    data = load_targets()
    for a in data["addresses"]:
        if a["id"] == addr_id:
            return a
    return None


def all_people() -> list[dict]:
    return load_targets()["people"]


def all_entities() -> list[dict]:
    return load_targets()["entities"]


def all_addresses() -> list[dict]:
    return load_targets()["addresses"]

