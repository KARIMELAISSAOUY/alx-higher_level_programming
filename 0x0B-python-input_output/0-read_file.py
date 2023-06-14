#!/usr/bin/python3
'''
Module to Read and print contents of a File
'''


def read_file(filename=""):
    ''' Reads File and prints contents '''
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")