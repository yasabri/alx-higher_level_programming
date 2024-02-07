#!/usr/bin/python3
""" Module has a method that yields an object's JSON representation
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj (object): The object to be converted to JSON.

    Raises:
        Exception: If the object cannot be encoded to JSON.
    """

    return json.dumps(my_obj)
