#!/usr/bin/python3
'''Creates a class with a method'''


class MyList(list):
    '''Prints a sorted list'''
    def print_sorted(self):
        ls = self.copy()
        ls.sort()
        print(ls)
        return ls
