"""
Module:
    Quicksort module adapted for animation.
    Randomized quicksort and regular quicksort.
Author:
    Jasmina Savić RA40/2017
Date:
    22.03.2020.
"""
import random


def randomized_quicksort(arr, p, r):
    if p < r:
        k = random.randint(p, r)
        arr[k], arr[r] = arr[r], arr[k]
        yield arr
        pivot = arr[r]
        i = p - 1
        for j in range(p, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr

        i += 1
        arr[i], arr[r] = arr[r], arr[i]
        yield arr
        q = i
        yield from randomized_quicksort(arr, p, q - 1)
        yield from randomized_quicksort(arr, q + 1, r)


def quicksort(arr, p, r):
    if p < r:
        pivot = arr[r]
        i = p - 1
        for j in range(p, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr

        i += 1
        arr[i], arr[r] = arr[r], arr[i]
        yield arr
        q = i
        yield from quicksort(arr, p, q - 1)
        yield from quicksort(arr, q + 1, r)
