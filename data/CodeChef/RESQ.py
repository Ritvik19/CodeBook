from math import floor
for t in range(int(input())):
    n = int(input())
    x = floor(n**0.5)
    while n%x != 0:
        x -= 1
    print(abs(x-(n//x)))
