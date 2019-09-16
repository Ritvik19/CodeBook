# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    s = input()
    while len(re.findall(r' && ', s)):
        s = re.sub(r' && ', ' and ', s)
    while len(re.findall(r' \|\| ', s)):
        s = re.sub(r' \|\| ', ' or ', s)
    print(s)
