#!/usr/bin/python3
def lookup(obj):
    '''Function that returns a list of available
    attributes and methods of an object'''
    lst = dir(obj)
    lst = [item for item in lst if item != '__init_subclass__']
    return lst
