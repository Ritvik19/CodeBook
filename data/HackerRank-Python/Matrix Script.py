#!/bin/python3

import math
import os
import random
import re
import sys

n, m = map(int, input().rstrip().split())
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
print(re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])',' ',"".join("".join(decode) for decode in zip(*matrix))))
