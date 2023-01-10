#!/usr/bin/python3
"""return json"""
import json


def to_json_string(my_obj):
    """function to return JSON from python
    Args:
        my_obj: object
    """
    return (json.dumps(my_obj))
