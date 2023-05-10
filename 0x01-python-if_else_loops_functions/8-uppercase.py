#!/usr/bin/python3

def uppercase(s):
    """Print a string in uppercase."""
    for c in s:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print(c, end="")
    print()
