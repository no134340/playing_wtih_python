"""
Module:
    Insertion sort adapted for animation.
Author:
    Jasmina Savić RA40/2017
Date:
    22.03.2020.
"""


def insertion(A):
    for i in range(1, len(A)):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            yield A
        A[j + 1] = key
        yield A
