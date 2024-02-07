#!/usr/bin/python3
"""discraeb inherited class-checking function."""


def inherits_from(obj, a_class):
    """determines if an item is a class instance that was inherited

    Args:
        obj (any): object to check
        a_class (type): class to match type of obje to.
    Returns:
        If obj is an instance of a_class that was inherited: True.
        If not, then false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
