#!/usr/bin/python3
""" Class basegeometry"""


class BaseGeometry:
    """class basegeometry"""
    def area(self):
        """method """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ method  that validates value
        Args:
            name: string
            value: value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value < 0:
            raise ValueError(f"{name} must be greater than 0")
