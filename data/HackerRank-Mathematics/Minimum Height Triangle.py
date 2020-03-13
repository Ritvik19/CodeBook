#!/bin/python3

import sys
from math import ceil


def lowestTriangle(base, area):
    return ceil(2*area/base)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
