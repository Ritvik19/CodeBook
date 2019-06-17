a, b = map(int, input().split())
count = 0
for x in range(1, a+1):
    p = x+1
    while (p*p)-(x*x) <= b:
        count += 1
        p += 1
print(count)
