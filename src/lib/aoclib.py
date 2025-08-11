"""
Advent of Code Python utilities.
"""

from os import getcwd
from pathlib import Path


def __version__():
    return "v0.1.0"


def get_data(year: int, day: int) -> str:
    """
    Get the input data for a specified year and day.

    :param year: Year of challenge
    :param day: Day of challenge
    :return Input data contents
    """

    cwd = Path(getcwd())
    infile = cwd / "input" / str(year) / f"day-{day:02d}.txt"
    if not infile.exists():
        print(f"get_data: missing input file: year={year} day={day}")
        exit(1)

    return infile.read_text().strip()
