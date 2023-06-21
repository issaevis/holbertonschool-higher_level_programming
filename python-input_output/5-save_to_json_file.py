#!/usr/bin/python3
'''module to create a JSON file'''


import json


def save_to_json_file(my_obj, filename):
    '''save my object as a JSON file in the current directory'''
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
