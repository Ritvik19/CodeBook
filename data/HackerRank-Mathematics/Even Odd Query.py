#!/bin/python3

import os
import sys


def solve(arr, queries):
    answers = []
    for x, y in queries:
        num = 1 if x < len(arr) and arr[x] == 0 and x != y else arr[x - 1]
        answers.append("Odd" if num % 2 else "Even")
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
