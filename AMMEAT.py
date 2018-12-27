for t in range(int(input())):
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    P = list(reversed(sorted(P)))
    i = sum = 0
    while sum < m and i < n:
        sum += P[i]
        i += 1
    if sum >= m:
        print(i)
    else:
        print(-1)
