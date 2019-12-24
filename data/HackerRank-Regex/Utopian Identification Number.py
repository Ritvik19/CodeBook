import re

for n in range(int(input())):
    print('VALID') if re.match(
        r"^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$", input()) else print('INVALID')
