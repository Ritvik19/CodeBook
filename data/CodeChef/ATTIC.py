for t in range(int(input())):
    attic = input()
    P = []
    l = 0
    for a in attic:
        if a == ".":
            l += 1
        else:
            if l != 0:
                P.append(l)
            l = 0
    count = 0
    max = 0
    for p in P:
        if p>max:
            max = p
            count += 1
    print(count)
