#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10000000007


def stepPerms(n):
    dp = [1, 2, 4]
    for i in range(n-3):
        dp.append((dp[-1]+dp[-2]+dp[-3]) % MOD)
    return dp[n-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
