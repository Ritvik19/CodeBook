for a in range(1, 1001 + 1):
    for b in range(a + 1, 1001 + 1):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(a * b * c) # 31875000
            break
