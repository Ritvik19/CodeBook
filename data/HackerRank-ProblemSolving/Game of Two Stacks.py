#!/bin/python3

import os
import sys


def twoStacks(x, a, b):
    m = len(b)
    a = list(reversed(a))
    b = list(reversed(b))
    total = 0
    atmp = []
    for i in range(n):
        val = a.pop()
        if total + val > x:
            break
        total += val
        atmp.append(val)

    max_count = len(atmp)
    cur_count = max_count
    while m:
        if total + b[-1] <= x:
            total += b.pop()
            m -= 1
            cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
            continue
        if not len(atmp):
            break
        aval = atmp.pop()
        total -= aval
        cur_count -= 1
    return max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
