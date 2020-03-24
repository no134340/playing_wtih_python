"""
Module:
    Counting sort adapted for animation.
Autor:
    Jasmina Savić RA40/2017
Datum:
    24.03.2020.
"""


def counting_sort(arr, ret, k):
    temp = [0 for i in range(k + 1)]
    for val in arr:
        temp[val] += 1
    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        ret[temp[arr[i]] - 1] = arr[i]
        temp[arr[i]] -= 1
        yield ret
