#!/usr/bin/python3
"""
    class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       class Square that inherits from Rectangle
       super class with id, x, y, width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """
           Str output
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value
