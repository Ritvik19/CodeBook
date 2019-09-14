import re
n = int(input())
p = r'^(.+) <([a-z][\w\.\-]*)@([a-z]+)\.([a-z]{1,3})>$'
for _ in range(n):
    m = re.match(p, input().strip(), flags=re.I)
    if m:
        print(m.group())
