"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize Square instance.

        Arguments:
            size (int): length of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description: [Square]<width>/<height>."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
