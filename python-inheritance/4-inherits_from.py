#!/usr/bin/python3
'''Function to check an object'''


def inherits_from(obj, a_class):
    '''Check if obj is instance of a subclass'''
    if isinstance(obj, a_class):
        if obj.__class__ is a_class:
            return False
        return True
    return False
