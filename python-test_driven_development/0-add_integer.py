#!/usr/bin/python3
def add_integer(a, b=98):
    '''Adds two integers and returns an int sum'''
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)

    return sum
