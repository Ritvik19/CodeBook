#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.


def minimumNumber(n, password):
    required = 0
    numbers = re.compile(r"[0-9]")
    lower_case = re.compile(r"[a-z]")
    upper_case = re.compile(r"[A-Z]")
    special_characters = re.compile(r"!|@|#|\$|%|\^|&|\*|\(|\)|-|\+")
    if len(numbers.findall(password)) == 0:
        required += 1
    if len(lower_case.findall(password)) == 0:
        required += 1
    if len(upper_case.findall(password)) == 0:
        required += 1
    if len(special_characters.findall(password)) == 0:
        required += 1
    return max(6-n, required) if required + n < 6 else required


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
