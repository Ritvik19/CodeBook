for t in range(int(input())):
    n, m = map(int, input().split())
    warriors = {}
    for i in range(n):
        c, l = map(int, input().split())
        if l in warriors.keys():
            warriors[l] += c
        else:
            warriors[l] = c
    for i in range(m):
        c, l = map(int, input().split())
        warriors[l] -= c
    magic = 0
    for v in warriors.values():
        if v < 0 :
            magic -= v
    print(magic)
