#!/usr/bin/python3
"""This module has function to load_from_json_file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        result_obj = json.load(file)
    return result_obj
