for t in range(int(input())):
    a, b, c = map(int, input().split())
    print(((c-b)//a)*a+b)
    