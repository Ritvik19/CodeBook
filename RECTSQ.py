from math import gcd
for i in range(int(input())):
    inp = input().split(" ")
    n = int(inp[0])
    m = int(inp[1])
    print(n*m//(gcd(n, m)**2))
