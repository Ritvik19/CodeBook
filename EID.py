for t in range(int(input())):
    N = int(input())
    V = list(map(int, input().split()))
    V = list(sorted(V))
    differences = []
    for i in range(N-1):
        differences.append(V[i+1]-V[i])
    print(min(differences))
