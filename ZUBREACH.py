for t in range(int(input())):
    M, N = map(int, input().split())
    Rx, Ry = map(int, input().split())
    x, y = 0, 0
    n = int(input())
    seq = input()
    for s in seq:
        if s == "U":
            y += 1
        if s == "D":
            y -= 1
        if s == "R":
            x += 1
        if s == "L":
            x -= 1
    if x == Rx and y == Ry:
        print("Case {}: REACHED".format(t+1))
    elif x in range(M) and y in range(N):
        print("Case {}: SOMEWHERE".format(t+1))
    else:
        print("Case {}: DANGER".format(t+1))
