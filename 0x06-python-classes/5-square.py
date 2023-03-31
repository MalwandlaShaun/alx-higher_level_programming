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

my_print is class method that prints in stdout 
the square with the character #
'''
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")   
