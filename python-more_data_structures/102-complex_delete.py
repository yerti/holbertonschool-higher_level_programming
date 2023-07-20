#!/usr/bin/python3
def complex_delete(a_dictionary, value):
      for value in a_dictionary.values():
        for i, n in a_dictionary.items():
            if n == value:
                del a_dictionary[i]
                break
        return a_dictionary
