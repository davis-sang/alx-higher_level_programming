#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of a side of the square

        Return:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the area of the square

        Args:
            None

        Return:
            Area
        """
        return(self.__size ** 2)
