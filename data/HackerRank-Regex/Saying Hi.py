import re

hi = re.compile(r"^[hH][iI]\s[^dD]")
for n in range(int(input())):
    s = input()
    if len(hi.findall(s)):
        print(s)
