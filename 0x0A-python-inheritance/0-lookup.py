#!/usr/bin/python3
"""Define an object attribute lookup function."""


def lookup(obj):
    """Return a list of available attributes on object."""
    return (dir(obj))
