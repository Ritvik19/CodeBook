import re

st = '\n'.join(['*'+input().strip().replace('_', '') +
                '*' for _ in range(int(input()))])
for _ in range(int(input())):
    wd = input().strip()
    reg = r'(?<=[\W])' + wd + '(?=[\W])'
    m = re.findall(reg, st)
    print(len(m))
