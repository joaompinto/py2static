from pathlib import Path
from subprocess import getoutput
from tempfile import NamedTemporaryFile

from py2static.process import process


def test_py2static():
    with NamedTemporaryFile(suffix="_test.py") as tmpfile:
        tmpfile.write(b"print('Hello World')")
        process(tmpfile.name)
        output_file = Path(tmpfile.name).parent.joinpath(Path(tmpfile.name).stem)
        output = getoutput(f"file {output_file}")
        assert "statically linked" in output
