#!/usr/bin/python3
"""describes a class for inherited lists. MyList"""


class MyList(list):
    """Deploys sorted printing functionality for the integrated list class."""

    def print_sorted(self):
        """A list arranged ascendingly can be printed."""
        print(sorted(self))
