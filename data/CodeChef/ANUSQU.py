from math import ceil
n = int(input())
if ceil(n**(0.5)) == n**(0.5):
    print(int(4*n**(0.5)))
else:
    x = ceil(n**(0.5))
    if n > x**2 - x:
        print(4*x)
    else:
        print(4*x-2)
