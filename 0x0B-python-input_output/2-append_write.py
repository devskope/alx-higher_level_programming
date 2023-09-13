#!/usr/bin/python3
"""Defines a function to append to file."""


def append_write(name="", text=""):
    """Append a string to the end of a UTF8 text file.

    Args:
        name (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(name, "a", encoding="utf-8") as file:
        return file.write(text)
