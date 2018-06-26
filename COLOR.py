for i in range(int(input())):
    n = int(input())
    S = input()
    r = g = b = 0
    for color in S:
        if color == "R":
            r += 1
        elif color == "G":
            g += 1
        else:
            b += 1
    print(n-max(r,g,b))
