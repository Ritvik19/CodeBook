import re

ALIEN_NAME = re.compile(r"^[_\.]\d+[a-zA-Z]*(_)?$")

for n in range(int(input())):
    print('VALID') if ALIEN_NAME.match(input()) else print('INVALID')
