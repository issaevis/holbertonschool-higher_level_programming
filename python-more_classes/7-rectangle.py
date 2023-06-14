#!/usr/bin/python3
'''module that creates an empty class called rectangle'''


class Rectangle:
    '''the rectangle class'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height)+(2 * self.__width)

    def area(self):
        '''returns the area of the rectangle'''
        return (self.__width * self.__height)

    def __str__(self):
        '''Returns a string'''
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "{}".format(self.print_symbol)
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        '''returns a representation of the string'''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        '''Detects if an instance is deleted and prints a message'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
