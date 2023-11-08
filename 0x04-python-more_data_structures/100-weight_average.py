#!/usr/bin/python3
def weight_average(my_list=[]):
    """Average of tuple in a list"""
    if not my_list:
        return 0

    sum = 0
    div = 0
    for tup in my_list:
        sum += (tup[0] * tup[1])
        div += tup[1]
    return (sum / div)
