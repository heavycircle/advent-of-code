from __future__ import annotations

import os
import shutil
import stat
from pathlib import Path

import typer

from advent_of_code.api import AdventError, ui
from advent_of_code.core.fetch import fetch
from advent_of_code.core.readme import update_readme


app = typer.Typer()


@app.command()
def init(year: int, day: int, lang: str = "py") -> None:
    """Make a new project directory.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.
        lang (str, optional): The challenge default languge.
            Defaults to python.

    """

    ui.out_info("Fetching Files...")
    fetch(year, day)

    ui.out_info("Making Directories...")
    challenge_dir = Path("challenges") / f"{year:04}" / f"day-{day:02}"
    challenge_dir.mkdir(parents=True, exist_ok=True)

    cache_root = Path.home() / ".cache" / "advent-of-code" / "challenges"
    cache_dir = cache_root / f"{year:04}" / f"day-{day:02}"
    cache_dir.mkdir(parents=True, exist_ok=True)

    for file in ("real.txt", "test.txt"):
        source_file = cache_dir / file
        source_file.touch(exist_ok=True)

        link_path = challenge_dir / file
        if link_path.exists() or link_path.is_symlink():
            link_path.unlink()
        os.symlink(source_file, link_path)

    template_dir = Path("templates")
    if template_dir.exists() and template_dir.is_dir():
        challenge_file = template_dir / f"main.{lang}"
        template_file = template_dir / f"main.{lang}"
        if not template_file.exists():
            ui.out_warning("No template file!")
            challenge_file.touch()
        else:
            shutil.copy(template_file, challenge_file)

        st = os.stat(challenge_file)
        os.chmod(challenge_file, st.st_mode | stat.S_IEXEC)


@app.command()
def run(year: int, day: int, lang: str = "py") -> None:
    """Run the AOC project for a language."""

    if not fetch(year, day):
        raise AdventError("Cannot fetch input files!")


@app.command()
def readme() -> None:
    """Update the README with the number of solves."""

    update_readme()
