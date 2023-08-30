#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __str__(self):
        """Print the square a custom way."""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square instance.

        Args:
            size: a side of square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of the coordinates of this Square.

        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this Square.

        Args: value as a tuple of two positive integers.
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate area of the square.

        Returns: The square of the size
        """
        return (self.__size ** 2)

    def pos_print(self):
        """Return the position in spaces."""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square in position."""
        print(self.pos_print(), end='')
