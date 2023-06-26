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

    process(input_file)
