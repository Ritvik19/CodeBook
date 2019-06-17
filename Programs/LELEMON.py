for t in range(int(input())):
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    V = []
    for i in range(n):
        V.append(list(sorted(list(map(int, input().split()))[1:]))[::-1])
    count = 0
    for i in range(m):
        if len(V[P[i]]) != 0:
            count += V[P[i]][0]
            del(V[P[i]][0])
    print(count)
