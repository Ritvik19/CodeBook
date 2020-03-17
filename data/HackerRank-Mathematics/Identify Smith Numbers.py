#!/bin/python3

import os
import sys


def factorize(n):
    array = []
    while not n % 2:
        n //= 2
        array.append(2)
    i = 3
    while n >= i**2:
        if not n % i:
            array.append(i)
            n //= i
        else:
            i += 2
    array.append(n)
    return array


def digsum(n):
    array = list(str(n))
    return sum(map(int, array))


def solve(n):
    return int(digsum(n) == sum(map(digsum, factorize(n)))) if n != 1 else 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
