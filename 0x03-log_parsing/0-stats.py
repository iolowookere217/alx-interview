#!/usr/bin/python3
"""A script for parsing HTTP request logs from stdin"""
import sys

status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]
total_file_size = 0
number_of_lines = 0
status_code_map = {}


def print_stats():
    """handles the printing out of the statistics"""
    print("File Size: {}".format(total_file_size))
    for status, count in sorted(status_code_map.items()):
        print("{}: {}".format(status, count))


try:
    for line in sys.stdin:
        split_line = line.split()
        try:
            file_size = int(split_line[-1])
            total_file_size += file_size
            status_code = int(split_line[-2])
            if status_code in status_code_list:
                if status_code in status_code_map:
                    status_code_map[status_code] += 1
                else:
                    status_code_map[status_code] = 1

        except ValueError:
            pass

        number_of_lines += 1

        if number_of_lines % 10 == 0:
            print_stats()

    if (number_of_lines == 0) or (number_of_lines % 10 != 0):
        print_stats()

except (KeyboardInterrupt):
    print_stats()

