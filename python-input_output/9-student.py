#!/usr/bin/python3
"""create a student class"""


class Student:
    """we define the attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if hasattr(self, '__dict__'):
            obj_dict = self.__dict__.copy()
            json_dict = {}

            for at_key, at_vl in obj_dict.items():
                if isinstance(at_vl, (list, dict, str, int, bool)):
                    json_dict[at_key] = at_vl
            return json_dict
