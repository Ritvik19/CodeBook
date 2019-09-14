for t in range(int(input())):
    r, c, k = map(int, input().split())
    lr = max(r-k, 1)
    lc = max(c-k, 1)
    ur = min(r+k, 8)
    uc = min(c+k, 8)
    sq = (ur-lr+1)*(uc-lc+1)
    print(sq)
