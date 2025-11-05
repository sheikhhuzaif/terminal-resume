"""Main CLI entry point."""

import typer
from rich.console import Console
from rich.panel import Panel
from typing import Optional

from .commands import info, work_exp, contact, summary, projects, education, skills

app = typer.Typer(
    name="sheikh-huzaif-resume",
    help="A CLI tool to showcase my CV",
    add_completion=False,
    rich_markup_mode="rich",  # Explicitly set rich markup mode
)
console = Console()

# Register commands
app.command(name="info")(info.main)
app.command(name="contact")(contact.main)
app.command(name="summary")(summary.main)
app.command(name="work-exp")(work_exp.main)
app.command(name="projects")(projects.main)
app.command(name="education")(education.main)
app.command(name="skills")(skills.main)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        is_flag=True,
    ),
):
    """
    My CLI Tool - A powerful command-line application.
    
    Run my-cli COMMAND --help for command-specific help.
    """
    if version:
        console.print("[bold cyan]my-cli[/bold cyan] version 1.0.0")
        raise typer.Exit()
    
    if ctx.invoked_subcommand is None:
        welcome_text = """[bold cyan]Welcome to My CLI Tool![/bold cyan]

A powerful command-line application built with Python.

Run [bold green]my-cli --help[/bold green] to see available commands."""
        
        console.print(Panel(welcome_text, border_style="cyan", padding=(1, 2)))


def run():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    run()