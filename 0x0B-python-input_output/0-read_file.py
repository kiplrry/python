#!/usr/bin/python3
"""readng a file"""


def read_file(filename=""):
    """func to read file
    Args:
        filename: the filename
    """
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
