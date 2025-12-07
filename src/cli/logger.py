import logging
import sys

from rich.console import Console
from rich.logging import RichHandler

LOG_LEVEL = logging.INFO
FORMAT = "%(message)s"

ICON_MAP = {
    logging.DEBUG: "[bold blue]•[/bold blue]",
    logging.INFO: "[bold green]:white_check_mark:[/bold green]",
    logging.WARNING: "[bold yellow]*[/bold yellow]",
    logging.ERROR: "[bold red]:x:[/bold red]",
    logging.CRITICAL: "[bold red]:cross_mark:[/bold red]",
}


class CustomFormatter(logging.Formatter):
    """Custom formatter prepending the icon"""

    def format(self, record: logging.LogRecord) -> str:
        icon = ICON_MAP.get(record.levelno, "[grey]?[/grey]")
        record.msg = f"[{icon}]  {record.getMessage()}"
        return super().format(record)


def get_logger():
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    console = Console(file=sys.stderr)
    handler = RichHandler(
        level=LOG_LEVEL,
        markup=True,
        rich_tracebacks=True,
        show_time=False,
        show_level=False,
        console=console,
    )

    handler.setFormatter(CustomFormatter(fmt=FORMAT))
    root_logger.handlers = [handler]
    return root_logger
