#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        st = ''.join(char for char in my_string if char != 'c' and char != 'C')
        return st
