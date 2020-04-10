for t in range(int(input())):
    n = input()
    l = []
    for i in range(len(n)):
        l.append(int(n.replace(n[i], '', 1)))
    print(min(l))