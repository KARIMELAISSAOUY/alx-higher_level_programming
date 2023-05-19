#!/usr/bin/python3

def uniq_add(my_list=[]):
    # return [result := result + num for num in new_list][-1]

    new_list = list(set(my_list))
    result = 0

    for num in new_list:
        result += num
    return result
