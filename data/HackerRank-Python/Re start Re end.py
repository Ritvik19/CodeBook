import re
s = input().strip()
k = input().strip()
p = r'(?=%s)' % k
m = re.finditer(p, s)
for match in m:
    print((match.start(), match.start()+len(k)-1))
if not re.search(p, s):
    print((-1, -1))
