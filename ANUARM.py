def pos(p, n):
    pstn = [0]*n
    for i in range(p+1,n):
        pstn[i] = pstn[i-1]+1
    for i in range(p-1, -1,-1):
        pstn[i] = pstn[i+1]+1
    return pstn

for t in range(int(input())):
    n, m = map(int, input().split())
    P = list(map(int, input().split()))
    maxpos = pos(P[0], n)
    for i in range(1, m):
        newpos = pos(P[i], n)
        for j in range(n):
            maxpos[j] = max(maxpos[j], newpos[j])
    print(*maxpos)
