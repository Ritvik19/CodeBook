import re
text = '\n'.join(input() for _ in range(int(input())))
for i in range(int(input())):
    word = input()
    print(len(re.findall(word[:len(word)-2] + '[sz]e', text)))
