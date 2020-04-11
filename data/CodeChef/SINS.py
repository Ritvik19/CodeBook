from math import gcd
for t in range(int(input())):
    x, y = map(int, input().split())
    print(2*gcd(x, y))
