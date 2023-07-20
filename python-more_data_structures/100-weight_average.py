#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    t_score = 0
    t_weight = 0
    for key, value in my_list:
        t_score += key * value
        t_weight += value
    result_prom = t_score / t_weight
    return result_prom
