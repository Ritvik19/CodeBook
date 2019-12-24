import re

pat = re.compile(r'<a href="(.*?)".*?>([\w ,./]*)(?=</)')

for n in range(int(input())):
    res = pat.findall(input())
    for link, title in res:
        print(f"{link},{title.strip()}")
