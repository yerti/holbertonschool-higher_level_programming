#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_ord = sorted(a_dictionary)
    for clave in keys_ord:
        value = a_dictionary[clave]
        print(f"{clave}: {value}")
