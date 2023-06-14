#!/usr/bin/python3
'''
Module that works with JSON
'''

import json


def from_json_string(my_str):
    ''' Return an object from JSON string '''
    return json.loads(my_str)
