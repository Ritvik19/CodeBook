#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):
    def add_digits(string):
        if len(string) == 1:
            return string
        result = sum(int(s) for s in string)
        return add_digits(str(result))

    start = sum(int(s) for s in n) * k
    return add_digits(str(start))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
