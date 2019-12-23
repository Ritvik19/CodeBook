matches = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8':7, '9': 6}
for t in range(int(input())):
    a, b = map(int, input().split())
    c = str(a+b)
    res = 0
    for _ in c:
        res += matches[_]
    print(res)