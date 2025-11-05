"""Contact command implementation."""

import typer
from rich.console import Console
from rich.table import Table

from ..data import resume
console = Console()

def main(
        verbose: bool = typer.Option(
        False,
        help="Show detailed information"
    ),
):
    """Contact Information"""
    contact_info = resume.get("contact")
    if not contact_info:
        console.print("[bold red]Error:[/bold red] No contact information found.")
        raise typer.Exit(code=1)

    table = Table(title="📇 Contact Information", show_header=False, box=None, padding=(0, 2))
    table.add_row("[bold cyan]Name[/bold cyan]", contact_info.get("name", "N/A"))
    table.add_row("[bold cyan]Email[/bold cyan]", contact_info.get("email", "N/A"))
    table.add_row("[bold cyan]Phone[/bold cyan]", contact_info.get("phone", "N/A"))
    table.add_row("[bold cyan]LinkedIn[/bold cyan]", contact_info.get("linkedin", "N/A"))
    table.add_row("[bold cyan]GitHub[/bold cyan]", contact_info.get("github", "N/A"))

    console.print(table)
        
