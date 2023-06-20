#!/usr/bin/python3
'''Creates a class with a method'''


class MyList(list):
    
    def print_sorted(self):
        '''method to print the list in ascending order'''
        list = self.copy()
        list.sort()
        print(list)
