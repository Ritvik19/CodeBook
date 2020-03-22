#!/bin/python3

import os
import random
import re
import sys

from math import factorial


def redJohn(n):
    quo = n // 4
    count = 0

    for x in range(quo, -1, -1):
        rem = n - x * 4
        count += (factorial(x + rem)) // (factorial(x) * factorial(rem))

    return count


def sieve(n):
    A = [1] * (n + 1)
    A[0], A[1] = 0, 0

    for i in range(2, n + 1):
        if A[i] == 1:
            A[i * i::i] = [0 for k in A[i * i::i]]

    return [k for k in range(n + 1) if A[k] == 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = len(sieve(redJohn(n)))

        fptr.write(str(result) + '\n')

    fptr.close()
