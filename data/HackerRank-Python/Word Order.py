from collections import OrderedDict
d =OrderedDict()
for _ in range(int(input())):
    k = input()
    if k not in d.keys():
        d[k] = 0
    d[k] += 1
print(len(d.keys()))
print(*d.values())
