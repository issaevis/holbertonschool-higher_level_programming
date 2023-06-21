#!/usr/bin/python3
'''module to append to a file'''


def append_write(filename="", text=""):
    '''function that appends to a text file
    and returns the number of chars written to it'''
    with open(filename, "a", encoding='utf-8') as file:
        file.write(text)
        return len(text)
