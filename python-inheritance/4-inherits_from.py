#!/usr/bin/python3
"""function that return true or false"""


def inherits_from(oibj, a_class):
    """ conditional of type and instanci that return true"""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
