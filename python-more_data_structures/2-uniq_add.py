#!/usr/bin/python3
def uniq_add(my_list=[]):
    number_nrepit = set(my_list)
    result_add = 0
    for i in number_nrepit:
        result_add += i
    return (result_add)
