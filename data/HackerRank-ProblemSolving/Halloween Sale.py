#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if s < p:
        return 0
    total = p
    count = 1
    lastprice = p
    while True:
        newprice = lastprice-d if lastprice-d > m else m
        if newprice+total <= s:
            total += newprice
            lastprice = newprice
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
