#!/usr/bin/python3
"""function that return true or false"""


def inherits_from(obj, a_class):
    """ conditional of type and instanci that return true"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
