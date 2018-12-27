for t in range(int(input())):
    n = int(input())
    train = [list(map(int, input().split())) for i in range(n)]
    time = 0
    time += train[0][0] + train[0][1]
    for i in range(1, n):
        at = train[i][0]
        while at < time:
            at += train[i][2]
        time = at + train[i][1]
    print(time)
