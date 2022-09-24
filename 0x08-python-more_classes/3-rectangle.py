#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the attribute  height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area"""
        return (self.height * self.width)

    def perimeter(self):
        """returns the perimeter"""
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2*self.height + 2*self.width)

    def __str__(self):
        """Prints the rectangle with the `#` character."""
        string = ""

        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(0, self.__height):
            string += "{:s}".format(self.__width * "#")
            if i + 1 is not self.__height:
                string += "\n"
        return string
