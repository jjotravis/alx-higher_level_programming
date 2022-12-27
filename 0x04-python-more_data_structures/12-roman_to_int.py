#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    """Define major roman values"""
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    """Create list with int values"""
    int_list = []
    for i in range(len(roman_string)):
        if i > 0 and values[roman_string[i]] > values[roman_string[i - 1]]:
            to_list = values[roman_string[i]] - 2 * values[roman_string[i - 1]]
            int_list.append(to_list)
        else:
            int_list.append(values[roman_string[i]])
    """Use reduce to get value"""
    return (reduce(lambda a, b: a + b, int_list))
