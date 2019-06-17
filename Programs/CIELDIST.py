for t in range(int(input())):
    ds, dt, d = map(int, input().split())
    if d < ds+dt or d < dt or d < ds:
        print(0)
    else:
        print(d-dt-ds)
