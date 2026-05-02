from __future__ import annotations

from typing import Any

from rich.console import Console
from rich.theme import Theme


screener_theme = Theme(
    {
        "debug": "dim italic",
        "info": "bold cyan",
        "warning": "bold yellow",
        "error": "bold red",
        "success": "bold green",
    }
)


class UserInterface:
    """Provide a logging interface."""

    def __init__(self) -> None:
        self.console = Console(theme=screener_theme, stderr=True)
        self.debug_mode: bool = False

    def set_debug(self, enabled: bool) -> None:
        """Set the debug mode for the ui.

        Args:
            enabled (bool): True if debug mode is enabled.

        """
        self.debug_mode = enabled
        if enabled:
            self.out_debug("Debug mode enabled!")

    def out_debug(self, msg: Any) -> None:
        """Print a debug message.

        Args:
            msg (Any): String to print to console.

        """
        if self.debug_mode:
            self.console.print(f"[debug][ ] {msg}[/debug]")

    def out_info(self, msg: Any) -> None:
        """Print an info message with a cyan [*] prefix.

        Args:
            msg (Any): String to print to console.

        """
        self.console.print(f"[info][*][/info] {msg}")

    def out_success(self, msg: Any) -> None:
        """Print a success message with a green [+] prefix.

        Args:
            msg (Any): String to print to console.

        """
        self.console.print(f"[success][+][/success] {msg}")

    def out_warning(self, msg: Any) -> None:
        """Print a warning message with a yellow [*] prefix.

        Args:
            msg (Any): String to print to console.

        """
        self.console.print(f"[warning][*][/warning] {msg}")

    def out_error(self, msg: Any) -> None:
        """Print an error message with a red [!] prefix.

        Args:
            msg (Any): String to print to console.

        """
        self.console.print(f"[error][!][/error] {msg}")

    @property
    def raw(self) -> Console:
        """Return the console itself."""
        return self.console


ui = UserInterface()
