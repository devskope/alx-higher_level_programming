#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print list in reverse."""
    [print('{:d}'.format(i))for i in reversed(my_list)]
