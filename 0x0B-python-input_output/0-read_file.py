#!/usr/bin/python3
"""Define a function to read text from a file."""


def read_file(filename=""):
    """Print contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
