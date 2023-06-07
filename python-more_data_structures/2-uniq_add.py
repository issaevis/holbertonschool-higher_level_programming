#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        sum = 0
        for num in sorted(set(my_list)):
            sum = sum + num
        return sum
