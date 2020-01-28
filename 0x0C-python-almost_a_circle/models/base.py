#!/usr/bin/python3
"""
   This class will be the “base” of all other classes in this project.
   The goal of it is to manage id attribute in all your future classes
   and to avoid duplicating the same code
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
           returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
           writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        l = []
        if list_objs is not None:
            with open(filename, "w") as f:
                for i in list_objs:
                    l.append(i.to_dictionary())
                f.write(cls.to_json_string(l))
