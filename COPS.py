for i in range(int(input())):
    H = []
    for j in range(100):
        H.append(1)
    M, x, y = input().split()
    M, x, y = int(M), int(x), int(y)
    cops = [int(e) for e in input().split()]

    for c in cops:
        for j in range(max(0, c-x*y-1), min(100, c+x*y)):
            H[j] = 0
    safe = 0
    for h in H:
        safe += h

    print(safe)
