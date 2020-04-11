for t in range(int(input())):
    a, b, n = map(int, input().split())
    if a == b:
        print(0)
    else:
        if a >= 0 and b >= 0:
            if a > b:
                print(1)
            else:
                print(2)
        elif a < 0 and b < 0:
            if n %2 == 0:
                if abs(a) > abs(b):
                    print(1)
                else:
                    print(2)
            else:
                if abs(a) < abs(b):
                    print(1)
                else:
                    print(2)
        else:
            if n %2 == 0:
                if abs(a) == abs(b):
                    print(0)
                elif abs(a) > abs(b):
                    print(1)
                else:
                    print(2)
            else:
                if a >= 0:
                    print(1)
                else:
                    print(2)
