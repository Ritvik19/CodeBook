# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys
for _ in range(int(input())):
    n = int(input())
    arr = map(int,input().split())
    lst = deque(arr)

    curr = 9999999999999999
    flag = 0
    if (len(lst)<=2):
        print("Yes")
        continue
    left = lst.popleft()
    right = lst.pop()
    latest = -1
    while (len(lst)>0):
        flag = 0
        if (left >= right and left <= curr):
            curr = left
            left = lst.popleft()
            latest = left
            flag = 1
        elif (right> left and right <= curr):
            curr = right
            right = lst.pop()
            latest = right
            flag = 1
        if flag == 0:
            break
    if len(lst)>0 or latest > curr:
        print("No")
    else:
        print("Yes")
