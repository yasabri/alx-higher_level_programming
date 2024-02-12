#*/usr/bin/python3
"""the model of base class"""

class Base:
    """representation of the base for oop hierarchy"""

    __nb_objects = 0

    def __init__(self, id=None):
        """construc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
