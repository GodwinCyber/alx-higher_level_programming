#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return o
    sum_product = 0
    sum_weight = 0

    for score, weight in my_list:
        sum_product += score * weight
        sum_weight += weight

        weight_average = sum_product / sum_weight
    return weight_average
