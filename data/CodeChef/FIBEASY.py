for t in range(int(input())):
    n = int(input())
    m = 0
    p = n
    while (n != 1):
        m += 1
        n = n // 2
    temp = m % 4
    if temp == 1:
        if p == 2 or p == 3:
            print(1)
        else:
            print(9)
    else:
        print(temp)