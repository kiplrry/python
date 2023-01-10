#!/usr/bin/python3
"""Append to file"""
import json


def save_to_json_file(my_obj, filename):
    """save JSON from an Object to a file
    Args:
        filename: name of the file
        my_obj: object to to written to the file
    """
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
