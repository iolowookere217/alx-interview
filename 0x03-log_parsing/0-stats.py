#!/usr/bin/python3
"""A script for parsing HTTP request logs from stdin
"""

import sys

status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]
total_file_size = 0
number_of_lines = 0
status_code_map = {}


def print_stats():
     """handles the printing out of the statistics"""
    print(f"File Size: {total_file_size}")
    for status, count in sorted(status_code_map.items()):
        print(f"{status}: {count}")


try:
    for line in sys.stdin:
        try:
            line = line.split()
            fileSize = int(line[-1])
            total_file_size += fileSize
            statusCode = int(line[-2])

            if statusCode in status_code_list:
                if statusCode in status_code_map:
                    status_code_map[statusCode] += 1
                else:
                    status_code_map[statusCode] = 1

                number_of_lines += 1

                if (number_of_lines % 10) == 0:
                    print_stats()

        except ValueError:
            pass

    if (number_of_lines == 0) or (number_of_line % 10 != 0):
        print_stats()

except KeyboardInterrupt:
    print_stats()
