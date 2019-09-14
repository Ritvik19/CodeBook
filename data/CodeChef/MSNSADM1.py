for t in range(int(input())):
    n = int(input())
    A = list(map(lambda x: int(x)*20, input().split()))
    B = list(map(lambda x: int(x)*10, input().split()))
    C = []
    for i in range(n):
        C.append(max(0, A[i]-B[i]))
    print(max(C))
