# py2static

This is a simple tool for building Linux static binaries (x64) from Python scripts.

[![PyPi](https://img.shields.io/pypi/v/py2static.svg?style=flat-square)](https://pypi.python.org/pypi/py2static)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

# Introduction

It uses [Pyinstaller](https://pyinstaller.org/) to build a dynamic binary and  uses [staticx](https://github.com/JonathonReinhart/staticx) to make it static.

# Installation

```bash
pip install py2static
```
# Usage

```bash
# This will generate the binary "script"
py2static script.py
```

# Limitations
It was developed and tested with single scripts using the standard python library. It may not work with more complex projects. Feel free to open an issue if you have more complex cases that would like to be supported.
