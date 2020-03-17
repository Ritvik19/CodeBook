#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


def checkMagazine(magazine, note):
    magazine = Counter(magazine)
    note = Counter(note)
    min_diff = 0
    try:
        min_diff = min((note-magazine).values())
    except:
        pass
    print('Yes' if min_diff <= 0 else 'No')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
