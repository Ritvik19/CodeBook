digits = lambda x: len(str(x))
x = 1
y = 1
count = 2
while digits(x) < 1000:
    x, y = y, x + y
    count += 1
print(count-1) # 4782
