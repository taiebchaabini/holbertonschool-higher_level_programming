#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        self.__type = "Rectangle"

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[%s] %d/%d" % (self.__type, self.__width, self.__height)
