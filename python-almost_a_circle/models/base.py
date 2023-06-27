#!/usr/bin/python3
'''Module to create a class'''


import json


class Base:
    '''Class that defines a Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Convert list of dictionaries into json string"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''method that writes the JSON into a file'''
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding="utf-8") as file:
            if not list_objs:
                file.write('[]')
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(json_list))
