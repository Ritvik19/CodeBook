for t in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        if a%m == 0:
            count += 1
    print((2**count)-1)
