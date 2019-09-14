for i in range(int(input())):
    p,s = map(int,input().split())
    b = (p/12)-((p**(2) - 24 * s) ** (1/2))/12
    l = p/4-2*b
    print(round(float(l*(b**2)),2))
