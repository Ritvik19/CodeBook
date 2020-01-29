#!/bin/python3

import math
import os
import random
import re
import sys

def stones(n, a, b):
    n = n - 1
    min_ = min(a, b)
    max_ = max(a, b)
    result = [min_ * n]
    maxi = max_ * n
    diff = max_ - min_

    while result[- 1] < maxi:
        result.append(result[- 1] + diff)

    return result;
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
