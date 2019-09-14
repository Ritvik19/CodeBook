import re
REGEX = re.compile(r'([0-9a-zA-Z])\1')
m = REGEX.search(input())
if m != None:
    print(m.group(0)[0])
else:
    print('-1')
