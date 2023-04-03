#!/bin/usr/python3

class Square:
    '''
    Square is class definition for creating objects

    __init__ is the constructor with size as the parameter

    __size is the private attribute
    '''

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
