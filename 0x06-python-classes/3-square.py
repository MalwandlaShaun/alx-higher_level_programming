#!/usr/bin/python3

class Square:
    '''
    Square is class definition for creating objects
    
    __init__ is the constructor and size is it's parameter
    
    area is the class method which evaluates the area expression
    and return an integer value
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
