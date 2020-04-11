for _ in range(int(input())):
    s, t, i = map(int, input().split())
    if i < s or t < i:
        print(-1)
    elif i == s and i == t:
        print(i, i)
        print(1)
    else:
        count = 0
        while s<t:
            print(s, t)
            count += 1
            mid = (s+t)//2
            if i > mid:
                s = mid+1
            elif i<=mid:
                t = mid
        count += 1
        print(i, i)
        print(count)
