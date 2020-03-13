#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        print((n - 1 - k) * 2 if (k >= n // 2) else 2 * k + 1)
