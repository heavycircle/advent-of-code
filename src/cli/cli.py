import os
import pathlib

import typer

from .fetch import fetch
from .logger import get_logger
from .readme import update_readme


app = typer.Typer()
logger = get_logger()


@app.command()
def init(year: int, day: int, lang: str = "py"):
    """Make a new project directory."""

    logger.info("Fetching Files...")
    if not fetch(year, day):
        logger.error("Could not fetch input files!")
        return False

    logger.info("Making Directories...")
    dir_name = f"{year:04}/day-{day:02}"
    os.makedirs(dir_name, exist_ok=True)
    for file in ("real.txt", "test.txt"):
        rel_dir = pathlib.Path("../..") / ".cache" / dir_name
        rel_path = rel_dir / file

        link_path = pathlib.Path(dir_name) / file
        os.symlink(rel_path, link_path)


@app.command()
def run(year: int, day: int, lang: str = "py"):
    """Run the AOC project for a language."""

    if not fetch(year, day):
        logger.error("Could not fetch input files!")
        return False


@app.command()
def readme():
    """Update the README with the number of solves."""

    update_readme()
