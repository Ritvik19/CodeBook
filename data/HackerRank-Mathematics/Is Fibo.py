#!/bin/python3

import os
import sys


def solve(n):
    if n in fibs:
        return "IsFibo"
    else:
        return "IsNotFibo"


fibs = [0]
a = 0
b = 1
for i in range(0, 10000):
    c = a+b
    a = b
    b = c
    fibs.append(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
