#!/bin/python3

import os
import sys

def solve(a):
    L = sum(a)
    R = 0
    ret = []
    for i in a[::-1]:
        if L == 0:
            break
        if R % L == 0:
            """ 
            L is a potential candidate, 
            check if suitable
            """
            b = 0
            for j in a:
                b += j
                if b == L:
                    b = 0
                elif b > L:
                    break
            if b == 0:
                ret.insert(0, L)
        L -= i
        R += i
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
