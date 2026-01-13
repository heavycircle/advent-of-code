"""
Fetch input from the remote service.
"""

from pathlib import Path

import requests
from bs4 import BeautifulSoup

from ..logger import get_logger


logger = get_logger()


def fetch_test(year: int, day: int) -> bool:
    """Fetch the test file from AOC"""

    # Check the cache
    fp = Path(f".cache/{year:04}/day-{day:02}/test.txt").resolve()
    if fp.is_file():
        logger.warning("Test Input file already exists!")
        return True

    # Get the source code
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}",
        headers={"User-Agent": "heavycircle (+https://github.com/heavycircle)"},
    )
    assert res.status_code == requests.codes.ok

    # Find the first <code> tag inside a <pre> tag
    soup = BeautifulSoup(res.content, "html.parser")
    pre = soup.find("pre")
    if not pre:
        logger.error("Could not find pre block in HTML")
        return False
    code = pre.find("code")
    if not code:
        logger.error("Could not find code block inside a pre")
        return False

    # Write to the cache
    fp.parent.mkdir(parents=True, exist_ok=True)
    with fp.open(mode="w") as fw:
        fw.write(code.get_text(strip=False))
    return True
