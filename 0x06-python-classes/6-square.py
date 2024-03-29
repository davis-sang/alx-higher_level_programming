#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square

        Args:
            size (int): size of a side of the square
            position (tuple): coordinates of the square in space

        Return:
            None
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """prints the square

        Args:
            None

        Returns:
            None
        """
        if self.size == 0:
            print()
            return
        for a in range(self.position[1]):
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end='')
            for k in range(self.size):
                print('#', end='')
            print()

    @property
    def position(self):
        """getter of __position

        Args:
            None

        Return:
            The position/coordinates  of the square in 2D
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position

        Args:
            value(int): Tuple of 2 positive integers

        Return:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
