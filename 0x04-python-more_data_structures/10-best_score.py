#!/usr/bin/python3
def best_score(a_dictionary):
    """Print dictionary key with biggest value."""
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
