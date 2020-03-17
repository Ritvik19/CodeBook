#!/bin/python3

import os
import sys

counts = [0]*100


def solve(dates):
    for _ in dates:
        m, d = _
        try:
            counts[int(str(d), m)] += 1
        except:
            pass
    return sum(c*(c-1)//2 for c in counts)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()
