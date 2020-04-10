for t in range(int(input())):
    s, w1, w2, w3 = map(int, input().split())
    if s >= w1 + w2 + w3:
        print(1)
    elif s >= w1 + w2 or s >= w2 + w3:
        print(2)
    else:
        print(3)