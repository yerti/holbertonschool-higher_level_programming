#!/usr/bin/python3
"""Defines empty class square"""


class Square:
    """Defines class and instantiates private"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Getter that accesses private values"""
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    """Setter to update attribute value"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        result = self.__size * self.__size
        return (result)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for ejeY in range(self.__position[1]):
                print()
            for columns in range(self.__size):
                for ejeX in range(self.__position[0]):
                    print(" ", end="")
                for rows in range(self.__size):
                    print("#", end="")
                print()
                
