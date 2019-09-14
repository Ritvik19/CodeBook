import re
PHONE_REGEX = re.compile(r"[789]\d{9}")
for i in range(int(input())):
    _ = input()
    if len(_) == 10:
        if PHONE_REGEX.match(_):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
