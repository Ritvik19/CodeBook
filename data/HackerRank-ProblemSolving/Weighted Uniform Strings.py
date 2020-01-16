#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.


def alpha(c):
    return ord(c) - 96


def weightedUniformStrings(s, queries):
    scores = set()
    ctr = 1
    for i in range(len(s)):
        score = alpha(s[i])
        ctr = ctr+1 if (i+1 != len(s) and s[i+1] == s[i]) else 1
        scores.add(score*ctr)

    results = []
    for q in queries:
        results.append("Yes" if q in scores else "No")

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
