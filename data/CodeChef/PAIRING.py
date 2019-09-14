for t in range(int(input())):
    n, m= map(int, input().split())
    pairs = []
    status = [0]*n
    selected = []
    for i in range(m):
        pairs.append(list(map(int, input().split())))
    i = m-1
    while 0 in status and i >= 0:
        # print(status[pairs[i][0]], status[pairs[i][1]])
        if status[pairs[i][0]] == 0 and status[pairs[i][1]] == 0:
            selected = [i] + selected[:]
            status[pairs[i][0]] = 1
            status[pairs[i][1]] = 1
            # print(selected)
            # print(status)
        i -= 1
    print(*selected)
