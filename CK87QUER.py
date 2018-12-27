for t in range(int(input())):
    y = int(input())
    count = 0
    for a in range(int(y**(1/2))):
        for b in range(1, 701):
            if (a*a) + b == y:
                count += 1
    print(count)
