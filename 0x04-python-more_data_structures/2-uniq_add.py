#!/usr/bin/python3
#2-uniq_add.py
def uniq_add(my_list=[]):
     """adds all unique integers in a list (only once for each integer)
    You are not allowed to import any module
    """
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i
    return (num)
