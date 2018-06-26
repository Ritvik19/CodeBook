for i in range(int(input())):
    D = input()
    n0 = n1 = 0
    for d in D:
        if d == '1':
            n1 += 1
        else:
            n0 += 1
    if n1 == 1 or n0 == 1:
        print("Yes")
    else:
        print("No")
