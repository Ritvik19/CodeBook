import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    neg = pos = zer = 0
    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            zer += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
