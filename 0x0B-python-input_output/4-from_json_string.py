#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Provide back a JSON string's object representation in Python."""
    return json.loads(my_str)
