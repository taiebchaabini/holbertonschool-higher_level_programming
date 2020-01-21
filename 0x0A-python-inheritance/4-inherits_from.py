#!/usr/bin/python3


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
