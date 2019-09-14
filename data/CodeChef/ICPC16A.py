for i in range(int(input())):
    inp = input().split(" ")
    x1 = int(inp[0])
    y1 = int(inp[1])
    x2 = int(inp[2])
    y2 = int(inp[3])

    if x1 == x2:
        if y1 > y2:
            print("down")
        elif y1 < y2:
            print("up")
    elif y1 == y2:
        if x1 > x2:
            print("left")
        elif x1 < x2:
            print("right")
    else:
        print("sad")
