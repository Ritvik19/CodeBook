for t  in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    m = min(A)
    M = max(A)
    if A.index(m) < A.index(M):
        print(m, M)
    else:
        print(M, m)