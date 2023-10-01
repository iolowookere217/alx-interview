#!/usr/bin/python3
'''
this creates a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:
'''


def pascal_triangle(n):
    # declaring empty list
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if (j == 0) or (j == i):
                row.append(1)
            else:
                row.append(triangle[i-1][j] + triangle[i-1][j-1])
        triangle.append(row)
    return triangle
