count = 0
for n in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    a = (x2-x1)**2 + (y2-y1)**2
    b = (x3-x2)**2 + (y3-y2)**2
    c = (x1-x3)**2 + (y1-y3)**2
    if a + b == c or b + c == a or c + a == b:
        count += 1
print(count)
