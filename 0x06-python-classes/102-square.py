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
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """Compare if square is less than another by area

        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size > other.size
