#!/usr/bin/python3

def validUTF8(data):
    "convertion to binary"
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
