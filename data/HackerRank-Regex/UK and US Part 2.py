import re
lst = []
for x in range(int(input())):
    lst.append(input())
string = '\n'.join([x for x in lst])
for x in range(int(input())):
    words = re.sub('our', 'o[u]?r', input())
    regex = re.compile('\\b'+words+'\\b', re.IGNORECASE)
    words = regex.finditer(string)
    print(len(list(words)))
