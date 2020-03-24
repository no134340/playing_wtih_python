"""
Module:
    Heap sort adapted for animation.
Autor:
    Jasmina Savić RA40/2017
Datum:
    24.03.2020.
"""


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def build_max_heap(arr, heap_size):
    for i in range(len(arr) // 2, -1, -1):
        yield from max_heapify(arr, i, heap_size)


def max_heapify(arr, i, heap_size):
    l = left(i)
    r = right(i)

    largest = i

    if l <= (heap_size - 1) and arr[l] > arr[i]:
        largest = l
    if r <= (heap_size - 1) and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr
        yield from max_heapify(arr, largest, heap_size)


def heap_sort(arr):
    heap_size = len(arr)
    yield from build_max_heap(arr, heap_size)
    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        yield arr
        heap_size -= 1
        yield from max_heapify(arr, 0, heap_size)
