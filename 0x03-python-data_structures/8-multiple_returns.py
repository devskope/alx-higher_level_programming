#!/usr/bin/python3

def multiple_returns(sentence):
    """Return length and first character of string."""
    first_char = None if len(sentence) == 0 else sentence[0]
    return (len(sentence), first_char)
