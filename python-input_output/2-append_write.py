#!/usr/bin/python3
"""Function that writes a string to a text file"""


def append_write(filename="", text=""):
    """Writin permissions and number of character in the text"""
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
