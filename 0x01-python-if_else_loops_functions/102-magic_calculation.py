#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        if c > a:
            return c - b
        else:
            return (a * b) - c
    return (a + b) * c
