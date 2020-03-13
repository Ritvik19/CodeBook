#!/bin/python3

import math
import os
import random
import re
import sys


def sumOfDigits(n):
    return sum([int(i) for i in list(str(n))])


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    print(max(a, key=sumOfDigits))
