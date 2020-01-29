#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(scores, alice):
    unique_scores = list(reversed(sorted(set(scores))))

    i = len(alice)-1
    j = 0
    ans = []

    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= alice[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1

    return reversed(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
