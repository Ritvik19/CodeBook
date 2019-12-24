import re
PAN = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
for n in range(int(input())):
    print('YES') if PAN.match(input()) else print('NO')
