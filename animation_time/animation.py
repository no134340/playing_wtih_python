"""
Description:
    Animation of sorting algorithms using matplotlib.animation.
    Will be updated as more algorithms are implemented.
Based on:
    https://github.com/nrsyed/sorts
"""

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bubble_sort import bubble_sort
from insertion import insertion
from merge_module import merge_sort
from quicksort_module import randomized_quicksort, quicksort
from heap_sort import heap_sort
from bucket_sort import bucket_sort
from counting_sort import counting_sort


def update_figure(A, bars, iterations):
    for bar, val in zip(bars, A):
        bar.set_height(val)
    iterations[0] += 1
    text.set_text(f'# of operations: {iterations[0]}')


max_elems = 200

try:
    N = int(input(f'Enter number of elements (0 < x < {max_elems}):'))
    if N > max_elems or N < 1:
        raise ValueError(f'I said a number between 0 and {max_elems}!')
except ValueError as err:
    print(err)
    exit()

A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)

print(
    'Enter one of the following algorithms: counting, bucket, quick, randomized_quick, heap, merge, bubble, insertion:')
algo = input()

fig, ax = plt.subplots()
plt.xlabel('Index')
plt.ylabel('Value')

bars = None
generator = None
B = [0 for x in range(N)]

if algo == 'quick':
    generator = quicksort(A, 0, len(A) - 1)
    bars = ax.bar(range(len(A)), A, align='edge', color='red')
elif algo == 'randomized_quick':
    generator = randomized_quicksort(A, 0, len(A) - 1)
    bars = ax.bar(range(len(A)), A, align='edge', color='orange')
elif algo == 'merge':
    generator = merge_sort(A, 0, len(A) - 1)
    bars = ax.bar(range(len(A)), A, align='edge', color='magenta')
elif algo == 'heap':
    generator = heap_sort(A)
    bars = ax.bar(range(len(A)), A, align='edge', color='yellow')
elif algo == 'bubble':
    generator = bubble_sort(A)
    bars = ax.bar(range(len(A)), A, align='edge', color='cyan')
elif algo == 'insertion':
    generator = insertion(A)
    bars = ax.bar(range(len(A)), A, align='edge', color='black')
elif algo == 'bucket':
    generator = bucket_sort(A)
    bars = ax.bar(range(len(A)), A, align='edge', color='brown')
elif algo == 'counting':
    generator = counting_sort(A, B, N + 1)
    bars = ax.bar(range(len(B)), B, align='edge', color='grey')
else:
    print('Not a valid algorithm!')
    exit()

title = algo.replace('_', ' ').title()
ax.set_title(f'{title} sort')
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.07 * N))

iterations = [0]
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

animate = animation.FuncAnimation(fig, func=update_figure, fargs=(bars, iterations), frames=generator, interval=1,
                                  repeat=False)

plt.show()
