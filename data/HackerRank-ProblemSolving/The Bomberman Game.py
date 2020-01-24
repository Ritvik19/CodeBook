#!/bin/python3

import math
import os
import random
import re
import sys


def detonation(grid, n_r, n_c):   # it returns grid as a list of lists
        grid = [['O' if x == '.' else '.' for x in row] for row in grid]
        for i, row in enumerate(grid):
                for j, element in enumerate(row):
                        if element == '.':
                                if i > 0:
                                        grid[i-1][j] = '.'
                                if j > 0:
                                        grid[i][j-1] = '.'
                                if j < n_c-1 and grid[i][j+1] != '.':
                                        grid[i][j+1] = '1'
                                if i < n_r-1 and grid[i+1][j] != '.':
                                        grid[i+1][j] = '1'
                        if element == '1':
                                grid[i][j] = '.'
        return grid


def bomberMan(n, grid):
        n_r = len(grid)
        n_c = len(grid[0])
        if n == 1:
                return grid
        elif n % 2 == 0:
                return ['O'*n_c]*n_r
        elif n % 4 == 3:
                return [''.join(row) for row in detonation(grid, n_r, n_c)]
        elif n % 4 == 1:
                return [''.join(row) for row in detonation(detonation(grid, n_r, n_c), n_r, n_c)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
