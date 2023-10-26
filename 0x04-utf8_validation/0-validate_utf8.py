#!/usr/bin/python3
"""This module defines a function `validUTF8`"""


def validUTF8(data):
    "convertion to binary and checking validation condition"
    for item in data:
        binary_data = format(item, '08b')
        if binary_data.startswith("0"):
            continue
        elif binary_data.startswith("110"):
            continue
        elif binary_data.startswith("1110"):
            continue
        elif binary_data.startswith("11110"):
            continue
        return False
    return True
