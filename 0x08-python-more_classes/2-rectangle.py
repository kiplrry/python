#!/usr/bin/python3
""" Define a class Rectangle """


class Rectangle:
    """ Represents a Rectangle instance """
    def __init__(self, width=0, height=0):
        """ Initializes a rectangle instance
        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrives the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ sets the Height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrives the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ returns the area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)
