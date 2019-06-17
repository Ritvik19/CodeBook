for t in range(int(input())):
    s, sg, fg, d, t = map(int, input().split())
    cs = s + (180*d/t) #correct speed
    fc = abs(cs-fg)
    sc = abs(cs-sg)
    if fc < sc:
        print("FATHER")
    elif sc < fc:
        print("SEBI")
    else:
        print("DRAW")
