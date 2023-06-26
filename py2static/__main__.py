import typer

from .cli import main

is_verbose = False

app = typer.Typer(short_help="Utility to manage rootbox containers")
app.command()(main.py2static)

if __name__ == "__main__":
    app()
