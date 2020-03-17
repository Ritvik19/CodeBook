#!/bin/python3

import os
import sys

from math import factorial

p = 10**9+7


def factorial(n):
    result = 1
    while n >= 2:
        result = ((result)*(n % p)) % p
        n -= 1
    return result


def solve(x, y):
    num = factorial(x+y-2)
    denom = factorial(x-1)*factorial(y-1)
    return ((num % p) * (fastEXP(denom, p-2, p))) % p


def fastEXP(base, exp, modulus):
    base %= modulus
    result = 1
    while exp > 0:
        if exp & 1:
            result = (result * base) % modulus
        base = (base*base) % modulus
        exp >>= 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
