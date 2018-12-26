for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A = list(sorted(A))
    print(sum(A[n//2:])-sum(A[:n//2]))
