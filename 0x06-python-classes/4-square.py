#!/usr/bin/python3

"""Define a class Square."""


class Square:
'''
Square is class definition for creating objects

__init__ is the constructor and size is the parameter

@property is acting as our getter

@size.setter is acting as our setter

area is class method that returns an integer value
of the area 
'''
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
