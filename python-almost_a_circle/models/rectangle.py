#!/usr/bin/python3
'''Module to create a class that inherits'''


from models.base import Base


class Rectangle(Base):
    '''Class that defines a Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''get the area of the rectangle'''
        return (self.width * self.height)

    def display(self):
        '''prints a square with '#' '''

        if self.__y is not None:
            for num in range(self.__y):
                print()

        for i in range(self.__height):
            if self.__x is not None:
                for num in range(self.__x):
                    print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        s = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        s += " - {}/{}".format(self.__width, self.__height)
        return s
