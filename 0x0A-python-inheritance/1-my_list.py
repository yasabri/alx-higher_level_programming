#!/usr/bin/python3
"""Describes the MyList inheritable list class"""

class MyList(list):
    """Sorted printing is implemented for the built-in list class"""

    def print_sorted(self):
        """Print a list with the items arranged ascending"""
        print(sorted(self))
