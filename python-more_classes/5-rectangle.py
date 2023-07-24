#!/usr/bin/python3
"""Defines empty class Rectangle"""


class Rectangle:
    """Defines class and instanties private"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Getter that accesses private values"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width and self.__height != 0:
            return self.__width + self.__height + self.__width + self.__height
        else:
            return 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += "#"
                if i < self.__height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
