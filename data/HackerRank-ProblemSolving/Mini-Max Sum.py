import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    arr = list(sorted(arr))
    print(sum(arr[:4]), sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
