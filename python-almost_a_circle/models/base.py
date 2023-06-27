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
            return []
        return json.dumps(list_dictionaries)
