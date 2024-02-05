#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """Sorted printing is implemented for the built-in list class"""
    def __init__(self):
        """Sorted printing is implemented for the built-in list class"""
        super().__init__()

    def print_sorted(self):
        """Print a list with the items arranged ascending"""
        print(sorted(self))
