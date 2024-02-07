#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the basic data structure's dictionary representation"""
    return obj.__dict__
