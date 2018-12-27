for t in range(int(input())):
    n = int(input())
    G = list(map(int, input().split()))
    min =G[0]
    dif = 0
    for i in range(n):
        if G[i] < min:
            min = G[i]
        elif G[i] > min and dif < G[i]-min:
            dif = G[i]-min
    if dif:
        print(dif)
    else:
        print("UNFIT")
