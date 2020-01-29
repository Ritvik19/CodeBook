#!/bin/python3

import math
import os
import random
import re
import sys

def squares(a, b):
    return math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
