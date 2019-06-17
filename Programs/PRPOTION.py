for t in range(int(input())):
    Nr, Ng, Nb, M = map(int, input().split())
    R = list(map(int, input().split()))
    G = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(M):
        Mr, Mg, Mb = max(R), max(G), max(B)
        if Mr >= Mg and Mr >= Mb:
            R = list(map(lambda x: x//2, R))
        elif Mg >= Mb:
            G = list(map(lambda x: x//2, G))
        else:
            B = list(map(lambda x: x//2, B))
    Mr, Mg, Mb = max(R), max(G), max(B)
    print(max(Mr, Mg, Mb))
