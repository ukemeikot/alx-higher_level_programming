#!/usr/bin/python3

"""This is the Base Model"""


class Base:
    """Base class from which all other classes are derived from"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the class constructor for the base class

            its the with R/W capabilities.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id
