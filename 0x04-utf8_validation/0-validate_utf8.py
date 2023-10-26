#!/usr/bin/python3
""" Defines a method to check UTF8 Valid integers """


def validUTF8(data):
    """ Checks UTF8 Valid data set """
    no_bytes_rem = 0
    for byt in data:
        bin_char = format(byt, '08b')
        if no_bytes_rem == 0:
            if bin_char.startswith('0'):
                continue
            elif bin_char.startswith('110'):
                no_bytes_rem = 1
            elif bin_char.startswith('1110'):
                no_bytes_rem = 2
            elif bin_char.startswith('11110'):
                no_bytes_rem = 3
            else:
                return False
        else:
            if bin_char.startswith('10'):
                no_bytes_rem -= 1
                continue
            return False
    return True
