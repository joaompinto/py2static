from pathlib import Path

import typer

from ..process import process

is_verbose = False


def py2static(
    input_file: str = typer.Argument(..., help="Python input file"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose mode"),
):
    if verbose:
        print("Running in verbose mode")
        global is_verbose
        is_verbose = True
    ouput_file = Path(Path(input_file).resolve().stem)
    if ouput_file.exists():
        raise Exception(f"Output file `{ouput_file}` already exists")
    process(input_file)
