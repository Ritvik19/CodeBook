from math import gcd
for i in range(int(input())):
    inp = input().split(" ")
    q = int(inp[0])
    p = int(inp[1])
    print(str(gcd(q, p))+" "+str(q*p//gcd(q, p)))
