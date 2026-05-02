"""Fetch input from the remote service."""

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup

from advent_of_code.api import AdventApiError, ui
from advent_of_code.core.utils import get_token, safe_request


CACHE_ROOT = Path.home() / ".cache" / "advent-of-code" / "challenges"
USER_AGENT = "heavycircle (+https://github.com/heavycircle)"


def get_cache_path(year: int, day: int, filename: str) -> Path:
    """Helper to resolve the absolute cache path.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.
        filename (str): The name of the cache file.

    Returns:
        Path: The path to the expected cache file.

    """
    return CACHE_ROOT / f"{year:04}" / f"day-{day:02}" / filename


def fetch_real(year: int, day: int) -> None:
    """Fetch the real input from the AoC API.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.

    """
    fp = get_cache_path(year, day, "real.txt")
    if fp.is_file():
        ui.out_warning(f"Real input for Day {day} already cached.")
        return

    ui.out_info(f"Downloading real input for {year} Day {day}...")
    token = get_token().strip()

    res = safe_request(
        "get",
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={
            "Cookie": f"session={token}",
            "User-Agent": USER_AGENT,
        },
    )

    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_bytes(res.content)


def fetch_test(year: int, day: int) -> None:
    """Scrape the test input from the AoC Challenge page.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.

    Raises:
        AdventApiError: Cannot find example code block on the page.

    """
    fp = get_cache_path(year, day, "test.txt")
    if fp.is_file():
        ui.out_warning(f"Test input for Day {day} already cached.")
        return

    ui.out_info(f"Scraping test input for {year} Day {day}...")
    res = safe_request(
        "get",
        f"https://adventofcode.com/{year}/day/{day}",
        headers={"User-Agent": USER_AGENT},
    )

    soup = BeautifulSoup(res.content, "html.parser")
    code_block = soup.select_one("pre > code")
    if not code_block:
        raise AdventApiError("Could not find the example code block (pre > code) in the page.")

    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(code_block.get_text(strip=False), encoding="utf-8")


def fetch(year: int, day: int) -> None:
    """Fetch the challenge real and test input.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.

    """
    fetch_real(year, day)
    fetch_test(year, day)


__all__ = ["fetch"]
