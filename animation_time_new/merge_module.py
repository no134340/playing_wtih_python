"""
Module:
    Merge sort adapted for animation.
Author:
    Jasmina Savić RA40/2017
Date:
    22.03.2020.
"""

import math


def merge(arr, p, q, r):
    left = list(arr[p:r + 1])
    left.append(math.inf)
    right = list(arr[r + 1:q + 1])
    right.append(math.inf)
    lind, rind = 0, 0
    for i in range(p, q + 1):
        if left[lind] > right[rind]:
            arr[i] = right[rind]
            rind += 1
        else:
            arr[i] = left[lind]
            lind += 1
        yield arr


def merge_sort(arr, p, q):
    if p < q:
        div = (q + p) // 2
        yield from merge_sort(arr, p, div)
        yield from merge_sort(arr, div + 1, q)
        yield from merge(arr, p, q, div)


