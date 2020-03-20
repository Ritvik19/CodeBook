#!/bin/python3

import math
import os
import random
import re
import sys


def flippingBits(n):
    # the number is (2**32)-1
    # 2**32 = 4294967296
    # to flip is to just minus 1
    THE_FLIPPING = 4294967295
    # ^ = bitwise XOR
    return n ^ THE_FLIPPING


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
