import re
p = r"([qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBN])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBN])"
m = re.finditer(p, input())
result = list(map(lambda x: x.group(2), m))
if result:
    for s in result:
        print(s)
else: print(-1)
