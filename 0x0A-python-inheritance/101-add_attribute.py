#!/usr/bin/python3


def add_attribute(obj, name="name", value="default"):
    types = (int, float, str, bool)
    if not isinstance(obj, types):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
