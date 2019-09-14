for t in range(int(input())):
    n, k = map(int, input().split())
    if k != 0:
        print(n//k, n%k)
    else:
        print(0, n)
