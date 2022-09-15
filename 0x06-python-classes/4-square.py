#!/usr/bin/python3
"""defines class Square"""


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
        self.size = size

    def area(self):
        """calculates the area of the square

        Args:
            None

        Return:
            Area
        """
        return(self.size ** 2)

    @property
    def size(self):
        """getter of __size

        Args:
            None

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size

        Args:
            value(int): the size of the square

        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
