#!/usr/bin/python3
'''Module that creates a class the inherits from rectangle'''


class BaseGeometry:
    '''Class with a function'''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''Class for creating rectangles'''
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''gives the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''configures __str__'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    '''Class that defines a square'''
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)