#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def class_to_json(obj):
    """returns the dictionary representation of a
    a simple data structure
    """
    return obj.__dict__
