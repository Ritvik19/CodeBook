#!/bin/python3

import os
import sys

# Complete the solve function below.


def solve(n):
    i = 1
    while True:
        j = int(bin(i)[2:].replace('1', '9'))
        if j % n == 0:
            break
        i += 1
    return str(j)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
