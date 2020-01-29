#!/bin/python3

import math
import os
import random
import re
import sys

def matrixRotation(matrix, r):
    n = len(matrix)
    m = len(matrix[0])
    a = min(n//2, m//2)
    for i in range(a):
        k = 2*(n-2*i)+2*(m-2*i-2)
        k = r % k
        l = []
        for j in range(i, m-i):
            l.append(matrix[i][j])
        for j in range(i+1, n-i-1):
            l.append(matrix[j][-1-i])
        for j in range(-1-i, -1*m+i-1, -1):
            l.append(matrix[-1-i][j])
        for j in range(-1-i-1, n*-1+i, -1):
            l.append(matrix[j][i])
        l = l[k:]+l[:k]
        flag = 0
        for j in range(i, m-i):
            matrix[i][j] = l[flag]
            flag += 1
        for j in range(i+1, n-i-1):
            matrix[j][-1-i] = l[flag]
            flag += 1
        for j in range(-1-i, -1*m+i-1, -1):
            matrix[-1-i][j] = l[flag]
            flag += 1
        for j in range(-1-i-1, n*-1+i, -1):
            matrix[j][i] = l[flag]
            flag += 1

    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
