import re
FLOAT_REGEX = re.compile(r"[+-]?\d*\.\d+")
for i in range(int(input())):
    print(bool(FLOAT_REGEX.fullmatch(input())))
