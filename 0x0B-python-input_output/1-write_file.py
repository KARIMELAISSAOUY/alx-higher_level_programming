#!/usr/bin/python3
'''
Module to Write to file
'''


def write_file(filename="", text=""):
    ''' Writes Text to file '''
    with open(filename, 'w') as open_file:
        open_file.write(text)
        count = open_file.tell()
    return count
