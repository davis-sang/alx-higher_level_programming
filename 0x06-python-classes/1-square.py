#!/usr/bin/python3
"""Square class Definition"""


class Square:
    """Represents a Square

    Attributes:
    __size(int): size of a side of the square
    """
    def __init__(self, size):
        """Initilizes a square

        Args:
            size(int): size of a side of the square

        Returns: None
        """
        self.__size = size
