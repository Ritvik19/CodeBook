import re
import sys
p = sys.stdin.read()
pat = '[\w\.]+@(?:\w+\.)+\w+'
emaillist = re.findall(pat, p)
print(';'.join(sorted(list(set(emaillist)))))
