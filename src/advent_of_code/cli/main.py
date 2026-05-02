from __future__ import annotations

import sys

import typer

from advent_of_code.api import AdventError, ui
from advent_of_code.cli import commands


app = typer.Typer()
app.add_typer(commands.app)


@app.callback()
def main_config(debug: bool = typer.Option(False, "--debug", help="Enable debug logging and tracebacks.")) -> None:
    """The AdventOfCode CLI is responsible for initializing AoC challenges.

    Args:
        debug (bool): True if this CLI run is in debug mode.

    """
    ui.set_debug(debug)


def main() -> None:
    """CLI entrypoint and app driver.

    Raises:
        AdventError: Catch-all for Runtime errors.
            Debug-mode only for more source outputs.
        Exception: Catch-all for unexpected errors.
            Debug-mode only for more source outputs.

    """
    try:
        app()
    except AdventError as e:
        if ui.debug_mode:
            raise
        ui.out_error(f"{e}")
        sys.exit(1)
    except Exception as e:  # pylint: disable=broad-exception-caught
        if ui.debug_mode:
            raise
        ui.out_error(f"{e}")
        ui.out_info("Run with --debug for more details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
