#!/usr/bin/python3
"""
    function that returns the dictionary description with simple data
"""
import json


def class_to_json(obj):
    """
        function that returns the dictionary description with simple data
    """
    return dict(obj.__dict__)
