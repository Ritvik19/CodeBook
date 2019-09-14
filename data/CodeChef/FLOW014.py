for i in range(int(input())):
    inp = input().split(" ")
    h = float(inp[0])
    c = float(inp[1])
    t = float(inp[2])
    if h > 50 and c < 0.7 and t > 5600:
        print(10)
    elif h >50 and c < 0.7:
        print(9)
    elif c < 0.7 and t >5600:
        print(8)
    elif h > 50 and t > 5600:
        print(7)
    elif h > 50 or c < 0.7 or t > 5600:
        print(6)
    else:
        print(5)
