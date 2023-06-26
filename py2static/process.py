import sys
from pathlib import Path
from subprocess import getoutput, getstatusoutput
from tempfile import NamedTemporaryFile, TemporaryDirectory


def process(input_file: str, output_file: str = None):
    if output_file is None:
        output_file = Path(input_file).stem
    print("Processing", input_file)
    input_file = Path(input_file).resolve().as_posix()
    spec_file = Path(__file__).parent.joinpath("default.spec_txt")
    with open(spec_file, "r") as spec_file:
        data = spec_file.read()
        data = data.replace("{{input_file}}", input_file)
        data = data.replace("{{output_file}}", output_file)
    with TemporaryDirectory() as tmpdir:
        with NamedTemporaryFile(suffix=".spec") as tmpfile:
            tmpfile.write(data.encode("utf-8"))
            tmpfile.flush()
            print("Building dynamic binary... ", end="")
            rc, output = getstatusoutput(
                f'pyinstaller --workpath "{tmpdir}" --distpath "{tmpdir}" {tmpfile.name}'
            )
            if rc != 0:
                print(output, file=sys.stderr)
                raise Exception("Error running pyinstaller")
            output = getoutput(f"file {tmpdir}/{output_file}")
            if "ELF 64-bit LSB executable" not in output:
                print(output, file=sys.stderr)
                raise Exception("Failed to build dynamic binary")
            print("done")
            output_dir = Path(input_file).parent
            print("Building static binary... ", end="")
            rc, output = getstatusoutput(
                f"staticx {tmpdir}/{output_file} {output_dir}/{output_file}"
            )
            if rc != 0:
                print(output, file=sys.stderr)
                raise Exception("Failed to build static binary")
            print("done")
