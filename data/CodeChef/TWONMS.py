for i in range(int(input())):
    a, b, n = input().split()
    a, b, n = int(a), int(b), int(n)
    if n%2 == 0:
        print(max(a,b)//min(a, b))
    else:
        print(max(2*a,b)//min(2*a, b))
