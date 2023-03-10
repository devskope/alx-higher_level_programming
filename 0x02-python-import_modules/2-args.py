#!/usr/bin/python3

"""Command line args."""


def printArgs():
    """Print the number of and list of arguments."""
    from sys import argv

    count = len(argv) - 1

    if count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments{':' if count else '.'}")

    for (i, v) in enumerate(argv[1:]):
        print(f"{i + 1}: {v}")


if __name__ == "__main__":
    printArgs()
