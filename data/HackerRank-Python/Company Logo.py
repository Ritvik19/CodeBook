import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    c = Counter(input())
    i = 0
    for k, v in sorted(sorted(c.items(), key=lambda x: x[0]),key=lambda x: x[1], reverse=True):
        print(k, v)
        i += 1
        if i == 3:
            break
