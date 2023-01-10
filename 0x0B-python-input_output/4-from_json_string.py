#!/usr/bin/python3
"""return python object from JSON"""
import json


def from_json_string(my_str):
    """function to return Python object from JSON
    Args:
        my_str: object
    """
    return (json.loads(my_str))
