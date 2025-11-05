"""Summary command implementation."""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import textwrap

from ..data import resume
console = Console()

def main(
        verbose: bool = typer.Option(
        False,
        help="Show detailed information"
    ),
):
    """
    Professional Summary
    """
    summary = resume.get("summary")
    if not summary:
        console.print("[bold red]No summary provided.[/bold red]")
        return

    # Wrap text for better CLI readability
    wrapped = textwrap.fill(summary, width=80)

    # Create styled text
    styled_text = Text(wrapped, justify="left")
    styled_text.stylize("italic cyan", 0, len(wrapped))

    # Print inside a panel for nice border and title
    panel = Panel(
        styled_text,
        title="💼 Professional Summary",
        border_style="bright_blue",
        padding=(1, 2),
        expand=False,
    )
    console.print(panel)
