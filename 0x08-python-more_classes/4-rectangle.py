#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retriever for the width of the private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """height, a private instance property setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retriever for the width of the private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height, a private instance property setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """provides a reproducible string representation of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """provides a reproducible string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """provides a reproducible string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """provides a reproducible string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
