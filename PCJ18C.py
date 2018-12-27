for t in range(int(input())):
    n, a, k= map(int, input().split())
    print(int(((k-1)/(n-1))*((360*(n-2)/n)-2*a)) + a, 1)
