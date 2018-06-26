for i in range(int(input())):
    string = input()
    a = b = 0
    for balloon in string:
        if balloon == 'a':
            a += 1
        else:
            b += 1
    print(min(a, b))
