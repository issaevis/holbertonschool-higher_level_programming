#!/usr/bin/python3
'''Module to create a class Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class using Rectangle as inheritance'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        s += " - {}".format(self.width)
        return s
