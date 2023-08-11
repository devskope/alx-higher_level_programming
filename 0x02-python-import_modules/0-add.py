#!/usr/bin/python3
"""Import external function."""

if __name__ == "__main__":
    """Import add(a, b)."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
