for t in range(int(input())):
    n, k = input().split()
    _ = len(set(list(n)))
    if _ == 3:
        print(27)
    elif _ == 2:
        print(8)
    else:
        print(1)
