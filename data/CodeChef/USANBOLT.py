for t in range(int(input())):
    s, d, a, u = map(int, input().split())
    tt = (2*(s+d)/a)**0.5
    tb = (s/u)
    print("Bolt") if tb < tt else print("Tiger")