for t in range(int(input())):
    l, r = map(int, input().split())
    d = r-l+1
    if d %4 == 0:
        result = 'Even'
    elif d %4 == 1:
        if l %2 == 0:
            result = 'Even'
        else:
            result = 'Odd'
    elif d %4 == 2:
        result = 'Odd'
    else:
        if l %2 == 0:
            result = 'Odd'
        else:
            result = 'Even'
    print(result)
