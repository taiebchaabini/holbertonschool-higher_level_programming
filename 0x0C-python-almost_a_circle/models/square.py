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
        self.width = size
        self.height = size
        super().__init__(self.width, self.height, x, y, id)

    def __str__(self):
        """
           Str output
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)
