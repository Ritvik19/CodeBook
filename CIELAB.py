a, b = map(int, input().split())
c = a - b
if c%10 in [0, 1]:
    print(c+1)
else:
    print(c-1)
