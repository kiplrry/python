#!/usr/bin/python3
"""Append to file"""


def append_write(filename="", text=""):
    """wite to a file
    Args:
        filename: name of the file
        text: text to to written to the file
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return(myFile.write(text))
