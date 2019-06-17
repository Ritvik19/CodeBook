def gcd(a, b):
    while b!= 0:
        a, b = b, a%b
    return a

for t in range(int(input())):
    a, b = map(int, input().split())
    print(gcd(a, b))
