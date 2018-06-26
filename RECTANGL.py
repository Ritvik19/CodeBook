def RECTANGL(a, b, c, d):
    xor = int(a)^int(b)^int(c)^int(d)
    if xor :
        return "NO"
    else:
        return "YES"

t = int(input())

for i in range(t):
    a, b, c, d = input().split(" ")
    print(RECTANGL(a, b, c, d))
