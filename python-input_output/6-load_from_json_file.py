#!/usr/bin/python3
'''module to create an object from a JSON file'''


import json


def load_from_json_file(filename):
    '''create an object form a JSON file'''
    with open(filename, 'r', encoding="utf-8") as file:
        file.read(json.loads(filename))
