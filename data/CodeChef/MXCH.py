for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(range(1, n+1))
    A[k], A[-1] = A[-1], A[k]
    print(*A)