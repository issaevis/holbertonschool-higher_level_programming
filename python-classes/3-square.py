#!/usr/bin/python3
'''module to get the size and print the area of a square'''


class Square:
    def __init__(self, size=0):
        '''initialize the size of the square'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''method to get the area of a square'''
        return self.__size * self.__size
