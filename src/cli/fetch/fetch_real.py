"""
Fetch input from the remote service.
"""

from pathlib import Path

import requests

from ..logger import get_logger
from .utils import get_token


logger = get_logger()


def fetch_real(year: int, day: int) -> bool:
    """Fetch the input file from AOC"""

    # Check the cache
    fp = Path(f".cache/{year:04}/day-{day:02}/real.txt").resolve()
    if fp.is_file():
        logger.warning("Real Input file already exists!")
        return True

    # Get the token from advent
    token = get_token().strip()
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={
            "Cookie": f"session={token}",
            "User-Agent": "heavycircle (+https://github.com/heavycircle)",
        },
    )
    assert res.status_code == 200

    # Write to the cache
    fp.parent.mkdir(parents=True, exist_ok=True)
    with fp.open(mode="wb") as fw:
        fw.write(res.content)
    return True
