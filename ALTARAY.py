for t in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    op = [1]*n
    for i in range(n-1, 0, -1):
        if A[i]*A[i-1] < 0:
            op[i-1] = op[i]+1
    print(*op)
