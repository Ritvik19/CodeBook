from collections import Counter
for t in range(int(input())):
    n = int(input())
    s = input()
    print('YES') if Counter(s)[s[-1]] >= 2 else print('NO')
        