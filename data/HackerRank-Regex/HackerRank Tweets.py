import re
HACKERRANK = re.compile('hackerrank', re.IGNORECASE)

count = 0
for n in range(int(input())):
    count += 1 if HACKERRANK.search(input()) else 0
print(count)
