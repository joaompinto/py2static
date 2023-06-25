import io
from pathlib import Path
from setuptools import setup

SCRIPT_DIR = Path(__file__).parent


scm_version_options = {"write_to": "py2static/version.py"}


def setup_package():

    # Get readme
    readme_path = Path(SCRIPT_DIR, "README.md")
    with io.open(readme_path, encoding="utf8") as f:
        readme = f.read()

    # Get requiremeents
    with io.open("requirements.txt", encoding="utf8") as f:
        requirements = f.read()

    setup(
        use_scm_version=scm_version_options,
        long_description=readme,
        long_description_content_type="text/markdown",
        install_requires=[x for x in requirements.splitlines() if x],
    )


if __name__ == "__main__":
    setup_package()
