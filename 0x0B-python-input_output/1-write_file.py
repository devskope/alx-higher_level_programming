#!/usr/bin/python3
"""Defines a function to write to a file."""


def write_file(name="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        name (str): Name of the file to write into.
        text (str): Text to insert into the file.
    Returns:
        The number of characters written.
    """
    with open(name, "w", encoding="utf-8") as file:
        return file.write(text)
