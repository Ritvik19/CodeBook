import re

text = "\n".join(input() for n in range(int(input())))
for q in range(int(input())):
    print(len(re.findall(r'\w%s\w' % input().strip(), text)))
