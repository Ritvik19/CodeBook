for t in range(int(input())):
    x = int(input())
    i = (-1 + (4 + 8 * x) ** (0.5)) // 2
    time = min(i + x - (i * (i + 1) // 2), i + (i + 2) * (i + 1) // 2 - x + 1)
    print(int(time))
