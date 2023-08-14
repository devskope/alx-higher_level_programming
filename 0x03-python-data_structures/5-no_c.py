#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_str = ""
    for i in my_string:
        if i not in "cC":
            new_str += i
    return new_str
