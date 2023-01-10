#!/usr/bin/python3
"""dictionary representation of a simple data structure”"""



def class_to_json(obj):
    """returns the dictionary representation of a
    a simple data structure
    """
    return obj.__dict__
