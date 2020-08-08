from collections import Counter

for t in range(int(input())):
    N = int(input())
    S = input()
    res = Counter(S)
    flag = 'YES'
    for i in res.values():
        if i % 2 != 0:
            flag = 'NO'
            
    print(flag)