#!/bin/python3

import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = sum([c*2**i for i, c in enumerate(calorie)])
    return miles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
