from collections import  OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    *a, b = input().split()
    a = ' '.join(a)
    if a in d.keys():
        d[a] += int(b)
    else:
        d[a] = int(b)
for k,v in d.items():
    print(k,v)
