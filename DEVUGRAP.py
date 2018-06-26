for i in range(int(input())):
    n, k = input().split()
    n, k = int(n), int(k)
    grapes = [int(e) for e in input().split()]
    op = 0
    for g in grapes:
        if g<k:
            op+=(k-g)
        else:
            op+=min(g%k,k-(g%k))
    print(op)
