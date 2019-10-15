import math
import os
import random
import re
import sys

def getMaxLessThanK(n, k):
    maxk = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            temp = i&j
            if temp > maxk and temp < k:
                maxk = temp
    return maxk

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        max_and = 0
        starting_point = n
        i = starting_point
        largest_possible = k - 1
        max_reached = False
        while i > 1:
            j = i - 1
            while j > 0:
                iteration_and = j & i
                if iteration_and > max_and and iteration_and < k:
                    max_and = iteration_and
                    if max_and == largest_possible:
                        max_reached = True
                        break
                j -= 1

            if max_reached:
                break
            i -= 1
        print(max_and)
