#!/usr/bin/python3

"""Print number of and list of arguments."""


def printArgs():
    """Print the number of and list of arguments."""
    from sys import argv

    count = len(argv) - 1

    if count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments{':' if count else '.'}")

    for (i, val) in enumerate(argv[1:]):
        print(f"{i + 1}: {val}")


if __name__ == "__main__":
    printArgs()
