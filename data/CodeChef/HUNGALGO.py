import numpy as np
for t in range(int(input())):
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(int, input().split())))
    m = np.array(m)
    f = 'YES'
    for i in range(n):
        if 0 not in m[i,:]:
            f = 'NO'
            break
    for i in range(n):
        if 0 not in m[:, i]:
            f = 'NO'
            break
    print(f)
