#!/bin/python3

import os
import sys


def halloweenParty(k):
    n = k//2
    m = k-n
    return m*n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        k = int(input())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()
