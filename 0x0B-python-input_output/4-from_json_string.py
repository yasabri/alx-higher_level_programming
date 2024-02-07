#!/usr/bin/python3
""" Module that contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
        """determines if an item is a class instance that was inherited

    Args:
        obj (any): object to check
        a_class (type): class to match type of obje to.
    Returns:
        If obj is an instance of a_class that was inherited: True.
        If not, then false
    """
    return json.loads(my_str)
