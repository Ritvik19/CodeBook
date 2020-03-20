#!/bin/python3

import math
import os
import random
import re
import sys


def primality(n):
    if (n <= 1):
        return 'Not prime'
    if (n <= 3):
        return 'Prime'

    if (n % 2 == 0 or n % 3 == 0):
        return 'Not prime'

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return 'Not prime'
        i = i + 6

    return 'Prime'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
