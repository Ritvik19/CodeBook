for t in range(int(input())):
    n, minx, maxx = map(int, input().split())
    if minx %2 == 0 and maxx %2 == 0:
        o, e = (maxx-minx+1)//2, ((maxx-minx+1)//2) +1
    elif minx %2 == 0 or maxx %2 == 0:
        o, e = (maxx-minx+1)//2, (maxx-minx+1)//2
    else:
        o, e = (maxx-minx+1)//2 + 1, ((maxx-minx+1)//2)
    for i in range(n):
        w, b = map(int, input().split())
        if w %2 == 0 and b %2 == 0:
            o, e = 0, o+e
        elif w %2 == 0 and b %2 != 0:
            o, e = o+e, 0
        elif w %2 != 0 and b %2 == 0:
            o, e = o, e
        else:
            o, e = e, o
    print(e, o)
