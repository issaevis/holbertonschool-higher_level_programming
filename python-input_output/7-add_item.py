#!/usr/bin/python3
'''module to create a JSON file'''


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
if __name__ == "__main__":

    my_list = []
    i = 1

    while i < len(sys.argv):
        my_list.append(sys.argv[i])
        i += 1

    with open("add_item.json", "w", encoding='utf-8') as file:
        file.write(str(my_list))
