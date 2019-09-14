for i in range(int(input())):
    n, k = input().split()
    n, k = int(n), int(k)
    td = []
    for j in range(n):
        td.append([int(e) for e in input().split()])
    cost = 0
    for t,d in td:
        if t > k:
            t -= k
            k = 0
        else:
            k -= t
            t = 0
        cost += t*d
    print(cost)
