from math import gcd

for t in range(int(input())):
    x, y = map(int, input().split())
    print('YES') if gcd(x, y) == 1 else print('NO')