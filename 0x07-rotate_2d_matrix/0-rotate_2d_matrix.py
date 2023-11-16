#!/usr/bin/python3
""" A python script that rotates a
    n x n 2D matrix, 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ A function that rotates a 2D Non-empty matrix in-place"""
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for array in matrix:
        array.reverse()
