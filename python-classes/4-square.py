#!/usr/bin/python3
"""Defines empty class square"""


class Square:
    """Defines class and instantiates private"""
    def __init__(self, size=0):
        self.__size = size

    """getter that accesses private values"""
    @property
    def size(self):
        return self.__size

    """setter to update attribute value"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return of area of square"""
        result = self.__size * self.__size
        return (result)
