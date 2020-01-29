#!/bin/python3

import math
import os
import random
import re
import sys

def add(p1, p2):
    return sum((i or j) for i, j in zip(p1, p2))


def acmTeam(topic):
    scores = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            scores.append(add(topic[i], topic[j]))
    highest = max(scores)
    return highest, scores.count(highest)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = [int(_) for _ in list(input())]
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
