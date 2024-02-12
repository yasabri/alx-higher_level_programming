#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """
        Base is implemented by class Rectangle.
        Techniques:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            sets the class instance to its initial state
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            __width getter function
            Returns:
                width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter function.
            Args:
                value (int): value that should be determined
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            get function for altitude
            Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter function
            Args:
                value (int): to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter method used to x
            Args:
                value (int): to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter method for the variable y
            Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function pertaining to y
            Args:
                value (int): to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            returns area of Rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
            prints stdout Rectangle instance with '#'
        """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height - 1):
#            rectangle += print_symbol * self.__width + "\n"
#        rectangle += print_symbol * self.__width

#        print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            allocates a key/value argument to an attribute;
            if args is not empty, kwargs is skipped.
            Args:
                *args: a variable number of arguments without keywords;
                **kwargs: a variable number of arguments with keywords
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            yields the dictionary representation of a correct
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
