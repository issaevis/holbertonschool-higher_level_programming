#!/usr/bin/python3
'''module to convert a json'''


import json


def from_json_string(my_str):
    '''function that converts a JSON file to an object'''
    return json.loads(my_str)
