for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))
    survivors = []
    for i in range(n):
        if A[(i-1)%n] + A[(i+1)%n] < D[i]:
            survivors.append(D[i])
    print(max(survivors)) if len(survivors) != 0 else print(-1)
