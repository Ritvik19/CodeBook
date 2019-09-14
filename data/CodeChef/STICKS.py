for i in range(int(input())):
    n = int(input())
    sticks = [int(e) for e in input().split()]
    sticks = sorted(sticks)[::-1]
    i = 0
    a = b = 0
    while i < n-1:
        if sticks[i] == sticks[i+1] and a == 0:
            a = sticks[i]
            i += 1
        elif sticks[i] == sticks[i+1] and a != 0 and b == 0:
            b = sticks[i]
            i += 1
        i += 1
    area = a*b
    if area > 0:
        print(area)
    else:
        print(-1)
