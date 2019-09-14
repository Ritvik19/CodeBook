# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
CAPS = re.compile(r"[A-Z]")
DIGITS = re.compile(r"[0-9]")
ALPHA = re.compile(r"[0-9a-zA-Z]{10}")
for i in range(int(input())):
    UID = input()
    flag1 = bool(len(CAPS.findall(UID)) >= 2)
    flag2 = bool(len(DIGITS.findall(UID)) >= 3)
    flag3 = bool(ALPHA.fullmatch(UID))
    flag4 = bool(len(set(list(UID))) == len(list(UID)))
    if all([flag1, flag2, flag3, flag4]):
        print("Valid")
    else:
        print("Invalid")
