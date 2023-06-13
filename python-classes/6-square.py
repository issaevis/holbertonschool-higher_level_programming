#!/usr/bin/python3
'''module to get access and update private attribute'''


class Square:
    '''class that gets the attributes for a square'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all(v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''method to get the area of a square'''
        return self.__size * self.__size

    def my_print(self):
        '''method to print a square'''
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                pass

            if self.position[0] > 0:
                for i in range(self.size):
                    for spc in range(self.position[0]):
                        print(" ", end="")
                    for j in range(self.size):
                        print("#", end="")
                    print()
            else:
                for i in range(self.size):
                    for j in range(self.size):
                        print("#", end="")
                    print()
