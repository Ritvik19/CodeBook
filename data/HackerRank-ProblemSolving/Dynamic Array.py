#!/bin/python3

import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    for t, x, y in queries:
        if t == 1:
            seq[(x ^ lastAnswer) % n].append(y)
        else:
            lastAnswer = seq[(x ^ lastAnswer) %
                            n][y % len(seq[(x ^ lastAnswer) % n])]
            result.append(lastAnswer)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
