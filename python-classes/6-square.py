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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if i <= 0:
                raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        result = self.__ * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("_")
            for g in range(self.__size):
                for e in range(self.__position[0]):
                    print("_", end="")
                for r in range(self.__size):
                    print("#", end="")
                print()
                
