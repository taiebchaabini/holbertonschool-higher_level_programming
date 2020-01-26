#!/usr/bin/python3
"""
   This class will be the “base” of all other classes in this project.
   The goal of it is to manage id attribute in all your future classes
   and to avoid duplicating the same code
"""


class Base:
    """
       This class will be the “base” of all other classes in this project.
       The goal of it is to manage id attribute in all your future classes
       and to avoid duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
