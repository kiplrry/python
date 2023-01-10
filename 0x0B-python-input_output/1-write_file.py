#!/usr/bin/python3
"""Write to file"""


def write_file(filename="", text=""):
    """wite to a file
    Args:
        filename: name of the file
        text: text to to written to the file
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        return(myFile.write(text))
