def variants(n, m, c):
    res = [(i, c // i) for i in range(1, c + 1) if c % i == 0 and i <= n and c // i <= m]
    return len(res)

for t in range(int(input())):
    n, m ,c = input().split()
    n, m, c = int(n), int(m), int(c)
    print(variants(n, m, c))
