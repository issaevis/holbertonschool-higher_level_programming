#!/usr/bin/python3
'''module to create a json'''


import json


def to_json_string(my_obj):
    '''function that make a JSON file out of an object(string)'''
    json_string = json.dumps(my_obj)

    return json_string
