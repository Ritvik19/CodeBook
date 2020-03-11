#!/bin/python3

import os
import sys
from itertools import accumulate


def equalStacks(h1, h2, h3):
    acc1 = list(accumulate(reversed(h1)))
    acc2 = list(accumulate(reversed(h2)))
    acc3 = list(accumulate(reversed(h3)))
    height = set(acc1) & set(acc2) & set(acc3)
    height = max(height) if bool(height) else 0

    return height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
