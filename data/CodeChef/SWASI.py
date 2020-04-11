for t in range(int(input())):
    string = input()
    count = [0, 0]
    for char in string:
        if char in ["a", "e", "i", "o", "u"]:
            count[0] += 1
        elif char in["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            count[1] += 1
    print(*count)
