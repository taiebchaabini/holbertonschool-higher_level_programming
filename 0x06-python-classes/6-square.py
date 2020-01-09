#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (all(isinstance(n, int) for n in tuple(value)) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        size = self.size
        return size * size

    def my_print(self):
        size = self.size
        position = self.position
        if (size == 0):
            print("")
        else:
            if (position[1] > 0):
                print("")
            for i in range(size):
                if position[0] == position[1]:
                    print(" " * position[0], end="")
                else:
                    for i in range(position[1], position[0]):
                        print(" ", end="")
                print("#" * size)
