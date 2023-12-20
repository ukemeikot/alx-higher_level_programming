#!/usr/bin/python3

"""Square module: this class <sqaure> models a square object"""


class Square:
    """Square class
     this class implements a square class with setters and getters



    """
    def __init__(self, size=0):
        """ __init__ method


        this method is a special method that acts as an instance
        constructor after initialization.


        Args:
            size (int): <size> is a private attribute of an integer.


        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area method


        this method returns the area of the square

        Args:
            None


        """

    @property
    def size(self):
        """Getter method"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) is not int:
            TypeError("size must be an integer")
