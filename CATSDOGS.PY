for i in range(int(input())):
    c, d, n = input().split()
    c, d, n = int(c), int(d), int(n)
    if n%4 != 0 or n>(c+d)*4 or n<(d)*4:
        print("no")
    elif c + d - n//4 <= 2*d:
        print("yes")
    else:
        print("no")
