#!/usr/bin/python3
"""Print sum of args."""


def sumArgs():
    """Print the addition of all arguments."""
    from sys import argv

    args = [int(i) for i in argv[1:]]
    print(f"{sum(args)}")


if __name__ == "__main__":
    sumArgs()
