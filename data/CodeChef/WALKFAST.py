for t in range(int(input())):
    n, a, b, c, d, p, q, y = map(int, input().split())
    arr = list(map(int, input().split()))
    t1 = abs(arr[a-1] - arr[b-1]) * p
    t2 = (abs(arr[c-1] - arr[a-1]) * p)
    if t2 <= y:
        t2 = y + (abs(arr[d-1] - arr[c-1]) * q)
        t2 = t2 + (abs(arr[d-1] - arr[b-1]) * p)
        print(t2) if t2 < t1 else print(t1)
    else:
        print(t1)