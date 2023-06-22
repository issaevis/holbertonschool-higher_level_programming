#!/usr/bin/python3
'''returns '''


def class_to_json(obj):
    d = dict()

    for attr, value in obj.__dict__.items():
        d[attr] = value
    return d
