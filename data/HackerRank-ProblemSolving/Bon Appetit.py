import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    b_actual = sum(bill[:k]+bill[k+1:])/2
    if b == b_actual:
        print('Bon Appetit')
    else:
        print(round(b-b_actual))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
