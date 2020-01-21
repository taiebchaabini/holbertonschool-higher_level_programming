#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] %d/%d" % (self.__width, self.__height)
