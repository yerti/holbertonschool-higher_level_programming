#!/usr/bin/python3
"""function that return true or false"""


def is_kind_of_class(obj, a_class):
    """Return true/false if obj is a instance a_classs"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
