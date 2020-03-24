"""
Module:
    Bubble sort adapted for animation.
Author:
    Jasmina Savić RA40/2017
Date:
    22.03.2020.
"""


def bubble_sort(A):
    compare = True
    for i in range(len(A) - 1, -1, -1):
        if not compare:
            break
        compare = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                compare = True
            yield A
