for t in range(int(input())):
    n, c, q = map(int, input().split())
    b = c
    for i in range(q):
        l, r = map(int, input().split())
        if l <= b <= r:
            b = l + r - b
    print(b)
