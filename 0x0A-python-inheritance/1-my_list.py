#!/usr/bin/python3
"""MyList class."""


class MyList(list):
    """Subclass of list."""

    def __init__(self):
        """Initialize the object."""
        super().__init__()

    def print_sorted(self):
        """Print sorted list."""
        print(sorted(self.copy()))
