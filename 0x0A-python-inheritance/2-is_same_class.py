#!/usr/bin/python3
"""Check if an object is exactly an instance of a given class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
