import re

for _ in range(int(input())):
    s = input()
    if re.search(r'^hackerrank(.*hackerrank)?$', s):
        print(0)
    elif re.search(r'^hackerrank', s):
        print(1)
    elif re.search(r'hackerrank$', s):
        print(2)
    else:
        print(-1)
