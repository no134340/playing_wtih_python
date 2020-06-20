"""
    Main program to run the visualization Python script.
"""
import os
import sys

if __name__ == '__main__':
    print(
        'For comparison of 2 algorithms, enter: compare\n' +
        'For single algorithm animation, enter one of the following algorithms: counting, bucket, quick, randomized_quick, heap, merge, bubble, insertion.\n'
        + 'To exit, enter exit.\n')

    while True:
        algo = None
        try:
            sys.stdout.write(">> ")
            algo = input()
            if algo == 'exit':
                break
            if algo not in ['counting', 'bucket', 'quick', 'randomized_quick', 'heap', 'merge', 'bubble',
                            'insertion', 'compare']:
                raise ValueError('Not a valid option!')
        except ValueError as err:
            print(err)
            continue

        algos = []
        if algo == "compare":
            try:
                print("Enter the algorithims:")
                for i in range(2):
                    sys.stdout.write(">> ")
                    inp = input()
                    if inp not in ['counting', 'bucket', 'quick', 'randomized_quick', 'heap', 'merge', 'bubble',
                                    'insertion', 'compare']:
                        raise ValueError('Not a valid option!')
                    else:
                        algos.append(inp)
            except ValueError as err:
                print(err)
                continue
        else:
            algos.append(algo)

        min_elems = 5
        max_elems = 200


        try:
            N = int(input(f'Enter number of elements ({min_elems} <= x <= {max_elems}): '))
            if N > max_elems or N < min_elems:
                raise ValueError(f'Wrong number of elements')
        except ValueError as err:
            print(err)
            continue

        if algo == 'compare':
            os.system(f"./cmp.sh {algos[0]} {N} {algos[1]} {N}")
        else:
            os.system(f"python3 animation.py {algo} {N} 0")
