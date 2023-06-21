#!/usr/bin/python3
'''module to read a file'''


def read_file(filename=""):
    '''reads a file and prints it'''
    with open(filename, 'r') as file:
        print(file.read())
