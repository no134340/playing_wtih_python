"""
Module:
    Bucket sort (with integers) adapted for animation.
Autor:
    Jasmina Savić RA40/2017
Datum:
    24.03.2020.
"""


def insertion_sort(t):
    for i in range(1, len(t)):
        j = i - 1
        key = t[i]
        while j >= 0 and t[j] > key:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = key


def bucket_sort(arr):
    k = max(arr)
    n = len(arr)
    temp = [[] for x in range(n + 1)]
    for i in range(n):
        temp[((arr[i] * n) // k)].append(arr[i])
    arr.clear()
    for t in temp:
        insertion_sort(t)
        for val in t:
            arr.append(val)
            yield arr
