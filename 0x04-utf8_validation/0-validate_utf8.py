#!/usr/bin/python3
"""This module defines a function validUTF8

        UTF8 Format:

        1-byte Sequence: 0xxxxxxx;
        2-byte Sequence: 110xxxxx 10xxxxxx;
        3-byte Sequence: 1110xxxx 10xxxxxx 10xxxxxx;
        4-byte Sequence: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx;
    """


def validUTF8(data):
    byts_remaining = 0
    for item in data:
        binary_char = format(item, '08b')
        if byts_remaining == 0:
            if binary_char.startswith("0"):
                continue
            elif binary_char.startswith("110"):
                byts_remaining = 1
            elif binary_char.startswith("1110"):
                byts_remaining = 2
            elif binary_char.startswith("11110"):
                byts_remaining = 3
            else:
                return False
        else:
            if binary_char.startswith("10"):
                byts_remaining -= 1
                continue
            return False
    return True
