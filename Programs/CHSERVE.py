for t in range(int(input())):
    p1, p2, k = map(int, input().split())
    x = (p1+p2)//k
    out = 'CHEF' if x%2 == 0 else 'COOK'
    print(out)
