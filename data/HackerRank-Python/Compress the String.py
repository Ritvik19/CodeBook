string = input()
symbol = string[0]
compressed = []
count = 0
for s in string:
    if s == symbol:
        count += 1
    else:
        compressed.append((count, int(symbol)))
        count = 1
        symbol = s
compressed.append((count, int(symbol)))        
print(*compressed)
