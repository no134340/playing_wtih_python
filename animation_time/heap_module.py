"""
Module:
    Max heap and min heap implemented using heap types inside one class.
    Adapted for animation of heapsort.
Author:
    Jasmina Savić RA40/2017
Date:
    22.03.2020.
"""

from math import floor
from math import log2
from math import inf


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


class Heap:
    """
        DESCPRIPTION:
            Heap class.
        FILEDS:
            heap - the min/max heap
            sorted - the sorted array (increasing if max heap, decreasing if min heap)
            height - heap height
            length - heap length (used during sorting)
            heap_type - min/max heap. max by defalut.
        NOTE:
            AFTER SORTING, THE SORTED (BY KEY) ARRAY IS PLACED IN A SEPERATE
            CLASS FIELD (self.sorted)
        """

    def __init__(self, heap_type='max'):
        self.heap_type = heap_type
        self.heap = []
        self.sorted = []
        self.height = 0
        self.length = len(self.heap)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def get_height(self):
        return floor(log2(self.length))

    def heapify_sort(self, i):
        # with yielding
        if self.heap_type == 'max':
            l = left(i)
            r = right(i)

            largest = i
            if l <= (self.length - 1) and self.heap[l] > self.heap[i]:
                largest = l
            if r <= (self.length - 1) and self.heap[r] > self.heap[largest]:
                largest = r

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                yield self.heap
                yield from self.heapify_sort(largest)
        else:
            l = left(i)
            r = right(i)

            smallest = i
            if l <= (self.length - 1) and self.heap[l] < self.heap[i]:
                smallest = l
            if r <= (self.length - 1) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                yield self.heap
                yield from self.heapify_sort(smallest)

    def heapify(self, i):
        # for building the heap, without yielding,
        # had to be done separately because yielding
        # causes the heap building to not work properly
        if self.heap_type == 'max':
            l = left(i)
            r = right(i)

            largest = i
            if l <= (self.length - 1) and self.heap[l] > self.heap[i]:
                largest = l
            if r <= (self.length - 1) and self.heap[r] > self.heap[largest]:
                largest = r

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                self.heap
                self.heapify(largest)
        else:
            l = left(i)
            r = right(i)

            smallest = i
            if l <= (self.length - 1) and self.heap[l] < self.heap[i]:
                smallest = l
            if r <= (self.length - 1) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                self.heapify(smallest)

    def build_heap(self, arr):
        self.heap = list(arr)
        self.length = len(self.heap)
        self.height = self.get_height()
        for i in range(self.length // 2, -1, -1):
            self.heapify(i)

    def sort(self):
        length = self.length
        temp = list(self.heap)
        for i in range(length - 1, -1, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            yield self.heap
            self.length -= 1
            yield from self.heapify_sort(0)
            yield self.heap
        self.sorted = self.heap
        self.heap = temp
        self.length = len(self.heap)
        return self.sorted

    def extract_top(self):
        top = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.heap.pop(self.length - 1)
        self.length -= 1
        self.heapify(0)
        return top

    def increase_key(self, i, key):
        if self.heap_type == 'max' and key > self.heap[i]:
            self.heap[i] = key
            while i > 0 and self.heap[i] > self.heap[parent(i)]:
                self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                i = parent(i)
            return i

    def decrease_key(self, i, key):
        if self.heap_type == 'min' and key < self.heap[i]:
            self.heap[i] = key
            while i > 0 and self.heap[i] < self.heap[parent(i)]:
                self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                i = parent(i)
            return i

    def heap_insert(self, key):
        self.length += 1
        if self.heap_type == 'max':
            self.heap.append(-inf)
            ind = self.increase_key(self.length - 1, key)
        else:
            self.heap.append(inf)
            ind = self.decrease_key(self.length - 1, key)
        return ind

    def heap_delete(self, i):
        deleted = self.heap[i]
        if self.heap_type == 'max':
            self.increase_key(i, inf)
        else:
            self.decrease_key(i, -inf)
        self.extract_top()
        return deleted
