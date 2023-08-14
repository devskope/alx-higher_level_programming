#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print list of intergers."""
    [print('{:d}'.format(i)) for i in my_list]
