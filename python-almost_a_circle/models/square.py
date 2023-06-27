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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''method that updates the attributes of an object'''
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)
     