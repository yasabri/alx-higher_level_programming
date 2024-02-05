#!/usr/bin/python3
"""Specifies a BaseGeometry class for basic geometry"""

class BaseGeometry:
    """class with integer_validator and public instance methods area"""
    def area(self):
        """creates an exception when prompted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """confirms that the value is an integer bigger than zero"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
