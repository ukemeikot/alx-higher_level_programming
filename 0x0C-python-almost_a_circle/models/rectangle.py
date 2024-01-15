#!/usr/bin/python3
""" Subclass module for Base implementing Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Subclass for Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle constructor

            this class has 4 private attribute and 4 public getter and setter
            property.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter property """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter property """
        if isinstance(width, int):
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ Getter property for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter property for height """
        if isinstance(height, int):
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ Getter property for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter property for x """
        if isinstance(x, int):
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ Getter property for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter property for y """
        if isinstance(y, int):
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ calculate rectangle area """
        return self.width * self.height

