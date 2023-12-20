#!/usr/bin/python3

import math

class MagicClass:
    """magic class
    this class carries out some calculations
    """

    def __init__(self, radius=0):
    """__init__ method
    initialises instances of a class
    """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
    """area method
    calculates area of a circle
    """
        return self.__radius ** 2 * math.pi

    def circumference(self):
    """circumference method
    calculates circumference of a circle
    """
        return 2 * math.pi * self.__radius
