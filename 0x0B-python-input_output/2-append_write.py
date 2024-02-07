#!/usr/bin/python3
"""describes class-checking function."""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of given class """

    if type(obj) == a_class:
        return True
    return False
