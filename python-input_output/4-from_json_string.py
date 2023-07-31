#!/usr/bin/python3
"""This module has function to from_json_string"""


import json


def from_json_string(my_str):
    """Function that return an object json"""
    return json.loads(my_str)
