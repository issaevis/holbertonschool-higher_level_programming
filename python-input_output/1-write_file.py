#!/usr/bin/python3
'''module to write to a file'''


def write_file(filename="", text=""):
    '''function that writes to a text file
    and returns the number of chars written to it'''
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
        return len(text)
