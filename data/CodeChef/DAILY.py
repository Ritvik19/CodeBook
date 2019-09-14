from math import factorial

def c(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

x, n = map(int, input().split())
ways = 0
for i in range(n):
    car = input()
    start = 0
    end = 52
    for j in range(9):
        compartment = car[start:start+4]+car[end:end+2]
        vacant = compartment.count('0')
        if vacant >= x:
            ways += c(vacant, x)
        start += 4
        end -= 2
print(ways)
