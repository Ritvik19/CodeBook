#!/bin/python3

import os
import sys


def solve(coordinates):
    on_x = [p for p in coordinates if p[1] == 0]
    on_y = [p for p in coordinates if p[0] == 0]
    max_x = max(on_x)
    min_x = min(on_x)
    max_y = max(on_y)
    min_y = min(on_y)
    dists = []
    dists.append(abs(max_x[0] - min_x[0]))
    dists.append(abs(max_y[1] - min_y[1]))
    dists.append((max_x[0]**2 + max_y[1]**2)**0.5)
    dists.append((min_x[0]**2 + min_y[1]**2)**0.5)
    dists.append((min_x[0]**2 + max_y[1]**2)**0.5)
    dists.append((max_x[0]**2 + min_y[1]**2)**0.5)
    return max(dists)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
